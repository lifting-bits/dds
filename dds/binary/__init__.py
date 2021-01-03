# Copyright 2020, Trail of Bits. All rights reserved.

from typing import Optional

from .parser import BinaryParser, BinaryMetadataVisitor
from .ida import IDABinaryParser

def LIEFBinaryMetadata(arch_name: str, os_name: str, target: str) \
        -> Optional[BinaryParser]:
    """Parse the binary `target` with LIEF."""
    import lief
    parsed = lief.parse(target)
    if isinstance(parsed, lief.ELF.Binary):
        from .lief_elf import LIEFELFBinaryParser
        return LIEFELFBinaryParser(arch_name, os_name, parsed)
