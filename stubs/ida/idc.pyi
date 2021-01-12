# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Final, Sequence

ea_t = int

BADADDR: Final[ea_t] = ~0

ARGV: Sequence[str]

def get_fixup_target_off(ea: ea_t) -> ea_t:
    ...
