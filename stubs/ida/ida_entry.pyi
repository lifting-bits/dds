# Copyright 2021, Trail of Bits. All rights reserved.

from typing import Optional

ea_t = int


def get_entry_qty() -> int:
    """Get the number of entrypoints"""
    ...

def get_entry(ord_: int) -> ea_t:
    """Get an entrypoint by its ordinal."""
    ...

def get_entry_ordinal(index: int) -> int:
    """Get the entrypoint ordinal given the index of an entrypoint."""
    ...