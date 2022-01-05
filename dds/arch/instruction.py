# Copyright 2020, Trail of Bits. All rights reserved.

from abc import ABC, abstractmethod
from enum import IntEnum
from typing import Dict, Final, Optional, Union


class ControlFlowBehavior:
    """Flags describing the types of control flows that an instruction has."""
    HAS_TARGET = 1 << 1
    HAS_FALL_THROUGH = 1 << 2

    TARGET_IS_CONDITIONAL = 1 << 3
    TARGET_IS_DIRECT = 1 << 4

    HAS_DIRECT_TARGET = HAS_TARGET | TARGET_IS_DIRECT


class ControlFlowEdgeKind(IntEnum):
    # In a `call target`, this represents the flow between the `call`
    # instruction and `target`.
    FUNCTION_CALL = (1 << 1)

    # With `jmp target`, this represents the flow between the `jmp` and
    # `target`.
    JUMP_TAKEN = (1 << 2)

    # This represents the flow between one instruction and its next instruction.
    # For `jmp` instructions, this is a kind of pseudo edge.
    FALL_THROUGH = (1 << 3)

    # This represents the flow between one instruction and its next instruction.
    # For `jmp` and `ret` instructions, this is a kind of pseudo edge. The goal
    # is to capture the notion of linear disassembly.
    PSEUDO_FALL_THROUGH = (1 << 4)

    # In something like a `jCC label`, this represents the flow between the
    # `jCC` and the following instruction.
    JUMP_NOT_TAKEN = (1 << 5) | JUMP_TAKEN | FALL_THROUGH

    # In a `call target`, this represents the flow between `target` back
    # to the instruction following the `call`.
    FUNCTION_CALL_RETURN = (1 << 6) | FUNCTION_CALL | FALL_THROUGH

    # If we have a `jmp target`, where `target` is a function head.
    #
    # NOTE: This is a Datalog-derived edge type.
    TAIL_FUNCTION_CALL = (1 << 7) | FUNCTION_CALL | JUMP_TAKEN

    # If we have something like `call $+5` on x86, which is used to get the
    # program counter onto the stack (or into a register).
    #
    # NOTE: This is a Datalog-derived edge type.
    PC_THUNK_FUNCTION_CALL = (1 << 8) | FUNCTION_CALL | FUNCTION_CALL_RETURN


class InstructionType(IntEnum):
    """Represents different categories of instructions. An invalid instruction
    category is not represented, as we don't add invalid instructions into
    the database."""

    # An error instruction, e.g. `ud2`, `hlt`, etc.
    #
    # Represented with an empty flag set, i.e. it doesn't have either a target
    # or a fall-through.
    ERROR = (1 << 16)

    # Normal, single-entry, single-exit instructions. These instructions
    # transfer control to the next instruction.
    NORMAL = (1 << 17) | ControlFlowBehavior.HAS_FALL_THROUGH

    # An indirect jump, e.g. `jmp rax` or `jmp [rax]` on x86-64.
    INDIRECT_JUMP = \
        (1 << 18) | \
        ControlFlowBehavior.HAS_TARGET

    # A direct jump, e.g. `jmp label` on x86.
    DIRECT_JUMP = \
        (1 << 19) | \
        INDIRECT_JUMP | \
        ControlFlowBehavior.TARGET_IS_DIRECT

    # A conditional jump. E.g. `bne [r2]` on armv7.
    CONDITIONAL_INDIRECT_JUMP = \
        (1 << 20) | \
        ControlFlowBehavior.HAS_TARGET | \
        ControlFlowBehavior.HAS_FALL_THROUGH | \
        ControlFlowBehavior.TARGET_IS_CONDITIONAL

    # A conditional jump. E.g. `jz label` on x86.
    CONDITIONAL_DIRECT_JUMP = \
        (1 << 21) | \
        CONDITIONAL_INDIRECT_JUMP | \
        ControlFlowBehavior.TARGET_IS_DIRECT

    # An indirect function call, e.g. `call rax` or `call [rax]` on x86-64.
    INDIRECT_FUNCTION_CALL = \
        (1 << 22) | \
        ControlFlowBehavior.HAS_TARGET | \
        ControlFlowBehavior.HAS_FALL_THROUGH

    # A direct function call, e.g. `call label`.
    DIRECT_FUNCTION_CALL = \
        (1 << 23) | \
        INDIRECT_FUNCTION_CALL | \
        ControlFlowBehavior.TARGET_IS_DIRECT

    # A conditional direct function call. E.g. a conditional branch-and-link
    # on AArch32.
    CONDITIONAL_DIRECT_FUNCTION_CALL = \
        (1 << 24) | \
        DIRECT_FUNCTION_CALL | \
        ControlFlowBehavior.TARGET_IS_CONDITIONAL

    # A conditional indirect function call. E.g. a conditional branch-and-link
    # on AArch32.
    CONDITIONAL_INDIRECT_FUNCTION_CALL = \
        (1 << 25) | \
        INDIRECT_FUNCTION_CALL | \
        ControlFlowBehavior.TARGET_IS_CONDITIONAL

    # Function return, e.g. `ret` on x86.
    FUNCTION_RETURN = (1 << 26)

    # Function return, e.g. `rnz` on Intel 8085.
    CONDITIONAL_FUNCTION_RETURN = \
        (1 << 27) | \
        FUNCTION_RETURN | \
        ControlFlowBehavior.HAS_FALL_THROUGH | \
        ControlFlowBehavior.TARGET_IS_CONDITIONAL


