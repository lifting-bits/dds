# Copyright 2020, Trail of Bits. All rights reserved.

from abc import ABC, abstractmethod
from typing import Final, Optional


class BinaryMetadataVisitor:
    def visit_relocation(self, from_ea: int, to_ea: int, size: int):
        """Visit a relocation entry, applied to `size` bytes at `from_ea`,
        and pointing to `to_ea`."""
        pass

    def visit_entrypoint_function(self, ea: int):
        """Visit the entrypoint of the binary. This is something like
        `_start` or `_init` in ELF binaries."""
        pass
    
    def visit_constructor_function(self, ea: int):
        """Visit a constructor function that is defined at `ea`."""
        pass
    
    def visit_destructor_function(self, ea: int):
        """Visit a destructor function that is defined at `ea`."""
        pass
    
    def visit_imported_function(self, ea: int, name: bytes):
        """Visit a function that is imported by this binary from other binaries.
        In practice, these functions are externals."""
        pass
    
    def visit_exported_function(self, ea: int, name: bytes):
        """Visit a function that is exported by this binary to other binaries.
        For example, if this is a shared library, then this would be called
        for each symbol that the library exports to users of the library."""
        pass
    
    def visit_local_function(self, ea: int, name: Optional[bytes]):
        """Visit a named function that is neither exported nor imported."""
        pass
    
    def visit_imported_symbol(self, ea: int, name: bytes):
        """Visit a symbol that is imported by this binary from other binaries.
        In practice, these symbols are externals. There are no guarantees that
        this is code or data."""
        pass
    
    def visit_exported_symbol(self, ea: int, name: bytes):
        """Visit a symbol that is exported by this binary to other binaries.
        For example, if this is a shared library, then this would be called
        for each symbol that the library exports to users of the library.
        There are no guarantees that this is code or data."""
        pass
    
    def visit_local_symbol(self, ea: int, name: Optional[bytes]):
        """Visit a named symbol that is neither exported nor imported. A local
        symbol is not necessarily the head of a logical entity. For example,
        it could point inside the middle of a logical entity."""
        pass

    def visit_section(self, begin_ea: int, end_ea: int, name: bytes):
        """Visit a named section `[begin_ea, end_ea)`."""
        pass

    def visit_memory(self, ea: int, data: bytes, is_writable: bool,
                     is_executable: bool):
        """Visit a range of mapped memory in the range `[ea, ea + len(data))`.
        The memory is readable, and is executable is `is_executable == True`
        and writeable if `is_writeable == True`."""
        pass


class BinaryParser(ABC):

    ADDRESS_SIZE_BITS = {
        "x86": 32,
        "x86_avx": 32,
        "x86_avx512": 32,
        "amd64": 64,
        "amd64_avx": 64,
        "amd64_avx512": 64,
        "aarch32": 32,
        "aarch64": 64,
        "sparc32": 32,
        "sparc64": 64
    }

    def __init__(self, arch_name: str, os_name: str):
        self.arch: Final[str] = arch_name
        self.os: Final[str] = os_name
        self.address_size_bits: Final[int] = self.ADDRESS_SIZE_BITS[arch_name]
        self.address_size: Final[int] = self.address_size_bits // 8

    @abstractmethod
    def visit_metadata(self, visitor: BinaryMetadataVisitor):
        ...