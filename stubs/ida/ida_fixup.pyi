# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Final

ea_t = int


class fixup_data_t:
    off: ea_t

    def calc_size(self) -> int:
        ...

    def get(self, ea: ea_t) -> bool:
        ...


class fixup_info_t:
    ea: ea_t
    fd: fixup_data_t


def get_first_fixup_ea() -> ea_t:
    ...

def get_next_fixup_ea(ea: ea_t) -> ea_t:
    ...

