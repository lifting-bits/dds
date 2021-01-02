#!/usr/bin/env python3
# Copyright 2020, Trail of Bits. All rights reserved.

from capstone import *
import capstone.x86
import lief, os, sys

from datalog import DatabaseFunctors, DatabaseLog, Database
from util import *
from defs import *


def debug(message, *args):
    print(message.format(*args))


# Add an `.extern` section (4-byte aligned) with 
# enough slots to accommodate each PLT relocations.
def lief_relocate_externs(db, parsed, relocs):

    externs = []
    relocations = []

    # Start address of our fake `.extern` section.
    s_addr = max((x.virtual_address + x.size) for x in parsed.sections)
    s_addr = ((s_addr + 3) // 4) * 4  # Align to a four-byte boundary.

    # Generate relocation and external addresses.
    s_size = 0
    for reloc in relocs:

        if not reloc.symbol or not reloc.symbol.name:
            continue

        e_addr = s_addr + s_size
        s_size += 4  # TODO: Fix me

        debug("Relocation from {:x} to external {} at {:x}", reloc.address, reloc.symbol.name, e_addr)
        relocations.append((reloc.address, e_addr))
        externs.append((e_addr, bytes(reloc.symbol.name, "utf-8")))

    debug("Faking .extern section [{:x}, {:x})", s_addr, s_addr + s_size)
    db.section_4([(b'.extern', s_addr, s_addr + s_size, SECTION_EXEC)])
    db.external_symbol_2(externs)
    db.relocation_2(relocations)



# For edges with two outgoing edges (including calls
# and jumps), add their corresponding target and 
# fallthrough (or pseudo-fallthrough) edges.
def lief_add_two_edges(instruction, target_type, fallthru_type, transfers):
    i_addr = instruction.address
    i_next = instruction.address + instruction.size
    i_targ = get_transfer_target(instruction)

    if i_targ:
        transfers.append((i_addr, i_targ, target_type))

    transfers.append((i_addr, i_next, fallthru_type))


# Comprehensively decode instructions in `data`, treating the first byte of
# data as beginning at the virtual address `addr`.
def decode_instructions(cs, addr, data, size_range):
    seen = set()
    for offset in size_range:
        if not len(data):
            break
        for i in cs.disasm(data, addr + offset):

            # We've aligned with another decoding, so all remaining instructions will
            # also be in `seen`.
            if i.address in seen:
                break
            if i.mnemonic == ".byte":
                continue  # It's not an instruction.
            yield i
            seen.add(i.address)
        data = bytearray(data[1:])


# Disassemble with lief.
def lief_disassemble(db, target):
    parsed                     = lief.parse(target)
    (b_type, b_arch, b_relocs) = get_target_info(parsed)
    cs                         = get_capstone(b_type, b_arch)

    # Set up necessary relocations.
    lief_relocate_externs(db, parsed, b_relocs)

    sections = []
    insts = []
    transfers = []
    address_operands = []

    # Iterate all sections.
    for s in parsed.sections:
        s_name  = bytes(s.name, "utf-8")
        s_start = s.virtual_address
        s_end   = s.virtual_address + s.size
        if s_start >= s_end:
            continue
        s_bytes = bytearray(s.content)
        s_flags = s.flags_list

        # Parse executable sections.
        if FLAG_ELF_EXEC in s_flags:
            debug("Adding code section {} [{:x}, {:x}) ".format(s.name, s_start, s_end))
            sections.append((s_name, s_start, s_end, SECTION_EXEC))

            # Decode instructions with Capstone.
            #
            # TODO(pag): Eventually replace `range(15)`, which is specific to x86,
            #                         with something generic.
            for i in decode_instructions(cs, s_start, s_bytes, range(15)):
                i_addr  = i.address
                i_next  = i.address + i.size
                i_type  = get_instruction_type(i.mnemonic, i.op_str)
                i_bytes = i.bytes.hex()

                debug("  Adding instruction {:x}: {} {}".format(i_addr, i.mnemonic, i.op_str))

                # Add the instruction to our database.
                insts.append((i_addr, i_type, i_bytes, s_name))

                # Conditional branches: add target and fallthrough edges.
                if i_type == INSN_COND_DIRECT_JUMP:
                    lief_add_two_edges(i, EDGE_COND_TRUE, EDGE_COND_FALSE, transfers)

                # Jumps: add target edge, and post-jump fallthrough.
                elif i_type in (INSN_DIRECT_JUMP, INSN_INDIRECT_JUMP):
                    lief_add_two_edges(i, EDGE_JUMP_TARG, EDGE_JUMP_PSEUDO, transfers)

                # Calls: add target edge, and post-call fallthrough.
                elif i_type in (INSN_DIRECT_CALL, INSN_INDIRECT_CALL):
                    lief_add_two_edges(i, EDGE_CALL_TARG, EDGE_CALL_PSEUDO, transfers)

                # Rest: add fallthrough edges (except if RET or HLT).
                elif i_type in (INSN_NORMAL, INSN_NOP):
                    transfers.append((i_addr, i_next, EDGE_FALLTHRU))

                elif i_type == INSN_RETURN:
                    pass

                else:
                    debug("    No transfer???")

                for o in i.operands:
                    # Indirect transfers
                    if o.type == capstone.x86.X86_OP_MEM:
                        m = o.mem
                        m_addr = 0
                        # PC-relative, e.g. `jmp [RIP + 0xdisp]`.
                        if m.base == capstone.x86.X86_REG_RIP and not m.segment and not m.index:
                            m_addr = i.address + m.disp
                        # Absolute addr, e.g. `jmp [0xaddr]`.
                        elif not m.base and not m.segment and not m.index and m.disp:
                            m_addr = m.disp
                        else:
                            continue

                        if m_addr:
                            address_operands.append((i_addr, m_addr))


        else:
            debug("Adding data section {} [{:x}, {:x}) ".format(s.name, s_start, s_end))
            sections.append((s_name, s_start, s_end, SECTION_DATA))

    # Send all the instructions and transfers to datalog in one batch.
    db.section_4(sections)
    db.instruction_4(insts)
    db.entrypoint_1([(parsed.entrypoint)])
    db.address_operand_2(address_operands)
    db.raw_transfer_3(transfers)

    for f in sorted(db.function_f()):
        print("Function {:x}".format(f))
        for i in sorted(db.function_instruction_bf(f)):
            print("  {:x}".format(i))
        print ('')

    #for i in db.get_external_calls_f():
    #    print (hex(i))

    return


def main(args):
    usage = '''Usage: 
            \tpython3 %s [target_binary] [disassembler]
            \tSupported disassemblers:
            \t  lief
            ''' % sys.argv[0]

    functors = DatabaseFunctors()
    log = DatabaseLog()
    db = Database(log, functors)

    if len(sys.argv) != 3:
        print("ERROR: Missing argument(s)!")
        print(usage)
        exit(0)

    target = sys.argv[1]
    if not os.path.exists(target):
        print("ERROR: Can't find target binary (%s)!" % target)
        print(usage)
        exit(0)

    lief_disassemble(db, target)


# Main function.
if __name__ == "__main__":
    sys.exit(main(sys.argv))

