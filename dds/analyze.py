# Copyright 2021, Trail of Bits. All rights reserved.

import hashlib
import os
import tempfile

from typing import cast, Final, Iterator, Optional, Union

from dds.datalog import \
    Database, \
    DatabaseLog, \
    DatabaseFunctors, \
    DatabaseLogInterface, \
    DatabaseInputMessageProducer

from dds.arch import \
    ArchName, \
    ControlFlowBehavior, \
    ControlFlowEdgeKind, \
    decoder_from_string, \
    Instruction, \
    InstructionDecoder, \
    InstructionOperandVisitor, \
    InvalidInstructionDecoder

from dds.binary import \
    BinaryParser, \
    BinaryMetadataVisitor

from dds.heuristic import ControlFlowRecoveryHeuristic


def debug(message, *args):
    #print(message.format(*args), file=sys.stderr)
    pass


class BinaryAnalysisError(Exception):
    pass


class BinaryMetadataImporter(BinaryMetadataVisitor, InstructionOperandVisitor,
                             DatabaseInputMessageProducer):
    """Imports metadata about a binary into a Datalog database."""

    def __init__(self, decoder: InstructionDecoder):
        super(BinaryMetadataImporter, self).__init__()
        self._decoder: Final[InstructionDecoder] = decoder

    def visit_entrypoint_function(self, ea: int):
        """Visit the entrypoint of the binary. This is something like
        `_start` or `_init` in ELF binaries."""
        self.produce_entrypoint_1(ea)

    def visit_imported_function(self, ea: int, name: Optional[bytes]):
        """Visit functions imported to this binary. In practice,
        these are externals."""
        self.produce_imported_function_2(ea, name)
        self.produce_external_symbol_2(ea, name)

    def visit_imported_variable(self, ea: int, name: Optional[bytes]):
        """Visit variables imported to this binary."""
        # self._db.imported_variable_2([(ea, name)])
        pass

    def visit_imported_symbol(self, ea: int, name: Optional[bytes]):
        """Visit unknown imported symbols. There are no guarantees
        that this is either code or data."""
        self.produce_imported_symbol_2(ea, name)

    def visit_exported_function(self, ea: int, name: Optional[bytes]):
        """Visit functions exported by this binary."""
        self.produce_exported_function_2(ea, name)

    def visit_exported_variable(self, ea: int, name: Optional[bytes]):
        """Visit variables exported by this binary."""
        # self._db.exported_variable_2([(ea, name)])
        pass

    def visit_exported_symbol(self, ea: int, name: Optional[bytes]):
        """Visit unknown exported symbols. There are no guarantees
        that this is either code or data."""
        self.produce_exported_symbol_2(ea, name)

    def visit_local_function(self, ea: int, name: Optional[bytes]):
        """Visit functions local to this binary."""
        self.produce_local_function_2(ea, name)

    def visit_local_variable(self, ea: int, name: Optional[bytes]):
        """Visit variables local to this binary."""
        # self._db.local_variable_2([(ea, name)])
        pass

    def visit_local_symbol(self, ea: int, name: Optional[bytes]):
        """Visit unknown local symbols. There are no guarantees
        that this is either code or data."""
        self.produce_local_symbol_2(ea, name)

    def visit_relocation(self, from_ea: int, to_ea: int, size: int):
        """Visit a relocation entry, applied to `size` bytes at `from_ea`,
        and pointing to `to_ea`."""
        self.produce_relocation_2(from_ea, to_ea)

    def visit_section(self, begin_ea: int, end_ea: int, name: bytes):
        """Visit a named section `[begin_ea, end_ea)`."""
        self.produce_section_3(name, begin_ea, end_ea)

    def visit_address_operand(self, inst: Instruction, op_index: int,
                              addr: int):
        """Add in a cross-reference between in instruction and one of its
        memory operands, which references an absolute address."""
        self.produce_address_operand_2(inst.ea, addr)

    def visit_memory(self, ea: int, data: Union[bytes, bytearray],
                     is_writable: bool, is_executable: bool):
        """Visit a range of mapped memory in the range `[ea, ea + len(data))`.
        The memory is readable, and is executable is `is_executable == True`
        and writeable if `is_writeable == True`."""
        if not is_executable:
            return

        for i in self._decoder.decode_instructions(ea, data):
            debug("  Adding instruction {:x}:\n\ttype: {}\n\tbytes: {}\n\tassembly: {}".format(
                 i.ea, i.type, " ".join("{:02x}".format(b) for b in i.data),
                 i.assembly))

            # Add the instruction to our database.
            self.produce_instruction_3(i.ea, i.type, i.data)

            # If this instruction has a direct control-flow target then add it
            # in.
            if (i.type & ControlFlowBehavior.HAS_DIRECT_TARGET) == \
                    ControlFlowBehavior.HAS_DIRECT_TARGET:
                target_ea = i.target_ea
                assert target_ea is not None
                self.produce_raw_transfer_3(i.ea, target_ea, i.target_type)
                debug("    transfer: {:x} {}", target_ea, i.target_type)

            # If this instruction has a fall-through control-flow target
            # then add it in.
            if (i.type & ControlFlowBehavior.HAS_FALL_THROUGH) == \
                    ControlFlowBehavior.HAS_FALL_THROUGH:
                fall_through_ea = i.fall_through_ea
                assert fall_through_ea is not None
                self.produce_raw_transfer_3(
                    i.ea, fall_through_ea, i.fall_through_type)
                debug("    transfer: {:x} {}", fall_through_ea, i.fall_through_type)

            # Otherwise it's a "pseudo edge", which is useful for linear
            # disassembly.
            else:
                self.produce_raw_transfer_3(
                    i.ea, i.next_ea, ControlFlowEdgeKind.PSEUDO_FALL_THROUGH)
                debug("    transfer: {:x} {}", i.next_ea,
                      ControlFlowEdgeKind.PSEUDO_FALL_THROUGH)

            i.visit_operands(self)


