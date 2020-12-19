# Auto-generated file

from __future__ import annotations
import sys
from collections import defaultdict, namedtuple
from typing import Callable, cast, DefaultDict, Final, Iterator, List, NamedTuple, Optional, Sequence, Set, Tuple, Union
try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol #type: ignore

class DatabaseFunctors:
    pass
class DatabaseLog:
    pass

from capstone import CsInsn

class Database:

    def __init__(self, log: DatabaseLog, functors: DatabaseFunctors):
        self._log: DatabaseLog = log
        self._functors: DatabaseFunctors = functors
        self._refs: DefaultDict[int, List[object]] = defaultdict(list)

        self.table_0: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_35: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_3: DefaultDict[int, int] = defaultdict(int)

        self.table_5: DefaultDict[int, int] = defaultdict(int)

        self.table_7: DefaultDict[bytes, int] = defaultdict(int)

        self.table_9: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_23: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_12: DefaultDict[bytes, int] = defaultdict(int)
        self.index_24 = self.table_12

        self.init_14_()

    _HAS_MERGE_METHOD_instruction: Final[bool] = hasattr(CsInsn, 'merge_into')
    _MERGE_METHOD_instruction: Final[Callable[[CsInsn, CsInsn], None]] = getattr(CsInsn, 'merge_into', lambda a, b: None)

    def _resolve_instruction(self, obj: CsInsn) -> CsInsn:
        if Database._HAS_MERGE_METHOD_instruction:
            ref_list = self._refs[hash(obj)]
            for maybe_obj in ref_list:
                if obj is maybe_obj:
                    return obj
                elif obj == maybe_obj:
                    prior_obj: CsInsn = cast(CsInsn, maybe_obj)
                    Database._MERGE_METHOD_instruction(obj, prior_obj)
                    return prior_obj
            ref_list.append(obj)
        return obj

    def init_14_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False

    def section_3(self, vec_16: List[Tuple[bytes, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index16: int = 0
        vec_20: List[bytes] = list()
        vec_index20: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index16 = 0
        while vec_index16 < len(vec_16):
            var_17, var_18, var_19 = vec_16[vec_index16]
            vec_index16 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_17 = var_17
            prev_state = self.table_12[tuple_17]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_12[tuple_17] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_20.append(var_17)
            # Program TransitionState Region
            tuple_19 = var_19
            prev_state = self.table_3[tuple_19]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_3[tuple_19] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_18 = var_18
            prev_state = self.table_5[tuple_18]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_5[tuple_18] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_17 = var_17
            prev_state = self.table_7[tuple_17]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_7[tuple_17] = 1 | 4
                if not present_bit:
                    pass
        # Program VectorUnique Region
        vec_20 = list(set(vec_20))
        vec_index20 = 0
        # Program TableJoin Region
        while vec_index20 < len(vec_20):
            var_22 = vec_20[vec_index20]
            vec_index20 += 1
            tuple_21_0_index: int = 0
            tuple_21_0_vec: List[int] = self.index_23[var_22]
            while tuple_21_0_index < len(tuple_21_0_vec):
                tuple_21_0 = tuple_21_0_vec[tuple_21_0_index]
                tuple_21_0_index += 1
                var_25 = tuple_21_0
                if var_22 in self.index_24:
                    # Program TransitionState Region
                    tuple_22_25 = (var_22, var_25)
                    prev_state = self.table_0[tuple_22_25]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_0[tuple_22_25] = 1 | 4
                        if not present_bit:
                            self.index_35[tuple_22_25[0]].append(tuple_22_25[1])
        # Program VectorClear Region
        del vec_20[:]
        vec_index20 = 0
        # Program Return Region
        return False

    def dec_instruction_3(self, vec_27: List[Tuple[bytes, int, CsInsn]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index27: int = 0
        vec_31: List[bytes] = list()
        vec_index31: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index27 = 0
        while vec_index27 < len(vec_27):
            var_28, var_29, var_30 = vec_27[vec_index27]
            vec_index27 += 1
            # Program TransitionState Region
            tuple_28_29 = (var_28, var_29)
            prev_state = self.table_9[tuple_28_29]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_9[tuple_28_29] = 1 | 4
                if not present_bit:
                    self.index_23[tuple_28_29[0]].append(tuple_28_29[1])
                # Program VectorAppend Region
                vec_31.append(var_28)
        # Program VectorUnique Region
        vec_31 = list(set(vec_31))
        vec_index31 = 0
        # Program TableJoin Region
        while vec_index31 < len(vec_31):
            var_33 = vec_31[vec_index31]
            vec_index31 += 1
            tuple_32_0_index: int = 0
            tuple_32_0_vec: List[int] = self.index_23[var_33]
            while tuple_32_0_index < len(tuple_32_0_vec):
                tuple_32_0 = tuple_32_0_vec[tuple_32_0_index]
                tuple_32_0_index += 1
                var_34 = tuple_32_0
                if var_33 in self.index_24:
                    # Program TransitionState Region
                    tuple_33_34 = (var_33, var_34)
                    prev_state = self.table_0[tuple_33_34]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_0[tuple_33_34] = 1 | 4
                        if not present_bit:
                            self.index_35[tuple_33_34[0]].append(tuple_33_34[1])
        # Program VectorClear Region
        del vec_31[:]
        vec_index31 = 0
        # Program Return Region
        return False

    def get_sec_insns_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_35[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_0[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_sec_ends_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_3:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_3[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_sec_starts_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_5:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_5[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_sec_names_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_7:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_7[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

