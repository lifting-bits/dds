#!/usr/bin/env python3
# Copyright 2020, Trail of Bits. All rights reserved.

import argparse
import os
import subprocess
import sys
from typing import Final, Iterable, Optional, Union

try:
  from shlex import quote
except:
  from pipes import quote

from capstone import *
import capstone.x86

from datalog import DatabaseFunctors, DatabaseLog, Database
from util import *
from defs import *


from binary import BinaryParser, BinaryMetadataVisitor, LIEFBinaryMetadata


def debug(message, *args):
    print(message.format(*args), file=sys.stderr)


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


Instruction = capstone.CsInsn

class InstructionDecoder:
    CAPSTONE_ARCH_MODE = {
        "x86": capstone.CS_MODE_32,
        "x86_avx": capstone.CS_MODE_32,
        "x86_avx512": capstone.CS_MODE_32,
        "amd64": capstone.CS_MODE_64,
        "amd64_avx": capstone.CS_MODE_64,
        "amd64_avx512": capstone.CS_MODE_64,
        "aarch32": capstone.CS_MODE_32,
        "aarch64": capstone.CS_MODE_64,
        "sparc32": capstone.CS_MODE_32,
        "sparc64": capstone.CS_MODE_64
    }

    CAPSTONE_ARCH_NAME = {
        "x86": capstone.CS_ARCH_X86,
        "x86_avx": capstone.CS_ARCH_X86,
        "x86_avx512": capstone.CS_ARCH_X86,
        "amd64": capstone.CS_ARCH_X86,
        "amd64_avx": capstone.CS_ARCH_X86,
        "amd64_avx512": capstone.CS_ARCH_X86,
        "aarch32": capstone.CS_ARCH_ARM,
        "aarch64": capstone.CS_ARCH_ARM64,
        "sparc32": capstone.CS_ARCH_SPARC,
        "sparc64": capstone.CS_ARCH_SPARC,
    }

    MIN_INST_SIZE = {
        "x86": 1,
        "x86_avx": 1,
        "x86_avx512": 1,
        "amd64": 1,
        "amd64_avx": 1,
        "amd64_avx512": 1,
        "aarch32": 4,
        "aarch64": 4,
        "sparc32": 4,
        "sparc64": 4
    }

    MAX_INST_SIZE = {
        "x86": 15,
        "x86_avx": 15,
        "x86_avx512": 15,
        "amd64": 15,
        "amd64_avx": 15,
        "amd64_avx512": 15,
        "aarch32": 4,
        "aarch64": 4,
        "sparc32": 4,
        "sparc64": 4
    }

    def __init__(self, arch_name: str):
        cs_mode = self.CAPSTONE_ARCH_MODE[arch_name]
        cs_arch_name = self.CAPSTONE_ARCH_NAME[arch_name]
        self.min_instruction_size: Final[int] = self.MIN_INST_SIZE[arch_name]
        self.max_instruction_size: Final[int] = self.MAX_INST_SIZE[arch_name]
        self._cs = capstone.Cs(cs_arch_name, cs_mode)
        self._cs.detail = True
        self._cs.syntax = CS_OPT_SYNTAX_DEFAULT
        self._cs.skipdata = True

    def decode_instruction(self, addr: int, data: Union[bytes, bytearray]) \
            -> Optional[Instruction]:
        """Decode one instruction in `data`, interpreting it to start at address
        `addr`. Returns the decoded instruction, or `None`."""
        for i in self._cs.disasm(data, addr):
            return i.mnemonic != ".byte" and i or None
        return None

    def decode_instructions(self, addr, data: Union[bytes, bytearray]) \
            -> Iterable[Instruction]:
        """Decode all instructions in `data`, interpreting the first
        instruction to begin at `addr`. Returns an iterable of the
        successfully decoded instructions."""
        i = 0
        data_len: Final[int] = len(data)
        while i < data_len:
            inst_data = bytearray()
            j = self.min_instruction_size
            while (i + j) < data_len and j < self.max_instruction_size:
                inst_data.append(data[i + j])
                j += 1
            if inst_data:
                inst = self.decode_instruction(addr + i, inst_data)
                if inst:
                    yield inst
            i += self.min_instruction_size


