# Copyright 2020, Trail of Bits. All rights reserved.

from abc import ABC, abstractmethod
from aenum import NamedConstant
from enum import Flag, auto
from typing import Dict, Final, Optional, Union


class ControlFlowBehavior:
    """Flags describing the types of control flows that an instruction has."""
    HAS_TARGET = 1 << 1
    HAS_FALL_THROUGH = 1 << 2

    TARGET_IS_CONDITIONAL = 1 << 3
    TARGET_IS_DIRECT = 1 << 4

    HAS_DIRECT_TARGET = HAS_TARGET | TARGET_IS_DIRECT


class ControlFlowEdgeKind(Flag):
    # In a `call target`, this represents the flow between the `call`
    # instruction and `target`.
    FUNCTION_CALL = auto()

    # With `jmp target`, this represents the flow between the `jmp` and
    # `target`.
    JUMP_TAKEN = auto()

    # This represents the flow between one instruction and its next instruction.
    # For `jmp` instructions, this is a kind of pseudo edge.
    FALL_THROUGH = auto()

    # This represents the flow between one instruction and its next instruction.
    # For `jmp` and `ret` instructions, this is a kind of pseudo edge. The goal
    # is to capture the notion of linear disassembly.
    PSEUDO_FALL_THROUGH = auto()

    # In something like a `jCC label`, this represents the flow between the
    # `jCC` and the following instruction.
    JUMP_NOT_TAKEN = JUMP_TAKEN | FALL_THROUGH

    # In a `call target`, this represents the flow between `target` back
    # to the instruction following the `call`.
    FUNCTION_CALL_RETURN = FUNCTION_CALL | FALL_THROUGH

    # If we have a `jmp target`, where `target` is a function head.
    #
    # NOTE: This is a Datalog-derived edge type.
    TAIL_FUNCTION_CALL = FUNCTION_CALL | JUMP_TAKEN

    # If we have something like `call $+5` on x86, which is used to get the
    # program counter onto the stack (or into a register).
    #
    # NOTE: This is a Datalog-derived edge type.
    PC_THUNK_FUNCTION_CALL = FUNCTION_CALL | FUNCTION_CALL_RETURN


class InstructionType(NamedConstant):
    """Represents different categories of instructions. An invalid instruction
    category is not represented, as we don't add invalid instructions into
    the database."""

    # An error instruction, e.g. `ud2`, `hlt`, etc.
    #
    # Represented with an empty flag set, i.e. it doesn't have either a target
    # or a fall-through.
    ERROR = 0

    # Normal, single-entry, single-exit instructions. These instructions
    # transfer control to the next instruction.
    NORMAL = ControlFlowBehavior.HAS_FALL_THROUGH

    # A direct jump, e.g. `jmp label` on x86.
    DIRECT_JUMP = \
        ControlFlowBehavior.HAS_TARGET | ControlFlowBehavior.TARGET_IS_DIRECT

    # An indirect jump, e.g. `jmp rax` or `jmp [rax]` on x86-64.
    INDIRECT_JUMP = ControlFlowBehavior.HAS_TARGET

    # A conditional jump. E.g. `jz label` on x86.
    CONDITIONAL_DIRECT_JUMP = \
        ControlFlowBehavior.HAS_TARGET | \
        ControlFlowBehavior.HAS_FALL_THROUGH | \
        ControlFlowBehavior.TARGET_IS_CONDITIONAL | \
        ControlFlowBehavior.TARGET_IS_DIRECT

    # A conditional jump. E.g. `jz label` on x86.
    CONDITIONAL_INDIRECT_JUMP = \
        ControlFlowBehavior.HAS_TARGET | \
        ControlFlowBehavior.HAS_FALL_THROUGH | \
        ControlFlowBehavior.TARGET_IS_CONDITIONAL

    # A direct function call, e.g. `call label`.
    DIRECT_FUNCTION_CALL = \
        ControlFlowBehavior.HAS_TARGET | \
        ControlFlowBehavior.HAS_FALL_THROUGH | \
        ControlFlowBehavior.TARGET_IS_DIRECT

    # An indirect function call, e.g. `call rax` or `call [rax]` on x86-64.
    INDIRECT_FUNCTION_CALL = \
        ControlFlowBehavior.HAS_TARGET | ControlFlowBehavior.HAS_FALL_THROUGH

    # A conditional direct function call. E.g. a conditional branch-and-link
    # on AArch32.
    CONDITIONAL_DIRECT_FUNCTION_CALL = \
        ControlFlowBehavior.HAS_TARGET | \
        ControlFlowBehavior.HAS_FALL_THROUGH | \
        ControlFlowBehavior.TARGET_IS_CONDITIONAL | \
        ControlFlowBehavior.TARGET_IS_DIRECT

    # A conditional indirect function call. E.g. a conditional branch-and-link
    # on AArch32.
    CONDITIONAL_INDIRECT_FUNCTION_CALL = \
        ControlFlowBehavior.HAS_TARGET | \
        ControlFlowBehavior.HAS_FALL_THROUGH | \
        ControlFlowBehavior.TARGET_IS_CONDITIONAL

    # Function return, e.g. `ret` on x86.
    FUNCTION_RETURN = 0

    # Function return, e.g. `ret` on x86.
    CONDITIONAL_FUNCTION_RETURN = \
        ControlFlowBehavior.HAS_FALL_THROUGH | \
        ControlFlowBehavior.TARGET_IS_CONDITIONAL