class BinaryObject:
    def __init__(self, db: Database, ea: int):
        self._db: Final = db
        self._ea: Final = ea

    @property
    def ea(self) -> int:
        return self._ea

    def __eq__(self, other) -> bool:
        return self.__class__ is other.__class__ and \
               self._db is other._db and \
               self._ea == other._ea

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, BinaryObject):
            return (id(self._db), self._ea) < (id(other._db), other._ea)
        else:
            return id(self) < id(other)

    def __le__(self, other):
        if isinstance(other, BinaryObject):
            return (id(self._db), self._ea) <= (id(other._db), other._ea)
        else:
            return id(self) <= id(other)


class BinaryExternal(BinaryObject):
    """Represents an external of some kind."""

    def __bool__(self) -> bool:
        """Returns `True` if this external remains valid in the database."""
        return self._db.external_b(self._ea)


class BinaryControlFlowTarget(BinaryObject):
    """Represents the target of a control flow."""

    def __init__(self, db: Database, ea: int, kind: ControlFlowEdgeKind):
        BinaryObject.__init__(self, db, ea)
        self._kind: Final = kind

    @property
    def kind(self) -> ControlFlowEdgeKind:
        return self._kind

    @property
    def instruction(self) -> Optional['BinaryInstruction']:
        """The instruction associated with this control-flow target, if any."""
        for _ in self._db.function_instruction_fb(self._ea):
            return BinaryInstruction(self._db, self._ea)
        return None

    @property
    def external(self) -> Optional[BinaryExternal]:
        """The external associated with this control-flow target, if any."""
        if self._db.external_b(self._ea):
            return BinaryExternal(self._db, self._ea)
        return None


class BinaryInstruction(BinaryObject):
    """Wrapper around an individual instruction in the binary."""

    @property
    def flows(self) -> Iterator[BinaryControlFlowTarget]:
        for ea, kind in self._db.transfer_bff(self._ea):
            yield BinaryControlFlowTarget(self._db, ea, kind)

    @property
    def functions(self) -> Iterator['BinaryFunction']:
        """Generates the set of functions containing this instructions."""
        for func_ea in self._db.function_instruction_fb(self._ea):
            yield BinaryFunction(self._db, func_ea)

    def __bool__(self) -> bool:
        """Returns `True` if this instruction remains valid in the database,
        i.e. if it belongs to at least one function."""
        for _ in self._db.function_instruction_fb(self._ea):
            return True
        return False


class BinaryFunction(BinaryObject):
    """Wrapper around an individual function in the binary."""

    @property
    def instructions(self) -> Iterator[BinaryInstruction]:
        """Generates the set of instructions associated with this function."""
        for ea in sorted(self._db.function_instruction_bf(self._ea)):
            yield BinaryInstruction(self._db, ea)

    def __bool__(self) -> bool:
        """Returns `True` if this function remains valid in the database."""
        return self._db.function_b(self._ea)


