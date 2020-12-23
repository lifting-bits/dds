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

        self.table_0: DefaultDict[int, int] = defaultdict(int)

        self.table_2: DefaultDict[int, int] = defaultdict(int)

        self.table_4: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_36: DefaultDict[bytes, List[int]] = defaultdict(list)

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

    _HAS_MERGE_METHOD_personality: Final[bool] = hasattr(int, 'merge_into')
    _MERGE_METHOD_personality: Final[Callable[[int, int], None]] = getattr(int, 'merge_into', lambda a, b: None)

    def _resolve_personality(self, obj: int) -> int:
        if Database._HAS_MERGE_METHOD_personality:
            ref_list = self._refs[hash(obj)]
            for maybe_obj in ref_list:
                if obj is maybe_obj:
                    return obj
                elif obj == maybe_obj:
                    prior_obj: int = cast(int, maybe_obj)
                    Database._MERGE_METHOD_personality(obj, prior_obj)
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
            prev_state = self.table_0[tuple_19]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_0[tuple_19] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_18 = var_18
            prev_state = self.table_2[tuple_18]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_2[tuple_18] = 1 | 4
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
                    prev_state = self.table_4[tuple_22_25]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_4[tuple_22_25] = 1 | 4
                        if not present_bit:
                            self.index_36[tuple_22_25[0]].append(tuple_22_25[1])
        # Program VectorClear Region
        del vec_20[:]
        vec_index20 = 0
        # Program Return Region
        return False

    def decoded_instruction_4(self, vec_27: List[Tuple[bytes, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index27: int = 0
        vec_32: List[bytes] = list()
        vec_index32: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index27 = 0
        while vec_index27 < len(vec_27):
            var_28, var_29, var_30, var_31 = vec_27[vec_index27]
            vec_index27 += 1
            # Program TransitionState Region
            tuple_28_30 = (var_28, var_30)
            prev_state = self.table_9[tuple_28_30]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_9[tuple_28_30] = 1 | 4
                if not present_bit:
                    self.index_23[tuple_28_30[0]].append(tuple_28_30[1])
                # Program VectorAppend Region
                vec_32.append(var_28)
        # Program VectorUnique Region
        vec_32 = list(set(vec_32))
        vec_index32 = 0
        # Program TableJoin Region
        while vec_index32 < len(vec_32):
            var_34 = vec_32[vec_index32]
            vec_index32 += 1
            tuple_33_0_index: int = 0
            tuple_33_0_vec: List[int] = self.index_23[var_34]
            while tuple_33_0_index < len(tuple_33_0_vec):
                tuple_33_0 = tuple_33_0_vec[tuple_33_0_index]
                tuple_33_0_index += 1
                var_35 = tuple_33_0
                if var_34 in self.index_24:
                    # Program TransitionState Region
                    tuple_34_35 = (var_34, var_35)
                    prev_state = self.table_4[tuple_34_35]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_4[tuple_34_35] = 1 | 4
                        if not present_bit:
                            self.index_36[tuple_34_35[0]].append(tuple_34_35[1])
        # Program VectorClear Region
        del vec_32[:]
        vec_index32 = 0
        # Program Return Region
        return False

    def get_section_ends_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_0:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_0[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_section_starts_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_2:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_2[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def instructions_from_section_name_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_36[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_4[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_section_names_f(self) -> Iterator[bytes]:
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

