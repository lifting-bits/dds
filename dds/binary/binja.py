# Copyright 2021, Trail of Bits. All rights reserved.

from binaryninja import *

from typing import Dict, Final, Set
from .parser import BinaryParser, BinaryMetadataVisitor


# Helper function for some of Binja's list attributes,
# which might contain sublists.
def _expand(_list):
    for i in _list:
        if isinstance(i, list):
            yield from _expand(i)
        else:
            yield i


class BinjaBinaryParser(BinaryParser):
    """Metadata provider, implemented via information available through Binary
    Ninja."""

    def __init__(self, arch_name: str, os_name: str,
                 binary: binaryview.BinaryView):
        binary.update_analysis_and_wait()
        BinaryParser.__init__(self, arch_name, os_name)
        self._binary: Final[binaryview.BinaryView] = binary

    def visit_metadata(self, visitor: BinaryMetadataVisitor):
        """Extract metadata about this binary and invoke the appropriate
        methods in `visitor`."""

        visitor.visit_entrypoint_function(self._binary.entry_point)

        # Retrieve all sections and their metadata.
        for s in self._binary.sections.values():
            s_name = bytes(s.name, "utf-8")
            visitor.visit_section(s.start, s.end, s_name)

        # Add `0` as a default, so that some invalid addresses get treated as
        # seen.
        seen: Set[int] = set([0])
        imported_addrs: Dict[bytes, int] = {}

        # Parse all symbols into imported, exported, and local symbols into
        # functions, variables, and unknowns.
        for s in _expand(self._binary.symbols.values()):  
            s_addr = s.address

            # Eliminate anything in a symbol's name that 
            # stars with '@' (i.e., '@GOT').
            s_name = bytes(s.name.split('@')[0], "utf-8")
            if not s_name or s_addr in seen:
                continue
            
            # Parse imported symbols.
            if s.type == SymbolType.ImportedFunctionSymbol \
            or s.type == SymbolType.LibraryFunctionSymbol:
                visitor.visit_imported_function(s_addr, s_name)
            elif s.type == SymbolType.ImportedDataSymbol:
                visitor.visit_imported_variable(s_addr, s_name)
            elif s.type == SymbolType.ImportAddressSymbol:
                visitor.visit_imported_symbol(s_addr, s_name)

            # Parse local (static) symbols.
            elif s.type == SymbolType.FunctionSymbol:
                visitor.visit_local_function(s_addr, s_name)
            elif s.type == SymbolType.DataSymbol:
                visitor.visit_local_variable(s_addr, s_name)

            # We omit external symbols (SymbolType.ExternalSymbol) 
            # as we parse them later into relocations.
            else:
                continue

            seen.add(s_addr)

        # Process relocations. We match each ExternalSymbol by
        # name to an ImportAddressSymbol, and then map their
        # respective addresses as a relocation.
        for r in _expand(
                self._binary.get_symbols_of_type(SymbolType.ExternalSymbol)):
            if r.name:
                s_name = bytes(r.name, "utf-8")
                if s_name in imported_addrs:
                    s_addr = imported_addrs[s_name]
                    r_size = 0  # irrelevant for Binja
                    visitor.visit_relocation(r.address, s_addr, r_size)

        # Retrieve any remaining functions not already seen
        # from the symbol table.
        for f in self._binary.functions:
            f_name = bytes(f.name, "utf-8")
            visitor.visit_local_function(f.start, f_name)

        # Finally, go through and decode the sections accordingly.
        for s in self._binary.sections.values():

            # Omit sections that have no semantics (probably 
            # indicating an erroneous section).
            if not s.semantics:
                continue

            is_executable = SectionSemantics.ReadOnlyCodeSectionSemantics == \
                            s.semantics
            is_writeable = SectionSemantics.ReadWriteDataSectionSemantics == \
                           s.semantics

            # TODO(snagy2, pag): Visit segments?
            visitor.visit_memory(s.start, self._binary.read(s.start, s.end),
                                 is_writeable, is_executable)
