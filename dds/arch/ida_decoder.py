# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Dict, Final, Callable, Iterable, List, Optional, Tuple, Union

import ida_allins
import ida_auto
import ida_bytes
import ida_segment
import ida_ua
import ida_xref
import idc

from .name import ArchName
from .decoder import InstructionDecoder
from .instruction import \
    Instruction, \
    InstructionOperandVisitor, \
    InstructionType


_PREFIX_TYPES: Final[Tuple[int, ...]] = (
    ida_allins.NN_lock, ida_allins.NN_rep,
    ida_allins.NN_repe, ida_allins.NN_repne)


_X86_INST_TYPES: Final[Dict[int, InstructionType]] = {
    # Near call.
    ida_allins.NN_call: InstructionType.DIRECT_FUNCTION_CALL,

    # Near call, indirect.
    ida_allins.NN_callni: InstructionType.INDIRECT_FUNCTION_CALL,

    # Far call, indiret.
    ida_allins.NN_callfi: InstructionType.INDIRECT_FUNCTION_CALL,

    # System calls, treat these as indirect procedure calls.
    ida_allins.NN_syscall: InstructionType.INDIRECT_FUNCTION_CALL,
    ida_allins.NN_sysenter: InstructionType.INDIRECT_FUNCTION_CALL,

    # Far returns. These use segment selectors.
    ida_allins.NN_retf: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_retfd: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_retfq: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_retfw: InstructionType.FUNCTION_RETURN,

    # Near returns. These are more typical procedure returns.
    ida_allins.NN_retn: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_retnd: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_retnq: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_retnw: InstructionType.FUNCTION_RETURN,

    # Near jumps. These are use for inter- and intra-procedural control flow
    # transfers.
    ida_allins.NN_jmp: InstructionType.DIRECT_JUMP,
    ida_allins.NN_jmpshort: InstructionType.DIRECT_JUMP,
    ida_allins.NN_jmpni: InstructionType.INDIRECT_JUMP,

    # Far jump. These use segment selectors.
    ida_allins.NN_jmpfi: InstructionType.INDIRECT_JUMP,

    # Error conditions.
    ida_allins.NN_int: InstructionType.ERROR,
    ida_allins.NN_into: InstructionType.CONDITIONAL_INDIRECT_JUMP,
    ida_allins.NN_int3: InstructionType.ERROR,
    ida_allins.NN_ud0: InstructionType.ERROR,
    ida_allins.NN_ud1: InstructionType.ERROR,
    ida_allins.NN_ud2: InstructionType.ERROR,
    ida_allins.NN_hlt: InstructionType.ERROR,
    ida_allins.NN_icebp: InstructionType.ERROR,

    # System return instructions; treat them as procedure returns.
    ida_allins.NN_iretw: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_iret: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_iretd: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_iretq: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_sysret: InstructionType.FUNCTION_RETURN,
    ida_allins.NN_sysexit: InstructionType.FUNCTION_RETURN,

    # Direct, conditional control flows.
    ida_allins.NN_ja: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jae: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jb: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jbe: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jc: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jcxz: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_je: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jecxz: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jg: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jge: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jl: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jle: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jna: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jnae: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jnb: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jnbe: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jnc: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jne: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jng: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jnge: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jnl: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jnle: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jno: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jnp: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jns: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jnz: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jo: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jp: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jpe: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jpo: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jrcxz: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_js: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_jz: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loop: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopd: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopde: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopdne: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loope: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopne: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopq: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopqe: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopqne: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopw: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopwe: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_loopwne: InstructionType.CONDITIONAL_DIRECT_JUMP,

    # Restricted hardware transactional memory.
    ida_allins.NN_xbegin: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.NN_xend: InstructionType.CONDITIONAL_INDIRECT_JUMP,
    ida_allins.NN_xabort: InstructionType.INDIRECT_JUMP,

    # Intel CET.
    ida_allins.NN_endbr32: InstructionType.CONDITIONAL_INDIRECT_JUMP,
    ida_allins.NN_endbr64: InstructionType.CONDITIONAL_INDIRECT_JUMP,

    # `bound` instruction, which conditionally traps.
    ida_allins.NN_bound: InstructionType.CONDITIONAL_INDIRECT_JUMP,
}


