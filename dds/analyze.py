# Copyright 2021, Trail of Bits. All rights reserved.

import hashlib
import os

from typing import cast, Final, Iterator, Optional, Union

from dds.datalog import \
    Database, \
    DatabaseLog, \
    DatabaseFunctors, \
    DatabaseLogInterface, \
    DatabaseInputMessageProducer, \
    DatabaseOutputMessageProducer

from dds.arch import \
    ArchName, \
    arch_from_string, \
    ControlFlowBehavior, \
    ControlFlowEdgeKind, \
    decoder_from_string, \
    Instruction, \
    InstructionDecoder, \
    InstructionOperandVisitor, \
    InvalidInstructionDecoder

from dds.binary import \
    binary_parser_from_string, \
    BinaryParser, \
    BinaryMetadataVisitor


class BinaryAnalyzerFeatureError(Exception):
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
            # debug("  Adding instruction {:x}: {}\t\t{}".format(
            #     i.ea, " ".join("{:02x}".format(b) for b in i.data),
            #     i.assembly))

            # Add the instruction to our database.
            self.produce_instruction_3(i.ea, i.type, i.data)

            # If this instruction has a direct control-flow target then add it
            # in.
            if (i.type & ControlFlowBehavior.HAS_DIRECT_TARGET) == \
                    ControlFlowBehavior.HAS_DIRECT_TARGET:
                target_ea = i.target_ea
                assert target_ea is not None
                self.produce_raw_transfer_3(i.ea, target_ea, i.target_type)
                # debug("    -> {:x} {}", target_ea, i.target_type)

            # If this instruction has a fall-through control-flow target
            # then add it in.
            if (i.type & ControlFlowBehavior.HAS_FALL_THROUGH) == \
                    ControlFlowBehavior.HAS_FALL_THROUGH:
                fall_through_ea = i.fall_through_ea
                assert fall_through_ea is not None
                self.produce_raw_transfer_3(
                    i.ea, fall_through_ea, i.fall_through_type)
                # debug("    -> {:x} {}", fall_through_ea, i.fall_through_type)

            # Otherwise it's a "pseudo edge", which is useful for linear
            # disassembly.
            else:
                self.produce_raw_transfer_3(
                    i.ea, i.next_ea, ControlFlowEdgeKind.PSEUDO_FALL_THROUGH)
                # debug("    -> {:x} {}", i.next_ea,
                #       ControlFlowEdgeKind.PSEUDO_FALL_THROUGH)

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
        for ea in self._db.function_instruction_bf(self._ea):
            yield BinaryInstruction(self._db, ea)

    def __bool__(self) -> bool:
        """Returns `True` if this function remains valid in the database."""
        return self._db.function_b(self._ea)


class BinaryAnalyzer:
    """Packages up Dr. Disassembler into a binary analyzer."""

    def __init__(self, workspace_dir: str, arch_name: str,
                 os_name: str, binary_data: bytes,
                 producer: Optional[DatabaseOutputMessageProducer] = None):
        # Detect what features are available.
        self._has_binary_ninja = False
        self._has_ida = False
        self._has_lief = False
        self._has_capstone = False
        self._detect_features()

        # Go get the architecture.
        self._arch: Final[ArchName] = arch_from_string(arch_name)
        if self._arch is None:
            raise BinaryAnalyzerFeatureError(
                f"Unrecognized architecture '{arch_name}'")

        # Go get the instruction decoder.
        decoder_name = self.instruction_decoder
        decoder = decoder_from_string(decoder_name, self._arch)
        if isinstance(decoder, InvalidInstructionDecoder):
            raise BinaryAnalyzerFeatureError(
                f"Unsupported instruction decoder '{decoder_name}' "
                f"for architecture '{arch_name}'")
        self._decoder: Final[InstructionDecoder] = decoder

        # Get the constructor for a binary parser.
        parser_name = self.binary_parser
        make_parser = binary_parser_from_string(parser_name)
        if not make_parser:
            raise BinaryAnalyzerFeatureError(
                f"Unhandled binary parser type '{self.binary_parser}'")

        # Copy the binary into the workspace.
        self._workspace_dir: Final[str] = os.path.abspath(workspace_dir)
        self._uuid: Final[str] = hashlib.sha1(binary_data).hexdigest()
        self._binary_path: Final[str] = \
            os.path.join(self._workspace_dir, self._uuid)

        with open(self._binary_path, "wb+") as local_file:
            local_file.write(binary_data)

        try:
            parser = make_parser(self._arch, os_name, self._binary_path)
        except Exception as e:
            raise BinaryAnalyzerFeatureError(
                f"Error parsing binary with parser '{parser_name}': {e}")
        self._parser: Final[BinaryParser] = parser

        # Create a database.
        if not producer:
            producer = DatabaseLog()
        self._producer: Final = cast(DatabaseLogInterface, producer)
        self._db: Final = Database(producer, DatabaseFunctors())

        # Analyze the binary.
        metadata_importer = BinaryMetadataImporter(self._decoder)
        self._parser.visit_metadata(metadata_importer)
        metadata = metadata_importer.produce()
        if metadata is not None:
            metadata.apply(self._db)

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
    def binary_parser(self) -> str:
        """Return the name of the binary parser that we are using."""
        if self._has_binary_ninja:
            return "binja"
        elif self._has_ida:
            return "ida"
        elif self._has_lief:
            return "lief"
        else:
            raise BinaryAnalyzerFeatureError(
                "Failed to identify a suitable binary parser")

    @property
    def instruction_decoder(self) -> str:
        """Return the name of the instruction decoder that we are using."""
        if self._has_binary_ninja:
            return "binja"
        elif self._has_ida:
            return "ida"
        elif self._has_capstone:
            return "capstone"
        else:
            raise BinaryAnalyzerFeatureError(
                "Failed to identify a suitable instruction decoder")

    @property
    def functions(self) -> Iterator[BinaryFunction]:
        """Produce a list of functions in the binary."""
        for ea in self._db.function_f():
            yield BinaryFunction(self._db, ea)
