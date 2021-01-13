# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Optional, Final

ea_t = int
flags_t = int

FF_IVL: Final[int] = 256
MS_VAL: Final[int] = 255

def get_full_flags(ea: ea_t) -> flags_t:
    ...

def is_code(flags: flags_t) -> bool:
    ...

def has_dummy_name(flags: flags_t) -> bool:
    ...

def get_bytes(ea: ea_t, size: int, gmb_flags: int = 0x01) -> Optional[str]:
    ...