# TODO(pag): Make sure this is up-to-date with ARMv7.
_ARM_INST_TYPES: Final[Dict[int, InstructionType]] = {
    ida_allins.ARM_bl: InstructionType.DIRECT_FUNCTION_CALL,
    ida_allins.ARM_blx1: InstructionType.DIRECT_FUNCTION_CALL,
    ida_allins.ARM_blx2: InstructionType.DIRECT_FUNCTION_CALL,
    ida_allins.ARM_blr: InstructionType.INDIRECT_FUNCTION_CALL,

    ida_allins.ARM_ret: InstructionType.FUNCTION_RETURN,

    ida_allins.ARM_b: InstructionType.DIRECT_JUMP,
    ida_allins.ARM_bx: InstructionType.DIRECT_JUMP,
    ida_allins.ARM_br: InstructionType.INDIRECT_JUMP,

    ida_allins.ARM_brk: InstructionType.CONDITIONAL_INDIRECT_JUMP,
    ida_allins.ARM_bkpt: InstructionType.CONDITIONAL_INDIRECT_JUMP,

    ida_allins.ARM_svc: InstructionType.CONDITIONAL_INDIRECT_JUMP,
    ida_allins.ARM_hvc: InstructionType.CONDITIONAL_INDIRECT_JUMP,
    ida_allins.ARM_smc: InstructionType.CONDITIONAL_INDIRECT_JUMP,

    ida_allins.ARM_hlt: InstructionType.ERROR,

    ida_allins.ARM_cbnz: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.ARM_cbz: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.ARM_tbnz: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.ARM_tbz: InstructionType.CONDITIONAL_DIRECT_JUMP,
}


_SPARC_INST_TYPES: Final[Dict[int, InstructionType]] = {
    ida_allins.SPARC_call: InstructionType.DIRECT_FUNCTION_CALL,
    ida_allins.SPARC_ret: InstructionType.FUNCTION_RETURN,
    ida_allins.SPARC_retl: InstructionType.FUNCTION_RETURN,
    ida_allins.SPARC_rett: InstructionType.FUNCTION_RETURN,
    ida_allins.SPARC_return: InstructionType.FUNCTION_RETURN,
    ida_allins.SPARC_b: InstructionType.DIRECT_JUMP,  # Subject to fixing.
    ida_allins.SPARC_jmp: InstructionType.INDIRECT_JUMP,
    ida_allins.SPARC_jmpl: InstructionType.INDIRECT_JUMP,
    ida_allins.SPARC_done: InstructionType.INDIRECT_JUMP,
    ida_allins.SPARC_retry: InstructionType.INDIRECT_JUMP,
    ida_allins.SPARC_bp: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.SPARC_bpr: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.SPARC_fb: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.SPARC_fbp: InstructionType.CONDITIONAL_DIRECT_JUMP,
    ida_allins.SPARC_illtrap: InstructionType.ERROR,
}


_ITYPE_MAP: Final[Dict[ArchName, Dict]] = {
    ArchName.X86: _X86_INST_TYPES,
    ArchName.X86_AVX: _X86_INST_TYPES,
    ArchName.X86_AVX512: _X86_INST_TYPES,
    ArchName.AMD64: _X86_INST_TYPES,
    ArchName.AMD64_AVX: _X86_INST_TYPES,
    ArchName.AMD64_AVX512: _X86_INST_TYPES,
    ArchName.AARCH64: _ARM_INST_TYPES,
    ArchName.AARCH32: _ARM_INST_TYPES,
    ArchName.SPARC32: _SPARC_INST_TYPES,
    ArchName.SPARC64: _SPARC_INST_TYPES,
}


