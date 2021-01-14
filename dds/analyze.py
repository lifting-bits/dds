#!/usr/bin/env python3
# Copyright 2020, Trail of Bits. All rights reserved.

import argparse
import os
import subprocess
import sys
from typing import Final, List, Optional, Sequence, Union

try:
    from shlex import quote
except:
    from pipes import quote

# TODO(pag): I don't understand Python packaging, but this makes it work under
#            PyCharm's venv, and a `setup.py` install, and when executed within
#            an IDA Pro subprocess.
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from dds.datalog import \
    Database, \
    DatabaseFunctors, \
    DatabaseLog

from dds.arch import \
    arch_from_string, \
    ControlFlowBehavior, \
    ControlFlowEdgeKind, \
    decoder_from_string, \
    Instruction, \
    InstructionDecoder, \
    InstructionOperandVisitor

from dds.binary import \
    binary_parser_from_string, \
    BinaryParser, \
    BinaryMetadataVisitor


def debug(message, *args):
    print(message.format(*args), file=sys.stderr)


def _argv() -> Sequence[str]:
    try:
        import idc
        return idc.ARGV
    except:
        return sys.argv


def _exit(code: int):
    try:
        import idc
        idc.process_config_line("ABANDON_DATABASE=YES")
        idc.qexit(code)
    except:
        sys.exit(code)


class BinaryMetadataImporter(BinaryMetadataVisitor, InstructionOperandVisitor):
    """Imports metadata about a binary into a Datalog database."""

    def __init__(self, db: Database, decoder: InstructionDecoder):
        self._db: Final[Database] = db
        self._decoder: Final[InstructionDecoder] = decoder

    def visit_entrypoint_function(self, ea: int):
        """Visit the entrypoint of the binary. This is something like
        `_start` or `_init` in ELF binaries."""
        self._db.entrypoint_1([ea])

    def visit_imported_function(self, ea:int, name: Optional[bytes]):
        """Visit functions imported to this binary. In practice, 
        these are externals."""
        self._db.imported_function_2([(ea, name)])
        self._db.external_symbol_2([(ea, name)])
    
    def visit_imported_variable(self, ea:int, name: Optional[bytes]):
        """Visit variables imported to this binary."""
        #self._db.imported_variable_2([(ea, name)])
    
    def visit_imported_symbol(self, ea:int, name: Optional[bytes]):
        """Visit unknown imported symbols. There are no guarantees
        that this is either code or data."""
        self._db.imported_symbol_2([(ea, name)])

    def visit_exported_function(self, ea:int, name: Optional[bytes]):
        """Visit functions exported by this binary."""
        self._db.exported_function_2([(ea, name)])
    
    def visit_exported_variable(self, ea:int, name: Optional[bytes]):
        """Visit variables exported by this binary."""
        #self._db.exported_variable_2([(ea, name)])
    
    def visit_exported_symbol(self, ea:int, name: Optional[bytes]):
        """Visit unknown exported symbols. There are no guarantees
        that this is either code or data."""
        self._db.exported_symbol_2([(ea, name)])

    def visit_local_function(self, ea:int, name: Optional[bytes]):
        """Visit functions local to this binary."""
        self._db.local_function_2([(ea, name)])
    
    def visit_local_variable(self, ea:int, name: Optional[bytes]):
        """Visit variables local to this binary."""
        #self._db.local_variable_2([(ea, name)])
    
    def visit_local_symbol(self, ea:int, name: Optional[bytes]):
        """Visit unknown local symbols. There are no guarantees
        that this is either code or data."""
        self._db.local_symbol_2([(ea, name)])        

    def visit_relocation(self, from_ea: int, to_ea: int, size: int):
        """Visit a relocation entry, applied to `size` bytes at `from_ea`,
        and pointing to `to_ea`."""
        self._db.relocation_2([(from_ea, to_ea)])

    def visit_section(self, begin_ea: int, end_ea: int, name: bytes):
        """Visit a named section `[begin_ea, end_ea)`."""
        self._db.section_3([(name, begin_ea, end_ea)])

    def visit_address_operand(self, inst: Instruction, op_index: int,
                              addr: int):
        """Add in a cross-reference between in instruction and one of its
        memory operands, which references an absolute address."""
        self._db.address_operand_2([(inst.ea, addr)])

    def visit_memory(self, ea: int, data: Union[bytes, bytearray],
                     is_writable: bool, is_executable: bool):
        """Visit a range of mapped memory in the range `[ea, ea + len(data))`.
        The memory is readable, and is executable is `is_executable == True`
        and writeable if `is_writeable == True`."""
        if not is_executable:
            return

        insns = []
        transfers = []

        for i in self._decoder.decode_instructions(ea, data):
            debug("  Adding instruction {:x}: {}\t\t{}".format(
                i.ea, " ".join("{:02x}".format(b) for b in i.data),
                i.assembly))

            # Add the instruction to our database.
            insns.append((i.ea, i.type, i.data))

            # If this instruction has a direct control-flow target then add it
            # in.
            if (i.type & ControlFlowBehavior.HAS_DIRECT_TARGET) == \
                    ControlFlowBehavior.HAS_DIRECT_TARGET:
                target_ea = i.target_ea
                assert target_ea is not None
                transfers.append((i.ea, target_ea, i.target_type))
                debug("    -> {:x} {}", target_ea, i.target_type)

            # If this instruction has a fall-through control-flow target
            # then add it in.
            if (i.type & ControlFlowBehavior.HAS_FALL_THROUGH) == \
                    ControlFlowBehavior.HAS_FALL_THROUGH:
                fall_through_ea = i.fall_through_ea
                assert fall_through_ea is not None
                transfers.append((i.ea, fall_through_ea, i.fall_through_type))
                debug("    -> {:x} {}", fall_through_ea, i.fall_through_type)

            # Otherwise it's a "pseudo edge", which is useful for linear
            # disassembly.
            else:
                transfers.append((i.ea, i.next_ea,
                                  ControlFlowEdgeKind.PSEUDO_FALL_THROUGH))
                debug("    -> {:x} {}", i.next_ea,
                      ControlFlowEdgeKind.PSEUDO_FALL_THROUGH)

            i.visit_operands(self)

        self._db.instruction_3(insns)
        self._db.raw_transfer_3(transfers)


