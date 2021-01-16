# Copyright 2021, Trail of Bits. All rights reserved.

from abc import ABC
from typing import Dict, Final, Callable, Iterable, Optional, Union, Set
from binaryninja import *

from .name import ArchName
from .decoder import InstructionDecoder
from .instruction import \
    ControlFlowBehavior, \
    Instruction, \
    InstructionOperandVisitor, \
    InstructionType

_BINJA_ARCH_MODE: Final[Dict[ArchName, int]] = {
    ArchName.X86: Architecture['x86'],
    ArchName.X86_AVX: Architecture['x86'],
    ArchName.X86_AVX512: Architecture['x86'],
    ArchName.AMD64: Architecture['x86_64'],
    ArchName.AMD64_AVX: Architecture['x86_64'],
    ArchName.AMD64_AVX512: Architecture['x86_64'],
    ArchName.AARCH32: Architecture['armv7'],
    ArchName.AARCH64: Architecture['aarch64']
    # ArchName.SPARC32:
    # ArchName.SPARC32:
}

_JUMP_TARGET_KIND: Dict[LowLevelILOperation, InstructionType] = {
    LowLevelILOperation.LLIL_CONST: InstructionType.DIRECT_JUMP,
    LowLevelILOperation.LLIL_CONST_PTR: InstructionType.DIRECT_JUMP,
    LowLevelILOperation.LLIL_EXTERN_PTR: InstructionType.DIRECT_JUMP,
}

_CALL_TARGET_KIND: Dict[LowLevelILOperation, InstructionType] = {
    LowLevelILOperation.LLIL_CONST: InstructionType.DIRECT_FUNCTION_CALL,
    LowLevelILOperation.LLIL_CONST_PTR: InstructionType.DIRECT_FUNCTION_CALL,
    LowLevelILOperation.LLIL_EXTERN_PTR: InstructionType.DIRECT_FUNCTION_CALL,
}

# An extra flag for bitmasks returned by `_visit_llil` that signal conditional
# control flow. This hels us distinguish a `bound` instruction on x86 as not
# being an error, as really it's a conditional error, or alternatively, a
# conditional indirect jump.
_FLAG_IS_CONDITIONAL: Final[int] = (1 << 63)


def _visit_llil(func: LowLevelILFunction, index: int) -> int:
    """Recursively visit the instructions of a low levle IL function and build
    up a bitmask representing the possible control flow features and instruction
    types of the instruction which produced `func`."""

    try:
        insn: LowLevelILInstruction = func[index]
    except IndexError as e:
        return InstructionType.NORMAL

    # Goto within the IL. If we see a backwards edge the assume we're dealing
    # with something conditional; we'll merge later.
    if insn.operation == LowLevelILOperation.LLIL_GOTO:
        if insn.dest < index:
            return InstructionType.CONDITIONAL_DIRECT_JUMP
        else:
            return _visit_llil(func, insn.dest)

    # Unconditional branches.
    elif insn.operation == LowLevelILOperation.LLIL_JUMP or \
            insn.operation == LowLevelILOperation.LLIL_TAILCALL:
        return _JUMP_TARGET_KIND.get(insn.dest.operation,
                                     InstructionType.INDIRECT_JUMP)

    # Jump tables.
    elif insn.operation == LowLevelILOperation.LLIL_JUMP_TO:
        return InstructionType.INDIRECT_JUMP

    elif insn.operation == LowLevelILOperation.LLIL_CALL:
        return _CALL_TARGET_KIND.get(insn.dest.operation,
                                     InstructionType.INDIRECT_FUNCTION_CALL)

    elif insn.operation == LowLevelILOperation.LLIL_RET:
        return InstructionType.FUNCTION_RETURN

    # Conditional branches.
    elif insn.operation == LowLevelILOperation.LLIL_IF:

        true_kind: int = ControlFlowBehavior.HAS_TARGET | \
                         ControlFlowBehavior.TARGET_IS_CONDITIONAL

        if insn.true > index:
            true_kind = _visit_llil(func, insn.true)
        false_kind: int = 0
        if insn.false > index:
            false_kind = _visit_llil(func, insn.false)
        return true_kind | false_kind | _FLAG_IS_CONDITIONAL

    elif insn.operation == LowLevelILOperation.LLIL_SYSCALL:
        return InstructionType.INDIRECT_FUNCTION_CALL

    # Returns.
    elif insn.operation == lowlevelil.LowLevelILOperation.LLIL_RET:
        return InstructionType.FUNCTION_RETURN

    elif insn.operation == LowLevelILOperation.LLIL_NORET or \
            insn.operation == LowLevelILOperation.LLIL_TRAP or \
            insn.operation == LowLevelILOperation.LLIL_UNDEF:
        return InstructionType.ERROR

    else:
        return _visit_llil(func, index + 1)