def _fix_none(insn: ida_ua.insn_t, itype: InstructionType) -> InstructionType:
    return itype


def _fix_sparc(insn: ida_ua.insn_t, itype: InstructionType) -> InstructionType:
    """Fix the instruction type on SPARC by looking at the instruction's
    operands."""
    if insn.itype == ida_allins.SPARC_b:
        if 0 <= insn.segpref <= 0xf and insn.segpref != 0x8:
            return InstructionType.CONDITIONAL_DIRECT_JUMP
    elif insn.itype == ida_allins.SPARC_bp:
        if insn.segpref == 0x8:
            return InstructionType.DIRECT_JUMP
    elif insn.itype == ida_allins.SPARC_call:
        if insn.ops[0].type == idc.o_phrase:  # Not sure why it's not `o_reg`...
            return InstructionType.INDIRECT_FUNCTION_CALL
    return itype


# TODO(pag): Make sure this is up-to-date with ARMv7.
def _fix_arm(insn: ida_ua.insn_t, itype: InstructionType) -> InstructionType:
    """For things like b.le, IDA will give us the `ARM_b` opcode, and we need
    to figure out if it's actually conditional. This is stored in the `segpref`
    field, and `0xe` is the unconditional version."""
    if insn.itype == ida_allins.ARM_b or insn.itype == ida_allins.ARM_bx:
        if 0 <= insn.segpref <= 0xf and insn.segpref != 0xe:
            return InstructionType.CONDITIONAL_DIRECT_JUMP
    return itype


_ITYPE_FIXER: Final[Dict[ArchName, Callable]] = {
    ArchName.SPARC32: _fix_sparc,
    ArchName.SPARC64: _fix_sparc,
    ArchName.AARCH32: _fix_arm,
    ArchName.AARCH64: _fix_arm,
}


def _is_code(ea: int) -> bool:
    """Returns `true` if IDA Pro thinks the data at address `ea` is code."""
    flags = ida_bytes.get_full_flags(ea)
    if ida_bytes.is_code(flags):
        return True
    s = ida_segment.getseg(ea)
    if s:
        return (s.type == ida_segment.SEG_CODE) or \
               ((s.perm & ida_segment.SEGPERM_EXEC) != 0)
    return False


def _xref_generator(ea: int, get_first, get_next) -> Iterable[int]:
    """Invokes an a first and next function to generate cross-references."""
    target_ea = get_first(ea)
    while target_ea != idc.BADADDR:
        yield target_ea
        target_ea = get_next(ea, target_ea)


def _code_refs_from(ea: int, taken_flow: bool = True,
                    predicate=_is_code) -> Iterable[int]:
    """Generate the sequence of references to code from `ea`."""

    # First, go see if there's a fixed-up relocation that is code.
    fixup_ea: int = idc.get_fixup_target_off(ea)
    if fixup_ea != idc.BADADDR and predicate(fixup_ea):
        yield fixup_ea

    # If the target wasn't fixed up as a result of a relocation, then go
    # and look for it as a cross-reference.
    first, next = ida_xref.get_first_cref_from, ida_xref.get_next_cref_from
    if not taken_flow:
        first, next = (ida_xref.get_first_fcref_from,
                       ida_xref.get_next_fcref_from)

    for target_ea in _xref_generator(ea, first, next):
        if target_ea != fixup_ea and predicate(target_ea):
            yield target_ea