def parse_binary(args) -> Optional[BinaryParser]:
    """Parse the binary at `path` with the binary parser named by
    `parser_name`."""
    parser = binary_parser_from_string(args.binary_parser)
    if not parser:
        raise Exception("Unhandled binary parser type '{}'".format(
            args.binary_parser))

    binary = parser(args.arch, args.os, args.binary)
    if not binary:
        raise Exception("Invalid or unrecognized file format")

    return binary


def run_under_ida(parser, args) -> int:
    """Re-run this program under the control of IDA Pro. This will give us
    access to IDA Pro's APIs."""

    ida_path = os.path.dirname(args.ida_path)

    env = {}
    env["IDALOG"] = os.devnull
    env["TVHEADLESS"] = "1"
    env["HOME"] = os.path.expanduser('~')
    env["IDA_PATH"] = ida_path

    # path: List[str] = [ida_path]
    # if "PYTHONPATH" in os.environ:
    #     path.extend(os.environ["PYTHONPATH"].split(os.pathsep))
    # path.extend(sys.path)
    # #
    # env["PYTHONPATH"] = os.pathsep.join(path)

    if "SystemRoot" in os.environ:
        env["SystemRoot"] = os.environ["SystemRoot"]

    script_cmd = []
    script_cmd.append(os.path.abspath(__file__))
    script_cmd.append("--binary")
    script_cmd.append(os.path.abspath(args.binary))
    script_cmd.append("--binary_parser")
    script_cmd.append(args.binary_parser)
    script_cmd.append("--instruction_decoder")
    script_cmd.append(args.instruction_decoder)
    script_cmd.append("--arch")
    script_cmd.append(args.arch)
    script_cmd.append("--os")
    script_cmd.append(args.os)

    cmd: List[str] = []
    cmd.append(quote(args.ida_path))  # Path to IDA.
    cmd.append("-B")  # Batch mode.
    cmd.append("-S\"{}\"".format(" ".join(script_cmd)))
    cmd.append(quote(os.path.abspath(args.binary)))

    try:
        print(" ".join(cmd))
        print()
        with open(os.devnull, "w") as devnull:
            return subprocess.check_call(
                " ".join(cmd),
                env=env,
                stdin=None,
                stdout=devnull,  # Necessary.
                stderr=sys.stderr,  # For enabling `--log_file /dev/stderr`.
                shell=True)  # Necessary.

    except Exception as e:
        parser.error("Error executing under the control of IDA Pro: {}".format(e))
        return 1


def main(argv: Optional[Sequence[str]] = None):
    """Disassemble a binary."""
    if argv is None:
        argv = _argv()

    parser = argparse.ArgumentParser(
        prog=argv[0], description="Dr. Disassembler's binary analyzer")
    parser.add_argument("--binary", type=str, required=True,
                        help="Path to the binary to analyze.")

    parser.add_argument(
        "--binary_parser", type=str, default="lief",
        help="Which binary parser to use.",
        choices=("lief", "binja", "ida",))

    parser.add_argument(
        "--instruction_decoder", type=str, default="capstone",
        help="Instruction instruction used by the binary",
        choices=("capstone", "binja", "ida", ))

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

    if args.ida_path:
        return run_under_ida(parser, args)

    binary: Optional[BinaryParser] = None
    try:
        binary = parse_binary(args)
    except Exception as e:
        parser.error("Error parsing file '{}': {}".format(args.binary, str(e)))
        return 1

    functors = DatabaseFunctors()
    log = DatabaseLog()
    db = Database(log, functors)

    arch = arch_from_string(args.arch)
    decoder = decoder_from_string(args.instruction_decoder, arch)
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
    _exit(main(_argv()))