class BinaryAnalyzer:
    """Packages up Dr. Disassembler into a binary analyzer."""

    def __init__(self, arch_name: str, os_name: str, binary_data: bytes,
                 workspace_dir: Optional[str] = None,
                 producer: Optional[DatabaseLogInterface] = DatabaseLog(),
                 instruction_decoder: Optional[str] = None,
                 binary_parser: Optional[str] = None):

        # Detect what features are available.
        self._has_binary_ninja = False
        self._has_ida = False
        self._has_lief = False
        self._has_capstone = False
        self._detect_features()
        self._arch: Final[ArchName] = self._get_arch(arch_name)
        self._decoder: Final[InstructionDecoder] = self._get_decoder(
            arch_name, instruction_decoder)

        # Create a workspace, copy the binary into the workspace, then parse
        # the binary.
        self._delete_workspace = False
        self._workspace_dir: Final[str] = self._get_or_create_workspace(
            workspace_dir)
        self._binary_path: Final[str] = self._save_binary_to_workspace(
            binary_data)
        self._parser: Final[BinaryParser] = self._parse_binary(
            os_name, binary_parser)

        # Create a database.
        self._producer: Final = cast(DatabaseLogInterface, producer)
        self._db: Final = Database(self._producer, DatabaseFunctors())

        self._db.enable_heuristic_1(
            [], [])

        # Analyze the binary.
        metadata_importer = BinaryMetadataImporter(self._decoder)
        self._parser.visit_metadata(metadata_importer)
        metadata = metadata_importer.produce()
        if metadata is not None:
            metadata.apply(self._db)

    def __del__(self):
        if self._delete_workspace:
            try:
                os.rmdir(self._workspace_dir)
            except:
                pass

    def _get_or_create_workspace(self, workspace_dir: Optional[str]) -> str:
        """Get or create the workspace in which the binary will be placed."""
        if workspace_dir is None:
            self._delete_workspace = True
            workspace_dir = tempfile.mkdtemp()
        workspace_dir = os.path.abspath(workspace_dir)
        os.makedirs(workspace_dir, exist_ok=True)
        return workspace_dir

    def _save_binary_to_workspace(self, data: bytes) -> str:
        """Saves `data` into the workspace directory."""
        uuid = hashlib.sha256(data).hexdigest()
        binary_path = os.path.join(self._workspace_dir, uuid)

        if not os.path.exists(binary_path):
            with open(binary_path, "wb+") as local_file:
                local_file.write(data)

        return binary_path

    @staticmethod
    def _get_arch(arch_name: str) -> ArchName:
        name = ArchName.from_string(arch_name)
        if name is None:
            raise BinaryAnalysisError(
                f"Unrecognized architecture '{arch_name}'")
        return name

    def _get_decoder(self, arch_name: str, instruction_decoder: Optional[str]) \
            -> InstructionDecoder:
        decoder_name = instruction_decoder or self.default_instruction_decoder
        decoder = decoder_from_string(decoder_name, self._arch)
        if isinstance(decoder, InvalidInstructionDecoder):
            raise BinaryAnalysisError(
                f"Unsupported instruction decoder '{decoder_name}' "
                f"for architecture '{arch_name}'")
        return decoder

    def _parse_binary(self, os_name: str, binary_parser: Optional[str]) \
            -> BinaryParser:
        """Try to parse the binary."""
        parser_name = binary_parser or self.default_binary_parser
        parser = BinaryParser.from_string(
            parser_name, self._arch, os_name, self._binary_path)
        if parser is None:
            raise BinaryAnalysisError(
                f"Error parsing binary with parser '{parser_name}'")
        return parser

    def _detect_features(self):
        """Detect what the supported features are that we can depend upon."""
        try:
            import binaryninja
            self._has_binary_ninja = True
        except:
            pass

        try:
            import ida_ua
            self._has_ida = True
        except:
            pass

        try:
            import capstone
            self._has_capstone = True
        except:
            pass

        try:
            import lief
            self._has_lief = True
        except:
            pass

    @property
    def arch(self) -> ArchName:
        return self._arch

    @property
    def os(self) -> str:
        return self._os

    @property
    def default_binary_parser(self) -> str:
        """Return the name of the binary parser that we are using."""

        # Prefer IDA as the binary parser if we have it, because it implies
        # that we've already loaded IDA itself.
        if self._has_ida:
            return "ida"
        elif self._has_binary_ninja:
            return "binja"
        elif self._has_lief:
            return "lief"
        else:
            raise BinaryAnalysisError(
                "Failed to identify a suitable binary parser")

    @property
    def default_instruction_decoder(self) -> str:
        """Return the name of the instruction decoder that we are using."""
        if self._has_binary_ninja:
            return "binja"
        elif self._has_ida:
            return "ida"
        elif self._has_capstone:
            return "capstone"
        else:
            raise BinaryAnalysisError(
                "Failed to identify a suitable instruction decoder")

    @property
    def functions(self) -> Iterator[BinaryFunction]:
        """Produce a list of functions in the binary."""
        for ea in sorted(self._db.function_f()):
            yield BinaryFunction(self._db, ea)
