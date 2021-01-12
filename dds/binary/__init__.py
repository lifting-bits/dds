# Copyright 2020, Trail of Bits. All rights reserved.

from typing import Callable, Optional

from .parser import BinaryParser, BinaryMetadataVisitor
from .ida import IDABinaryParser


def _lief_parser(arch_name: str, os_name: str, target: str) \
        -> Optional[BinaryParser]:
    """Parse the binary `target` with LIEF."""
    import lief
    parsed = lief.parse(target)
    if isinstance(parsed, lief.ELF.Binary):
        from .lief_elf import LIEFELFBinaryParser
        return LIEFELFBinaryParser(arch_name, os_name, parsed)
    else:
        return None


def binary_parser_from_string(parser_name: str) -> Optional[Callable]:
    if parser_name == "lief":
        return _lief_parser
    else:
        return None
