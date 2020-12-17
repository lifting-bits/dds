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

        self.table_0: DefaultDict[Tuple[int, bytes], int] = defaultdict(int)
        self.index_46: DefaultDict[int, List[bytes]] = defaultdict(list)
        self.index_47: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_3: DefaultDict[bytes, int] = defaultdict(int)

        self.table_5: DefaultDict[int, int] = defaultdict(int)
        self.index_29 = self.table_5

        self.table_7: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_30: DefaultDict[int, List[bytes]] = defaultdict(list)

        self.table_10: DefaultDict[Tuple[bytes, int, int], int] = defaultdict(int)

        self.init_14_()

    _HAS_MERGE_METHOD_Instruction: Final[bool] = hasattr(CsInsn, 'merge_into')
    _MERGE_METHOD_Instruction: Final[Callable[[CsInsn, CsInsn], None]] = getattr(CsInsn, 'merge_into', lambda a, b: None)

    def _resolve_Instruction(self, obj: CsInsn) -> CsInsn:
        if Database._HAS_MERGE_METHOD_Instruction:
            ref_list = self._refs[hash(obj)]
            for maybe_obj in ref_list:
                if obj is maybe_obj:
                    return obj
                elif obj == maybe_obj:
                    prior_obj: CsInsn = cast(CsInsn, maybe_obj)
                    Database._MERGE_METHOD_Instruction(obj, prior_obj)
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
        vec_20: List[Tuple[bytes, int, int]] = list()
        vec_index20: int = 0
        vec_21: List[int] = list()
        vec_index21: int = 0
        vec_26: List[int] = list()
        vec_index26: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index16 = 0
        while vec_index16 < len(vec_16):
            var_17, var_18, var_19 = vec_16[vec_index16]
            vec_index16 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_17_18_19 = (var_17, var_18, var_19)
            prev_state = self.table_10[tuple_17_18_19]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_10[tuple_17_18_19] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_17_18 = (var_17, var_18)
                prev_state = self.table_7[tuple_17_18]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_7[tuple_17_18] = 1 | 4
                    if not present_bit:
                        self.index_30[tuple_17_18[1]].append(tuple_17_18[0])
                    # Program VectorAppend Region
                    vec_26.append(var_18)
                # Program VectorAppend Region
                vec_20.append((var_17, var_18, var_19))
                # Program TransitionState Region
                tuple_17 = var_17
                prev_state = self.table_3[tuple_17]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_3[tuple_17] = 1 | 4
                    if not present_bit:
                        pass
            # Program TransitionState Region
            tuple_17_18_19 = (var_17, var_18, var_19)
            prev_state = self.table_10[tuple_17_18_19]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_10[tuple_17_18_19] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_17_18 = (var_17, var_18)
                prev_state = self.table_7[tuple_17_18]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_7[tuple_17_18] = 1 | 4
                    if not present_bit:
                        self.index_30[tuple_17_18[1]].append(tuple_17_18[0])
                    # Program VectorAppend Region
                    vec_26.append(var_18)
                # Program VectorAppend Region
                vec_20.append((var_17, var_18, var_19))
                # Program TransitionState Region
                tuple_17 = var_17
                prev_state = self.table_3[tuple_17]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_3[tuple_17] = 1 | 4
                    if not present_bit:
                        pass
            # Program TransitionState Region
            tuple_17_18_19 = (var_17, var_18, var_19)
            prev_state = self.table_10[tuple_17_18_19]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_10[tuple_17_18_19] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_17_18 = (var_17, var_18)
                prev_state = self.table_7[tuple_17_18]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_7[tuple_17_18] = 1 | 4
                    if not present_bit:
                        self.index_30[tuple_17_18[1]].append(tuple_17_18[0])
                    # Program VectorAppend Region
                    vec_26.append(var_18)
                # Program VectorAppend Region
                vec_20.append((var_17, var_18, var_19))
                # Program TransitionState Region
                tuple_17 = var_17
                prev_state = self.table_3[tuple_17]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_3[tuple_17] = 1 | 4
                    if not present_bit:
                        pass
        # Program VectorUnique Region
        vec_20 = list(set(vec_20))
        vec_index20 = 0
        # Program TableProduct Region
        pass  # TODO(ekilmer): ProgramTableProductRegion
        # Program VectorClear Region
        del vec_20[:]
        vec_index20 = 0
        # Program VectorUnique Region
        vec_26 = list(set(vec_26))
        vec_index26 = 0
        # Program TableJoin Region
        while vec_index26 < len(vec_26):
            var_28 = vec_26[vec_index26]
            vec_index26 += 1
            if var_28 in self.index_29:
                tuple_27_1_index: int = 0
                tuple_27_1_vec: List[bytes] = self.index_30[var_28]
                while tuple_27_1_index < len(tuple_27_1_vec):
                    tuple_27_1 = tuple_27_1_vec[tuple_27_1_index]
                    tuple_27_1_index += 1
                    var_31 = tuple_27_1
                    # Program TransitionState Region
                    tuple_28_31 = (var_28, var_31)
                    prev_state = self.table_0[tuple_28_31]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_0[tuple_28_31] = 1 | 4
                        if not present_bit:
                            self.index_46[tuple_28_31[0]].append(tuple_28_31[1])
                            self.index_47[tuple_28_31[1]].append(tuple_28_31[0])
        # Program VectorClear Region
        del vec_26[:]
        vec_index26 = 0
        # Program Return Region
        return False

    def decoded_instruction_2(self, vec_33: List[Tuple[int, CsInsn]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index33: int = 0
        vec_36: List[int] = list()
        vec_index36: int = 0
        vec_38: List[Tuple[bytes, int, int]] = list()
        vec_index38: int = 0
        vec_42: List[int] = list()
        vec_index42: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index33 = 0
        while vec_index33 < len(vec_33):
            var_34, var_35 = vec_33[vec_index33]
            vec_index33 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_34 = var_34
            prev_state = self.table_5[tuple_34]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_5[tuple_34] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_42.append(var_34)
                # Program VectorAppend Region
                vec_36.append(var_34)
            # Program TransitionState Region
            tuple_34 = var_34
            prev_state = self.table_5[tuple_34]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_5[tuple_34] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_42.append(var_34)
                # Program VectorAppend Region
                vec_36.append(var_34)
        # Program VectorUnique Region
        vec_36 = list(set(vec_36))
        vec_index36 = 0
        # Program TableProduct Region
        pass  # TODO(ekilmer): ProgramTableProductRegion
        # Program VectorClear Region
        del vec_36[:]
        vec_index36 = 0
        # Program VectorUnique Region
        vec_42 = list(set(vec_42))
        vec_index42 = 0
        # Program TableJoin Region
        while vec_index42 < len(vec_42):
            var_44 = vec_42[vec_index42]
            vec_index42 += 1
            if var_44 in self.index_29:
                tuple_43_1_index: int = 0
                tuple_43_1_vec: List[bytes] = self.index_30[var_44]
                while tuple_43_1_index < len(tuple_43_1_vec):
                    tuple_43_1 = tuple_43_1_vec[tuple_43_1_index]
                    tuple_43_1_index += 1
                    var_45 = tuple_43_1
                    # Program TransitionState Region
                    tuple_44_45 = (var_44, var_45)
                    prev_state = self.table_0[tuple_44_45]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_0[tuple_44_45] = 1 | 4
                        if not present_bit:
                            self.index_46[tuple_44_45[0]].append(tuple_44_45[1])
                            self.index_47[tuple_44_45[1]].append(tuple_44_45[0])
        # Program VectorClear Region
        del vec_42[:]
        vec_index42 = 0
        # Program Return Region
        return False

    def instruction_section_bf(self, param_0: int) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[bytes] = self.index_46[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: bytes = tuple
            full_tuple = (param_0, param_1)
            state = self.table_0[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def instruction_section_fb(self, param_1: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_47[param_1]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_0: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_0[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_section_name_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_3:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_3[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

