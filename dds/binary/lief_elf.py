# Copyright 2020, Trail of Bits. All rights reserved.

import lief
from typing import Final

from . import BinaryMetadataVisitor
from .parser import BinaryParser


class LIEFELFBinaryParser(BinaryParser):
    """ELF metadata provider, implemented via information available through
    LIEF."""

    def __init__(self, arch_name: str, os_name: str, binary: lief.ELF.Binary):
        BinaryParser.__init__(self, arch_name, os_name)
        self._binary: Final[lief.ELF.Binary] = binary

    def visit_metadata(self, visitor: BinaryMetadataVisitor):
        """Extract metadata about this ELF binary and invoke the appropriate
        methods in `visitor`."""
        visitor.visit_entrypoint_function(self._binary.entrypoint)

        # Retrieve all sections and their metadata.
        max_addr = 0
        for s in self._binary.sections:
            s_addr = s.virtual_address
            s_name = bytes(s.name, "utf-8")
            max_addr = max(s.virtual_address + s.size, max_addr)
            visitor.visit_section(s_addr, s_addr + s.size, s_name)

        extern_sec_addr = ((max_addr + (self.address_size - 1)) //
                           self.address_size) * self.address_size
        next_import_addr = extern_sec_addr
        imported_addrs = {}

        # Add `0` as a default, so that some invalid addresses get treated as
        # seen.
        seen = set([0])

        # Retrieve constructor, destructor, imported, and exported functions.
        for f in self._binary.ctor_functions:
            f_addr = f.address
            seen.add(f_addr)
            visitor.visit_constructor_function(f_addr)

        for f in self._binary.dtor_functions:
            f_addr = f.address
            seen.add(f_addr)
            visitor.visit_destructor_function(f_addr)

        for f in self._binary.exported_functions:
            f_addr = f.address
            f_name = bytes(f.name, encoding="utf-8")
            seen.add(f_addr)
            visitor.visit_exported_function(f_addr, f_name)

        # Retrieve imported, exported, and local symbols. Assign each 
        # imported symbol an addresses in our fake `.extern` section.       
        for s in self._binary.symbols:
            s_name = bytes(s.name, "utf-8")
            if not s_name or s_name in imported_addrs:
                continue
            
            if s.imported:
                s_addr = next_import_addr
                next_import_addr += self.address_size
                imported_addrs[s_name] = s_addr
                if s.is_function:
                    self._binary.add_exported_function(s_addr, s.name)
                visitor.visit_imported_symbol(s_addr, s_name)

            elif s.exported:
                s_addr = s.value
                visitor.visit_exported_symbol(s_addr, s_name)

            elif s.is_static or s.is_function or s.is_variable:
                s_addr = s.value
                visitor.visit_local_symbol(s_addr, s_name)

            seen.add(s_addr)

        for f in self._binary.imported_functions:
            f_name = bytes(f.name, encoding="utf-8")
            f_addr = imported_addrs.get(f_name, f.address)
            if f_addr not in seen:
                seen.add(f_addr)
                visitor.visit_imported_function(f_addr, f_name)

        # Retrieve local functions (i.e., functions with addresses 
        # we haven't already seen in prior symbols).
        for f in self._binary.functions:
            f_addr = f.address
            if f_addr not in seen:
                seen.add(f_addr)
                f_name = bytes(f.name, encoding="utf-8") or None
                visitor.visit_local_function(f_addr, f_name)

        # Create a fake `.extern` section.
        if next_import_addr > extern_sec_addr:
            visitor.visit_section(extern_sec_addr, next_import_addr, b".extern")

        # Process relocations.
        for r in self._binary.relocations:

            # TODO(pag, snagy): Deal with addends / augends.

            r_size = r.size // 8
            if r.symbol and r.symbol.name:
                s_name = bytes(r.symbol.name, encoding="utf-8")
                if s_name in imported_addrs:
                    s_addr = imported_addrs[s_name]
                    visitor.visit_relocation(r.address, s_addr, r_size)

        # Now that we've added in most metadata, add in the real "contents"
        # of memory, which is more likely to trigger later instruction
        # decoding.
        for s in self._binary.sections:

            # Not loaded into memory.
            if lief.ELF.SECTION_FLAGS.ALLOC not in s.flags_list:
                continue

            is_executable = lief.ELF.SECTION_FLAGS.EXECINSTR in s.flags_list
            is_writeable = lief.ELF.SECTION_FLAGS.WRITE in s.flags_list

            # TODO(pag): Visit segments?
            visitor.visit_memory(s.virtual_address, bytes(s.content),
                                 is_writeable, is_executable)
