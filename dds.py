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

        self.table_3: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_109: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_6: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_110: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_9: DefaultDict[int, int] = defaultdict(int)

        self.table_11: DefaultDict[int, int] = defaultdict(int)

        self.table_13: DefaultDict[int, int] = defaultdict(int)
        self.index_59 = self.table_13

        self.table_15: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_111: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_18: DefaultDict[bytes, int] = defaultdict(int)

        self.table_20: DefaultDict[bytes, int] = defaultdict(int)
        self.index_50 = self.table_20

        self.table_22: DefaultDict[Tuple[int, bytes], int] = defaultdict(int)
        self.index_51: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_25: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_60: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_28: DefaultDict[int, int] = defaultdict(int)
        self.index_79 = self.table_28

        self.table_30: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_80: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_33: DefaultDict[int, int] = defaultdict(int)
        self.index_85 = self.table_33

        self.table_35: DefaultDict[int, int] = defaultdict(int)
        self.index_91 = self.table_35

        self.table_37: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_86: DefaultDict[int, List[int]] = defaultdict(list)

        self.var_0: int = 5
        self.var_1: int = 4
        self.var_2: int = 0
        self.init_40_()

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

    def init_40_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False

    def section_4(self, vec_42: List[Tuple[bytes, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index42: int = 0
        vec_47: List[bytes] = list()
        vec_index47: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index42 = 0
        while vec_index42 < len(vec_42):
            var_43, var_44, var_45, var_46 = vec_42[vec_index42]
            vec_index42 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_43 = var_43
            prev_state = self.table_20[tuple_43]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_20[tuple_43] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_47.append(var_43)
            # Program TransitionState Region
            tuple_43 = var_43
            prev_state = self.table_18[tuple_43]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_18[tuple_43] = 1 | 4
                if not present_bit:
                    pass
        # Program VectorUnique Region
        vec_47 = list(set(vec_47))
        vec_index47 = 0
        # Program TableJoin Region
        while vec_index47 < len(vec_47):
            var_49 = vec_47[vec_index47]
            vec_index47 += 1
            if var_49 in self.index_50:
                tuple_48_1_index: int = 0
                tuple_48_1_vec: List[int] = self.index_51[var_49]
                while tuple_48_1_index < len(tuple_48_1_vec):
                    tuple_48_1 = tuple_48_1_vec[tuple_48_1_index]
                    tuple_48_1_index += 1
                    var_52 = tuple_48_1
                    # Program TransitionState Region
                    tuple_49_52 = (var_49, var_52)
                    prev_state = self.table_6[tuple_49_52]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_49_52] = 1 | 4
                        if not present_bit:
                            self.index_110[tuple_49_52[0]].append(tuple_49_52[1])
        # Program VectorClear Region
        del vec_47[:]
        vec_index47 = 0
        # Program Return Region
        return False

    def function_1(self, vec_54: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index54: int = 0
        vec_56: List[int] = list()
        vec_index56: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index54 = 0
        while vec_index54 < len(vec_54):
            var_55 = vec_54[vec_index54]
            vec_index54 += 1
            # Program TransitionState Region
            tuple_55 = var_55
            prev_state = self.table_13[tuple_55]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_13[tuple_55] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_56.append(var_55)
        # Program VectorUnique Region
        vec_56 = list(set(vec_56))
        vec_index56 = 0
        # Program TableJoin Region
        while vec_index56 < len(vec_56):
            var_58 = vec_56[vec_index56]
            vec_index56 += 1
            if var_58 in self.index_59:
                tuple_57_1_index: int = 0
                tuple_57_1_vec: List[int] = self.index_60[var_58]
                while tuple_57_1_index < len(tuple_57_1_vec):
                    tuple_57_1 = tuple_57_1_vec[tuple_57_1_index]
                    tuple_57_1_index += 1
                    var_61 = tuple_57_1
                    # Program TransitionState Region
                    tuple_58_61 = (var_58, var_61)
                    prev_state = self.table_15[tuple_58_61]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_58_61] = 1 | 4
                        if not present_bit:
                            self.index_111[tuple_58_61[0]].append(tuple_58_61[1])
        # Program VectorClear Region
        del vec_56[:]
        vec_index56 = 0
        # Program Return Region
        return False

    def instruction_4(self, vec_63: List[Tuple[int, int, int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index63: int = 0
        vec_68: List[int] = list()
        vec_index68: int = 0
        vec_72: List[bytes] = list()
        vec_index72: int = 0
        vec_76: List[int] = list()
        vec_index76: int = 0
        vec_82: List[int] = list()
        vec_index82: int = 0
        vec_88: List[int] = list()
        vec_index88: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index63 = 0
        while vec_index63 < len(vec_63):
            var_64, var_65, var_66, var_67 = vec_63[vec_index63]
            vec_index63 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_64 = var_64
            prev_state = self.table_33[tuple_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_64] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_88.append(var_64)
                # Program VectorAppend Region
                vec_82.append(var_64)
            # Program TransitionState Region
            tuple_64_67 = (var_64, var_67)
            prev_state = self.table_22[tuple_64_67]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_22[tuple_64_67] = 1 | 4
                if not present_bit:
                    self.index_51[tuple_64_67[1]].append(tuple_64_67[0])
                # Program VectorAppend Region
                vec_72.append(var_67)
            # Program TransitionState Region
            tuple_64_66 = (var_64, var_66)
            prev_state = self.table_25[tuple_64_66]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_25[tuple_64_66] = 1 | 4
                if not present_bit:
                    self.index_60[tuple_64_66[1]].append(tuple_64_66[0])
                # Program VectorAppend Region
                vec_68.append(var_66)
            # Program TupleCompare Region
            if self.var_0 == var_65:
                # Program TransitionState Region
                tuple_64 = var_64
                prev_state = self.table_28[tuple_64]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_28[tuple_64] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_76.append(var_64)
            # Program TransitionState Region
            tuple_64 = var_64
            prev_state = self.table_9[tuple_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_9[tuple_64] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_64 = var_64
            prev_state = self.table_33[tuple_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_64] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_88.append(var_64)
                # Program VectorAppend Region
                vec_82.append(var_64)
            # Program TransitionState Region
            tuple_64 = var_64
            prev_state = self.table_33[tuple_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_64] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_88.append(var_64)
                # Program VectorAppend Region
                vec_82.append(var_64)
            # Program TransitionState Region
            tuple_64 = var_64
            prev_state = self.table_33[tuple_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_64] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_88.append(var_64)
                # Program VectorAppend Region
                vec_82.append(var_64)
            # Program TransitionState Region
            tuple_64 = var_64
            prev_state = self.table_33[tuple_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_64] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_88.append(var_64)
                # Program VectorAppend Region
                vec_82.append(var_64)
            # Program TransitionState Region
            tuple_64 = var_64
            prev_state = self.table_33[tuple_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_64] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_88.append(var_64)
                # Program VectorAppend Region
                vec_82.append(var_64)
        # Program VectorUnique Region
        vec_68 = list(set(vec_68))
        vec_index68 = 0
        # Program TableJoin Region
        while vec_index68 < len(vec_68):
            var_70 = vec_68[vec_index68]
            vec_index68 += 1
            if var_70 in self.index_59:
                tuple_69_1_index: int = 0
                tuple_69_1_vec: List[int] = self.index_60[var_70]
                while tuple_69_1_index < len(tuple_69_1_vec):
                    tuple_69_1 = tuple_69_1_vec[tuple_69_1_index]
                    tuple_69_1_index += 1
                    var_71 = tuple_69_1
                    # Program TransitionState Region
                    tuple_70_71 = (var_70, var_71)
                    prev_state = self.table_15[tuple_70_71]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_70_71] = 1 | 4
                        if not present_bit:
                            self.index_111[tuple_70_71[0]].append(tuple_70_71[1])
        # Program VectorClear Region
        del vec_68[:]
        vec_index68 = 0
        # Program VectorUnique Region
        vec_72 = list(set(vec_72))
        vec_index72 = 0
        # Program TableJoin Region
        while vec_index72 < len(vec_72):
            var_74 = vec_72[vec_index72]
            vec_index72 += 1
            if var_74 in self.index_50:
                tuple_73_1_index: int = 0
                tuple_73_1_vec: List[int] = self.index_51[var_74]
                while tuple_73_1_index < len(tuple_73_1_vec):
                    tuple_73_1 = tuple_73_1_vec[tuple_73_1_index]
                    tuple_73_1_index += 1
                    var_75 = tuple_73_1
                    # Program TransitionState Region
                    tuple_74_75 = (var_74, var_75)
                    prev_state = self.table_6[tuple_74_75]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_74_75] = 1 | 4
                        if not present_bit:
                            self.index_110[tuple_74_75[0]].append(tuple_74_75[1])
        # Program VectorClear Region
        del vec_72[:]
        vec_index72 = 0
        # Program VectorUnique Region
        vec_76 = list(set(vec_76))
        vec_index76 = 0
        # Program TableJoin Region
        while vec_index76 < len(vec_76):
            var_78 = vec_76[vec_index76]
            vec_index76 += 1
            if var_78 in self.index_79:
                tuple_77_1_index: int = 0
                tuple_77_1_vec: List[int] = self.index_80[var_78]
                while tuple_77_1_index < len(tuple_77_1_vec):
                    tuple_77_1 = tuple_77_1_vec[tuple_77_1_index]
                    tuple_77_1_index += 1
                    var_81 = tuple_77_1
                    # Program TransitionState Region
                    tuple_81 = var_81
                    prev_state = self.table_35[tuple_81]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_35[tuple_81] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_88.append(var_81)
        # Program VectorClear Region
        del vec_76[:]
        vec_index76 = 0
        # Program VectorUnique Region
        vec_82 = list(set(vec_82))
        vec_index82 = 0
        # Program TableJoin Region
        while vec_index82 < len(vec_82):
            var_84 = vec_82[vec_index82]
            vec_index82 += 1
            if var_84 in self.index_85:
                tuple_83_1_index: int = 0
                tuple_83_1_vec: List[int] = self.index_86[var_84]
                while tuple_83_1_index < len(tuple_83_1_vec):
                    tuple_83_1 = tuple_83_1_vec[tuple_83_1_index]
                    tuple_83_1_index += 1
                    var_87 = tuple_83_1
                    # Program TransitionState Region
                    tuple_87_84 = (var_87, var_84)
                    prev_state = self.table_3[tuple_87_84]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_3[tuple_87_84] = 1 | 4
                        if not present_bit:
                            self.index_109[tuple_87_84[0]].append(tuple_87_84[1])
        # Program VectorClear Region
        del vec_82[:]
        vec_index82 = 0
        # Program VectorUnique Region
        vec_88 = list(set(vec_88))
        vec_index88 = 0
        # Program TableJoin Region
        while vec_index88 < len(vec_88):
            var_90 = vec_88[vec_index88]
            vec_index88 += 1
            if var_90 in self.index_85:
                if var_90 in self.index_91:
                    # Program TransitionState Region
                    tuple_90 = var_90
                    prev_state = self.table_11[tuple_90]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_90] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_88[:]
        vec_index88 = 0
        # Program Return Region
        return False

    def instruction_transfer_4(self, vec_93: List[Tuple[int, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index93: int = 0
        vec_98: List[int] = list()
        vec_index98: int = 0
        vec_102: List[int] = list()
        vec_index102: int = 0
        vec_106: List[int] = list()
        vec_index106: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index93 = 0
        while vec_index93 < len(vec_93):
            var_94, var_95, var_96, var_97 = vec_93[vec_index93]
            vec_index93 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_1 == var_96:
                # Program TransitionState Region
                tuple_94_95 = (var_94, var_95)
                prev_state = self.table_30[tuple_94_95]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_30[tuple_94_95] = 1 | 4
                    if not present_bit:
                        self.index_80[tuple_94_95[0]].append(tuple_94_95[1])
                    # Program VectorAppend Region
                    vec_102.append(var_94)
            # Program TupleCompare Region
            if self.var_2 == var_97:
                # Program TransitionState Region
                tuple_94_95 = (var_94, var_95)
                prev_state = self.table_37[tuple_94_95]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_37[tuple_94_95] = 1 | 4
                    if not present_bit:
                        self.index_86[tuple_94_95[1]].append(tuple_94_95[0])
                    # Program VectorAppend Region
                    vec_98.append(var_95)
        # Program VectorUnique Region
        vec_98 = list(set(vec_98))
        vec_index98 = 0
        # Program TableJoin Region
        while vec_index98 < len(vec_98):
            var_100 = vec_98[vec_index98]
            vec_index98 += 1
            if var_100 in self.index_85:
                tuple_99_1_index: int = 0
                tuple_99_1_vec: List[int] = self.index_86[var_100]
                while tuple_99_1_index < len(tuple_99_1_vec):
                    tuple_99_1 = tuple_99_1_vec[tuple_99_1_index]
                    tuple_99_1_index += 1
                    var_101 = tuple_99_1
                    # Program TransitionState Region
                    tuple_101_100 = (var_101, var_100)
                    prev_state = self.table_3[tuple_101_100]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_3[tuple_101_100] = 1 | 4
                        if not present_bit:
                            self.index_109[tuple_101_100[0]].append(tuple_101_100[1])
        # Program VectorClear Region
        del vec_98[:]
        vec_index98 = 0
        # Program VectorUnique Region
        vec_102 = list(set(vec_102))
        vec_index102 = 0
        # Program TableJoin Region
        while vec_index102 < len(vec_102):
            var_104 = vec_102[vec_index102]
            vec_index102 += 1
            if var_104 in self.index_79:
                tuple_103_1_index: int = 0
                tuple_103_1_vec: List[int] = self.index_80[var_104]
                while tuple_103_1_index < len(tuple_103_1_vec):
                    tuple_103_1 = tuple_103_1_vec[tuple_103_1_index]
                    tuple_103_1_index += 1
                    var_105 = tuple_103_1
                    # Program TransitionState Region
                    tuple_105 = var_105
                    prev_state = self.table_35[tuple_105]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_35[tuple_105] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_106.append(var_105)
        # Program VectorClear Region
        del vec_102[:]
        vec_index102 = 0
        # Program VectorUnique Region
        vec_106 = list(set(vec_106))
        vec_index106 = 0
        # Program TableJoin Region
        while vec_index106 < len(vec_106):
            var_108 = vec_106[vec_index106]
            vec_index106 += 1
            if var_108 in self.index_85:
                if var_108 in self.index_91:
                    # Program TransitionState Region
                    tuple_108 = var_108
                    prev_state = self.table_11[tuple_108]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_108] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_106[:]
        vec_index106 = 0
        # Program Return Region
        return False

    def get_intraproc_successor_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_109[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_3[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_section_instructions_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_110[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_6[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_instructions_f(self) -> Iterator[int]:
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

    def get_direct_call_targets_f(self) -> Iterator[int]:
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

    def get_functions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_13:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_13[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_function_instructions_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_111[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_15[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_sections_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_18:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_18[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

