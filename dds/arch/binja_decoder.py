# Copyright 2021, Trail of Bits. All rights reserved.

from abc import ABC
from typing import Dict, Final, Callable, Iterable, Optional, Union
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
    #ArchName.SPARC32: 
    #ArchName.SPARC32: 
}


# TODO(snagy2): support LLIL_JUMP_TO (jump tables); 
# not clear if it represents jump instructions?
#
# https://docs.binary.ninja/dev/bnil-llil.html
def _llil_to_itype(insn):
    """Given a Binary Ninja LLIL, extract its InstructionType."""

    if insn.operation == lowlevelil.LowLevelILOperation.LLIL_JUMP:
        if insn.dest.operation == LowLevelILOperation.LLIL_CONST \
        or insn.dest.operation == LowLevelILOperation.LLIL_CONST_PTR:
            return InstructionType.CONDITIONAL_DIRECT_JUMP
        
        elif insn.dest.operation == LowLevelILOperation.LLIL_REG:
            return InstructionType.CONDITIONAL_INDIRECT_JUMP
        
        elif insn.dest.operation == LowLevelILOperation.LLIL_LOAD:
            return InstructionType.CONDITIONAL_INDIRECT_JUMP
        
        else:
            print (insn, insn.dest.operation)
            print ("Unsupported dest operation?")
            exit(0)

    elif insn.operation == lowlevelil.LowLevelILOperation.LLIL_GOTO:
        if insn.dest.operation == LowLevelILOperation.LLIL_CONST \
        or insn.dest.operation == LowLevelILOperation.LLIL_CONST_PTR:
            return InstructionType.DIRECT_JUMP
        
        elif insn.dest.operation == LowLevelILOperation.LLIL_REG:
            return InstructionType.INDIRECT_JUMP
        
        elif insn.dest.operation == LowLevelILOperation.LLIL_LOAD:
            return InstructionType.CONDITIONAL_INDIRECT_JUMP
            
        else:
            print (insn, insn, insn.operation)
            print ("Unsupported dest operation?")
            exit(0)        

    elif insn.operation == lowlevelil.LowLevelILOperation.LLIL_CALL\
    or insn.operation == lowlevelil.LowLevelILOperation.LLIL_SYSCALL:
        if insn.dest.operation == LowLevelILOperation.LLIL_CONST \
        or insn.dest.operation == LowLevelILOperation.LLIL_CONST_PTR:
            return InstructionType.DIRECT_FUNCTION_CALL
        
        elif insn.dest.operation == LowLevelILOperation.LLIL_REG:
            return InstructionType.INDIRECT_FUNCTION_CALL
        
        elif insn.dest.operation == LowLevelILOperation.LLIL_LOAD:
            return InstructionType.INDIRECT_FUNCTION_CALL
        
        else:
            print (insn, insn, insn.operation)
            print ("Unsupported dest operation?")
            exit(0)        

    elif insn.operation == lowlevelil.LowLevelILOperation.LLIL_RET:
        return InstructionType.FUNCTION_RETURN

    # TODO(snagy2): Hopefully LLIL_TRAP excludes all
    # breakpoints (e.g., x86's `int3` instruction).
    elif insn.operation in [lowlevelil.LowLevelILOperation.LLIL_NORET, lowlevelil.LowLevelILOperation.LLIL_TRAP]:
        return InstructionType.ERROR

    # TODO(snagy2): Do we really want to return `ERROR`
    # for undecodable instructions? Shouldn't this be
    # distinct from halting instructions?
    elif insn.operation in [lowlevelil.LowLevelILOperation.LLIL_UNDEF, lowlevelil.LowLevelILOperation.LLIL_UNIMPL, lowlevelil.LowLevelILOperation.LLIL_UNIMPL_MEM]:
        return InstructionType.ERROR

    else:
        return InstructionType.NORMAL


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
        return None

    @property
    def fall_through_ea(self) -> Optional[int]:
        #if self._type & ControlFlowBehavior.HAS_FALL_THROUGH:
        #    return self.next_ea
        #else:
        #    return None
        return None

class BinjaInstructionDecoder(InstructionDecoder):
    def __init__(self, arch_name: ArchName):
        InstructionDecoder.__init__(self, arch_name)
        self._bn = _BINJA_ARCH_MODE[arch_name]

    
    def decode_instruction(self, ea: int, data: Union[bytes, bytearray]) -> \
            Optional[Instruction]:

        insn = self._bn.get_low_level_il_from_bytes(bytes(data), ea)
        itype = _llil_to_itype(insn)
        print (hex(ea), insn, itype)

        #exit(0)
