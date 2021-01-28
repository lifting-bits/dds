# Copyright 2020, Trail of Bits. All rights reserved.

from abc import ABC, abstractmethod
from typing import Callable, Dict, Final, Optional, Union
from ..arch import ArchName


class BinaryMetadataVisitor:
    
    def visit_entrypoint_function(self, ea: int):
        """Visit the entrypoint of the binary. This is something like
        `_start` or `_init` in ELF binaries."""
        pass

    def visit_imported_function(self, ea:int, name: Optional[bytes]):
        """Functions imported to this binary. In practice, these are
        externals."""
        pass
    
    def visit_imported_variable(self, ea:int, name: Optional[bytes]):
        """Variables imported to this binary."""
        pass
    
    def visit_imported_symbol(self, ea:int, name: Optional[bytes]):
        """Unknown imported symbols. There are no guarantees this is
        either code or data."""
        pass

    def visit_exported_function(self, ea:int, name: Optional[bytes]):
        """Functions exported to other binaries."""
        pass
    
    def visit_exported_variable(self, ea:int, name: Optional[bytes]):
        """Variables exported to other binaries."""
        pass
    
    def visit_exported_symbol(self, ea:int, name: Optional[bytes]):
        """Unknown exported symbols. There are no guarantees this is
        either code or data."""
        pass

    def visit_local_function(self, ea:int, name: Optional[bytes]):
        """Functions local to this binary."""
        pass
    
    def visit_local_variable(self, ea:int, name: Optional[bytes]):
        """Variables local to this binary."""
        pass
    
    def visit_local_symbol(self, ea:int, name: Optional[bytes]):
        """Unknown local symbols. There are no guarantees this is
        either code or data."""
        pass

    def visit_relocation(self, from_ea: int, to_ea: int, size: int):
        """Visit a relocation entry, applied to `size` bytes at `from_ea`,
        and pointing to `to_ea`."""
        pass

    def visit_section(self, begin_ea: int, end_ea: int, name: bytes):
        """Visit a named section `[begin_ea, end_ea)`."""
        pass

    def visit_memory(self, ea: int, data: Union[bytes, bytearray],
                     is_writable: bool, is_executable: bool):
        """Visit a range of mapped memory in the range `[ea, ea + len(data))`.
        The memory is readable, and is executable is `is_executable == True`
        and writeable if `is_writeable == True`."""
        pass


_ADDRESS_SIZE_BITS: Final[Dict[ArchName, int]] = {
    ArchName.X86: 32,
    ArchName.X86_AVX: 32,
    ArchName.X86_AVX512: 32,
    ArchName.AMD64: 64,
    ArchName.AMD64_AVX: 64,
    ArchName.AMD64_AVX512: 64,
    ArchName.AARCH32: 32,
    ArchName.AARCH64: 64,
    ArchName.SPARC32: 32,
    ArchName.SPARC64: 64
}


class BinaryParser(ABC):

    def __init__(self, arch_name: ArchName, os_name: str):
        self.arch: Final[ArchName] = arch_name
        self.os: Final[str] = os_name
        self.address_size_bits: Final[int] = _ADDRESS_SIZE_BITS[arch_name]
        self.address_size: Final[int] = self.address_size_bits // 8

    @staticmethod
    def from_string(parser_name: str, arch_name: 'ArchName', os_name: str,
                    target: str) -> Optional['BinaryParser']:
        make_parser = binary_parser_from_string(parser_name)
        if not make_parser:
            return None
        try:
            return make_parser(arch_name, os_name, target)
        except:
            return None

    @abstractmethod
    def visit_metadata(self, visitor: BinaryMetadataVisitor):
        ...



def _lief_parser(arch_name: 'ArchName', os_name: str, target: str) \
        -> Optional[BinaryParser]:
    """Parse the binary `target` with LIEF."""
    import lief
    parsed = lief.parse(target)
    if isinstance(parsed, lief.ELF.Binary):
        from .lief_parser_elf import LIEFELFBinaryParser
        return LIEFELFBinaryParser(arch_name, os_name, parsed)
    else:
        return None


def _binja_parser(arch_name: 'ArchName', os_name: str, target: str) \
        -> Optional[BinaryParser]:
    """Parse the binary `target` with Binary Ninja."""
    import binaryninja
    from .binja_parser import BinjaBinaryParser
    parsed = binaryninja.BinaryViewType.get_view_of_file(target)
    return BinjaBinaryParser(arch_name, os_name, parsed)


def _ida_parser(arch_name: 'ArchName', os_name: str, target: str) \
        -> Optional[BinaryParser]:
    """Parse the binary `target` with IDA Pro."""
    from .ida_parser import IDABinaryParser
    return IDABinaryParser(arch_name, os_name)


def binary_parser_from_string(parser_name: str) -> Optional[Callable]:
    if parser_name == "lief":
        return _lief_parser
    elif parser_name == "binja":
        return _binja_parser
    elif parser_name == "ida":
        return _ida_parser
    else:
        return None
