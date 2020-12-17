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
        self.index_48: DefaultDict[int, List[bytes]] = defaultdict(list)
        self.index_49: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_3: DefaultDict[bytes, int] = defaultdict(int)

        self.table_5: DefaultDict[int, int] = defaultdict(int)
        self.index_30 = self.table_5

        self.table_7: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_31: DefaultDict[int, List[bytes]] = defaultdict(list)

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
        vec_22: List[int] = list()
        vec_index22: int = 0
        vec_27: List[int] = list()
        vec_index27: int = 0
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
                        self.index_31[tuple_17_18[1]].append(tuple_17_18[0])
                    # Program VectorAppend Region
                    vec_27.append(var_18)
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
                        self.index_31[tuple_17_18[1]].append(tuple_17_18[0])
                    # Program VectorAppend Region
                    vec_27.append(var_18)
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
                        self.index_31[tuple_17_18[1]].append(tuple_17_18[0])
                    # Program VectorAppend Region
                    vec_27.append(var_18)
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
        vec_21: List[Tuple[int, bytes, int, int]] = []
        for var_23 in vec_22:
            for var_24, var_25, var_26 in self.table_10:
                vec_21.append((var_23, var_24, var_25, var_26))
        for var_24, var_25, var_26 in vec_20:
            for var_23 in self.table_5:
                vec_21.append((var_23, var_24, var_25, var_26))
        for var_23, var_24, var_25, var_26 in vec_21:
            # Program TupleCompare Region
            if var_25 < var_23:
                # Program TupleCompare Region
                if var_23 < var_26:
                    # Program TransitionState Region
                    tuple_23_24 = (var_23, var_24)
                    prev_state = self.table_0[tuple_23_24]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_0[tuple_23_24] = 1 | 4
                        if not present_bit:
                            self.index_48[tuple_23_24[0]].append(tuple_23_24[1])
                            self.index_49[tuple_23_24[1]].append(tuple_23_24[0])
        # Program VectorClear Region
        del vec_20[:]
        vec_index20 = 0
        # Program VectorUnique Region
        vec_27 = list(set(vec_27))
        vec_index27 = 0
        # Program TableJoin Region
        while vec_index27 < len(vec_27):
            var_29 = vec_27[vec_index27]
            vec_index27 += 1
            if var_29 in self.index_30:
                tuple_28_1_index: int = 0
                tuple_28_1_vec: List[bytes] = self.index_31[var_29]
                while tuple_28_1_index < len(tuple_28_1_vec):
                    tuple_28_1 = tuple_28_1_vec[tuple_28_1_index]
                    tuple_28_1_index += 1
                    var_32 = tuple_28_1
                    # Program TransitionState Region
                    tuple_29_32 = (var_29, var_32)
                    prev_state = self.table_0[tuple_29_32]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_0[tuple_29_32] = 1 | 4
                        if not present_bit:
                            self.index_48[tuple_29_32[0]].append(tuple_29_32[1])
                            self.index_49[tuple_29_32[1]].append(tuple_29_32[0])
        # Program VectorClear Region
        del vec_27[:]
        vec_index27 = 0
        # Program Return Region
        return False

    def decoded_instruction_2(self, vec_34: List[Tuple[int, CsInsn]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index34: int = 0
        vec_37: List[int] = list()
        vec_index37: int = 0
        vec_40: List[Tuple[bytes, int, int]] = list()
        vec_index40: int = 0
        vec_44: List[int] = list()
        vec_index44: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index34 = 0
        while vec_index34 < len(vec_34):
            var_35, var_36 = vec_34[vec_index34]
            vec_index34 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_35 = var_35
            prev_state = self.table_5[tuple_35]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_5[tuple_35] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_44.append(var_35)
                # Program VectorAppend Region
                vec_37.append(var_35)
            # Program TransitionState Region
            tuple_35 = var_35
            prev_state = self.table_5[tuple_35]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_5[tuple_35] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_44.append(var_35)
                # Program VectorAppend Region
                vec_37.append(var_35)
        # Program VectorUnique Region
        vec_37 = list(set(vec_37))
        vec_index37 = 0
        # Program TableProduct Region
        vec_38: List[Tuple[int, bytes, int, int]] = []
        for var_39 in vec_37:
            for var_41, var_42, var_43 in self.table_10:
                vec_38.append((var_39, var_41, var_42, var_43))
        for var_41, var_42, var_43 in vec_40:
            for var_39 in self.table_5:
                vec_38.append((var_39, var_41, var_42, var_43))
        for var_39, var_41, var_42, var_43 in vec_38:
            # Program TupleCompare Region
            if var_42 < var_39:
                # Program TupleCompare Region
                if var_39 < var_43:
                    # Program TransitionState Region
                    tuple_39_41 = (var_39, var_41)
                    prev_state = self.table_0[tuple_39_41]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_0[tuple_39_41] = 1 | 4
                        if not present_bit:
                            self.index_48[tuple_39_41[0]].append(tuple_39_41[1])
                            self.index_49[tuple_39_41[1]].append(tuple_39_41[0])
        # Program VectorClear Region
        del vec_37[:]
        vec_index37 = 0
        # Program VectorUnique Region
        vec_44 = list(set(vec_44))
        vec_index44 = 0
        # Program TableJoin Region
        while vec_index44 < len(vec_44):
            var_46 = vec_44[vec_index44]
            vec_index44 += 1
            if var_46 in self.index_30:
                tuple_45_1_index: int = 0
                tuple_45_1_vec: List[bytes] = self.index_31[var_46]
                while tuple_45_1_index < len(tuple_45_1_vec):
                    tuple_45_1 = tuple_45_1_vec[tuple_45_1_index]
                    tuple_45_1_index += 1
                    var_47 = tuple_45_1
                    # Program TransitionState Region
                    tuple_46_47 = (var_46, var_47)
                    prev_state = self.table_0[tuple_46_47]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_0[tuple_46_47] = 1 | 4
                        if not present_bit:
                            self.index_48[tuple_46_47[0]].append(tuple_46_47[1])
                            self.index_49[tuple_46_47[1]].append(tuple_46_47[0])
        # Program VectorClear Region
        del vec_44[:]
        vec_index44 = 0
        # Program Return Region
        return False

    def instruction_section_bf(self, param_0: int) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[bytes] = self.index_48[param_0]
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
        tuple_vec: List[int] = self.index_49[param_1]
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

