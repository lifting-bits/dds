# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Optional


ea_t = int


class func_t:
    start_ea: ea_t
    end_ea: ea_t


def get_func(ea: ea_t) -> Optional[func_t]:
    ...


def get_next_func(ea: ea_t) -> Optional[func_t]:
    ...