_TARGET_TYPE: Final[Dict[InstructionType, Optional[ControlFlowEdgeKind]]] = {
    id(InstructionType.NORMAL): None,
    id(InstructionType.ERROR): None,
    id(InstructionType.DIRECT_JUMP): ControlFlowEdgeKind.JUMP_TAKEN,
    id(InstructionType.INDIRECT_JUMP): None,
    id(InstructionType.CONDITIONAL_DIRECT_JUMP): ControlFlowEdgeKind.JUMP_TAKEN,
    id(InstructionType.CONDITIONAL_INDIRECT_JUMP): None,
    id(InstructionType.DIRECT_FUNCTION_CALL): ControlFlowEdgeKind.FUNCTION_CALL,
    id(InstructionType.INDIRECT_FUNCTION_CALL): None,
    id(InstructionType.CONDITIONAL_DIRECT_FUNCTION_CALL):
    id(    ControlFlowEdgeKind.FUNCTION_CALL),
    id(InstructionType.CONDITIONAL_INDIRECT_FUNCTION_CALL): None,
    id(InstructionType.FUNCTION_RETURN): None,
    id(InstructionType.CONDITIONAL_FUNCTION_RETURN): None
}

_FALL_THROUGH_TYPE: Final[Dict[int, Optional[ControlFlowEdgeKind]]] = {
    id(InstructionType.NORMAL): ControlFlowEdgeKind.FALL_THROUGH,
    id(InstructionType.ERROR): ControlFlowEdgeKind.PSEUDO_FALL_THROUGH,
    id(InstructionType.DIRECT_JUMP): ControlFlowEdgeKind.PSEUDO_FALL_THROUGH,
    id(InstructionType.INDIRECT_JUMP): ControlFlowEdgeKind.PSEUDO_FALL_THROUGH,
    id(InstructionType.CONDITIONAL_DIRECT_JUMP):
        ControlFlowEdgeKind.JUMP_NOT_TAKEN,
    id(InstructionType.CONDITIONAL_INDIRECT_JUMP):
        ControlFlowEdgeKind.JUMP_NOT_TAKEN,
    id(InstructionType.DIRECT_FUNCTION_CALL):
        ControlFlowEdgeKind.FUNCTION_CALL_RETURN,
    id(InstructionType.INDIRECT_FUNCTION_CALL):
        ControlFlowEdgeKind.FUNCTION_CALL_RETURN,
    id(InstructionType.CONDITIONAL_DIRECT_FUNCTION_CALL):
        ControlFlowEdgeKind.FUNCTION_CALL_RETURN,
    id(InstructionType.CONDITIONAL_INDIRECT_FUNCTION_CALL):
        ControlFlowEdgeKind.FUNCTION_CALL_RETURN,
    id(InstructionType.FUNCTION_RETURN):
        ControlFlowEdgeKind.PSEUDO_FALL_THROUGH,
    id(InstructionType.CONDITIONAL_FUNCTION_RETURN):
        ControlFlowEdgeKind.JUMP_NOT_TAKEN
}


class InstructionOperandVisitor:
    def visit_address_operand(self, op_index: int, addr: int):
        pass

    # TODO: Eventually add others, if desirable.


class Instruction(ABC):
    """Abstraction over a decoded instruction."""

    @property
    @abstractmethod
    def type(self) -> InstructionType:
        ...

    @property
    @abstractmethod
    def ea(self) -> int:
        ...

    @property
    @abstractmethod
    def size(self) -> int:
        ...

    @property
    @abstractmethod
    def data(self) -> Union[bytes, bytearray]:
        ...

    @property
    def next_ea(self) -> int:
        return self.ea + self.size

    @property
    def fall_through_ea(self) -> Optional[int]:
        return self.next_ea

    @property
    @abstractmethod
    def target_ea(self) -> Optional[int]:
        ...

    @property
    def fall_through_type(self) -> Optional[ControlFlowEdgeKind]:
        return _FALL_THROUGH_TYPE[id(self.type)]

    @property
    def target_type(self) -> Optional[ControlFlowEdgeKind]:
        return _TARGET_TYPE[id(self.type)]

    @property
    def assembly(self) -> str:
        return ""

    @abstractmethod
    def visit_operands(self, visitor: InstructionOperandVisitor):
        ...
