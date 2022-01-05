# Auto-generated file

# flake8: noqa
# fmt: off

from __future__ import annotations
from dataclasses import dataclass
from typing import Final, Iterator, List, Optional, Tuple
try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore


from dds.arch import ControlFlowEdgeKind, InstructionType
from dds.heuristic import ControlFlowRecoveryHeuristic


class DatabaseInterface(Protocol):
    def raw_transfer_3(self, vector: List[Tuple[int, int, ControlFlowEdgeKind]]):
        ...

    def external_symbol_2(self, vector: List[Tuple[int, bytes]]):
        ...

    def local_function_2(self, vector: List[Tuple[int, bytes]]):
        ...

    def address_operand_2(self, vector: List[Tuple[int, int]]):
        ...

    def exported_function_2(self, vector: List[Tuple[int, bytes]]):
        ...

    def imported_function_2(self, vector: List[Tuple[int, bytes]]):
        ...

    def local_symbol_2(self, vector: List[Tuple[int, bytes]]):
        ...

    def imported_symbol_2(self, vector: List[Tuple[int, bytes]]):
        ...

    def exported_symbol_2(self, vector: List[Tuple[int, bytes]]):
        ...

    def relocation_2(self, vector: List[Tuple[int, int]]):
        ...

    def section_3(self, vector: List[Tuple[bytes, int, int]]):
        ...

    def entrypoint_1(self, vector: List[int]):
        ...

    def instruction_3(self, vector: List[Tuple[int, InstructionType, bytes]]):
        ...

    def enable_heuristic_1(self, vector: List[ControlFlowRecoveryHeuristic], added: bool):
        ...


@dataclass
class DatabaseInputMessage:
    _add_raw_transfer_3: Optional[List[Tuple[int, int, ControlFlowEdgeKind]]] = None
    _add_external_symbol_2: Optional[List[Tuple[int, bytes]]] = None
    _add_local_function_2: Optional[List[Tuple[int, bytes]]] = None
    _add_address_operand_2: Optional[List[Tuple[int, int]]] = None
    _add_exported_function_2: Optional[List[Tuple[int, bytes]]] = None
    _add_imported_function_2: Optional[List[Tuple[int, bytes]]] = None
    _add_local_symbol_2: Optional[List[Tuple[int, bytes]]] = None
    _add_imported_symbol_2: Optional[List[Tuple[int, bytes]]] = None
    _add_exported_symbol_2: Optional[List[Tuple[int, bytes]]] = None
    _add_relocation_2: Optional[List[Tuple[int, int]]] = None
    _add_section_3: Optional[List[Tuple[bytes, int, int]]] = None
    _add_entrypoint_1: Optional[List[int]] = None
    _add_instruction_3: Optional[List[Tuple[int, InstructionType, bytes]]] = None
    _add_enable_heuristic_1: Optional[List[ControlFlowRecoveryHeuristic]] = None
    _rem_enable_heuristic_1: Optional[List[ControlFlowRecoveryHeuristic]] = None

    def apply(self, db: DatabaseInterface) -> int:
        num_messages: int = 0
        if self._add_raw_transfer_3 is not None:
            num_messages += len(self._add_raw_transfer_3)
            db.raw_transfer_3(self._add_raw_transfer_3)
        if self._add_external_symbol_2 is not None:
            num_messages += len(self._add_external_symbol_2)
            db.external_symbol_2(self._add_external_symbol_2)
        if self._add_local_function_2 is not None:
            num_messages += len(self._add_local_function_2)
            db.local_function_2(self._add_local_function_2)
        if self._add_address_operand_2 is not None:
            num_messages += len(self._add_address_operand_2)
            db.address_operand_2(self._add_address_operand_2)
        if self._add_exported_function_2 is not None:
            num_messages += len(self._add_exported_function_2)
            db.exported_function_2(self._add_exported_function_2)
        if self._add_imported_function_2 is not None:
            num_messages += len(self._add_imported_function_2)
            db.imported_function_2(self._add_imported_function_2)
        if self._add_local_symbol_2 is not None:
            num_messages += len(self._add_local_symbol_2)
            db.local_symbol_2(self._add_local_symbol_2)
        if self._add_imported_symbol_2 is not None:
            num_messages += len(self._add_imported_symbol_2)
            db.imported_symbol_2(self._add_imported_symbol_2)
        if self._add_exported_symbol_2 is not None:
            num_messages += len(self._add_exported_symbol_2)
            db.exported_symbol_2(self._add_exported_symbol_2)
        if self._add_relocation_2 is not None:
            num_messages += len(self._add_relocation_2)
            db.relocation_2(self._add_relocation_2)
        if self._add_section_3 is not None:
            num_messages += len(self._add_section_3)
            db.section_3(self._add_section_3)
        if self._add_entrypoint_1 is not None:
            num_messages += len(self._add_entrypoint_1)
            db.entrypoint_1(self._add_entrypoint_1)
        if self._add_instruction_3 is not None:
            num_messages += len(self._add_instruction_3)
            db.instruction_3(self._add_instruction_3)
        if self._add_enable_heuristic_1 is not None:
            num_messages += len(self._add_enable_heuristic_1)
            db.enable_heuristic_1(self._add_enable_heuristic_1, True)
        if self._rem_enable_heuristic_1 is not None:
            num_messages += len(self._rem_enable_heuristic_1)
            db.enable_heuristic_1(self._rem_enable_heuristic_1, False)
        return num_messages