class BinaryMetadataImporter(BinaryMetadataVisitor):
    """Imports metadata about a binary into a Datalog database."""

    def __init__(self, db: Database, decoder: InstructionDecoder):
        self._db = db
        self._decoder = decoder

    def visit_relocation(self, from_ea: int, to_ea: int, size: int):
        """Visit a relocation entry, applied to `size` bytes at `from_ea`,
        and pointing to `to_ea`."""
        self._db.relocation_2([(from_ea, to_ea)])

    def visit_entrypoint_function(self, ea: int):
        """Visit the entrypoint of the binary. This is something like
        `_start` or `_init` in ELF binaries."""
        self._db.entrypoint_1([ea])

    def visit_constructor_function(self, ea: int):
        """Visit a constructor function that is defined at `ea`."""
        self._db.constructor_function_1([ea])

    def visit_destructor_function(self, ea: int):
        """Visit a destructor function that is defined at `ea`."""
        self._db.destructor_function_1([ea])

    def visit_imported_function(self, ea: int, name: bytes):
        """Visit a function that is imported by this binary from other binaries.
        In practice, these functions are externals."""
        self._db.external_symbol_2([(ea, name)])
        self._db.imported_function_2([(ea, name)])

    def visit_exported_function(self, ea: int, name: bytes):
        """Visit a function that is exported by this binary to other binaries.
        For example, if this is a shared library, then this would be called
        for each symbol that the library exports to users of the library."""
        self._db.exported_function_2([(ea, name)])

    def visit_local_function(self, ea: int, name: Optional[bytes]):
        """Visit a named function that is neither exported nor imported."""
        self._db.local_function_2([(ea, name)])

    def visit_imported_symbol(self, ea: int, name: bytes):
        """Visit a symbol that is imported by this binary from other binaries.
        In practice, these symbols are externals. There are no guarantees that
        this is code or data."""
        self._db.external_symbol_2([(ea, name)])

    def visit_exported_symbol(self, ea: int, name: bytes):
        """Visit a symbol that is exported by this binary to other binaries.
        For example, if this is a shared library, then this would be called
        for each symbol that the library exports to users of the library.
        There are no guarantees that this is code or data."""
        self._db.exported_symbol_2([(ea, name)])

    def visit_local_symbol(self, ea: int, name: Optional[bytes]):
        """Visit a named symbol that is neither exported nor imported. A local
        symbol is not necessarily the head of a logical entity. For example,
        it could point inside the middle of a logical entity."""
        self._db.imported_symbol_2([(ea, name)])

    def visit_section(self, begin_ea: int, end_ea: int, name: bytes):
        """Visit a named section `[begin_ea, end_ea)`."""
        self._db.section_3([(name, begin_ea, end_ea)])

    def visit_memory(self, ea: int, data: bytes, is_writable: bool,
                     is_executable: bool):
        """Visit a range of mapped memory in the range `[ea, ea + len(data))`.
        The memory is readable, and is executable is `is_executable == True`
        and writeable if `is_writeable == True`."""
        if not is_executable:
            return

        insts = []
        transfers = []
        address_operands = []

        for i in self._decoder.decode_instructions(ea, data):

            i_addr = i.address
            i_next = i.address + i.size
            i_type = get_instruction_type(i.mnemonic, i.op_str)
            i_bytes = i.bytes.hex()

            debug("  Adding instruction {:x}: {} {}".format(i_addr, i.mnemonic,
                                                            i.op_str))

            # Add the instruction to our database.
            insts.append((i_addr, i_type, i_bytes))

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

            # We omit edges from returns as these denote function endpoints.
            elif i_type == INSN_RETURN:
                pass

            # Report if no transfer instruction is detected.
            else:
                debug("    No transfer???")

            # Extract address-like operands found in any instruction.
            for o in i.operands:

                # Indirect transfers
                if o.type == capstone.x86.X86_OP_MEM:
                    m = o.mem
                    m_addr = 0

                    # PC-relative, e.g. `jmp [RIP + 0xdisp]`.
                    if m.base == capstone.x86.X86_REG_RIP and not m.segment and \
                            not m.index:
                        m_addr = i.address + m.disp

                    # Absolute addr, e.g. `jmp [0xaddr]`.
                    elif not m.base and not m.segment and not m.index and m.disp:
                        m_addr = m.disp

                    else:
                        continue

                    if m_addr:
                        address_operands.append((i_addr, m_addr))

        self._db.instruction_3(insts)
        self._db.address_operand_2(address_operands)
        self._db.raw_transfer_3(transfers)


