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

class Database:

    def __init__(self, log: DatabaseLog, functors: DatabaseFunctors):
        self._log: DatabaseLog = log
        self._functors: DatabaseFunctors = functors
        self._refs: DefaultDict[int, List[object]] = defaultdict(list)

        self.table_7: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_90: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_148: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_10: DefaultDict[int, int] = defaultdict(int)
        self.index_151 = self.table_10

        self.table_12: DefaultDict[int, int] = defaultdict(int)

        self.table_14: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_91: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_17: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_149: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_20: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_150: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_23: DefaultDict[bytes, int] = defaultdict(int)

        self.table_25: DefaultDict[Tuple[bytes, int, int, int], int] = defaultdict(int)
        self.index_58: DefaultDict[bytes, List[Tuple[int, int, int]]] = defaultdict(list)

        self.table_30: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_59: DefaultDict[bytes, List[Tuple[int, int, bytes]]] = defaultdict(list)
        self.index_69: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_35: DefaultDict[Tuple[int, bytes, int, int], int] = defaultdict(int)
        self.index_70: DefaultDict[int, List[Tuple[int, bytes, int]]] = defaultdict(list)

        self.table_40: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_134: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_44: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_135: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.var_0: int = 1
        self.var_1: int = 5
        self.var_2: int = 6
        self.var_3: int = 0
        self.var_4: int = 3
        self.var_5: int = 4
        self.var_6: int = 2
        self.init_48_()

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

    def init_48_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False

    def section_4(self, vec_50: List[Tuple[bytes, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index50: int = 0
        vec_55: List[bytes] = list()
        vec_index55: int = 0
        vec_66: List[int] = list()
        vec_index66: int = 0
        vec_81: List[Tuple[int, int]] = list()
        vec_index81: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index50 = 0
        while vec_index50 < len(vec_50):
            var_51, var_52, var_53, var_54 = vec_50[vec_index50]
            vec_index50 += 1
            # Program Parallel Region
            # Program TransitionState Region
            var_54 = self._resolve_sectype(var_54)
            tuple_51_52_53_54 = (var_51, var_52, var_53, var_54)
            prev_state = self.table_25[tuple_51_52_53_54]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_25[tuple_51_52_53_54] = 1 | 4
                if not present_bit:
                    self.index_58[tuple_51_52_53_54[0]].append((tuple_51_52_53_54[1], tuple_51_52_53_54[2], tuple_51_52_53_54[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_51 = var_51
                prev_state = self.table_23[tuple_51]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_23[tuple_51] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_55.append(var_51)
                # Program TupleCompare Region
                if self.var_0 == var_54:
                    # Program TransitionState Region
                    tuple_0_51_52_53 = (self.var_0, var_51, var_52, var_53)
                    prev_state = self.table_35[tuple_0_51_52_53]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_35[tuple_0_51_52_53] = 1 | 4
                        if not present_bit:
                            self.index_70[tuple_0_51_52_53[2]].append((tuple_0_51_52_53[0], tuple_0_51_52_53[1], tuple_0_51_52_53[3]))
                        # Program VectorAppend Region
                        vec_66.append(var_52)
            # Program TransitionState Region
            var_54 = self._resolve_sectype(var_54)
            tuple_51_52_53_54 = (var_51, var_52, var_53, var_54)
            prev_state = self.table_25[tuple_51_52_53_54]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_25[tuple_51_52_53_54] = 1 | 4
                if not present_bit:
                    self.index_58[tuple_51_52_53_54[0]].append((tuple_51_52_53_54[1], tuple_51_52_53_54[2], tuple_51_52_53_54[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_51 = var_51
                prev_state = self.table_23[tuple_51]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_23[tuple_51] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_55.append(var_51)
                # Program TupleCompare Region
                if self.var_0 == var_54:
                    # Program TransitionState Region
                    tuple_0_51_52_53 = (self.var_0, var_51, var_52, var_53)
                    prev_state = self.table_35[tuple_0_51_52_53]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_35[tuple_0_51_52_53] = 1 | 4
                        if not present_bit:
                            self.index_70[tuple_0_51_52_53[2]].append((tuple_0_51_52_53[0], tuple_0_51_52_53[1], tuple_0_51_52_53[3]))
                        # Program VectorAppend Region
                        vec_66.append(var_52)
            # Program TransitionState Region
            var_54 = self._resolve_sectype(var_54)
            tuple_51_52_53_54 = (var_51, var_52, var_53, var_54)
            prev_state = self.table_25[tuple_51_52_53_54]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_25[tuple_51_52_53_54] = 1 | 4
                if not present_bit:
                    self.index_58[tuple_51_52_53_54[0]].append((tuple_51_52_53_54[1], tuple_51_52_53_54[2], tuple_51_52_53_54[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_51 = var_51
                prev_state = self.table_23[tuple_51]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_23[tuple_51] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_55.append(var_51)
                # Program TupleCompare Region
                if self.var_0 == var_54:
                    # Program TransitionState Region
                    tuple_0_51_52_53 = (self.var_0, var_51, var_52, var_53)
                    prev_state = self.table_35[tuple_0_51_52_53]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_35[tuple_0_51_52_53] = 1 | 4
                        if not present_bit:
                            self.index_70[tuple_0_51_52_53[2]].append((tuple_0_51_52_53[0], tuple_0_51_52_53[1], tuple_0_51_52_53[3]))
                        # Program VectorAppend Region
                        vec_66.append(var_52)
        # Program VectorUnique Region
        vec_55 = list(set(vec_55))
        vec_index55 = 0
        # Program TableJoin Region
        while vec_index55 < len(vec_55):
            var_57 = vec_55[vec_index55]
            vec_index55 += 1
            tuple_56_0_index: int = 0
            tuple_56_0_vec: List[Tuple[int, int, int]] = self.index_58[var_57]
            while tuple_56_0_index < len(tuple_56_0_vec):
                tuple_56_0 = tuple_56_0_vec[tuple_56_0_index]
                tuple_56_0_index += 1
                var_60 = tuple_56_0[0]
                var_61 = tuple_56_0[1]
                var_62 = tuple_56_0[2]
                tuple_56_1_index: int = 0
                tuple_56_1_vec: List[Tuple[int, int, bytes]] = self.index_59[var_57]
                while tuple_56_1_index < len(tuple_56_1_vec):
                    tuple_56_1 = tuple_56_1_vec[tuple_56_1_index]
                    tuple_56_1_index += 1
                    var_63 = tuple_56_1[0]
                    var_64 = tuple_56_1[1]
                    var_65 = tuple_56_1[2]
                    # Program TransitionState Region
                    tuple_57_63 = (var_57, var_63)
                    prev_state = self.table_20[tuple_57_63]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_57_63] = 1 | 4
                        if not present_bit:
                            self.index_150[tuple_57_63[0]].append(tuple_57_63[1])
        # Program VectorClear Region
        del vec_55[:]
        vec_index55 = 0
        # Program VectorUnique Region
        vec_66 = list(set(vec_66))
        vec_index66 = 0
        # Program TableJoin Region
        while vec_index66 < len(vec_66):
            var_68 = vec_66[vec_index66]
            vec_index66 += 1
            tuple_67_0_index: int = 0
            tuple_67_0_vec: List[Tuple[int, bytes, bytes]] = self.index_69[var_68]
            while tuple_67_0_index < len(tuple_67_0_vec):
                tuple_67_0 = tuple_67_0_vec[tuple_67_0_index]
                tuple_67_0_index += 1
                var_71 = tuple_67_0[0]
                var_72 = tuple_67_0[1]
                var_73 = tuple_67_0[2]
                tuple_67_1_index: int = 0
                tuple_67_1_vec: List[Tuple[int, bytes, int]] = self.index_70[var_68]
                while tuple_67_1_index < len(tuple_67_1_vec):
                    tuple_67_1 = tuple_67_1_vec[tuple_67_1_index]
                    tuple_67_1_index += 1
                    var_74 = tuple_67_1[0]
                    var_75 = tuple_67_1[1]
                    var_76 = tuple_67_1[2]
                    # Program TupleCompare Region
                    if self.var_0 == var_74:
                        # Program TransitionState Region
                        tuple_68 = var_68
                        prev_state = self.table_10[tuple_68]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_10[tuple_68] = 1 | 4
                            if not present_bit:
                                pass
                            # Program TransitionState Region
                            tuple_68_68 = (var_68, var_68)
                            prev_state = self.table_7[tuple_68_68]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_7[tuple_68_68] = 1 | 4
                                if not present_bit:
                                    self.index_90[tuple_68_68[1]].append(tuple_68_68[0])
                                    self.index_148[tuple_68_68[0]].append(tuple_68_68[1])
                                # Program VectorAppend Region
                                vec_81.append((var_68, var_68))
        # Program VectorClear Region
        del vec_66[:]
        vec_index66 = 0
        # Induction Fixpoint Loop Region
        while len(vec_81):
            # Program Call Region
            param_83_0 = [vec_81]
            ret = self.proc_77_(param_83_0)
            vec_81 = param_83_0[0]

        vec_index81 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_81[:]
        vec_index81 = 0
        # Program Return Region
        return False

    def proc_77_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_78 = param_0[0]
        vec_index78: int = 0
        vec_84: List[Tuple[int, int]] = list()
        vec_index84: int = 0
        vec_87: List[int] = list()
        vec_index87: int = 0
        vec_94: List[Tuple[int, int]] = list()
        vec_index94: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorSwap Region
        vec_78, vec_84 = vec_84, vec_78
        # Program VectorLoop Region
        while vec_index84 < len(vec_84):
            var_85, var_86 = vec_84[vec_index84]
            vec_index84 += 1
            # Program VectorAppend Region
            vec_87.append(var_86)
        # Program VectorUnique Region
        vec_87 = list(set(vec_87))
        vec_index87 = 0
        # Program TableJoin Region
        while vec_index87 < len(vec_87):
            var_89 = vec_87[vec_index87]
            vec_index87 += 1
            tuple_88_0_index: int = 0
            tuple_88_0_vec: List[int] = self.index_90[var_89]
            while tuple_88_0_index < len(tuple_88_0_vec):
                tuple_88_0 = tuple_88_0_vec[tuple_88_0_index]
                tuple_88_0_index += 1
                var_92 = tuple_88_0
                tuple_88_1_index: int = 0
                tuple_88_1_vec: List[int] = self.index_91[var_89]
                while tuple_88_1_index < len(tuple_88_1_vec):
                    tuple_88_1 = tuple_88_1_vec[tuple_88_1_index]
                    tuple_88_1_index += 1
                    var_93 = tuple_88_1
                    # Program TransitionState Region
                    tuple_92_93 = (var_92, var_93)
                    prev_state = self.table_7[tuple_92_93]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_7[tuple_92_93] = 1 | 4
                        if not present_bit:
                            self.index_90[tuple_92_93[1]].append(tuple_92_93[0])
                            self.index_148[tuple_92_93[0]].append(tuple_92_93[1])
                        # Program VectorAppend Region
                        vec_94.append((var_92, var_93))
        # Program VectorClear Region
        del vec_87[:]
        vec_index87 = 0
        # Induction Fixpoint Loop Region
        while len(vec_94):
            # Program Call Region
            param_96_0 = [vec_94]
            ret = self.proc_77_(param_96_0)
            vec_94 = param_96_0[0]

        vec_index94 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_94[:]
        vec_index94 = 0
        # Program Return Region
        param_0[0] = vec_78
        return False

    def instruction_4(self, vec_100: List[Tuple[int, int, bytes, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index100: int = 0
        vec_105: List[bytes] = list()
        vec_index105: int = 0
        vec_114: List[int] = list()
        vec_index114: int = 0
        vec_123: List[Tuple[int, int]] = list()
        vec_index123: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index100 = 0
        while vec_index100 < len(vec_100):
            var_101, var_102, var_103, var_104 = vec_100[vec_index100]
            vec_index100 += 1
            # Program Parallel Region
            # Program TransitionState Region
            var_102 = self._resolve_insntype(var_102)
            tuple_101_102_103_104 = (var_101, var_102, var_103, var_104)
            prev_state = self.table_30[tuple_101_102_103_104]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_101_102_103_104] = 1 | 4
                if not present_bit:
                    self.index_59[tuple_101_102_103_104[3]].append((tuple_101_102_103_104[0], tuple_101_102_103_104[1], tuple_101_102_103_104[2]))
                    self.index_69[tuple_101_102_103_104[0]].append((tuple_101_102_103_104[1], tuple_101_102_103_104[2], tuple_101_102_103_104[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_101 = var_101
                prev_state = self.table_12[tuple_101]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_12[tuple_101] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_105.append(var_104)
                # Program VectorAppend Region
                vec_114.append(var_101)
            # Program TransitionState Region
            var_102 = self._resolve_insntype(var_102)
            tuple_101_102_103_104 = (var_101, var_102, var_103, var_104)
            prev_state = self.table_30[tuple_101_102_103_104]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_101_102_103_104] = 1 | 4
                if not present_bit:
                    self.index_59[tuple_101_102_103_104[3]].append((tuple_101_102_103_104[0], tuple_101_102_103_104[1], tuple_101_102_103_104[2]))
                    self.index_69[tuple_101_102_103_104[0]].append((tuple_101_102_103_104[1], tuple_101_102_103_104[2], tuple_101_102_103_104[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_101 = var_101
                prev_state = self.table_12[tuple_101]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_12[tuple_101] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_105.append(var_104)
                # Program VectorAppend Region
                vec_114.append(var_101)
            # Program TransitionState Region
            var_102 = self._resolve_insntype(var_102)
            tuple_101_102_103_104 = (var_101, var_102, var_103, var_104)
            prev_state = self.table_30[tuple_101_102_103_104]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_101_102_103_104] = 1 | 4
                if not present_bit:
                    self.index_59[tuple_101_102_103_104[3]].append((tuple_101_102_103_104[0], tuple_101_102_103_104[1], tuple_101_102_103_104[2]))
                    self.index_69[tuple_101_102_103_104[0]].append((tuple_101_102_103_104[1], tuple_101_102_103_104[2], tuple_101_102_103_104[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_101 = var_101
                prev_state = self.table_12[tuple_101]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_12[tuple_101] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_105.append(var_104)
                # Program VectorAppend Region
                vec_114.append(var_101)
        # Program VectorUnique Region
        vec_105 = list(set(vec_105))
        vec_index105 = 0
        # Program TableJoin Region
        while vec_index105 < len(vec_105):
            var_107 = vec_105[vec_index105]
            vec_index105 += 1
            tuple_106_0_index: int = 0
            tuple_106_0_vec: List[Tuple[int, int, int]] = self.index_58[var_107]
            while tuple_106_0_index < len(tuple_106_0_vec):
                tuple_106_0 = tuple_106_0_vec[tuple_106_0_index]
                tuple_106_0_index += 1
                var_108 = tuple_106_0[0]
                var_109 = tuple_106_0[1]
                var_110 = tuple_106_0[2]
                tuple_106_1_index: int = 0
                tuple_106_1_vec: List[Tuple[int, int, bytes]] = self.index_59[var_107]
                while tuple_106_1_index < len(tuple_106_1_vec):
                    tuple_106_1 = tuple_106_1_vec[tuple_106_1_index]
                    tuple_106_1_index += 1
                    var_111 = tuple_106_1[0]
                    var_112 = tuple_106_1[1]
                    var_113 = tuple_106_1[2]
                    # Program TransitionState Region
                    tuple_107_111 = (var_107, var_111)
                    prev_state = self.table_20[tuple_107_111]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_107_111] = 1 | 4
                        if not present_bit:
                            self.index_150[tuple_107_111[0]].append(tuple_107_111[1])
        # Program VectorClear Region
        del vec_105[:]
        vec_index105 = 0
        # Program VectorUnique Region
        vec_114 = list(set(vec_114))
        vec_index114 = 0
        # Program TableJoin Region
        while vec_index114 < len(vec_114):
            var_116 = vec_114[vec_index114]
            vec_index114 += 1
            tuple_115_0_index: int = 0
            tuple_115_0_vec: List[Tuple[int, bytes, bytes]] = self.index_69[var_116]
            while tuple_115_0_index < len(tuple_115_0_vec):
                tuple_115_0 = tuple_115_0_vec[tuple_115_0_index]
                tuple_115_0_index += 1
                var_117 = tuple_115_0[0]
                var_118 = tuple_115_0[1]
                var_119 = tuple_115_0[2]
                tuple_115_1_index: int = 0
                tuple_115_1_vec: List[Tuple[int, bytes, int]] = self.index_70[var_116]
                while tuple_115_1_index < len(tuple_115_1_vec):
                    tuple_115_1 = tuple_115_1_vec[tuple_115_1_index]
                    tuple_115_1_index += 1
                    var_120 = tuple_115_1[0]
                    var_121 = tuple_115_1[1]
                    var_122 = tuple_115_1[2]
                    # Program TupleCompare Region
                    if self.var_0 == var_120:
                        # Program TransitionState Region
                        tuple_116 = var_116
                        prev_state = self.table_10[tuple_116]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_10[tuple_116] = 1 | 4
                            if not present_bit:
                                pass
                            # Program TransitionState Region
                            tuple_116_116 = (var_116, var_116)
                            prev_state = self.table_7[tuple_116_116]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_7[tuple_116_116] = 1 | 4
                                if not present_bit:
                                    self.index_90[tuple_116_116[1]].append(tuple_116_116[0])
                                    self.index_148[tuple_116_116[0]].append(tuple_116_116[1])
                                # Program VectorAppend Region
                                vec_123.append((var_116, var_116))
        # Program VectorClear Region
        del vec_114[:]
        vec_index114 = 0
        # Induction Fixpoint Loop Region
        while len(vec_123):
            # Program Call Region
            param_125_0 = [vec_123]
            ret = self.proc_77_(param_125_0)
            vec_123 = param_125_0[0]

        vec_index123 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_123[:]
        vec_index123 = 0
        # Program Return Region
        return False

    def transfer_3(self, vec_127: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index127: int = 0
        vec_131: List[int] = list()
        vec_index131: int = 0
        vec_140: List[Tuple[int, int]] = list()
        vec_index140: int = 0
        vec_143: List[int] = list()
        vec_index143: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index127 = 0
        while vec_index127 < len(vec_127):
            var_128, var_129, var_130 = vec_127[vec_index127]
            vec_index127 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_1 == var_130:
                # Program TransitionState Region
                tuple_1_128_129 = (self.var_1, var_128, var_129)
                prev_state = self.table_40[tuple_1_128_129]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_40[tuple_1_128_129] = 1 | 4
                    if not present_bit:
                        self.index_134[tuple_1_128_129[1]].append((tuple_1_128_129[0], tuple_1_128_129[2]))
                    # Program VectorAppend Region
                    vec_131.append(var_128)
            # Program TupleCompare Region
            if self.var_2 == var_130:
                # Program TransitionState Region
                tuple_2_128_129 = (self.var_2, var_128, var_129)
                prev_state = self.table_44[tuple_2_128_129]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_44[tuple_2_128_129] = 1 | 4
                    if not present_bit:
                        self.index_135[tuple_2_128_129[1]].append((tuple_2_128_129[0], tuple_2_128_129[2]))
                    # Program VectorAppend Region
                    vec_131.append(var_128)
            # Program TupleCompare Region
            if self.var_3 == var_130:
                # Program TransitionState Region
                tuple_128_129 = (var_128, var_129)
                prev_state = self.table_14[tuple_128_129]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_14[tuple_128_129] = 1 | 4
                    if not present_bit:
                        self.index_91[tuple_128_129[0]].append(tuple_128_129[1])
                    # Program VectorAppend Region
                    vec_143.append(var_128)
            # Program TupleCompare Region
            if self.var_4 == var_130:
                # Program TransitionState Region
                tuple_128_129 = (var_128, var_129)
                prev_state = self.table_14[tuple_128_129]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_14[tuple_128_129] = 1 | 4
                    if not present_bit:
                        self.index_91[tuple_128_129[0]].append(tuple_128_129[1])
                    # Program VectorAppend Region
                    vec_143.append(var_128)
            # Program TupleCompare Region
            if self.var_5 == var_130:
                # Program TransitionState Region
                tuple_128_129 = (var_128, var_129)
                prev_state = self.table_14[tuple_128_129]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_14[tuple_128_129] = 1 | 4
                    if not present_bit:
                        self.index_91[tuple_128_129[0]].append(tuple_128_129[1])
                    # Program VectorAppend Region
                    vec_143.append(var_128)
            # Program TupleCompare Region
            if self.var_6 == var_130:
                # Program TransitionState Region
                tuple_128_129 = (var_128, var_129)
                prev_state = self.table_14[tuple_128_129]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_14[tuple_128_129] = 1 | 4
                    if not present_bit:
                        self.index_91[tuple_128_129[0]].append(tuple_128_129[1])
                    # Program VectorAppend Region
                    vec_143.append(var_128)
            # Program TupleCompare Region
            if self.var_2 == var_130:
                # Program TransitionState Region
                tuple_128_129 = (var_128, var_129)
                prev_state = self.table_14[tuple_128_129]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_14[tuple_128_129] = 1 | 4
                    if not present_bit:
                        self.index_91[tuple_128_129[0]].append(tuple_128_129[1])
                    # Program VectorAppend Region
                    vec_143.append(var_128)
        # Program VectorUnique Region
        vec_131 = list(set(vec_131))
        vec_index131 = 0
        # Program TableJoin Region
        while vec_index131 < len(vec_131):
            var_133 = vec_131[vec_index131]
            vec_index131 += 1
            tuple_132_0_index: int = 0
            tuple_132_0_vec: List[Tuple[int, int]] = self.index_134[var_133]
            while tuple_132_0_index < len(tuple_132_0_vec):
                tuple_132_0 = tuple_132_0_vec[tuple_132_0_index]
                tuple_132_0_index += 1
                var_136 = tuple_132_0[0]
                var_137 = tuple_132_0[1]
                tuple_132_1_index: int = 0
                tuple_132_1_vec: List[Tuple[int, int]] = self.index_135[var_133]
                while tuple_132_1_index < len(tuple_132_1_vec):
                    tuple_132_1 = tuple_132_1_vec[tuple_132_1_index]
                    tuple_132_1_index += 1
                    var_138 = tuple_132_1[0]
                    var_139 = tuple_132_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_136, var_138, ):
                        # Program TupleCompare Region
                        if var_137 != var_139:
                            # Program TransitionState Region
                            tuple_133_137 = (var_133, var_137)
                            prev_state = self.table_17[tuple_133_137]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_17[tuple_133_137] = 1 | 4
                                if not present_bit:
                                    self.index_149[tuple_133_137[0]].append(tuple_133_137[1])
                                # Program TransitionState Region
                                tuple_137 = var_137
                                prev_state = self.table_10[tuple_137]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_10[tuple_137] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program TransitionState Region
                                    tuple_137_137 = (var_137, var_137)
                                    prev_state = self.table_7[tuple_137_137]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_7[tuple_137_137] = 1 | 4
                                        if not present_bit:
                                            self.index_90[tuple_137_137[1]].append(tuple_137_137[0])
                                            self.index_148[tuple_137_137[0]].append(tuple_137_137[1])
                                        # Program VectorAppend Region
                                        vec_140.append((var_137, var_137))
        # Program VectorClear Region
        del vec_131[:]
        vec_index131 = 0
        # Program VectorUnique Region
        vec_143 = list(set(vec_143))
        vec_index143 = 0
        # Program TableJoin Region
        while vec_index143 < len(vec_143):
            var_145 = vec_143[vec_index143]
            vec_index143 += 1
            tuple_144_0_index: int = 0
            tuple_144_0_vec: List[int] = self.index_90[var_145]
            while tuple_144_0_index < len(tuple_144_0_vec):
                tuple_144_0 = tuple_144_0_vec[tuple_144_0_index]
                tuple_144_0_index += 1
                var_146 = tuple_144_0
                tuple_144_1_index: int = 0
                tuple_144_1_vec: List[int] = self.index_91[var_145]
                while tuple_144_1_index < len(tuple_144_1_vec):
                    tuple_144_1 = tuple_144_1_vec[tuple_144_1_index]
                    tuple_144_1_index += 1
                    var_147 = tuple_144_1
                    # Program TransitionState Region
                    tuple_146_147 = (var_146, var_147)
                    prev_state = self.table_7[tuple_146_147]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_7[tuple_146_147] = 1 | 4
                        if not present_bit:
                            self.index_90[tuple_146_147[1]].append(tuple_146_147[0])
                            self.index_148[tuple_146_147[0]].append(tuple_146_147[1])
                        # Program VectorAppend Region
                        vec_140.append((var_146, var_147))
        # Program VectorClear Region
        del vec_143[:]
        vec_index143 = 0
        # Induction Fixpoint Loop Region
        while len(vec_140):
            # Program Call Region
            param_142_0 = [vec_140]
            ret = self.proc_77_(param_142_0)
            vec_140 = param_142_0[0]

        vec_index140 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_140[:]
        vec_index140 = 0
        # Program Return Region
        return False

    def get_functions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_10:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_10[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

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

    def intraproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_91[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_14[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_function_instructions_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_148[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_7[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def interproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_149[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_17[full_tuple] & 3
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
            state = self.table_20[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def function_b(self, param_0: int) -> bool:
        state: int = 0
        tuple_index: int = 0
        if True:
            full_tuple = param_0
            state = self.table_10[full_tuple] & 3
            if state != 1:
                return False
            return True

    def get_sections_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_23:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_23[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