class DatabaseInputMessageProducer:
    def __init__(self):
        self._msg: DatabaseInputMessage = DatabaseInputMessage()
        self._num_msgs: int = 0

    def produce_raw_transfer_3(self, InsnEA: int, NextEA: int, EdgeType: ControlFlowEdgeKind):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_raw_transfer_3
            if _msgs is None:
                _msgs = []
                self._msg._add_raw_transfer_3 = _msgs
        _msgs.append((InsnEA, NextEA, EdgeType))  # type: ignore

    def produce_external_symbol_2(self, EA: int, Name: bytes):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_external_symbol_2
            if _msgs is None:
                _msgs = []
                self._msg._add_external_symbol_2 = _msgs
        _msgs.append((EA, Name))  # type: ignore

    def produce_local_function_2(self, EA: int, Name: bytes):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_local_function_2
            if _msgs is None:
                _msgs = []
                self._msg._add_local_function_2 = _msgs
        _msgs.append((EA, Name))  # type: ignore

    def produce_address_operand_2(self, InsnEA: int, MemAddr: int):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_address_operand_2
            if _msgs is None:
                _msgs = []
                self._msg._add_address_operand_2 = _msgs
        _msgs.append((InsnEA, MemAddr))  # type: ignore

    def produce_exported_function_2(self, EA: int, Name: bytes):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_exported_function_2
            if _msgs is None:
                _msgs = []
                self._msg._add_exported_function_2 = _msgs
        _msgs.append((EA, Name))  # type: ignore

    def produce_imported_function_2(self, EA: int, Name: bytes):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_imported_function_2
            if _msgs is None:
                _msgs = []
                self._msg._add_imported_function_2 = _msgs
        _msgs.append((EA, Name))  # type: ignore

    def produce_local_symbol_2(self, EA: int, Name: bytes):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_local_symbol_2
            if _msgs is None:
                _msgs = []
                self._msg._add_local_symbol_2 = _msgs
        _msgs.append((EA, Name))  # type: ignore

    def produce_imported_symbol_2(self, EA: int, Name: bytes):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_imported_symbol_2
            if _msgs is None:
                _msgs = []
                self._msg._add_imported_symbol_2 = _msgs
        _msgs.append((EA, Name))  # type: ignore

    def produce_exported_symbol_2(self, EA: int, Name: bytes):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_exported_symbol_2
            if _msgs is None:
                _msgs = []
                self._msg._add_exported_symbol_2 = _msgs
        _msgs.append((EA, Name))  # type: ignore

    def produce_relocation_2(self, RelocEA: int, ExternEA: int):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_relocation_2
            if _msgs is None:
                _msgs = []
                self._msg._add_relocation_2 = _msgs
        _msgs.append((RelocEA, ExternEA))  # type: ignore

    def produce_section_3(self, SecName: bytes, SecStart: int, SecEnd: int):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_section_3
            if _msgs is None:
                _msgs = []
                self._msg._add_section_3 = _msgs
        _msgs.append((SecName, SecStart, SecEnd))  # type: ignore

    def produce_entrypoint_1(self, EntryPointEA: int):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_entrypoint_1
            if _msgs is None:
                _msgs = []
                self._msg._add_entrypoint_1 = _msgs
        _msgs.append(EntryPointEA)  # type: ignore

    def produce_instruction_3(self, InsnEA: int, Type: InstructionType, Bytes: bytes):
        self._num_msgs += 1
        _added = True
        if _added:
            _msgs = self._msg._add_instruction_3
            if _msgs is None:
                _msgs = []
                self._msg._add_instruction_3 = _msgs
        _msgs.append((InsnEA, Type, Bytes))  # type: ignore

    def produce_enable_heuristic_1(self, Heuristic: ControlFlowRecoveryHeuristic, _added: bool):
        self._num_msgs += 1
        if _added:
            _msgs = self._msg._add_enable_heuristic_1
            if _msgs is None:
                _msgs = []
                self._msg._add_enable_heuristic_1 = _msgs
        else:
            _msgs = self._msg._rem_enable_heuristic_1
            if _msgs is None:
                _msgs = []
                self._msg._rem_enable_heuristic_1 = _msgs
        _msgs.append(Heuristic)  # type: ignore

    def produce(self) -> Optional[DatabaseInputMessage]:
        if not self._num_msgs:
            return None
        self._num_msgs = 0
        msg = self._msg
        self._msg = DatabaseInputMessage()
        return msg

    def __len__(self) -> int:
        return self._num_msgs


@dataclass
class DatabaseOutputMessage:
    pass


class DatabaseOutputMessageProducer:
    def __init__(self):
        self._num_msgs: int = 0
        self._msg: DatabaseOutputMessage = DatabaseOutputMessage()

    def produce(self) -> Optional[DatabaseOutputMessage]:
        if not self._num_msgs:
            return None
        self._num_msgs = 0
        msg = self._msg
        self._msg = DatabaseOutputMessage()
        return msg

    def __len__(self) -> int:
        return self._num_msgs


class DatabaseOutputMessageConsumer:
    def consume(self, msg: DatabaseOutputMessage):
        return

# End of auto-generated file