def _llil_to_itype(insn: LowLevelILInstruction) -> InstructionType:
    """Deduce an `InstructionType` from a low-level IL instruction"""

    joint_kind = _visit_llil(insn.function, 0)

    # Conditional flows with a target.
    if joint_kind & ControlFlowBehavior.TARGET_IS_CONDITIONAL:
        assert 0 != (joint_kind & ControlFlowBehavior.HAS_TARGET)

        # Conditional flows wiht a direct target, either conditional jump
        # or conditional call.
        if joint_kind & ControlFlowBehavior.TARGET_IS_DIRECT:
            if (joint_kind & InstructionType.DIRECT_FUNCTION_CALL) == \
                    InstructionType.DIRECT_FUNCTION_CALL:
                return InstructionType.CONDITIONAL_DIRECT_FUNCTION_CALL
            else:
                return InstructionType.CONDITIONAL_DIRECT_JUMP

        elif (joint_kind & InstructionType.FUNCTION_RETURN) == \
                InstructionType.FUNCTION_RETURN:
            return InstructionType.CONDITIONAL_FUNCTION_RETURN
        elif (joint_kind & InstructionType.INDIRECT_FUNCTION_CALL) == \
                InstructionType.INDIRECT_FUNCTION_CALL:
            return InstructionType.CONDITIONAL_INDIRECT_FUNCTION_CALL
        else:
            return InstructionType.CONDITIONAL_INDIRECT_JUMP

    # Direct flows with a target, either
    elif joint_kind & ControlFlowBehavior.TARGET_IS_DIRECT:
        if (joint_kind & InstructionType.DIRECT_FUNCTION_CALL) == \
                InstructionType.DIRECT_FUNCTION_CALL:
            return InstructionType.DIRECT_FUNCTION_CALL
        else:
            return InstructionType.DIRECT_JUMP

    elif (joint_kind & InstructionType.FUNCTION_RETURN) == \
            InstructionType.FUNCTION_RETURN:
        return InstructionType.FUNCTION_RETURN

    elif (joint_kind & InstructionType.INDIRECT_FUNCTION_CALL) == \
            InstructionType.INDIRECT_FUNCTION_CALL:
        return InstructionType.INDIRECT_FUNCTION_CALL

    elif (joint_kind & InstructionType.INDIRECT_JUMP) == \
            InstructionType.INDIRECT_JUMP:
        return InstructionType.INDIRECT_JUMP

    # We use the `_FLAG_IS_CONDITIONAL` as an extra test to distinguish
    # things like x86's `bound`.
    elif (joint_kind & InstructionType.ERROR) == InstructionType.ERROR and \
            0 == (joint_kind & _FLAG_IS_CONDITIONAL):
        return InstructionType.ERROR

    # Normal, fall-through instruction.
    else:
        return InstructionType.NORMAL