class IDAInstruction(Instruction):
    """Wrapper around an instruction decoded with IDA Pro."""
    _ea: Final[int]
    _data: Final[bytes]
    _type: Final[InstructionType]
    _ida_insn: Final[ida_ua.insn_t]

    def __init__(self, ea: int, data: bytes, itype: InstructionType,
                 ida_insn: ida_ua.insn_t):
        self._ea = ea
        self._data = data
        self._type = itype
        self._ida_insn = ida_insn

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
    def data(self) -> bytes:
        return self._data

    @property
    def target_ea(self, predicate=_is_code) -> Optional[int]:
        """Get the target of a direct branch (direct jump, direct call,
        taken target of a conditional branch)."""
        accept_any = lambda x: True
        for target_ea in _code_refs_from(self.ea, predicate=accept_any):
            return target_ea

        for i, op in enumerate(self._ida_insn.ops):
            if op.addr and op.addr != idc.BADADDR:
                return op.addr

        return None

    @property
    def fall_through_ea(self) -> int:
        """In the SPARC ABI, a function call can be followed by an `illtrap`
        that is meant to signal return-value optimization, where the `illtrap`
        embeds the size of the returned object as an immediate operand."""
        next_ea = self.next_ea

        if ida_allins.SPARC_call != self._ida_insn.itype:
            return next_ea

        # Go look for the `illtrap`. Note that all instructions on SPARC are
        # four bytes (although IDA may merge two into an eight byte idiom,
        # e.g. `SET`).
        insn = ida_ua.insn_t()
        insn_len: int = ida_ua.decode_insn(insn, next_ea)
        if 4 == insn_len and insn.itype == ida_allins.SPARC_illtrap:
            return next_ea + 4
        else:
            return next_ea

    def visit_operands(self, visitor: InstructionOperandVisitor):
        for op in self._ida_insn.ops:
            if op.type == ida_ua.o_mem or op.type == ida_ua.o_near:
                visitor.visit_address_operand(self, op.n, op.addr)

            # TODO(pag): `ida_ua.o_displ` generally seems to imply the presence
            #            of a base/index register.
            elif op.type == ida_ua.o_displ:
                visitor.visit_address_operand(self, op.n, op.addr)

    @property
    def assembly(self) -> str:
        parts: List[Optional[str]] = [ida_ua.print_insn_mnem(self._ea)]
        if not parts[0]:
            return ""

        if self._ea != self._ida_insn.ea:
            parts.append(ida_ua.print_insn_mnem(self._ida_insn.ea))

        for op in self._ida_insn.ops:
            if op.type:
                o_str = ida_ua.print_operand(self._ida_insn.ea, op.n)
                if o_str:
                    parts.append("".join(c for c in o_str if c.isprintable()))

        return " ".join(s for s in parts if s)


class IDAInstructionDecoder(InstructionDecoder):
    """Implements instruction decoding via IDA Pro. Data passed in is trusted
    to be 'in the right place', as IDA Pro doesn't appear to provide a decoder
    interface that isn't tied to the loaded image."""

    def __init__(self, arch_name: ArchName):
        ida_auto.auto_wait()
        InstructionDecoder.__init__(self, arch_name)
        self._itypes = _ITYPE_MAP[arch_name]

    def decode_instruction(self, ea: int, data: bytes) -> \
            Optional[Instruction]:
        if not ida_ua.can_decode(ea):
            return None

        insn = ida_ua.insn_t()
        insn_len: int = ida_ua.decode_insn(insn, ea)
        if insn_len <= 0:
            return None

        # On x86, the `lock` prefix can show up as a separate instruction, and
        # so here we try to merge it.
        if insn.size == 1 and insn.itype in _PREFIX_TYPES and \
                ida_ua.can_decode(ea + 1):

            succ_insn = ida_ua.insn_t()
            succ_insn_len: int = ida_ua.decode_insn(insn, ea)
            if 0 < succ_insn_len and (insn_len + succ_insn_len) <= len(data):
                insn_len += succ_insn_len
                insn = succ_insn

        # Figure out the instruction type, and possible "fix it" if the IDA
        # itypes themselves don't contain sufficient info to distinguish
        # things like direct and indirect calls.
        itype_fixer = _ITYPE_FIXER.get(self.arch, _fix_none)
        itype = self._itypes.get(insn.itype, InstructionType.NORMAL)
        itype = itype_fixer(insn, itype)

        if len(data) > insn_len:
            data = data[:insn_len]
        return IDAInstruction(ea, data, itype, insn)
