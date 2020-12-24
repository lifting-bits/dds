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

        self.table_2: DefaultDict[int, int] = defaultdict(int)

        self.table_4: DefaultDict[int, int] = defaultdict(int)

        self.table_6: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_67: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_9: DefaultDict[int, int] = defaultdict(int)

        self.table_11: DefaultDict[int, int] = defaultdict(int)

        self.table_13: DefaultDict[bytes, int] = defaultdict(int)

        self.table_15: DefaultDict[Tuple[int, bytes], int] = defaultdict(int)
        self.index_35: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_18: DefaultDict[bytes, int] = defaultdict(int)
        self.index_36 = self.table_18

        self.table_20: DefaultDict[int, int] = defaultdict(int)
        self.index_50 = self.table_20

        self.table_22: DefaultDict[int, int] = defaultdict(int)
        self.index_51 = self.table_22

        self.table_24: DefaultDict[int, int] = defaultdict(int)
        self.index_55 = self.table_24

        self.var_0: int = 4
        self.var_1: int = 1
        self.init_26_()

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

    def init_26_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False

    def section_3(self, vec_28: List[Tuple[bytes, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index28: int = 0
        vec_32: List[bytes] = list()
        vec_index32: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index28 = 0
        while vec_index28 < len(vec_28):
            var_29, var_30, var_31 = vec_28[vec_index28]
            vec_index28 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_29 = var_29
            prev_state = self.table_18[tuple_29]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_18[tuple_29] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_32.append(var_29)
            # Program TransitionState Region
            tuple_31 = var_31
            prev_state = self.table_9[tuple_31]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_9[tuple_31] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_30 = var_30
            prev_state = self.table_11[tuple_30]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_11[tuple_30] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_29 = var_29
            prev_state = self.table_13[tuple_29]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_13[tuple_29] = 1 | 4
                if not present_bit:
                    pass
        # Program VectorUnique Region
        vec_32 = list(set(vec_32))
        vec_index32 = 0
        # Program TableJoin Region
        while vec_index32 < len(vec_32):
            var_34 = vec_32[vec_index32]
            vec_index32 += 1
            tuple_33_0_index: int = 0
            tuple_33_0_vec: List[int] = self.index_35[var_34]
            while tuple_33_0_index < len(tuple_33_0_vec):
                tuple_33_0 = tuple_33_0_vec[tuple_33_0_index]
                tuple_33_0_index += 1
                var_37 = tuple_33_0
                if var_34 in self.index_36:
                    # Program TransitionState Region
                    tuple_34_37 = (var_34, var_37)
                    prev_state = self.table_6[tuple_34_37]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_34_37] = 1 | 4
                        if not present_bit:
                            self.index_67[tuple_34_37[0]].append(tuple_34_37[1])
        # Program VectorClear Region
        del vec_32[:]
        vec_index32 = 0
        # Program Return Region
        return False

    def instruction_3(self, vec_39: List[Tuple[int, int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index39: int = 0
        vec_43: List[bytes] = list()
        vec_index43: int = 0
        vec_47: List[int] = list()
        vec_index47: int = 0
        vec_52: List[int] = list()
        vec_index52: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index39 = 0
        while vec_index39 < len(vec_39):
            var_40, var_41, var_42 = vec_39[vec_index39]
            vec_index39 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_40 = var_40
            prev_state = self.table_20[tuple_40]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_20[tuple_40] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_52.append(var_40)
                # Program VectorAppend Region
                vec_47.append(var_40)
            # Program TransitionState Region
            tuple_40_42 = (var_40, var_42)
            prev_state = self.table_15[tuple_40_42]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_15[tuple_40_42] = 1 | 4
                if not present_bit:
                    self.index_35[tuple_40_42[1]].append(tuple_40_42[0])
                # Program VectorAppend Region
                vec_43.append(var_42)
            # Program TransitionState Region
            tuple_40 = var_40
            prev_state = self.table_20[tuple_40]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_20[tuple_40] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_52.append(var_40)
                # Program VectorAppend Region
                vec_47.append(var_40)
            # Program TransitionState Region
            tuple_40 = var_40
            prev_state = self.table_20[tuple_40]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_20[tuple_40] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_52.append(var_40)
                # Program VectorAppend Region
                vec_47.append(var_40)
            # Program TransitionState Region
            tuple_40 = var_40
            prev_state = self.table_20[tuple_40]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_20[tuple_40] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_52.append(var_40)
                # Program VectorAppend Region
                vec_47.append(var_40)
        # Program VectorUnique Region
        vec_43 = list(set(vec_43))
        vec_index43 = 0
        # Program TableJoin Region
        while vec_index43 < len(vec_43):
            var_45 = vec_43[vec_index43]
            vec_index43 += 1
            tuple_44_0_index: int = 0
            tuple_44_0_vec: List[int] = self.index_35[var_45]
            while tuple_44_0_index < len(tuple_44_0_vec):
                tuple_44_0 = tuple_44_0_vec[tuple_44_0_index]
                tuple_44_0_index += 1
                var_46 = tuple_44_0
                if var_45 in self.index_36:
                    # Program TransitionState Region
                    tuple_45_46 = (var_45, var_46)
                    prev_state = self.table_6[tuple_45_46]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_45_46] = 1 | 4
                        if not present_bit:
                            self.index_67[tuple_45_46[0]].append(tuple_45_46[1])
        # Program VectorClear Region
        del vec_43[:]
        vec_index43 = 0
        # Program VectorUnique Region
        vec_47 = list(set(vec_47))
        vec_index47 = 0
        # Program TableJoin Region
        while vec_index47 < len(vec_47):
            var_49 = vec_47[vec_index47]
            vec_index47 += 1
            if var_49 in self.index_50:
                if var_49 in self.index_51:
                    # Program TransitionState Region
                    tuple_49 = var_49
                    prev_state = self.table_4[tuple_49]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_4[tuple_49] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_47[:]
        vec_index47 = 0
        # Program VectorUnique Region
        vec_52 = list(set(vec_52))
        vec_index52 = 0
        # Program TableJoin Region
        while vec_index52 < len(vec_52):
            var_54 = vec_52[vec_index52]
            vec_index52 += 1
            if var_54 in self.index_50:
                if var_54 in self.index_51:
                    if var_54 in self.index_55:
                        # Program TransitionState Region
                        tuple_54 = var_54
                        prev_state = self.table_2[tuple_54]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_2[tuple_54] = 1 | 4
                            if not present_bit:
                                pass
        # Program VectorClear Region
        del vec_52[:]
        vec_index52 = 0
        # Program Return Region
        return False

    def instruction_transfer_3(self, vec_57: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index57: int = 0
        vec_61: List[int] = list()
        vec_index61: int = 0
        vec_64: List[int] = list()
        vec_index64: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index57 = 0
        while vec_index57 < len(vec_57):
            var_58, var_59, var_60 = vec_57[vec_index57]
            vec_index57 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_1 == var_60:
                # Program TransitionState Region
                tuple_59 = var_59
                prev_state = self.table_24[tuple_59]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_24[tuple_59] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_64.append(var_59)
            # Program TupleCompare Region
            if self.var_0 == var_60:
                # Program TransitionState Region
                tuple_59 = var_59
                prev_state = self.table_22[tuple_59]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_22[tuple_59] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_64.append(var_59)
                    # Program VectorAppend Region
                    vec_61.append(var_59)
            # Program TupleCompare Region
            if self.var_0 == var_60:
                # Program TransitionState Region
                tuple_59 = var_59
                prev_state = self.table_22[tuple_59]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_22[tuple_59] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_64.append(var_59)
                    # Program VectorAppend Region
                    vec_61.append(var_59)
            # Program TupleCompare Region
            if self.var_0 == var_60:
                # Program TransitionState Region
                tuple_59 = var_59
                prev_state = self.table_22[tuple_59]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_22[tuple_59] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_64.append(var_59)
                    # Program VectorAppend Region
                    vec_61.append(var_59)
            # Program TupleCompare Region
            if self.var_0 == var_60:
                # Program TransitionState Region
                tuple_59 = var_59
                prev_state = self.table_22[tuple_59]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_22[tuple_59] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_64.append(var_59)
                    # Program VectorAppend Region
                    vec_61.append(var_59)
        # Program VectorUnique Region
        vec_61 = list(set(vec_61))
        vec_index61 = 0
        # Program TableJoin Region
        while vec_index61 < len(vec_61):
            var_63 = vec_61[vec_index61]
            vec_index61 += 1
            if var_63 in self.index_50:
                if var_63 in self.index_51:
                    # Program TransitionState Region
                    tuple_63 = var_63
                    prev_state = self.table_4[tuple_63]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_4[tuple_63] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_61[:]
        vec_index61 = 0
        # Program VectorUnique Region
        vec_64 = list(set(vec_64))
        vec_index64 = 0
        # Program TableJoin Region
        while vec_index64 < len(vec_64):
            var_66 = vec_64[vec_index64]
            vec_index64 += 1
            if var_66 in self.index_50:
                if var_66 in self.index_51:
                    if var_66 in self.index_55:
                        # Program TransitionState Region
                        tuple_66 = var_66
                        prev_state = self.table_2[tuple_66]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_2[tuple_66] = 1 | 4
                            if not present_bit:
                                pass
        # Program VectorClear Region
        del vec_64[:]
        vec_index64 = 0
        # Program Return Region
        return False

    def get_tailcalled_functions_f(self) -> Iterator[int]:
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

    def get_called_functions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_4:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_4[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_section_instructions_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_67[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_6[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_extern_functions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_4:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_4[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_section_ends_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_9:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_9[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_section_starts_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_11:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_11[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_section_names_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_13:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_13[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

