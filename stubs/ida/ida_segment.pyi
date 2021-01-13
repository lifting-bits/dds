# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Optional


ea_t = int
segment_t_type: int
segment_t_perm: int

SEG_NORM: Final[segment_t_type] = 0
SEG_XTRN: Final[segment_t_type] = 1
SEG_CODE: Final[segment_t_type] = 2
SEG_DATA: Final[segment_t_type] = 3
SEG_IMP: Final[segment_t_type] = 4
# TODO(pag): What has value `5`?
SEG_GRP: Final[segment_t_type] = 6  # TODO(pag): A group of segments; think about these...
SEG_NULL: Final[segment_t_type] = 7
SEG_UNDF: Final[segment_t_type] = 8
SEG_BSS: Final[segment_t_type] = 9
SEG_ABSSYM: Final[segment_t_type] = 10  # Absolute symbol defs.
SEG_COMM: Final[segment_t_type] = 11  # Communal symbol defs.
SEG_IMEM: Final[segment_t_type] = 12


SEGPERM_EXEC: Final[segment_t_perm] = 1
SEGPERM_WRITE: Final[segment_t_perm] = 2
SEGPERM_READ: Final[segment_t_perm] = 4

class segment_t:
    start_ea: ea_t
    end_ea: ea_t
    type: segment_t_type
    perm: segment_t_perm

    def size(self) -> int:
        ...


def segtype(ea: ea_t) -> segment_t_type:
    ...


def get_first_seg() -> segment_t:
    ...


def get_next_seg(ea: ea_t) -> Optional[segment_t]:
    ...


def get_segm_name(seg: segment_t, flags=0) -> str:
    ...

def getseg(ea: ea_t) -> Optional[segment_t]:
    ...
