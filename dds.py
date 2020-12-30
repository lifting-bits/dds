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
        self.index_100: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_176: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_10: DefaultDict[int, int] = defaultdict(int)
        self.index_177 = self.table_10

        self.table_12: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_101: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_15: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_178: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_18: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_179: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_21: DefaultDict[int, int] = defaultdict(int)

        self.table_23: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_180: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_26: DefaultDict[bytes, int] = defaultdict(int)

        self.table_28: DefaultDict[Tuple[bytes, int, int, int], int] = defaultdict(int)
        self.index_68: DefaultDict[bytes, List[Tuple[int, int, int]]] = defaultdict(list)

        self.table_33: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_69: DefaultDict[bytes, List[Tuple[int, int, bytes]]] = defaultdict(list)
        self.index_79: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_38: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_144: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_42: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_145: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_45: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_152: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_49: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_153: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_53: DefaultDict[Tuple[int, bytes, int, int], int] = defaultdict(int)
        self.index_80: DefaultDict[int, List[Tuple[int, bytes, int]]] = defaultdict(list)

        self.var_0: int = 5
        self.var_1: int = 6
        self.var_2: int = 0
        self.var_3: int = 3
        self.var_4: int = 4
        self.var_5: int = 2
        self.var_6: int = 1
        self.init_58_()

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

    def init_58_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False

    def section_4(self, vec_60: List[Tuple[bytes, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index60: int = 0
        vec_65: List[bytes] = list()
        vec_index65: int = 0
        vec_76: List[int] = list()
        vec_index76: int = 0
        vec_91: List[Tuple[int, int]] = list()
        vec_index91: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index60 = 0
        while vec_index60 < len(vec_60):
            var_61, var_62, var_63, var_64 = vec_60[vec_index60]
            vec_index60 += 1
            # Program Parallel Region
            # Program TransitionState Region
            var_64 = self._resolve_sectype(var_64)
            tuple_61_62_63_64 = (var_61, var_62, var_63, var_64)
            prev_state = self.table_28[tuple_61_62_63_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_28[tuple_61_62_63_64] = 1 | 4
                if not present_bit:
                    self.index_68[tuple_61_62_63_64[0]].append((tuple_61_62_63_64[1], tuple_61_62_63_64[2], tuple_61_62_63_64[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_61 = var_61
                prev_state = self.table_26[tuple_61]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_26[tuple_61] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_65.append(var_61)
                # Program TupleCompare Region
                if self.var_6 == var_64:
                    # Program TransitionState Region
                    tuple_6_61_62_63 = (self.var_6, var_61, var_62, var_63)
                    prev_state = self.table_53[tuple_6_61_62_63]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_53[tuple_6_61_62_63] = 1 | 4
                        if not present_bit:
                            self.index_80[tuple_6_61_62_63[2]].append((tuple_6_61_62_63[0], tuple_6_61_62_63[1], tuple_6_61_62_63[3]))
                        # Program VectorAppend Region
                        vec_76.append(var_62)
            # Program TransitionState Region
            var_64 = self._resolve_sectype(var_64)
            tuple_61_62_63_64 = (var_61, var_62, var_63, var_64)
            prev_state = self.table_28[tuple_61_62_63_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_28[tuple_61_62_63_64] = 1 | 4
                if not present_bit:
                    self.index_68[tuple_61_62_63_64[0]].append((tuple_61_62_63_64[1], tuple_61_62_63_64[2], tuple_61_62_63_64[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_61 = var_61
                prev_state = self.table_26[tuple_61]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_26[tuple_61] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_65.append(var_61)
                # Program TupleCompare Region
                if self.var_6 == var_64:
                    # Program TransitionState Region
                    tuple_6_61_62_63 = (self.var_6, var_61, var_62, var_63)
                    prev_state = self.table_53[tuple_6_61_62_63]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_53[tuple_6_61_62_63] = 1 | 4
                        if not present_bit:
                            self.index_80[tuple_6_61_62_63[2]].append((tuple_6_61_62_63[0], tuple_6_61_62_63[1], tuple_6_61_62_63[3]))
                        # Program VectorAppend Region
                        vec_76.append(var_62)
            # Program TransitionState Region
            var_64 = self._resolve_sectype(var_64)
            tuple_61_62_63_64 = (var_61, var_62, var_63, var_64)
            prev_state = self.table_28[tuple_61_62_63_64]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_28[tuple_61_62_63_64] = 1 | 4
                if not present_bit:
                    self.index_68[tuple_61_62_63_64[0]].append((tuple_61_62_63_64[1], tuple_61_62_63_64[2], tuple_61_62_63_64[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_61 = var_61
                prev_state = self.table_26[tuple_61]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_26[tuple_61] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_65.append(var_61)
                # Program TupleCompare Region
                if self.var_6 == var_64:
                    # Program TransitionState Region
                    tuple_6_61_62_63 = (self.var_6, var_61, var_62, var_63)
                    prev_state = self.table_53[tuple_6_61_62_63]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_53[tuple_6_61_62_63] = 1 | 4
                        if not present_bit:
                            self.index_80[tuple_6_61_62_63[2]].append((tuple_6_61_62_63[0], tuple_6_61_62_63[1], tuple_6_61_62_63[3]))
                        # Program VectorAppend Region
                        vec_76.append(var_62)
        # Program VectorUnique Region
        vec_65 = list(set(vec_65))
        vec_index65 = 0
        # Program TableJoin Region
        while vec_index65 < len(vec_65):
            var_67 = vec_65[vec_index65]
            vec_index65 += 1
            tuple_66_0_index: int = 0
            tuple_66_0_vec: List[Tuple[int, int, int]] = self.index_68[var_67]
            while tuple_66_0_index < len(tuple_66_0_vec):
                tuple_66_0 = tuple_66_0_vec[tuple_66_0_index]
                tuple_66_0_index += 1
                var_70 = tuple_66_0[0]
                var_71 = tuple_66_0[1]
                var_72 = tuple_66_0[2]
                tuple_66_1_index: int = 0
                tuple_66_1_vec: List[Tuple[int, int, bytes]] = self.index_69[var_67]
                while tuple_66_1_index < len(tuple_66_1_vec):
                    tuple_66_1 = tuple_66_1_vec[tuple_66_1_index]
                    tuple_66_1_index += 1
                    var_73 = tuple_66_1[0]
                    var_74 = tuple_66_1[1]
                    var_75 = tuple_66_1[2]
                    # Program TransitionState Region
                    tuple_67_73 = (var_67, var_73)
                    prev_state = self.table_23[tuple_67_73]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_23[tuple_67_73] = 1 | 4
                        if not present_bit:
                            self.index_180[tuple_67_73[0]].append(tuple_67_73[1])
        # Program VectorClear Region
        del vec_65[:]
        vec_index65 = 0
        # Program VectorUnique Region
        vec_76 = list(set(vec_76))
        vec_index76 = 0
        # Program TableJoin Region
        while vec_index76 < len(vec_76):
            var_78 = vec_76[vec_index76]
            vec_index76 += 1
            tuple_77_0_index: int = 0
            tuple_77_0_vec: List[Tuple[int, bytes, bytes]] = self.index_79[var_78]
            while tuple_77_0_index < len(tuple_77_0_vec):
                tuple_77_0 = tuple_77_0_vec[tuple_77_0_index]
                tuple_77_0_index += 1
                var_81 = tuple_77_0[0]
                var_82 = tuple_77_0[1]
                var_83 = tuple_77_0[2]
                tuple_77_1_index: int = 0
                tuple_77_1_vec: List[Tuple[int, bytes, int]] = self.index_80[var_78]
                while tuple_77_1_index < len(tuple_77_1_vec):
                    tuple_77_1 = tuple_77_1_vec[tuple_77_1_index]
                    tuple_77_1_index += 1
                    var_84 = tuple_77_1[0]
                    var_85 = tuple_77_1[1]
                    var_86 = tuple_77_1[2]
                    # Program TupleCompare Region
                    if self.var_6 == var_84:
                        # Program TransitionState Region
                        tuple_78 = var_78
                        prev_state = self.table_10[tuple_78]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_10[tuple_78] = 1 | 4
                            if not present_bit:
                                pass
                            # Program TransitionState Region
                            tuple_78_78 = (var_78, var_78)
                            prev_state = self.table_7[tuple_78_78]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_7[tuple_78_78] = 1 | 4
                                if not present_bit:
                                    self.index_100[tuple_78_78[1]].append(tuple_78_78[0])
                                    self.index_176[tuple_78_78[0]].append(tuple_78_78[1])
                                # Program VectorAppend Region
                                vec_91.append((var_78, var_78))
        # Program VectorClear Region
        del vec_76[:]
        vec_index76 = 0
        # Induction Fixpoint Loop Region
        while len(vec_91):
            # Program Call Region
            param_93_0 = [vec_91]
            ret = self.proc_87_(param_93_0)
            vec_91 = param_93_0[0]

        vec_index91 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_91[:]
        vec_index91 = 0
        # Program Return Region
        return False

    def proc_87_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_88 = param_0[0]
        vec_index88: int = 0
        vec_94: List[Tuple[int, int]] = list()
        vec_index94: int = 0
        vec_97: List[int] = list()
        vec_index97: int = 0
        vec_104: List[Tuple[int, int]] = list()
        vec_index104: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorSwap Region
        vec_88, vec_94 = vec_94, vec_88
        # Program VectorLoop Region
        while vec_index94 < len(vec_94):
            var_95, var_96 = vec_94[vec_index94]
            vec_index94 += 1
            # Program VectorAppend Region
            vec_97.append(var_96)
        # Program VectorUnique Region
        vec_97 = list(set(vec_97))
        vec_index97 = 0
        # Program TableJoin Region
        while vec_index97 < len(vec_97):
            var_99 = vec_97[vec_index97]
            vec_index97 += 1
            tuple_98_0_index: int = 0
            tuple_98_0_vec: List[int] = self.index_100[var_99]
            while tuple_98_0_index < len(tuple_98_0_vec):
                tuple_98_0 = tuple_98_0_vec[tuple_98_0_index]
                tuple_98_0_index += 1
                var_102 = tuple_98_0
                tuple_98_1_index: int = 0
                tuple_98_1_vec: List[int] = self.index_101[var_99]
                while tuple_98_1_index < len(tuple_98_1_vec):
                    tuple_98_1 = tuple_98_1_vec[tuple_98_1_index]
                    tuple_98_1_index += 1
                    var_103 = tuple_98_1
                    # Program TransitionState Region
                    tuple_102_103 = (var_102, var_103)
                    prev_state = self.table_7[tuple_102_103]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_7[tuple_102_103] = 1 | 4
                        if not present_bit:
                            self.index_100[tuple_102_103[1]].append(tuple_102_103[0])
                            self.index_176[tuple_102_103[0]].append(tuple_102_103[1])
                        # Program VectorAppend Region
                        vec_104.append((var_102, var_103))
        # Program VectorClear Region
        del vec_97[:]
        vec_index97 = 0
        # Induction Fixpoint Loop Region
        while len(vec_104):
            # Program Call Region
            param_106_0 = [vec_104]
            ret = self.proc_87_(param_106_0)
            vec_104 = param_106_0[0]

        vec_index104 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_104[:]
        vec_index104 = 0
        # Program Return Region
        param_0[0] = vec_88
        return False

    def instruction_4(self, vec_110: List[Tuple[int, int, bytes, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index110: int = 0
        vec_115: List[bytes] = list()
        vec_index115: int = 0
        vec_124: List[int] = list()
        vec_index124: int = 0
        vec_133: List[Tuple[int, int]] = list()
        vec_index133: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index110 = 0
        while vec_index110 < len(vec_110):
            var_111, var_112, var_113, var_114 = vec_110[vec_index110]
            vec_index110 += 1
            # Program Parallel Region
            # Program TransitionState Region
            var_112 = self._resolve_insntype(var_112)
            tuple_111_112_113_114 = (var_111, var_112, var_113, var_114)
            prev_state = self.table_33[tuple_111_112_113_114]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_111_112_113_114] = 1 | 4
                if not present_bit:
                    self.index_69[tuple_111_112_113_114[3]].append((tuple_111_112_113_114[0], tuple_111_112_113_114[1], tuple_111_112_113_114[2]))
                    self.index_79[tuple_111_112_113_114[0]].append((tuple_111_112_113_114[1], tuple_111_112_113_114[2], tuple_111_112_113_114[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_111 = var_111
                prev_state = self.table_21[tuple_111]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_111] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_115.append(var_114)
                # Program VectorAppend Region
                vec_124.append(var_111)
            # Program TransitionState Region
            var_112 = self._resolve_insntype(var_112)
            tuple_111_112_113_114 = (var_111, var_112, var_113, var_114)
            prev_state = self.table_33[tuple_111_112_113_114]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_111_112_113_114] = 1 | 4
                if not present_bit:
                    self.index_69[tuple_111_112_113_114[3]].append((tuple_111_112_113_114[0], tuple_111_112_113_114[1], tuple_111_112_113_114[2]))
                    self.index_79[tuple_111_112_113_114[0]].append((tuple_111_112_113_114[1], tuple_111_112_113_114[2], tuple_111_112_113_114[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_111 = var_111
                prev_state = self.table_21[tuple_111]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_111] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_115.append(var_114)
                # Program VectorAppend Region
                vec_124.append(var_111)
            # Program TransitionState Region
            var_112 = self._resolve_insntype(var_112)
            tuple_111_112_113_114 = (var_111, var_112, var_113, var_114)
            prev_state = self.table_33[tuple_111_112_113_114]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_111_112_113_114] = 1 | 4
                if not present_bit:
                    self.index_69[tuple_111_112_113_114[3]].append((tuple_111_112_113_114[0], tuple_111_112_113_114[1], tuple_111_112_113_114[2]))
                    self.index_79[tuple_111_112_113_114[0]].append((tuple_111_112_113_114[1], tuple_111_112_113_114[2], tuple_111_112_113_114[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_111 = var_111
                prev_state = self.table_21[tuple_111]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_111] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_115.append(var_114)
                # Program VectorAppend Region
                vec_124.append(var_111)
        # Program VectorUnique Region
        vec_115 = list(set(vec_115))
        vec_index115 = 0
        # Program TableJoin Region
        while vec_index115 < len(vec_115):
            var_117 = vec_115[vec_index115]
            vec_index115 += 1
            tuple_116_0_index: int = 0
            tuple_116_0_vec: List[Tuple[int, int, int]] = self.index_68[var_117]
            while tuple_116_0_index < len(tuple_116_0_vec):
                tuple_116_0 = tuple_116_0_vec[tuple_116_0_index]
                tuple_116_0_index += 1
                var_118 = tuple_116_0[0]
                var_119 = tuple_116_0[1]
                var_120 = tuple_116_0[2]
                tuple_116_1_index: int = 0
                tuple_116_1_vec: List[Tuple[int, int, bytes]] = self.index_69[var_117]
                while tuple_116_1_index < len(tuple_116_1_vec):
                    tuple_116_1 = tuple_116_1_vec[tuple_116_1_index]
                    tuple_116_1_index += 1
                    var_121 = tuple_116_1[0]
                    var_122 = tuple_116_1[1]
                    var_123 = tuple_116_1[2]
                    # Program TransitionState Region
                    tuple_117_121 = (var_117, var_121)
                    prev_state = self.table_23[tuple_117_121]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_23[tuple_117_121] = 1 | 4
                        if not present_bit:
                            self.index_180[tuple_117_121[0]].append(tuple_117_121[1])
        # Program VectorClear Region
        del vec_115[:]
        vec_index115 = 0
        # Program VectorUnique Region
        vec_124 = list(set(vec_124))
        vec_index124 = 0
        # Program TableJoin Region
        while vec_index124 < len(vec_124):
            var_126 = vec_124[vec_index124]
            vec_index124 += 1
            tuple_125_0_index: int = 0
            tuple_125_0_vec: List[Tuple[int, bytes, bytes]] = self.index_79[var_126]
            while tuple_125_0_index < len(tuple_125_0_vec):
                tuple_125_0 = tuple_125_0_vec[tuple_125_0_index]
                tuple_125_0_index += 1
                var_127 = tuple_125_0[0]
                var_128 = tuple_125_0[1]
                var_129 = tuple_125_0[2]
                tuple_125_1_index: int = 0
                tuple_125_1_vec: List[Tuple[int, bytes, int]] = self.index_80[var_126]
                while tuple_125_1_index < len(tuple_125_1_vec):
                    tuple_125_1 = tuple_125_1_vec[tuple_125_1_index]
                    tuple_125_1_index += 1
                    var_130 = tuple_125_1[0]
                    var_131 = tuple_125_1[1]
                    var_132 = tuple_125_1[2]
                    # Program TupleCompare Region
                    if self.var_6 == var_130:
                        # Program TransitionState Region
                        tuple_126 = var_126
                        prev_state = self.table_10[tuple_126]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_10[tuple_126] = 1 | 4
                            if not present_bit:
                                pass
                            # Program TransitionState Region
                            tuple_126_126 = (var_126, var_126)
                            prev_state = self.table_7[tuple_126_126]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_7[tuple_126_126] = 1 | 4
                                if not present_bit:
                                    self.index_100[tuple_126_126[1]].append(tuple_126_126[0])
                                    self.index_176[tuple_126_126[0]].append(tuple_126_126[1])
                                # Program VectorAppend Region
                                vec_133.append((var_126, var_126))
        # Program VectorClear Region
        del vec_124[:]
        vec_index124 = 0
        # Induction Fixpoint Loop Region
        while len(vec_133):
            # Program Call Region
            param_135_0 = [vec_133]
            ret = self.proc_87_(param_135_0)
            vec_133 = param_135_0[0]

        vec_index133 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_133[:]
        vec_index133 = 0
        # Program Return Region
        return False

    def transfer_3(self, vec_137: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index137: int = 0
        vec_141: List[int] = list()
        vec_index141: int = 0
        vec_149: List[int] = list()
        vec_index149: int = 0
        vec_158: List[Tuple[int, int]] = list()
        vec_index158: int = 0
        vec_161: List[int] = list()
        vec_index161: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index137 = 0
        while vec_index137 < len(vec_137):
            var_138, var_139, var_140 = vec_137[vec_index137]
            vec_index137 += 1
            # Program Parallel Region
            # Program TransitionState Region
            var_140 = self._resolve_edgetype(var_140)
            tuple_138_139_140 = (var_138, var_139, var_140)
            prev_state = self.table_38[tuple_138_139_140]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_138_139_140] = 1 | 4
                if not present_bit:
                    self.index_144[tuple_138_139_140[1]].append((tuple_138_139_140[0], tuple_138_139_140[2]))
                # Program Parallel Region
                # Program VectorAppend Region
                vec_141.append(var_139)
                # Program TupleCompare Region
                if self.var_0 == var_140:
                    # Program TransitionState Region
                    tuple_0_138_139 = (self.var_0, var_138, var_139)
                    prev_state = self.table_45[tuple_0_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_45[tuple_0_138_139] = 1 | 4
                        if not present_bit:
                            self.index_152[tuple_0_138_139[1]].append((tuple_0_138_139[0], tuple_0_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_1_138_139 = (self.var_1, var_138, var_139)
                    prev_state = self.table_49[tuple_1_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_49[tuple_1_138_139] = 1 | 4
                        if not present_bit:
                            self.index_153[tuple_1_138_139[1]].append((tuple_1_138_139[0], tuple_1_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_2 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_3 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_4 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_5 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
            # Program TransitionState Region
            var_140 = self._resolve_edgetype(var_140)
            tuple_138_139_140 = (var_138, var_139, var_140)
            prev_state = self.table_38[tuple_138_139_140]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_138_139_140] = 1 | 4
                if not present_bit:
                    self.index_144[tuple_138_139_140[1]].append((tuple_138_139_140[0], tuple_138_139_140[2]))
                # Program Parallel Region
                # Program VectorAppend Region
                vec_141.append(var_139)
                # Program TupleCompare Region
                if self.var_0 == var_140:
                    # Program TransitionState Region
                    tuple_0_138_139 = (self.var_0, var_138, var_139)
                    prev_state = self.table_45[tuple_0_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_45[tuple_0_138_139] = 1 | 4
                        if not present_bit:
                            self.index_152[tuple_0_138_139[1]].append((tuple_0_138_139[0], tuple_0_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_1_138_139 = (self.var_1, var_138, var_139)
                    prev_state = self.table_49[tuple_1_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_49[tuple_1_138_139] = 1 | 4
                        if not present_bit:
                            self.index_153[tuple_1_138_139[1]].append((tuple_1_138_139[0], tuple_1_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_2 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_3 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_4 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_5 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
            # Program TransitionState Region
            var_140 = self._resolve_edgetype(var_140)
            tuple_138_139_140 = (var_138, var_139, var_140)
            prev_state = self.table_38[tuple_138_139_140]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_138_139_140] = 1 | 4
                if not present_bit:
                    self.index_144[tuple_138_139_140[1]].append((tuple_138_139_140[0], tuple_138_139_140[2]))
                # Program Parallel Region
                # Program VectorAppend Region
                vec_141.append(var_139)
                # Program TupleCompare Region
                if self.var_0 == var_140:
                    # Program TransitionState Region
                    tuple_0_138_139 = (self.var_0, var_138, var_139)
                    prev_state = self.table_45[tuple_0_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_45[tuple_0_138_139] = 1 | 4
                        if not present_bit:
                            self.index_152[tuple_0_138_139[1]].append((tuple_0_138_139[0], tuple_0_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_1_138_139 = (self.var_1, var_138, var_139)
                    prev_state = self.table_49[tuple_1_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_49[tuple_1_138_139] = 1 | 4
                        if not present_bit:
                            self.index_153[tuple_1_138_139[1]].append((tuple_1_138_139[0], tuple_1_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_2 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_3 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_4 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_5 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
            # Program TransitionState Region
            var_140 = self._resolve_edgetype(var_140)
            tuple_138_139_140 = (var_138, var_139, var_140)
            prev_state = self.table_38[tuple_138_139_140]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_138_139_140] = 1 | 4
                if not present_bit:
                    self.index_144[tuple_138_139_140[1]].append((tuple_138_139_140[0], tuple_138_139_140[2]))
                # Program Parallel Region
                # Program VectorAppend Region
                vec_141.append(var_139)
                # Program TupleCompare Region
                if self.var_0 == var_140:
                    # Program TransitionState Region
                    tuple_0_138_139 = (self.var_0, var_138, var_139)
                    prev_state = self.table_45[tuple_0_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_45[tuple_0_138_139] = 1 | 4
                        if not present_bit:
                            self.index_152[tuple_0_138_139[1]].append((tuple_0_138_139[0], tuple_0_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_1_138_139 = (self.var_1, var_138, var_139)
                    prev_state = self.table_49[tuple_1_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_49[tuple_1_138_139] = 1 | 4
                        if not present_bit:
                            self.index_153[tuple_1_138_139[1]].append((tuple_1_138_139[0], tuple_1_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_2 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_3 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_4 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_5 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
            # Program TransitionState Region
            var_140 = self._resolve_edgetype(var_140)
            tuple_138_139_140 = (var_138, var_139, var_140)
            prev_state = self.table_38[tuple_138_139_140]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_138_139_140] = 1 | 4
                if not present_bit:
                    self.index_144[tuple_138_139_140[1]].append((tuple_138_139_140[0], tuple_138_139_140[2]))
                # Program Parallel Region
                # Program VectorAppend Region
                vec_141.append(var_139)
                # Program TupleCompare Region
                if self.var_0 == var_140:
                    # Program TransitionState Region
                    tuple_0_138_139 = (self.var_0, var_138, var_139)
                    prev_state = self.table_45[tuple_0_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_45[tuple_0_138_139] = 1 | 4
                        if not present_bit:
                            self.index_152[tuple_0_138_139[1]].append((tuple_0_138_139[0], tuple_0_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_1_138_139 = (self.var_1, var_138, var_139)
                    prev_state = self.table_49[tuple_1_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_49[tuple_1_138_139] = 1 | 4
                        if not present_bit:
                            self.index_153[tuple_1_138_139[1]].append((tuple_1_138_139[0], tuple_1_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_2 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_3 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_4 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_5 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
            # Program TransitionState Region
            var_140 = self._resolve_edgetype(var_140)
            tuple_138_139_140 = (var_138, var_139, var_140)
            prev_state = self.table_38[tuple_138_139_140]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_138_139_140] = 1 | 4
                if not present_bit:
                    self.index_144[tuple_138_139_140[1]].append((tuple_138_139_140[0], tuple_138_139_140[2]))
                # Program Parallel Region
                # Program VectorAppend Region
                vec_141.append(var_139)
                # Program TupleCompare Region
                if self.var_0 == var_140:
                    # Program TransitionState Region
                    tuple_0_138_139 = (self.var_0, var_138, var_139)
                    prev_state = self.table_45[tuple_0_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_45[tuple_0_138_139] = 1 | 4
                        if not present_bit:
                            self.index_152[tuple_0_138_139[1]].append((tuple_0_138_139[0], tuple_0_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_1_138_139 = (self.var_1, var_138, var_139)
                    prev_state = self.table_49[tuple_1_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_49[tuple_1_138_139] = 1 | 4
                        if not present_bit:
                            self.index_153[tuple_1_138_139[1]].append((tuple_1_138_139[0], tuple_1_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_2 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_3 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_4 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_5 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
            # Program TransitionState Region
            var_140 = self._resolve_edgetype(var_140)
            tuple_138_139_140 = (var_138, var_139, var_140)
            prev_state = self.table_38[tuple_138_139_140]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_138_139_140] = 1 | 4
                if not present_bit:
                    self.index_144[tuple_138_139_140[1]].append((tuple_138_139_140[0], tuple_138_139_140[2]))
                # Program Parallel Region
                # Program VectorAppend Region
                vec_141.append(var_139)
                # Program TupleCompare Region
                if self.var_0 == var_140:
                    # Program TransitionState Region
                    tuple_0_138_139 = (self.var_0, var_138, var_139)
                    prev_state = self.table_45[tuple_0_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_45[tuple_0_138_139] = 1 | 4
                        if not present_bit:
                            self.index_152[tuple_0_138_139[1]].append((tuple_0_138_139[0], tuple_0_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_1_138_139 = (self.var_1, var_138, var_139)
                    prev_state = self.table_49[tuple_1_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_49[tuple_1_138_139] = 1 | 4
                        if not present_bit:
                            self.index_153[tuple_1_138_139[1]].append((tuple_1_138_139[0], tuple_1_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_2 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_3 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_4 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_5 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
            # Program TransitionState Region
            var_140 = self._resolve_edgetype(var_140)
            tuple_138_139_140 = (var_138, var_139, var_140)
            prev_state = self.table_38[tuple_138_139_140]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_138_139_140] = 1 | 4
                if not present_bit:
                    self.index_144[tuple_138_139_140[1]].append((tuple_138_139_140[0], tuple_138_139_140[2]))
                # Program Parallel Region
                # Program VectorAppend Region
                vec_141.append(var_139)
                # Program TupleCompare Region
                if self.var_0 == var_140:
                    # Program TransitionState Region
                    tuple_0_138_139 = (self.var_0, var_138, var_139)
                    prev_state = self.table_45[tuple_0_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_45[tuple_0_138_139] = 1 | 4
                        if not present_bit:
                            self.index_152[tuple_0_138_139[1]].append((tuple_0_138_139[0], tuple_0_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_1_138_139 = (self.var_1, var_138, var_139)
                    prev_state = self.table_49[tuple_1_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_49[tuple_1_138_139] = 1 | 4
                        if not present_bit:
                            self.index_153[tuple_1_138_139[1]].append((tuple_1_138_139[0], tuple_1_138_139[2]))
                        # Program VectorAppend Region
                        vec_149.append(var_138)
                # Program TupleCompare Region
                if self.var_2 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_3 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_4 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_5 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
                # Program TupleCompare Region
                if self.var_1 == var_140:
                    # Program TransitionState Region
                    tuple_138_139 = (var_138, var_139)
                    prev_state = self.table_12[tuple_138_139]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_138_139] = 1 | 4
                        if not present_bit:
                            self.index_101[tuple_138_139[0]].append(tuple_138_139[1])
                        # Program VectorAppend Region
                        vec_161.append(var_138)
        # Program VectorUnique Region
        vec_141 = list(set(vec_141))
        vec_index141 = 0
        # Program TableJoin Region
        while vec_index141 < len(vec_141):
            var_143 = vec_141[vec_index141]
            vec_index141 += 1
            tuple_142_0_index: int = 0
            tuple_142_0_vec: List[Tuple[int, int]] = self.index_144[var_143]
            while tuple_142_0_index < len(tuple_142_0_vec):
                tuple_142_0 = tuple_142_0_vec[tuple_142_0_index]
                tuple_142_0_index += 1
                var_146 = tuple_142_0[0]
                var_147 = tuple_142_0[1]
                tuple_142_1_index: int = 0
                tuple_142_1_vec: List[int] = self.index_145[var_143]
                while tuple_142_1_index < len(tuple_142_1_vec):
                    tuple_142_1 = tuple_142_1_vec[tuple_142_1_index]
                    tuple_142_1_index += 1
                    var_148 = tuple_142_1
                    # Program TransitionState Region
                    tuple_146_148 = (var_146, var_148)
                    prev_state = self.table_15[tuple_146_148]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_146_148] = 1 | 4
                        if not present_bit:
                            self.index_178[tuple_146_148[0]].append(tuple_146_148[1])
        # Program VectorClear Region
        del vec_141[:]
        vec_index141 = 0
        # Program VectorUnique Region
        vec_149 = list(set(vec_149))
        vec_index149 = 0
        # Program TableJoin Region
        while vec_index149 < len(vec_149):
            var_151 = vec_149[vec_index149]
            vec_index149 += 1
            tuple_150_0_index: int = 0
            tuple_150_0_vec: List[Tuple[int, int]] = self.index_152[var_151]
            while tuple_150_0_index < len(tuple_150_0_vec):
                tuple_150_0 = tuple_150_0_vec[tuple_150_0_index]
                tuple_150_0_index += 1
                var_154 = tuple_150_0[0]
                var_155 = tuple_150_0[1]
                tuple_150_1_index: int = 0
                tuple_150_1_vec: List[Tuple[int, int]] = self.index_153[var_151]
                while tuple_150_1_index < len(tuple_150_1_vec):
                    tuple_150_1 = tuple_150_1_vec[tuple_150_1_index]
                    tuple_150_1_index += 1
                    var_156 = tuple_150_1[0]
                    var_157 = tuple_150_1[1]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_1, ) == (var_154, var_156, ):
                        # Program TupleCompare Region
                        if var_155 != var_157:
                            # Program TransitionState Region
                            tuple_151_155 = (var_151, var_155)
                            prev_state = self.table_18[tuple_151_155]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_151_155] = 1 | 4
                                if not present_bit:
                                    self.index_179[tuple_151_155[0]].append(tuple_151_155[1])
                                # Program TransitionState Region
                                tuple_155 = var_155
                                prev_state = self.table_10[tuple_155]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_10[tuple_155] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program TransitionState Region
                                    tuple_155_155 = (var_155, var_155)
                                    prev_state = self.table_7[tuple_155_155]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_7[tuple_155_155] = 1 | 4
                                        if not present_bit:
                                            self.index_100[tuple_155_155[1]].append(tuple_155_155[0])
                                            self.index_176[tuple_155_155[0]].append(tuple_155_155[1])
                                        # Program VectorAppend Region
                                        vec_158.append((var_155, var_155))
        # Program VectorClear Region
        del vec_149[:]
        vec_index149 = 0
        # Program VectorUnique Region
        vec_161 = list(set(vec_161))
        vec_index161 = 0
        # Program TableJoin Region
        while vec_index161 < len(vec_161):
            var_163 = vec_161[vec_index161]
            vec_index161 += 1
            tuple_162_0_index: int = 0
            tuple_162_0_vec: List[int] = self.index_100[var_163]
            while tuple_162_0_index < len(tuple_162_0_vec):
                tuple_162_0 = tuple_162_0_vec[tuple_162_0_index]
                tuple_162_0_index += 1
                var_164 = tuple_162_0
                tuple_162_1_index: int = 0
                tuple_162_1_vec: List[int] = self.index_101[var_163]
                while tuple_162_1_index < len(tuple_162_1_vec):
                    tuple_162_1 = tuple_162_1_vec[tuple_162_1_index]
                    tuple_162_1_index += 1
                    var_165 = tuple_162_1
                    # Program TransitionState Region
                    tuple_164_165 = (var_164, var_165)
                    prev_state = self.table_7[tuple_164_165]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_7[tuple_164_165] = 1 | 4
                        if not present_bit:
                            self.index_100[tuple_164_165[1]].append(tuple_164_165[0])
                            self.index_176[tuple_164_165[0]].append(tuple_164_165[1])
                        # Program VectorAppend Region
                        vec_158.append((var_164, var_165))
        # Program VectorClear Region
        del vec_161[:]
        vec_index161 = 0
        # Induction Fixpoint Loop Region
        while len(vec_158):
            # Program Call Region
            param_160_0 = [vec_158]
            ret = self.proc_87_(param_160_0)
            vec_158 = param_160_0[0]

        vec_index158 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_158[:]
        vec_index158 = 0
        # Program Return Region
        return False

    def relocation_2(self, vec_167: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index167: int = 0
        vec_170: List[int] = list()
        vec_index170: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index167 = 0
        while vec_index167 < len(vec_167):
            var_168, var_169 = vec_167[vec_index167]
            vec_index167 += 1
            # Program TransitionState Region
            tuple_168_169 = (var_168, var_169)
            prev_state = self.table_42[tuple_168_169]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_42[tuple_168_169] = 1 | 4
                if not present_bit:
                    self.index_145[tuple_168_169[0]].append(tuple_168_169[1])
                # Program VectorAppend Region
                vec_170.append(var_168)
        # Program VectorUnique Region
        vec_170 = list(set(vec_170))
        vec_index170 = 0
        # Program TableJoin Region
        while vec_index170 < len(vec_170):
            var_172 = vec_170[vec_index170]
            vec_index170 += 1
            tuple_171_0_index: int = 0
            tuple_171_0_vec: List[Tuple[int, int]] = self.index_144[var_172]
            while tuple_171_0_index < len(tuple_171_0_vec):
                tuple_171_0 = tuple_171_0_vec[tuple_171_0_index]
                tuple_171_0_index += 1
                var_173 = tuple_171_0[0]
                var_174 = tuple_171_0[1]
                tuple_171_1_index: int = 0
                tuple_171_1_vec: List[int] = self.index_145[var_172]
                while tuple_171_1_index < len(tuple_171_1_vec):
                    tuple_171_1 = tuple_171_1_vec[tuple_171_1_index]
                    tuple_171_1_index += 1
                    var_175 = tuple_171_1
                    # Program TransitionState Region
                    tuple_173_175 = (var_173, var_175)
                    prev_state = self.table_15[tuple_173_175]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_173_175] = 1 | 4
                        if not present_bit:
                            self.index_178[tuple_173_175[0]].append(tuple_173_175[1])
        # Program VectorClear Region
        del vec_170[:]
        vec_index170 = 0
        # Program Return Region
        return False

    def get_function_instructions_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_176[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_7[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

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

    def function_b(self, param_0: int) -> bool:
        state: int = 0
        tuple_index: int = 0
        if True:
            full_tuple = param_0
            state = self.table_10[full_tuple] & 3
            if state != 1:
                return False
            return True

    def intraproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_101[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_12[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_relocated_target_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_178[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_15[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def interproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_179[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_18[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_instructions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_21:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_21[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_section_instructions_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_180[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_23[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_sections_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_26:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_26[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