def parse_binary(args) -> Optional[BinaryParser]:
    """Parse the binary at `path` with the binary parser named by
    `parser_name`."""
    if "lief" == args.binary_parser:
        binary = LIEFBinaryMetadata(args.arch, args.os, args.binary)
    else:
        raise Exception("Unhandled binary parser type '{}'".format(
            parser_name))

    if not binary:
        raise Exception("Invalid or unrecognized file format")

    return binary


def run_under_ida(parser, args) -> int:
    """Re-run this program under the control of IDA Pro. This will give us
    access to IDA Pro's APIs."""

    env = {}
    env["IDALOG"] = os.devnull
    env["TVHEADLESS"] = "1"
    env["HOME"] = os.path.expanduser('~')
    env["IDA_PATH"] = os.path.dirname(args.ida_path)
    #env["PYTHONPATH"] = os.path.dirname(ida_dir)
    if "SystemRoot" in os.environ:
        env["SystemRoot"] = os.environ["SystemRoot"]

    script_cmd = []
    script_cmd.append(os.path.abspath(__file__))
    script_cmd.append("--binary")
    script_cmd.append(args.binary)
    script_cmd.append("--binary_parser")
    script_cmd.append(args.binary_parser)
    script_cmd.append("--instruction_decoder")
    script_cmd.append(args.instruction_decoder)
    script_cmd.append("--arch")
    script_cmd.append(args.arch)
    script_cmd.append("--os")
    script_cmd.append(args.os)

    cmd = []
    cmd.append(quote(args.ida_path))  # Path to IDA.
    cmd.append("-B")  # Batch mode.
    cmd.append("-S\"{}\"".format(" ".join(script_cmd)))
    cmd.append(quote(args.binary))

    try:
        with open(os.devnull, "w") as devnull:
            return subprocess.check_call(
                " ".join(cmd),
                env=env,
                stdin=None,
                stdout=devnull,  # Necessary.
                stderr=sys.stderr,  # For enabling `--log_file /dev/stderr`.
                shell=True,  # Necessary.
                cwd=os.path.dirname(__file__))

    except:
        parser.error("Error executing under the control of IDA Pro")
        return 1


def main(argv):
    """Disassemble a binary."""

    parser = argparse.ArgumentParser(
        prog=argv[0], description="Dr. Disassembler's binary analyzer")
    parser.add_argument("--binary", type=str, required=True,
                        help="Path to the binary to analyze.")

    parser.add_argument(
        "--binary_parser", type=str, default="lief",
        help="Which binary parser to use.",
        choices=("lief",))

    parser.add_argument(
        "--instruction_decoder", type=str, default="capstone",
        help="Instruction decoder used by the binary",
        choices=("capstone",))

    parser.add_argument(
        "--ida_path", type=str, default="",
        help="Path to IDA Pro 7's `idat` or `idat64` binary.")

    parser.add_argument(
        "--arch", type=str, default="amd64",
        help="Architecture of the instructions of the binary.",
        choices=("x86", "x86_avx", "x86_avx512",
                 "amd64", "amd64_avx", "amd64_avx512",
                 "aarch32", "aarch64",
                 "sparc32", "sparc64"))

    parser.add_argument(
        "--os", type=str, default="linux",
        help="Operating system on which this binary is expected to execute.",
        choices=("linux", "macos", "windows", "solaris"))

    args = parser.parse_args(argv[1:])

    binary: Optional[BinaryParser] = None
    try:
        binary = parse_binary(args)
    except Exception as e:
        parser.error("Error parsing file '{}': {}".format(args.binary, str(e)))
        return 1

    if args.ida_path:
        return run_under_ida(parser, args)

    functors = DatabaseFunctors()
    log = DatabaseLog()
    db = Database(log, functors)

    decoder = InstructionDecoder(args.arch)
    visitor = BinaryMetadataImporter(db, decoder)
    binary.visit_metadata(visitor)

    for f in sorted(db.function_f()):
        print("Function {:x}".format(f))
        for i in sorted(db.function_instruction_bf(f)):
            print("  {:x}".format(i))
        print()

    return 0


# Main function.
if __name__ == "__main__":
    sys.exit(main(sys.argv))

