# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Sequence

ea_t = int

def get_first_cref_from(ea: ea_t) -> ea_t:
    ...

def get_next_cref_from(ea: ea_t, curr: ea_t) -> ea_t:
    ...