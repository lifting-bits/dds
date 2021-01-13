# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Final, Sequence

ea_t = int
gtn_flag_t = int

BADADDR: Final[ea_t] = ~0

ARGV: Sequence[str]

GN_LOCAL: Final[gtn_flag_t] = 0x0040

def get_fixup_target_off(ea: ea_t) -> ea_t:
    ...

def get_name(ea: ea_t, gtn_flags: gtn_flag_t = 0) -> str:
    ...

def get_func_name(ea: ea_t) -> str:
    ...

def get_segm_name(ea: ea_t) -> str:
    ...

def process_config_line(config_str: str):
    ...

def qexit(code: int):
    ...