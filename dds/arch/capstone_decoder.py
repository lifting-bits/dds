# Copyright 2020, Trail of Bits. All rights reserved.

from abc import ABC
from typing import Dict, Final, Callable, Iterable, Optional, Union
import capstone
import capstone.x86

from .name import ArchName
from .decoder import InstructionDecoder
from .instruction import \
    ControlFlowBehavior, \
    Instruction, \
    InstructionOperandVisitor, \
    InstructionType

_CAPSTONE_ARCH_MODE: Final[Dict[ArchName, int]] = {
    ArchName.X86: capstone.CS_MODE_32,
    ArchName.X86_AVX: capstone.CS_MODE_32,
    ArchName.X86_AVX512: capstone.CS_MODE_32,
    ArchName.AMD64: capstone.CS_MODE_64,
    ArchName.AMD64_AVX: capstone.CS_MODE_64,
    ArchName.AMD64_AVX512: capstone.CS_MODE_64,
    ArchName.AARCH32: capstone.CS_MODE_32,
    ArchName.AARCH64: capstone.CS_MODE_64,
    ArchName.SPARC32: capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN,
    ArchName.SPARC64: capstone.CS_MODE_64 | capstone.CS_MODE_BIG_ENDIAN | \
                      capstone.CS_MODE_V9
}

_CAPSTONE_ARCH_NAME: Final[Dict[ArchName, int]] = {
    ArchName.X86: capstone.CS_ARCH_X86,
    ArchName.X86_AVX: capstone.CS_ARCH_X86,
    ArchName.X86_AVX512: capstone.CS_ARCH_X86,
    ArchName.AMD64: capstone.CS_ARCH_X86,
    ArchName.AMD64_AVX: capstone.CS_ARCH_X86,
    ArchName.AMD64_AVX512: capstone.CS_ARCH_X86,
    ArchName.AARCH32: capstone.CS_ARCH_ARM,
    ArchName.AARCH64: capstone.CS_ARCH_ARM64,
    ArchName.SPARC32: capstone.CS_ARCH_SPARC,
    ArchName.SPARC64: capstone.CS_ARCH_SPARC,
}


class CapstoneInstruction(Instruction, ABC):
    def __init__(self, cs_insn: capstone.CsInsn):
        self._cs_insn: Final[capstone.CsInsn] = cs_insn

    @property
    def ea(self) -> int:
        return self._cs_insn.address

    @property
    def size(self) -> int:
        return self._cs_insn.size

    @property
    def data(self) -> Union[bytes, bytearray]:
        return self._cs_insn.bytes

    @property
    def assembly(self) -> str:
        return "{} {}".format(self._cs_insn.mnemonic, self._cs_insn.op_str)


def _x86_decode_other(insn: capstone.CsInsn) -> InstructionType:
    return InstructionType.NORMAL


def _x86_decode_call(insn: capstone.CsInsn) -> InstructionType:
    op0 = insn.operands[0]
    if op0.type == capstone.x86.X86_OP_IMM:
        return InstructionType.DIRECT_FUNCTION_CALL
    else:
        return InstructionType.INDIRECT_FUNCTION_CALL


def _x86_decode_jmp(insn: capstone.CsInsn) -> InstructionType:
    op0 = insn.operands[0]
    if op0.type == capstone.x86.X86_OP_IMM:
        return InstructionType.DIRECT_JUMP
    else:
        return InstructionType.INDIRECT_JUMP


def _x86_decode_ret(insn: capstone.CsInsn) -> InstructionType:
    return InstructionType.FUNCTION_RETURN


def _x86_decode_jcc(insn: capstone.CsInsn) -> InstructionType:
    return InstructionType.CONDITIONAL_DIRECT_JUMP


def _x86_decode_error(insn: capstone.CsInsn) -> InstructionType:
    return InstructionType.ERROR


