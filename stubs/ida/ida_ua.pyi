# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Optional, Sequence

ea_t = int
optype_t = int

o_void: Final[optype_t] = 0
o_reg: Final[optype_t] = 1
o_mem: Final[optype_t] = 2
o_phrase: Final[optype_t] = 3
o_displ: Final[optype_t] = 4
o_imm: Final[optype_t] = 5
o_far: Final[optype_t] = 6
o_near: Final[optype_t] = 7
o_idspec0: Final[optype_t] = 8
o_idspec1: Final[optype_t] = 9
o_idspec2: Final[optype_t] = 10
o_idspec3: Final[optype_t] = 11
o_idspec4: Final[optype_t] = 12
o_idspec5: Final[optype_t] = 13


class op_t:
    n: int  # Operand index.
    type: optype_t  # Operand type.
    offb: int  # Offset of operand value from the instruction start (0 means unknown).
    offo: int  # Same as offb (some operands have 2 numeric values used to form an operand).

    # Stuff that's inside unions.
    addr: ea_t


class insn_t:
    ea: ea_t
    size: int
    itype: int
    segpref: int
    ops: Sequence[op_t]


def can_decode(ea: ea_t) -> bool:
    ...

def decode_insn(insn: insn_t, ea: ea_t) -> int:
    ...

def print_insn_mnem(ea: ea_t) -> Optional[str]:
    ...

def print_operand(ea: ea_t, n: int, getn_flags: int = 0, newtype=None) -> Optional[str]:
    ...