def _find_jump_target(func: LowLevelILFunction, index: int, seen: Set[int]):
    """Find the direct target of a jump or call from the LLIL."""

    try:
        insn = func[index]
    except IndexError as e:
        return 0

    if index in seen:
        return 0

    seen.add(index)

    # Goto within the IL. If we see a backwards edge the assume we're
    # dealing
    # with something conditional; we'll merge later.
    if insn.operation == LowLevelILOperation.LLIL_GOTO:
        return _find_jump_target(func, insn.dest, seen)

    # Unconditional branches.
    elif insn.operation == LowLevelILOperation.LLIL_JUMP or \
            insn.operation == LowLevelILOperation.LLIL_TAILCALL:
        if insn.dest.operation == LowLevelILOperation.LLIL_CONST or \
                insn.dest.operation == LowLevelILOperation.LLIL_CONST_PTR:
            return insn.dest.constant
        else:
            return 0

    # Jump tables.
    elif insn.operation == LowLevelILOperation.LLIL_JUMP_TO:
        return 0

    elif insn.operation == LowLevelILOperation.LLIL_CALL:
        if insn.dest.operation == LowLevelILOperation.LLIL_CONST or \
                insn.dest.operation == LowLevelILOperation.LLIL_CONST_PTR:
            return insn.dest.constant
        else:
            return 0

    elif insn.operation == LowLevelILOperation.LLIL_RET:
        return 0

    # Conditional branches.
    elif insn.operation == LowLevelILOperation.LLIL_IF:
        return max(_find_jump_target(func, insn.true, seen),
                   _find_jump_target(func, insn.false, seen))

    elif insn.operation == LowLevelILOperation.LLIL_SYSCALL:
        return 0

    # Returns.
    elif insn.operation == lowlevelil.LowLevelILOperation.LLIL_RET:
        return 0

    elif insn.operation == LowLevelILOperation.LLIL_NORET or \
            insn.operation == LowLevelILOperation.LLIL_TRAP or \
            insn.operation == LowLevelILOperation.LLIL_UNDEF:
        return 0

    else:
        return _find_jump_target(func, index + 1, seen)


class BinjaInstruction(Instruction):
    _ea: Final[int]
    _data: Final[bytes]
    _type: Final[InstructionType]
    _llil_insn: Final[lowlevelil.LowLevelILInstruction]

    def __init__(self, ea: int, data: bytes, itype: InstructionType,
                 llil_insn: lowlevelil.LowLevelILInstruction):
        self._ea = ea
        self._data = data
        self._type = itype
        self._llil_insn = llil_insn
        # print (hex(ea), len(data))

    @property
    def type(self) -> InstructionType:
        return self._type

    @property
    def ea(self) -> int:
        return self._ea

    @property
    def size(self) -> int:
        return len(self._data)

    @property
    def data(self) -> Union[bytes, bytearray]:
        return self._data

    @property
    def target_ea(self) -> Optional[int]:
        """Get the target of a direct branch (direct jump, direct call,
        taken target of a conditional branch)."""
        if self._type & ControlFlowBehavior.HAS_DIRECT_TARGET:
            return _find_jump_target(self._llil_insn.function, 0, set())
        else:
            return None

    @property
    def fall_through_ea(self) -> Optional[int]:
        if self._type & ControlFlowBehavior.HAS_FALL_THROUGH:
            return self.next_ea
        else:
            return None

    def visit_operands(self, visitor: InstructionOperandVisitor):
        for i, op in enumerate(self._llil_insn.operands):
            if not isinstance(op, LowLevelILInstruction) or \
                    op.operation != LowLevelILOperation.LLIL_LOAD:
                continue

            if op.src.operation == LowLevelILOperation.LLIL_CONST or \
                    op.src.operation == LowLevelILOperation.LLIL_CONST_PTR:
                visitor.visit_address_operand(self, i, op.src.constant)


class BinjaInstructionDecoder(InstructionDecoder):
    def __init__(self, arch_name: ArchName):
        InstructionDecoder.__init__(self, arch_name)
        self._bn = _BINJA_ARCH_MODE[arch_name]

    def decode_instruction(self, ea: int, data: Union[bytes, bytearray]) -> \
            Optional[Instruction]:

        insn: LowLevelILInstruction = \
            self._bn.get_low_level_il_from_bytes(bytes(data), ea)

        if not insn or insn.operation == LowLevelILOperation.LLIL_UNDEF:
            return None

        itype = _llil_to_itype(insn)
        info: InstructionInfo = self._bn.get_instruction_info(bytes(data), ea)
        insn_len = info.length
        if not insn_len:
            return None

        return BinjaInstruction(ea, bytes(data[:insn_len]), itype, insn)