_X86_OP_TO_TYPE_DECODER: Final = {
    capstone.x86.X86_INS_CALL: _x86_decode_call,
    capstone.x86.X86_INS_RET: _x86_decode_ret,
    capstone.x86.X86_INS_RETF: _x86_decode_ret,
    capstone.x86.X86_INS_RETFQ: _x86_decode_ret,
    capstone.x86.X86_INS_JMP: _x86_decode_jmp,
    # TODO(pag): xabort?
    capstone.x86.X86_INS_XBEGIN: _x86_decode_jcc,
    capstone.x86.X86_INS_JAE: _x86_decode_jcc,
    capstone.x86.X86_INS_JA: _x86_decode_jcc,
    capstone.x86.X86_INS_JBE: _x86_decode_jcc,
    capstone.x86.X86_INS_JB: _x86_decode_jcc,
    capstone.x86.X86_INS_JCXZ: _x86_decode_jcc,
    capstone.x86.X86_INS_JECXZ: _x86_decode_jcc,
    capstone.x86.X86_INS_JE: _x86_decode_jcc,
    capstone.x86.X86_INS_JGE: _x86_decode_jcc,
    capstone.x86.X86_INS_JG: _x86_decode_jcc,
    capstone.x86.X86_INS_JLE: _x86_decode_jcc,
    capstone.x86.X86_INS_JL: _x86_decode_jcc,
    capstone.x86.X86_INS_JNE: _x86_decode_jcc,
    capstone.x86.X86_INS_JNO: _x86_decode_jcc,
    capstone.x86.X86_INS_JNP: _x86_decode_jcc,
    capstone.x86.X86_INS_JNS: _x86_decode_jcc,
    capstone.x86.X86_INS_JO: _x86_decode_jcc,
    capstone.x86.X86_INS_JP: _x86_decode_jcc,
    capstone.x86.X86_INS_JRCXZ: _x86_decode_jcc,
    capstone.x86.X86_INS_JS: _x86_decode_jcc,
    capstone.x86.X86_INS_HLT: _x86_decode_error,
    capstone.x86.X86_INS_UD0: _x86_decode_error,
    capstone.x86.X86_INS_UD2: _x86_decode_error,
    capstone.x86.X86_INS_UD2B: _x86_decode_error,
    capstone.x86.X86_INS_INT: _x86_decode_error,
    capstone.x86.X86_INS_INT1: _x86_decode_error,
    capstone.x86.X86_INS_INT3: _x86_decode_error,
    capstone.x86.X86_INS_INTO: _x86_decode_error,
}


class CapstoneX86Instruction(CapstoneInstruction):
    def __init__(self, insn: capstone.CsInsn):
        CapstoneInstruction.__init__(self, insn)
        d = _X86_OP_TO_TYPE_DECODER.get(insn.id, _x86_decode_other)
        self._type: Final[InstructionType] = d(insn)

    @property
    def fall_through_ea(self) -> Optional[int]:
        if self._type & ControlFlowBehavior.HAS_FALL_THROUGH:
            return self.next_ea
        else:
            return None

    @property
    def target_ea(self) -> Optional[int]:
        if self._type & ControlFlowBehavior.HAS_DIRECT_TARGET:
            return self._cs_insn.operands[0].imm

    @property
    def type(self) -> InstructionType:
        return self._type

    def visit_operands(self, visitor: InstructionOperandVisitor):
        for i, op in enumerate(self._cs_insn.operands):
            if op.type == capstone.x86.X86_OP_MEM:
                m = op.mem
                # TODO(pag): Handle pseudo RIZ register?
                if m.base == capstone.x86.X86_REG_RIP:
                    if not m.index and not m.segment:
                        visitor.visit_address_operand(i, self.ea + m.disp)
                elif not m.base and not m.index and not m.segment:
                    visitor.visit_address_operand(i, m.disp)


class CapstoneAArch32Instruction(CapstoneInstruction, ABC):
    pass


class CapstoneAArch64Instruction(CapstoneInstruction, ABC):
    pass


class CapstoneSparc32Instruction(CapstoneInstruction, ABC):
    pass


class CapstoneSparc64Instruction(CapstoneInstruction, ABC):
    pass


_CAPSTONE_ARCH_INSTRUCTION: Final = {
    ArchName.X86: CapstoneX86Instruction,
    ArchName.X86_AVX: CapstoneX86Instruction,
    ArchName.X86_AVX512: CapstoneX86Instruction,
    ArchName.AMD64: CapstoneX86Instruction,
    ArchName.AMD64_AVX: CapstoneX86Instruction,
    ArchName.AMD64_AVX512: CapstoneX86Instruction,
    ArchName.AARCH32: CapstoneAArch32Instruction,
    ArchName.AARCH64: CapstoneAArch64Instruction,
    ArchName.SPARC32: CapstoneSparc32Instruction,
    ArchName.SPARC64: CapstoneSparc64Instruction
}


class CapstoneInstructionDecoder(InstructionDecoder):
    """Capstone implementation of an instruction decoder."""

    def __init__(self, arch_name: ArchName):
        InstructionDecoder.__init__(self, arch_name)
        cs_mode = _CAPSTONE_ARCH_MODE[arch_name]
        cs_arch_name = _CAPSTONE_ARCH_NAME[arch_name]
        self._cs = capstone.Cs(cs_arch_name, cs_mode)
        self._cs.detail = True
        self._cs.syntax = capstone.CS_OPT_SYNTAX_DEFAULT
        self._cs.skipdata = True

    def decode_instruction(self, ea: int, data: Union[bytes, bytearray]) \
            -> Optional[Instruction]:
        """Decode one instruction in `data`, interpreting it to start at address
        `ea`. Returns the decoded instruction, or `None`."""
        for i in self._cs.disasm(data, ea):
            if i.mnemonic == ".byte":
                return None
            return _CAPSTONE_ARCH_INSTRUCTION[self.arch](i)
        return None
