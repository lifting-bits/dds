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

        self.table_5: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_77: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_131: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_8: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_132: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_11: DefaultDict[int, int] = defaultdict(int)

        self.table_13: DefaultDict[int, int] = defaultdict(int)

        self.table_15: DefaultDict[bytes, int] = defaultdict(int)

        self.table_17: DefaultDict[bytes, int] = defaultdict(int)
        self.index_46 = self.table_17

        self.table_19: DefaultDict[Tuple[int, bytes], int] = defaultdict(int)
        self.index_47: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_22: DefaultDict[int, int] = defaultdict(int)
        self.index_61 = self.table_22

        self.table_24: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_62: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_27: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_90: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_30: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_84: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_33: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_78: DefaultDict[int, List[int]] = defaultdict(list)

        self.var_0: int = 5
        self.var_1: int = 4
        self.var_2: int = 0
        self.var_3: int = 2
        self.var_4: int = 3
        self.init_36_()

    _HAS_MERGE_METHOD_sectype: Final[bool] = hasattr(int, 'merge_into')
    _MERGE_METHOD_sectype: Final[Callable[[int, int], None]] = getattr(int, 'merge_into', lambda a, b: None)

    def _resolve_sectype(self, obj: int) -> int:
        if Database._HAS_MERGE_METHOD_sectype:
            ref_list = self._refs[hash(obj)]
            for maybe_obj in ref_list:
                if obj is maybe_obj:
                    return obj
                elif obj == maybe_obj:
                    prior_obj: int = cast(int, maybe_obj)
                    Database._MERGE_METHOD_sectype(obj, prior_obj)
                    return prior_obj
            ref_list.append(obj)
        return obj

    _HAS_MERGE_METHOD_insntype: Final[bool] = hasattr(int, 'merge_into')
    _MERGE_METHOD_insntype: Final[Callable[[int, int], None]] = getattr(int, 'merge_into', lambda a, b: None)

    def _resolve_insntype(self, obj: int) -> int:
        if Database._HAS_MERGE_METHOD_insntype:
            ref_list = self._refs[hash(obj)]
            for maybe_obj in ref_list:
                if obj is maybe_obj:
                    return obj
                elif obj == maybe_obj:
                    prior_obj: int = cast(int, maybe_obj)
                    Database._MERGE_METHOD_insntype(obj, prior_obj)
                    return prior_obj
            ref_list.append(obj)
        return obj

    _HAS_MERGE_METHOD_edgetype: Final[bool] = hasattr(int, 'merge_into')
    _MERGE_METHOD_edgetype: Final[Callable[[int, int], None]] = getattr(int, 'merge_into', lambda a, b: None)

    def _resolve_edgetype(self, obj: int) -> int:
        if Database._HAS_MERGE_METHOD_edgetype:
            ref_list = self._refs[hash(obj)]
            for maybe_obj in ref_list:
                if obj is maybe_obj:
                    return obj
                elif obj == maybe_obj:
                    prior_obj: int = cast(int, maybe_obj)
                    Database._MERGE_METHOD_edgetype(obj, prior_obj)
                    return prior_obj
            ref_list.append(obj)
        return obj

    def init_36_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False

    def section_4(self, vec_38: List[Tuple[bytes, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index38: int = 0
        vec_43: List[bytes] = list()
        vec_index43: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index38 = 0
        while vec_index38 < len(vec_38):
            var_39, var_40, var_41, var_42 = vec_38[vec_index38]
            vec_index38 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_39 = var_39
            prev_state = self.table_17[tuple_39]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_17[tuple_39] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_43.append(var_39)
            # Program TransitionState Region
            tuple_39 = var_39
            prev_state = self.table_15[tuple_39]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_15[tuple_39] = 1 | 4
                if not present_bit:
                    pass
        # Program VectorUnique Region
        vec_43 = list(set(vec_43))
        vec_index43 = 0
        # Program TableJoin Region
        while vec_index43 < len(vec_43):
            var_45 = vec_43[vec_index43]
            vec_index43 += 1
            if var_45 in self.index_46:
                tuple_44_1_index: int = 0
                tuple_44_1_vec: List[int] = self.index_47[var_45]
                while tuple_44_1_index < len(tuple_44_1_vec):
                    tuple_44_1 = tuple_44_1_vec[tuple_44_1_index]
                    tuple_44_1_index += 1
                    var_48 = tuple_44_1
                    # Program TransitionState Region
                    tuple_45_48 = (var_45, var_48)
                    prev_state = self.table_8[tuple_45_48]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_8[tuple_45_48] = 1 | 4
                        if not present_bit:
                            self.index_132[tuple_45_48[0]].append(tuple_45_48[1])
        # Program VectorClear Region
        del vec_43[:]
        vec_index43 = 0
        # Program Return Region
        return False

    def instruction_3(self, vec_50: List[Tuple[int, int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index50: int = 0
        vec_54: List[bytes] = list()
        vec_index54: int = 0
        vec_58: List[int] = list()
        vec_index58: int = 0
        vec_68: List[Tuple[int, int]] = list()
        vec_index68: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index50 = 0
        while vec_index50 < len(vec_50):
            var_51, var_52, var_53 = vec_50[vec_index50]
            vec_index50 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_51_53 = (var_51, var_53)
            prev_state = self.table_19[tuple_51_53]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_19[tuple_51_53] = 1 | 4
                if not present_bit:
                    self.index_47[tuple_51_53[1]].append(tuple_51_53[0])
                # Program VectorAppend Region
                vec_54.append(var_53)
            # Program TupleCompare Region
            if self.var_0 == var_52:
                # Program TransitionState Region
                tuple_51 = var_51
                prev_state = self.table_22[tuple_51]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_22[tuple_51] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_58.append(var_51)
            # Program TransitionState Region
            tuple_51 = var_51
            prev_state = self.table_11[tuple_51]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_11[tuple_51] = 1 | 4
                if not present_bit:
                    pass
        # Program VectorUnique Region
        vec_54 = list(set(vec_54))
        vec_index54 = 0
        # Program TableJoin Region
        while vec_index54 < len(vec_54):
            var_56 = vec_54[vec_index54]
            vec_index54 += 1
            if var_56 in self.index_46:
                tuple_55_1_index: int = 0
                tuple_55_1_vec: List[int] = self.index_47[var_56]
                while tuple_55_1_index < len(tuple_55_1_vec):
                    tuple_55_1 = tuple_55_1_vec[tuple_55_1_index]
                    tuple_55_1_index += 1
                    var_57 = tuple_55_1
                    # Program TransitionState Region
                    tuple_56_57 = (var_56, var_57)
                    prev_state = self.table_8[tuple_56_57]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_8[tuple_56_57] = 1 | 4
                        if not present_bit:
                            self.index_132[tuple_56_57[0]].append(tuple_56_57[1])
        # Program VectorClear Region
        del vec_54[:]
        vec_index54 = 0
        # Program VectorUnique Region
        vec_58 = list(set(vec_58))
        vec_index58 = 0
        # Program TableJoin Region
        while vec_index58 < len(vec_58):
            var_60 = vec_58[vec_index58]
            vec_index58 += 1
            if var_60 in self.index_61:
                tuple_59_1_index: int = 0
                tuple_59_1_vec: List[int] = self.index_62[var_60]
                while tuple_59_1_index < len(tuple_59_1_vec):
                    tuple_59_1 = tuple_59_1_vec[tuple_59_1_index]
                    tuple_59_1_index += 1
                    var_63 = tuple_59_1
                    # Program TransitionState Region
                    tuple_60_63 = (var_60, var_63)
                    prev_state = self.table_5[tuple_60_63]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_5[tuple_60_63] = 1 | 4
                        if not present_bit:
                            self.index_77[tuple_60_63[1]].append(tuple_60_63[0])
                            self.index_131[tuple_60_63[0]].append(tuple_60_63[1])
                        # Program VectorAppend Region
                        vec_68.append((var_63, var_63))
        # Program VectorClear Region
        del vec_58[:]
        vec_index58 = 0
        # Induction Fixpoint Loop Region
        while len(vec_68):
            # Program Series Region
            # Program Call Region
            ret = self.proc_66_(vec_68)

            # Program Call Region
            param_70_0 = [vec_68]
            ret = self.proc_64_(param_70_0)
            vec_68 = param_70_0[0]

        vec_index68 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_68[:]
        vec_index68 = 0
        # Program Return Region
        return False

    def proc_64_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_65 = param_0[0]
        vec_index65: int = 0
        vec_71: List[Tuple[int, int]] = list()
        vec_index71: int = 0
        vec_74: List[int] = list()
        vec_index74: int = 0
        vec_81: List[int] = list()
        vec_index81: int = 0
        vec_87: List[int] = list()
        vec_index87: int = 0
        # Program Series Region
        # Program Series Region
        # Program VectorSwap Region
        vec_65, vec_71 = vec_71, vec_65
        # Program VectorLoop Region
        while vec_index71 < len(vec_71):
            var_72, var_73 = vec_71[vec_index71]
            vec_index71 += 1
            # Program Parallel Region
            # Program VectorAppend Region
            vec_87.append(var_73)
            # Program VectorAppend Region
            vec_81.append(var_73)
            # Program VectorAppend Region
            vec_74.append(var_73)
        # Program VectorUnique Region
        vec_74 = list(set(vec_74))
        vec_index74 = 0
        # Program TableJoin Region
        while vec_index74 < len(vec_74):
            var_76 = vec_74[vec_index74]
            vec_index74 += 1
            tuple_75_0_index: int = 0
            tuple_75_0_vec: List[int] = self.index_77[var_76]
            while tuple_75_0_index < len(tuple_75_0_vec):
                tuple_75_0 = tuple_75_0_vec[tuple_75_0_index]
                tuple_75_0_index += 1
                var_79 = tuple_75_0
                tuple_75_1_index: int = 0
                tuple_75_1_vec: List[int] = self.index_78[var_76]
                while tuple_75_1_index < len(tuple_75_1_vec):
                    tuple_75_1 = tuple_75_1_vec[tuple_75_1_index]
                    tuple_75_1_index += 1
                    var_80 = tuple_75_1
                    # Program TransitionState Region
                    tuple_79_80 = (var_79, var_80)
                    prev_state = self.table_5[tuple_79_80]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_5[tuple_79_80] = 1 | 4
                        if not present_bit:
                            self.index_77[tuple_79_80[1]].append(tuple_79_80[0])
                            self.index_131[tuple_79_80[0]].append(tuple_79_80[1])
                        # Program VectorAppend Region
                        vec_65.append((var_79, var_80))
        # Program VectorClear Region
        del vec_74[:]
        vec_index74 = 0
        # Program VectorUnique Region
        vec_81 = list(set(vec_81))
        vec_index81 = 0
        # Program TableJoin Region
        while vec_index81 < len(vec_81):
            var_83 = vec_81[vec_index81]
            vec_index81 += 1
            tuple_82_0_index: int = 0
            tuple_82_0_vec: List[int] = self.index_77[var_83]
            while tuple_82_0_index < len(tuple_82_0_vec):
                tuple_82_0 = tuple_82_0_vec[tuple_82_0_index]
                tuple_82_0_index += 1
                var_85 = tuple_82_0
                tuple_82_1_index: int = 0
                tuple_82_1_vec: List[int] = self.index_84[var_83]
                while tuple_82_1_index < len(tuple_82_1_vec):
                    tuple_82_1 = tuple_82_1_vec[tuple_82_1_index]
                    tuple_82_1_index += 1
                    var_86 = tuple_82_1
                    # Program TransitionState Region
                    tuple_85_86 = (var_85, var_86)
                    prev_state = self.table_5[tuple_85_86]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_5[tuple_85_86] = 1 | 4
                        if not present_bit:
                            self.index_77[tuple_85_86[1]].append(tuple_85_86[0])
                            self.index_131[tuple_85_86[0]].append(tuple_85_86[1])
                        # Program VectorAppend Region
                        vec_65.append((var_85, var_86))
        # Program VectorClear Region
        del vec_81[:]
        vec_index81 = 0
        # Program VectorUnique Region
        vec_87 = list(set(vec_87))
        vec_index87 = 0
        # Program TableJoin Region
        while vec_index87 < len(vec_87):
            var_89 = vec_87[vec_index87]
            vec_index87 += 1
            tuple_88_0_index: int = 0
            tuple_88_0_vec: List[int] = self.index_77[var_89]
            while tuple_88_0_index < len(tuple_88_0_vec):
                tuple_88_0 = tuple_88_0_vec[tuple_88_0_index]
                tuple_88_0_index += 1
                var_91 = tuple_88_0
                tuple_88_1_index: int = 0
                tuple_88_1_vec: List[int] = self.index_90[var_89]
                while tuple_88_1_index < len(tuple_88_1_vec):
                    tuple_88_1 = tuple_88_1_vec[tuple_88_1_index]
                    tuple_88_1_index += 1
                    var_92 = tuple_88_1
                    # Program TransitionState Region
                    tuple_91_92 = (var_91, var_92)
                    prev_state = self.table_5[tuple_91_92]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_5[tuple_91_92] = 1 | 4
                        if not present_bit:
                            self.index_77[tuple_91_92[1]].append(tuple_91_92[0])
                            self.index_131[tuple_91_92[0]].append(tuple_91_92[1])
                        # Program VectorAppend Region
                        vec_65.append((var_91, var_92))
        # Program VectorClear Region
        del vec_87[:]
        vec_index87 = 0
        # Program VectorClear Region
        del vec_71[:]
        vec_index71 = 0
        # Program Return Region
        param_0[0] = vec_65
        return False

    def proc_66_(self, vec_67: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index67: int = 0
        # Program Series Region
        # Program VectorLoop Region
        while vec_index67 < len(vec_67):
            var_93, var_94 = vec_67[vec_index67]
            vec_index67 += 1
            # Program TupleCompare Region
            if var_93 == var_94:
                # Program TransitionState Region
                tuple_93 = var_93
                prev_state = self.table_13[tuple_93]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_13[tuple_93] = 1 | 4
                    if not present_bit:
                        pass
        # Program Return Region
        return False

    def instruction_transfer_3(self, vec_96: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index96: int = 0
        vec_100: List[int] = list()
        vec_index100: int = 0
        vec_105: List[Tuple[int, int]] = list()
        vec_index105: int = 0
        vec_108: List[int] = list()
        vec_index108: int = 0
        vec_113: List[Tuple[int, int]] = list()
        vec_index113: int = 0
        vec_116: List[int] = list()
        vec_index116: int = 0
        vec_121: List[Tuple[int, int]] = list()
        vec_index121: int = 0
        vec_124: List[int] = list()
        vec_index124: int = 0
        vec_128: List[Tuple[int, int]] = list()
        vec_index128: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index96 = 0
        while vec_index96 < len(vec_96):
            var_97, var_98, var_99 = vec_96[vec_index96]
            vec_index96 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_1 == var_99:
                # Program TransitionState Region
                tuple_97_98 = (var_97, var_98)
                prev_state = self.table_24[tuple_97_98]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_24[tuple_97_98] = 1 | 4
                    if not present_bit:
                        self.index_62[tuple_97_98[0]].append(tuple_97_98[1])
                    # Program VectorAppend Region
                    vec_124.append(var_97)
            # Program TupleCompare Region
            if self.var_2 == var_99:
                # Program TransitionState Region
                tuple_97_98 = (var_97, var_98)
                prev_state = self.table_27[tuple_97_98]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_27[tuple_97_98] = 1 | 4
                    if not present_bit:
                        self.index_90[tuple_97_98[0]].append(tuple_97_98[1])
                    # Program VectorAppend Region
                    vec_116.append(var_97)
            # Program TupleCompare Region
            if self.var_3 == var_99:
                # Program TransitionState Region
                tuple_97_98 = (var_97, var_98)
                prev_state = self.table_30[tuple_97_98]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_30[tuple_97_98] = 1 | 4
                    if not present_bit:
                        self.index_84[tuple_97_98[0]].append(tuple_97_98[1])
                    # Program VectorAppend Region
                    vec_108.append(var_97)
            # Program TupleCompare Region
            if self.var_4 == var_99:
                # Program TransitionState Region
                tuple_97_98 = (var_97, var_98)
                prev_state = self.table_33[tuple_97_98]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_33[tuple_97_98] = 1 | 4
                    if not present_bit:
                        self.index_78[tuple_97_98[0]].append(tuple_97_98[1])
                    # Program VectorAppend Region
                    vec_100.append(var_97)
        # Program VectorUnique Region
        vec_100 = list(set(vec_100))
        vec_index100 = 0
        # Program TableJoin Region
        while vec_index100 < len(vec_100):
            var_102 = vec_100[vec_index100]
            vec_index100 += 1
            tuple_101_0_index: int = 0
            tuple_101_0_vec: List[int] = self.index_77[var_102]
            while tuple_101_0_index < len(tuple_101_0_vec):
                tuple_101_0 = tuple_101_0_vec[tuple_101_0_index]
                tuple_101_0_index += 1
                var_103 = tuple_101_0
                tuple_101_1_index: int = 0
                tuple_101_1_vec: List[int] = self.index_78[var_102]
                while tuple_101_1_index < len(tuple_101_1_vec):
                    tuple_101_1 = tuple_101_1_vec[tuple_101_1_index]
                    tuple_101_1_index += 1
                    var_104 = tuple_101_1
                    # Program TransitionState Region
                    tuple_103_104 = (var_103, var_104)
                    prev_state = self.table_5[tuple_103_104]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_5[tuple_103_104] = 1 | 4
                        if not present_bit:
                            self.index_77[tuple_103_104[1]].append(tuple_103_104[0])
                            self.index_131[tuple_103_104[0]].append(tuple_103_104[1])
                        # Program VectorAppend Region
                        vec_105.append((var_103, var_104))
        # Program VectorClear Region
        del vec_100[:]
        vec_index100 = 0
        # Program VectorUnique Region
        vec_108 = list(set(vec_108))
        vec_index108 = 0
        # Program TableJoin Region
        while vec_index108 < len(vec_108):
            var_110 = vec_108[vec_index108]
            vec_index108 += 1
            tuple_109_0_index: int = 0
            tuple_109_0_vec: List[int] = self.index_77[var_110]
            while tuple_109_0_index < len(tuple_109_0_vec):
                tuple_109_0 = tuple_109_0_vec[tuple_109_0_index]
                tuple_109_0_index += 1
                var_111 = tuple_109_0
                tuple_109_1_index: int = 0
                tuple_109_1_vec: List[int] = self.index_84[var_110]
                while tuple_109_1_index < len(tuple_109_1_vec):
                    tuple_109_1 = tuple_109_1_vec[tuple_109_1_index]
                    tuple_109_1_index += 1
                    var_112 = tuple_109_1
                    # Program TransitionState Region
                    tuple_111_112 = (var_111, var_112)
                    prev_state = self.table_5[tuple_111_112]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_5[tuple_111_112] = 1 | 4
                        if not present_bit:
                            self.index_77[tuple_111_112[1]].append(tuple_111_112[0])
                            self.index_131[tuple_111_112[0]].append(tuple_111_112[1])
                        # Program VectorAppend Region
                        vec_113.append((var_111, var_112))
        # Program VectorClear Region
        del vec_108[:]
        vec_index108 = 0
        # Program VectorUnique Region
        vec_116 = list(set(vec_116))
        vec_index116 = 0
        # Program TableJoin Region
        while vec_index116 < len(vec_116):
            var_118 = vec_116[vec_index116]
            vec_index116 += 1
            tuple_117_0_index: int = 0
            tuple_117_0_vec: List[int] = self.index_77[var_118]
            while tuple_117_0_index < len(tuple_117_0_vec):
                tuple_117_0 = tuple_117_0_vec[tuple_117_0_index]
                tuple_117_0_index += 1
                var_119 = tuple_117_0
                tuple_117_1_index: int = 0
                tuple_117_1_vec: List[int] = self.index_90[var_118]
                while tuple_117_1_index < len(tuple_117_1_vec):
                    tuple_117_1 = tuple_117_1_vec[tuple_117_1_index]
                    tuple_117_1_index += 1
                    var_120 = tuple_117_1
                    # Program TransitionState Region
                    tuple_119_120 = (var_119, var_120)
                    prev_state = self.table_5[tuple_119_120]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_5[tuple_119_120] = 1 | 4
                        if not present_bit:
                            self.index_77[tuple_119_120[1]].append(tuple_119_120[0])
                            self.index_131[tuple_119_120[0]].append(tuple_119_120[1])
                        # Program VectorAppend Region
                        vec_121.append((var_119, var_120))
        # Program VectorClear Region
        del vec_116[:]
        vec_index116 = 0
        # Program VectorUnique Region
        vec_124 = list(set(vec_124))
        vec_index124 = 0
        # Program TableJoin Region
        while vec_index124 < len(vec_124):
            var_126 = vec_124[vec_index124]
            vec_index124 += 1
            if var_126 in self.index_61:
                tuple_125_1_index: int = 0
                tuple_125_1_vec: List[int] = self.index_62[var_126]
                while tuple_125_1_index < len(tuple_125_1_vec):
                    tuple_125_1 = tuple_125_1_vec[tuple_125_1_index]
                    tuple_125_1_index += 1
                    var_127 = tuple_125_1
                    # Program TransitionState Region
                    tuple_126_127 = (var_126, var_127)
                    prev_state = self.table_5[tuple_126_127]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_5[tuple_126_127] = 1 | 4
                        if not present_bit:
                            self.index_77[tuple_126_127[1]].append(tuple_126_127[0])
                            self.index_131[tuple_126_127[0]].append(tuple_126_127[1])
                        # Program VectorAppend Region
                        vec_128.append((var_127, var_127))
        # Program VectorClear Region
        del vec_124[:]
        vec_index124 = 0
        # Induction Fixpoint Loop Region
        while len(vec_105) or len(vec_113) or len(vec_121) or len(vec_128):
            # Program Series Region
            # Program Call Region
            ret = self.proc_66_(vec_128)

            # Program Call Region
            param_130_0 = [vec_128]
            ret = self.proc_64_(param_130_0)
            vec_128 = param_130_0[0]

            # Program Call Region
            ret = self.proc_66_(vec_121)

            # Program Call Region
            param_123_0 = [vec_121]
            ret = self.proc_64_(param_123_0)
            vec_121 = param_123_0[0]

            # Program Call Region
            ret = self.proc_66_(vec_113)

            # Program Call Region
            param_115_0 = [vec_113]
            ret = self.proc_64_(param_115_0)
            vec_113 = param_115_0[0]

            # Program Call Region
            ret = self.proc_66_(vec_105)

            # Program Call Region
            param_107_0 = [vec_105]
            ret = self.proc_64_(param_107_0)
            vec_105 = param_107_0[0]

        vec_index105 = 0
        vec_index113 = 0
        vec_index121 = 0
        vec_index128 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_128[:]
        vec_index128 = 0
        # Program VectorClear Region
        del vec_121[:]
        vec_index121 = 0
        # Program VectorClear Region
        del vec_113[:]
        vec_index113 = 0
        # Program VectorClear Region
        del vec_105[:]
        vec_index105 = 0
        # Program Return Region
        return False

    def get_function_instructions_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_131[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_5[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_section_instructions_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_132[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_8[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_instructions_f(self) -> Iterator[int]:
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

    def get_sections_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_15:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_15[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

