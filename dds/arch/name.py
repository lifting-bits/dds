# Copyright 2020, Trail of Bits. All rights reserved.

from enum import IntEnum
from typing import Optional


class ArchName(IntEnum):
    """Name of an architecture."""
    X86 = 0
    X86_AVX = 1
    X86_AVX512 = 2
    AMD64 = 3
    AMD64_AVX = 4
    AMD64_AVX512 = 5
    AARCH32 = 6
    AARCH64 = 7
    SPARC32 = 8
    SPARC64 = 9

    @staticmethod
    def from_string(name: str) -> Optional['ArchName']:
        return arch_from_string(name)


_ARCH_NAME_TO_ARCH = {
    "x86": ArchName.X86,
    "x86_avx": ArchName.X86_AVX,
    "x86_avx512": ArchName.X86_AVX512,
    "amd64": ArchName.AMD64,
    "amd64_avx": ArchName.AMD64_AVX,
    "amd64_avx512": ArchName.AMD64_AVX512,
    "aarch32": ArchName.AARCH32,
    "aarch64": ArchName.AARCH64,
    "sparc32": ArchName.SPARC32,
    "sparc64": ArchName.SPARC64,
}


def arch_from_string(name: str) -> Optional[ArchName]:
    return _ARCH_NAME_TO_ARCH.get(name, None)


