# Copyright 2021, Trail of Bits. All rights reserved.

from .parser import BinaryParser, BinaryMetadataVisitor

from typing import Iterable, Tuple

import ida_auto
import ida_bytes
import ida_entry
import ida_fixup
import ida_funcs
import ida_segment
import ida_xref
import idc


def _segments() -> Iterable[ida_segment.segment_t]:
    """Returns an iterator over all segments."""
    seg = ida_segment.get_first_seg()
    while seg:
        yield seg
        seg = ida_segment.get_next_seg(seg.start_ea)


def _is_extern_ea(ea: int) -> bool:
    """Returns `true` if `ea` is in an external segment."""
    return ida_segment.segtype(ea) == ida_segment.SEG_XTRN


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


# Tries to get the name of a symbol.
def _symbol_name(ea: int) -> bytes:
    """Returns the symbol name associated with `ea`."""
    flags = ida_bytes.get_full_flags(ea)
    if ida_bytes.has_dummy_name(flags):
        return b""

    name: bytes = b""
    try:
        name = bytes(idc.get_name(ea), encoding="utf-8")
    except:
        pass

    try:
        name = name or bytes(idc.get_func_name(ea), encoding="utf-8")
    except:
        pass

    return name


def _entrypoints() -> Iterable[int]:
    """Returns an iterator of entrypoints into the binary."""
    i, n = 0, ida_entry.get_entry_qty()
    while i < n:
        o = ida_entry.get_entry_ordinal(i)
        ea = ida_entry.get_entry(o)
        if ea != idc.BADADDR:
            yield ea
        i += 1


def _functions() -> Iterable[ida_funcs.func_t]:
    """Returns an iterator of all functions that IDA Pro knows about."""
    ea = 0
    prev_f = ida_funcs.get_func(ea)
    if prev_f:
        yield prev_f

    while True:
        f = ida_funcs.get_next_func(ea)
        if f and f != prev_f:
            yield f
            prev_f = f
            ea = f.start_ea
        else:
            break


def _relocations() -> Iterable[Tuple[int, int, int]]:
    """Returns an iterator of all relocation tuples (from_ea, to_ea, size)."""
    from_ea = ida_fixup.get_first_fixup_ea()
    while from_ea != idc.BADADDR:
        fixup = ida_fixup.fixup_data_t()
        if not fixup.get(from_ea):
            break

        if fixup.off and fixup.off != idc.BADADDR:
            yield (from_ea, fixup.off, fixup.calc_size())

        from_ea = ida_fixup.get_next_fixup_ea(from_ea)


def _xref_generator(ea: int, get_first, get_next) -> Iterable[int]:
    """Invokes an a first and next function to generate cross-references."""
    target_ea = get_first(ea)
    while target_ea != idc.BADADDR:
        yield target_ea
        target_ea = get_next(ea, target_ea)


def _data_refs_to(ea: int) -> Iterable[int]:
    """Generate the sequence of references from data to `ea`."""
    for source_ea in _xref_generator(ea, ida_xref.get_first_dref_to,
                                     ida_xref.get_next_dref_to):
        if source_ea != idc.BADADDR:
            yield source_ea


def _read_segment_bytes(s: ida_segment.segment_t) -> bytearray:
    """Read the bytes of the segment."""
    s_size = s.size()
    data = bytearray(s_size)
    if s.type == ida_segment.SEG_BSS:
        return data

    o = 0
    while o < s_size:
        o_ea = s.start_ea + o
        o_flags = ida_bytes.get_full_flags(o_ea)
        if o_flags != 0:
            # Equivalent to `ida_bytes.has_value(flags)`.
            if o_flags & ida_bytes.FF_IVL:
                data[o] = o_flags & ida_bytes.MS_VAL
            else:
                found_bytes = ida_bytes.get_bytes(o_ea, 1)
                if found_bytes is not None:
                    if isinstance(found_bytes[0], int):
                        data[o] = found_bytes[0]
                    else:
                        data[o] = ord(found_bytes[0])
        o += 1
    return data


class IDABinaryParser(BinaryParser):
    """Parse a binary with IDA Pro, and provide a mechanism for visiting
    metadata."""

    def __init__(self, arch_name: 'ArchName', os_name: str):
        ida_auto.auto_wait()
        BinaryParser.__init__(self, arch_name, os_name)

    def visit_metadata(self, visitor: BinaryMetadataVisitor):
        entry_eas: Set[int] = set()
        for ea in _entrypoints():
            if _is_code(ea):
                entry_eas.add(ea)
                visitor.visit_entrypoint_function(ea)

        # Tell the database about each section.
        for s in _segments():
            s_name = bytes(ida_segment.get_segm_name(s), encoding="utf-8")
            visitor.visit_section(s.start_ea, s.end_ea, s_name)

        # Then tell it about each function.
        for f in _functions():
            if _is_extern_ea(f.start_ea):
                visitor.visit_imported_function(
                    f.start_ea, _symbol_name(f.start_ea))

            elif f.start_ea in entry_eas:
                visitor.visit_exported_symbol(
                    f.start_ea, _symbol_name(f.start_ea))

            else:
                visitor.visit_local_function(
                    f.start_ea, _symbol_name(f.start_ea) or None)

        # All relocations. These help with de-thunking.
        for (r_ea, r_target_ea, r_size) in _relocations():
            visitor.visit_relocation(r_ea, r_target_ea, r_size)

        # TODO(pag): Add data symbols.

        for s in _segments():
            is_executable = (s.type == ida_segment.SEG_CODE) or \
                            ((s.perm & ida_segment.SEGPERM_EXEC) != 0)
            is_writable = (s.perm & ida_segment.SEGPERM_WRITE) != 0
            data = _read_segment_bytes(s)
            visitor.visit_memory(s.start_ea, data, is_writable, is_executable)

