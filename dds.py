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

        self.table_7: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_114: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_254: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_10: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_255: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_13: DefaultDict[int, int] = defaultdict(int)

        self.table_15: DefaultDict[int, int] = defaultdict(int)

        self.table_17: DefaultDict[bytes, int] = defaultdict(int)

        self.table_19: DefaultDict[Tuple[bytes, int, int, int], int] = defaultdict(int)
        self.index_82: DefaultDict[bytes, List[Tuple[int, int, int]]] = defaultdict(list)

        self.table_24: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_83: DefaultDict[bytes, List[Tuple[int, int, bytes]]] = defaultdict(list)
        self.index_93: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_29: DefaultDict[Tuple[int, bytes, int, int], int] = defaultdict(int)
        self.index_94: DefaultDict[int, List[Tuple[int, bytes, int]]] = defaultdict(list)

        self.table_34: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_163: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_39: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_164: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_43: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_165: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_47: DefaultDict[Tuple[int, int, int, int, int, int, bytes, bytes], int] = defaultdict(int)
        self.index_188: DefaultDict[int, List[Tuple[int, int, int, int, int, bytes, bytes]]] = defaultdict(list)

        self.table_56: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_139: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_60: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_132: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_64: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_125: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_68: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_115: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.var_0: int = 1
        self.var_1: int = 5
        self.var_2: int = 4
        self.var_3: int = 5
        self.var_4: int = 0
        self.var_5: int = 2
        self.var_6: int = 3
        self.init_72_()

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

    def init_72_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False

    def section_4(self, vec_74: List[Tuple[bytes, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index74: int = 0
        vec_79: List[bytes] = list()
        vec_index79: int = 0
        vec_90: List[int] = list()
        vec_index90: int = 0
        vec_105: List[Tuple[int, int]] = list()
        vec_index105: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index74 = 0
        while vec_index74 < len(vec_74):
            var_75, var_76, var_77, var_78 = vec_74[vec_index74]
            vec_index74 += 1
            # Program Parallel Region
            # Program TransitionState Region
            var_78 = self._resolve_sectype(var_78)
            tuple_75_76_77_78 = (var_75, var_76, var_77, var_78)
            prev_state = self.table_19[tuple_75_76_77_78]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_19[tuple_75_76_77_78] = 1 | 4
                if not present_bit:
                    self.index_82[tuple_75_76_77_78[0]].append((tuple_75_76_77_78[1], tuple_75_76_77_78[2], tuple_75_76_77_78[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_75 = var_75
                prev_state = self.table_17[tuple_75]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_17[tuple_75] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_79.append(var_75)
                # Program TupleCompare Region
                if self.var_0 == var_78:
                    # Program TransitionState Region
                    tuple_0_75_76_77 = (self.var_0, var_75, var_76, var_77)
                    prev_state = self.table_29[tuple_0_75_76_77]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_29[tuple_0_75_76_77] = 1 | 4
                        if not present_bit:
                            self.index_94[tuple_0_75_76_77[2]].append((tuple_0_75_76_77[0], tuple_0_75_76_77[1], tuple_0_75_76_77[3]))
                        # Program VectorAppend Region
                        vec_90.append(var_76)
            # Program TransitionState Region
            var_78 = self._resolve_sectype(var_78)
            tuple_75_76_77_78 = (var_75, var_76, var_77, var_78)
            prev_state = self.table_19[tuple_75_76_77_78]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_19[tuple_75_76_77_78] = 1 | 4
                if not present_bit:
                    self.index_82[tuple_75_76_77_78[0]].append((tuple_75_76_77_78[1], tuple_75_76_77_78[2], tuple_75_76_77_78[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_75 = var_75
                prev_state = self.table_17[tuple_75]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_17[tuple_75] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_79.append(var_75)
                # Program TupleCompare Region
                if self.var_0 == var_78:
                    # Program TransitionState Region
                    tuple_0_75_76_77 = (self.var_0, var_75, var_76, var_77)
                    prev_state = self.table_29[tuple_0_75_76_77]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_29[tuple_0_75_76_77] = 1 | 4
                        if not present_bit:
                            self.index_94[tuple_0_75_76_77[2]].append((tuple_0_75_76_77[0], tuple_0_75_76_77[1], tuple_0_75_76_77[3]))
                        # Program VectorAppend Region
                        vec_90.append(var_76)
            # Program TransitionState Region
            var_78 = self._resolve_sectype(var_78)
            tuple_75_76_77_78 = (var_75, var_76, var_77, var_78)
            prev_state = self.table_19[tuple_75_76_77_78]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_19[tuple_75_76_77_78] = 1 | 4
                if not present_bit:
                    self.index_82[tuple_75_76_77_78[0]].append((tuple_75_76_77_78[1], tuple_75_76_77_78[2], tuple_75_76_77_78[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_75 = var_75
                prev_state = self.table_17[tuple_75]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_17[tuple_75] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_79.append(var_75)
                # Program TupleCompare Region
                if self.var_0 == var_78:
                    # Program TransitionState Region
                    tuple_0_75_76_77 = (self.var_0, var_75, var_76, var_77)
                    prev_state = self.table_29[tuple_0_75_76_77]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_29[tuple_0_75_76_77] = 1 | 4
                        if not present_bit:
                            self.index_94[tuple_0_75_76_77[2]].append((tuple_0_75_76_77[0], tuple_0_75_76_77[1], tuple_0_75_76_77[3]))
                        # Program VectorAppend Region
                        vec_90.append(var_76)
        # Program VectorUnique Region
        vec_79 = list(set(vec_79))
        vec_index79 = 0
        # Program TableJoin Region
        while vec_index79 < len(vec_79):
            var_81 = vec_79[vec_index79]
            vec_index79 += 1
            tuple_80_0_index: int = 0
            tuple_80_0_vec: List[Tuple[int, int, int]] = self.index_82[var_81]
            while tuple_80_0_index < len(tuple_80_0_vec):
                tuple_80_0 = tuple_80_0_vec[tuple_80_0_index]
                tuple_80_0_index += 1
                var_84 = tuple_80_0[0]
                var_85 = tuple_80_0[1]
                var_86 = tuple_80_0[2]
                tuple_80_1_index: int = 0
                tuple_80_1_vec: List[Tuple[int, int, bytes]] = self.index_83[var_81]
                while tuple_80_1_index < len(tuple_80_1_vec):
                    tuple_80_1 = tuple_80_1_vec[tuple_80_1_index]
                    tuple_80_1_index += 1
                    var_87 = tuple_80_1[0]
                    var_88 = tuple_80_1[1]
                    var_89 = tuple_80_1[2]
                    # Program TransitionState Region
                    tuple_81_87 = (var_81, var_87)
                    prev_state = self.table_10[tuple_81_87]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_10[tuple_81_87] = 1 | 4
                        if not present_bit:
                            self.index_255[tuple_81_87[0]].append(tuple_81_87[1])
        # Program VectorClear Region
        del vec_79[:]
        vec_index79 = 0
        # Program VectorUnique Region
        vec_90 = list(set(vec_90))
        vec_index90 = 0
        # Program TableJoin Region
        while vec_index90 < len(vec_90):
            var_92 = vec_90[vec_index90]
            vec_index90 += 1
            tuple_91_0_index: int = 0
            tuple_91_0_vec: List[Tuple[int, bytes, bytes]] = self.index_93[var_92]
            while tuple_91_0_index < len(tuple_91_0_vec):
                tuple_91_0 = tuple_91_0_vec[tuple_91_0_index]
                tuple_91_0_index += 1
                var_95 = tuple_91_0[0]
                var_96 = tuple_91_0[1]
                var_97 = tuple_91_0[2]
                tuple_91_1_index: int = 0
                tuple_91_1_vec: List[Tuple[int, bytes, int]] = self.index_94[var_92]
                while tuple_91_1_index < len(tuple_91_1_vec):
                    tuple_91_1 = tuple_91_1_vec[tuple_91_1_index]
                    tuple_91_1_index += 1
                    var_98 = tuple_91_1[0]
                    var_99 = tuple_91_1[1]
                    var_100 = tuple_91_1[2]
                    # Program TupleCompare Region
                    if self.var_0 == var_98:
                        # Program TransitionState Region
                        tuple_92_92 = (var_92, var_92)
                        prev_state = self.table_7[tuple_92_92]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_92_92] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_92_92[1]].append(tuple_92_92[0])
                                self.index_254[tuple_92_92[0]].append(tuple_92_92[1])
                            # Program VectorAppend Region
                            vec_105.append((var_92, var_92))
        # Program VectorClear Region
        del vec_90[:]
        vec_index90 = 0
        # Induction Fixpoint Loop Region
        while len(vec_105):
            # Program Call Region
            param_107_0 = [vec_105]
            ret = self.proc_101_(param_107_0)
            vec_105 = param_107_0[0]

        vec_index105 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_105[:]
        vec_index105 = 0
        # Program Return Region
        return False

    def proc_101_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_102 = param_0[0]
        vec_index102: int = 0
        vec_108: List[Tuple[int, int]] = list()
        vec_index108: int = 0
        vec_111: List[int] = list()
        vec_index111: int = 0
        vec_119: List[Tuple[int, int]] = list()
        vec_index119: int = 0
        vec_122: List[int] = list()
        vec_index122: int = 0
        vec_129: List[int] = list()
        vec_index129: int = 0
        vec_136: List[int] = list()
        vec_index136: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorSwap Region
        vec_102, vec_108 = vec_108, vec_102
        # Program VectorLoop Region
        while vec_index108 < len(vec_108):
            var_109, var_110 = vec_108[vec_index108]
            vec_index108 += 1
            # Program Parallel Region
            # Program VectorAppend Region
            vec_136.append(var_110)
            # Program VectorAppend Region
            vec_129.append(var_110)
            # Program VectorAppend Region
            vec_122.append(var_110)
            # Program VectorAppend Region
            vec_111.append(var_110)
            # Program TupleCompare Region
            if var_109 == var_110:
                # Program TransitionState Region
                tuple_109 = var_109
                prev_state = self.table_15[tuple_109]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_15[tuple_109] = 1 | 4
                    if not present_bit:
                        pass
        # Program VectorUnique Region
        vec_111 = list(set(vec_111))
        vec_index111 = 0
        # Program TableJoin Region
        while vec_index111 < len(vec_111):
            var_113 = vec_111[vec_index111]
            vec_index111 += 1
            tuple_112_0_index: int = 0
            tuple_112_0_vec: List[int] = self.index_114[var_113]
            while tuple_112_0_index < len(tuple_112_0_vec):
                tuple_112_0 = tuple_112_0_vec[tuple_112_0_index]
                tuple_112_0_index += 1
                var_116 = tuple_112_0
                tuple_112_1_index: int = 0
                tuple_112_1_vec: List[Tuple[int, int]] = self.index_115[var_113]
                while tuple_112_1_index < len(tuple_112_1_vec):
                    tuple_112_1 = tuple_112_1_vec[tuple_112_1_index]
                    tuple_112_1_index += 1
                    var_117 = tuple_112_1[0]
                    var_118 = tuple_112_1[1]
                    # Program TupleCompare Region
                    if self.var_3 == var_117:
                        # Program TransitionState Region
                        tuple_116_118 = (var_116, var_118)
                        prev_state = self.table_7[tuple_116_118]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_116_118] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_116_118[1]].append(tuple_116_118[0])
                                self.index_254[tuple_116_118[0]].append(tuple_116_118[1])
                            # Program VectorAppend Region
                            vec_119.append((var_116, var_118))
        # Program VectorClear Region
        del vec_111[:]
        vec_index111 = 0
        # Program VectorUnique Region
        vec_122 = list(set(vec_122))
        vec_index122 = 0
        # Program TableJoin Region
        while vec_index122 < len(vec_122):
            var_124 = vec_122[vec_index122]
            vec_index122 += 1
            tuple_123_0_index: int = 0
            tuple_123_0_vec: List[int] = self.index_114[var_124]
            while tuple_123_0_index < len(tuple_123_0_vec):
                tuple_123_0 = tuple_123_0_vec[tuple_123_0_index]
                tuple_123_0_index += 1
                var_126 = tuple_123_0
                tuple_123_1_index: int = 0
                tuple_123_1_vec: List[Tuple[int, int]] = self.index_125[var_124]
                while tuple_123_1_index < len(tuple_123_1_vec):
                    tuple_123_1 = tuple_123_1_vec[tuple_123_1_index]
                    tuple_123_1_index += 1
                    var_127 = tuple_123_1[0]
                    var_128 = tuple_123_1[1]
                    # Program TupleCompare Region
                    if self.var_6 == var_127:
                        # Program TransitionState Region
                        tuple_126_128 = (var_126, var_128)
                        prev_state = self.table_7[tuple_126_128]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_126_128] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_126_128[1]].append(tuple_126_128[0])
                                self.index_254[tuple_126_128[0]].append(tuple_126_128[1])
                            # Program VectorAppend Region
                            vec_119.append((var_126, var_128))
        # Program VectorClear Region
        del vec_122[:]
        vec_index122 = 0
        # Program VectorUnique Region
        vec_129 = list(set(vec_129))
        vec_index129 = 0
        # Program TableJoin Region
        while vec_index129 < len(vec_129):
            var_131 = vec_129[vec_index129]
            vec_index129 += 1
            tuple_130_0_index: int = 0
            tuple_130_0_vec: List[int] = self.index_114[var_131]
            while tuple_130_0_index < len(tuple_130_0_vec):
                tuple_130_0 = tuple_130_0_vec[tuple_130_0_index]
                tuple_130_0_index += 1
                var_133 = tuple_130_0
                tuple_130_1_index: int = 0
                tuple_130_1_vec: List[Tuple[int, int]] = self.index_132[var_131]
                while tuple_130_1_index < len(tuple_130_1_vec):
                    tuple_130_1 = tuple_130_1_vec[tuple_130_1_index]
                    tuple_130_1_index += 1
                    var_134 = tuple_130_1[0]
                    var_135 = tuple_130_1[1]
                    # Program TupleCompare Region
                    if self.var_5 == var_134:
                        # Program TransitionState Region
                        tuple_133_135 = (var_133, var_135)
                        prev_state = self.table_7[tuple_133_135]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_133_135] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_133_135[1]].append(tuple_133_135[0])
                                self.index_254[tuple_133_135[0]].append(tuple_133_135[1])
                            # Program VectorAppend Region
                            vec_119.append((var_133, var_135))
        # Program VectorClear Region
        del vec_129[:]
        vec_index129 = 0
        # Program VectorUnique Region
        vec_136 = list(set(vec_136))
        vec_index136 = 0
        # Program TableJoin Region
        while vec_index136 < len(vec_136):
            var_138 = vec_136[vec_index136]
            vec_index136 += 1
            tuple_137_0_index: int = 0
            tuple_137_0_vec: List[int] = self.index_114[var_138]
            while tuple_137_0_index < len(tuple_137_0_vec):
                tuple_137_0 = tuple_137_0_vec[tuple_137_0_index]
                tuple_137_0_index += 1
                var_140 = tuple_137_0
                tuple_137_1_index: int = 0
                tuple_137_1_vec: List[Tuple[int, int]] = self.index_139[var_138]
                while tuple_137_1_index < len(tuple_137_1_vec):
                    tuple_137_1 = tuple_137_1_vec[tuple_137_1_index]
                    tuple_137_1_index += 1
                    var_141 = tuple_137_1[0]
                    var_142 = tuple_137_1[1]
                    # Program TupleCompare Region
                    if self.var_4 == var_141:
                        # Program TransitionState Region
                        tuple_140_142 = (var_140, var_142)
                        prev_state = self.table_7[tuple_140_142]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_140_142] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_140_142[1]].append(tuple_140_142[0])
                                self.index_254[tuple_140_142[0]].append(tuple_140_142[1])
                            # Program VectorAppend Region
                            vec_119.append((var_140, var_142))
        # Program VectorClear Region
        del vec_136[:]
        vec_index136 = 0
        # Induction Fixpoint Loop Region
        while len(vec_119):
            # Program Call Region
            param_121_0 = [vec_119]
            ret = self.proc_101_(param_121_0)
            vec_119 = param_121_0[0]

        vec_index119 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_119[:]
        vec_index119 = 0
        # Program Return Region
        param_0[0] = vec_102
        return False

    def instruction_4(self, vec_146: List[Tuple[int, int, bytes, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index146: int = 0
        vec_151: List[bytes] = list()
        vec_index151: int = 0
        vec_160: List[int] = list()
        vec_index160: int = 0
        vec_173: List[int] = list()
        vec_index173: int = 0
        vec_182: List[Tuple[int, int]] = list()
        vec_index182: int = 0
        vec_185: List[int] = list()
        vec_index185: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index146 = 0
        while vec_index146 < len(vec_146):
            var_147, var_148, var_149, var_150 = vec_146[vec_index146]
            vec_index146 += 1
            # Program Parallel Region
            # Program TransitionState Region
            var_148 = self._resolve_insntype(var_148)
            tuple_147_148_149_150 = (var_147, var_148, var_149, var_150)
            prev_state = self.table_24[tuple_147_148_149_150]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_24[tuple_147_148_149_150] = 1 | 4
                if not present_bit:
                    self.index_83[tuple_147_148_149_150[3]].append((tuple_147_148_149_150[0], tuple_147_148_149_150[1], tuple_147_148_149_150[2]))
                    self.index_93[tuple_147_148_149_150[0]].append((tuple_147_148_149_150[1], tuple_147_148_149_150[2], tuple_147_148_149_150[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_147 = var_147
                prev_state = self.table_13[tuple_147]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_13[tuple_147] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_151.append(var_150)
                # Program VectorAppend Region
                vec_173.append(var_147)
                # Program VectorAppend Region
                vec_185.append(var_147)
                # Program TupleCompare Region
                if self.var_1 == var_148:
                    # Program TransitionState Region
                    tuple_1_147_149_150 = (self.var_1, var_147, var_149, var_150)
                    prev_state = self.table_34[tuple_1_147_149_150]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_34[tuple_1_147_149_150] = 1 | 4
                        if not present_bit:
                            self.index_163[tuple_1_147_149_150[1]].append((tuple_1_147_149_150[0], tuple_1_147_149_150[2], tuple_1_147_149_150[3]))
                        # Program VectorAppend Region
                        vec_160.append(var_147)
            # Program TransitionState Region
            var_148 = self._resolve_insntype(var_148)
            tuple_147_148_149_150 = (var_147, var_148, var_149, var_150)
            prev_state = self.table_24[tuple_147_148_149_150]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_24[tuple_147_148_149_150] = 1 | 4
                if not present_bit:
                    self.index_83[tuple_147_148_149_150[3]].append((tuple_147_148_149_150[0], tuple_147_148_149_150[1], tuple_147_148_149_150[2]))
                    self.index_93[tuple_147_148_149_150[0]].append((tuple_147_148_149_150[1], tuple_147_148_149_150[2], tuple_147_148_149_150[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_147 = var_147
                prev_state = self.table_13[tuple_147]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_13[tuple_147] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_151.append(var_150)
                # Program VectorAppend Region
                vec_173.append(var_147)
                # Program VectorAppend Region
                vec_185.append(var_147)
                # Program TupleCompare Region
                if self.var_1 == var_148:
                    # Program TransitionState Region
                    tuple_1_147_149_150 = (self.var_1, var_147, var_149, var_150)
                    prev_state = self.table_34[tuple_1_147_149_150]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_34[tuple_1_147_149_150] = 1 | 4
                        if not present_bit:
                            self.index_163[tuple_1_147_149_150[1]].append((tuple_1_147_149_150[0], tuple_1_147_149_150[2], tuple_1_147_149_150[3]))
                        # Program VectorAppend Region
                        vec_160.append(var_147)
            # Program TransitionState Region
            var_148 = self._resolve_insntype(var_148)
            tuple_147_148_149_150 = (var_147, var_148, var_149, var_150)
            prev_state = self.table_24[tuple_147_148_149_150]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_24[tuple_147_148_149_150] = 1 | 4
                if not present_bit:
                    self.index_83[tuple_147_148_149_150[3]].append((tuple_147_148_149_150[0], tuple_147_148_149_150[1], tuple_147_148_149_150[2]))
                    self.index_93[tuple_147_148_149_150[0]].append((tuple_147_148_149_150[1], tuple_147_148_149_150[2], tuple_147_148_149_150[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_147 = var_147
                prev_state = self.table_13[tuple_147]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_13[tuple_147] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_151.append(var_150)
                # Program VectorAppend Region
                vec_173.append(var_147)
                # Program VectorAppend Region
                vec_185.append(var_147)
                # Program TupleCompare Region
                if self.var_1 == var_148:
                    # Program TransitionState Region
                    tuple_1_147_149_150 = (self.var_1, var_147, var_149, var_150)
                    prev_state = self.table_34[tuple_1_147_149_150]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_34[tuple_1_147_149_150] = 1 | 4
                        if not present_bit:
                            self.index_163[tuple_1_147_149_150[1]].append((tuple_1_147_149_150[0], tuple_1_147_149_150[2], tuple_1_147_149_150[3]))
                        # Program VectorAppend Region
                        vec_160.append(var_147)
            # Program TransitionState Region
            var_148 = self._resolve_insntype(var_148)
            tuple_147_148_149_150 = (var_147, var_148, var_149, var_150)
            prev_state = self.table_24[tuple_147_148_149_150]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_24[tuple_147_148_149_150] = 1 | 4
                if not present_bit:
                    self.index_83[tuple_147_148_149_150[3]].append((tuple_147_148_149_150[0], tuple_147_148_149_150[1], tuple_147_148_149_150[2]))
                    self.index_93[tuple_147_148_149_150[0]].append((tuple_147_148_149_150[1], tuple_147_148_149_150[2], tuple_147_148_149_150[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_147 = var_147
                prev_state = self.table_13[tuple_147]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_13[tuple_147] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_151.append(var_150)
                # Program VectorAppend Region
                vec_173.append(var_147)
                # Program VectorAppend Region
                vec_185.append(var_147)
                # Program TupleCompare Region
                if self.var_1 == var_148:
                    # Program TransitionState Region
                    tuple_1_147_149_150 = (self.var_1, var_147, var_149, var_150)
                    prev_state = self.table_34[tuple_1_147_149_150]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_34[tuple_1_147_149_150] = 1 | 4
                        if not present_bit:
                            self.index_163[tuple_1_147_149_150[1]].append((tuple_1_147_149_150[0], tuple_1_147_149_150[2], tuple_1_147_149_150[3]))
                        # Program VectorAppend Region
                        vec_160.append(var_147)
            # Program TransitionState Region
            var_148 = self._resolve_insntype(var_148)
            tuple_147_148_149_150 = (var_147, var_148, var_149, var_150)
            prev_state = self.table_24[tuple_147_148_149_150]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_24[tuple_147_148_149_150] = 1 | 4
                if not present_bit:
                    self.index_83[tuple_147_148_149_150[3]].append((tuple_147_148_149_150[0], tuple_147_148_149_150[1], tuple_147_148_149_150[2]))
                    self.index_93[tuple_147_148_149_150[0]].append((tuple_147_148_149_150[1], tuple_147_148_149_150[2], tuple_147_148_149_150[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_147 = var_147
                prev_state = self.table_13[tuple_147]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_13[tuple_147] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_151.append(var_150)
                # Program VectorAppend Region
                vec_173.append(var_147)
                # Program VectorAppend Region
                vec_185.append(var_147)
                # Program TupleCompare Region
                if self.var_1 == var_148:
                    # Program TransitionState Region
                    tuple_1_147_149_150 = (self.var_1, var_147, var_149, var_150)
                    prev_state = self.table_34[tuple_1_147_149_150]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_34[tuple_1_147_149_150] = 1 | 4
                        if not present_bit:
                            self.index_163[tuple_1_147_149_150[1]].append((tuple_1_147_149_150[0], tuple_1_147_149_150[2], tuple_1_147_149_150[3]))
                        # Program VectorAppend Region
                        vec_160.append(var_147)
        # Program VectorUnique Region
        vec_151 = list(set(vec_151))
        vec_index151 = 0
        # Program TableJoin Region
        while vec_index151 < len(vec_151):
            var_153 = vec_151[vec_index151]
            vec_index151 += 1
            tuple_152_0_index: int = 0
            tuple_152_0_vec: List[Tuple[int, int, int]] = self.index_82[var_153]
            while tuple_152_0_index < len(tuple_152_0_vec):
                tuple_152_0 = tuple_152_0_vec[tuple_152_0_index]
                tuple_152_0_index += 1
                var_154 = tuple_152_0[0]
                var_155 = tuple_152_0[1]
                var_156 = tuple_152_0[2]
                tuple_152_1_index: int = 0
                tuple_152_1_vec: List[Tuple[int, int, bytes]] = self.index_83[var_153]
                while tuple_152_1_index < len(tuple_152_1_vec):
                    tuple_152_1 = tuple_152_1_vec[tuple_152_1_index]
                    tuple_152_1_index += 1
                    var_157 = tuple_152_1[0]
                    var_158 = tuple_152_1[1]
                    var_159 = tuple_152_1[2]
                    # Program TransitionState Region
                    tuple_153_157 = (var_153, var_157)
                    prev_state = self.table_10[tuple_153_157]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_10[tuple_153_157] = 1 | 4
                        if not present_bit:
                            self.index_255[tuple_153_157[0]].append(tuple_153_157[1])
        # Program VectorClear Region
        del vec_151[:]
        vec_index151 = 0
        # Program VectorUnique Region
        vec_160 = list(set(vec_160))
        vec_index160 = 0
        # Program TableJoin Region
        while vec_index160 < len(vec_160):
            var_162 = vec_160[vec_index160]
            vec_index160 += 1
            tuple_161_0_index: int = 0
            tuple_161_0_vec: List[Tuple[int, bytes, bytes]] = self.index_163[var_162]
            while tuple_161_0_index < len(tuple_161_0_vec):
                tuple_161_0 = tuple_161_0_vec[tuple_161_0_index]
                tuple_161_0_index += 1
                var_166 = tuple_161_0[0]
                var_167 = tuple_161_0[1]
                var_168 = tuple_161_0[2]
                tuple_161_1_index: int = 0
                tuple_161_1_vec: List[Tuple[int, int]] = self.index_164[var_162]
                while tuple_161_1_index < len(tuple_161_1_vec):
                    tuple_161_1 = tuple_161_1_vec[tuple_161_1_index]
                    tuple_161_1_index += 1
                    var_169 = tuple_161_1[0]
                    var_170 = tuple_161_1[1]
                    tuple_161_2_index: int = 0
                    tuple_161_2_vec: List[Tuple[int, int]] = self.index_165[var_162]
                    while tuple_161_2_index < len(tuple_161_2_vec):
                        tuple_161_2 = tuple_161_2_vec[tuple_161_2_index]
                        tuple_161_2_index += 1
                        var_171 = tuple_161_2[0]
                        var_172 = tuple_161_2[1]
                        # Program TupleCompare Region
                        if (self.var_1, self.var_2, self.var_3, ) == (var_166, var_169, var_171, ):
                            # Program TupleCompare Region
                            if var_172 != var_170:
                                # Program TransitionState Region
                                tuple_172_170_3_2_1_162_167_168 = (var_172, var_170, self.var_3, self.var_2, self.var_1, var_162, var_167, var_168)
                                prev_state = self.table_47[tuple_172_170_3_2_1_162_167_168]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_47[tuple_172_170_3_2_1_162_167_168] = 1 | 4
                                    if not present_bit:
                                        self.index_188[tuple_172_170_3_2_1_162_167_168[0]].append((tuple_172_170_3_2_1_162_167_168[1], tuple_172_170_3_2_1_162_167_168[2], tuple_172_170_3_2_1_162_167_168[3], tuple_172_170_3_2_1_162_167_168[4], tuple_172_170_3_2_1_162_167_168[5], tuple_172_170_3_2_1_162_167_168[6], tuple_172_170_3_2_1_162_167_168[7]))
                                    # Program VectorAppend Region
                                    vec_185.append(var_172)
        # Program VectorClear Region
        del vec_160[:]
        vec_index160 = 0
        # Program VectorUnique Region
        vec_173 = list(set(vec_173))
        vec_index173 = 0
        # Program TableJoin Region
        while vec_index173 < len(vec_173):
            var_175 = vec_173[vec_index173]
            vec_index173 += 1
            tuple_174_0_index: int = 0
            tuple_174_0_vec: List[Tuple[int, bytes, bytes]] = self.index_93[var_175]
            while tuple_174_0_index < len(tuple_174_0_vec):
                tuple_174_0 = tuple_174_0_vec[tuple_174_0_index]
                tuple_174_0_index += 1
                var_176 = tuple_174_0[0]
                var_177 = tuple_174_0[1]
                var_178 = tuple_174_0[2]
                tuple_174_1_index: int = 0
                tuple_174_1_vec: List[Tuple[int, bytes, int]] = self.index_94[var_175]
                while tuple_174_1_index < len(tuple_174_1_vec):
                    tuple_174_1 = tuple_174_1_vec[tuple_174_1_index]
                    tuple_174_1_index += 1
                    var_179 = tuple_174_1[0]
                    var_180 = tuple_174_1[1]
                    var_181 = tuple_174_1[2]
                    # Program TupleCompare Region
                    if self.var_0 == var_179:
                        # Program TransitionState Region
                        tuple_175_175 = (var_175, var_175)
                        prev_state = self.table_7[tuple_175_175]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_175_175] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_175_175[1]].append(tuple_175_175[0])
                                self.index_254[tuple_175_175[0]].append(tuple_175_175[1])
                            # Program VectorAppend Region
                            vec_182.append((var_175, var_175))
        # Program VectorClear Region
        del vec_173[:]
        vec_index173 = 0
        # Program VectorUnique Region
        vec_185 = list(set(vec_185))
        vec_index185 = 0
        # Program TableJoin Region
        while vec_index185 < len(vec_185):
            var_187 = vec_185[vec_index185]
            vec_index185 += 1
            tuple_186_0_index: int = 0
            tuple_186_0_vec: List[Tuple[int, bytes, bytes]] = self.index_93[var_187]
            while tuple_186_0_index < len(tuple_186_0_vec):
                tuple_186_0 = tuple_186_0_vec[tuple_186_0_index]
                tuple_186_0_index += 1
                var_189 = tuple_186_0[0]
                var_190 = tuple_186_0[1]
                var_191 = tuple_186_0[2]
                tuple_186_1_index: int = 0
                tuple_186_1_vec: List[Tuple[int, int, int, int, int, bytes, bytes]] = self.index_188[var_187]
                while tuple_186_1_index < len(tuple_186_1_vec):
                    tuple_186_1 = tuple_186_1_vec[tuple_186_1_index]
                    tuple_186_1_index += 1
                    var_192 = tuple_186_1[0]
                    var_193 = tuple_186_1[1]
                    var_194 = tuple_186_1[2]
                    var_195 = tuple_186_1[3]
                    var_196 = tuple_186_1[4]
                    var_197 = tuple_186_1[5]
                    var_198 = tuple_186_1[6]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, self.var_3, ) == (var_195, var_194, var_193, ):
                        # Program TransitionState Region
                        tuple_192_192 = (var_192, var_192)
                        prev_state = self.table_7[tuple_192_192]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_192_192] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_192_192[1]].append(tuple_192_192[0])
                                self.index_254[tuple_192_192[0]].append(tuple_192_192[1])
                            # Program VectorAppend Region
                            vec_182.append((var_192, var_192))
        # Program VectorClear Region
        del vec_185[:]
        vec_index185 = 0
        # Induction Fixpoint Loop Region
        while len(vec_182):
            # Program Call Region
            param_184_0 = [vec_182]
            ret = self.proc_101_(param_184_0)
            vec_182 = param_184_0[0]

        vec_index182 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_182[:]
        vec_index182 = 0
        # Program Return Region
        return False

    def instruction_transfer_3(self, vec_200: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index200: int = 0
        vec_204: List[int] = list()
        vec_index204: int = 0
        vec_210: List[Tuple[int, int]] = list()
        vec_index210: int = 0
        vec_213: List[int] = list()
        vec_index213: int = 0
        vec_219: List[int] = list()
        vec_index219: int = 0
        vec_225: List[int] = list()
        vec_index225: int = 0
        vec_231: List[int] = list()
        vec_index231: int = 0
        vec_241: List[int] = list()
        vec_index241: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index200 = 0
        while vec_index200 < len(vec_200):
            var_201, var_202, var_203 = vec_200[vec_index200]
            vec_index200 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_2 == var_203:
                # Program TransitionState Region
                tuple_2_201_202 = (self.var_2, var_201, var_202)
                prev_state = self.table_39[tuple_2_201_202]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_39[tuple_2_201_202] = 1 | 4
                    if not present_bit:
                        self.index_164[tuple_2_201_202[1]].append((tuple_2_201_202[0], tuple_2_201_202[2]))
                    # Program VectorAppend Region
                    vec_231.append(var_201)
            # Program TupleCompare Region
            if self.var_3 == var_203:
                # Program TransitionState Region
                tuple_3_201_202 = (self.var_3, var_201, var_202)
                prev_state = self.table_43[tuple_3_201_202]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_43[tuple_3_201_202] = 1 | 4
                    if not present_bit:
                        self.index_165[tuple_3_201_202[1]].append((tuple_3_201_202[0], tuple_3_201_202[2]))
                    # Program VectorAppend Region
                    vec_231.append(var_201)
            # Program TupleCompare Region
            if self.var_4 == var_203:
                # Program TransitionState Region
                tuple_4_201_202 = (self.var_4, var_201, var_202)
                prev_state = self.table_56[tuple_4_201_202]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_4_201_202] = 1 | 4
                    if not present_bit:
                        self.index_139[tuple_4_201_202[1]].append((tuple_4_201_202[0], tuple_4_201_202[2]))
                    # Program VectorAppend Region
                    vec_225.append(var_201)
            # Program TupleCompare Region
            if self.var_5 == var_203:
                # Program TransitionState Region
                tuple_5_201_202 = (self.var_5, var_201, var_202)
                prev_state = self.table_60[tuple_5_201_202]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_60[tuple_5_201_202] = 1 | 4
                    if not present_bit:
                        self.index_132[tuple_5_201_202[1]].append((tuple_5_201_202[0], tuple_5_201_202[2]))
                    # Program VectorAppend Region
                    vec_219.append(var_201)
            # Program TupleCompare Region
            if self.var_6 == var_203:
                # Program TransitionState Region
                tuple_6_201_202 = (self.var_6, var_201, var_202)
                prev_state = self.table_64[tuple_6_201_202]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_64[tuple_6_201_202] = 1 | 4
                    if not present_bit:
                        self.index_125[tuple_6_201_202[1]].append((tuple_6_201_202[0], tuple_6_201_202[2]))
                    # Program VectorAppend Region
                    vec_213.append(var_201)
            # Program TupleCompare Region
            if self.var_3 == var_203:
                # Program TransitionState Region
                tuple_3_201_202 = (self.var_3, var_201, var_202)
                prev_state = self.table_68[tuple_3_201_202]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_68[tuple_3_201_202] = 1 | 4
                    if not present_bit:
                        self.index_115[tuple_3_201_202[1]].append((tuple_3_201_202[0], tuple_3_201_202[2]))
                    # Program VectorAppend Region
                    vec_204.append(var_201)
        # Program VectorUnique Region
        vec_204 = list(set(vec_204))
        vec_index204 = 0
        # Program TableJoin Region
        while vec_index204 < len(vec_204):
            var_206 = vec_204[vec_index204]
            vec_index204 += 1
            tuple_205_0_index: int = 0
            tuple_205_0_vec: List[int] = self.index_114[var_206]
            while tuple_205_0_index < len(tuple_205_0_vec):
                tuple_205_0 = tuple_205_0_vec[tuple_205_0_index]
                tuple_205_0_index += 1
                var_207 = tuple_205_0
                tuple_205_1_index: int = 0
                tuple_205_1_vec: List[Tuple[int, int]] = self.index_115[var_206]
                while tuple_205_1_index < len(tuple_205_1_vec):
                    tuple_205_1 = tuple_205_1_vec[tuple_205_1_index]
                    tuple_205_1_index += 1
                    var_208 = tuple_205_1[0]
                    var_209 = tuple_205_1[1]
                    # Program TupleCompare Region
                    if self.var_3 == var_208:
                        # Program TransitionState Region
                        tuple_207_209 = (var_207, var_209)
                        prev_state = self.table_7[tuple_207_209]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_207_209] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_207_209[1]].append(tuple_207_209[0])
                                self.index_254[tuple_207_209[0]].append(tuple_207_209[1])
                            # Program VectorAppend Region
                            vec_210.append((var_207, var_209))
        # Program VectorClear Region
        del vec_204[:]
        vec_index204 = 0
        # Program VectorUnique Region
        vec_213 = list(set(vec_213))
        vec_index213 = 0
        # Program TableJoin Region
        while vec_index213 < len(vec_213):
            var_215 = vec_213[vec_index213]
            vec_index213 += 1
            tuple_214_0_index: int = 0
            tuple_214_0_vec: List[int] = self.index_114[var_215]
            while tuple_214_0_index < len(tuple_214_0_vec):
                tuple_214_0 = tuple_214_0_vec[tuple_214_0_index]
                tuple_214_0_index += 1
                var_216 = tuple_214_0
                tuple_214_1_index: int = 0
                tuple_214_1_vec: List[Tuple[int, int]] = self.index_125[var_215]
                while tuple_214_1_index < len(tuple_214_1_vec):
                    tuple_214_1 = tuple_214_1_vec[tuple_214_1_index]
                    tuple_214_1_index += 1
                    var_217 = tuple_214_1[0]
                    var_218 = tuple_214_1[1]
                    # Program TupleCompare Region
                    if self.var_6 == var_217:
                        # Program TransitionState Region
                        tuple_216_218 = (var_216, var_218)
                        prev_state = self.table_7[tuple_216_218]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_216_218] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_216_218[1]].append(tuple_216_218[0])
                                self.index_254[tuple_216_218[0]].append(tuple_216_218[1])
                            # Program VectorAppend Region
                            vec_210.append((var_216, var_218))
        # Program VectorClear Region
        del vec_213[:]
        vec_index213 = 0
        # Program VectorUnique Region
        vec_219 = list(set(vec_219))
        vec_index219 = 0
        # Program TableJoin Region
        while vec_index219 < len(vec_219):
            var_221 = vec_219[vec_index219]
            vec_index219 += 1
            tuple_220_0_index: int = 0
            tuple_220_0_vec: List[int] = self.index_114[var_221]
            while tuple_220_0_index < len(tuple_220_0_vec):
                tuple_220_0 = tuple_220_0_vec[tuple_220_0_index]
                tuple_220_0_index += 1
                var_222 = tuple_220_0
                tuple_220_1_index: int = 0
                tuple_220_1_vec: List[Tuple[int, int]] = self.index_132[var_221]
                while tuple_220_1_index < len(tuple_220_1_vec):
                    tuple_220_1 = tuple_220_1_vec[tuple_220_1_index]
                    tuple_220_1_index += 1
                    var_223 = tuple_220_1[0]
                    var_224 = tuple_220_1[1]
                    # Program TupleCompare Region
                    if self.var_5 == var_223:
                        # Program TransitionState Region
                        tuple_222_224 = (var_222, var_224)
                        prev_state = self.table_7[tuple_222_224]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_222_224] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_222_224[1]].append(tuple_222_224[0])
                                self.index_254[tuple_222_224[0]].append(tuple_222_224[1])
                            # Program VectorAppend Region
                            vec_210.append((var_222, var_224))
        # Program VectorClear Region
        del vec_219[:]
        vec_index219 = 0
        # Program VectorUnique Region
        vec_225 = list(set(vec_225))
        vec_index225 = 0
        # Program TableJoin Region
        while vec_index225 < len(vec_225):
            var_227 = vec_225[vec_index225]
            vec_index225 += 1
            tuple_226_0_index: int = 0
            tuple_226_0_vec: List[int] = self.index_114[var_227]
            while tuple_226_0_index < len(tuple_226_0_vec):
                tuple_226_0 = tuple_226_0_vec[tuple_226_0_index]
                tuple_226_0_index += 1
                var_228 = tuple_226_0
                tuple_226_1_index: int = 0
                tuple_226_1_vec: List[Tuple[int, int]] = self.index_139[var_227]
                while tuple_226_1_index < len(tuple_226_1_vec):
                    tuple_226_1 = tuple_226_1_vec[tuple_226_1_index]
                    tuple_226_1_index += 1
                    var_229 = tuple_226_1[0]
                    var_230 = tuple_226_1[1]
                    # Program TupleCompare Region
                    if self.var_4 == var_229:
                        # Program TransitionState Region
                        tuple_228_230 = (var_228, var_230)
                        prev_state = self.table_7[tuple_228_230]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_228_230] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_228_230[1]].append(tuple_228_230[0])
                                self.index_254[tuple_228_230[0]].append(tuple_228_230[1])
                            # Program VectorAppend Region
                            vec_210.append((var_228, var_230))
        # Program VectorClear Region
        del vec_225[:]
        vec_index225 = 0
        # Program VectorUnique Region
        vec_231 = list(set(vec_231))
        vec_index231 = 0
        # Program TableJoin Region
        while vec_index231 < len(vec_231):
            var_233 = vec_231[vec_index231]
            vec_index231 += 1
            tuple_232_0_index: int = 0
            tuple_232_0_vec: List[Tuple[int, bytes, bytes]] = self.index_163[var_233]
            while tuple_232_0_index < len(tuple_232_0_vec):
                tuple_232_0 = tuple_232_0_vec[tuple_232_0_index]
                tuple_232_0_index += 1
                var_234 = tuple_232_0[0]
                var_235 = tuple_232_0[1]
                var_236 = tuple_232_0[2]
                tuple_232_1_index: int = 0
                tuple_232_1_vec: List[Tuple[int, int]] = self.index_164[var_233]
                while tuple_232_1_index < len(tuple_232_1_vec):
                    tuple_232_1 = tuple_232_1_vec[tuple_232_1_index]
                    tuple_232_1_index += 1
                    var_237 = tuple_232_1[0]
                    var_238 = tuple_232_1[1]
                    tuple_232_2_index: int = 0
                    tuple_232_2_vec: List[Tuple[int, int]] = self.index_165[var_233]
                    while tuple_232_2_index < len(tuple_232_2_vec):
                        tuple_232_2 = tuple_232_2_vec[tuple_232_2_index]
                        tuple_232_2_index += 1
                        var_239 = tuple_232_2[0]
                        var_240 = tuple_232_2[1]
                        # Program TupleCompare Region
                        if (self.var_1, self.var_2, self.var_3, ) == (var_234, var_237, var_239, ):
                            # Program TupleCompare Region
                            if var_240 != var_238:
                                # Program TransitionState Region
                                tuple_240_238_3_2_1_233_235_236 = (var_240, var_238, self.var_3, self.var_2, self.var_1, var_233, var_235, var_236)
                                prev_state = self.table_47[tuple_240_238_3_2_1_233_235_236]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_47[tuple_240_238_3_2_1_233_235_236] = 1 | 4
                                    if not present_bit:
                                        self.index_188[tuple_240_238_3_2_1_233_235_236[0]].append((tuple_240_238_3_2_1_233_235_236[1], tuple_240_238_3_2_1_233_235_236[2], tuple_240_238_3_2_1_233_235_236[3], tuple_240_238_3_2_1_233_235_236[4], tuple_240_238_3_2_1_233_235_236[5], tuple_240_238_3_2_1_233_235_236[6], tuple_240_238_3_2_1_233_235_236[7]))
                                    # Program VectorAppend Region
                                    vec_241.append(var_240)
        # Program VectorClear Region
        del vec_231[:]
        vec_index231 = 0
        # Program VectorUnique Region
        vec_241 = list(set(vec_241))
        vec_index241 = 0
        # Program TableJoin Region
        while vec_index241 < len(vec_241):
            var_243 = vec_241[vec_index241]
            vec_index241 += 1
            tuple_242_0_index: int = 0
            tuple_242_0_vec: List[Tuple[int, bytes, bytes]] = self.index_93[var_243]
            while tuple_242_0_index < len(tuple_242_0_vec):
                tuple_242_0 = tuple_242_0_vec[tuple_242_0_index]
                tuple_242_0_index += 1
                var_244 = tuple_242_0[0]
                var_245 = tuple_242_0[1]
                var_246 = tuple_242_0[2]
                tuple_242_1_index: int = 0
                tuple_242_1_vec: List[Tuple[int, int, int, int, int, bytes, bytes]] = self.index_188[var_243]
                while tuple_242_1_index < len(tuple_242_1_vec):
                    tuple_242_1 = tuple_242_1_vec[tuple_242_1_index]
                    tuple_242_1_index += 1
                    var_247 = tuple_242_1[0]
                    var_248 = tuple_242_1[1]
                    var_249 = tuple_242_1[2]
                    var_250 = tuple_242_1[3]
                    var_251 = tuple_242_1[4]
                    var_252 = tuple_242_1[5]
                    var_253 = tuple_242_1[6]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, self.var_3, ) == (var_250, var_249, var_248, ):
                        # Program TransitionState Region
                        tuple_247_247 = (var_247, var_247)
                        prev_state = self.table_7[tuple_247_247]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_7[tuple_247_247] = 1 | 4
                            if not present_bit:
                                self.index_114[tuple_247_247[1]].append(tuple_247_247[0])
                                self.index_254[tuple_247_247[0]].append(tuple_247_247[1])
                            # Program VectorAppend Region
                            vec_210.append((var_247, var_247))
        # Program VectorClear Region
        del vec_241[:]
        vec_index241 = 0
        # Induction Fixpoint Loop Region
        while len(vec_210):
            # Program Call Region
            param_212_0 = [vec_210]
            ret = self.proc_101_(param_212_0)
            vec_210 = param_212_0[0]

        vec_index210 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_210[:]
        vec_index210 = 0
        # Program Return Region
        return False

    def get_function_instructions_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_254[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_7[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_section_instructions_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_255[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_10[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_instructions_f(self) -> Iterator[int]:
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

    def get_functions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_15:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_15[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_sections_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_17:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_17[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

