# Copyright 2020, Trail of Bits. All rights reserved.

from abc import ABC, abstractmethod
from enum import IntEnum
from typing import Callable, Dict, Final, Iterable, Optional, Union

from .name import ArchName
from .instruction import Instruction

# Minimum alignment of instructions.
_MIN_INST_ALIGN: Final[Dict[ArchName, int]] = {
    ArchName.X86: 1,
    ArchName.X86_AVX: 1,
    ArchName.X86_AVX512: 1,
    ArchName.AMD64: 1,
    ArchName.AMD64_AVX: 1,
    ArchName.AMD64_AVX512: 1,
    ArchName.AARCH32: 4,
    ArchName.AARCH64: 4,
    ArchName.SPARC32: 4,
    ArchName.SPARC64: 4
}

# Minimum size of instructions.
_MIN_INST_SIZE: Final[Dict[ArchName, int]] = {
    ArchName.X86: 1,
    ArchName.X86_AVX: 1,
    ArchName.X86_AVX512: 1,
    ArchName.AMD64: 1,
    ArchName.AMD64_AVX: 1,
    ArchName.AMD64_AVX512: 1,
    ArchName.AARCH32: 4,
    ArchName.AARCH64: 4,
    ArchName.SPARC32: 4,
    ArchName.SPARC64: 4
}

# Maximum size of instructions.
_MAX_INST_SIZE: Final[Dict[ArchName, int]] = {
    ArchName.X86: 15,
    ArchName.X86_AVX: 15,
    ArchName.X86_AVX512: 15,
    ArchName.AMD64: 15,
    ArchName.AMD64_AVX: 15,
    ArchName.AMD64_AVX512: 15,
    ArchName.AARCH32: 4,
    ArchName.AARCH64: 4,
    ArchName.SPARC32: 4,
    ArchName.SPARC64: 4
}


class InstructionDecoder(ABC):
    """Abstract instruction decoder."""

    def __init__(self, arch_name: ArchName):
        self.arch: Final[ArchName] = arch_name
        self.min_instruction_align: Final[int] = _MIN_INST_ALIGN[arch_name]
        self.min_instruction_size: Final[int] = _MIN_INST_SIZE[arch_name]
        self.max_instruction_size: Final[int] = _MAX_INST_SIZE[arch_name]

    @abstractmethod
    def decode_instruction(self, ea: int, data: Union[bytes, bytearray]) \
            -> Optional[Instruction]:
        """Decode one instruction in `data`, interpreting it to start at address
        `ea`. Returns the decoded instruction, or `None`."""
        ...

    def decode_instructions(self, ea, data: Union[bytes, bytearray]) \
            -> Iterable[Instruction]:
        """Decode zero-or-more instructions in `data`, interpreting the first
        instruction as starting at address `ea`. Returns the decoded
        instruction, or `None`.

        NOTE: This will exhaustively decode all possible instructions in
        `data`."""

        i = 0
        data_len: Final[int] = len(data)
        while i < data_len:

            # Don't bother trying to decode unaligned instructions.
            if (ea + i) % self.min_instruction_align:
                i += 1
                continue

            # First, collect the minimum number of bytes needed by an
            # instruction.
            inst_data = bytearray()
            j = 0
            while j < self.min_instruction_size and (i + j) < data_len:
                inst_data.append(data[i + j])
                j += 1

            # Can't find a full instruction at `i`.
            if j != self.min_instruction_size:
                break

            # Now, try to decode the instruction. Each time we fail, try to
            # add another by to the instruction, up until the maximum
            # instruction size.
            while j <= self.max_instruction_size:
                inst = self.decode_instruction(ea + i, inst_data)
                if inst:
                    yield inst
                    break
                elif (i + j) < data_len:
                    inst_data.append(data[i + j])
                    j += 1
                else:
                    break

            # Advance to the next possible instruction head. Note that this is
            # not necessarily the logically next instruction; this will decode
            # overlapping instructions on variable-width architectures like x86.
            i += self.min_instruction_size


class InvalidInstructionDecoder(InstructionDecoder):
    """An invalid instruction decoder that always fails to decode
    instructions."""

    def decode_instruction(self, ea: int, data: Union[bytes, bytearray]) -> \
            Optional[Instruction]:
        return None


def _capstone_decoder(arch_name: ArchName) -> InstructionDecoder:
    from .capstone_decoder import CapstoneInstructionDecoder
    return CapstoneInstructionDecoder(arch_name)


def _ida_decoder(arch_name: ArchName) -> InstructionDecoder:
    from .ida_decoder import IDAInstructionDecoder
    return IDAInstructionDecoder(arch_name)


def _invalid_decoder(arch_name: ArchName) -> InstructionDecoder:
    return InvalidInstructionDecoder(arch_name)


_DECODER_MAP: Final[Dict[str, Callable]] = {
    "capstone": _capstone_decoder,
    "ida": _ida_decoder,
}


def decoder_from_string(decoder_name: str, arch_name: ArchName) \
        -> InstructionDecoder:
    return _DECODER_MAP.get(decoder_name, _invalid_decoder)(arch_name)
