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

        self.table_6: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_81: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_149: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_9: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_150: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_12: DefaultDict[int, int] = defaultdict(int)

        self.table_14: DefaultDict[int, int] = defaultdict(int)

        self.table_16: DefaultDict[bytes, int] = defaultdict(int)

        self.table_18: DefaultDict[bytes, int] = defaultdict(int)
        self.index_50 = self.table_18

        self.table_20: DefaultDict[Tuple[int, bytes], int] = defaultdict(int)
        self.index_51: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_23: DefaultDict[int, int] = defaultdict(int)
        self.index_65 = self.table_23

        self.table_25: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_66: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_28: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_100: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_31: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_94: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_34: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_88: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_37: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_82: DefaultDict[int, List[int]] = defaultdict(list)

        self.var_0: int = 5
        self.var_1: int = 4
        self.var_2: int = 0
        self.var_3: int = 2
        self.var_4: int = 3
        self.var_5: int = 5
        self.init_40_()

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
            prev_state = self.table_18[tuple_43]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_18[tuple_43] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_47.append(var_43)
            # Program TransitionState Region
            tuple_43 = var_43
            prev_state = self.table_16[tuple_43]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_16[tuple_43] = 1 | 4
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
                    prev_state = self.table_9[tuple_49_52]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_49_52] = 1 | 4
                        if not present_bit:
                            self.index_150[tuple_49_52[0]].append(tuple_49_52[1])
        # Program VectorClear Region
        del vec_47[:]
        vec_index47 = 0
        # Program Return Region
        return False

    def instruction_3(self, vec_54: List[Tuple[int, int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index54: int = 0
        vec_58: List[bytes] = list()
        vec_index58: int = 0
        vec_62: List[int] = list()
        vec_index62: int = 0
        vec_72: List[Tuple[int, int]] = list()
        vec_index72: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index54 = 0
        while vec_index54 < len(vec_54):
            var_55, var_56, var_57 = vec_54[vec_index54]
            vec_index54 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_55_57 = (var_55, var_57)
            prev_state = self.table_20[tuple_55_57]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_20[tuple_55_57] = 1 | 4
                if not present_bit:
                    self.index_51[tuple_55_57[1]].append(tuple_55_57[0])
                # Program VectorAppend Region
                vec_58.append(var_57)
            # Program TupleCompare Region
            if self.var_0 == var_56:
                # Program TransitionState Region
                tuple_55 = var_55
                prev_state = self.table_23[tuple_55]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_23[tuple_55] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_62.append(var_55)
            # Program TransitionState Region
            tuple_55 = var_55
            prev_state = self.table_12[tuple_55]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_12[tuple_55] = 1 | 4
                if not present_bit:
                    pass
        # Program VectorUnique Region
        vec_58 = list(set(vec_58))
        vec_index58 = 0
        # Program TableJoin Region
        while vec_index58 < len(vec_58):
            var_60 = vec_58[vec_index58]
            vec_index58 += 1
            if var_60 in self.index_50:
                tuple_59_1_index: int = 0
                tuple_59_1_vec: List[int] = self.index_51[var_60]
                while tuple_59_1_index < len(tuple_59_1_vec):
                    tuple_59_1 = tuple_59_1_vec[tuple_59_1_index]
                    tuple_59_1_index += 1
                    var_61 = tuple_59_1
                    # Program TransitionState Region
                    tuple_60_61 = (var_60, var_61)
                    prev_state = self.table_9[tuple_60_61]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_60_61] = 1 | 4
                        if not present_bit:
                            self.index_150[tuple_60_61[0]].append(tuple_60_61[1])
        # Program VectorClear Region
        del vec_58[:]
        vec_index58 = 0
        # Program VectorUnique Region
        vec_62 = list(set(vec_62))
        vec_index62 = 0
        # Program TableJoin Region
        while vec_index62 < len(vec_62):
            var_64 = vec_62[vec_index62]
            vec_index62 += 1
            if var_64 in self.index_65:
                tuple_63_1_index: int = 0
                tuple_63_1_vec: List[int] = self.index_66[var_64]
                while tuple_63_1_index < len(tuple_63_1_vec):
                    tuple_63_1 = tuple_63_1_vec[tuple_63_1_index]
                    tuple_63_1_index += 1
                    var_67 = tuple_63_1
                    # Program TransitionState Region
                    tuple_64_67 = (var_64, var_67)
                    prev_state = self.table_6[tuple_64_67]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_64_67] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_64_67[1]].append(tuple_64_67[0])
                            self.index_149[tuple_64_67[0]].append(tuple_64_67[1])
                        # Program VectorAppend Region
                        vec_72.append((var_67, var_67))
        # Program VectorClear Region
        del vec_62[:]
        vec_index62 = 0
        # Induction Fixpoint Loop Region
        while len(vec_72):
            # Program Series Region
            # Program Call Region
            ret = self.proc_70_(vec_72)

            # Program Call Region
            param_74_0 = [vec_72]
            ret = self.proc_68_(param_74_0)
            vec_72 = param_74_0[0]

        vec_index72 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_72[:]
        vec_index72 = 0
        # Program Return Region
        return False

    def proc_68_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_69 = param_0[0]
        vec_index69: int = 0
        vec_75: List[Tuple[int, int]] = list()
        vec_index75: int = 0
        vec_78: List[int] = list()
        vec_index78: int = 0
        vec_85: List[int] = list()
        vec_index85: int = 0
        vec_91: List[int] = list()
        vec_index91: int = 0
        vec_97: List[int] = list()
        vec_index97: int = 0
        # Program Series Region
        # Program Series Region
        # Program VectorSwap Region
        vec_69, vec_75 = vec_75, vec_69
        # Program VectorLoop Region
        while vec_index75 < len(vec_75):
            var_76, var_77 = vec_75[vec_index75]
            vec_index75 += 1
            # Program Parallel Region
            # Program VectorAppend Region
            vec_97.append(var_77)
            # Program VectorAppend Region
            vec_91.append(var_77)
            # Program VectorAppend Region
            vec_85.append(var_77)
            # Program VectorAppend Region
            vec_78.append(var_77)
        # Program VectorUnique Region
        vec_78 = list(set(vec_78))
        vec_index78 = 0
        # Program TableJoin Region
        while vec_index78 < len(vec_78):
            var_80 = vec_78[vec_index78]
            vec_index78 += 1
            tuple_79_0_index: int = 0
            tuple_79_0_vec: List[int] = self.index_81[var_80]
            while tuple_79_0_index < len(tuple_79_0_vec):
                tuple_79_0 = tuple_79_0_vec[tuple_79_0_index]
                tuple_79_0_index += 1
                var_83 = tuple_79_0
                tuple_79_1_index: int = 0
                tuple_79_1_vec: List[int] = self.index_82[var_80]
                while tuple_79_1_index < len(tuple_79_1_vec):
                    tuple_79_1 = tuple_79_1_vec[tuple_79_1_index]
                    tuple_79_1_index += 1
                    var_84 = tuple_79_1
                    # Program TransitionState Region
                    tuple_83_84 = (var_83, var_84)
                    prev_state = self.table_6[tuple_83_84]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_83_84] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_83_84[1]].append(tuple_83_84[0])
                            self.index_149[tuple_83_84[0]].append(tuple_83_84[1])
                        # Program VectorAppend Region
                        vec_69.append((var_83, var_84))
        # Program VectorClear Region
        del vec_78[:]
        vec_index78 = 0
        # Program VectorUnique Region
        vec_85 = list(set(vec_85))
        vec_index85 = 0
        # Program TableJoin Region
        while vec_index85 < len(vec_85):
            var_87 = vec_85[vec_index85]
            vec_index85 += 1
            tuple_86_0_index: int = 0
            tuple_86_0_vec: List[int] = self.index_81[var_87]
            while tuple_86_0_index < len(tuple_86_0_vec):
                tuple_86_0 = tuple_86_0_vec[tuple_86_0_index]
                tuple_86_0_index += 1
                var_89 = tuple_86_0
                tuple_86_1_index: int = 0
                tuple_86_1_vec: List[int] = self.index_88[var_87]
                while tuple_86_1_index < len(tuple_86_1_vec):
                    tuple_86_1 = tuple_86_1_vec[tuple_86_1_index]
                    tuple_86_1_index += 1
                    var_90 = tuple_86_1
                    # Program TransitionState Region
                    tuple_89_90 = (var_89, var_90)
                    prev_state = self.table_6[tuple_89_90]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_89_90] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_89_90[1]].append(tuple_89_90[0])
                            self.index_149[tuple_89_90[0]].append(tuple_89_90[1])
                        # Program VectorAppend Region
                        vec_69.append((var_89, var_90))
        # Program VectorClear Region
        del vec_85[:]
        vec_index85 = 0
        # Program VectorUnique Region
        vec_91 = list(set(vec_91))
        vec_index91 = 0
        # Program TableJoin Region
        while vec_index91 < len(vec_91):
            var_93 = vec_91[vec_index91]
            vec_index91 += 1
            tuple_92_0_index: int = 0
            tuple_92_0_vec: List[int] = self.index_81[var_93]
            while tuple_92_0_index < len(tuple_92_0_vec):
                tuple_92_0 = tuple_92_0_vec[tuple_92_0_index]
                tuple_92_0_index += 1
                var_95 = tuple_92_0
                tuple_92_1_index: int = 0
                tuple_92_1_vec: List[int] = self.index_94[var_93]
                while tuple_92_1_index < len(tuple_92_1_vec):
                    tuple_92_1 = tuple_92_1_vec[tuple_92_1_index]
                    tuple_92_1_index += 1
                    var_96 = tuple_92_1
                    # Program TransitionState Region
                    tuple_95_96 = (var_95, var_96)
                    prev_state = self.table_6[tuple_95_96]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_95_96] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_95_96[1]].append(tuple_95_96[0])
                            self.index_149[tuple_95_96[0]].append(tuple_95_96[1])
                        # Program VectorAppend Region
                        vec_69.append((var_95, var_96))
        # Program VectorClear Region
        del vec_91[:]
        vec_index91 = 0
        # Program VectorUnique Region
        vec_97 = list(set(vec_97))
        vec_index97 = 0
        # Program TableJoin Region
        while vec_index97 < len(vec_97):
            var_99 = vec_97[vec_index97]
            vec_index97 += 1
            tuple_98_0_index: int = 0
            tuple_98_0_vec: List[int] = self.index_81[var_99]
            while tuple_98_0_index < len(tuple_98_0_vec):
                tuple_98_0 = tuple_98_0_vec[tuple_98_0_index]
                tuple_98_0_index += 1
                var_101 = tuple_98_0
                tuple_98_1_index: int = 0
                tuple_98_1_vec: List[int] = self.index_100[var_99]
                while tuple_98_1_index < len(tuple_98_1_vec):
                    tuple_98_1 = tuple_98_1_vec[tuple_98_1_index]
                    tuple_98_1_index += 1
                    var_102 = tuple_98_1
                    # Program TransitionState Region
                    tuple_101_102 = (var_101, var_102)
                    prev_state = self.table_6[tuple_101_102]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_101_102] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_101_102[1]].append(tuple_101_102[0])
                            self.index_149[tuple_101_102[0]].append(tuple_101_102[1])
                        # Program VectorAppend Region
                        vec_69.append((var_101, var_102))
        # Program VectorClear Region
        del vec_97[:]
        vec_index97 = 0
        # Program VectorClear Region
        del vec_75[:]
        vec_index75 = 0
        # Program Return Region
        param_0[0] = vec_69
        return False

    def proc_70_(self, vec_71: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index71: int = 0
        # Program Series Region
        # Program VectorLoop Region
        while vec_index71 < len(vec_71):
            var_103, var_104 = vec_71[vec_index71]
            vec_index71 += 1
            # Program TupleCompare Region
            if var_103 == var_104:
                # Program TransitionState Region
                tuple_103 = var_103
                prev_state = self.table_14[tuple_103]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_14[tuple_103] = 1 | 4
                    if not present_bit:
                        pass
        # Program Return Region
        return False

    def instruction_transfer_3(self, vec_106: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index106: int = 0
        vec_110: List[int] = list()
        vec_index110: int = 0
        vec_115: List[Tuple[int, int]] = list()
        vec_index115: int = 0
        vec_118: List[int] = list()
        vec_index118: int = 0
        vec_123: List[Tuple[int, int]] = list()
        vec_index123: int = 0
        vec_126: List[int] = list()
        vec_index126: int = 0
        vec_131: List[Tuple[int, int]] = list()
        vec_index131: int = 0
        vec_134: List[int] = list()
        vec_index134: int = 0
        vec_139: List[Tuple[int, int]] = list()
        vec_index139: int = 0
        vec_142: List[int] = list()
        vec_index142: int = 0
        vec_146: List[Tuple[int, int]] = list()
        vec_index146: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index106 = 0
        while vec_index106 < len(vec_106):
            var_107, var_108, var_109 = vec_106[vec_index106]
            vec_index106 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_1 == var_109:
                # Program TransitionState Region
                tuple_107_108 = (var_107, var_108)
                prev_state = self.table_25[tuple_107_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_25[tuple_107_108] = 1 | 4
                    if not present_bit:
                        self.index_66[tuple_107_108[0]].append(tuple_107_108[1])
                    # Program VectorAppend Region
                    vec_142.append(var_107)
            # Program TupleCompare Region
            if self.var_2 == var_109:
                # Program TransitionState Region
                tuple_107_108 = (var_107, var_108)
                prev_state = self.table_28[tuple_107_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_28[tuple_107_108] = 1 | 4
                    if not present_bit:
                        self.index_100[tuple_107_108[0]].append(tuple_107_108[1])
                    # Program VectorAppend Region
                    vec_134.append(var_107)
            # Program TupleCompare Region
            if self.var_3 == var_109:
                # Program TransitionState Region
                tuple_107_108 = (var_107, var_108)
                prev_state = self.table_31[tuple_107_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_31[tuple_107_108] = 1 | 4
                    if not present_bit:
                        self.index_94[tuple_107_108[0]].append(tuple_107_108[1])
                    # Program VectorAppend Region
                    vec_126.append(var_107)
            # Program TupleCompare Region
            if self.var_4 == var_109:
                # Program TransitionState Region
                tuple_107_108 = (var_107, var_108)
                prev_state = self.table_34[tuple_107_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_34[tuple_107_108] = 1 | 4
                    if not present_bit:
                        self.index_88[tuple_107_108[0]].append(tuple_107_108[1])
                    # Program VectorAppend Region
                    vec_118.append(var_107)
            # Program TupleCompare Region
            if self.var_5 == var_109:
                # Program TransitionState Region
                tuple_107_108 = (var_107, var_108)
                prev_state = self.table_37[tuple_107_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_37[tuple_107_108] = 1 | 4
                    if not present_bit:
                        self.index_82[tuple_107_108[0]].append(tuple_107_108[1])
                    # Program VectorAppend Region
                    vec_110.append(var_107)
        # Program VectorUnique Region
        vec_110 = list(set(vec_110))
        vec_index110 = 0
        # Program TableJoin Region
        while vec_index110 < len(vec_110):
            var_112 = vec_110[vec_index110]
            vec_index110 += 1
            tuple_111_0_index: int = 0
            tuple_111_0_vec: List[int] = self.index_81[var_112]
            while tuple_111_0_index < len(tuple_111_0_vec):
                tuple_111_0 = tuple_111_0_vec[tuple_111_0_index]
                tuple_111_0_index += 1
                var_113 = tuple_111_0
                tuple_111_1_index: int = 0
                tuple_111_1_vec: List[int] = self.index_82[var_112]
                while tuple_111_1_index < len(tuple_111_1_vec):
                    tuple_111_1 = tuple_111_1_vec[tuple_111_1_index]
                    tuple_111_1_index += 1
                    var_114 = tuple_111_1
                    # Program TransitionState Region
                    tuple_113_114 = (var_113, var_114)
                    prev_state = self.table_6[tuple_113_114]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_113_114] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_113_114[1]].append(tuple_113_114[0])
                            self.index_149[tuple_113_114[0]].append(tuple_113_114[1])
                        # Program VectorAppend Region
                        vec_115.append((var_113, var_114))
        # Program VectorClear Region
        del vec_110[:]
        vec_index110 = 0
        # Program VectorUnique Region
        vec_118 = list(set(vec_118))
        vec_index118 = 0
        # Program TableJoin Region
        while vec_index118 < len(vec_118):
            var_120 = vec_118[vec_index118]
            vec_index118 += 1
            tuple_119_0_index: int = 0
            tuple_119_0_vec: List[int] = self.index_81[var_120]
            while tuple_119_0_index < len(tuple_119_0_vec):
                tuple_119_0 = tuple_119_0_vec[tuple_119_0_index]
                tuple_119_0_index += 1
                var_121 = tuple_119_0
                tuple_119_1_index: int = 0
                tuple_119_1_vec: List[int] = self.index_88[var_120]
                while tuple_119_1_index < len(tuple_119_1_vec):
                    tuple_119_1 = tuple_119_1_vec[tuple_119_1_index]
                    tuple_119_1_index += 1
                    var_122 = tuple_119_1
                    # Program TransitionState Region
                    tuple_121_122 = (var_121, var_122)
                    prev_state = self.table_6[tuple_121_122]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_121_122] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_121_122[1]].append(tuple_121_122[0])
                            self.index_149[tuple_121_122[0]].append(tuple_121_122[1])
                        # Program VectorAppend Region
                        vec_123.append((var_121, var_122))
        # Program VectorClear Region
        del vec_118[:]
        vec_index118 = 0
        # Program VectorUnique Region
        vec_126 = list(set(vec_126))
        vec_index126 = 0
        # Program TableJoin Region
        while vec_index126 < len(vec_126):
            var_128 = vec_126[vec_index126]
            vec_index126 += 1
            tuple_127_0_index: int = 0
            tuple_127_0_vec: List[int] = self.index_81[var_128]
            while tuple_127_0_index < len(tuple_127_0_vec):
                tuple_127_0 = tuple_127_0_vec[tuple_127_0_index]
                tuple_127_0_index += 1
                var_129 = tuple_127_0
                tuple_127_1_index: int = 0
                tuple_127_1_vec: List[int] = self.index_94[var_128]
                while tuple_127_1_index < len(tuple_127_1_vec):
                    tuple_127_1 = tuple_127_1_vec[tuple_127_1_index]
                    tuple_127_1_index += 1
                    var_130 = tuple_127_1
                    # Program TransitionState Region
                    tuple_129_130 = (var_129, var_130)
                    prev_state = self.table_6[tuple_129_130]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_129_130] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_129_130[1]].append(tuple_129_130[0])
                            self.index_149[tuple_129_130[0]].append(tuple_129_130[1])
                        # Program VectorAppend Region
                        vec_131.append((var_129, var_130))
        # Program VectorClear Region
        del vec_126[:]
        vec_index126 = 0
        # Program VectorUnique Region
        vec_134 = list(set(vec_134))
        vec_index134 = 0
        # Program TableJoin Region
        while vec_index134 < len(vec_134):
            var_136 = vec_134[vec_index134]
            vec_index134 += 1
            tuple_135_0_index: int = 0
            tuple_135_0_vec: List[int] = self.index_81[var_136]
            while tuple_135_0_index < len(tuple_135_0_vec):
                tuple_135_0 = tuple_135_0_vec[tuple_135_0_index]
                tuple_135_0_index += 1
                var_137 = tuple_135_0
                tuple_135_1_index: int = 0
                tuple_135_1_vec: List[int] = self.index_100[var_136]
                while tuple_135_1_index < len(tuple_135_1_vec):
                    tuple_135_1 = tuple_135_1_vec[tuple_135_1_index]
                    tuple_135_1_index += 1
                    var_138 = tuple_135_1
                    # Program TransitionState Region
                    tuple_137_138 = (var_137, var_138)
                    prev_state = self.table_6[tuple_137_138]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_137_138] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_137_138[1]].append(tuple_137_138[0])
                            self.index_149[tuple_137_138[0]].append(tuple_137_138[1])
                        # Program VectorAppend Region
                        vec_139.append((var_137, var_138))
        # Program VectorClear Region
        del vec_134[:]
        vec_index134 = 0
        # Program VectorUnique Region
        vec_142 = list(set(vec_142))
        vec_index142 = 0
        # Program TableJoin Region
        while vec_index142 < len(vec_142):
            var_144 = vec_142[vec_index142]
            vec_index142 += 1
            if var_144 in self.index_65:
                tuple_143_1_index: int = 0
                tuple_143_1_vec: List[int] = self.index_66[var_144]
                while tuple_143_1_index < len(tuple_143_1_vec):
                    tuple_143_1 = tuple_143_1_vec[tuple_143_1_index]
                    tuple_143_1_index += 1
                    var_145 = tuple_143_1
                    # Program TransitionState Region
                    tuple_144_145 = (var_144, var_145)
                    prev_state = self.table_6[tuple_144_145]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_144_145] = 1 | 4
                        if not present_bit:
                            self.index_81[tuple_144_145[1]].append(tuple_144_145[0])
                            self.index_149[tuple_144_145[0]].append(tuple_144_145[1])
                        # Program VectorAppend Region
                        vec_146.append((var_145, var_145))
        # Program VectorClear Region
        del vec_142[:]
        vec_index142 = 0
        # Induction Fixpoint Loop Region
        while len(vec_115) or len(vec_123) or len(vec_131) or len(vec_139) or len(vec_146):
            # Program Series Region
            # Program Call Region
            ret = self.proc_70_(vec_146)

            # Program Call Region
            param_148_0 = [vec_146]
            ret = self.proc_68_(param_148_0)
            vec_146 = param_148_0[0]

            # Program Call Region
            ret = self.proc_70_(vec_139)

            # Program Call Region
            param_141_0 = [vec_139]
            ret = self.proc_68_(param_141_0)
            vec_139 = param_141_0[0]

            # Program Call Region
            ret = self.proc_70_(vec_131)

            # Program Call Region
            param_133_0 = [vec_131]
            ret = self.proc_68_(param_133_0)
            vec_131 = param_133_0[0]

            # Program Call Region
            ret = self.proc_70_(vec_123)

            # Program Call Region
            param_125_0 = [vec_123]
            ret = self.proc_68_(param_125_0)
            vec_123 = param_125_0[0]

            # Program Call Region
            ret = self.proc_70_(vec_115)

            # Program Call Region
            param_117_0 = [vec_115]
            ret = self.proc_68_(param_117_0)
            vec_115 = param_117_0[0]

        vec_index115 = 0
        vec_index123 = 0
        vec_index131 = 0
        vec_index139 = 0
        vec_index146 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_146[:]
        vec_index146 = 0
        # Program VectorClear Region
        del vec_139[:]
        vec_index139 = 0
        # Program VectorClear Region
        del vec_131[:]
        vec_index131 = 0
        # Program VectorClear Region
        del vec_123[:]
        vec_index123 = 0
        # Program VectorClear Region
        del vec_115[:]
        vec_index115 = 0
        # Program Return Region
        return False

    def get_function_instructions_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_149[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_6[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_section_instructions_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_150[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_9[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_instructions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_12:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_12[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_functions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_14:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_14[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_sections_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_16:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_16[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

