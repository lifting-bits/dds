# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Final

ea_t = int
flags_t = int

def get_full_flags(ea: ea_t) -> flags_t:
    ...

def is_code(flags: flags_t) -> bool:
    ...