_TARGET_TYPE: Final[Dict[InstructionType, Optional[ControlFlowEdgeKind]]] = {
    InstructionType.NORMAL: 
        None,
    InstructionType.ERROR: 
        None,
    InstructionType.DIRECT_JUMP: 
        ControlFlowEdgeKind.JUMP_TAKEN,
    InstructionType.INDIRECT_JUMP: 
        None,
    InstructionType.CONDITIONAL_DIRECT_JUMP: 
        ControlFlowEdgeKind.JUMP_TAKEN,
    InstructionType.CONDITIONAL_INDIRECT_JUMP: 
        None,
    InstructionType.DIRECT_FUNCTION_CALL: 
        ControlFlowEdgeKind.FUNCTION_CALL,
    InstructionType.INDIRECT_FUNCTION_CALL: 
        None,
    InstructionType.CONDITIONAL_DIRECT_FUNCTION_CALL:
        ControlFlowEdgeKind.FUNCTION_CALL,
    InstructionType.CONDITIONAL_INDIRECT_FUNCTION_CALL: 
        None,
    InstructionType.FUNCTION_RETURN: 
        None,
    InstructionType.CONDITIONAL_FUNCTION_RETURN: None
}

_FALL_THROUGH_TYPE: Final[
    Dict[InstructionType, Optional[ControlFlowEdgeKind]]] = {
    InstructionType.NORMAL: 
        ControlFlowEdgeKind.FALL_THROUGH,
    InstructionType.ERROR: 
        ControlFlowEdgeKind.PSEUDO_FALL_THROUGH,
    InstructionType.DIRECT_JUMP: 
        ControlFlowEdgeKind.PSEUDO_FALL_THROUGH,
    InstructionType.INDIRECT_JUMP: 
        ControlFlowEdgeKind.PSEUDO_FALL_THROUGH,
    InstructionType.CONDITIONAL_DIRECT_JUMP: 
        ControlFlowEdgeKind.JUMP_NOT_TAKEN,
    InstructionType.CONDITIONAL_INDIRECT_JUMP:
        ControlFlowEdgeKind.JUMP_NOT_TAKEN,
    InstructionType.DIRECT_FUNCTION_CALL:
        ControlFlowEdgeKind.FUNCTION_CALL_RETURN,
    InstructionType.INDIRECT_FUNCTION_CALL:
        ControlFlowEdgeKind.FUNCTION_CALL_RETURN,
    InstructionType.CONDITIONAL_DIRECT_FUNCTION_CALL:
        ControlFlowEdgeKind.FUNCTION_CALL_RETURN,
    InstructionType.CONDITIONAL_INDIRECT_FUNCTION_CALL:
        ControlFlowEdgeKind.FUNCTION_CALL_RETURN,
    InstructionType.FUNCTION_RETURN: 
        ControlFlowEdgeKind.PSEUDO_FALL_THROUGH,
    InstructionType.CONDITIONAL_FUNCTION_RETURN:
        ControlFlowEdgeKind.JUMP_NOT_TAKEN
}


class InstructionOperandVisitor:
    def visit_address_operand(self, inst: 'Instruction', op_index: int,
                              addr: int):
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
    def data(self) -> bytes:
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
        return _FALL_THROUGH_TYPE[self.type]

    @property
    def target_type(self) -> Optional[ControlFlowEdgeKind]:
        return _TARGET_TYPE[self.type]

    @property
    def assembly(self) -> str:
        return ""

    @abstractmethod
    def visit_operands(self, visitor: InstructionOperandVisitor):
        ...
