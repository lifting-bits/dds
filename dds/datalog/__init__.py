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

        self.table_6: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_387: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_949: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_9: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_388: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_1000: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_12: DefaultDict[int, int] = defaultdict(int)

        self.table_14: DefaultDict[int, int] = defaultdict(int)
        self.index_381 = self.table_14

        self.table_16: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_406: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_956: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_19: DefaultDict[bytes, int] = defaultdict(int)

        self.table_21: DefaultDict[int, int] = defaultdict(int)

        self.table_23: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_957: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_26: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_248: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)
        self.index_974: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)

        self.table_30: DefaultDict[Tuple[bytes, int, int, int], int] = defaultdict(int)
        self.index_166: DefaultDict[bytes, List[Tuple[int, int, int]]] = defaultdict(list)

        self.table_35: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_167: DefaultDict[bytes, List[Tuple[int, int, bytes]]] = defaultdict(list)

        self.table_40: DefaultDict[Tuple[int, bytes], int] = defaultdict(int)
        self.index_345: DefaultDict[int, List[bytes]] = defaultdict(list)

        self.table_43: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_346: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_47: DefaultDict[int, int] = defaultdict(int)
        self.index_307 = self.table_47

        self.table_49: DefaultDict[int, int] = defaultdict(int)
        self.index_228 = self.table_49

        self.table_51: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_357: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_56: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_358: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_60: DefaultDict[Tuple[int, int, int, bytes, bytes, int], int] = defaultdict(int)
        self.index_367: DefaultDict[int, List[Tuple[int, int, int, bytes, bytes]]] = defaultdict(list)

        self.table_67: DefaultDict[Tuple[int, int, int, int, int], int] = defaultdict(int)
        self.index_292: DefaultDict[int, List[Tuple[int, int, int, int]]] = defaultdict(list)

        self.table_73: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_618: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_77: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_619: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_81: DefaultDict[Tuple[int, int, int, int, int], int] = defaultdict(int)
        self.index_330: DefaultDict[int, List[Tuple[int, int, int, int]]] = defaultdict(list)

        self.table_87: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_609: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_91: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_610: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_95: DefaultDict[Tuple[int, int, int, int, int], int] = defaultdict(int)
        self.index_315: DefaultDict[int, List[Tuple[int, int, int, int]]] = defaultdict(list)

        self.table_101: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_201: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_106: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_193: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_109: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_209: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_112: DefaultDict[Tuple[int, int, bytes, bytes, int], int] = defaultdict(int)
        self.index_210: DefaultDict[int, List[Tuple[int, int, bytes, bytes]]] = defaultdict(list)

        self.table_118: DefaultDict[Tuple[int, int, int, int, bytes, bytes], int] = defaultdict(int)
        self.index_276: DefaultDict[int, List[Tuple[int, int, int, bytes, bytes]]] = defaultdict(list)

        self.table_125: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_192: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_130: DefaultDict[Tuple[int, int, bytes, bytes, int], int] = defaultdict(int)
        self.index_219: DefaultDict[int, List[Tuple[int, int, bytes, bytes]]] = defaultdict(list)

        self.table_136: DefaultDict[Tuple[int, int, int, int, bytes, bytes], int] = defaultdict(int)
        self.index_260: DefaultDict[int, List[Tuple[int, int, int, bytes, bytes]]] = defaultdict(list)

        self.table_143: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_602: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)

        self.table_147: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_603: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)

        self.table_151: DefaultDict[Tuple[int, int, int, int], int] = defaultdict(int)
        self.index_229: DefaultDict[int, List[Tuple[int, int, int]]] = defaultdict(list)

        self.var_0: int = 5
        self.var_1: int = 2
        self.var_2: int = 1
        self.var_3: int = 6
        self.var_4: int = 6
        self.var_5: int = 0
        self.init_156_()

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

    def init_156_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False

    def section_4(self, vec_158: List[Tuple[bytes, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index158: int = 0
        vec_163: List[bytes] = list()
        vec_index163: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index158 = 0
        while vec_index158 < len(vec_158):
            var_159, var_160, var_161, var_162 = vec_158[vec_index158]
            vec_index158 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_162 = self._resolve_sectype(var_162)
            tuple_159_160_161_162 = (var_159, var_160, var_161, var_162)
            prev_state = self.table_30[tuple_159_160_161_162]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_159_160_161_162] = 1 | 4
                if not present_bit:
                    self.index_166[tuple_159_160_161_162[0]].append((tuple_159_160_161_162[1], tuple_159_160_161_162[2], tuple_159_160_161_162[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_159 = var_159
                prev_state = self.table_19[tuple_159]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_19[tuple_159] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_163.append(var_159)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_162 = self._resolve_sectype(var_162)
            tuple_159_160_161_162 = (var_159, var_160, var_161, var_162)
            prev_state = self.table_30[tuple_159_160_161_162]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_159_160_161_162] = 1 | 4
                if not present_bit:
                    self.index_166[tuple_159_160_161_162[0]].append((tuple_159_160_161_162[1], tuple_159_160_161_162[2], tuple_159_160_161_162[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_159 = var_159
                prev_state = self.table_19[tuple_159]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_19[tuple_159] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_163.append(var_159)
        # Program VectorUnique Region
        vec_163 = list(set(vec_163))
        vec_index163 = 0
        # Program TableJoin Region
        while vec_index163 < len(vec_163):
            var_165 = vec_163[vec_index163]
            vec_index163 += 1
            tuple_164_0_index: int = 0
            tuple_164_0_vec: List[Tuple[int, int, int]] = self.index_166[var_165]
            while tuple_164_0_index < len(tuple_164_0_vec):
                tuple_164_0 = tuple_164_0_vec[tuple_164_0_index]
                tuple_164_0_index += 1
                var_168 = tuple_164_0[0]
                var_169 = tuple_164_0[1]
                var_170 = tuple_164_0[2]
                tuple_164_1_index: int = 0
                tuple_164_1_vec: List[Tuple[int, int, bytes]] = self.index_167[var_165]
                while tuple_164_1_index < len(tuple_164_1_vec):
                    tuple_164_1 = tuple_164_1_vec[tuple_164_1_index]
                    tuple_164_1_index += 1
                    var_171 = tuple_164_1[0]
                    var_172 = tuple_164_1[1]
                    var_173 = tuple_164_1[2]
                    # Program TransitionState Region
                    tuple_165_171 = (var_165, var_171)
                    prev_state = self.table_23[tuple_165_171]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_23[tuple_165_171] = 1 | 4
                        if not present_bit:
                            self.index_957[tuple_165_171[0]].append(tuple_165_171[1])
        # Program VectorClear Region
        del vec_163[:]
        vec_index163 = 0
        # Program Return Region
        return False

    def instruction_4(self, vec_175: List[Tuple[int, int, bytes, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index175: int = 0
        vec_180: List[bytes] = list()
        vec_index180: int = 0
        vec_189: List[int] = list()
        vec_index189: int = 0
        vec_198: List[int] = list()
        vec_index198: int = 0
        vec_206: List[int] = list()
        vec_index206: int = 0
        vec_216: List[int] = list()
        vec_index216: int = 0
        vec_225: List[int] = list()
        vec_index225: int = 0
        vec_245: List[Tuple[int, int]] = list()
        vec_index245: int = 0
        vec_249: List[Tuple[int, int]] = list()
        vec_index249: int = 0
        vec_257: List[int] = list()
        vec_index257: int = 0
        vec_269: List[Tuple[int, int]] = list()
        vec_index269: int = 0
        vec_273: List[int] = list()
        vec_index273: int = 0
        vec_285: List[Tuple[int, int]] = list()
        vec_index285: int = 0
        vec_289: List[int] = list()
        vec_index289: int = 0
        vec_300: List[Tuple[int, int]] = list()
        vec_index300: int = 0
        vec_304: List[int] = list()
        vec_index304: int = 0
        vec_308: List[Tuple[int, int]] = list()
        vec_index308: int = 0
        vec_312: List[int] = list()
        vec_index312: int = 0
        vec_323: List[Tuple[int, int]] = list()
        vec_index323: int = 0
        vec_327: List[int] = list()
        vec_index327: int = 0
        vec_338: List[Tuple[int, int]] = list()
        vec_index338: int = 0
        vec_342: List[int] = list()
        vec_index342: int = 0
        vec_350: List[Tuple[int, int]] = list()
        vec_index350: int = 0
        vec_354: List[int] = list()
        vec_index354: int = 0
        vec_364: List[int] = list()
        vec_index364: int = 0
        vec_374: List[Tuple[int, int]] = list()
        vec_index374: int = 0
        vec_378: List[int] = list()
        vec_index378: int = 0
        vec_384: List[int] = list()
        vec_index384: int = 0
        vec_403: List[int] = list()
        vec_index403: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index175 = 0
        while vec_index175 < len(vec_175):
            var_176, var_177, var_178, var_179 = vec_175[vec_index175]
            vec_index175 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_177 = self._resolve_insntype(var_177)
            tuple_176_177_178_179 = (var_176, var_177, var_178, var_179)
            prev_state = self.table_35[tuple_176_177_178_179]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_176_177_178_179] = 1 | 4
                if not present_bit:
                    self.index_167[tuple_176_177_178_179[3]].append((tuple_176_177_178_179[0], tuple_176_177_178_179[1], tuple_176_177_178_179[2]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_21[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_49[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_304.append(var_176)
                    # Program VectorAppend Region
                    vec_289.append(var_176)
                    # Program VectorAppend Region
                    vec_327.append(var_176)
                    # Program VectorAppend Region
                    vec_312.append(var_176)
                    # Program VectorAppend Region
                    vec_273.append(var_176)
                    # Program VectorAppend Region
                    vec_257.append(var_176)
                    # Program VectorAppend Region
                    vec_225.append(var_176)
                # Program VectorAppend Region
                vec_180.append(var_179)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_51[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_357[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_354.append(var_176)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_101[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_101[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_201[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_198.append(var_176)
                # Program TupleCompare Region
                if self.var_4 == var_177:
                    # Program TransitionState Region
                    tuple_4_176_178_179 = (self.var_4, var_176, var_178, var_179)
                    prev_state = self.table_125[tuple_4_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_125[tuple_4_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_192[tuple_4_176_178_179[1]].append((tuple_4_176_178_179[0], tuple_4_176_178_179[2], tuple_4_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_189.append(var_176)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_177 = self._resolve_insntype(var_177)
            tuple_176_177_178_179 = (var_176, var_177, var_178, var_179)
            prev_state = self.table_35[tuple_176_177_178_179]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_176_177_178_179] = 1 | 4
                if not present_bit:
                    self.index_167[tuple_176_177_178_179[3]].append((tuple_176_177_178_179[0], tuple_176_177_178_179[1], tuple_176_177_178_179[2]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_21[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_49[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_304.append(var_176)
                    # Program VectorAppend Region
                    vec_289.append(var_176)
                    # Program VectorAppend Region
                    vec_327.append(var_176)
                    # Program VectorAppend Region
                    vec_312.append(var_176)
                    # Program VectorAppend Region
                    vec_273.append(var_176)
                    # Program VectorAppend Region
                    vec_257.append(var_176)
                    # Program VectorAppend Region
                    vec_225.append(var_176)
                # Program VectorAppend Region
                vec_180.append(var_179)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_51[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_357[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_354.append(var_176)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_101[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_101[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_201[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_198.append(var_176)
                # Program TupleCompare Region
                if self.var_4 == var_177:
                    # Program TransitionState Region
                    tuple_4_176_178_179 = (self.var_4, var_176, var_178, var_179)
                    prev_state = self.table_125[tuple_4_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_125[tuple_4_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_192[tuple_4_176_178_179[1]].append((tuple_4_176_178_179[0], tuple_4_176_178_179[2], tuple_4_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_189.append(var_176)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_177 = self._resolve_insntype(var_177)
            tuple_176_177_178_179 = (var_176, var_177, var_178, var_179)
            prev_state = self.table_35[tuple_176_177_178_179]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_176_177_178_179] = 1 | 4
                if not present_bit:
                    self.index_167[tuple_176_177_178_179[3]].append((tuple_176_177_178_179[0], tuple_176_177_178_179[1], tuple_176_177_178_179[2]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_21[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_49[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_304.append(var_176)
                    # Program VectorAppend Region
                    vec_289.append(var_176)
                    # Program VectorAppend Region
                    vec_327.append(var_176)
                    # Program VectorAppend Region
                    vec_312.append(var_176)
                    # Program VectorAppend Region
                    vec_273.append(var_176)
                    # Program VectorAppend Region
                    vec_257.append(var_176)
                    # Program VectorAppend Region
                    vec_225.append(var_176)
                # Program VectorAppend Region
                vec_180.append(var_179)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_51[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_357[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_354.append(var_176)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_101[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_101[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_201[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_198.append(var_176)
                # Program TupleCompare Region
                if self.var_4 == var_177:
                    # Program TransitionState Region
                    tuple_4_176_178_179 = (self.var_4, var_176, var_178, var_179)
                    prev_state = self.table_125[tuple_4_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_125[tuple_4_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_192[tuple_4_176_178_179[1]].append((tuple_4_176_178_179[0], tuple_4_176_178_179[2], tuple_4_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_189.append(var_176)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_177 = self._resolve_insntype(var_177)
            tuple_176_177_178_179 = (var_176, var_177, var_178, var_179)
            prev_state = self.table_35[tuple_176_177_178_179]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_176_177_178_179] = 1 | 4
                if not present_bit:
                    self.index_167[tuple_176_177_178_179[3]].append((tuple_176_177_178_179[0], tuple_176_177_178_179[1], tuple_176_177_178_179[2]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_21[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_49[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_304.append(var_176)
                    # Program VectorAppend Region
                    vec_289.append(var_176)
                    # Program VectorAppend Region
                    vec_327.append(var_176)
                    # Program VectorAppend Region
                    vec_312.append(var_176)
                    # Program VectorAppend Region
                    vec_273.append(var_176)
                    # Program VectorAppend Region
                    vec_257.append(var_176)
                    # Program VectorAppend Region
                    vec_225.append(var_176)
                # Program VectorAppend Region
                vec_180.append(var_179)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_51[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_357[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_354.append(var_176)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_101[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_101[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_201[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_198.append(var_176)
                # Program TupleCompare Region
                if self.var_4 == var_177:
                    # Program TransitionState Region
                    tuple_4_176_178_179 = (self.var_4, var_176, var_178, var_179)
                    prev_state = self.table_125[tuple_4_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_125[tuple_4_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_192[tuple_4_176_178_179[1]].append((tuple_4_176_178_179[0], tuple_4_176_178_179[2], tuple_4_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_189.append(var_176)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_177 = self._resolve_insntype(var_177)
            tuple_176_177_178_179 = (var_176, var_177, var_178, var_179)
            prev_state = self.table_35[tuple_176_177_178_179]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_176_177_178_179] = 1 | 4
                if not present_bit:
                    self.index_167[tuple_176_177_178_179[3]].append((tuple_176_177_178_179[0], tuple_176_177_178_179[1], tuple_176_177_178_179[2]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_21[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_49[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_304.append(var_176)
                    # Program VectorAppend Region
                    vec_289.append(var_176)
                    # Program VectorAppend Region
                    vec_327.append(var_176)
                    # Program VectorAppend Region
                    vec_312.append(var_176)
                    # Program VectorAppend Region
                    vec_273.append(var_176)
                    # Program VectorAppend Region
                    vec_257.append(var_176)
                    # Program VectorAppend Region
                    vec_225.append(var_176)
                # Program VectorAppend Region
                vec_180.append(var_179)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_51[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_357[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_354.append(var_176)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_101[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_101[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_201[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_198.append(var_176)
                # Program TupleCompare Region
                if self.var_4 == var_177:
                    # Program TransitionState Region
                    tuple_4_176_178_179 = (self.var_4, var_176, var_178, var_179)
                    prev_state = self.table_125[tuple_4_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_125[tuple_4_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_192[tuple_4_176_178_179[1]].append((tuple_4_176_178_179[0], tuple_4_176_178_179[2], tuple_4_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_189.append(var_176)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_177 = self._resolve_insntype(var_177)
            tuple_176_177_178_179 = (var_176, var_177, var_178, var_179)
            prev_state = self.table_35[tuple_176_177_178_179]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_176_177_178_179] = 1 | 4
                if not present_bit:
                    self.index_167[tuple_176_177_178_179[3]].append((tuple_176_177_178_179[0], tuple_176_177_178_179[1], tuple_176_177_178_179[2]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_21[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_176 = var_176
                prev_state = self.table_49[tuple_176]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_176] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_304.append(var_176)
                    # Program VectorAppend Region
                    vec_289.append(var_176)
                    # Program VectorAppend Region
                    vec_327.append(var_176)
                    # Program VectorAppend Region
                    vec_312.append(var_176)
                    # Program VectorAppend Region
                    vec_273.append(var_176)
                    # Program VectorAppend Region
                    vec_257.append(var_176)
                    # Program VectorAppend Region
                    vec_225.append(var_176)
                # Program VectorAppend Region
                vec_180.append(var_179)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_51[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_357[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_354.append(var_176)
                # Program TupleCompare Region
                if self.var_1 == var_177:
                    # Program TransitionState Region
                    tuple_1_176_178_179 = (self.var_1, var_176, var_178, var_179)
                    prev_state = self.table_101[tuple_1_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_101[tuple_1_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_201[tuple_1_176_178_179[1]].append((tuple_1_176_178_179[0], tuple_1_176_178_179[2], tuple_1_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_198.append(var_176)
                # Program TupleCompare Region
                if self.var_4 == var_177:
                    # Program TransitionState Region
                    tuple_4_176_178_179 = (self.var_4, var_176, var_178, var_179)
                    prev_state = self.table_125[tuple_4_176_178_179]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_125[tuple_4_176_178_179] = 1 | 4
                        if not present_bit:
                            self.index_192[tuple_4_176_178_179[1]].append((tuple_4_176_178_179[0], tuple_4_176_178_179[2], tuple_4_176_178_179[3]))
                        # Program VectorAppend Region
                        vec_189.append(var_176)
        # Program VectorUnique Region
        vec_180 = list(set(vec_180))
        vec_index180 = 0
        # Program TableJoin Region
        while vec_index180 < len(vec_180):
            var_182 = vec_180[vec_index180]
            vec_index180 += 1
            tuple_181_0_index: int = 0
            tuple_181_0_vec: List[Tuple[int, int, int]] = self.index_166[var_182]
            while tuple_181_0_index < len(tuple_181_0_vec):
                tuple_181_0 = tuple_181_0_vec[tuple_181_0_index]
                tuple_181_0_index += 1
                var_183 = tuple_181_0[0]
                var_184 = tuple_181_0[1]
                var_185 = tuple_181_0[2]
                tuple_181_1_index: int = 0
                tuple_181_1_vec: List[Tuple[int, int, bytes]] = self.index_167[var_182]
                while tuple_181_1_index < len(tuple_181_1_vec):
                    tuple_181_1 = tuple_181_1_vec[tuple_181_1_index]
                    tuple_181_1_index += 1
                    var_186 = tuple_181_1[0]
                    var_187 = tuple_181_1[1]
                    var_188 = tuple_181_1[2]
                    # Program TransitionState Region
                    tuple_182_186 = (var_182, var_186)
                    prev_state = self.table_23[tuple_182_186]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_23[tuple_182_186] = 1 | 4
                        if not present_bit:
                            self.index_957[tuple_182_186[0]].append(tuple_182_186[1])
        # Program VectorClear Region
        del vec_180[:]
        vec_index180 = 0
        # Program VectorUnique Region
        vec_189 = list(set(vec_189))
        vec_index189 = 0
        # Program TableJoin Region
        while vec_index189 < len(vec_189):
            var_191 = vec_189[vec_index189]
            vec_index189 += 1
            tuple_190_0_index: int = 0
            tuple_190_0_vec: List[Tuple[int, bytes, bytes]] = self.index_192[var_191]
            while tuple_190_0_index < len(tuple_190_0_vec):
                tuple_190_0 = tuple_190_0_vec[tuple_190_0_index]
                tuple_190_0_index += 1
                var_194 = tuple_190_0[0]
                var_195 = tuple_190_0[1]
                var_196 = tuple_190_0[2]
                tuple_190_1_index: int = 0
                tuple_190_1_vec: List[int] = self.index_193[var_191]
                while tuple_190_1_index < len(tuple_190_1_vec):
                    tuple_190_1 = tuple_190_1_vec[tuple_190_1_index]
                    tuple_190_1_index += 1
                    var_197 = tuple_190_1
                    # Program TupleCompare Region
                    if self.var_4 == var_194:
                        # Program TransitionState Region
                        tuple_4_191_195_196_197 = (self.var_4, var_191, var_195, var_196, var_197)
                        prev_state = self.table_130[tuple_4_191_195_196_197]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_130[tuple_4_191_195_196_197] = 1 | 4
                            if not present_bit:
                                self.index_219[tuple_4_191_195_196_197[4]].append((tuple_4_191_195_196_197[0], tuple_4_191_195_196_197[1], tuple_4_191_195_196_197[2], tuple_4_191_195_196_197[3]))
                            # Program VectorAppend Region
                            vec_216.append(var_197)
        # Program VectorClear Region
        del vec_189[:]
        vec_index189 = 0
        # Program VectorUnique Region
        vec_198 = list(set(vec_198))
        vec_index198 = 0
        # Program TableJoin Region
        while vec_index198 < len(vec_198):
            var_200 = vec_198[vec_index198]
            vec_index198 += 1
            tuple_199_0_index: int = 0
            tuple_199_0_vec: List[Tuple[int, bytes, bytes]] = self.index_201[var_200]
            while tuple_199_0_index < len(tuple_199_0_vec):
                tuple_199_0 = tuple_199_0_vec[tuple_199_0_index]
                tuple_199_0_index += 1
                var_202 = tuple_199_0[0]
                var_203 = tuple_199_0[1]
                var_204 = tuple_199_0[2]
                tuple_199_1_index: int = 0
                tuple_199_1_vec: List[int] = self.index_193[var_200]
                while tuple_199_1_index < len(tuple_199_1_vec):
                    tuple_199_1 = tuple_199_1_vec[tuple_199_1_index]
                    tuple_199_1_index += 1
                    var_205 = tuple_199_1
                    # Program TupleCompare Region
                    if self.var_1 == var_202:
                        # Program TransitionState Region
                        tuple_1_200_203_204_205 = (self.var_1, var_200, var_203, var_204, var_205)
                        prev_state = self.table_112[tuple_1_200_203_204_205]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_112[tuple_1_200_203_204_205] = 1 | 4
                            if not present_bit:
                                self.index_210[tuple_1_200_203_204_205[4]].append((tuple_1_200_203_204_205[0], tuple_1_200_203_204_205[1], tuple_1_200_203_204_205[2], tuple_1_200_203_204_205[3]))
                            # Program VectorAppend Region
                            vec_206.append(var_205)
        # Program VectorClear Region
        del vec_198[:]
        vec_index198 = 0
        # Program VectorUnique Region
        vec_206 = list(set(vec_206))
        vec_index206 = 0
        # Program TableJoin Region
        while vec_index206 < len(vec_206):
            var_208 = vec_206[vec_index206]
            vec_index206 += 1
            tuple_207_0_index: int = 0
            tuple_207_0_vec: List[int] = self.index_209[var_208]
            while tuple_207_0_index < len(tuple_207_0_vec):
                tuple_207_0 = tuple_207_0_vec[tuple_207_0_index]
                tuple_207_0_index += 1
                var_211 = tuple_207_0
                tuple_207_1_index: int = 0
                tuple_207_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_210[var_208]
                while tuple_207_1_index < len(tuple_207_1_vec):
                    tuple_207_1 = tuple_207_1_vec[tuple_207_1_index]
                    tuple_207_1_index += 1
                    var_212 = tuple_207_1[0]
                    var_213 = tuple_207_1[1]
                    var_214 = tuple_207_1[2]
                    var_215 = tuple_207_1[3]
                    # Program TupleCompare Region
                    if self.var_1 == var_212:
                        # Program TransitionState Region
                        tuple_1_208_211_213_214_215 = (self.var_1, var_208, var_211, var_213, var_214, var_215)
                        prev_state = self.table_118[tuple_1_208_211_213_214_215]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_118[tuple_1_208_211_213_214_215] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_1_208_211_213_214_215[2]].append((tuple_1_208_211_213_214_215[0], tuple_1_208_211_213_214_215[1], tuple_1_208_211_213_214_215[3], tuple_1_208_211_213_214_215[4], tuple_1_208_211_213_214_215[5]))
                            # Program VectorAppend Region
                            vec_273.append(var_211)
        # Program VectorClear Region
        del vec_206[:]
        vec_index206 = 0
        # Program VectorUnique Region
        vec_216 = list(set(vec_216))
        vec_index216 = 0
        # Program TableJoin Region
        while vec_index216 < len(vec_216):
            var_218 = vec_216[vec_index216]
            vec_index216 += 1
            tuple_217_0_index: int = 0
            tuple_217_0_vec: List[int] = self.index_209[var_218]
            while tuple_217_0_index < len(tuple_217_0_vec):
                tuple_217_0 = tuple_217_0_vec[tuple_217_0_index]
                tuple_217_0_index += 1
                var_220 = tuple_217_0
                tuple_217_1_index: int = 0
                tuple_217_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_219[var_218]
                while tuple_217_1_index < len(tuple_217_1_vec):
                    tuple_217_1 = tuple_217_1_vec[tuple_217_1_index]
                    tuple_217_1_index += 1
                    var_221 = tuple_217_1[0]
                    var_222 = tuple_217_1[1]
                    var_223 = tuple_217_1[2]
                    var_224 = tuple_217_1[3]
                    # Program TupleCompare Region
                    if self.var_4 == var_221:
                        # Program TransitionState Region
                        tuple_4_218_220_222_223_224 = (self.var_4, var_218, var_220, var_222, var_223, var_224)
                        prev_state = self.table_136[tuple_4_218_220_222_223_224]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_136[tuple_4_218_220_222_223_224] = 1 | 4
                            if not present_bit:
                                self.index_260[tuple_4_218_220_222_223_224[2]].append((tuple_4_218_220_222_223_224[0], tuple_4_218_220_222_223_224[1], tuple_4_218_220_222_223_224[3], tuple_4_218_220_222_223_224[4], tuple_4_218_220_222_223_224[5]))
                            # Program VectorAppend Region
                            vec_257.append(var_220)
        # Program VectorClear Region
        del vec_216[:]
        vec_index216 = 0
        # Program VectorUnique Region
        vec_225 = list(set(vec_225))
        vec_index225 = 0
        # Program TableJoin Region
        while vec_index225 < len(vec_225):
            var_227 = vec_225[vec_index225]
            vec_index225 += 1
            if var_227 in self.index_228:
                tuple_226_1_index: int = 0
                tuple_226_1_vec: List[Tuple[int, int, int]] = self.index_229[var_227]
                while tuple_226_1_index < len(tuple_226_1_vec):
                    tuple_226_1 = tuple_226_1_vec[tuple_226_1_index]
                    tuple_226_1_index += 1
                    var_230 = tuple_226_1[0]
                    var_231 = tuple_226_1[1]
                    var_232 = tuple_226_1[2]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_231, var_230, ):
                        # Program TransitionState Region
                        tuple_232_227_5 = (var_232, var_227, self.var_5)
                        prev_state = self.table_43[tuple_232_227_5]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_232_227_5] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_232_227_5[1]].append((tuple_232_227_5[0], tuple_232_227_5[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_227_232_5 = (var_227, var_232, self.var_5)
                            prev_state = self.table_26[tuple_227_232_5]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_227_232_5] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_227_232_5[0]].append((tuple_227_232_5[1], tuple_227_232_5[2]))
                                    self.index_974[(tuple_227_232_5[0], tuple_227_232_5[1])].append(tuple_227_232_5[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_227)
                            if not ret:
                                # Program TransitionState Region
                                tuple_227_232_5 = (var_227, var_232, self.var_5)
                                prev_state = self.table_26[tuple_227_232_5]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_227_232_5] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_227_232_5[0]].append((tuple_227_232_5[1], tuple_227_232_5[2]))
                                        self.index_974[(tuple_227_232_5[0], tuple_227_232_5[1])].append(tuple_227_232_5[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_232, var_227)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_232_227 = (var_232, var_227)
                                        prev_state = self.table_9[tuple_232_227]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_232_227] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_232_227[0]].append(tuple_232_227[1])
                                                self.index_1000[tuple_232_227[1]].append(tuple_232_227[0])
                                            # Program VectorAppend Region
                                            vec_384.append(var_232)
                            # Program VectorAppend Region
                            vec_342.append(var_227)
                            # Program VectorAppend Region
                            vec_378.append(var_227)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_5:
                                # Program TransitionState Region
                                tuple_227 = var_227
                                prev_state = self.table_14[tuple_227]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_227] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_249: Tuple[int, int]
                                    scan_index_249: int = 0
                                    scan_tuple_249_vec: List[Tuple[int, int]] = self.index_248[var_227]
                                    while scan_index_249 < len(scan_tuple_249_vec):
                                        scan_tuple_249 = scan_tuple_249_vec[scan_index_249]
                                        scan_index_249 += 1
                                        vec_249.append(scan_tuple_249)
                                    # Program VectorLoop Region
                                    vec_index249 = 0
                                    while vec_index249 < len(vec_249):
                                        var_250, var_251 = vec_249[vec_index249]
                                        vec_index249 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_251 = self._resolve_edgetype(var_251)
                                        tuple_227_250_251 = (var_227, var_250, var_251)
                                        prev_state = self.table_26[tuple_227_250_251]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_227_250_251] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_227, var_250, var_251)

                                    # Program TransitionState Region
                                    tuple_227_227 = (var_227, var_227)
                                    prev_state = self.table_6[tuple_227_227]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_227_227] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_227_227[1]].append(tuple_227_227[0])
                                            self.index_949[tuple_227_227[0]].append(tuple_227_227[1])
                                        # Program VectorAppend Region
                                        vec_245.append((var_227, var_227))
                                    # Program VectorAppend Region
                                    vec_378.append(var_227)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_5:
                                # Program TransitionState Region
                                tuple_2_232_227 = (self.var_2, var_232, var_227)
                                prev_state = self.table_56[tuple_2_232_227]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_232_227] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_2_232_227[1]].append((tuple_2_232_227[0], tuple_2_232_227[2]))
                                    # Program VectorAppend Region
                                    vec_354.append(var_232)
        # Program VectorClear Region
        del vec_225[:]
        vec_index225 = 0
        # Program VectorUnique Region
        vec_257 = list(set(vec_257))
        vec_index257 = 0
        # Program TableJoin Region
        while vec_index257 < len(vec_257):
            var_259 = vec_257[vec_index257]
            vec_index257 += 1
            if var_259 in self.index_228:
                tuple_258_1_index: int = 0
                tuple_258_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_260[var_259]
                while tuple_258_1_index < len(tuple_258_1_vec):
                    tuple_258_1 = tuple_258_1_vec[tuple_258_1_index]
                    tuple_258_1_index += 1
                    var_261 = tuple_258_1[0]
                    var_262 = tuple_258_1[1]
                    var_263 = tuple_258_1[2]
                    var_264 = tuple_258_1[3]
                    var_265 = tuple_258_1[4]
                    # Program TupleCompare Region
                    if self.var_4 == var_261:
                        # Program TransitionState Region
                        tuple_263_259_0 = (var_263, var_259, self.var_0)
                        prev_state = self.table_43[tuple_263_259_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_263_259_0] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_263_259_0[1]].append((tuple_263_259_0[0], tuple_263_259_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_259_263_0 = (var_259, var_263, self.var_0)
                            prev_state = self.table_26[tuple_259_263_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_259_263_0] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_259_263_0[0]].append((tuple_259_263_0[1], tuple_259_263_0[2]))
                                    self.index_974[(tuple_259_263_0[0], tuple_259_263_0[1])].append(tuple_259_263_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_259)
                            if not ret:
                                # Program TransitionState Region
                                tuple_259_263_0 = (var_259, var_263, self.var_0)
                                prev_state = self.table_26[tuple_259_263_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_259_263_0] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_259_263_0[0]].append((tuple_259_263_0[1], tuple_259_263_0[2]))
                                        self.index_974[(tuple_259_263_0[0], tuple_259_263_0[1])].append(tuple_259_263_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_263, var_259)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_263_259 = (var_263, var_259)
                                        prev_state = self.table_9[tuple_263_259]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_263_259] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_263_259[0]].append(tuple_263_259[1])
                                                self.index_1000[tuple_263_259[1]].append(tuple_263_259[0])
                                            # Program VectorAppend Region
                                            vec_384.append(var_263)
                            # Program VectorAppend Region
                            vec_342.append(var_259)
                            # Program VectorAppend Region
                            vec_378.append(var_259)
                            # Program TransitionState Region
                            tuple_259 = var_259
                            prev_state = self.table_14[tuple_259]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_14[tuple_259] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_269: Tuple[int, int]
                                scan_index_269: int = 0
                                scan_tuple_269_vec: List[Tuple[int, int]] = self.index_248[var_259]
                                while scan_index_269 < len(scan_tuple_269_vec):
                                    scan_tuple_269 = scan_tuple_269_vec[scan_index_269]
                                    scan_index_269 += 1
                                    vec_269.append(scan_tuple_269)
                                # Program VectorLoop Region
                                vec_index269 = 0
                                while vec_index269 < len(vec_269):
                                    var_270, var_271 = vec_269[vec_index269]
                                    vec_index269 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_271 = self._resolve_edgetype(var_271)
                                    tuple_259_270_271 = (var_259, var_270, var_271)
                                    prev_state = self.table_26[tuple_259_270_271]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_259_270_271] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_252_(var_259, var_270, var_271)

                                # Program TransitionState Region
                                tuple_259_259 = (var_259, var_259)
                                prev_state = self.table_6[tuple_259_259]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_259_259] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_259_259[1]].append(tuple_259_259[0])
                                        self.index_949[tuple_259_259[0]].append(tuple_259_259[1])
                                    # Program VectorAppend Region
                                    vec_245.append((var_259, var_259))
                                # Program VectorAppend Region
                                vec_378.append(var_259)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_263_259 = (self.var_0, var_263, var_259)
                                prev_state = self.table_56[tuple_0_263_259]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_263_259] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_0_263_259[1]].append((tuple_0_263_259[0], tuple_0_263_259[2]))
                                    # Program VectorAppend Region
                                    vec_354.append(var_263)
        # Program VectorClear Region
        del vec_257[:]
        vec_index257 = 0
        # Program VectorUnique Region
        vec_273 = list(set(vec_273))
        vec_index273 = 0
        # Program TableJoin Region
        while vec_index273 < len(vec_273):
            var_275 = vec_273[vec_index273]
            vec_index273 += 1
            if var_275 in self.index_228:
                tuple_274_1_index: int = 0
                tuple_274_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_276[var_275]
                while tuple_274_1_index < len(tuple_274_1_vec):
                    tuple_274_1 = tuple_274_1_vec[tuple_274_1_index]
                    tuple_274_1_index += 1
                    var_277 = tuple_274_1[0]
                    var_278 = tuple_274_1[1]
                    var_279 = tuple_274_1[2]
                    var_280 = tuple_274_1[3]
                    var_281 = tuple_274_1[4]
                    # Program TupleCompare Region
                    if self.var_1 == var_277:
                        # Program TransitionState Region
                        tuple_279_275_2 = (var_279, var_275, self.var_2)
                        prev_state = self.table_43[tuple_279_275_2]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_279_275_2] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_279_275_2[1]].append((tuple_279_275_2[0], tuple_279_275_2[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_275_279_2 = (var_275, var_279, self.var_2)
                            prev_state = self.table_26[tuple_275_279_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_275_279_2] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_275_279_2[0]].append((tuple_275_279_2[1], tuple_275_279_2[2]))
                                    self.index_974[(tuple_275_279_2[0], tuple_275_279_2[1])].append(tuple_275_279_2[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_275)
                            if not ret:
                                # Program TransitionState Region
                                tuple_275_279_2 = (var_275, var_279, self.var_2)
                                prev_state = self.table_26[tuple_275_279_2]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_275_279_2] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_275_279_2[0]].append((tuple_275_279_2[1], tuple_275_279_2[2]))
                                        self.index_974[(tuple_275_279_2[0], tuple_275_279_2[1])].append(tuple_275_279_2[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_279, var_275)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_279_275 = (var_279, var_275)
                                        prev_state = self.table_9[tuple_279_275]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_279_275] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_279_275[0]].append(tuple_279_275[1])
                                                self.index_1000[tuple_279_275[1]].append(tuple_279_275[0])
                                            # Program VectorAppend Region
                                            vec_384.append(var_279)
                            # Program VectorAppend Region
                            vec_342.append(var_275)
                            # Program VectorAppend Region
                            vec_378.append(var_275)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_275 = var_275
                                prev_state = self.table_14[tuple_275]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_275] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_285: Tuple[int, int]
                                    scan_index_285: int = 0
                                    scan_tuple_285_vec: List[Tuple[int, int]] = self.index_248[var_275]
                                    while scan_index_285 < len(scan_tuple_285_vec):
                                        scan_tuple_285 = scan_tuple_285_vec[scan_index_285]
                                        scan_index_285 += 1
                                        vec_285.append(scan_tuple_285)
                                    # Program VectorLoop Region
                                    vec_index285 = 0
                                    while vec_index285 < len(vec_285):
                                        var_286, var_287 = vec_285[vec_index285]
                                        vec_index285 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_287 = self._resolve_edgetype(var_287)
                                        tuple_275_286_287 = (var_275, var_286, var_287)
                                        prev_state = self.table_26[tuple_275_286_287]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_275_286_287] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_275, var_286, var_287)

                                    # Program TransitionState Region
                                    tuple_275_275 = (var_275, var_275)
                                    prev_state = self.table_6[tuple_275_275]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_275_275] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_275_275[1]].append(tuple_275_275[0])
                                            self.index_949[tuple_275_275[0]].append(tuple_275_275[1])
                                        # Program VectorAppend Region
                                        vec_245.append((var_275, var_275))
                                    # Program VectorAppend Region
                                    vec_378.append(var_275)
                            # Program TransitionState Region
                            tuple_2_279_275 = (self.var_2, var_279, var_275)
                            prev_state = self.table_56[tuple_2_279_275]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_56[tuple_2_279_275] = 1 | 4
                                if not present_bit:
                                    self.index_358[tuple_2_279_275[1]].append((tuple_2_279_275[0], tuple_2_279_275[2]))
                                # Program VectorAppend Region
                                vec_354.append(var_279)
        # Program VectorClear Region
        del vec_273[:]
        vec_index273 = 0
        # Program VectorUnique Region
        vec_289 = list(set(vec_289))
        vec_index289 = 0
        # Program TableJoin Region
        while vec_index289 < len(vec_289):
            var_291 = vec_289[vec_index289]
            vec_index289 += 1
            tuple_290_0_index: int = 0
            tuple_290_0_vec: List[Tuple[int, int, int, int]] = self.index_292[var_291]
            while tuple_290_0_index < len(tuple_290_0_vec):
                tuple_290_0 = tuple_290_0_vec[tuple_290_0_index]
                tuple_290_0_index += 1
                var_293 = tuple_290_0[0]
                var_294 = tuple_290_0[1]
                var_295 = tuple_290_0[2]
                var_296 = tuple_290_0[3]
                if var_291 in self.index_228:
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_295, var_294, ):
                        # Program TransitionState Region
                        var_293 = self._resolve_edgetype(var_293)
                        tuple_296_291_293 = (var_296, var_291, var_293)
                        prev_state = self.table_43[tuple_296_291_293]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_296_291_293] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_296_291_293[1]].append((tuple_296_291_293[0], tuple_296_291_293[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            var_293 = self._resolve_edgetype(var_293)
                            tuple_291_296_293 = (var_291, var_296, var_293)
                            prev_state = self.table_26[tuple_291_296_293]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_291_296_293] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_291_296_293[0]].append((tuple_291_296_293[1], tuple_291_296_293[2]))
                                    self.index_974[(tuple_291_296_293[0], tuple_291_296_293[1])].append(tuple_291_296_293[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_291)
                            if not ret:
                                # Program TransitionState Region
                                var_293 = self._resolve_edgetype(var_293)
                                tuple_291_296_293 = (var_291, var_296, var_293)
                                prev_state = self.table_26[tuple_291_296_293]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_291_296_293] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_291_296_293[0]].append((tuple_291_296_293[1], tuple_291_296_293[2]))
                                        self.index_974[(tuple_291_296_293[0], tuple_291_296_293[1])].append(tuple_291_296_293[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_296, var_291)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_296_291 = (var_296, var_291)
                                        prev_state = self.table_9[tuple_296_291]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_296_291] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_296_291[0]].append(tuple_296_291[1])
                                                self.index_1000[tuple_296_291[1]].append(tuple_296_291[0])
                                            # Program VectorAppend Region
                                            vec_384.append(var_296)
                            # Program VectorAppend Region
                            vec_342.append(var_291)
                            # Program VectorAppend Region
                            vec_378.append(var_291)
                            # Program TupleCompare Region
                            if self.var_0 == var_293:
                                # Program TransitionState Region
                                tuple_291 = var_291
                                prev_state = self.table_14[tuple_291]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_291] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_300: Tuple[int, int]
                                    scan_index_300: int = 0
                                    scan_tuple_300_vec: List[Tuple[int, int]] = self.index_248[var_291]
                                    while scan_index_300 < len(scan_tuple_300_vec):
                                        scan_tuple_300 = scan_tuple_300_vec[scan_index_300]
                                        scan_index_300 += 1
                                        vec_300.append(scan_tuple_300)
                                    # Program VectorLoop Region
                                    vec_index300 = 0
                                    while vec_index300 < len(vec_300):
                                        var_301, var_302 = vec_300[vec_index300]
                                        vec_index300 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_302 = self._resolve_edgetype(var_302)
                                        tuple_291_301_302 = (var_291, var_301, var_302)
                                        prev_state = self.table_26[tuple_291_301_302]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_291_301_302] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_291, var_301, var_302)

                                    # Program TransitionState Region
                                    tuple_291_291 = (var_291, var_291)
                                    prev_state = self.table_6[tuple_291_291]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_291_291] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_291_291[1]].append(tuple_291_291[0])
                                            self.index_949[tuple_291_291[0]].append(tuple_291_291[1])
                                        # Program VectorAppend Region
                                        vec_245.append((var_291, var_291))
                                    # Program VectorAppend Region
                                    vec_378.append(var_291)
                            # Program TupleCompare Region
                            if self.var_2 == var_293:
                                # Program TransitionState Region
                                tuple_2_296_291 = (self.var_2, var_296, var_291)
                                prev_state = self.table_56[tuple_2_296_291]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_296_291] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_2_296_291[1]].append((tuple_2_296_291[0], tuple_2_296_291[2]))
                                    # Program VectorAppend Region
                                    vec_354.append(var_296)
        # Program VectorClear Region
        del vec_289[:]
        vec_index289 = 0
        # Program VectorUnique Region
        vec_304 = list(set(vec_304))
        vec_index304 = 0
        # Program TableJoin Region
        while vec_index304 < len(vec_304):
            var_306 = vec_304[vec_index304]
            vec_index304 += 1
            if var_306 in self.index_307:
                if var_306 in self.index_228:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_306 = var_306
                    prev_state = self.table_14[tuple_306]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_14[tuple_306] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_308: Tuple[int, int]
                        scan_index_308: int = 0
                        scan_tuple_308_vec: List[Tuple[int, int]] = self.index_248[var_306]
                        while scan_index_308 < len(scan_tuple_308_vec):
                            scan_tuple_308 = scan_tuple_308_vec[scan_index_308]
                            scan_index_308 += 1
                            vec_308.append(scan_tuple_308)
                        # Program VectorLoop Region
                        vec_index308 = 0
                        while vec_index308 < len(vec_308):
                            var_309, var_310 = vec_308[vec_index308]
                            vec_index308 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_310 = self._resolve_edgetype(var_310)
                            tuple_306_309_310 = (var_306, var_309, var_310)
                            prev_state = self.table_26[tuple_306_309_310]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_306_309_310] = 0 | 4
                                # Program Call Region
                                ret = self.proc_252_(var_306, var_309, var_310)

                        # Program TransitionState Region
                        tuple_306_306 = (var_306, var_306)
                        prev_state = self.table_6[tuple_306_306]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_306_306] = 1 | 4
                            if not present_bit:
                                self.index_387[tuple_306_306[1]].append(tuple_306_306[0])
                                self.index_949[tuple_306_306[0]].append(tuple_306_306[1])
                            # Program VectorAppend Region
                            vec_245.append((var_306, var_306))
                        # Program VectorAppend Region
                        vec_378.append(var_306)
        # Program VectorClear Region
        del vec_304[:]
        vec_index304 = 0
        # Program VectorUnique Region
        vec_312 = list(set(vec_312))
        vec_index312 = 0
        # Program TableJoin Region
        while vec_index312 < len(vec_312):
            var_314 = vec_312[vec_index312]
            vec_index312 += 1
            if var_314 in self.index_228:
                tuple_313_1_index: int = 0
                tuple_313_1_vec: List[Tuple[int, int, int, int]] = self.index_315[var_314]
                while tuple_313_1_index < len(tuple_313_1_vec):
                    tuple_313_1 = tuple_313_1_vec[tuple_313_1_index]
                    tuple_313_1_index += 1
                    var_316 = tuple_313_1[0]
                    var_317 = tuple_313_1[1]
                    var_318 = tuple_313_1[2]
                    var_319 = tuple_313_1[3]
                    # Program TupleCompare Region
                    if (self.var_3, self.var_0, ) == (var_317, var_318, ):
                        # Program TransitionState Region
                        tuple_319_314_3 = (var_319, var_314, self.var_3)
                        prev_state = self.table_43[tuple_319_314_3]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_319_314_3] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_319_314_3[1]].append((tuple_319_314_3[0], tuple_319_314_3[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_314_319_3 = (var_314, var_319, self.var_3)
                            prev_state = self.table_26[tuple_314_319_3]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_314_319_3] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_314_319_3[0]].append((tuple_314_319_3[1], tuple_314_319_3[2]))
                                    self.index_974[(tuple_314_319_3[0], tuple_314_319_3[1])].append(tuple_314_319_3[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_314)
                            if not ret:
                                # Program TransitionState Region
                                tuple_314_319_3 = (var_314, var_319, self.var_3)
                                prev_state = self.table_26[tuple_314_319_3]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_314_319_3] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_314_319_3[0]].append((tuple_314_319_3[1], tuple_314_319_3[2]))
                                        self.index_974[(tuple_314_319_3[0], tuple_314_319_3[1])].append(tuple_314_319_3[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_319, var_314)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_319_314 = (var_319, var_314)
                                        prev_state = self.table_9[tuple_319_314]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_319_314] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_319_314[0]].append(tuple_319_314[1])
                                                self.index_1000[tuple_319_314[1]].append(tuple_319_314[0])
                                            # Program VectorAppend Region
                                            vec_384.append(var_319)
                            # Program VectorAppend Region
                            vec_342.append(var_314)
                            # Program VectorAppend Region
                            vec_378.append(var_314)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_3:
                                # Program TransitionState Region
                                tuple_314 = var_314
                                prev_state = self.table_14[tuple_314]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_314] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_323: Tuple[int, int]
                                    scan_index_323: int = 0
                                    scan_tuple_323_vec: List[Tuple[int, int]] = self.index_248[var_314]
                                    while scan_index_323 < len(scan_tuple_323_vec):
                                        scan_tuple_323 = scan_tuple_323_vec[scan_index_323]
                                        scan_index_323 += 1
                                        vec_323.append(scan_tuple_323)
                                    # Program VectorLoop Region
                                    vec_index323 = 0
                                    while vec_index323 < len(vec_323):
                                        var_324, var_325 = vec_323[vec_index323]
                                        vec_index323 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_325 = self._resolve_edgetype(var_325)
                                        tuple_314_324_325 = (var_314, var_324, var_325)
                                        prev_state = self.table_26[tuple_314_324_325]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_314_324_325] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_314, var_324, var_325)

                                    # Program TransitionState Region
                                    tuple_314_314 = (var_314, var_314)
                                    prev_state = self.table_6[tuple_314_314]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_314_314] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_314_314[1]].append(tuple_314_314[0])
                                            self.index_949[tuple_314_314[0]].append(tuple_314_314[1])
                                        # Program VectorAppend Region
                                        vec_245.append((var_314, var_314))
                                    # Program VectorAppend Region
                                    vec_378.append(var_314)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_3:
                                # Program TransitionState Region
                                tuple_2_319_314 = (self.var_2, var_319, var_314)
                                prev_state = self.table_56[tuple_2_319_314]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_319_314] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_2_319_314[1]].append((tuple_2_319_314[0], tuple_2_319_314[2]))
                                    # Program VectorAppend Region
                                    vec_354.append(var_319)
        # Program VectorClear Region
        del vec_312[:]
        vec_index312 = 0
        # Program VectorUnique Region
        vec_327 = list(set(vec_327))
        vec_index327 = 0
        # Program TableJoin Region
        while vec_index327 < len(vec_327):
            var_329 = vec_327[vec_index327]
            vec_index327 += 1
            if var_329 in self.index_228:
                tuple_328_1_index: int = 0
                tuple_328_1_vec: List[Tuple[int, int, int, int]] = self.index_330[var_329]
                while tuple_328_1_index < len(tuple_328_1_vec):
                    tuple_328_1 = tuple_328_1_vec[tuple_328_1_index]
                    tuple_328_1_index += 1
                    var_331 = tuple_328_1[0]
                    var_332 = tuple_328_1[1]
                    var_333 = tuple_328_1[2]
                    var_334 = tuple_328_1[3]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_333, var_332, ):
                        # Program TransitionState Region
                        tuple_334_329_0 = (var_334, var_329, self.var_0)
                        prev_state = self.table_43[tuple_334_329_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_334_329_0] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_334_329_0[1]].append((tuple_334_329_0[0], tuple_334_329_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_329_334_0 = (var_329, var_334, self.var_0)
                            prev_state = self.table_26[tuple_329_334_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_329_334_0] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_329_334_0[0]].append((tuple_329_334_0[1], tuple_329_334_0[2]))
                                    self.index_974[(tuple_329_334_0[0], tuple_329_334_0[1])].append(tuple_329_334_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_329)
                            if not ret:
                                # Program TransitionState Region
                                tuple_329_334_0 = (var_329, var_334, self.var_0)
                                prev_state = self.table_26[tuple_329_334_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_329_334_0] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_329_334_0[0]].append((tuple_329_334_0[1], tuple_329_334_0[2]))
                                        self.index_974[(tuple_329_334_0[0], tuple_329_334_0[1])].append(tuple_329_334_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_334, var_329)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_334_329 = (var_334, var_329)
                                        prev_state = self.table_9[tuple_334_329]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_334_329] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_334_329[0]].append(tuple_334_329[1])
                                                self.index_1000[tuple_334_329[1]].append(tuple_334_329[0])
                                            # Program VectorAppend Region
                                            vec_384.append(var_334)
                            # Program VectorAppend Region
                            vec_342.append(var_329)
                            # Program VectorAppend Region
                            vec_378.append(var_329)
                            # Program TransitionState Region
                            tuple_329 = var_329
                            prev_state = self.table_14[tuple_329]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_14[tuple_329] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_338: Tuple[int, int]
                                scan_index_338: int = 0
                                scan_tuple_338_vec: List[Tuple[int, int]] = self.index_248[var_329]
                                while scan_index_338 < len(scan_tuple_338_vec):
                                    scan_tuple_338 = scan_tuple_338_vec[scan_index_338]
                                    scan_index_338 += 1
                                    vec_338.append(scan_tuple_338)
                                # Program VectorLoop Region
                                vec_index338 = 0
                                while vec_index338 < len(vec_338):
                                    var_339, var_340 = vec_338[vec_index338]
                                    vec_index338 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_340 = self._resolve_edgetype(var_340)
                                    tuple_329_339_340 = (var_329, var_339, var_340)
                                    prev_state = self.table_26[tuple_329_339_340]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_329_339_340] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_252_(var_329, var_339, var_340)

                                # Program TransitionState Region
                                tuple_329_329 = (var_329, var_329)
                                prev_state = self.table_6[tuple_329_329]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_329_329] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_329_329[1]].append(tuple_329_329[0])
                                        self.index_949[tuple_329_329[0]].append(tuple_329_329[1])
                                    # Program VectorAppend Region
                                    vec_245.append((var_329, var_329))
                                # Program VectorAppend Region
                                vec_378.append(var_329)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_334_329 = (self.var_0, var_334, var_329)
                                prev_state = self.table_56[tuple_0_334_329]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_334_329] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_0_334_329[1]].append((tuple_0_334_329[0], tuple_0_334_329[2]))
                                    # Program VectorAppend Region
                                    vec_354.append(var_334)
        # Program VectorClear Region
        del vec_327[:]
        vec_index327 = 0
        # Program VectorUnique Region
        vec_342 = list(set(vec_342))
        vec_index342 = 0
        # Program TableJoin Region
        while vec_index342 < len(vec_342):
            var_344 = vec_342[vec_index342]
            vec_index342 += 1
            tuple_343_0_index: int = 0
            tuple_343_0_vec: List[bytes] = self.index_345[var_344]
            while tuple_343_0_index < len(tuple_343_0_vec):
                tuple_343_0 = tuple_343_0_vec[tuple_343_0_index]
                tuple_343_0_index += 1
                var_347 = tuple_343_0
                tuple_343_1_index: int = 0
                tuple_343_1_vec: List[Tuple[int, int]] = self.index_346[var_344]
                while tuple_343_1_index < len(tuple_343_1_vec):
                    tuple_343_1 = tuple_343_1_vec[tuple_343_1_index]
                    tuple_343_1_index += 1
                    var_348 = tuple_343_1[0]
                    var_349 = tuple_343_1[1]
                    # Program TransitionState Region
                    tuple_344 = var_344
                    prev_state = self.table_14[tuple_344]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_14[tuple_344] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_350: Tuple[int, int]
                        scan_index_350: int = 0
                        scan_tuple_350_vec: List[Tuple[int, int]] = self.index_248[var_344]
                        while scan_index_350 < len(scan_tuple_350_vec):
                            scan_tuple_350 = scan_tuple_350_vec[scan_index_350]
                            scan_index_350 += 1
                            vec_350.append(scan_tuple_350)
                        # Program VectorLoop Region
                        vec_index350 = 0
                        while vec_index350 < len(vec_350):
                            var_351, var_352 = vec_350[vec_index350]
                            vec_index350 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_352 = self._resolve_edgetype(var_352)
                            tuple_344_351_352 = (var_344, var_351, var_352)
                            prev_state = self.table_26[tuple_344_351_352]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_344_351_352] = 0 | 4
                                # Program Call Region
                                ret = self.proc_252_(var_344, var_351, var_352)

                        # Program TransitionState Region
                        tuple_344_344 = (var_344, var_344)
                        prev_state = self.table_6[tuple_344_344]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_344_344] = 1 | 4
                            if not present_bit:
                                self.index_387[tuple_344_344[1]].append(tuple_344_344[0])
                                self.index_949[tuple_344_344[0]].append(tuple_344_344[1])
                            # Program VectorAppend Region
                            vec_245.append((var_344, var_344))
                        # Program VectorAppend Region
                        vec_378.append(var_344)
        # Program VectorClear Region
        del vec_342[:]
        vec_index342 = 0
        # Program VectorUnique Region
        vec_354 = list(set(vec_354))
        vec_index354 = 0
        # Program TableJoin Region
        while vec_index354 < len(vec_354):
            var_356 = vec_354[vec_index354]
            vec_index354 += 1
            tuple_355_0_index: int = 0
            tuple_355_0_vec: List[Tuple[int, bytes, bytes]] = self.index_357[var_356]
            while tuple_355_0_index < len(tuple_355_0_vec):
                tuple_355_0 = tuple_355_0_vec[tuple_355_0_index]
                tuple_355_0_index += 1
                var_359 = tuple_355_0[0]
                var_360 = tuple_355_0[1]
                var_361 = tuple_355_0[2]
                tuple_355_1_index: int = 0
                tuple_355_1_vec: List[Tuple[int, int]] = self.index_358[var_356]
                while tuple_355_1_index < len(tuple_355_1_vec):
                    tuple_355_1 = tuple_355_1_vec[tuple_355_1_index]
                    tuple_355_1_index += 1
                    var_362 = tuple_355_1[0]
                    var_363 = tuple_355_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_359, var_362, ):
                        # Program TransitionState Region
                        tuple_2_1_356_360_361_363 = (self.var_2, self.var_1, var_356, var_360, var_361, var_363)
                        prev_state = self.table_60[tuple_2_1_356_360_361_363]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_356_360_361_363] = 1 | 4
                            if not present_bit:
                                self.index_367[tuple_2_1_356_360_361_363[5]].append((tuple_2_1_356_360_361_363[0], tuple_2_1_356_360_361_363[1], tuple_2_1_356_360_361_363[2], tuple_2_1_356_360_361_363[3], tuple_2_1_356_360_361_363[4]))
                            # Program VectorAppend Region
                            vec_364.append(var_363)
        # Program VectorClear Region
        del vec_354[:]
        vec_index354 = 0
        # Program VectorUnique Region
        vec_364 = list(set(vec_364))
        vec_index364 = 0
        # Program TableJoin Region
        while vec_index364 < len(vec_364):
            var_366 = vec_364[vec_index364]
            vec_index364 += 1
            tuple_365_0_index: int = 0
            tuple_365_0_vec: List[bytes] = self.index_345[var_366]
            while tuple_365_0_index < len(tuple_365_0_vec):
                tuple_365_0 = tuple_365_0_vec[tuple_365_0_index]
                tuple_365_0_index += 1
                var_368 = tuple_365_0
                tuple_365_1_index: int = 0
                tuple_365_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_367[var_366]
                while tuple_365_1_index < len(tuple_365_1_vec):
                    tuple_365_1 = tuple_365_1_vec[tuple_365_1_index]
                    tuple_365_1_index += 1
                    var_369 = tuple_365_1[0]
                    var_370 = tuple_365_1[1]
                    var_371 = tuple_365_1[2]
                    var_372 = tuple_365_1[3]
                    var_373 = tuple_365_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_370, var_369, ):
                        # Program TransitionState Region
                        tuple_371 = var_371
                        prev_state = self.table_14[tuple_371]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_14[tuple_371] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_374: Tuple[int, int]
                            scan_index_374: int = 0
                            scan_tuple_374_vec: List[Tuple[int, int]] = self.index_248[var_371]
                            while scan_index_374 < len(scan_tuple_374_vec):
                                scan_tuple_374 = scan_tuple_374_vec[scan_index_374]
                                scan_index_374 += 1
                                vec_374.append(scan_tuple_374)
                            # Program VectorLoop Region
                            vec_index374 = 0
                            while vec_index374 < len(vec_374):
                                var_375, var_376 = vec_374[vec_index374]
                                vec_index374 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_376 = self._resolve_edgetype(var_376)
                                tuple_371_375_376 = (var_371, var_375, var_376)
                                prev_state = self.table_26[tuple_371_375_376]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_371_375_376] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_252_(var_371, var_375, var_376)

                            # Program TransitionState Region
                            tuple_371_371 = (var_371, var_371)
                            prev_state = self.table_6[tuple_371_371]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_371_371] = 1 | 4
                                if not present_bit:
                                    self.index_387[tuple_371_371[1]].append(tuple_371_371[0])
                                    self.index_949[tuple_371_371[0]].append(tuple_371_371[1])
                                # Program VectorAppend Region
                                vec_245.append((var_371, var_371))
                            # Program VectorAppend Region
                            vec_378.append(var_371)
        # Program VectorClear Region
        del vec_364[:]
        vec_index364 = 0
        # Program VectorUnique Region
        vec_378 = list(set(vec_378))
        vec_index378 = 0
        # Program TableJoin Region
        while vec_index378 < len(vec_378):
            var_380 = vec_378[vec_index378]
            vec_index378 += 1
            tuple_379_0_index: int = 0
            tuple_379_0_vec: List[Tuple[int, int]] = self.index_346[var_380]
            while tuple_379_0_index < len(tuple_379_0_vec):
                tuple_379_0 = tuple_379_0_vec[tuple_379_0_index]
                tuple_379_0_index += 1
                var_382 = tuple_379_0[0]
                var_383 = tuple_379_0[1]
                if var_380 in self.index_381:
                    # Program TransitionState Region
                    tuple_382_380 = (var_382, var_380)
                    prev_state = self.table_16[tuple_382_380]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_16[tuple_382_380] = 1 | 4
                        if not present_bit:
                            self.index_406[tuple_382_380[1]].append(tuple_382_380[0])
                            self.index_956[tuple_382_380[0]].append(tuple_382_380[1])
                        # Program VectorAppend Region
                        vec_403.append(var_380)
        # Program VectorClear Region
        del vec_378[:]
        vec_index378 = 0
        # Program VectorUnique Region
        vec_384 = list(set(vec_384))
        vec_index384 = 0
        # Program TableJoin Region
        while vec_index384 < len(vec_384):
            var_386 = vec_384[vec_index384]
            vec_index384 += 1
            tuple_385_0_index: int = 0
            tuple_385_0_vec: List[int] = self.index_387[var_386]
            while tuple_385_0_index < len(tuple_385_0_vec):
                tuple_385_0 = tuple_385_0_vec[tuple_385_0_index]
                tuple_385_0_index += 1
                var_389 = tuple_385_0
                tuple_385_1_index: int = 0
                tuple_385_1_vec: List[int] = self.index_388[var_386]
                while tuple_385_1_index < len(tuple_385_1_vec):
                    tuple_385_1 = tuple_385_1_vec[tuple_385_1_index]
                    tuple_385_1_index += 1
                    var_390 = tuple_385_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_950_(var_389, var_386)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_953_(var_386, var_390)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_399_(var_389, var_390)
                            if not ret:
                                # Program TransitionState Region
                                tuple_389_390 = (var_389, var_390)
                                prev_state = self.table_6[tuple_389_390]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_389_390] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_389_390[1]].append(tuple_389_390[0])
                                        self.index_949[tuple_389_390[0]].append(tuple_389_390[1])
                                    # Program VectorAppend Region
                                    vec_245.append((var_389, var_390))
        # Program VectorClear Region
        del vec_384[:]
        vec_index384 = 0
        # Program VectorUnique Region
        vec_403 = list(set(vec_403))
        vec_index403 = 0
        # Program TableJoin Region
        while vec_index403 < len(vec_403):
            var_405 = vec_403[vec_index403]
            vec_index403 += 1
            tuple_404_0_index: int = 0
            tuple_404_0_vec: List[int] = self.index_406[var_405]
            while tuple_404_0_index < len(tuple_404_0_vec):
                tuple_404_0 = tuple_404_0_vec[tuple_404_0_index]
                tuple_404_0_index += 1
                var_407 = tuple_404_0
                tuple_404_1_index: int = 0
                tuple_404_1_vec: List[bytes] = self.index_345[var_405]
                while tuple_404_1_index < len(tuple_404_1_vec):
                    tuple_404_1 = tuple_404_1_vec[tuple_404_1_index]
                    tuple_404_1_index += 1
                    var_408 = tuple_404_1
                    # Program TransitionState Region
                    tuple_407 = var_407
                    prev_state = self.table_12[tuple_407]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_407] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_403[:]
        vec_index403 = 0
        # Induction Fixpoint Loop Region
        while len(vec_245):
            # Program Call Region
            param_247_0 = [vec_245]
            ret = self.proc_241_(param_247_0)
            vec_245 = param_247_0[0]

        vec_index245 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_245[:]
        vec_index245 = 0
        # Program Return Region
        return False

    def proc_234_(self, var_235: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1012_(var_235)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_237_(self, var_238: int, var_239: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_9[(var_238, var_239)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_238_239 = (var_238, var_239)
            prev_state = self.table_9[tuple_238_239]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_9[tuple_238_239] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_970_(var_239, var_238)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_238_239 = (var_238, var_239)
                    prev_state = self.table_9[tuple_238_239]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_238_239] = 1 | 4
                        if not present_bit:
                            self.index_388[tuple_238_239[0]].append(tuple_238_239[1])
                            self.index_1000[tuple_238_239[1]].append(tuple_238_239[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False

    def proc_241_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_242 = param_0[0]
        vec_index242: int = 0
        vec_409: List[Tuple[int, int]] = list()
        vec_index409: int = 0
        vec_412: List[int] = list()
        vec_index412: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_242, vec_409 = vec_409, vec_242
        # Program VectorLoop Region
        while vec_index409 < len(vec_409):
            var_410, var_411 = vec_409[vec_index409]
            vec_index409 += 1
            # Program VectorAppend Region
            vec_412.append(var_411)
        # Program VectorUnique Region
        vec_412 = list(set(vec_412))
        vec_index412 = 0
        # Program TableJoin Region
        while vec_index412 < len(vec_412):
            var_414 = vec_412[vec_index412]
            vec_index412 += 1
            tuple_413_0_index: int = 0
            tuple_413_0_vec: List[int] = self.index_387[var_414]
            while tuple_413_0_index < len(tuple_413_0_vec):
                tuple_413_0 = tuple_413_0_vec[tuple_413_0_index]
                tuple_413_0_index += 1
                var_415 = tuple_413_0
                tuple_413_1_index: int = 0
                tuple_413_1_vec: List[int] = self.index_388[var_414]
                while tuple_413_1_index < len(tuple_413_1_vec):
                    tuple_413_1 = tuple_413_1_vec[tuple_413_1_index]
                    tuple_413_1_index += 1
                    var_416 = tuple_413_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_950_(var_415, var_414)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_953_(var_414, var_416)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_399_(var_415, var_416)
                            if not ret:
                                # Program TransitionState Region
                                tuple_415_416 = (var_415, var_416)
                                prev_state = self.table_6[tuple_415_416]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_415_416] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_415_416[1]].append(tuple_415_416[0])
                                        self.index_949[tuple_415_416[0]].append(tuple_415_416[1])
                                    # Program VectorAppend Region
                                    vec_242.append((var_415, var_416))
        # Program VectorClear Region
        del vec_412[:]
        vec_index412 = 0
        # Program VectorClear Region
        del vec_409[:]
        vec_index409 = 0
        # Program Return Region
        param_0[0] = vec_242
        return False

    def proc_252_(self, var_253: int, var_254: int, var_255: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_254_253 = (var_254, var_253)
        prev_state = self.table_9[tuple_254_253]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_9[tuple_254_253] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1035_(var_254, var_253)

            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1031_(var_254, var_253)

        # Program Return Region
        return False

    def proc_399_(self, var_400: int, var_401: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_400, var_401)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_400_401 = (var_400, var_401)
            prev_state = self.table_6[tuple_400_401]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_400_401] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_995_(var_400, var_401)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_400_401 = (var_400, var_401)
                    prev_state = self.table_6[tuple_400_401]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_400_401] = 1 | 4
                        if not present_bit:
                            self.index_387[tuple_400_401[1]].append(tuple_400_401[0])
                            self.index_949[tuple_400_401[0]].append(tuple_400_401[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False

    def external_symbol_2(self, vec_423: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index423: int = 0
        vec_426: List[int] = list()
        vec_index426: int = 0
        vec_435: List[Tuple[int, int]] = list()
        vec_index435: int = 0
        vec_438: List[Tuple[int, int]] = list()
        vec_index438: int = 0
        vec_442: List[int] = list()
        vec_index442: int = 0
        vec_453: List[Tuple[int, int]] = list()
        vec_index453: int = 0
        vec_457: List[int] = list()
        vec_index457: int = 0
        vec_468: List[Tuple[int, int]] = list()
        vec_index468: int = 0
        vec_472: List[int] = list()
        vec_index472: int = 0
        vec_482: List[Tuple[int, int]] = list()
        vec_index482: int = 0
        vec_486: List[int] = list()
        vec_index486: int = 0
        vec_489: List[Tuple[int, int]] = list()
        vec_index489: int = 0
        vec_493: List[int] = list()
        vec_index493: int = 0
        vec_503: List[Tuple[int, int]] = list()
        vec_index503: int = 0
        vec_507: List[int] = list()
        vec_index507: int = 0
        vec_517: List[Tuple[int, int]] = list()
        vec_index517: int = 0
        vec_521: List[int] = list()
        vec_index521: int = 0
        vec_527: List[Tuple[int, int]] = list()
        vec_index527: int = 0
        vec_531: List[int] = list()
        vec_index531: int = 0
        vec_539: List[int] = list()
        vec_index539: int = 0
        vec_548: List[Tuple[int, int]] = list()
        vec_index548: int = 0
        vec_552: List[int] = list()
        vec_index552: int = 0
        vec_557: List[int] = list()
        vec_index557: int = 0
        vec_565: List[int] = list()
        vec_index565: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index423 = 0
        while vec_index423 < len(vec_423):
            var_424, var_425 = vec_423[vec_index423]
            vec_index423 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_424_425 = (var_424, var_425)
            prev_state = self.table_40[tuple_424_425]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_40[tuple_424_425] = 1 | 4
                if not present_bit:
                    self.index_345[tuple_424_425[0]].append(tuple_424_425[1])
                # Program Parallel Region
                # Program TransitionState Region
                tuple_424 = var_424
                prev_state = self.table_49[tuple_424]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_424] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_486.append(var_424)
                    # Program VectorAppend Region
                    vec_472.append(var_424)
                    # Program VectorAppend Region
                    vec_507.append(var_424)
                    # Program VectorAppend Region
                    vec_493.append(var_424)
                    # Program VectorAppend Region
                    vec_457.append(var_424)
                    # Program VectorAppend Region
                    vec_442.append(var_424)
                    # Program VectorAppend Region
                    vec_426.append(var_424)
                # Program VectorAppend Region
                vec_521.append(var_424)
                # Program VectorAppend Region
                vec_539.append(var_424)
                # Program VectorAppend Region
                vec_565.append(var_424)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_424_425 = (var_424, var_425)
            prev_state = self.table_40[tuple_424_425]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_40[tuple_424_425] = 1 | 4
                if not present_bit:
                    self.index_345[tuple_424_425[0]].append(tuple_424_425[1])
                # Program Parallel Region
                # Program TransitionState Region
                tuple_424 = var_424
                prev_state = self.table_49[tuple_424]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_424] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_486.append(var_424)
                    # Program VectorAppend Region
                    vec_472.append(var_424)
                    # Program VectorAppend Region
                    vec_507.append(var_424)
                    # Program VectorAppend Region
                    vec_493.append(var_424)
                    # Program VectorAppend Region
                    vec_457.append(var_424)
                    # Program VectorAppend Region
                    vec_442.append(var_424)
                    # Program VectorAppend Region
                    vec_426.append(var_424)
                # Program VectorAppend Region
                vec_521.append(var_424)
                # Program VectorAppend Region
                vec_539.append(var_424)
                # Program VectorAppend Region
                vec_565.append(var_424)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_424_425 = (var_424, var_425)
            prev_state = self.table_40[tuple_424_425]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_40[tuple_424_425] = 1 | 4
                if not present_bit:
                    self.index_345[tuple_424_425[0]].append(tuple_424_425[1])
                # Program Parallel Region
                # Program TransitionState Region
                tuple_424 = var_424
                prev_state = self.table_49[tuple_424]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_424] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_486.append(var_424)
                    # Program VectorAppend Region
                    vec_472.append(var_424)
                    # Program VectorAppend Region
                    vec_507.append(var_424)
                    # Program VectorAppend Region
                    vec_493.append(var_424)
                    # Program VectorAppend Region
                    vec_457.append(var_424)
                    # Program VectorAppend Region
                    vec_442.append(var_424)
                    # Program VectorAppend Region
                    vec_426.append(var_424)
                # Program VectorAppend Region
                vec_521.append(var_424)
                # Program VectorAppend Region
                vec_539.append(var_424)
                # Program VectorAppend Region
                vec_565.append(var_424)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_424_425 = (var_424, var_425)
            prev_state = self.table_40[tuple_424_425]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_40[tuple_424_425] = 1 | 4
                if not present_bit:
                    self.index_345[tuple_424_425[0]].append(tuple_424_425[1])
                # Program Parallel Region
                # Program TransitionState Region
                tuple_424 = var_424
                prev_state = self.table_49[tuple_424]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_424] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_486.append(var_424)
                    # Program VectorAppend Region
                    vec_472.append(var_424)
                    # Program VectorAppend Region
                    vec_507.append(var_424)
                    # Program VectorAppend Region
                    vec_493.append(var_424)
                    # Program VectorAppend Region
                    vec_457.append(var_424)
                    # Program VectorAppend Region
                    vec_442.append(var_424)
                    # Program VectorAppend Region
                    vec_426.append(var_424)
                # Program VectorAppend Region
                vec_521.append(var_424)
                # Program VectorAppend Region
                vec_539.append(var_424)
                # Program VectorAppend Region
                vec_565.append(var_424)
        # Program VectorUnique Region
        vec_426 = list(set(vec_426))
        vec_index426 = 0
        # Program TableJoin Region
        while vec_index426 < len(vec_426):
            var_428 = vec_426[vec_index426]
            vec_index426 += 1
            if var_428 in self.index_228:
                tuple_427_1_index: int = 0
                tuple_427_1_vec: List[Tuple[int, int, int]] = self.index_229[var_428]
                while tuple_427_1_index < len(tuple_427_1_vec):
                    tuple_427_1 = tuple_427_1_vec[tuple_427_1_index]
                    tuple_427_1_index += 1
                    var_429 = tuple_427_1[0]
                    var_430 = tuple_427_1[1]
                    var_431 = tuple_427_1[2]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_430, var_429, ):
                        # Program TransitionState Region
                        tuple_431_428_5 = (var_431, var_428, self.var_5)
                        prev_state = self.table_43[tuple_431_428_5]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_431_428_5] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_431_428_5[1]].append((tuple_431_428_5[0], tuple_431_428_5[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_428_431_5 = (var_428, var_431, self.var_5)
                            prev_state = self.table_26[tuple_428_431_5]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_428_431_5] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_428_431_5[0]].append((tuple_428_431_5[1], tuple_428_431_5[2]))
                                    self.index_974[(tuple_428_431_5[0], tuple_428_431_5[1])].append(tuple_428_431_5[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_428)
                            if not ret:
                                # Program TransitionState Region
                                tuple_428_431_5 = (var_428, var_431, self.var_5)
                                prev_state = self.table_26[tuple_428_431_5]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_428_431_5] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_428_431_5[0]].append((tuple_428_431_5[1], tuple_428_431_5[2]))
                                        self.index_974[(tuple_428_431_5[0], tuple_428_431_5[1])].append(tuple_428_431_5[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_431, var_428)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_431_428 = (var_431, var_428)
                                        prev_state = self.table_9[tuple_431_428]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_431_428] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_431_428[0]].append(tuple_431_428[1])
                                                self.index_1000[tuple_431_428[1]].append(tuple_431_428[0])
                                            # Program VectorAppend Region
                                            vec_557.append(var_431)
                            # Program VectorAppend Region
                            vec_521.append(var_428)
                            # Program VectorAppend Region
                            vec_552.append(var_428)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_5:
                                # Program TransitionState Region
                                tuple_428 = var_428
                                prev_state = self.table_14[tuple_428]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_428] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_438: Tuple[int, int]
                                    scan_index_438: int = 0
                                    scan_tuple_438_vec: List[Tuple[int, int]] = self.index_248[var_428]
                                    while scan_index_438 < len(scan_tuple_438_vec):
                                        scan_tuple_438 = scan_tuple_438_vec[scan_index_438]
                                        scan_index_438 += 1
                                        vec_438.append(scan_tuple_438)
                                    # Program VectorLoop Region
                                    vec_index438 = 0
                                    while vec_index438 < len(vec_438):
                                        var_439, var_440 = vec_438[vec_index438]
                                        vec_index438 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_440 = self._resolve_edgetype(var_440)
                                        tuple_428_439_440 = (var_428, var_439, var_440)
                                        prev_state = self.table_26[tuple_428_439_440]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_428_439_440] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_428, var_439, var_440)

                                    # Program TransitionState Region
                                    tuple_428_428 = (var_428, var_428)
                                    prev_state = self.table_6[tuple_428_428]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_428_428] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_428_428[1]].append(tuple_428_428[0])
                                            self.index_949[tuple_428_428[0]].append(tuple_428_428[1])
                                        # Program VectorAppend Region
                                        vec_435.append((var_428, var_428))
                                    # Program VectorAppend Region
                                    vec_552.append(var_428)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_5:
                                # Program TransitionState Region
                                tuple_2_431_428 = (self.var_2, var_431, var_428)
                                prev_state = self.table_56[tuple_2_431_428]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_431_428] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_2_431_428[1]].append((tuple_2_431_428[0], tuple_2_431_428[2]))
                                    # Program VectorAppend Region
                                    vec_531.append(var_431)
        # Program VectorClear Region
        del vec_426[:]
        vec_index426 = 0
        # Program VectorUnique Region
        vec_442 = list(set(vec_442))
        vec_index442 = 0
        # Program TableJoin Region
        while vec_index442 < len(vec_442):
            var_444 = vec_442[vec_index442]
            vec_index442 += 1
            if var_444 in self.index_228:
                tuple_443_1_index: int = 0
                tuple_443_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_260[var_444]
                while tuple_443_1_index < len(tuple_443_1_vec):
                    tuple_443_1 = tuple_443_1_vec[tuple_443_1_index]
                    tuple_443_1_index += 1
                    var_445 = tuple_443_1[0]
                    var_446 = tuple_443_1[1]
                    var_447 = tuple_443_1[2]
                    var_448 = tuple_443_1[3]
                    var_449 = tuple_443_1[4]
                    # Program TupleCompare Region
                    if self.var_4 == var_445:
                        # Program TransitionState Region
                        tuple_447_444_0 = (var_447, var_444, self.var_0)
                        prev_state = self.table_43[tuple_447_444_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_447_444_0] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_447_444_0[1]].append((tuple_447_444_0[0], tuple_447_444_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_444_447_0 = (var_444, var_447, self.var_0)
                            prev_state = self.table_26[tuple_444_447_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_444_447_0] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_444_447_0[0]].append((tuple_444_447_0[1], tuple_444_447_0[2]))
                                    self.index_974[(tuple_444_447_0[0], tuple_444_447_0[1])].append(tuple_444_447_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_444)
                            if not ret:
                                # Program TransitionState Region
                                tuple_444_447_0 = (var_444, var_447, self.var_0)
                                prev_state = self.table_26[tuple_444_447_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_444_447_0] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_444_447_0[0]].append((tuple_444_447_0[1], tuple_444_447_0[2]))
                                        self.index_974[(tuple_444_447_0[0], tuple_444_447_0[1])].append(tuple_444_447_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_447, var_444)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_447_444 = (var_447, var_444)
                                        prev_state = self.table_9[tuple_447_444]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_447_444] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_447_444[0]].append(tuple_447_444[1])
                                                self.index_1000[tuple_447_444[1]].append(tuple_447_444[0])
                                            # Program VectorAppend Region
                                            vec_557.append(var_447)
                            # Program VectorAppend Region
                            vec_521.append(var_444)
                            # Program VectorAppend Region
                            vec_552.append(var_444)
                            # Program TransitionState Region
                            tuple_444 = var_444
                            prev_state = self.table_14[tuple_444]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_14[tuple_444] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_453: Tuple[int, int]
                                scan_index_453: int = 0
                                scan_tuple_453_vec: List[Tuple[int, int]] = self.index_248[var_444]
                                while scan_index_453 < len(scan_tuple_453_vec):
                                    scan_tuple_453 = scan_tuple_453_vec[scan_index_453]
                                    scan_index_453 += 1
                                    vec_453.append(scan_tuple_453)
                                # Program VectorLoop Region
                                vec_index453 = 0
                                while vec_index453 < len(vec_453):
                                    var_454, var_455 = vec_453[vec_index453]
                                    vec_index453 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_455 = self._resolve_edgetype(var_455)
                                    tuple_444_454_455 = (var_444, var_454, var_455)
                                    prev_state = self.table_26[tuple_444_454_455]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_444_454_455] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_252_(var_444, var_454, var_455)

                                # Program TransitionState Region
                                tuple_444_444 = (var_444, var_444)
                                prev_state = self.table_6[tuple_444_444]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_444_444] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_444_444[1]].append(tuple_444_444[0])
                                        self.index_949[tuple_444_444[0]].append(tuple_444_444[1])
                                    # Program VectorAppend Region
                                    vec_435.append((var_444, var_444))
                                # Program VectorAppend Region
                                vec_552.append(var_444)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_447_444 = (self.var_0, var_447, var_444)
                                prev_state = self.table_56[tuple_0_447_444]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_447_444] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_0_447_444[1]].append((tuple_0_447_444[0], tuple_0_447_444[2]))
                                    # Program VectorAppend Region
                                    vec_531.append(var_447)
        # Program VectorClear Region
        del vec_442[:]
        vec_index442 = 0
        # Program VectorUnique Region
        vec_457 = list(set(vec_457))
        vec_index457 = 0
        # Program TableJoin Region
        while vec_index457 < len(vec_457):
            var_459 = vec_457[vec_index457]
            vec_index457 += 1
            if var_459 in self.index_228:
                tuple_458_1_index: int = 0
                tuple_458_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_276[var_459]
                while tuple_458_1_index < len(tuple_458_1_vec):
                    tuple_458_1 = tuple_458_1_vec[tuple_458_1_index]
                    tuple_458_1_index += 1
                    var_460 = tuple_458_1[0]
                    var_461 = tuple_458_1[1]
                    var_462 = tuple_458_1[2]
                    var_463 = tuple_458_1[3]
                    var_464 = tuple_458_1[4]
                    # Program TupleCompare Region
                    if self.var_1 == var_460:
                        # Program TransitionState Region
                        tuple_462_459_2 = (var_462, var_459, self.var_2)
                        prev_state = self.table_43[tuple_462_459_2]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_462_459_2] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_462_459_2[1]].append((tuple_462_459_2[0], tuple_462_459_2[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_459_462_2 = (var_459, var_462, self.var_2)
                            prev_state = self.table_26[tuple_459_462_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_459_462_2] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_459_462_2[0]].append((tuple_459_462_2[1], tuple_459_462_2[2]))
                                    self.index_974[(tuple_459_462_2[0], tuple_459_462_2[1])].append(tuple_459_462_2[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_459)
                            if not ret:
                                # Program TransitionState Region
                                tuple_459_462_2 = (var_459, var_462, self.var_2)
                                prev_state = self.table_26[tuple_459_462_2]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_459_462_2] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_459_462_2[0]].append((tuple_459_462_2[1], tuple_459_462_2[2]))
                                        self.index_974[(tuple_459_462_2[0], tuple_459_462_2[1])].append(tuple_459_462_2[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_462, var_459)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_462_459 = (var_462, var_459)
                                        prev_state = self.table_9[tuple_462_459]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_462_459] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_462_459[0]].append(tuple_462_459[1])
                                                self.index_1000[tuple_462_459[1]].append(tuple_462_459[0])
                                            # Program VectorAppend Region
                                            vec_557.append(var_462)
                            # Program VectorAppend Region
                            vec_521.append(var_459)
                            # Program VectorAppend Region
                            vec_552.append(var_459)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_459 = var_459
                                prev_state = self.table_14[tuple_459]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_459] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_468: Tuple[int, int]
                                    scan_index_468: int = 0
                                    scan_tuple_468_vec: List[Tuple[int, int]] = self.index_248[var_459]
                                    while scan_index_468 < len(scan_tuple_468_vec):
                                        scan_tuple_468 = scan_tuple_468_vec[scan_index_468]
                                        scan_index_468 += 1
                                        vec_468.append(scan_tuple_468)
                                    # Program VectorLoop Region
                                    vec_index468 = 0
                                    while vec_index468 < len(vec_468):
                                        var_469, var_470 = vec_468[vec_index468]
                                        vec_index468 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_470 = self._resolve_edgetype(var_470)
                                        tuple_459_469_470 = (var_459, var_469, var_470)
                                        prev_state = self.table_26[tuple_459_469_470]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_459_469_470] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_459, var_469, var_470)

                                    # Program TransitionState Region
                                    tuple_459_459 = (var_459, var_459)
                                    prev_state = self.table_6[tuple_459_459]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_459_459] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_459_459[1]].append(tuple_459_459[0])
                                            self.index_949[tuple_459_459[0]].append(tuple_459_459[1])
                                        # Program VectorAppend Region
                                        vec_435.append((var_459, var_459))
                                    # Program VectorAppend Region
                                    vec_552.append(var_459)
                            # Program TransitionState Region
                            tuple_2_462_459 = (self.var_2, var_462, var_459)
                            prev_state = self.table_56[tuple_2_462_459]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_56[tuple_2_462_459] = 1 | 4
                                if not present_bit:
                                    self.index_358[tuple_2_462_459[1]].append((tuple_2_462_459[0], tuple_2_462_459[2]))
                                # Program VectorAppend Region
                                vec_531.append(var_462)
        # Program VectorClear Region
        del vec_457[:]
        vec_index457 = 0
        # Program VectorUnique Region
        vec_472 = list(set(vec_472))
        vec_index472 = 0
        # Program TableJoin Region
        while vec_index472 < len(vec_472):
            var_474 = vec_472[vec_index472]
            vec_index472 += 1
            tuple_473_0_index: int = 0
            tuple_473_0_vec: List[Tuple[int, int, int, int]] = self.index_292[var_474]
            while tuple_473_0_index < len(tuple_473_0_vec):
                tuple_473_0 = tuple_473_0_vec[tuple_473_0_index]
                tuple_473_0_index += 1
                var_475 = tuple_473_0[0]
                var_476 = tuple_473_0[1]
                var_477 = tuple_473_0[2]
                var_478 = tuple_473_0[3]
                if var_474 in self.index_228:
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_477, var_476, ):
                        # Program TransitionState Region
                        var_475 = self._resolve_edgetype(var_475)
                        tuple_478_474_475 = (var_478, var_474, var_475)
                        prev_state = self.table_43[tuple_478_474_475]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_478_474_475] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_478_474_475[1]].append((tuple_478_474_475[0], tuple_478_474_475[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            var_475 = self._resolve_edgetype(var_475)
                            tuple_474_478_475 = (var_474, var_478, var_475)
                            prev_state = self.table_26[tuple_474_478_475]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_474_478_475] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_474_478_475[0]].append((tuple_474_478_475[1], tuple_474_478_475[2]))
                                    self.index_974[(tuple_474_478_475[0], tuple_474_478_475[1])].append(tuple_474_478_475[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_474)
                            if not ret:
                                # Program TransitionState Region
                                var_475 = self._resolve_edgetype(var_475)
                                tuple_474_478_475 = (var_474, var_478, var_475)
                                prev_state = self.table_26[tuple_474_478_475]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_474_478_475] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_474_478_475[0]].append((tuple_474_478_475[1], tuple_474_478_475[2]))
                                        self.index_974[(tuple_474_478_475[0], tuple_474_478_475[1])].append(tuple_474_478_475[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_478, var_474)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_478_474 = (var_478, var_474)
                                        prev_state = self.table_9[tuple_478_474]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_478_474] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_478_474[0]].append(tuple_478_474[1])
                                                self.index_1000[tuple_478_474[1]].append(tuple_478_474[0])
                                            # Program VectorAppend Region
                                            vec_557.append(var_478)
                            # Program VectorAppend Region
                            vec_521.append(var_474)
                            # Program VectorAppend Region
                            vec_552.append(var_474)
                            # Program TupleCompare Region
                            if self.var_0 == var_475:
                                # Program TransitionState Region
                                tuple_474 = var_474
                                prev_state = self.table_14[tuple_474]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_474] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_482: Tuple[int, int]
                                    scan_index_482: int = 0
                                    scan_tuple_482_vec: List[Tuple[int, int]] = self.index_248[var_474]
                                    while scan_index_482 < len(scan_tuple_482_vec):
                                        scan_tuple_482 = scan_tuple_482_vec[scan_index_482]
                                        scan_index_482 += 1
                                        vec_482.append(scan_tuple_482)
                                    # Program VectorLoop Region
                                    vec_index482 = 0
                                    while vec_index482 < len(vec_482):
                                        var_483, var_484 = vec_482[vec_index482]
                                        vec_index482 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_484 = self._resolve_edgetype(var_484)
                                        tuple_474_483_484 = (var_474, var_483, var_484)
                                        prev_state = self.table_26[tuple_474_483_484]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_474_483_484] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_474, var_483, var_484)

                                    # Program TransitionState Region
                                    tuple_474_474 = (var_474, var_474)
                                    prev_state = self.table_6[tuple_474_474]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_474_474] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_474_474[1]].append(tuple_474_474[0])
                                            self.index_949[tuple_474_474[0]].append(tuple_474_474[1])
                                        # Program VectorAppend Region
                                        vec_435.append((var_474, var_474))
                                    # Program VectorAppend Region
                                    vec_552.append(var_474)
                            # Program TupleCompare Region
                            if self.var_2 == var_475:
                                # Program TransitionState Region
                                tuple_2_478_474 = (self.var_2, var_478, var_474)
                                prev_state = self.table_56[tuple_2_478_474]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_478_474] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_2_478_474[1]].append((tuple_2_478_474[0], tuple_2_478_474[2]))
                                    # Program VectorAppend Region
                                    vec_531.append(var_478)
        # Program VectorClear Region
        del vec_472[:]
        vec_index472 = 0
        # Program VectorUnique Region
        vec_486 = list(set(vec_486))
        vec_index486 = 0
        # Program TableJoin Region
        while vec_index486 < len(vec_486):
            var_488 = vec_486[vec_index486]
            vec_index486 += 1
            if var_488 in self.index_307:
                if var_488 in self.index_228:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_488 = var_488
                    prev_state = self.table_14[tuple_488]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_14[tuple_488] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_489: Tuple[int, int]
                        scan_index_489: int = 0
                        scan_tuple_489_vec: List[Tuple[int, int]] = self.index_248[var_488]
                        while scan_index_489 < len(scan_tuple_489_vec):
                            scan_tuple_489 = scan_tuple_489_vec[scan_index_489]
                            scan_index_489 += 1
                            vec_489.append(scan_tuple_489)
                        # Program VectorLoop Region
                        vec_index489 = 0
                        while vec_index489 < len(vec_489):
                            var_490, var_491 = vec_489[vec_index489]
                            vec_index489 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_491 = self._resolve_edgetype(var_491)
                            tuple_488_490_491 = (var_488, var_490, var_491)
                            prev_state = self.table_26[tuple_488_490_491]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_488_490_491] = 0 | 4
                                # Program Call Region
                                ret = self.proc_252_(var_488, var_490, var_491)

                        # Program TransitionState Region
                        tuple_488_488 = (var_488, var_488)
                        prev_state = self.table_6[tuple_488_488]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_488_488] = 1 | 4
                            if not present_bit:
                                self.index_387[tuple_488_488[1]].append(tuple_488_488[0])
                                self.index_949[tuple_488_488[0]].append(tuple_488_488[1])
                            # Program VectorAppend Region
                            vec_435.append((var_488, var_488))
                        # Program VectorAppend Region
                        vec_552.append(var_488)
        # Program VectorClear Region
        del vec_486[:]
        vec_index486 = 0
        # Program VectorUnique Region
        vec_493 = list(set(vec_493))
        vec_index493 = 0
        # Program TableJoin Region
        while vec_index493 < len(vec_493):
            var_495 = vec_493[vec_index493]
            vec_index493 += 1
            if var_495 in self.index_228:
                tuple_494_1_index: int = 0
                tuple_494_1_vec: List[Tuple[int, int, int, int]] = self.index_315[var_495]
                while tuple_494_1_index < len(tuple_494_1_vec):
                    tuple_494_1 = tuple_494_1_vec[tuple_494_1_index]
                    tuple_494_1_index += 1
                    var_496 = tuple_494_1[0]
                    var_497 = tuple_494_1[1]
                    var_498 = tuple_494_1[2]
                    var_499 = tuple_494_1[3]
                    # Program TupleCompare Region
                    if (self.var_3, self.var_0, ) == (var_497, var_498, ):
                        # Program TransitionState Region
                        tuple_499_495_3 = (var_499, var_495, self.var_3)
                        prev_state = self.table_43[tuple_499_495_3]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_499_495_3] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_499_495_3[1]].append((tuple_499_495_3[0], tuple_499_495_3[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_495_499_3 = (var_495, var_499, self.var_3)
                            prev_state = self.table_26[tuple_495_499_3]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_495_499_3] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_495_499_3[0]].append((tuple_495_499_3[1], tuple_495_499_3[2]))
                                    self.index_974[(tuple_495_499_3[0], tuple_495_499_3[1])].append(tuple_495_499_3[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_495)
                            if not ret:
                                # Program TransitionState Region
                                tuple_495_499_3 = (var_495, var_499, self.var_3)
                                prev_state = self.table_26[tuple_495_499_3]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_495_499_3] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_495_499_3[0]].append((tuple_495_499_3[1], tuple_495_499_3[2]))
                                        self.index_974[(tuple_495_499_3[0], tuple_495_499_3[1])].append(tuple_495_499_3[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_499, var_495)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_499_495 = (var_499, var_495)
                                        prev_state = self.table_9[tuple_499_495]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_499_495] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_499_495[0]].append(tuple_499_495[1])
                                                self.index_1000[tuple_499_495[1]].append(tuple_499_495[0])
                                            # Program VectorAppend Region
                                            vec_557.append(var_499)
                            # Program VectorAppend Region
                            vec_521.append(var_495)
                            # Program VectorAppend Region
                            vec_552.append(var_495)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_3:
                                # Program TransitionState Region
                                tuple_495 = var_495
                                prev_state = self.table_14[tuple_495]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_495] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_503: Tuple[int, int]
                                    scan_index_503: int = 0
                                    scan_tuple_503_vec: List[Tuple[int, int]] = self.index_248[var_495]
                                    while scan_index_503 < len(scan_tuple_503_vec):
                                        scan_tuple_503 = scan_tuple_503_vec[scan_index_503]
                                        scan_index_503 += 1
                                        vec_503.append(scan_tuple_503)
                                    # Program VectorLoop Region
                                    vec_index503 = 0
                                    while vec_index503 < len(vec_503):
                                        var_504, var_505 = vec_503[vec_index503]
                                        vec_index503 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_505 = self._resolve_edgetype(var_505)
                                        tuple_495_504_505 = (var_495, var_504, var_505)
                                        prev_state = self.table_26[tuple_495_504_505]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_495_504_505] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_495, var_504, var_505)

                                    # Program TransitionState Region
                                    tuple_495_495 = (var_495, var_495)
                                    prev_state = self.table_6[tuple_495_495]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_495_495] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_495_495[1]].append(tuple_495_495[0])
                                            self.index_949[tuple_495_495[0]].append(tuple_495_495[1])
                                        # Program VectorAppend Region
                                        vec_435.append((var_495, var_495))
                                    # Program VectorAppend Region
                                    vec_552.append(var_495)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_3:
                                # Program TransitionState Region
                                tuple_2_499_495 = (self.var_2, var_499, var_495)
                                prev_state = self.table_56[tuple_2_499_495]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_499_495] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_2_499_495[1]].append((tuple_2_499_495[0], tuple_2_499_495[2]))
                                    # Program VectorAppend Region
                                    vec_531.append(var_499)
        # Program VectorClear Region
        del vec_493[:]
        vec_index493 = 0
        # Program VectorUnique Region
        vec_507 = list(set(vec_507))
        vec_index507 = 0
        # Program TableJoin Region
        while vec_index507 < len(vec_507):
            var_509 = vec_507[vec_index507]
            vec_index507 += 1
            if var_509 in self.index_228:
                tuple_508_1_index: int = 0
                tuple_508_1_vec: List[Tuple[int, int, int, int]] = self.index_330[var_509]
                while tuple_508_1_index < len(tuple_508_1_vec):
                    tuple_508_1 = tuple_508_1_vec[tuple_508_1_index]
                    tuple_508_1_index += 1
                    var_510 = tuple_508_1[0]
                    var_511 = tuple_508_1[1]
                    var_512 = tuple_508_1[2]
                    var_513 = tuple_508_1[3]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_512, var_511, ):
                        # Program TransitionState Region
                        tuple_513_509_0 = (var_513, var_509, self.var_0)
                        prev_state = self.table_43[tuple_513_509_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_513_509_0] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_513_509_0[1]].append((tuple_513_509_0[0], tuple_513_509_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_509_513_0 = (var_509, var_513, self.var_0)
                            prev_state = self.table_26[tuple_509_513_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_509_513_0] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_509_513_0[0]].append((tuple_509_513_0[1], tuple_509_513_0[2]))
                                    self.index_974[(tuple_509_513_0[0], tuple_509_513_0[1])].append(tuple_509_513_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_509)
                            if not ret:
                                # Program TransitionState Region
                                tuple_509_513_0 = (var_509, var_513, self.var_0)
                                prev_state = self.table_26[tuple_509_513_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_509_513_0] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_509_513_0[0]].append((tuple_509_513_0[1], tuple_509_513_0[2]))
                                        self.index_974[(tuple_509_513_0[0], tuple_509_513_0[1])].append(tuple_509_513_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_513, var_509)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_513_509 = (var_513, var_509)
                                        prev_state = self.table_9[tuple_513_509]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_513_509] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_513_509[0]].append(tuple_513_509[1])
                                                self.index_1000[tuple_513_509[1]].append(tuple_513_509[0])
                                            # Program VectorAppend Region
                                            vec_557.append(var_513)
                            # Program VectorAppend Region
                            vec_521.append(var_509)
                            # Program VectorAppend Region
                            vec_552.append(var_509)
                            # Program TransitionState Region
                            tuple_509 = var_509
                            prev_state = self.table_14[tuple_509]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_14[tuple_509] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_517: Tuple[int, int]
                                scan_index_517: int = 0
                                scan_tuple_517_vec: List[Tuple[int, int]] = self.index_248[var_509]
                                while scan_index_517 < len(scan_tuple_517_vec):
                                    scan_tuple_517 = scan_tuple_517_vec[scan_index_517]
                                    scan_index_517 += 1
                                    vec_517.append(scan_tuple_517)
                                # Program VectorLoop Region
                                vec_index517 = 0
                                while vec_index517 < len(vec_517):
                                    var_518, var_519 = vec_517[vec_index517]
                                    vec_index517 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_519 = self._resolve_edgetype(var_519)
                                    tuple_509_518_519 = (var_509, var_518, var_519)
                                    prev_state = self.table_26[tuple_509_518_519]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_509_518_519] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_252_(var_509, var_518, var_519)

                                # Program TransitionState Region
                                tuple_509_509 = (var_509, var_509)
                                prev_state = self.table_6[tuple_509_509]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_509_509] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_509_509[1]].append(tuple_509_509[0])
                                        self.index_949[tuple_509_509[0]].append(tuple_509_509[1])
                                    # Program VectorAppend Region
                                    vec_435.append((var_509, var_509))
                                # Program VectorAppend Region
                                vec_552.append(var_509)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_513_509 = (self.var_0, var_513, var_509)
                                prev_state = self.table_56[tuple_0_513_509]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_513_509] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_0_513_509[1]].append((tuple_0_513_509[0], tuple_0_513_509[2]))
                                    # Program VectorAppend Region
                                    vec_531.append(var_513)
        # Program VectorClear Region
        del vec_507[:]
        vec_index507 = 0
        # Program VectorUnique Region
        vec_521 = list(set(vec_521))
        vec_index521 = 0
        # Program TableJoin Region
        while vec_index521 < len(vec_521):
            var_523 = vec_521[vec_index521]
            vec_index521 += 1
            tuple_522_0_index: int = 0
            tuple_522_0_vec: List[bytes] = self.index_345[var_523]
            while tuple_522_0_index < len(tuple_522_0_vec):
                tuple_522_0 = tuple_522_0_vec[tuple_522_0_index]
                tuple_522_0_index += 1
                var_524 = tuple_522_0
                tuple_522_1_index: int = 0
                tuple_522_1_vec: List[Tuple[int, int]] = self.index_346[var_523]
                while tuple_522_1_index < len(tuple_522_1_vec):
                    tuple_522_1 = tuple_522_1_vec[tuple_522_1_index]
                    tuple_522_1_index += 1
                    var_525 = tuple_522_1[0]
                    var_526 = tuple_522_1[1]
                    # Program TransitionState Region
                    tuple_523 = var_523
                    prev_state = self.table_14[tuple_523]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_14[tuple_523] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_527: Tuple[int, int]
                        scan_index_527: int = 0
                        scan_tuple_527_vec: List[Tuple[int, int]] = self.index_248[var_523]
                        while scan_index_527 < len(scan_tuple_527_vec):
                            scan_tuple_527 = scan_tuple_527_vec[scan_index_527]
                            scan_index_527 += 1
                            vec_527.append(scan_tuple_527)
                        # Program VectorLoop Region
                        vec_index527 = 0
                        while vec_index527 < len(vec_527):
                            var_528, var_529 = vec_527[vec_index527]
                            vec_index527 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_529 = self._resolve_edgetype(var_529)
                            tuple_523_528_529 = (var_523, var_528, var_529)
                            prev_state = self.table_26[tuple_523_528_529]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_523_528_529] = 0 | 4
                                # Program Call Region
                                ret = self.proc_252_(var_523, var_528, var_529)

                        # Program TransitionState Region
                        tuple_523_523 = (var_523, var_523)
                        prev_state = self.table_6[tuple_523_523]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_523_523] = 1 | 4
                            if not present_bit:
                                self.index_387[tuple_523_523[1]].append(tuple_523_523[0])
                                self.index_949[tuple_523_523[0]].append(tuple_523_523[1])
                            # Program VectorAppend Region
                            vec_435.append((var_523, var_523))
                        # Program VectorAppend Region
                        vec_552.append(var_523)
        # Program VectorClear Region
        del vec_521[:]
        vec_index521 = 0
        # Program VectorUnique Region
        vec_531 = list(set(vec_531))
        vec_index531 = 0
        # Program TableJoin Region
        while vec_index531 < len(vec_531):
            var_533 = vec_531[vec_index531]
            vec_index531 += 1
            tuple_532_0_index: int = 0
            tuple_532_0_vec: List[Tuple[int, bytes, bytes]] = self.index_357[var_533]
            while tuple_532_0_index < len(tuple_532_0_vec):
                tuple_532_0 = tuple_532_0_vec[tuple_532_0_index]
                tuple_532_0_index += 1
                var_534 = tuple_532_0[0]
                var_535 = tuple_532_0[1]
                var_536 = tuple_532_0[2]
                tuple_532_1_index: int = 0
                tuple_532_1_vec: List[Tuple[int, int]] = self.index_358[var_533]
                while tuple_532_1_index < len(tuple_532_1_vec):
                    tuple_532_1 = tuple_532_1_vec[tuple_532_1_index]
                    tuple_532_1_index += 1
                    var_537 = tuple_532_1[0]
                    var_538 = tuple_532_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_534, var_537, ):
                        # Program TransitionState Region
                        tuple_2_1_533_535_536_538 = (self.var_2, self.var_1, var_533, var_535, var_536, var_538)
                        prev_state = self.table_60[tuple_2_1_533_535_536_538]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_533_535_536_538] = 1 | 4
                            if not present_bit:
                                self.index_367[tuple_2_1_533_535_536_538[5]].append((tuple_2_1_533_535_536_538[0], tuple_2_1_533_535_536_538[1], tuple_2_1_533_535_536_538[2], tuple_2_1_533_535_536_538[3], tuple_2_1_533_535_536_538[4]))
                            # Program VectorAppend Region
                            vec_539.append(var_538)
        # Program VectorClear Region
        del vec_531[:]
        vec_index531 = 0
        # Program VectorUnique Region
        vec_539 = list(set(vec_539))
        vec_index539 = 0
        # Program TableJoin Region
        while vec_index539 < len(vec_539):
            var_541 = vec_539[vec_index539]
            vec_index539 += 1
            tuple_540_0_index: int = 0
            tuple_540_0_vec: List[bytes] = self.index_345[var_541]
            while tuple_540_0_index < len(tuple_540_0_vec):
                tuple_540_0 = tuple_540_0_vec[tuple_540_0_index]
                tuple_540_0_index += 1
                var_542 = tuple_540_0
                tuple_540_1_index: int = 0
                tuple_540_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_367[var_541]
                while tuple_540_1_index < len(tuple_540_1_vec):
                    tuple_540_1 = tuple_540_1_vec[tuple_540_1_index]
                    tuple_540_1_index += 1
                    var_543 = tuple_540_1[0]
                    var_544 = tuple_540_1[1]
                    var_545 = tuple_540_1[2]
                    var_546 = tuple_540_1[3]
                    var_547 = tuple_540_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_544, var_543, ):
                        # Program TransitionState Region
                        tuple_545 = var_545
                        prev_state = self.table_14[tuple_545]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_14[tuple_545] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_548: Tuple[int, int]
                            scan_index_548: int = 0
                            scan_tuple_548_vec: List[Tuple[int, int]] = self.index_248[var_545]
                            while scan_index_548 < len(scan_tuple_548_vec):
                                scan_tuple_548 = scan_tuple_548_vec[scan_index_548]
                                scan_index_548 += 1
                                vec_548.append(scan_tuple_548)
                            # Program VectorLoop Region
                            vec_index548 = 0
                            while vec_index548 < len(vec_548):
                                var_549, var_550 = vec_548[vec_index548]
                                vec_index548 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_550 = self._resolve_edgetype(var_550)
                                tuple_545_549_550 = (var_545, var_549, var_550)
                                prev_state = self.table_26[tuple_545_549_550]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_545_549_550] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_252_(var_545, var_549, var_550)

                            # Program TransitionState Region
                            tuple_545_545 = (var_545, var_545)
                            prev_state = self.table_6[tuple_545_545]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_545_545] = 1 | 4
                                if not present_bit:
                                    self.index_387[tuple_545_545[1]].append(tuple_545_545[0])
                                    self.index_949[tuple_545_545[0]].append(tuple_545_545[1])
                                # Program VectorAppend Region
                                vec_435.append((var_545, var_545))
                            # Program VectorAppend Region
                            vec_552.append(var_545)
        # Program VectorClear Region
        del vec_539[:]
        vec_index539 = 0
        # Program VectorUnique Region
        vec_552 = list(set(vec_552))
        vec_index552 = 0
        # Program TableJoin Region
        while vec_index552 < len(vec_552):
            var_554 = vec_552[vec_index552]
            vec_index552 += 1
            tuple_553_0_index: int = 0
            tuple_553_0_vec: List[Tuple[int, int]] = self.index_346[var_554]
            while tuple_553_0_index < len(tuple_553_0_vec):
                tuple_553_0 = tuple_553_0_vec[tuple_553_0_index]
                tuple_553_0_index += 1
                var_555 = tuple_553_0[0]
                var_556 = tuple_553_0[1]
                if var_554 in self.index_381:
                    # Program TransitionState Region
                    tuple_555_554 = (var_555, var_554)
                    prev_state = self.table_16[tuple_555_554]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_16[tuple_555_554] = 1 | 4
                        if not present_bit:
                            self.index_406[tuple_555_554[1]].append(tuple_555_554[0])
                            self.index_956[tuple_555_554[0]].append(tuple_555_554[1])
                        # Program VectorAppend Region
                        vec_565.append(var_554)
        # Program VectorClear Region
        del vec_552[:]
        vec_index552 = 0
        # Program VectorUnique Region
        vec_557 = list(set(vec_557))
        vec_index557 = 0
        # Program TableJoin Region
        while vec_index557 < len(vec_557):
            var_559 = vec_557[vec_index557]
            vec_index557 += 1
            tuple_558_0_index: int = 0
            tuple_558_0_vec: List[int] = self.index_387[var_559]
            while tuple_558_0_index < len(tuple_558_0_vec):
                tuple_558_0 = tuple_558_0_vec[tuple_558_0_index]
                tuple_558_0_index += 1
                var_560 = tuple_558_0
                tuple_558_1_index: int = 0
                tuple_558_1_vec: List[int] = self.index_388[var_559]
                while tuple_558_1_index < len(tuple_558_1_vec):
                    tuple_558_1 = tuple_558_1_vec[tuple_558_1_index]
                    tuple_558_1_index += 1
                    var_561 = tuple_558_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_950_(var_560, var_559)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_953_(var_559, var_561)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_399_(var_560, var_561)
                            if not ret:
                                # Program TransitionState Region
                                tuple_560_561 = (var_560, var_561)
                                prev_state = self.table_6[tuple_560_561]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_560_561] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_560_561[1]].append(tuple_560_561[0])
                                        self.index_949[tuple_560_561[0]].append(tuple_560_561[1])
                                    # Program VectorAppend Region
                                    vec_435.append((var_560, var_561))
        # Program VectorClear Region
        del vec_557[:]
        vec_index557 = 0
        # Program VectorUnique Region
        vec_565 = list(set(vec_565))
        vec_index565 = 0
        # Program TableJoin Region
        while vec_index565 < len(vec_565):
            var_567 = vec_565[vec_index565]
            vec_index565 += 1
            tuple_566_0_index: int = 0
            tuple_566_0_vec: List[int] = self.index_406[var_567]
            while tuple_566_0_index < len(tuple_566_0_vec):
                tuple_566_0 = tuple_566_0_vec[tuple_566_0_index]
                tuple_566_0_index += 1
                var_568 = tuple_566_0
                tuple_566_1_index: int = 0
                tuple_566_1_vec: List[bytes] = self.index_345[var_567]
                while tuple_566_1_index < len(tuple_566_1_vec):
                    tuple_566_1 = tuple_566_1_vec[tuple_566_1_index]
                    tuple_566_1_index += 1
                    var_569 = tuple_566_1
                    # Program TransitionState Region
                    tuple_568 = var_568
                    prev_state = self.table_12[tuple_568]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_568] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_565[:]
        vec_index565 = 0
        # Induction Fixpoint Loop Region
        while len(vec_435):
            # Program Call Region
            param_437_0 = [vec_435]
            ret = self.proc_241_(param_437_0)
            vec_435 = param_437_0[0]

        vec_index435 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_435[:]
        vec_index435 = 0
        # Program Return Region
        return False

    def entrypoint_1(self, vec_571: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index571: int = 0
        vec_573: List[int] = list()
        vec_index573: int = 0
        vec_576: List[Tuple[int, int]] = list()
        vec_index576: int = 0
        vec_579: List[Tuple[int, int]] = list()
        vec_index579: int = 0
        vec_583: List[int] = list()
        vec_index583: int = 0
        vec_588: List[int] = list()
        vec_index588: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index571 = 0
        while vec_index571 < len(vec_571):
            var_572 = vec_571[vec_index571]
            vec_index571 += 1
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_572 = var_572
            prev_state = self.table_47[tuple_572]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_47[tuple_572] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_573.append(var_572)
        # Program VectorUnique Region
        vec_573 = list(set(vec_573))
        vec_index573 = 0
        # Program TableJoin Region
        while vec_index573 < len(vec_573):
            var_575 = vec_573[vec_index573]
            vec_index573 += 1
            if var_575 in self.index_307:
                if var_575 in self.index_228:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_575 = var_575
                    prev_state = self.table_14[tuple_575]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_14[tuple_575] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_579: Tuple[int, int]
                        scan_index_579: int = 0
                        scan_tuple_579_vec: List[Tuple[int, int]] = self.index_248[var_575]
                        while scan_index_579 < len(scan_tuple_579_vec):
                            scan_tuple_579 = scan_tuple_579_vec[scan_index_579]
                            scan_index_579 += 1
                            vec_579.append(scan_tuple_579)
                        # Program VectorLoop Region
                        vec_index579 = 0
                        while vec_index579 < len(vec_579):
                            var_580, var_581 = vec_579[vec_index579]
                            vec_index579 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_581 = self._resolve_edgetype(var_581)
                            tuple_575_580_581 = (var_575, var_580, var_581)
                            prev_state = self.table_26[tuple_575_580_581]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_575_580_581] = 0 | 4
                                # Program Call Region
                                ret = self.proc_252_(var_575, var_580, var_581)

                        # Program TransitionState Region
                        tuple_575_575 = (var_575, var_575)
                        prev_state = self.table_6[tuple_575_575]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_575_575] = 1 | 4
                            if not present_bit:
                                self.index_387[tuple_575_575[1]].append(tuple_575_575[0])
                                self.index_949[tuple_575_575[0]].append(tuple_575_575[1])
                            # Program VectorAppend Region
                            vec_576.append((var_575, var_575))
                        # Program VectorAppend Region
                        vec_583.append(var_575)
        # Program VectorClear Region
        del vec_573[:]
        vec_index573 = 0
        # Program VectorUnique Region
        vec_583 = list(set(vec_583))
        vec_index583 = 0
        # Program TableJoin Region
        while vec_index583 < len(vec_583):
            var_585 = vec_583[vec_index583]
            vec_index583 += 1
            tuple_584_0_index: int = 0
            tuple_584_0_vec: List[Tuple[int, int]] = self.index_346[var_585]
            while tuple_584_0_index < len(tuple_584_0_vec):
                tuple_584_0 = tuple_584_0_vec[tuple_584_0_index]
                tuple_584_0_index += 1
                var_586 = tuple_584_0[0]
                var_587 = tuple_584_0[1]
                if var_585 in self.index_381:
                    # Program TransitionState Region
                    tuple_586_585 = (var_586, var_585)
                    prev_state = self.table_16[tuple_586_585]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_16[tuple_586_585] = 1 | 4
                        if not present_bit:
                            self.index_406[tuple_586_585[1]].append(tuple_586_585[0])
                            self.index_956[tuple_586_585[0]].append(tuple_586_585[1])
                        # Program VectorAppend Region
                        vec_588.append(var_585)
        # Program VectorClear Region
        del vec_583[:]
        vec_index583 = 0
        # Program VectorUnique Region
        vec_588 = list(set(vec_588))
        vec_index588 = 0
        # Program TableJoin Region
        while vec_index588 < len(vec_588):
            var_590 = vec_588[vec_index588]
            vec_index588 += 1
            tuple_589_0_index: int = 0
            tuple_589_0_vec: List[int] = self.index_406[var_590]
            while tuple_589_0_index < len(tuple_589_0_vec):
                tuple_589_0 = tuple_589_0_vec[tuple_589_0_index]
                tuple_589_0_index += 1
                var_591 = tuple_589_0
                tuple_589_1_index: int = 0
                tuple_589_1_vec: List[bytes] = self.index_345[var_590]
                while tuple_589_1_index < len(tuple_589_1_vec):
                    tuple_589_1 = tuple_589_1_vec[tuple_589_1_index]
                    tuple_589_1_index += 1
                    var_592 = tuple_589_1
                    # Program TransitionState Region
                    tuple_591 = var_591
                    prev_state = self.table_12[tuple_591]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_591] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_588[:]
        vec_index588 = 0
        # Induction Fixpoint Loop Region
        while len(vec_576):
            # Program Call Region
            param_578_0 = [vec_576]
            ret = self.proc_241_(param_578_0)
            vec_576 = param_578_0[0]

        vec_index576 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_576[:]
        vec_index576 = 0
        # Program Return Region
        return False

    def raw_transfer_3(self, vec_594: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index594: int = 0
        vec_598: List[Tuple[int, int]] = list()
        vec_index598: int = 0
        vec_606: List[int] = list()
        vec_index606: int = 0
        vec_615: List[int] = list()
        vec_index615: int = 0
        vec_624: List[int] = list()
        vec_index624: int = 0
        vec_633: List[Tuple[int, int]] = list()
        vec_index633: int = 0
        vec_636: List[Tuple[int, int]] = list()
        vec_index636: int = 0
        vec_640: List[int] = list()
        vec_index640: int = 0
        vec_650: List[Tuple[int, int]] = list()
        vec_index650: int = 0
        vec_654: List[int] = list()
        vec_index654: int = 0
        vec_664: List[Tuple[int, int]] = list()
        vec_index664: int = 0
        vec_668: List[int] = list()
        vec_index668: int = 0
        vec_678: List[Tuple[int, int]] = list()
        vec_index678: int = 0
        vec_682: List[int] = list()
        vec_index682: int = 0
        vec_688: List[Tuple[int, int]] = list()
        vec_index688: int = 0
        vec_692: List[int] = list()
        vec_index692: int = 0
        vec_700: List[int] = list()
        vec_index700: int = 0
        vec_709: List[Tuple[int, int]] = list()
        vec_index709: int = 0
        vec_713: List[int] = list()
        vec_index713: int = 0
        vec_718: List[int] = list()
        vec_index718: int = 0
        vec_726: List[int] = list()
        vec_index726: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index594 = 0
        while vec_index594 < len(vec_594):
            var_595, var_596, var_597 = vec_594[vec_index594]
            vec_index594 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if var_597 != self.var_0:
                # Program TupleCompare Region
                if var_597 != self.var_3:
                    # Program TransitionState Region
                    var_597 = self._resolve_edgetype(var_597)
                    tuple_597_3_0_595_596 = (var_597, self.var_3, self.var_0, var_595, var_596)
                    prev_state = self.table_67[tuple_597_3_0_595_596]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_67[tuple_597_3_0_595_596] = 1 | 4
                        if not present_bit:
                            self.index_292[tuple_597_3_0_595_596[4]].append((tuple_597_3_0_595_596[0], tuple_597_3_0_595_596[1], tuple_597_3_0_595_596[2], tuple_597_3_0_595_596[3]))
                        # Program VectorAppend Region
                        vec_640.append(var_596)
            # Program TupleCompare Region
            if self.var_0 == var_597:
                # Program TransitionState Region
                tuple_0_595_596 = (self.var_0, var_595, var_596)
                prev_state = self.table_73[tuple_0_595_596]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_0_595_596] = 1 | 4
                    if not present_bit:
                        self.index_618[tuple_0_595_596[1]].append((tuple_0_595_596[0], tuple_0_595_596[2]))
                    # Program VectorAppend Region
                    vec_615.append(var_595)
            # Program TupleCompare Region
            if self.var_3 == var_597:
                # Program TransitionState Region
                tuple_3_595_596 = (self.var_3, var_595, var_596)
                prev_state = self.table_77[tuple_3_595_596]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_77[tuple_3_595_596] = 1 | 4
                    if not present_bit:
                        self.index_619[tuple_3_595_596[1]].append((tuple_3_595_596[0], tuple_3_595_596[2]))
                    # Program VectorAppend Region
                    vec_615.append(var_595)
            # Program TupleCompare Region
            if self.var_0 == var_597:
                # Program TransitionState Region
                tuple_0_595_596 = (self.var_0, var_595, var_596)
                prev_state = self.table_87[tuple_0_595_596]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_87[tuple_0_595_596] = 1 | 4
                    if not present_bit:
                        self.index_609[tuple_0_595_596[1]].append((tuple_0_595_596[0], tuple_0_595_596[2]))
                    # Program VectorAppend Region
                    vec_606.append(var_595)
            # Program TupleCompare Region
            if self.var_3 == var_597:
                # Program TransitionState Region
                tuple_3_595_596 = (self.var_3, var_595, var_596)
                prev_state = self.table_91[tuple_3_595_596]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_91[tuple_3_595_596] = 1 | 4
                    if not present_bit:
                        self.index_610[tuple_3_595_596[1]].append((tuple_3_595_596[0], tuple_3_595_596[2]))
                    # Program VectorAppend Region
                    vec_606.append(var_595)
            # Program TupleCompare Region
            if self.var_0 == var_597:
                # Program TransitionState Region
                tuple_0_595_596 = (self.var_0, var_595, var_596)
                prev_state = self.table_143[tuple_0_595_596]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_143[tuple_0_595_596] = 1 | 4
                    if not present_bit:
                        self.index_602[(tuple_0_595_596[1], tuple_0_595_596[2])].append(tuple_0_595_596[0])
                    # Program VectorAppend Region
                    vec_598.append((var_595, var_596))
            # Program TupleCompare Region
            if self.var_3 == var_597:
                # Program TransitionState Region
                tuple_3_595_596 = (self.var_3, var_595, var_596)
                prev_state = self.table_147[tuple_3_595_596]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_147[tuple_3_595_596] = 1 | 4
                    if not present_bit:
                        self.index_603[(tuple_3_595_596[1], tuple_3_595_596[2])].append(tuple_3_595_596[0])
                    # Program VectorAppend Region
                    vec_598.append((var_595, var_596))
        # Program VectorUnique Region
        vec_598 = list(set(vec_598))
        vec_index598 = 0
        # Program TableJoin Region
        while vec_index598 < len(vec_598):
            var_600, var_601 = vec_598[vec_index598]
            vec_index598 += 1
            tuple_599_0_index: int = 0
            tuple_599_0_vec: List[int] = self.index_602[(var_600, var_601)]
            while tuple_599_0_index < len(tuple_599_0_vec):
                tuple_599_0 = tuple_599_0_vec[tuple_599_0_index]
                tuple_599_0_index += 1
                var_604 = tuple_599_0
                tuple_599_1_index: int = 0
                tuple_599_1_vec: List[int] = self.index_603[(var_600, var_601)]
                while tuple_599_1_index < len(tuple_599_1_vec):
                    tuple_599_1 = tuple_599_1_vec[tuple_599_1_index]
                    tuple_599_1_index += 1
                    var_605 = tuple_599_1
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_604, var_605, ):
                        # Program TransitionState Region
                        tuple_3_0_600_601 = (self.var_3, self.var_0, var_600, var_601)
                        prev_state = self.table_151[tuple_3_0_600_601]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_151[tuple_3_0_600_601] = 1 | 4
                            if not present_bit:
                                self.index_229[tuple_3_0_600_601[3]].append((tuple_3_0_600_601[0], tuple_3_0_600_601[1], tuple_3_0_600_601[2]))
                            # Program VectorAppend Region
                            vec_624.append(var_601)
        # Program VectorClear Region
        del vec_598[:]
        vec_index598 = 0
        # Program VectorUnique Region
        vec_606 = list(set(vec_606))
        vec_index606 = 0
        # Program TableJoin Region
        while vec_index606 < len(vec_606):
            var_608 = vec_606[vec_index606]
            vec_index606 += 1
            tuple_607_0_index: int = 0
            tuple_607_0_vec: List[Tuple[int, int]] = self.index_609[var_608]
            while tuple_607_0_index < len(tuple_607_0_vec):
                tuple_607_0 = tuple_607_0_vec[tuple_607_0_index]
                tuple_607_0_index += 1
                var_611 = tuple_607_0[0]
                var_612 = tuple_607_0[1]
                tuple_607_1_index: int = 0
                tuple_607_1_vec: List[Tuple[int, int]] = self.index_610[var_608]
                while tuple_607_1_index < len(tuple_607_1_vec):
                    tuple_607_1 = tuple_607_1_vec[tuple_607_1_index]
                    tuple_607_1_index += 1
                    var_613 = tuple_607_1[0]
                    var_614 = tuple_607_1[1]
                    # Program TupleCompare Region
                    if (self.var_3, self.var_0, ) == (var_613, var_611, ):
                        # Program TupleCompare Region
                        if var_612 != var_614:
                            # Program TransitionState Region
                            tuple_612_614_3_0_608 = (var_612, var_614, self.var_3, self.var_0, var_608)
                            prev_state = self.table_95[tuple_612_614_3_0_608]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_95[tuple_612_614_3_0_608] = 1 | 4
                                if not present_bit:
                                    self.index_315[tuple_612_614_3_0_608[1]].append((tuple_612_614_3_0_608[0], tuple_612_614_3_0_608[2], tuple_612_614_3_0_608[3], tuple_612_614_3_0_608[4]))
                                # Program VectorAppend Region
                                vec_668.append(var_614)
        # Program VectorClear Region
        del vec_606[:]
        vec_index606 = 0
        # Program VectorUnique Region
        vec_615 = list(set(vec_615))
        vec_index615 = 0
        # Program TableJoin Region
        while vec_index615 < len(vec_615):
            var_617 = vec_615[vec_index615]
            vec_index615 += 1
            tuple_616_0_index: int = 0
            tuple_616_0_vec: List[Tuple[int, int]] = self.index_618[var_617]
            while tuple_616_0_index < len(tuple_616_0_vec):
                tuple_616_0 = tuple_616_0_vec[tuple_616_0_index]
                tuple_616_0_index += 1
                var_620 = tuple_616_0[0]
                var_621 = tuple_616_0[1]
                tuple_616_1_index: int = 0
                tuple_616_1_vec: List[Tuple[int, int]] = self.index_619[var_617]
                while tuple_616_1_index < len(tuple_616_1_vec):
                    tuple_616_1 = tuple_616_1_vec[tuple_616_1_index]
                    tuple_616_1_index += 1
                    var_622 = tuple_616_1[0]
                    var_623 = tuple_616_1[1]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_620, var_622, ):
                        # Program TupleCompare Region
                        if var_621 != var_623:
                            # Program TransitionState Region
                            tuple_621_623_3_0_617 = (var_621, var_623, self.var_3, self.var_0, var_617)
                            prev_state = self.table_81[tuple_621_623_3_0_617]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_81[tuple_621_623_3_0_617] = 1 | 4
                                if not present_bit:
                                    self.index_330[tuple_621_623_3_0_617[0]].append((tuple_621_623_3_0_617[1], tuple_621_623_3_0_617[2], tuple_621_623_3_0_617[3], tuple_621_623_3_0_617[4]))
                                # Program VectorAppend Region
                                vec_654.append(var_621)
        # Program VectorClear Region
        del vec_615[:]
        vec_index615 = 0
        # Program VectorUnique Region
        vec_624 = list(set(vec_624))
        vec_index624 = 0
        # Program TableJoin Region
        while vec_index624 < len(vec_624):
            var_626 = vec_624[vec_index624]
            vec_index624 += 1
            if var_626 in self.index_228:
                tuple_625_1_index: int = 0
                tuple_625_1_vec: List[Tuple[int, int, int]] = self.index_229[var_626]
                while tuple_625_1_index < len(tuple_625_1_vec):
                    tuple_625_1 = tuple_625_1_vec[tuple_625_1_index]
                    tuple_625_1_index += 1
                    var_627 = tuple_625_1[0]
                    var_628 = tuple_625_1[1]
                    var_629 = tuple_625_1[2]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_628, var_627, ):
                        # Program TransitionState Region
                        tuple_629_626_5 = (var_629, var_626, self.var_5)
                        prev_state = self.table_43[tuple_629_626_5]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_629_626_5] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_629_626_5[1]].append((tuple_629_626_5[0], tuple_629_626_5[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_626_629_5 = (var_626, var_629, self.var_5)
                            prev_state = self.table_26[tuple_626_629_5]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_626_629_5] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_626_629_5[0]].append((tuple_626_629_5[1], tuple_626_629_5[2]))
                                    self.index_974[(tuple_626_629_5[0], tuple_626_629_5[1])].append(tuple_626_629_5[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_626)
                            if not ret:
                                # Program TransitionState Region
                                tuple_626_629_5 = (var_626, var_629, self.var_5)
                                prev_state = self.table_26[tuple_626_629_5]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_626_629_5] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_626_629_5[0]].append((tuple_626_629_5[1], tuple_626_629_5[2]))
                                        self.index_974[(tuple_626_629_5[0], tuple_626_629_5[1])].append(tuple_626_629_5[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_629, var_626)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_629_626 = (var_629, var_626)
                                        prev_state = self.table_9[tuple_629_626]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_629_626] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_629_626[0]].append(tuple_629_626[1])
                                                self.index_1000[tuple_629_626[1]].append(tuple_629_626[0])
                                            # Program VectorAppend Region
                                            vec_718.append(var_629)
                            # Program VectorAppend Region
                            vec_682.append(var_626)
                            # Program VectorAppend Region
                            vec_713.append(var_626)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_5:
                                # Program TransitionState Region
                                tuple_626 = var_626
                                prev_state = self.table_14[tuple_626]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_626] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_636: Tuple[int, int]
                                    scan_index_636: int = 0
                                    scan_tuple_636_vec: List[Tuple[int, int]] = self.index_248[var_626]
                                    while scan_index_636 < len(scan_tuple_636_vec):
                                        scan_tuple_636 = scan_tuple_636_vec[scan_index_636]
                                        scan_index_636 += 1
                                        vec_636.append(scan_tuple_636)
                                    # Program VectorLoop Region
                                    vec_index636 = 0
                                    while vec_index636 < len(vec_636):
                                        var_637, var_638 = vec_636[vec_index636]
                                        vec_index636 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_638 = self._resolve_edgetype(var_638)
                                        tuple_626_637_638 = (var_626, var_637, var_638)
                                        prev_state = self.table_26[tuple_626_637_638]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_626_637_638] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_626, var_637, var_638)

                                    # Program TransitionState Region
                                    tuple_626_626 = (var_626, var_626)
                                    prev_state = self.table_6[tuple_626_626]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_626_626] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_626_626[1]].append(tuple_626_626[0])
                                            self.index_949[tuple_626_626[0]].append(tuple_626_626[1])
                                        # Program VectorAppend Region
                                        vec_633.append((var_626, var_626))
                                    # Program VectorAppend Region
                                    vec_713.append(var_626)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_5:
                                # Program TransitionState Region
                                tuple_2_629_626 = (self.var_2, var_629, var_626)
                                prev_state = self.table_56[tuple_2_629_626]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_629_626] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_2_629_626[1]].append((tuple_2_629_626[0], tuple_2_629_626[2]))
                                    # Program VectorAppend Region
                                    vec_692.append(var_629)
        # Program VectorClear Region
        del vec_624[:]
        vec_index624 = 0
        # Program VectorUnique Region
        vec_640 = list(set(vec_640))
        vec_index640 = 0
        # Program TableJoin Region
        while vec_index640 < len(vec_640):
            var_642 = vec_640[vec_index640]
            vec_index640 += 1
            tuple_641_0_index: int = 0
            tuple_641_0_vec: List[Tuple[int, int, int, int]] = self.index_292[var_642]
            while tuple_641_0_index < len(tuple_641_0_vec):
                tuple_641_0 = tuple_641_0_vec[tuple_641_0_index]
                tuple_641_0_index += 1
                var_643 = tuple_641_0[0]
                var_644 = tuple_641_0[1]
                var_645 = tuple_641_0[2]
                var_646 = tuple_641_0[3]
                if var_642 in self.index_228:
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_645, var_644, ):
                        # Program TransitionState Region
                        var_643 = self._resolve_edgetype(var_643)
                        tuple_646_642_643 = (var_646, var_642, var_643)
                        prev_state = self.table_43[tuple_646_642_643]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_646_642_643] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_646_642_643[1]].append((tuple_646_642_643[0], tuple_646_642_643[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            var_643 = self._resolve_edgetype(var_643)
                            tuple_642_646_643 = (var_642, var_646, var_643)
                            prev_state = self.table_26[tuple_642_646_643]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_642_646_643] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_642_646_643[0]].append((tuple_642_646_643[1], tuple_642_646_643[2]))
                                    self.index_974[(tuple_642_646_643[0], tuple_642_646_643[1])].append(tuple_642_646_643[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_642)
                            if not ret:
                                # Program TransitionState Region
                                var_643 = self._resolve_edgetype(var_643)
                                tuple_642_646_643 = (var_642, var_646, var_643)
                                prev_state = self.table_26[tuple_642_646_643]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_642_646_643] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_642_646_643[0]].append((tuple_642_646_643[1], tuple_642_646_643[2]))
                                        self.index_974[(tuple_642_646_643[0], tuple_642_646_643[1])].append(tuple_642_646_643[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_646, var_642)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_646_642 = (var_646, var_642)
                                        prev_state = self.table_9[tuple_646_642]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_646_642] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_646_642[0]].append(tuple_646_642[1])
                                                self.index_1000[tuple_646_642[1]].append(tuple_646_642[0])
                                            # Program VectorAppend Region
                                            vec_718.append(var_646)
                            # Program VectorAppend Region
                            vec_682.append(var_642)
                            # Program VectorAppend Region
                            vec_713.append(var_642)
                            # Program TupleCompare Region
                            if self.var_0 == var_643:
                                # Program TransitionState Region
                                tuple_642 = var_642
                                prev_state = self.table_14[tuple_642]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_642] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_650: Tuple[int, int]
                                    scan_index_650: int = 0
                                    scan_tuple_650_vec: List[Tuple[int, int]] = self.index_248[var_642]
                                    while scan_index_650 < len(scan_tuple_650_vec):
                                        scan_tuple_650 = scan_tuple_650_vec[scan_index_650]
                                        scan_index_650 += 1
                                        vec_650.append(scan_tuple_650)
                                    # Program VectorLoop Region
                                    vec_index650 = 0
                                    while vec_index650 < len(vec_650):
                                        var_651, var_652 = vec_650[vec_index650]
                                        vec_index650 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_652 = self._resolve_edgetype(var_652)
                                        tuple_642_651_652 = (var_642, var_651, var_652)
                                        prev_state = self.table_26[tuple_642_651_652]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_642_651_652] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_642, var_651, var_652)

                                    # Program TransitionState Region
                                    tuple_642_642 = (var_642, var_642)
                                    prev_state = self.table_6[tuple_642_642]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_642_642] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_642_642[1]].append(tuple_642_642[0])
                                            self.index_949[tuple_642_642[0]].append(tuple_642_642[1])
                                        # Program VectorAppend Region
                                        vec_633.append((var_642, var_642))
                                    # Program VectorAppend Region
                                    vec_713.append(var_642)
                            # Program TupleCompare Region
                            if self.var_2 == var_643:
                                # Program TransitionState Region
                                tuple_2_646_642 = (self.var_2, var_646, var_642)
                                prev_state = self.table_56[tuple_2_646_642]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_646_642] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_2_646_642[1]].append((tuple_2_646_642[0], tuple_2_646_642[2]))
                                    # Program VectorAppend Region
                                    vec_692.append(var_646)
        # Program VectorClear Region
        del vec_640[:]
        vec_index640 = 0
        # Program VectorUnique Region
        vec_654 = list(set(vec_654))
        vec_index654 = 0
        # Program TableJoin Region
        while vec_index654 < len(vec_654):
            var_656 = vec_654[vec_index654]
            vec_index654 += 1
            if var_656 in self.index_228:
                tuple_655_1_index: int = 0
                tuple_655_1_vec: List[Tuple[int, int, int, int]] = self.index_330[var_656]
                while tuple_655_1_index < len(tuple_655_1_vec):
                    tuple_655_1 = tuple_655_1_vec[tuple_655_1_index]
                    tuple_655_1_index += 1
                    var_657 = tuple_655_1[0]
                    var_658 = tuple_655_1[1]
                    var_659 = tuple_655_1[2]
                    var_660 = tuple_655_1[3]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_659, var_658, ):
                        # Program TransitionState Region
                        tuple_660_656_0 = (var_660, var_656, self.var_0)
                        prev_state = self.table_43[tuple_660_656_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_660_656_0] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_660_656_0[1]].append((tuple_660_656_0[0], tuple_660_656_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_656_660_0 = (var_656, var_660, self.var_0)
                            prev_state = self.table_26[tuple_656_660_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_656_660_0] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_656_660_0[0]].append((tuple_656_660_0[1], tuple_656_660_0[2]))
                                    self.index_974[(tuple_656_660_0[0], tuple_656_660_0[1])].append(tuple_656_660_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_656)
                            if not ret:
                                # Program TransitionState Region
                                tuple_656_660_0 = (var_656, var_660, self.var_0)
                                prev_state = self.table_26[tuple_656_660_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_656_660_0] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_656_660_0[0]].append((tuple_656_660_0[1], tuple_656_660_0[2]))
                                        self.index_974[(tuple_656_660_0[0], tuple_656_660_0[1])].append(tuple_656_660_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_660, var_656)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_660_656 = (var_660, var_656)
                                        prev_state = self.table_9[tuple_660_656]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_660_656] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_660_656[0]].append(tuple_660_656[1])
                                                self.index_1000[tuple_660_656[1]].append(tuple_660_656[0])
                                            # Program VectorAppend Region
                                            vec_718.append(var_660)
                            # Program VectorAppend Region
                            vec_682.append(var_656)
                            # Program VectorAppend Region
                            vec_713.append(var_656)
                            # Program TransitionState Region
                            tuple_656 = var_656
                            prev_state = self.table_14[tuple_656]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_14[tuple_656] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_664: Tuple[int, int]
                                scan_index_664: int = 0
                                scan_tuple_664_vec: List[Tuple[int, int]] = self.index_248[var_656]
                                while scan_index_664 < len(scan_tuple_664_vec):
                                    scan_tuple_664 = scan_tuple_664_vec[scan_index_664]
                                    scan_index_664 += 1
                                    vec_664.append(scan_tuple_664)
                                # Program VectorLoop Region
                                vec_index664 = 0
                                while vec_index664 < len(vec_664):
                                    var_665, var_666 = vec_664[vec_index664]
                                    vec_index664 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_666 = self._resolve_edgetype(var_666)
                                    tuple_656_665_666 = (var_656, var_665, var_666)
                                    prev_state = self.table_26[tuple_656_665_666]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_656_665_666] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_252_(var_656, var_665, var_666)

                                # Program TransitionState Region
                                tuple_656_656 = (var_656, var_656)
                                prev_state = self.table_6[tuple_656_656]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_656_656] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_656_656[1]].append(tuple_656_656[0])
                                        self.index_949[tuple_656_656[0]].append(tuple_656_656[1])
                                    # Program VectorAppend Region
                                    vec_633.append((var_656, var_656))
                                # Program VectorAppend Region
                                vec_713.append(var_656)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_660_656 = (self.var_0, var_660, var_656)
                                prev_state = self.table_56[tuple_0_660_656]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_660_656] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_0_660_656[1]].append((tuple_0_660_656[0], tuple_0_660_656[2]))
                                    # Program VectorAppend Region
                                    vec_692.append(var_660)
        # Program VectorClear Region
        del vec_654[:]
        vec_index654 = 0
        # Program VectorUnique Region
        vec_668 = list(set(vec_668))
        vec_index668 = 0
        # Program TableJoin Region
        while vec_index668 < len(vec_668):
            var_670 = vec_668[vec_index668]
            vec_index668 += 1
            if var_670 in self.index_228:
                tuple_669_1_index: int = 0
                tuple_669_1_vec: List[Tuple[int, int, int, int]] = self.index_315[var_670]
                while tuple_669_1_index < len(tuple_669_1_vec):
                    tuple_669_1 = tuple_669_1_vec[tuple_669_1_index]
                    tuple_669_1_index += 1
                    var_671 = tuple_669_1[0]
                    var_672 = tuple_669_1[1]
                    var_673 = tuple_669_1[2]
                    var_674 = tuple_669_1[3]
                    # Program TupleCompare Region
                    if (self.var_3, self.var_0, ) == (var_672, var_673, ):
                        # Program TransitionState Region
                        tuple_674_670_3 = (var_674, var_670, self.var_3)
                        prev_state = self.table_43[tuple_674_670_3]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_674_670_3] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_674_670_3[1]].append((tuple_674_670_3[0], tuple_674_670_3[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_670_674_3 = (var_670, var_674, self.var_3)
                            prev_state = self.table_26[tuple_670_674_3]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_670_674_3] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_670_674_3[0]].append((tuple_670_674_3[1], tuple_670_674_3[2]))
                                    self.index_974[(tuple_670_674_3[0], tuple_670_674_3[1])].append(tuple_670_674_3[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_670)
                            if not ret:
                                # Program TransitionState Region
                                tuple_670_674_3 = (var_670, var_674, self.var_3)
                                prev_state = self.table_26[tuple_670_674_3]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_670_674_3] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_670_674_3[0]].append((tuple_670_674_3[1], tuple_670_674_3[2]))
                                        self.index_974[(tuple_670_674_3[0], tuple_670_674_3[1])].append(tuple_670_674_3[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_674, var_670)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_674_670 = (var_674, var_670)
                                        prev_state = self.table_9[tuple_674_670]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_674_670] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_674_670[0]].append(tuple_674_670[1])
                                                self.index_1000[tuple_674_670[1]].append(tuple_674_670[0])
                                            # Program VectorAppend Region
                                            vec_718.append(var_674)
                            # Program VectorAppend Region
                            vec_682.append(var_670)
                            # Program VectorAppend Region
                            vec_713.append(var_670)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_3:
                                # Program TransitionState Region
                                tuple_670 = var_670
                                prev_state = self.table_14[tuple_670]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_670] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_678: Tuple[int, int]
                                    scan_index_678: int = 0
                                    scan_tuple_678_vec: List[Tuple[int, int]] = self.index_248[var_670]
                                    while scan_index_678 < len(scan_tuple_678_vec):
                                        scan_tuple_678 = scan_tuple_678_vec[scan_index_678]
                                        scan_index_678 += 1
                                        vec_678.append(scan_tuple_678)
                                    # Program VectorLoop Region
                                    vec_index678 = 0
                                    while vec_index678 < len(vec_678):
                                        var_679, var_680 = vec_678[vec_index678]
                                        vec_index678 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_680 = self._resolve_edgetype(var_680)
                                        tuple_670_679_680 = (var_670, var_679, var_680)
                                        prev_state = self.table_26[tuple_670_679_680]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_670_679_680] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_670, var_679, var_680)

                                    # Program TransitionState Region
                                    tuple_670_670 = (var_670, var_670)
                                    prev_state = self.table_6[tuple_670_670]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_670_670] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_670_670[1]].append(tuple_670_670[0])
                                            self.index_949[tuple_670_670[0]].append(tuple_670_670[1])
                                        # Program VectorAppend Region
                                        vec_633.append((var_670, var_670))
                                    # Program VectorAppend Region
                                    vec_713.append(var_670)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_3:
                                # Program TransitionState Region
                                tuple_2_674_670 = (self.var_2, var_674, var_670)
                                prev_state = self.table_56[tuple_2_674_670]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_674_670] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_2_674_670[1]].append((tuple_2_674_670[0], tuple_2_674_670[2]))
                                    # Program VectorAppend Region
                                    vec_692.append(var_674)
        # Program VectorClear Region
        del vec_668[:]
        vec_index668 = 0
        # Program VectorUnique Region
        vec_682 = list(set(vec_682))
        vec_index682 = 0
        # Program TableJoin Region
        while vec_index682 < len(vec_682):
            var_684 = vec_682[vec_index682]
            vec_index682 += 1
            tuple_683_0_index: int = 0
            tuple_683_0_vec: List[bytes] = self.index_345[var_684]
            while tuple_683_0_index < len(tuple_683_0_vec):
                tuple_683_0 = tuple_683_0_vec[tuple_683_0_index]
                tuple_683_0_index += 1
                var_685 = tuple_683_0
                tuple_683_1_index: int = 0
                tuple_683_1_vec: List[Tuple[int, int]] = self.index_346[var_684]
                while tuple_683_1_index < len(tuple_683_1_vec):
                    tuple_683_1 = tuple_683_1_vec[tuple_683_1_index]
                    tuple_683_1_index += 1
                    var_686 = tuple_683_1[0]
                    var_687 = tuple_683_1[1]
                    # Program TransitionState Region
                    tuple_684 = var_684
                    prev_state = self.table_14[tuple_684]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_14[tuple_684] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_688: Tuple[int, int]
                        scan_index_688: int = 0
                        scan_tuple_688_vec: List[Tuple[int, int]] = self.index_248[var_684]
                        while scan_index_688 < len(scan_tuple_688_vec):
                            scan_tuple_688 = scan_tuple_688_vec[scan_index_688]
                            scan_index_688 += 1
                            vec_688.append(scan_tuple_688)
                        # Program VectorLoop Region
                        vec_index688 = 0
                        while vec_index688 < len(vec_688):
                            var_689, var_690 = vec_688[vec_index688]
                            vec_index688 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_690 = self._resolve_edgetype(var_690)
                            tuple_684_689_690 = (var_684, var_689, var_690)
                            prev_state = self.table_26[tuple_684_689_690]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_684_689_690] = 0 | 4
                                # Program Call Region
                                ret = self.proc_252_(var_684, var_689, var_690)

                        # Program TransitionState Region
                        tuple_684_684 = (var_684, var_684)
                        prev_state = self.table_6[tuple_684_684]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_684_684] = 1 | 4
                            if not present_bit:
                                self.index_387[tuple_684_684[1]].append(tuple_684_684[0])
                                self.index_949[tuple_684_684[0]].append(tuple_684_684[1])
                            # Program VectorAppend Region
                            vec_633.append((var_684, var_684))
                        # Program VectorAppend Region
                        vec_713.append(var_684)
        # Program VectorClear Region
        del vec_682[:]
        vec_index682 = 0
        # Program VectorUnique Region
        vec_692 = list(set(vec_692))
        vec_index692 = 0
        # Program TableJoin Region
        while vec_index692 < len(vec_692):
            var_694 = vec_692[vec_index692]
            vec_index692 += 1
            tuple_693_0_index: int = 0
            tuple_693_0_vec: List[Tuple[int, bytes, bytes]] = self.index_357[var_694]
            while tuple_693_0_index < len(tuple_693_0_vec):
                tuple_693_0 = tuple_693_0_vec[tuple_693_0_index]
                tuple_693_0_index += 1
                var_695 = tuple_693_0[0]
                var_696 = tuple_693_0[1]
                var_697 = tuple_693_0[2]
                tuple_693_1_index: int = 0
                tuple_693_1_vec: List[Tuple[int, int]] = self.index_358[var_694]
                while tuple_693_1_index < len(tuple_693_1_vec):
                    tuple_693_1 = tuple_693_1_vec[tuple_693_1_index]
                    tuple_693_1_index += 1
                    var_698 = tuple_693_1[0]
                    var_699 = tuple_693_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_695, var_698, ):
                        # Program TransitionState Region
                        tuple_2_1_694_696_697_699 = (self.var_2, self.var_1, var_694, var_696, var_697, var_699)
                        prev_state = self.table_60[tuple_2_1_694_696_697_699]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_694_696_697_699] = 1 | 4
                            if not present_bit:
                                self.index_367[tuple_2_1_694_696_697_699[5]].append((tuple_2_1_694_696_697_699[0], tuple_2_1_694_696_697_699[1], tuple_2_1_694_696_697_699[2], tuple_2_1_694_696_697_699[3], tuple_2_1_694_696_697_699[4]))
                            # Program VectorAppend Region
                            vec_700.append(var_699)
        # Program VectorClear Region
        del vec_692[:]
        vec_index692 = 0
        # Program VectorUnique Region
        vec_700 = list(set(vec_700))
        vec_index700 = 0
        # Program TableJoin Region
        while vec_index700 < len(vec_700):
            var_702 = vec_700[vec_index700]
            vec_index700 += 1
            tuple_701_0_index: int = 0
            tuple_701_0_vec: List[bytes] = self.index_345[var_702]
            while tuple_701_0_index < len(tuple_701_0_vec):
                tuple_701_0 = tuple_701_0_vec[tuple_701_0_index]
                tuple_701_0_index += 1
                var_703 = tuple_701_0
                tuple_701_1_index: int = 0
                tuple_701_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_367[var_702]
                while tuple_701_1_index < len(tuple_701_1_vec):
                    tuple_701_1 = tuple_701_1_vec[tuple_701_1_index]
                    tuple_701_1_index += 1
                    var_704 = tuple_701_1[0]
                    var_705 = tuple_701_1[1]
                    var_706 = tuple_701_1[2]
                    var_707 = tuple_701_1[3]
                    var_708 = tuple_701_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_705, var_704, ):
                        # Program TransitionState Region
                        tuple_706 = var_706
                        prev_state = self.table_14[tuple_706]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_14[tuple_706] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_709: Tuple[int, int]
                            scan_index_709: int = 0
                            scan_tuple_709_vec: List[Tuple[int, int]] = self.index_248[var_706]
                            while scan_index_709 < len(scan_tuple_709_vec):
                                scan_tuple_709 = scan_tuple_709_vec[scan_index_709]
                                scan_index_709 += 1
                                vec_709.append(scan_tuple_709)
                            # Program VectorLoop Region
                            vec_index709 = 0
                            while vec_index709 < len(vec_709):
                                var_710, var_711 = vec_709[vec_index709]
                                vec_index709 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_711 = self._resolve_edgetype(var_711)
                                tuple_706_710_711 = (var_706, var_710, var_711)
                                prev_state = self.table_26[tuple_706_710_711]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_706_710_711] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_252_(var_706, var_710, var_711)

                            # Program TransitionState Region
                            tuple_706_706 = (var_706, var_706)
                            prev_state = self.table_6[tuple_706_706]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_706_706] = 1 | 4
                                if not present_bit:
                                    self.index_387[tuple_706_706[1]].append(tuple_706_706[0])
                                    self.index_949[tuple_706_706[0]].append(tuple_706_706[1])
                                # Program VectorAppend Region
                                vec_633.append((var_706, var_706))
                            # Program VectorAppend Region
                            vec_713.append(var_706)
        # Program VectorClear Region
        del vec_700[:]
        vec_index700 = 0
        # Program VectorUnique Region
        vec_713 = list(set(vec_713))
        vec_index713 = 0
        # Program TableJoin Region
        while vec_index713 < len(vec_713):
            var_715 = vec_713[vec_index713]
            vec_index713 += 1
            tuple_714_0_index: int = 0
            tuple_714_0_vec: List[Tuple[int, int]] = self.index_346[var_715]
            while tuple_714_0_index < len(tuple_714_0_vec):
                tuple_714_0 = tuple_714_0_vec[tuple_714_0_index]
                tuple_714_0_index += 1
                var_716 = tuple_714_0[0]
                var_717 = tuple_714_0[1]
                if var_715 in self.index_381:
                    # Program TransitionState Region
                    tuple_716_715 = (var_716, var_715)
                    prev_state = self.table_16[tuple_716_715]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_16[tuple_716_715] = 1 | 4
                        if not present_bit:
                            self.index_406[tuple_716_715[1]].append(tuple_716_715[0])
                            self.index_956[tuple_716_715[0]].append(tuple_716_715[1])
                        # Program VectorAppend Region
                        vec_726.append(var_715)
        # Program VectorClear Region
        del vec_713[:]
        vec_index713 = 0
        # Program VectorUnique Region
        vec_718 = list(set(vec_718))
        vec_index718 = 0
        # Program TableJoin Region
        while vec_index718 < len(vec_718):
            var_720 = vec_718[vec_index718]
            vec_index718 += 1
            tuple_719_0_index: int = 0
            tuple_719_0_vec: List[int] = self.index_387[var_720]
            while tuple_719_0_index < len(tuple_719_0_vec):
                tuple_719_0 = tuple_719_0_vec[tuple_719_0_index]
                tuple_719_0_index += 1
                var_721 = tuple_719_0
                tuple_719_1_index: int = 0
                tuple_719_1_vec: List[int] = self.index_388[var_720]
                while tuple_719_1_index < len(tuple_719_1_vec):
                    tuple_719_1 = tuple_719_1_vec[tuple_719_1_index]
                    tuple_719_1_index += 1
                    var_722 = tuple_719_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_950_(var_721, var_720)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_953_(var_720, var_722)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_399_(var_721, var_722)
                            if not ret:
                                # Program TransitionState Region
                                tuple_721_722 = (var_721, var_722)
                                prev_state = self.table_6[tuple_721_722]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_721_722] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_721_722[1]].append(tuple_721_722[0])
                                        self.index_949[tuple_721_722[0]].append(tuple_721_722[1])
                                    # Program VectorAppend Region
                                    vec_633.append((var_721, var_722))
        # Program VectorClear Region
        del vec_718[:]
        vec_index718 = 0
        # Program VectorUnique Region
        vec_726 = list(set(vec_726))
        vec_index726 = 0
        # Program TableJoin Region
        while vec_index726 < len(vec_726):
            var_728 = vec_726[vec_index726]
            vec_index726 += 1
            tuple_727_0_index: int = 0
            tuple_727_0_vec: List[int] = self.index_406[var_728]
            while tuple_727_0_index < len(tuple_727_0_vec):
                tuple_727_0 = tuple_727_0_vec[tuple_727_0_index]
                tuple_727_0_index += 1
                var_729 = tuple_727_0
                tuple_727_1_index: int = 0
                tuple_727_1_vec: List[bytes] = self.index_345[var_728]
                while tuple_727_1_index < len(tuple_727_1_vec):
                    tuple_727_1 = tuple_727_1_vec[tuple_727_1_index]
                    tuple_727_1_index += 1
                    var_730 = tuple_727_1
                    # Program TransitionState Region
                    tuple_729 = var_729
                    prev_state = self.table_12[tuple_729]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_729] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_726[:]
        vec_index726 = 0
        # Induction Fixpoint Loop Region
        while len(vec_633):
            # Program Call Region
            param_635_0 = [vec_633]
            ret = self.proc_241_(param_635_0)
            vec_633 = param_635_0[0]

        vec_index633 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_633[:]
        vec_index633 = 0
        # Program Return Region
        return False

    def address_operand_2(self, vec_732: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index732: int = 0
        vec_735: List[int] = list()
        vec_index735: int = 0
        vec_742: List[int] = list()
        vec_index742: int = 0
        vec_749: List[int] = list()
        vec_index749: int = 0
        vec_757: List[int] = list()
        vec_index757: int = 0
        vec_765: List[int] = list()
        vec_index765: int = 0
        vec_776: List[Tuple[int, int]] = list()
        vec_index776: int = 0
        vec_779: List[Tuple[int, int]] = list()
        vec_index779: int = 0
        vec_783: List[int] = list()
        vec_index783: int = 0
        vec_794: List[Tuple[int, int]] = list()
        vec_index794: int = 0
        vec_798: List[int] = list()
        vec_index798: int = 0
        vec_804: List[Tuple[int, int]] = list()
        vec_index804: int = 0
        vec_808: List[int] = list()
        vec_index808: int = 0
        vec_816: List[int] = list()
        vec_index816: int = 0
        vec_825: List[Tuple[int, int]] = list()
        vec_index825: int = 0
        vec_829: List[int] = list()
        vec_index829: int = 0
        vec_834: List[int] = list()
        vec_index834: int = 0
        vec_842: List[int] = list()
        vec_index842: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index732 = 0
        while vec_index732 < len(vec_732):
            var_733, var_734 = vec_732[vec_index732]
            vec_index732 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_733_734 = (var_733, var_734)
            prev_state = self.table_106[tuple_733_734]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_106[tuple_733_734] = 1 | 4
                if not present_bit:
                    self.index_193[tuple_733_734[0]].append(tuple_733_734[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_742.append(var_733)
                # Program VectorAppend Region
                vec_735.append(var_733)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_733_734 = (var_733, var_734)
            prev_state = self.table_106[tuple_733_734]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_106[tuple_733_734] = 1 | 4
                if not present_bit:
                    self.index_193[tuple_733_734[0]].append(tuple_733_734[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_742.append(var_733)
                # Program VectorAppend Region
                vec_735.append(var_733)
        # Program VectorUnique Region
        vec_735 = list(set(vec_735))
        vec_index735 = 0
        # Program TableJoin Region
        while vec_index735 < len(vec_735):
            var_737 = vec_735[vec_index735]
            vec_index735 += 1
            tuple_736_0_index: int = 0
            tuple_736_0_vec: List[Tuple[int, bytes, bytes]] = self.index_192[var_737]
            while tuple_736_0_index < len(tuple_736_0_vec):
                tuple_736_0 = tuple_736_0_vec[tuple_736_0_index]
                tuple_736_0_index += 1
                var_738 = tuple_736_0[0]
                var_739 = tuple_736_0[1]
                var_740 = tuple_736_0[2]
                tuple_736_1_index: int = 0
                tuple_736_1_vec: List[int] = self.index_193[var_737]
                while tuple_736_1_index < len(tuple_736_1_vec):
                    tuple_736_1 = tuple_736_1_vec[tuple_736_1_index]
                    tuple_736_1_index += 1
                    var_741 = tuple_736_1
                    # Program TupleCompare Region
                    if self.var_4 == var_738:
                        # Program TransitionState Region
                        tuple_4_737_739_740_741 = (self.var_4, var_737, var_739, var_740, var_741)
                        prev_state = self.table_130[tuple_4_737_739_740_741]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_130[tuple_4_737_739_740_741] = 1 | 4
                            if not present_bit:
                                self.index_219[tuple_4_737_739_740_741[4]].append((tuple_4_737_739_740_741[0], tuple_4_737_739_740_741[1], tuple_4_737_739_740_741[2], tuple_4_737_739_740_741[3]))
                            # Program VectorAppend Region
                            vec_757.append(var_741)
        # Program VectorClear Region
        del vec_735[:]
        vec_index735 = 0
        # Program VectorUnique Region
        vec_742 = list(set(vec_742))
        vec_index742 = 0
        # Program TableJoin Region
        while vec_index742 < len(vec_742):
            var_744 = vec_742[vec_index742]
            vec_index742 += 1
            tuple_743_0_index: int = 0
            tuple_743_0_vec: List[Tuple[int, bytes, bytes]] = self.index_201[var_744]
            while tuple_743_0_index < len(tuple_743_0_vec):
                tuple_743_0 = tuple_743_0_vec[tuple_743_0_index]
                tuple_743_0_index += 1
                var_745 = tuple_743_0[0]
                var_746 = tuple_743_0[1]
                var_747 = tuple_743_0[2]
                tuple_743_1_index: int = 0
                tuple_743_1_vec: List[int] = self.index_193[var_744]
                while tuple_743_1_index < len(tuple_743_1_vec):
                    tuple_743_1 = tuple_743_1_vec[tuple_743_1_index]
                    tuple_743_1_index += 1
                    var_748 = tuple_743_1
                    # Program TupleCompare Region
                    if self.var_1 == var_745:
                        # Program TransitionState Region
                        tuple_1_744_746_747_748 = (self.var_1, var_744, var_746, var_747, var_748)
                        prev_state = self.table_112[tuple_1_744_746_747_748]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_112[tuple_1_744_746_747_748] = 1 | 4
                            if not present_bit:
                                self.index_210[tuple_1_744_746_747_748[4]].append((tuple_1_744_746_747_748[0], tuple_1_744_746_747_748[1], tuple_1_744_746_747_748[2], tuple_1_744_746_747_748[3]))
                            # Program VectorAppend Region
                            vec_749.append(var_748)
        # Program VectorClear Region
        del vec_742[:]
        vec_index742 = 0
        # Program VectorUnique Region
        vec_749 = list(set(vec_749))
        vec_index749 = 0
        # Program TableJoin Region
        while vec_index749 < len(vec_749):
            var_751 = vec_749[vec_index749]
            vec_index749 += 1
            tuple_750_0_index: int = 0
            tuple_750_0_vec: List[int] = self.index_209[var_751]
            while tuple_750_0_index < len(tuple_750_0_vec):
                tuple_750_0 = tuple_750_0_vec[tuple_750_0_index]
                tuple_750_0_index += 1
                var_752 = tuple_750_0
                tuple_750_1_index: int = 0
                tuple_750_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_210[var_751]
                while tuple_750_1_index < len(tuple_750_1_vec):
                    tuple_750_1 = tuple_750_1_vec[tuple_750_1_index]
                    tuple_750_1_index += 1
                    var_753 = tuple_750_1[0]
                    var_754 = tuple_750_1[1]
                    var_755 = tuple_750_1[2]
                    var_756 = tuple_750_1[3]
                    # Program TupleCompare Region
                    if self.var_1 == var_753:
                        # Program TransitionState Region
                        tuple_1_751_752_754_755_756 = (self.var_1, var_751, var_752, var_754, var_755, var_756)
                        prev_state = self.table_118[tuple_1_751_752_754_755_756]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_118[tuple_1_751_752_754_755_756] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_1_751_752_754_755_756[2]].append((tuple_1_751_752_754_755_756[0], tuple_1_751_752_754_755_756[1], tuple_1_751_752_754_755_756[3], tuple_1_751_752_754_755_756[4], tuple_1_751_752_754_755_756[5]))
                            # Program VectorAppend Region
                            vec_783.append(var_752)
        # Program VectorClear Region
        del vec_749[:]
        vec_index749 = 0
        # Program VectorUnique Region
        vec_757 = list(set(vec_757))
        vec_index757 = 0
        # Program TableJoin Region
        while vec_index757 < len(vec_757):
            var_759 = vec_757[vec_index757]
            vec_index757 += 1
            tuple_758_0_index: int = 0
            tuple_758_0_vec: List[int] = self.index_209[var_759]
            while tuple_758_0_index < len(tuple_758_0_vec):
                tuple_758_0 = tuple_758_0_vec[tuple_758_0_index]
                tuple_758_0_index += 1
                var_760 = tuple_758_0
                tuple_758_1_index: int = 0
                tuple_758_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_219[var_759]
                while tuple_758_1_index < len(tuple_758_1_vec):
                    tuple_758_1 = tuple_758_1_vec[tuple_758_1_index]
                    tuple_758_1_index += 1
                    var_761 = tuple_758_1[0]
                    var_762 = tuple_758_1[1]
                    var_763 = tuple_758_1[2]
                    var_764 = tuple_758_1[3]
                    # Program TupleCompare Region
                    if self.var_4 == var_761:
                        # Program TransitionState Region
                        tuple_4_759_760_762_763_764 = (self.var_4, var_759, var_760, var_762, var_763, var_764)
                        prev_state = self.table_136[tuple_4_759_760_762_763_764]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_136[tuple_4_759_760_762_763_764] = 1 | 4
                            if not present_bit:
                                self.index_260[tuple_4_759_760_762_763_764[2]].append((tuple_4_759_760_762_763_764[0], tuple_4_759_760_762_763_764[1], tuple_4_759_760_762_763_764[3], tuple_4_759_760_762_763_764[4], tuple_4_759_760_762_763_764[5]))
                            # Program VectorAppend Region
                            vec_765.append(var_760)
        # Program VectorClear Region
        del vec_757[:]
        vec_index757 = 0
        # Program VectorUnique Region
        vec_765 = list(set(vec_765))
        vec_index765 = 0
        # Program TableJoin Region
        while vec_index765 < len(vec_765):
            var_767 = vec_765[vec_index765]
            vec_index765 += 1
            if var_767 in self.index_228:
                tuple_766_1_index: int = 0
                tuple_766_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_260[var_767]
                while tuple_766_1_index < len(tuple_766_1_vec):
                    tuple_766_1 = tuple_766_1_vec[tuple_766_1_index]
                    tuple_766_1_index += 1
                    var_768 = tuple_766_1[0]
                    var_769 = tuple_766_1[1]
                    var_770 = tuple_766_1[2]
                    var_771 = tuple_766_1[3]
                    var_772 = tuple_766_1[4]
                    # Program TupleCompare Region
                    if self.var_4 == var_768:
                        # Program TransitionState Region
                        tuple_770_767_0 = (var_770, var_767, self.var_0)
                        prev_state = self.table_43[tuple_770_767_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_770_767_0] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_770_767_0[1]].append((tuple_770_767_0[0], tuple_770_767_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_767_770_0 = (var_767, var_770, self.var_0)
                            prev_state = self.table_26[tuple_767_770_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_767_770_0] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_767_770_0[0]].append((tuple_767_770_0[1], tuple_767_770_0[2]))
                                    self.index_974[(tuple_767_770_0[0], tuple_767_770_0[1])].append(tuple_767_770_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_767)
                            if not ret:
                                # Program TransitionState Region
                                tuple_767_770_0 = (var_767, var_770, self.var_0)
                                prev_state = self.table_26[tuple_767_770_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_767_770_0] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_767_770_0[0]].append((tuple_767_770_0[1], tuple_767_770_0[2]))
                                        self.index_974[(tuple_767_770_0[0], tuple_767_770_0[1])].append(tuple_767_770_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_770, var_767)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_770_767 = (var_770, var_767)
                                        prev_state = self.table_9[tuple_770_767]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_770_767] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_770_767[0]].append(tuple_770_767[1])
                                                self.index_1000[tuple_770_767[1]].append(tuple_770_767[0])
                                            # Program VectorAppend Region
                                            vec_834.append(var_770)
                            # Program VectorAppend Region
                            vec_798.append(var_767)
                            # Program VectorAppend Region
                            vec_829.append(var_767)
                            # Program TransitionState Region
                            tuple_767 = var_767
                            prev_state = self.table_14[tuple_767]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_14[tuple_767] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_779: Tuple[int, int]
                                scan_index_779: int = 0
                                scan_tuple_779_vec: List[Tuple[int, int]] = self.index_248[var_767]
                                while scan_index_779 < len(scan_tuple_779_vec):
                                    scan_tuple_779 = scan_tuple_779_vec[scan_index_779]
                                    scan_index_779 += 1
                                    vec_779.append(scan_tuple_779)
                                # Program VectorLoop Region
                                vec_index779 = 0
                                while vec_index779 < len(vec_779):
                                    var_780, var_781 = vec_779[vec_index779]
                                    vec_index779 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_781 = self._resolve_edgetype(var_781)
                                    tuple_767_780_781 = (var_767, var_780, var_781)
                                    prev_state = self.table_26[tuple_767_780_781]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_767_780_781] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_252_(var_767, var_780, var_781)

                                # Program TransitionState Region
                                tuple_767_767 = (var_767, var_767)
                                prev_state = self.table_6[tuple_767_767]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_767_767] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_767_767[1]].append(tuple_767_767[0])
                                        self.index_949[tuple_767_767[0]].append(tuple_767_767[1])
                                    # Program VectorAppend Region
                                    vec_776.append((var_767, var_767))
                                # Program VectorAppend Region
                                vec_829.append(var_767)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_770_767 = (self.var_0, var_770, var_767)
                                prev_state = self.table_56[tuple_0_770_767]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_770_767] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_0_770_767[1]].append((tuple_0_770_767[0], tuple_0_770_767[2]))
                                    # Program VectorAppend Region
                                    vec_808.append(var_770)
        # Program VectorClear Region
        del vec_765[:]
        vec_index765 = 0
        # Program VectorUnique Region
        vec_783 = list(set(vec_783))
        vec_index783 = 0
        # Program TableJoin Region
        while vec_index783 < len(vec_783):
            var_785 = vec_783[vec_index783]
            vec_index783 += 1
            if var_785 in self.index_228:
                tuple_784_1_index: int = 0
                tuple_784_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_276[var_785]
                while tuple_784_1_index < len(tuple_784_1_vec):
                    tuple_784_1 = tuple_784_1_vec[tuple_784_1_index]
                    tuple_784_1_index += 1
                    var_786 = tuple_784_1[0]
                    var_787 = tuple_784_1[1]
                    var_788 = tuple_784_1[2]
                    var_789 = tuple_784_1[3]
                    var_790 = tuple_784_1[4]
                    # Program TupleCompare Region
                    if self.var_1 == var_786:
                        # Program TransitionState Region
                        tuple_788_785_2 = (var_788, var_785, self.var_2)
                        prev_state = self.table_43[tuple_788_785_2]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_788_785_2] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_788_785_2[1]].append((tuple_788_785_2[0], tuple_788_785_2[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_785_788_2 = (var_785, var_788, self.var_2)
                            prev_state = self.table_26[tuple_785_788_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_785_788_2] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_785_788_2[0]].append((tuple_785_788_2[1], tuple_785_788_2[2]))
                                    self.index_974[(tuple_785_788_2[0], tuple_785_788_2[1])].append(tuple_785_788_2[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_785)
                            if not ret:
                                # Program TransitionState Region
                                tuple_785_788_2 = (var_785, var_788, self.var_2)
                                prev_state = self.table_26[tuple_785_788_2]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_785_788_2] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_785_788_2[0]].append((tuple_785_788_2[1], tuple_785_788_2[2]))
                                        self.index_974[(tuple_785_788_2[0], tuple_785_788_2[1])].append(tuple_785_788_2[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_788, var_785)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_788_785 = (var_788, var_785)
                                        prev_state = self.table_9[tuple_788_785]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_788_785] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_788_785[0]].append(tuple_788_785[1])
                                                self.index_1000[tuple_788_785[1]].append(tuple_788_785[0])
                                            # Program VectorAppend Region
                                            vec_834.append(var_788)
                            # Program VectorAppend Region
                            vec_798.append(var_785)
                            # Program VectorAppend Region
                            vec_829.append(var_785)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_785 = var_785
                                prev_state = self.table_14[tuple_785]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_785] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_794: Tuple[int, int]
                                    scan_index_794: int = 0
                                    scan_tuple_794_vec: List[Tuple[int, int]] = self.index_248[var_785]
                                    while scan_index_794 < len(scan_tuple_794_vec):
                                        scan_tuple_794 = scan_tuple_794_vec[scan_index_794]
                                        scan_index_794 += 1
                                        vec_794.append(scan_tuple_794)
                                    # Program VectorLoop Region
                                    vec_index794 = 0
                                    while vec_index794 < len(vec_794):
                                        var_795, var_796 = vec_794[vec_index794]
                                        vec_index794 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_796 = self._resolve_edgetype(var_796)
                                        tuple_785_795_796 = (var_785, var_795, var_796)
                                        prev_state = self.table_26[tuple_785_795_796]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_785_795_796] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_785, var_795, var_796)

                                    # Program TransitionState Region
                                    tuple_785_785 = (var_785, var_785)
                                    prev_state = self.table_6[tuple_785_785]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_785_785] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_785_785[1]].append(tuple_785_785[0])
                                            self.index_949[tuple_785_785[0]].append(tuple_785_785[1])
                                        # Program VectorAppend Region
                                        vec_776.append((var_785, var_785))
                                    # Program VectorAppend Region
                                    vec_829.append(var_785)
                            # Program TransitionState Region
                            tuple_2_788_785 = (self.var_2, var_788, var_785)
                            prev_state = self.table_56[tuple_2_788_785]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_56[tuple_2_788_785] = 1 | 4
                                if not present_bit:
                                    self.index_358[tuple_2_788_785[1]].append((tuple_2_788_785[0], tuple_2_788_785[2]))
                                # Program VectorAppend Region
                                vec_808.append(var_788)
        # Program VectorClear Region
        del vec_783[:]
        vec_index783 = 0
        # Program VectorUnique Region
        vec_798 = list(set(vec_798))
        vec_index798 = 0
        # Program TableJoin Region
        while vec_index798 < len(vec_798):
            var_800 = vec_798[vec_index798]
            vec_index798 += 1
            tuple_799_0_index: int = 0
            tuple_799_0_vec: List[bytes] = self.index_345[var_800]
            while tuple_799_0_index < len(tuple_799_0_vec):
                tuple_799_0 = tuple_799_0_vec[tuple_799_0_index]
                tuple_799_0_index += 1
                var_801 = tuple_799_0
                tuple_799_1_index: int = 0
                tuple_799_1_vec: List[Tuple[int, int]] = self.index_346[var_800]
                while tuple_799_1_index < len(tuple_799_1_vec):
                    tuple_799_1 = tuple_799_1_vec[tuple_799_1_index]
                    tuple_799_1_index += 1
                    var_802 = tuple_799_1[0]
                    var_803 = tuple_799_1[1]
                    # Program TransitionState Region
                    tuple_800 = var_800
                    prev_state = self.table_14[tuple_800]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_14[tuple_800] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_804: Tuple[int, int]
                        scan_index_804: int = 0
                        scan_tuple_804_vec: List[Tuple[int, int]] = self.index_248[var_800]
                        while scan_index_804 < len(scan_tuple_804_vec):
                            scan_tuple_804 = scan_tuple_804_vec[scan_index_804]
                            scan_index_804 += 1
                            vec_804.append(scan_tuple_804)
                        # Program VectorLoop Region
                        vec_index804 = 0
                        while vec_index804 < len(vec_804):
                            var_805, var_806 = vec_804[vec_index804]
                            vec_index804 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_806 = self._resolve_edgetype(var_806)
                            tuple_800_805_806 = (var_800, var_805, var_806)
                            prev_state = self.table_26[tuple_800_805_806]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_800_805_806] = 0 | 4
                                # Program Call Region
                                ret = self.proc_252_(var_800, var_805, var_806)

                        # Program TransitionState Region
                        tuple_800_800 = (var_800, var_800)
                        prev_state = self.table_6[tuple_800_800]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_800_800] = 1 | 4
                            if not present_bit:
                                self.index_387[tuple_800_800[1]].append(tuple_800_800[0])
                                self.index_949[tuple_800_800[0]].append(tuple_800_800[1])
                            # Program VectorAppend Region
                            vec_776.append((var_800, var_800))
                        # Program VectorAppend Region
                        vec_829.append(var_800)
        # Program VectorClear Region
        del vec_798[:]
        vec_index798 = 0
        # Program VectorUnique Region
        vec_808 = list(set(vec_808))
        vec_index808 = 0
        # Program TableJoin Region
        while vec_index808 < len(vec_808):
            var_810 = vec_808[vec_index808]
            vec_index808 += 1
            tuple_809_0_index: int = 0
            tuple_809_0_vec: List[Tuple[int, bytes, bytes]] = self.index_357[var_810]
            while tuple_809_0_index < len(tuple_809_0_vec):
                tuple_809_0 = tuple_809_0_vec[tuple_809_0_index]
                tuple_809_0_index += 1
                var_811 = tuple_809_0[0]
                var_812 = tuple_809_0[1]
                var_813 = tuple_809_0[2]
                tuple_809_1_index: int = 0
                tuple_809_1_vec: List[Tuple[int, int]] = self.index_358[var_810]
                while tuple_809_1_index < len(tuple_809_1_vec):
                    tuple_809_1 = tuple_809_1_vec[tuple_809_1_index]
                    tuple_809_1_index += 1
                    var_814 = tuple_809_1[0]
                    var_815 = tuple_809_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_811, var_814, ):
                        # Program TransitionState Region
                        tuple_2_1_810_812_813_815 = (self.var_2, self.var_1, var_810, var_812, var_813, var_815)
                        prev_state = self.table_60[tuple_2_1_810_812_813_815]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_810_812_813_815] = 1 | 4
                            if not present_bit:
                                self.index_367[tuple_2_1_810_812_813_815[5]].append((tuple_2_1_810_812_813_815[0], tuple_2_1_810_812_813_815[1], tuple_2_1_810_812_813_815[2], tuple_2_1_810_812_813_815[3], tuple_2_1_810_812_813_815[4]))
                            # Program VectorAppend Region
                            vec_816.append(var_815)
        # Program VectorClear Region
        del vec_808[:]
        vec_index808 = 0
        # Program VectorUnique Region
        vec_816 = list(set(vec_816))
        vec_index816 = 0
        # Program TableJoin Region
        while vec_index816 < len(vec_816):
            var_818 = vec_816[vec_index816]
            vec_index816 += 1
            tuple_817_0_index: int = 0
            tuple_817_0_vec: List[bytes] = self.index_345[var_818]
            while tuple_817_0_index < len(tuple_817_0_vec):
                tuple_817_0 = tuple_817_0_vec[tuple_817_0_index]
                tuple_817_0_index += 1
                var_819 = tuple_817_0
                tuple_817_1_index: int = 0
                tuple_817_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_367[var_818]
                while tuple_817_1_index < len(tuple_817_1_vec):
                    tuple_817_1 = tuple_817_1_vec[tuple_817_1_index]
                    tuple_817_1_index += 1
                    var_820 = tuple_817_1[0]
                    var_821 = tuple_817_1[1]
                    var_822 = tuple_817_1[2]
                    var_823 = tuple_817_1[3]
                    var_824 = tuple_817_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_821, var_820, ):
                        # Program TransitionState Region
                        tuple_822 = var_822
                        prev_state = self.table_14[tuple_822]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_14[tuple_822] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_825: Tuple[int, int]
                            scan_index_825: int = 0
                            scan_tuple_825_vec: List[Tuple[int, int]] = self.index_248[var_822]
                            while scan_index_825 < len(scan_tuple_825_vec):
                                scan_tuple_825 = scan_tuple_825_vec[scan_index_825]
                                scan_index_825 += 1
                                vec_825.append(scan_tuple_825)
                            # Program VectorLoop Region
                            vec_index825 = 0
                            while vec_index825 < len(vec_825):
                                var_826, var_827 = vec_825[vec_index825]
                                vec_index825 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_827 = self._resolve_edgetype(var_827)
                                tuple_822_826_827 = (var_822, var_826, var_827)
                                prev_state = self.table_26[tuple_822_826_827]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_822_826_827] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_252_(var_822, var_826, var_827)

                            # Program TransitionState Region
                            tuple_822_822 = (var_822, var_822)
                            prev_state = self.table_6[tuple_822_822]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_822_822] = 1 | 4
                                if not present_bit:
                                    self.index_387[tuple_822_822[1]].append(tuple_822_822[0])
                                    self.index_949[tuple_822_822[0]].append(tuple_822_822[1])
                                # Program VectorAppend Region
                                vec_776.append((var_822, var_822))
                            # Program VectorAppend Region
                            vec_829.append(var_822)
        # Program VectorClear Region
        del vec_816[:]
        vec_index816 = 0
        # Program VectorUnique Region
        vec_829 = list(set(vec_829))
        vec_index829 = 0
        # Program TableJoin Region
        while vec_index829 < len(vec_829):
            var_831 = vec_829[vec_index829]
            vec_index829 += 1
            tuple_830_0_index: int = 0
            tuple_830_0_vec: List[Tuple[int, int]] = self.index_346[var_831]
            while tuple_830_0_index < len(tuple_830_0_vec):
                tuple_830_0 = tuple_830_0_vec[tuple_830_0_index]
                tuple_830_0_index += 1
                var_832 = tuple_830_0[0]
                var_833 = tuple_830_0[1]
                if var_831 in self.index_381:
                    # Program TransitionState Region
                    tuple_832_831 = (var_832, var_831)
                    prev_state = self.table_16[tuple_832_831]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_16[tuple_832_831] = 1 | 4
                        if not present_bit:
                            self.index_406[tuple_832_831[1]].append(tuple_832_831[0])
                            self.index_956[tuple_832_831[0]].append(tuple_832_831[1])
                        # Program VectorAppend Region
                        vec_842.append(var_831)
        # Program VectorClear Region
        del vec_829[:]
        vec_index829 = 0
        # Program VectorUnique Region
        vec_834 = list(set(vec_834))
        vec_index834 = 0
        # Program TableJoin Region
        while vec_index834 < len(vec_834):
            var_836 = vec_834[vec_index834]
            vec_index834 += 1
            tuple_835_0_index: int = 0
            tuple_835_0_vec: List[int] = self.index_387[var_836]
            while tuple_835_0_index < len(tuple_835_0_vec):
                tuple_835_0 = tuple_835_0_vec[tuple_835_0_index]
                tuple_835_0_index += 1
                var_837 = tuple_835_0
                tuple_835_1_index: int = 0
                tuple_835_1_vec: List[int] = self.index_388[var_836]
                while tuple_835_1_index < len(tuple_835_1_vec):
                    tuple_835_1 = tuple_835_1_vec[tuple_835_1_index]
                    tuple_835_1_index += 1
                    var_838 = tuple_835_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_950_(var_837, var_836)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_953_(var_836, var_838)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_399_(var_837, var_838)
                            if not ret:
                                # Program TransitionState Region
                                tuple_837_838 = (var_837, var_838)
                                prev_state = self.table_6[tuple_837_838]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_837_838] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_837_838[1]].append(tuple_837_838[0])
                                        self.index_949[tuple_837_838[0]].append(tuple_837_838[1])
                                    # Program VectorAppend Region
                                    vec_776.append((var_837, var_838))
        # Program VectorClear Region
        del vec_834[:]
        vec_index834 = 0
        # Program VectorUnique Region
        vec_842 = list(set(vec_842))
        vec_index842 = 0
        # Program TableJoin Region
        while vec_index842 < len(vec_842):
            var_844 = vec_842[vec_index842]
            vec_index842 += 1
            tuple_843_0_index: int = 0
            tuple_843_0_vec: List[int] = self.index_406[var_844]
            while tuple_843_0_index < len(tuple_843_0_vec):
                tuple_843_0 = tuple_843_0_vec[tuple_843_0_index]
                tuple_843_0_index += 1
                var_845 = tuple_843_0
                tuple_843_1_index: int = 0
                tuple_843_1_vec: List[bytes] = self.index_345[var_844]
                while tuple_843_1_index < len(tuple_843_1_vec):
                    tuple_843_1 = tuple_843_1_vec[tuple_843_1_index]
                    tuple_843_1_index += 1
                    var_846 = tuple_843_1
                    # Program TransitionState Region
                    tuple_845 = var_845
                    prev_state = self.table_12[tuple_845]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_845] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_842[:]
        vec_index842 = 0
        # Induction Fixpoint Loop Region
        while len(vec_776):
            # Program Call Region
            param_778_0 = [vec_776]
            ret = self.proc_241_(param_778_0)
            vec_776 = param_778_0[0]

        vec_index776 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_776[:]
        vec_index776 = 0
        # Program Return Region
        return False

    def relocation_2(self, vec_848: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index848: int = 0
        vec_851: List[int] = list()
        vec_index851: int = 0
        vec_859: List[int] = list()
        vec_index859: int = 0
        vec_867: List[int] = list()
        vec_index867: int = 0
        vec_878: List[Tuple[int, int]] = list()
        vec_index878: int = 0
        vec_881: List[Tuple[int, int]] = list()
        vec_index881: int = 0
        vec_885: List[int] = list()
        vec_index885: int = 0
        vec_896: List[Tuple[int, int]] = list()
        vec_index896: int = 0
        vec_900: List[int] = list()
        vec_index900: int = 0
        vec_906: List[Tuple[int, int]] = list()
        vec_index906: int = 0
        vec_910: List[int] = list()
        vec_index910: int = 0
        vec_918: List[int] = list()
        vec_index918: int = 0
        vec_927: List[Tuple[int, int]] = list()
        vec_index927: int = 0
        vec_931: List[int] = list()
        vec_index931: int = 0
        vec_936: List[int] = list()
        vec_index936: int = 0
        vec_944: List[int] = list()
        vec_index944: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index848 = 0
        while vec_index848 < len(vec_848):
            var_849, var_850 = vec_848[vec_index848]
            vec_index848 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_849_850 = (var_849, var_850)
            prev_state = self.table_109[tuple_849_850]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_109[tuple_849_850] = 1 | 4
                if not present_bit:
                    self.index_209[tuple_849_850[0]].append(tuple_849_850[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_859.append(var_849)
                # Program VectorAppend Region
                vec_851.append(var_849)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_849_850 = (var_849, var_850)
            prev_state = self.table_109[tuple_849_850]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_109[tuple_849_850] = 1 | 4
                if not present_bit:
                    self.index_209[tuple_849_850[0]].append(tuple_849_850[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_859.append(var_849)
                # Program VectorAppend Region
                vec_851.append(var_849)
        # Program VectorUnique Region
        vec_851 = list(set(vec_851))
        vec_index851 = 0
        # Program TableJoin Region
        while vec_index851 < len(vec_851):
            var_853 = vec_851[vec_index851]
            vec_index851 += 1
            tuple_852_0_index: int = 0
            tuple_852_0_vec: List[int] = self.index_209[var_853]
            while tuple_852_0_index < len(tuple_852_0_vec):
                tuple_852_0 = tuple_852_0_vec[tuple_852_0_index]
                tuple_852_0_index += 1
                var_854 = tuple_852_0
                tuple_852_1_index: int = 0
                tuple_852_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_219[var_853]
                while tuple_852_1_index < len(tuple_852_1_vec):
                    tuple_852_1 = tuple_852_1_vec[tuple_852_1_index]
                    tuple_852_1_index += 1
                    var_855 = tuple_852_1[0]
                    var_856 = tuple_852_1[1]
                    var_857 = tuple_852_1[2]
                    var_858 = tuple_852_1[3]
                    # Program TupleCompare Region
                    if self.var_4 == var_855:
                        # Program TransitionState Region
                        tuple_4_853_854_856_857_858 = (self.var_4, var_853, var_854, var_856, var_857, var_858)
                        prev_state = self.table_136[tuple_4_853_854_856_857_858]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_136[tuple_4_853_854_856_857_858] = 1 | 4
                            if not present_bit:
                                self.index_260[tuple_4_853_854_856_857_858[2]].append((tuple_4_853_854_856_857_858[0], tuple_4_853_854_856_857_858[1], tuple_4_853_854_856_857_858[3], tuple_4_853_854_856_857_858[4], tuple_4_853_854_856_857_858[5]))
                            # Program VectorAppend Region
                            vec_885.append(var_854)
        # Program VectorClear Region
        del vec_851[:]
        vec_index851 = 0
        # Program VectorUnique Region
        vec_859 = list(set(vec_859))
        vec_index859 = 0
        # Program TableJoin Region
        while vec_index859 < len(vec_859):
            var_861 = vec_859[vec_index859]
            vec_index859 += 1
            tuple_860_0_index: int = 0
            tuple_860_0_vec: List[int] = self.index_209[var_861]
            while tuple_860_0_index < len(tuple_860_0_vec):
                tuple_860_0 = tuple_860_0_vec[tuple_860_0_index]
                tuple_860_0_index += 1
                var_862 = tuple_860_0
                tuple_860_1_index: int = 0
                tuple_860_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_210[var_861]
                while tuple_860_1_index < len(tuple_860_1_vec):
                    tuple_860_1 = tuple_860_1_vec[tuple_860_1_index]
                    tuple_860_1_index += 1
                    var_863 = tuple_860_1[0]
                    var_864 = tuple_860_1[1]
                    var_865 = tuple_860_1[2]
                    var_866 = tuple_860_1[3]
                    # Program TupleCompare Region
                    if self.var_1 == var_863:
                        # Program TransitionState Region
                        tuple_1_861_862_864_865_866 = (self.var_1, var_861, var_862, var_864, var_865, var_866)
                        prev_state = self.table_118[tuple_1_861_862_864_865_866]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_118[tuple_1_861_862_864_865_866] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_1_861_862_864_865_866[2]].append((tuple_1_861_862_864_865_866[0], tuple_1_861_862_864_865_866[1], tuple_1_861_862_864_865_866[3], tuple_1_861_862_864_865_866[4], tuple_1_861_862_864_865_866[5]))
                            # Program VectorAppend Region
                            vec_867.append(var_862)
        # Program VectorClear Region
        del vec_859[:]
        vec_index859 = 0
        # Program VectorUnique Region
        vec_867 = list(set(vec_867))
        vec_index867 = 0
        # Program TableJoin Region
        while vec_index867 < len(vec_867):
            var_869 = vec_867[vec_index867]
            vec_index867 += 1
            if var_869 in self.index_228:
                tuple_868_1_index: int = 0
                tuple_868_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_276[var_869]
                while tuple_868_1_index < len(tuple_868_1_vec):
                    tuple_868_1 = tuple_868_1_vec[tuple_868_1_index]
                    tuple_868_1_index += 1
                    var_870 = tuple_868_1[0]
                    var_871 = tuple_868_1[1]
                    var_872 = tuple_868_1[2]
                    var_873 = tuple_868_1[3]
                    var_874 = tuple_868_1[4]
                    # Program TupleCompare Region
                    if self.var_1 == var_870:
                        # Program TransitionState Region
                        tuple_872_869_2 = (var_872, var_869, self.var_2)
                        prev_state = self.table_43[tuple_872_869_2]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_872_869_2] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_872_869_2[1]].append((tuple_872_869_2[0], tuple_872_869_2[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_869_872_2 = (var_869, var_872, self.var_2)
                            prev_state = self.table_26[tuple_869_872_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_869_872_2] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_869_872_2[0]].append((tuple_869_872_2[1], tuple_869_872_2[2]))
                                    self.index_974[(tuple_869_872_2[0], tuple_869_872_2[1])].append(tuple_869_872_2[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_869)
                            if not ret:
                                # Program TransitionState Region
                                tuple_869_872_2 = (var_869, var_872, self.var_2)
                                prev_state = self.table_26[tuple_869_872_2]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_869_872_2] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_869_872_2[0]].append((tuple_869_872_2[1], tuple_869_872_2[2]))
                                        self.index_974[(tuple_869_872_2[0], tuple_869_872_2[1])].append(tuple_869_872_2[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_872, var_869)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_872_869 = (var_872, var_869)
                                        prev_state = self.table_9[tuple_872_869]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_872_869] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_872_869[0]].append(tuple_872_869[1])
                                                self.index_1000[tuple_872_869[1]].append(tuple_872_869[0])
                                            # Program VectorAppend Region
                                            vec_936.append(var_872)
                            # Program VectorAppend Region
                            vec_900.append(var_869)
                            # Program VectorAppend Region
                            vec_931.append(var_869)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_869 = var_869
                                prev_state = self.table_14[tuple_869]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_14[tuple_869] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_881: Tuple[int, int]
                                    scan_index_881: int = 0
                                    scan_tuple_881_vec: List[Tuple[int, int]] = self.index_248[var_869]
                                    while scan_index_881 < len(scan_tuple_881_vec):
                                        scan_tuple_881 = scan_tuple_881_vec[scan_index_881]
                                        scan_index_881 += 1
                                        vec_881.append(scan_tuple_881)
                                    # Program VectorLoop Region
                                    vec_index881 = 0
                                    while vec_index881 < len(vec_881):
                                        var_882, var_883 = vec_881[vec_index881]
                                        vec_index881 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_883 = self._resolve_edgetype(var_883)
                                        tuple_869_882_883 = (var_869, var_882, var_883)
                                        prev_state = self.table_26[tuple_869_882_883]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_869_882_883] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_252_(var_869, var_882, var_883)

                                    # Program TransitionState Region
                                    tuple_869_869 = (var_869, var_869)
                                    prev_state = self.table_6[tuple_869_869]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_869_869] = 1 | 4
                                        if not present_bit:
                                            self.index_387[tuple_869_869[1]].append(tuple_869_869[0])
                                            self.index_949[tuple_869_869[0]].append(tuple_869_869[1])
                                        # Program VectorAppend Region
                                        vec_878.append((var_869, var_869))
                                    # Program VectorAppend Region
                                    vec_931.append(var_869)
                            # Program TransitionState Region
                            tuple_2_872_869 = (self.var_2, var_872, var_869)
                            prev_state = self.table_56[tuple_2_872_869]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_56[tuple_2_872_869] = 1 | 4
                                if not present_bit:
                                    self.index_358[tuple_2_872_869[1]].append((tuple_2_872_869[0], tuple_2_872_869[2]))
                                # Program VectorAppend Region
                                vec_910.append(var_872)
        # Program VectorClear Region
        del vec_867[:]
        vec_index867 = 0
        # Program VectorUnique Region
        vec_885 = list(set(vec_885))
        vec_index885 = 0
        # Program TableJoin Region
        while vec_index885 < len(vec_885):
            var_887 = vec_885[vec_index885]
            vec_index885 += 1
            if var_887 in self.index_228:
                tuple_886_1_index: int = 0
                tuple_886_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_260[var_887]
                while tuple_886_1_index < len(tuple_886_1_vec):
                    tuple_886_1 = tuple_886_1_vec[tuple_886_1_index]
                    tuple_886_1_index += 1
                    var_888 = tuple_886_1[0]
                    var_889 = tuple_886_1[1]
                    var_890 = tuple_886_1[2]
                    var_891 = tuple_886_1[3]
                    var_892 = tuple_886_1[4]
                    # Program TupleCompare Region
                    if self.var_4 == var_888:
                        # Program TransitionState Region
                        tuple_890_887_0 = (var_890, var_887, self.var_0)
                        prev_state = self.table_43[tuple_890_887_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_890_887_0] = 1 | 4
                            if not present_bit:
                                self.index_346[tuple_890_887_0[1]].append((tuple_890_887_0[0], tuple_890_887_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_887_890_0 = (var_887, var_890, self.var_0)
                            prev_state = self.table_26[tuple_887_890_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_887_890_0] = 2 | 4
                                if not present_bit:
                                    self.index_248[tuple_887_890_0[0]].append((tuple_887_890_0[1], tuple_887_890_0[2]))
                                    self.index_974[(tuple_887_890_0[0], tuple_887_890_0[1])].append(tuple_887_890_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_234_(var_887)
                            if not ret:
                                # Program TransitionState Region
                                tuple_887_890_0 = (var_887, var_890, self.var_0)
                                prev_state = self.table_26[tuple_887_890_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_887_890_0] = 1 | 4
                                    if not present_bit:
                                        self.index_248[tuple_887_890_0[0]].append((tuple_887_890_0[1], tuple_887_890_0[2]))
                                        self.index_974[(tuple_887_890_0[0], tuple_887_890_0[1])].append(tuple_887_890_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_237_(var_890, var_887)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_890_887 = (var_890, var_887)
                                        prev_state = self.table_9[tuple_890_887]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_890_887] = 1 | 4
                                            if not present_bit:
                                                self.index_388[tuple_890_887[0]].append(tuple_890_887[1])
                                                self.index_1000[tuple_890_887[1]].append(tuple_890_887[0])
                                            # Program VectorAppend Region
                                            vec_936.append(var_890)
                            # Program VectorAppend Region
                            vec_900.append(var_887)
                            # Program VectorAppend Region
                            vec_931.append(var_887)
                            # Program TransitionState Region
                            tuple_887 = var_887
                            prev_state = self.table_14[tuple_887]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_14[tuple_887] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_896: Tuple[int, int]
                                scan_index_896: int = 0
                                scan_tuple_896_vec: List[Tuple[int, int]] = self.index_248[var_887]
                                while scan_index_896 < len(scan_tuple_896_vec):
                                    scan_tuple_896 = scan_tuple_896_vec[scan_index_896]
                                    scan_index_896 += 1
                                    vec_896.append(scan_tuple_896)
                                # Program VectorLoop Region
                                vec_index896 = 0
                                while vec_index896 < len(vec_896):
                                    var_897, var_898 = vec_896[vec_index896]
                                    vec_index896 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_898 = self._resolve_edgetype(var_898)
                                    tuple_887_897_898 = (var_887, var_897, var_898)
                                    prev_state = self.table_26[tuple_887_897_898]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_887_897_898] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_252_(var_887, var_897, var_898)

                                # Program TransitionState Region
                                tuple_887_887 = (var_887, var_887)
                                prev_state = self.table_6[tuple_887_887]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_887_887] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_887_887[1]].append(tuple_887_887[0])
                                        self.index_949[tuple_887_887[0]].append(tuple_887_887[1])
                                    # Program VectorAppend Region
                                    vec_878.append((var_887, var_887))
                                # Program VectorAppend Region
                                vec_931.append(var_887)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_890_887 = (self.var_0, var_890, var_887)
                                prev_state = self.table_56[tuple_0_890_887]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_890_887] = 1 | 4
                                    if not present_bit:
                                        self.index_358[tuple_0_890_887[1]].append((tuple_0_890_887[0], tuple_0_890_887[2]))
                                    # Program VectorAppend Region
                                    vec_910.append(var_890)
        # Program VectorClear Region
        del vec_885[:]
        vec_index885 = 0
        # Program VectorUnique Region
        vec_900 = list(set(vec_900))
        vec_index900 = 0
        # Program TableJoin Region
        while vec_index900 < len(vec_900):
            var_902 = vec_900[vec_index900]
            vec_index900 += 1
            tuple_901_0_index: int = 0
            tuple_901_0_vec: List[bytes] = self.index_345[var_902]
            while tuple_901_0_index < len(tuple_901_0_vec):
                tuple_901_0 = tuple_901_0_vec[tuple_901_0_index]
                tuple_901_0_index += 1
                var_903 = tuple_901_0
                tuple_901_1_index: int = 0
                tuple_901_1_vec: List[Tuple[int, int]] = self.index_346[var_902]
                while tuple_901_1_index < len(tuple_901_1_vec):
                    tuple_901_1 = tuple_901_1_vec[tuple_901_1_index]
                    tuple_901_1_index += 1
                    var_904 = tuple_901_1[0]
                    var_905 = tuple_901_1[1]
                    # Program TransitionState Region
                    tuple_902 = var_902
                    prev_state = self.table_14[tuple_902]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_14[tuple_902] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_906: Tuple[int, int]
                        scan_index_906: int = 0
                        scan_tuple_906_vec: List[Tuple[int, int]] = self.index_248[var_902]
                        while scan_index_906 < len(scan_tuple_906_vec):
                            scan_tuple_906 = scan_tuple_906_vec[scan_index_906]
                            scan_index_906 += 1
                            vec_906.append(scan_tuple_906)
                        # Program VectorLoop Region
                        vec_index906 = 0
                        while vec_index906 < len(vec_906):
                            var_907, var_908 = vec_906[vec_index906]
                            vec_index906 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_908 = self._resolve_edgetype(var_908)
                            tuple_902_907_908 = (var_902, var_907, var_908)
                            prev_state = self.table_26[tuple_902_907_908]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_902_907_908] = 0 | 4
                                # Program Call Region
                                ret = self.proc_252_(var_902, var_907, var_908)

                        # Program TransitionState Region
                        tuple_902_902 = (var_902, var_902)
                        prev_state = self.table_6[tuple_902_902]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_902_902] = 1 | 4
                            if not present_bit:
                                self.index_387[tuple_902_902[1]].append(tuple_902_902[0])
                                self.index_949[tuple_902_902[0]].append(tuple_902_902[1])
                            # Program VectorAppend Region
                            vec_878.append((var_902, var_902))
                        # Program VectorAppend Region
                        vec_931.append(var_902)
        # Program VectorClear Region
        del vec_900[:]
        vec_index900 = 0
        # Program VectorUnique Region
        vec_910 = list(set(vec_910))
        vec_index910 = 0
        # Program TableJoin Region
        while vec_index910 < len(vec_910):
            var_912 = vec_910[vec_index910]
            vec_index910 += 1
            tuple_911_0_index: int = 0
            tuple_911_0_vec: List[Tuple[int, bytes, bytes]] = self.index_357[var_912]
            while tuple_911_0_index < len(tuple_911_0_vec):
                tuple_911_0 = tuple_911_0_vec[tuple_911_0_index]
                tuple_911_0_index += 1
                var_913 = tuple_911_0[0]
                var_914 = tuple_911_0[1]
                var_915 = tuple_911_0[2]
                tuple_911_1_index: int = 0
                tuple_911_1_vec: List[Tuple[int, int]] = self.index_358[var_912]
                while tuple_911_1_index < len(tuple_911_1_vec):
                    tuple_911_1 = tuple_911_1_vec[tuple_911_1_index]
                    tuple_911_1_index += 1
                    var_916 = tuple_911_1[0]
                    var_917 = tuple_911_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_913, var_916, ):
                        # Program TransitionState Region
                        tuple_2_1_912_914_915_917 = (self.var_2, self.var_1, var_912, var_914, var_915, var_917)
                        prev_state = self.table_60[tuple_2_1_912_914_915_917]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_912_914_915_917] = 1 | 4
                            if not present_bit:
                                self.index_367[tuple_2_1_912_914_915_917[5]].append((tuple_2_1_912_914_915_917[0], tuple_2_1_912_914_915_917[1], tuple_2_1_912_914_915_917[2], tuple_2_1_912_914_915_917[3], tuple_2_1_912_914_915_917[4]))
                            # Program VectorAppend Region
                            vec_918.append(var_917)
        # Program VectorClear Region
        del vec_910[:]
        vec_index910 = 0
        # Program VectorUnique Region
        vec_918 = list(set(vec_918))
        vec_index918 = 0
        # Program TableJoin Region
        while vec_index918 < len(vec_918):
            var_920 = vec_918[vec_index918]
            vec_index918 += 1
            tuple_919_0_index: int = 0
            tuple_919_0_vec: List[bytes] = self.index_345[var_920]
            while tuple_919_0_index < len(tuple_919_0_vec):
                tuple_919_0 = tuple_919_0_vec[tuple_919_0_index]
                tuple_919_0_index += 1
                var_921 = tuple_919_0
                tuple_919_1_index: int = 0
                tuple_919_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_367[var_920]
                while tuple_919_1_index < len(tuple_919_1_vec):
                    tuple_919_1 = tuple_919_1_vec[tuple_919_1_index]
                    tuple_919_1_index += 1
                    var_922 = tuple_919_1[0]
                    var_923 = tuple_919_1[1]
                    var_924 = tuple_919_1[2]
                    var_925 = tuple_919_1[3]
                    var_926 = tuple_919_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_923, var_922, ):
                        # Program TransitionState Region
                        tuple_924 = var_924
                        prev_state = self.table_14[tuple_924]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_14[tuple_924] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_927: Tuple[int, int]
                            scan_index_927: int = 0
                            scan_tuple_927_vec: List[Tuple[int, int]] = self.index_248[var_924]
                            while scan_index_927 < len(scan_tuple_927_vec):
                                scan_tuple_927 = scan_tuple_927_vec[scan_index_927]
                                scan_index_927 += 1
                                vec_927.append(scan_tuple_927)
                            # Program VectorLoop Region
                            vec_index927 = 0
                            while vec_index927 < len(vec_927):
                                var_928, var_929 = vec_927[vec_index927]
                                vec_index927 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_929 = self._resolve_edgetype(var_929)
                                tuple_924_928_929 = (var_924, var_928, var_929)
                                prev_state = self.table_26[tuple_924_928_929]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_924_928_929] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_252_(var_924, var_928, var_929)

                            # Program TransitionState Region
                            tuple_924_924 = (var_924, var_924)
                            prev_state = self.table_6[tuple_924_924]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_924_924] = 1 | 4
                                if not present_bit:
                                    self.index_387[tuple_924_924[1]].append(tuple_924_924[0])
                                    self.index_949[tuple_924_924[0]].append(tuple_924_924[1])
                                # Program VectorAppend Region
                                vec_878.append((var_924, var_924))
                            # Program VectorAppend Region
                            vec_931.append(var_924)
        # Program VectorClear Region
        del vec_918[:]
        vec_index918 = 0
        # Program VectorUnique Region
        vec_931 = list(set(vec_931))
        vec_index931 = 0
        # Program TableJoin Region
        while vec_index931 < len(vec_931):
            var_933 = vec_931[vec_index931]
            vec_index931 += 1
            tuple_932_0_index: int = 0
            tuple_932_0_vec: List[Tuple[int, int]] = self.index_346[var_933]
            while tuple_932_0_index < len(tuple_932_0_vec):
                tuple_932_0 = tuple_932_0_vec[tuple_932_0_index]
                tuple_932_0_index += 1
                var_934 = tuple_932_0[0]
                var_935 = tuple_932_0[1]
                if var_933 in self.index_381:
                    # Program TransitionState Region
                    tuple_934_933 = (var_934, var_933)
                    prev_state = self.table_16[tuple_934_933]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_16[tuple_934_933] = 1 | 4
                        if not present_bit:
                            self.index_406[tuple_934_933[1]].append(tuple_934_933[0])
                            self.index_956[tuple_934_933[0]].append(tuple_934_933[1])
                        # Program VectorAppend Region
                        vec_944.append(var_933)
        # Program VectorClear Region
        del vec_931[:]
        vec_index931 = 0
        # Program VectorUnique Region
        vec_936 = list(set(vec_936))
        vec_index936 = 0
        # Program TableJoin Region
        while vec_index936 < len(vec_936):
            var_938 = vec_936[vec_index936]
            vec_index936 += 1
            tuple_937_0_index: int = 0
            tuple_937_0_vec: List[int] = self.index_387[var_938]
            while tuple_937_0_index < len(tuple_937_0_vec):
                tuple_937_0 = tuple_937_0_vec[tuple_937_0_index]
                tuple_937_0_index += 1
                var_939 = tuple_937_0
                tuple_937_1_index: int = 0
                tuple_937_1_vec: List[int] = self.index_388[var_938]
                while tuple_937_1_index < len(tuple_937_1_vec):
                    tuple_937_1 = tuple_937_1_vec[tuple_937_1_index]
                    tuple_937_1_index += 1
                    var_940 = tuple_937_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_950_(var_939, var_938)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_953_(var_938, var_940)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_399_(var_939, var_940)
                            if not ret:
                                # Program TransitionState Region
                                tuple_939_940 = (var_939, var_940)
                                prev_state = self.table_6[tuple_939_940]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_939_940] = 1 | 4
                                    if not present_bit:
                                        self.index_387[tuple_939_940[1]].append(tuple_939_940[0])
                                        self.index_949[tuple_939_940[0]].append(tuple_939_940[1])
                                    # Program VectorAppend Region
                                    vec_878.append((var_939, var_940))
        # Program VectorClear Region
        del vec_936[:]
        vec_index936 = 0
        # Program VectorUnique Region
        vec_944 = list(set(vec_944))
        vec_index944 = 0
        # Program TableJoin Region
        while vec_index944 < len(vec_944):
            var_946 = vec_944[vec_index944]
            vec_index944 += 1
            tuple_945_0_index: int = 0
            tuple_945_0_vec: List[int] = self.index_406[var_946]
            while tuple_945_0_index < len(tuple_945_0_vec):
                tuple_945_0 = tuple_945_0_vec[tuple_945_0_index]
                tuple_945_0_index += 1
                var_947 = tuple_945_0
                tuple_945_1_index: int = 0
                tuple_945_1_vec: List[bytes] = self.index_345[var_946]
                while tuple_945_1_index < len(tuple_945_1_vec):
                    tuple_945_1 = tuple_945_1_vec[tuple_945_1_index]
                    tuple_945_1_index += 1
                    var_948 = tuple_945_1
                    # Program TransitionState Region
                    tuple_947 = var_947
                    prev_state = self.table_12[tuple_947]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_947] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_944[:]
        vec_index944 = 0
        # Induction Fixpoint Loop Region
        while len(vec_878):
            # Program Call Region
            param_880_0 = [vec_878]
            ret = self.proc_241_(param_880_0)
            vec_878 = param_880_0[0]

        vec_index878 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_878[:]
        vec_index878 = 0
        # Program Return Region
        return False

    def proc_950_(self, var_951: int, var_952: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_991_(var_951, var_952)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_953_(self, var_954: int, var_955: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_958_(var_954, var_955)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_958_(self, var_959: int, var_960: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_9[(var_959, var_960)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_959_960 = (var_959, var_960)
            prev_state = self.table_9[tuple_959_960]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_9[tuple_959_960] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Union.cpp: BuildTopDownUnionChecker::call_preds
                ret = self.proc_962_(var_959, var_960)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_959_960 = (var_959, var_960)
                    prev_state = self.table_9[tuple_959_960]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_959_960] = 1 | 4
                        if not present_bit:
                            self.index_388[tuple_959_960[0]].append(tuple_959_960[1])
                            self.index_1000[tuple_959_960[1]].append(tuple_959_960[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False

    def proc_962_(self, var_963: int, var_964: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_966_(var_963, var_964)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_966_(self, var_967: int, var_968: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_970_(var_968, var_967)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_970_(self, var_971: int, var_972: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_975: List[int] = list()
        vec_index975: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_975: int
        scan_index_975: int = 0
        scan_tuple_975_vec: List[int] = self.index_974[var_971, var_972]
        while scan_index_975 < len(scan_tuple_975_vec):
            scan_tuple_975 = scan_tuple_975_vec[scan_index_975]
            scan_index_975 += 1
            vec_975.append(scan_tuple_975)
        # Program VectorLoop Region
        vec_index975 = 0
        while vec_index975 < len(vec_975):
            var_976 = vec_975[vec_index975]
            vec_index975 += 1
            # Program CheckState Region
            state = self.table_26[(var_971, var_972, var_976)] & 3
            if state == 0:
                # Program Return Region
                return False
            elif state == 1:
                # Program Series Region
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_234_(var_971)
                if not ret:
                    # Program Return Region
                    return True
                # Program TransitionState Region
                var_976 = self._resolve_edgetype(var_976)
                tuple_971_972_976 = (var_971, var_972, var_976)
                prev_state = self.table_26[tuple_971_972_976]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 1:
                    self.table_26[tuple_971_972_976] = 0 | 4
            elif state == 2:
                # Program TransitionState Region
                var_976 = self._resolve_edgetype(var_976)
                tuple_971_972_976 = (var_971, var_972, var_976)
                prev_state = self.table_26[tuple_971_972_976]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_26[tuple_971_972_976] = 0 | 4
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                    ret = self.proc_234_(var_971)
                    if not ret:
                        # Program Call Region
                        ret = self.proc_981_(var_972, var_971, var_976)
                        if ret:
                            # Program Return Region
                            return True
        # Program Return Region
        return False

    def proc_981_(self, var_982: int, var_983: int, var_984: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_986_(var_982, var_983, var_984)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_986_(self, var_987: int, var_988: int, var_989: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program CheckState Region
        state = self.table_43[(var_987, var_988, var_989)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program Return Region
            return False

    def proc_991_(self, var_992: int, var_993: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program CheckState Region
        state = self.table_6[(var_992, var_993)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program Return Region
            return False

    def proc_995_(self, var_996: int, var_997: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_999: List[int] = list()
        vec_index999: int = 0
        vec_1001: List[int] = list()
        vec_index1001: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1001: int
        scan_index_1001: int = 0
        scan_tuple_1001_vec: List[int] = self.index_1000[var_997]
        while scan_index_1001 < len(scan_tuple_1001_vec):
            scan_tuple_1001 = scan_tuple_1001_vec[scan_index_1001]
            scan_index_1001 += 1
            vec_1001.append(scan_tuple_1001)
        # Program VectorLoop Region
        vec_index1001 = 0
        while vec_index1001 < len(vec_1001):
            var_1002 = vec_1001[vec_index1001]
            vec_index1001 += 1
            # Program VectorAppend Region
            vec_999.append(var_1002)
        # Program VectorUnique Region
        vec_999 = list(set(vec_999))
        vec_index999 = 0
        # Program TableJoin Region
        while vec_index999 < len(vec_999):
            var_1004 = vec_999[vec_index999]
            vec_index999 += 1
            tuple_1003_0_index: int = 0
            tuple_1003_0_vec: List[int] = self.index_387[var_1004]
            while tuple_1003_0_index < len(tuple_1003_0_vec):
                tuple_1003_0 = tuple_1003_0_vec[tuple_1003_0_index]
                tuple_1003_0_index += 1
                var_1005 = tuple_1003_0
                tuple_1003_1_index: int = 0
                tuple_1003_1_vec: List[int] = self.index_388[var_1004]
                while tuple_1003_1_index < len(tuple_1003_1_vec):
                    tuple_1003_1 = tuple_1003_1_vec[tuple_1003_1_index]
                    tuple_1003_1_index += 1
                    var_1006 = tuple_1003_1
                    # Program TupleCompare Region
                    if (var_996, var_997, ) == (var_1005, var_1006, ):
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_950_(var_1005, var_1004)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_953_(var_1004, var_1006)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_999[:]
        vec_index999 = 0
        # Program Return Region
        return False

    def proc_1012_(self, var_1013: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program CheckState Region
        state = self.table_14[var_1013] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program Return Region
            return False

    def proc_1031_(self, var_1032: int, var_1033: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Union.cpp: BuildTopDownUnionChecker::call_preds
        ret = self.proc_962_(var_1032, var_1033)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1035_(self, var_1036: int, var_1037: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1039: List[int] = list()
        vec_index1039: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1039: int
        scan_index_1039: int = 0
        scan_tuple_1039_vec: List[int] = self.index_387[var_1036]
        while scan_index_1039 < len(scan_tuple_1039_vec):
            scan_tuple_1039 = scan_tuple_1039_vec[scan_index_1039]
            scan_index_1039 += 1
            vec_1039.append(scan_tuple_1039)
        # Program VectorLoop Region
        vec_index1039 = 0
        while vec_index1039 < len(vec_1039):
            var_1040 = vec_1039[vec_index1039]
            vec_index1039 += 1
            # Program Call Region
            ret = self.proc_1041_(var_1036, var_1040, var_1037)

        # Program Return Region
        return False

    def proc_1041_(self, var_1042: int, var_1043: int, var_1044: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1043_1044 = (var_1043, var_1044)
        prev_state = self.table_6[tuple_1043_1044]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_6[tuple_1043_1044] = 2 | 4
            # Program Call Region
            ret = self.proc_1054_(var_1043, var_1044)

        # Program Return Region
        return False

    def proc_1054_(self, var_1055: int, var_1056: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Union.cpp: CreateBottomUpUnionRemover
        ret = self.proc_1058_(var_1055, var_1056)
        if not ret:
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1071_(var_1055, var_1056)

            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1058_(var_1055, var_1056)

        # Program Return Region
        return False

    def proc_1058_(self, var_1059: int, var_1060: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1059_1060 = (var_1059, var_1060)
        prev_state = self.table_6[tuple_1059_1060]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_6[tuple_1059_1060] = 0 | 4
            # Program Parallel Region
            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_1078_(var_1059, var_1060)
            if ret:
                # Program Series Region
                # Program TransitionState Region
                tuple_1059_1060 = (var_1059, var_1060)
                prev_state = self.table_6[tuple_1059_1060]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_6[tuple_1059_1060] = 1 | 4
                    if not present_bit:
                        self.index_387[tuple_1059_1060[1]].append(tuple_1059_1060[0])
                        self.index_949[tuple_1059_1060[0]].append(tuple_1059_1060[1])
                # Program Return Region
                return True
            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_1082_(var_1059, var_1060)
            if ret:
                # Program Series Region
                # Program TransitionState Region
                tuple_1059_1060 = (var_1059, var_1060)
                prev_state = self.table_6[tuple_1059_1060]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_6[tuple_1059_1060] = 1 | 4
                    if not present_bit:
                        self.index_387[tuple_1059_1060[1]].append(tuple_1059_1060[0])
                        self.index_949[tuple_1059_1060[0]].append(tuple_1059_1060[1])
                # Program Return Region
                return True
        # Program Return Region
        return False

    def proc_1071_(self, var_1072: int, var_1073: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1075: List[int] = list()
        vec_index1075: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1075: int
        scan_index_1075: int = 0
        scan_tuple_1075_vec: List[int] = self.index_388[var_1073]
        while scan_index_1075 < len(scan_tuple_1075_vec):
            scan_tuple_1075 = scan_tuple_1075_vec[scan_index_1075]
            scan_index_1075 += 1
            vec_1075.append(scan_tuple_1075)
        # Program VectorLoop Region
        vec_index1075 = 0
        while vec_index1075 < len(vec_1075):
            var_1076 = vec_1075[vec_index1075]
            vec_index1075 += 1
            # Program Call Region
            ret = self.proc_1041_(var_1073, var_1072, var_1076)

        # Program Return Region
        return False

    def proc_1078_(self, var_1079: int, var_1080: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1095_(var_1079, var_1080)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1082_(self, var_1083: int, var_1084: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1086_(var_1083, var_1084)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1086_(self, var_1087: int, var_1088: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1090_(var_1087, var_1088)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1090_(self, var_1091: int, var_1092: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_995_(var_1091, var_1092)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1095_(self, var_1096: int, var_1097: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1099_(var_1096, var_1097)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1099_(self, var_1100: int, var_1101: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_234_(var_1101)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def get_external_calls_f(self) -> Iterator[int]:
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

    def function_instruction_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_949[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_950_(param_0, param_1):
                continue
            yield param_1

    def intraproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_388[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_953_(param_0, param_1):
                continue
            yield param_1

    def function_b(self, param_0: int) -> bool:
        state: int = 0
        tuple_index: int = 0
        if True:
            full_tuple = param_0
            state = self.table_14[full_tuple] & 3
            if state != 1:
                return False
            return True

    def function_f(self) -> Iterator[int]:
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

    def interproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_956[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_16[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_sections_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_19:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_19[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

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
        tuple_vec: List[int] = self.index_957[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_23[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

