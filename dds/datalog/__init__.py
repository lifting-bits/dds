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
        self.index_414: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_1029: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_9: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_415: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_1079: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_12: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_433: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_1028: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_15: DefaultDict[int, int] = defaultdict(int)

        self.table_17: DefaultDict[int, int] = defaultdict(int)
        self.index_408 = self.table_17

        self.table_19: DefaultDict[bytes, int] = defaultdict(int)

        self.table_21: DefaultDict[int, int] = defaultdict(int)

        self.table_23: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_1036: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_26: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_199: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)
        self.index_1053: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)

        self.table_30: DefaultDict[Tuple[bytes, int, int, int], int] = defaultdict(int)
        self.index_170: DefaultDict[bytes, List[Tuple[int, int, int]]] = defaultdict(list)

        self.table_35: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_171: DefaultDict[bytes, List[Tuple[int, int, bytes]]] = defaultdict(list)
        self.index_188: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_40: DefaultDict[Tuple[int, bytes], int] = defaultdict(int)
        self.index_372: DefaultDict[int, List[bytes]] = defaultdict(list)

        self.table_43: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_373: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_47: DefaultDict[int, int] = defaultdict(int)
        self.index_334 = self.table_47

        self.table_49: DefaultDict[int, int] = defaultdict(int)
        self.index_267 = self.table_49

        self.table_51: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_384: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_56: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_385: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_60: DefaultDict[Tuple[int, int, int, bytes, bytes, int], int] = defaultdict(int)
        self.index_394: DefaultDict[int, List[Tuple[int, int, int, bytes, bytes]]] = defaultdict(list)

        self.table_67: DefaultDict[int, int] = defaultdict(int)
        self.index_211 = self.table_67

        self.table_69: DefaultDict[int, int] = defaultdict(int)
        self.index_187 = self.table_69

        self.table_71: DefaultDict[Tuple[int, int, int, int, int], int] = defaultdict(int)
        self.index_319: DefaultDict[int, List[Tuple[int, int, int, int]]] = defaultdict(list)

        self.table_77: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_697: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_81: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_698: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_85: DefaultDict[Tuple[int, int, int, int, int], int] = defaultdict(int)
        self.index_357: DefaultDict[int, List[Tuple[int, int, int, int]]] = defaultdict(list)

        self.table_91: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_688: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_95: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_689: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_99: DefaultDict[Tuple[int, int, int, int, int], int] = defaultdict(int)
        self.index_342: DefaultDict[int, List[Tuple[int, int, int, int]]] = defaultdict(list)

        self.table_105: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_240: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_110: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_232: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_113: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_248: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_116: DefaultDict[Tuple[int, int, bytes, bytes, int], int] = defaultdict(int)
        self.index_249: DefaultDict[int, List[Tuple[int, int, bytes, bytes]]] = defaultdict(list)

        self.table_122: DefaultDict[Tuple[int, int, int, int, bytes, bytes], int] = defaultdict(int)
        self.index_303: DefaultDict[int, List[Tuple[int, int, int, bytes, bytes]]] = defaultdict(list)

        self.table_129: DefaultDict[Tuple[int, int, bytes, bytes], int] = defaultdict(int)
        self.index_231: DefaultDict[int, List[Tuple[int, bytes, bytes]]] = defaultdict(list)

        self.table_134: DefaultDict[Tuple[int, int, bytes, bytes, int], int] = defaultdict(int)
        self.index_258: DefaultDict[int, List[Tuple[int, int, bytes, bytes]]] = defaultdict(list)

        self.table_140: DefaultDict[Tuple[int, int, int, int, bytes, bytes], int] = defaultdict(int)
        self.index_287: DefaultDict[int, List[Tuple[int, int, int, bytes, bytes]]] = defaultdict(list)

        self.table_147: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_681: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)

        self.table_151: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_682: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)

        self.table_155: DefaultDict[Tuple[int, int, int, int], int] = defaultdict(int)
        self.index_268: DefaultDict[int, List[Tuple[int, int, int]]] = defaultdict(list)

        self.var_0: int = 5
        self.var_1: int = 2
        self.var_2: int = 1
        self.var_3: int = 6
        self.var_4: int = 6
        self.var_5: int = 0
        self.init_160_()

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

    def init_160_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False

    def section_4(self, vec_162: List[Tuple[bytes, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index162: int = 0
        vec_167: List[bytes] = list()
        vec_index167: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index162 = 0
        while vec_index162 < len(vec_162):
            var_163, var_164, var_165, var_166 = vec_162[vec_index162]
            vec_index162 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_166 = self._resolve_sectype(var_166)
            tuple_163_164_165_166 = (var_163, var_164, var_165, var_166)
            prev_state = self.table_30[tuple_163_164_165_166]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_163_164_165_166] = 1 | 4
                if not present_bit:
                    self.index_170[tuple_163_164_165_166[0]].append((tuple_163_164_165_166[1], tuple_163_164_165_166[2], tuple_163_164_165_166[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_163 = var_163
                prev_state = self.table_19[tuple_163]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_19[tuple_163] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_167.append(var_163)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_166 = self._resolve_sectype(var_166)
            tuple_163_164_165_166 = (var_163, var_164, var_165, var_166)
            prev_state = self.table_30[tuple_163_164_165_166]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_163_164_165_166] = 1 | 4
                if not present_bit:
                    self.index_170[tuple_163_164_165_166[0]].append((tuple_163_164_165_166[1], tuple_163_164_165_166[2], tuple_163_164_165_166[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_163 = var_163
                prev_state = self.table_19[tuple_163]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_19[tuple_163] = 1 | 4
                    if not present_bit:
                        pass
                # Program VectorAppend Region
                vec_167.append(var_163)
        # Program VectorUnique Region
        vec_167 = list(set(vec_167))
        vec_index167 = 0
        # Program TableJoin Region
        while vec_index167 < len(vec_167):
            var_169 = vec_167[vec_index167]
            vec_index167 += 1
            tuple_168_0_index: int = 0
            tuple_168_0_vec: List[Tuple[int, int, int]] = self.index_170[var_169]
            while tuple_168_0_index < len(tuple_168_0_vec):
                tuple_168_0 = tuple_168_0_vec[tuple_168_0_index]
                tuple_168_0_index += 1
                var_172 = tuple_168_0[0]
                var_173 = tuple_168_0[1]
                var_174 = tuple_168_0[2]
                tuple_168_1_index: int = 0
                tuple_168_1_vec: List[Tuple[int, int, bytes]] = self.index_171[var_169]
                while tuple_168_1_index < len(tuple_168_1_vec):
                    tuple_168_1 = tuple_168_1_vec[tuple_168_1_index]
                    tuple_168_1_index += 1
                    var_175 = tuple_168_1[0]
                    var_176 = tuple_168_1[1]
                    var_177 = tuple_168_1[2]
                    # Program TransitionState Region
                    tuple_169_175 = (var_169, var_175)
                    prev_state = self.table_23[tuple_169_175]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_23[tuple_169_175] = 1 | 4
                        if not present_bit:
                            self.index_1036[tuple_169_175[0]].append(tuple_169_175[1])
        # Program VectorClear Region
        del vec_167[:]
        vec_index167 = 0
        # Program Return Region
        return False

    def instruction_4(self, vec_179: List[Tuple[int, int, bytes, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index179: int = 0
        vec_184: List[int] = list()
        vec_index184: int = 0
        vec_196: List[Tuple[int, int]] = list()
        vec_index196: int = 0
        vec_200: List[Tuple[int, int]] = list()
        vec_index200: int = 0
        vec_208: List[int] = list()
        vec_index208: int = 0
        vec_215: List[Tuple[int, int]] = list()
        vec_index215: int = 0
        vec_219: List[bytes] = list()
        vec_index219: int = 0
        vec_228: List[int] = list()
        vec_index228: int = 0
        vec_237: List[int] = list()
        vec_index237: int = 0
        vec_245: List[int] = list()
        vec_index245: int = 0
        vec_255: List[int] = list()
        vec_index255: int = 0
        vec_264: List[int] = list()
        vec_index264: int = 0
        vec_280: List[Tuple[int, int]] = list()
        vec_index280: int = 0
        vec_284: List[int] = list()
        vec_index284: int = 0
        vec_296: List[Tuple[int, int]] = list()
        vec_index296: int = 0
        vec_300: List[int] = list()
        vec_index300: int = 0
        vec_312: List[Tuple[int, int]] = list()
        vec_index312: int = 0
        vec_316: List[int] = list()
        vec_index316: int = 0
        vec_327: List[Tuple[int, int]] = list()
        vec_index327: int = 0
        vec_331: List[int] = list()
        vec_index331: int = 0
        vec_335: List[Tuple[int, int]] = list()
        vec_index335: int = 0
        vec_339: List[int] = list()
        vec_index339: int = 0
        vec_350: List[Tuple[int, int]] = list()
        vec_index350: int = 0
        vec_354: List[int] = list()
        vec_index354: int = 0
        vec_365: List[Tuple[int, int]] = list()
        vec_index365: int = 0
        vec_369: List[int] = list()
        vec_index369: int = 0
        vec_377: List[Tuple[int, int]] = list()
        vec_index377: int = 0
        vec_381: List[int] = list()
        vec_index381: int = 0
        vec_391: List[int] = list()
        vec_index391: int = 0
        vec_401: List[Tuple[int, int]] = list()
        vec_index401: int = 0
        vec_405: List[int] = list()
        vec_index405: int = 0
        vec_411: List[int] = list()
        vec_index411: int = 0
        vec_430: List[int] = list()
        vec_index430: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index179 = 0
        while vec_index179 < len(vec_179):
            var_180, var_181, var_182, var_183 = vec_179[vec_index179]
            vec_index179 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_181 = self._resolve_insntype(var_181)
            tuple_180_181_182_183 = (var_180, var_181, var_182, var_183)
            prev_state = self.table_35[tuple_180_181_182_183]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_180_181_182_183] = 1 | 4
                if not present_bit:
                    self.index_171[tuple_180_181_182_183[3]].append((tuple_180_181_182_183[0], tuple_180_181_182_183[1], tuple_180_181_182_183[2]))
                    self.index_188[tuple_180_181_182_183[0]].append((tuple_180_181_182_183[1], tuple_180_181_182_183[2], tuple_180_181_182_183[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_21[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_49[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_331.append(var_180)
                    # Program VectorAppend Region
                    vec_316.append(var_180)
                    # Program VectorAppend Region
                    vec_354.append(var_180)
                    # Program VectorAppend Region
                    vec_339.append(var_180)
                    # Program VectorAppend Region
                    vec_300.append(var_180)
                    # Program VectorAppend Region
                    vec_284.append(var_180)
                    # Program VectorAppend Region
                    vec_264.append(var_180)
                # Program VectorAppend Region
                vec_219.append(var_183)
                # Program VectorAppend Region
                vec_208.append(var_180)
                # Program VectorAppend Region
                vec_184.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_51[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_384[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_381.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_105[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_240[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_237.append(var_180)
                # Program TupleCompare Region
                if self.var_4 == var_181:
                    # Program TransitionState Region
                    tuple_4_180_182_183 = (self.var_4, var_180, var_182, var_183)
                    prev_state = self.table_129[tuple_4_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_129[tuple_4_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_231[tuple_4_180_182_183[1]].append((tuple_4_180_182_183[0], tuple_4_180_182_183[2], tuple_4_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_228.append(var_180)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_181 = self._resolve_insntype(var_181)
            tuple_180_181_182_183 = (var_180, var_181, var_182, var_183)
            prev_state = self.table_35[tuple_180_181_182_183]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_180_181_182_183] = 1 | 4
                if not present_bit:
                    self.index_171[tuple_180_181_182_183[3]].append((tuple_180_181_182_183[0], tuple_180_181_182_183[1], tuple_180_181_182_183[2]))
                    self.index_188[tuple_180_181_182_183[0]].append((tuple_180_181_182_183[1], tuple_180_181_182_183[2], tuple_180_181_182_183[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_21[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_49[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_331.append(var_180)
                    # Program VectorAppend Region
                    vec_316.append(var_180)
                    # Program VectorAppend Region
                    vec_354.append(var_180)
                    # Program VectorAppend Region
                    vec_339.append(var_180)
                    # Program VectorAppend Region
                    vec_300.append(var_180)
                    # Program VectorAppend Region
                    vec_284.append(var_180)
                    # Program VectorAppend Region
                    vec_264.append(var_180)
                # Program VectorAppend Region
                vec_219.append(var_183)
                # Program VectorAppend Region
                vec_208.append(var_180)
                # Program VectorAppend Region
                vec_184.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_51[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_384[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_381.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_105[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_240[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_237.append(var_180)
                # Program TupleCompare Region
                if self.var_4 == var_181:
                    # Program TransitionState Region
                    tuple_4_180_182_183 = (self.var_4, var_180, var_182, var_183)
                    prev_state = self.table_129[tuple_4_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_129[tuple_4_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_231[tuple_4_180_182_183[1]].append((tuple_4_180_182_183[0], tuple_4_180_182_183[2], tuple_4_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_228.append(var_180)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_181 = self._resolve_insntype(var_181)
            tuple_180_181_182_183 = (var_180, var_181, var_182, var_183)
            prev_state = self.table_35[tuple_180_181_182_183]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_180_181_182_183] = 1 | 4
                if not present_bit:
                    self.index_171[tuple_180_181_182_183[3]].append((tuple_180_181_182_183[0], tuple_180_181_182_183[1], tuple_180_181_182_183[2]))
                    self.index_188[tuple_180_181_182_183[0]].append((tuple_180_181_182_183[1], tuple_180_181_182_183[2], tuple_180_181_182_183[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_21[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_49[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_331.append(var_180)
                    # Program VectorAppend Region
                    vec_316.append(var_180)
                    # Program VectorAppend Region
                    vec_354.append(var_180)
                    # Program VectorAppend Region
                    vec_339.append(var_180)
                    # Program VectorAppend Region
                    vec_300.append(var_180)
                    # Program VectorAppend Region
                    vec_284.append(var_180)
                    # Program VectorAppend Region
                    vec_264.append(var_180)
                # Program VectorAppend Region
                vec_219.append(var_183)
                # Program VectorAppend Region
                vec_208.append(var_180)
                # Program VectorAppend Region
                vec_184.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_51[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_384[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_381.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_105[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_240[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_237.append(var_180)
                # Program TupleCompare Region
                if self.var_4 == var_181:
                    # Program TransitionState Region
                    tuple_4_180_182_183 = (self.var_4, var_180, var_182, var_183)
                    prev_state = self.table_129[tuple_4_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_129[tuple_4_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_231[tuple_4_180_182_183[1]].append((tuple_4_180_182_183[0], tuple_4_180_182_183[2], tuple_4_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_228.append(var_180)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_181 = self._resolve_insntype(var_181)
            tuple_180_181_182_183 = (var_180, var_181, var_182, var_183)
            prev_state = self.table_35[tuple_180_181_182_183]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_180_181_182_183] = 1 | 4
                if not present_bit:
                    self.index_171[tuple_180_181_182_183[3]].append((tuple_180_181_182_183[0], tuple_180_181_182_183[1], tuple_180_181_182_183[2]))
                    self.index_188[tuple_180_181_182_183[0]].append((tuple_180_181_182_183[1], tuple_180_181_182_183[2], tuple_180_181_182_183[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_21[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_49[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_331.append(var_180)
                    # Program VectorAppend Region
                    vec_316.append(var_180)
                    # Program VectorAppend Region
                    vec_354.append(var_180)
                    # Program VectorAppend Region
                    vec_339.append(var_180)
                    # Program VectorAppend Region
                    vec_300.append(var_180)
                    # Program VectorAppend Region
                    vec_284.append(var_180)
                    # Program VectorAppend Region
                    vec_264.append(var_180)
                # Program VectorAppend Region
                vec_219.append(var_183)
                # Program VectorAppend Region
                vec_208.append(var_180)
                # Program VectorAppend Region
                vec_184.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_51[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_384[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_381.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_105[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_240[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_237.append(var_180)
                # Program TupleCompare Region
                if self.var_4 == var_181:
                    # Program TransitionState Region
                    tuple_4_180_182_183 = (self.var_4, var_180, var_182, var_183)
                    prev_state = self.table_129[tuple_4_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_129[tuple_4_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_231[tuple_4_180_182_183[1]].append((tuple_4_180_182_183[0], tuple_4_180_182_183[2], tuple_4_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_228.append(var_180)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_181 = self._resolve_insntype(var_181)
            tuple_180_181_182_183 = (var_180, var_181, var_182, var_183)
            prev_state = self.table_35[tuple_180_181_182_183]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_180_181_182_183] = 1 | 4
                if not present_bit:
                    self.index_171[tuple_180_181_182_183[3]].append((tuple_180_181_182_183[0], tuple_180_181_182_183[1], tuple_180_181_182_183[2]))
                    self.index_188[tuple_180_181_182_183[0]].append((tuple_180_181_182_183[1], tuple_180_181_182_183[2], tuple_180_181_182_183[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_21[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_49[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_331.append(var_180)
                    # Program VectorAppend Region
                    vec_316.append(var_180)
                    # Program VectorAppend Region
                    vec_354.append(var_180)
                    # Program VectorAppend Region
                    vec_339.append(var_180)
                    # Program VectorAppend Region
                    vec_300.append(var_180)
                    # Program VectorAppend Region
                    vec_284.append(var_180)
                    # Program VectorAppend Region
                    vec_264.append(var_180)
                # Program VectorAppend Region
                vec_219.append(var_183)
                # Program VectorAppend Region
                vec_208.append(var_180)
                # Program VectorAppend Region
                vec_184.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_51[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_384[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_381.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_105[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_240[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_237.append(var_180)
                # Program TupleCompare Region
                if self.var_4 == var_181:
                    # Program TransitionState Region
                    tuple_4_180_182_183 = (self.var_4, var_180, var_182, var_183)
                    prev_state = self.table_129[tuple_4_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_129[tuple_4_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_231[tuple_4_180_182_183[1]].append((tuple_4_180_182_183[0], tuple_4_180_182_183[2], tuple_4_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_228.append(var_180)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_181 = self._resolve_insntype(var_181)
            tuple_180_181_182_183 = (var_180, var_181, var_182, var_183)
            prev_state = self.table_35[tuple_180_181_182_183]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_180_181_182_183] = 1 | 4
                if not present_bit:
                    self.index_171[tuple_180_181_182_183[3]].append((tuple_180_181_182_183[0], tuple_180_181_182_183[1], tuple_180_181_182_183[2]))
                    self.index_188[tuple_180_181_182_183[0]].append((tuple_180_181_182_183[1], tuple_180_181_182_183[2], tuple_180_181_182_183[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_21[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_49[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_331.append(var_180)
                    # Program VectorAppend Region
                    vec_316.append(var_180)
                    # Program VectorAppend Region
                    vec_354.append(var_180)
                    # Program VectorAppend Region
                    vec_339.append(var_180)
                    # Program VectorAppend Region
                    vec_300.append(var_180)
                    # Program VectorAppend Region
                    vec_284.append(var_180)
                    # Program VectorAppend Region
                    vec_264.append(var_180)
                # Program VectorAppend Region
                vec_219.append(var_183)
                # Program VectorAppend Region
                vec_208.append(var_180)
                # Program VectorAppend Region
                vec_184.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_51[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_384[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_381.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_105[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_240[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_237.append(var_180)
                # Program TupleCompare Region
                if self.var_4 == var_181:
                    # Program TransitionState Region
                    tuple_4_180_182_183 = (self.var_4, var_180, var_182, var_183)
                    prev_state = self.table_129[tuple_4_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_129[tuple_4_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_231[tuple_4_180_182_183[1]].append((tuple_4_180_182_183[0], tuple_4_180_182_183[2], tuple_4_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_228.append(var_180)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_181 = self._resolve_insntype(var_181)
            tuple_180_181_182_183 = (var_180, var_181, var_182, var_183)
            prev_state = self.table_35[tuple_180_181_182_183]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_180_181_182_183] = 1 | 4
                if not present_bit:
                    self.index_171[tuple_180_181_182_183[3]].append((tuple_180_181_182_183[0], tuple_180_181_182_183[1], tuple_180_181_182_183[2]))
                    self.index_188[tuple_180_181_182_183[0]].append((tuple_180_181_182_183[1], tuple_180_181_182_183[2], tuple_180_181_182_183[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_21[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_49[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_331.append(var_180)
                    # Program VectorAppend Region
                    vec_316.append(var_180)
                    # Program VectorAppend Region
                    vec_354.append(var_180)
                    # Program VectorAppend Region
                    vec_339.append(var_180)
                    # Program VectorAppend Region
                    vec_300.append(var_180)
                    # Program VectorAppend Region
                    vec_284.append(var_180)
                    # Program VectorAppend Region
                    vec_264.append(var_180)
                # Program VectorAppend Region
                vec_219.append(var_183)
                # Program VectorAppend Region
                vec_208.append(var_180)
                # Program VectorAppend Region
                vec_184.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_51[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_384[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_381.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_105[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_240[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_237.append(var_180)
                # Program TupleCompare Region
                if self.var_4 == var_181:
                    # Program TransitionState Region
                    tuple_4_180_182_183 = (self.var_4, var_180, var_182, var_183)
                    prev_state = self.table_129[tuple_4_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_129[tuple_4_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_231[tuple_4_180_182_183[1]].append((tuple_4_180_182_183[0], tuple_4_180_182_183[2], tuple_4_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_228.append(var_180)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            var_181 = self._resolve_insntype(var_181)
            tuple_180_181_182_183 = (var_180, var_181, var_182, var_183)
            prev_state = self.table_35[tuple_180_181_182_183]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_180_181_182_183] = 1 | 4
                if not present_bit:
                    self.index_171[tuple_180_181_182_183[3]].append((tuple_180_181_182_183[0], tuple_180_181_182_183[1], tuple_180_181_182_183[2]))
                    self.index_188[tuple_180_181_182_183[0]].append((tuple_180_181_182_183[1], tuple_180_181_182_183[2], tuple_180_181_182_183[3]))
                # Program Parallel Region
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_21[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_21[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                # Program TransitionState Region
                tuple_180 = var_180
                prev_state = self.table_49[tuple_180]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_180] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_331.append(var_180)
                    # Program VectorAppend Region
                    vec_316.append(var_180)
                    # Program VectorAppend Region
                    vec_354.append(var_180)
                    # Program VectorAppend Region
                    vec_339.append(var_180)
                    # Program VectorAppend Region
                    vec_300.append(var_180)
                    # Program VectorAppend Region
                    vec_284.append(var_180)
                    # Program VectorAppend Region
                    vec_264.append(var_180)
                # Program VectorAppend Region
                vec_219.append(var_183)
                # Program VectorAppend Region
                vec_208.append(var_180)
                # Program VectorAppend Region
                vec_184.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_51[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_384[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_381.append(var_180)
                # Program TupleCompare Region
                if self.var_1 == var_181:
                    # Program TransitionState Region
                    tuple_1_180_182_183 = (self.var_1, var_180, var_182, var_183)
                    prev_state = self.table_105[tuple_1_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_1_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_240[tuple_1_180_182_183[1]].append((tuple_1_180_182_183[0], tuple_1_180_182_183[2], tuple_1_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_237.append(var_180)
                # Program TupleCompare Region
                if self.var_4 == var_181:
                    # Program TransitionState Region
                    tuple_4_180_182_183 = (self.var_4, var_180, var_182, var_183)
                    prev_state = self.table_129[tuple_4_180_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_129[tuple_4_180_182_183] = 1 | 4
                        if not present_bit:
                            self.index_231[tuple_4_180_182_183[1]].append((tuple_4_180_182_183[0], tuple_4_180_182_183[2], tuple_4_180_182_183[3]))
                        # Program VectorAppend Region
                        vec_228.append(var_180)
        # Program VectorUnique Region
        vec_184 = list(set(vec_184))
        vec_index184 = 0
        # Program TableJoin Region
        while vec_index184 < len(vec_184):
            var_186 = vec_184[vec_index184]
            vec_index184 += 1
            if var_186 in self.index_187:
                tuple_185_1_index: int = 0
                tuple_185_1_vec: List[Tuple[int, bytes, bytes]] = self.index_188[var_186]
                while tuple_185_1_index < len(tuple_185_1_vec):
                    tuple_185_1 = tuple_185_1_vec[tuple_185_1_index]
                    tuple_185_1_index += 1
                    var_189 = tuple_185_1[0]
                    var_190 = tuple_185_1[1]
                    var_191 = tuple_185_1[2]
                    # Program TransitionState Region
                    tuple_186 = var_186
                    prev_state = self.table_17[tuple_186]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_186] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_200: Tuple[int, int]
                        scan_index_200: int = 0
                        scan_tuple_200_vec: List[Tuple[int, int]] = self.index_199[var_186]
                        while scan_index_200 < len(scan_tuple_200_vec):
                            scan_tuple_200 = scan_tuple_200_vec[scan_index_200]
                            scan_index_200 += 1
                            vec_200.append(scan_tuple_200)
                        # Program VectorLoop Region
                        vec_index200 = 0
                        while vec_index200 < len(vec_200):
                            var_201, var_202 = vec_200[vec_index200]
                            vec_index200 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_202 = self._resolve_edgetype(var_202)
                            tuple_186_201_202 = (var_186, var_201, var_202)
                            prev_state = self.table_26[tuple_186_201_202]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_186_201_202] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_186, var_201, var_202)

                        # Program TransitionState Region
                        tuple_186_186 = (var_186, var_186)
                        prev_state = self.table_6[tuple_186_186]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_186_186] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_186_186[1]].append(tuple_186_186[0])
                                self.index_1029[tuple_186_186[0]].append(tuple_186_186[1])
                            # Program VectorAppend Region
                            vec_196.append((var_186, var_186))
                        # Program VectorAppend Region
                        vec_405.append(var_186)
        # Program VectorClear Region
        del vec_184[:]
        vec_index184 = 0
        # Program VectorUnique Region
        vec_208 = list(set(vec_208))
        vec_index208 = 0
        # Program TableJoin Region
        while vec_index208 < len(vec_208):
            var_210 = vec_208[vec_index208]
            vec_index208 += 1
            if var_210 in self.index_211:
                tuple_209_1_index: int = 0
                tuple_209_1_vec: List[Tuple[int, bytes, bytes]] = self.index_188[var_210]
                while tuple_209_1_index < len(tuple_209_1_vec):
                    tuple_209_1 = tuple_209_1_vec[tuple_209_1_index]
                    tuple_209_1_index += 1
                    var_212 = tuple_209_1[0]
                    var_213 = tuple_209_1[1]
                    var_214 = tuple_209_1[2]
                    # Program TransitionState Region
                    tuple_210 = var_210
                    prev_state = self.table_17[tuple_210]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_210] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_215: Tuple[int, int]
                        scan_index_215: int = 0
                        scan_tuple_215_vec: List[Tuple[int, int]] = self.index_199[var_210]
                        while scan_index_215 < len(scan_tuple_215_vec):
                            scan_tuple_215 = scan_tuple_215_vec[scan_index_215]
                            scan_index_215 += 1
                            vec_215.append(scan_tuple_215)
                        # Program VectorLoop Region
                        vec_index215 = 0
                        while vec_index215 < len(vec_215):
                            var_216, var_217 = vec_215[vec_index215]
                            vec_index215 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_217 = self._resolve_edgetype(var_217)
                            tuple_210_216_217 = (var_210, var_216, var_217)
                            prev_state = self.table_26[tuple_210_216_217]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_210_216_217] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_210, var_216, var_217)

                        # Program TransitionState Region
                        tuple_210_210 = (var_210, var_210)
                        prev_state = self.table_6[tuple_210_210]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_210_210] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_210_210[1]].append(tuple_210_210[0])
                                self.index_1029[tuple_210_210[0]].append(tuple_210_210[1])
                            # Program VectorAppend Region
                            vec_196.append((var_210, var_210))
                        # Program VectorAppend Region
                        vec_405.append(var_210)
        # Program VectorClear Region
        del vec_208[:]
        vec_index208 = 0
        # Program VectorUnique Region
        vec_219 = list(set(vec_219))
        vec_index219 = 0
        # Program TableJoin Region
        while vec_index219 < len(vec_219):
            var_221 = vec_219[vec_index219]
            vec_index219 += 1
            tuple_220_0_index: int = 0
            tuple_220_0_vec: List[Tuple[int, int, int]] = self.index_170[var_221]
            while tuple_220_0_index < len(tuple_220_0_vec):
                tuple_220_0 = tuple_220_0_vec[tuple_220_0_index]
                tuple_220_0_index += 1
                var_222 = tuple_220_0[0]
                var_223 = tuple_220_0[1]
                var_224 = tuple_220_0[2]
                tuple_220_1_index: int = 0
                tuple_220_1_vec: List[Tuple[int, int, bytes]] = self.index_171[var_221]
                while tuple_220_1_index < len(tuple_220_1_vec):
                    tuple_220_1 = tuple_220_1_vec[tuple_220_1_index]
                    tuple_220_1_index += 1
                    var_225 = tuple_220_1[0]
                    var_226 = tuple_220_1[1]
                    var_227 = tuple_220_1[2]
                    # Program TransitionState Region
                    tuple_221_225 = (var_221, var_225)
                    prev_state = self.table_23[tuple_221_225]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_23[tuple_221_225] = 1 | 4
                        if not present_bit:
                            self.index_1036[tuple_221_225[0]].append(tuple_221_225[1])
        # Program VectorClear Region
        del vec_219[:]
        vec_index219 = 0
        # Program VectorUnique Region
        vec_228 = list(set(vec_228))
        vec_index228 = 0
        # Program TableJoin Region
        while vec_index228 < len(vec_228):
            var_230 = vec_228[vec_index228]
            vec_index228 += 1
            tuple_229_0_index: int = 0
            tuple_229_0_vec: List[Tuple[int, bytes, bytes]] = self.index_231[var_230]
            while tuple_229_0_index < len(tuple_229_0_vec):
                tuple_229_0 = tuple_229_0_vec[tuple_229_0_index]
                tuple_229_0_index += 1
                var_233 = tuple_229_0[0]
                var_234 = tuple_229_0[1]
                var_235 = tuple_229_0[2]
                tuple_229_1_index: int = 0
                tuple_229_1_vec: List[int] = self.index_232[var_230]
                while tuple_229_1_index < len(tuple_229_1_vec):
                    tuple_229_1 = tuple_229_1_vec[tuple_229_1_index]
                    tuple_229_1_index += 1
                    var_236 = tuple_229_1
                    # Program TupleCompare Region
                    if self.var_4 == var_233:
                        # Program TransitionState Region
                        tuple_4_230_234_235_236 = (self.var_4, var_230, var_234, var_235, var_236)
                        prev_state = self.table_134[tuple_4_230_234_235_236]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_134[tuple_4_230_234_235_236] = 1 | 4
                            if not present_bit:
                                self.index_258[tuple_4_230_234_235_236[4]].append((tuple_4_230_234_235_236[0], tuple_4_230_234_235_236[1], tuple_4_230_234_235_236[2], tuple_4_230_234_235_236[3]))
                            # Program VectorAppend Region
                            vec_255.append(var_236)
        # Program VectorClear Region
        del vec_228[:]
        vec_index228 = 0
        # Program VectorUnique Region
        vec_237 = list(set(vec_237))
        vec_index237 = 0
        # Program TableJoin Region
        while vec_index237 < len(vec_237):
            var_239 = vec_237[vec_index237]
            vec_index237 += 1
            tuple_238_0_index: int = 0
            tuple_238_0_vec: List[Tuple[int, bytes, bytes]] = self.index_240[var_239]
            while tuple_238_0_index < len(tuple_238_0_vec):
                tuple_238_0 = tuple_238_0_vec[tuple_238_0_index]
                tuple_238_0_index += 1
                var_241 = tuple_238_0[0]
                var_242 = tuple_238_0[1]
                var_243 = tuple_238_0[2]
                tuple_238_1_index: int = 0
                tuple_238_1_vec: List[int] = self.index_232[var_239]
                while tuple_238_1_index < len(tuple_238_1_vec):
                    tuple_238_1 = tuple_238_1_vec[tuple_238_1_index]
                    tuple_238_1_index += 1
                    var_244 = tuple_238_1
                    # Program TupleCompare Region
                    if self.var_1 == var_241:
                        # Program TransitionState Region
                        tuple_1_239_242_243_244 = (self.var_1, var_239, var_242, var_243, var_244)
                        prev_state = self.table_116[tuple_1_239_242_243_244]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_116[tuple_1_239_242_243_244] = 1 | 4
                            if not present_bit:
                                self.index_249[tuple_1_239_242_243_244[4]].append((tuple_1_239_242_243_244[0], tuple_1_239_242_243_244[1], tuple_1_239_242_243_244[2], tuple_1_239_242_243_244[3]))
                            # Program VectorAppend Region
                            vec_245.append(var_244)
        # Program VectorClear Region
        del vec_237[:]
        vec_index237 = 0
        # Program VectorUnique Region
        vec_245 = list(set(vec_245))
        vec_index245 = 0
        # Program TableJoin Region
        while vec_index245 < len(vec_245):
            var_247 = vec_245[vec_index245]
            vec_index245 += 1
            tuple_246_0_index: int = 0
            tuple_246_0_vec: List[int] = self.index_248[var_247]
            while tuple_246_0_index < len(tuple_246_0_vec):
                tuple_246_0 = tuple_246_0_vec[tuple_246_0_index]
                tuple_246_0_index += 1
                var_250 = tuple_246_0
                tuple_246_1_index: int = 0
                tuple_246_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_249[var_247]
                while tuple_246_1_index < len(tuple_246_1_vec):
                    tuple_246_1 = tuple_246_1_vec[tuple_246_1_index]
                    tuple_246_1_index += 1
                    var_251 = tuple_246_1[0]
                    var_252 = tuple_246_1[1]
                    var_253 = tuple_246_1[2]
                    var_254 = tuple_246_1[3]
                    # Program TupleCompare Region
                    if self.var_1 == var_251:
                        # Program TransitionState Region
                        tuple_1_247_250_252_253_254 = (self.var_1, var_247, var_250, var_252, var_253, var_254)
                        prev_state = self.table_122[tuple_1_247_250_252_253_254]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_122[tuple_1_247_250_252_253_254] = 1 | 4
                            if not present_bit:
                                self.index_303[tuple_1_247_250_252_253_254[2]].append((tuple_1_247_250_252_253_254[0], tuple_1_247_250_252_253_254[1], tuple_1_247_250_252_253_254[3], tuple_1_247_250_252_253_254[4], tuple_1_247_250_252_253_254[5]))
                            # Program VectorAppend Region
                            vec_300.append(var_250)
        # Program VectorClear Region
        del vec_245[:]
        vec_index245 = 0
        # Program VectorUnique Region
        vec_255 = list(set(vec_255))
        vec_index255 = 0
        # Program TableJoin Region
        while vec_index255 < len(vec_255):
            var_257 = vec_255[vec_index255]
            vec_index255 += 1
            tuple_256_0_index: int = 0
            tuple_256_0_vec: List[int] = self.index_248[var_257]
            while tuple_256_0_index < len(tuple_256_0_vec):
                tuple_256_0 = tuple_256_0_vec[tuple_256_0_index]
                tuple_256_0_index += 1
                var_259 = tuple_256_0
                tuple_256_1_index: int = 0
                tuple_256_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_258[var_257]
                while tuple_256_1_index < len(tuple_256_1_vec):
                    tuple_256_1 = tuple_256_1_vec[tuple_256_1_index]
                    tuple_256_1_index += 1
                    var_260 = tuple_256_1[0]
                    var_261 = tuple_256_1[1]
                    var_262 = tuple_256_1[2]
                    var_263 = tuple_256_1[3]
                    # Program TupleCompare Region
                    if self.var_4 == var_260:
                        # Program TransitionState Region
                        tuple_4_257_259_261_262_263 = (self.var_4, var_257, var_259, var_261, var_262, var_263)
                        prev_state = self.table_140[tuple_4_257_259_261_262_263]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_140[tuple_4_257_259_261_262_263] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_4_257_259_261_262_263[2]].append((tuple_4_257_259_261_262_263[0], tuple_4_257_259_261_262_263[1], tuple_4_257_259_261_262_263[3], tuple_4_257_259_261_262_263[4], tuple_4_257_259_261_262_263[5]))
                            # Program VectorAppend Region
                            vec_284.append(var_259)
        # Program VectorClear Region
        del vec_255[:]
        vec_index255 = 0
        # Program VectorUnique Region
        vec_264 = list(set(vec_264))
        vec_index264 = 0
        # Program TableJoin Region
        while vec_index264 < len(vec_264):
            var_266 = vec_264[vec_index264]
            vec_index264 += 1
            if var_266 in self.index_267:
                tuple_265_1_index: int = 0
                tuple_265_1_vec: List[Tuple[int, int, int]] = self.index_268[var_266]
                while tuple_265_1_index < len(tuple_265_1_vec):
                    tuple_265_1 = tuple_265_1_vec[tuple_265_1_index]
                    tuple_265_1_index += 1
                    var_269 = tuple_265_1[0]
                    var_270 = tuple_265_1[1]
                    var_271 = tuple_265_1[2]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_270, var_269, ):
                        # Program TransitionState Region
                        tuple_271_266_5 = (var_271, var_266, self.var_5)
                        prev_state = self.table_43[tuple_271_266_5]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_271_266_5] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_271_266_5[1]].append((tuple_271_266_5[0], tuple_271_266_5[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_266_271_5 = (var_266, var_271, self.var_5)
                            prev_state = self.table_26[tuple_266_271_5]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_266_271_5] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_266_271_5[0]].append((tuple_266_271_5[1], tuple_266_271_5[2]))
                                    self.index_1053[(tuple_266_271_5[0], tuple_266_271_5[1])].append(tuple_266_271_5[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_266)
                            if not ret:
                                # Program TransitionState Region
                                tuple_266_271_5 = (var_266, var_271, self.var_5)
                                prev_state = self.table_26[tuple_266_271_5]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_266_271_5] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_266_271_5[0]].append((tuple_266_271_5[1], tuple_266_271_5[2]))
                                        self.index_1053[(tuple_266_271_5[0], tuple_266_271_5[1])].append(tuple_266_271_5[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_271, var_266)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_271_266 = (var_271, var_266)
                                        prev_state = self.table_9[tuple_271_266]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_271_266] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_271_266[0]].append(tuple_271_266[1])
                                                self.index_1079[tuple_271_266[1]].append(tuple_271_266[0])
                                            # Program VectorAppend Region
                                            vec_411.append(var_271)
                            # Program VectorAppend Region
                            vec_369.append(var_266)
                            # Program VectorAppend Region
                            vec_405.append(var_266)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_5:
                                # Program TransitionState Region
                                tuple_266 = var_266
                                prev_state = self.table_17[tuple_266]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_266] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_280: Tuple[int, int]
                                    scan_index_280: int = 0
                                    scan_tuple_280_vec: List[Tuple[int, int]] = self.index_199[var_266]
                                    while scan_index_280 < len(scan_tuple_280_vec):
                                        scan_tuple_280 = scan_tuple_280_vec[scan_index_280]
                                        scan_index_280 += 1
                                        vec_280.append(scan_tuple_280)
                                    # Program VectorLoop Region
                                    vec_index280 = 0
                                    while vec_index280 < len(vec_280):
                                        var_281, var_282 = vec_280[vec_index280]
                                        vec_index280 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_282 = self._resolve_edgetype(var_282)
                                        tuple_266_281_282 = (var_266, var_281, var_282)
                                        prev_state = self.table_26[tuple_266_281_282]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_266_281_282] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_266, var_281, var_282)

                                    # Program TransitionState Region
                                    tuple_266_266 = (var_266, var_266)
                                    prev_state = self.table_6[tuple_266_266]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_266_266] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_266_266[1]].append(tuple_266_266[0])
                                            self.index_1029[tuple_266_266[0]].append(tuple_266_266[1])
                                        # Program VectorAppend Region
                                        vec_196.append((var_266, var_266))
                                    # Program VectorAppend Region
                                    vec_405.append(var_266)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_5:
                                # Program TransitionState Region
                                tuple_2_271_266 = (self.var_2, var_271, var_266)
                                prev_state = self.table_56[tuple_2_271_266]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_271_266] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_2_271_266[1]].append((tuple_2_271_266[0], tuple_2_271_266[2]))
                                    # Program VectorAppend Region
                                    vec_381.append(var_271)
        # Program VectorClear Region
        del vec_264[:]
        vec_index264 = 0
        # Program VectorUnique Region
        vec_284 = list(set(vec_284))
        vec_index284 = 0
        # Program TableJoin Region
        while vec_index284 < len(vec_284):
            var_286 = vec_284[vec_index284]
            vec_index284 += 1
            if var_286 in self.index_267:
                tuple_285_1_index: int = 0
                tuple_285_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_287[var_286]
                while tuple_285_1_index < len(tuple_285_1_vec):
                    tuple_285_1 = tuple_285_1_vec[tuple_285_1_index]
                    tuple_285_1_index += 1
                    var_288 = tuple_285_1[0]
                    var_289 = tuple_285_1[1]
                    var_290 = tuple_285_1[2]
                    var_291 = tuple_285_1[3]
                    var_292 = tuple_285_1[4]
                    # Program TupleCompare Region
                    if self.var_4 == var_288:
                        # Program TransitionState Region
                        tuple_290_286_0 = (var_290, var_286, self.var_0)
                        prev_state = self.table_43[tuple_290_286_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_290_286_0] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_290_286_0[1]].append((tuple_290_286_0[0], tuple_290_286_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_286_290_0 = (var_286, var_290, self.var_0)
                            prev_state = self.table_26[tuple_286_290_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_286_290_0] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_286_290_0[0]].append((tuple_286_290_0[1], tuple_286_290_0[2]))
                                    self.index_1053[(tuple_286_290_0[0], tuple_286_290_0[1])].append(tuple_286_290_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_286)
                            if not ret:
                                # Program TransitionState Region
                                tuple_286_290_0 = (var_286, var_290, self.var_0)
                                prev_state = self.table_26[tuple_286_290_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_286_290_0] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_286_290_0[0]].append((tuple_286_290_0[1], tuple_286_290_0[2]))
                                        self.index_1053[(tuple_286_290_0[0], tuple_286_290_0[1])].append(tuple_286_290_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_290, var_286)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_290_286 = (var_290, var_286)
                                        prev_state = self.table_9[tuple_290_286]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_290_286] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_290_286[0]].append(tuple_290_286[1])
                                                self.index_1079[tuple_290_286[1]].append(tuple_290_286[0])
                                            # Program VectorAppend Region
                                            vec_411.append(var_290)
                            # Program VectorAppend Region
                            vec_369.append(var_286)
                            # Program VectorAppend Region
                            vec_405.append(var_286)
                            # Program TransitionState Region
                            tuple_286 = var_286
                            prev_state = self.table_17[tuple_286]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_17[tuple_286] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_296: Tuple[int, int]
                                scan_index_296: int = 0
                                scan_tuple_296_vec: List[Tuple[int, int]] = self.index_199[var_286]
                                while scan_index_296 < len(scan_tuple_296_vec):
                                    scan_tuple_296 = scan_tuple_296_vec[scan_index_296]
                                    scan_index_296 += 1
                                    vec_296.append(scan_tuple_296)
                                # Program VectorLoop Region
                                vec_index296 = 0
                                while vec_index296 < len(vec_296):
                                    var_297, var_298 = vec_296[vec_index296]
                                    vec_index296 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_298 = self._resolve_edgetype(var_298)
                                    tuple_286_297_298 = (var_286, var_297, var_298)
                                    prev_state = self.table_26[tuple_286_297_298]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_286_297_298] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_203_(var_286, var_297, var_298)

                                # Program TransitionState Region
                                tuple_286_286 = (var_286, var_286)
                                prev_state = self.table_6[tuple_286_286]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_286_286] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_286_286[1]].append(tuple_286_286[0])
                                        self.index_1029[tuple_286_286[0]].append(tuple_286_286[1])
                                    # Program VectorAppend Region
                                    vec_196.append((var_286, var_286))
                                # Program VectorAppend Region
                                vec_405.append(var_286)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_290_286 = (self.var_0, var_290, var_286)
                                prev_state = self.table_56[tuple_0_290_286]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_290_286] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_0_290_286[1]].append((tuple_0_290_286[0], tuple_0_290_286[2]))
                                    # Program VectorAppend Region
                                    vec_381.append(var_290)
        # Program VectorClear Region
        del vec_284[:]
        vec_index284 = 0
        # Program VectorUnique Region
        vec_300 = list(set(vec_300))
        vec_index300 = 0
        # Program TableJoin Region
        while vec_index300 < len(vec_300):
            var_302 = vec_300[vec_index300]
            vec_index300 += 1
            if var_302 in self.index_267:
                tuple_301_1_index: int = 0
                tuple_301_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_303[var_302]
                while tuple_301_1_index < len(tuple_301_1_vec):
                    tuple_301_1 = tuple_301_1_vec[tuple_301_1_index]
                    tuple_301_1_index += 1
                    var_304 = tuple_301_1[0]
                    var_305 = tuple_301_1[1]
                    var_306 = tuple_301_1[2]
                    var_307 = tuple_301_1[3]
                    var_308 = tuple_301_1[4]
                    # Program TupleCompare Region
                    if self.var_1 == var_304:
                        # Program TransitionState Region
                        tuple_306_302_2 = (var_306, var_302, self.var_2)
                        prev_state = self.table_43[tuple_306_302_2]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_306_302_2] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_306_302_2[1]].append((tuple_306_302_2[0], tuple_306_302_2[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_302_306_2 = (var_302, var_306, self.var_2)
                            prev_state = self.table_26[tuple_302_306_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_302_306_2] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_302_306_2[0]].append((tuple_302_306_2[1], tuple_302_306_2[2]))
                                    self.index_1053[(tuple_302_306_2[0], tuple_302_306_2[1])].append(tuple_302_306_2[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_302)
                            if not ret:
                                # Program TransitionState Region
                                tuple_302_306_2 = (var_302, var_306, self.var_2)
                                prev_state = self.table_26[tuple_302_306_2]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_302_306_2] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_302_306_2[0]].append((tuple_302_306_2[1], tuple_302_306_2[2]))
                                        self.index_1053[(tuple_302_306_2[0], tuple_302_306_2[1])].append(tuple_302_306_2[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_306, var_302)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_306_302 = (var_306, var_302)
                                        prev_state = self.table_9[tuple_306_302]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_306_302] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_306_302[0]].append(tuple_306_302[1])
                                                self.index_1079[tuple_306_302[1]].append(tuple_306_302[0])
                                            # Program VectorAppend Region
                                            vec_411.append(var_306)
                            # Program VectorAppend Region
                            vec_369.append(var_302)
                            # Program VectorAppend Region
                            vec_405.append(var_302)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_302 = var_302
                                prev_state = self.table_17[tuple_302]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_302] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_312: Tuple[int, int]
                                    scan_index_312: int = 0
                                    scan_tuple_312_vec: List[Tuple[int, int]] = self.index_199[var_302]
                                    while scan_index_312 < len(scan_tuple_312_vec):
                                        scan_tuple_312 = scan_tuple_312_vec[scan_index_312]
                                        scan_index_312 += 1
                                        vec_312.append(scan_tuple_312)
                                    # Program VectorLoop Region
                                    vec_index312 = 0
                                    while vec_index312 < len(vec_312):
                                        var_313, var_314 = vec_312[vec_index312]
                                        vec_index312 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_314 = self._resolve_edgetype(var_314)
                                        tuple_302_313_314 = (var_302, var_313, var_314)
                                        prev_state = self.table_26[tuple_302_313_314]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_302_313_314] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_302, var_313, var_314)

                                    # Program TransitionState Region
                                    tuple_302_302 = (var_302, var_302)
                                    prev_state = self.table_6[tuple_302_302]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_302_302] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_302_302[1]].append(tuple_302_302[0])
                                            self.index_1029[tuple_302_302[0]].append(tuple_302_302[1])
                                        # Program VectorAppend Region
                                        vec_196.append((var_302, var_302))
                                    # Program VectorAppend Region
                                    vec_405.append(var_302)
                            # Program TransitionState Region
                            tuple_2_306_302 = (self.var_2, var_306, var_302)
                            prev_state = self.table_56[tuple_2_306_302]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_56[tuple_2_306_302] = 1 | 4
                                if not present_bit:
                                    self.index_385[tuple_2_306_302[1]].append((tuple_2_306_302[0], tuple_2_306_302[2]))
                                # Program VectorAppend Region
                                vec_381.append(var_306)
        # Program VectorClear Region
        del vec_300[:]
        vec_index300 = 0
        # Program VectorUnique Region
        vec_316 = list(set(vec_316))
        vec_index316 = 0
        # Program TableJoin Region
        while vec_index316 < len(vec_316):
            var_318 = vec_316[vec_index316]
            vec_index316 += 1
            tuple_317_0_index: int = 0
            tuple_317_0_vec: List[Tuple[int, int, int, int]] = self.index_319[var_318]
            while tuple_317_0_index < len(tuple_317_0_vec):
                tuple_317_0 = tuple_317_0_vec[tuple_317_0_index]
                tuple_317_0_index += 1
                var_320 = tuple_317_0[0]
                var_321 = tuple_317_0[1]
                var_322 = tuple_317_0[2]
                var_323 = tuple_317_0[3]
                if var_318 in self.index_267:
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_322, var_321, ):
                        # Program TransitionState Region
                        var_320 = self._resolve_edgetype(var_320)
                        tuple_323_318_320 = (var_323, var_318, var_320)
                        prev_state = self.table_43[tuple_323_318_320]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_323_318_320] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_323_318_320[1]].append((tuple_323_318_320[0], tuple_323_318_320[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            var_320 = self._resolve_edgetype(var_320)
                            tuple_318_323_320 = (var_318, var_323, var_320)
                            prev_state = self.table_26[tuple_318_323_320]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_318_323_320] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_318_323_320[0]].append((tuple_318_323_320[1], tuple_318_323_320[2]))
                                    self.index_1053[(tuple_318_323_320[0], tuple_318_323_320[1])].append(tuple_318_323_320[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_318)
                            if not ret:
                                # Program TransitionState Region
                                var_320 = self._resolve_edgetype(var_320)
                                tuple_318_323_320 = (var_318, var_323, var_320)
                                prev_state = self.table_26[tuple_318_323_320]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_318_323_320] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_318_323_320[0]].append((tuple_318_323_320[1], tuple_318_323_320[2]))
                                        self.index_1053[(tuple_318_323_320[0], tuple_318_323_320[1])].append(tuple_318_323_320[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_323, var_318)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_323_318 = (var_323, var_318)
                                        prev_state = self.table_9[tuple_323_318]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_323_318] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_323_318[0]].append(tuple_323_318[1])
                                                self.index_1079[tuple_323_318[1]].append(tuple_323_318[0])
                                            # Program VectorAppend Region
                                            vec_411.append(var_323)
                            # Program VectorAppend Region
                            vec_369.append(var_318)
                            # Program VectorAppend Region
                            vec_405.append(var_318)
                            # Program TupleCompare Region
                            if self.var_0 == var_320:
                                # Program TransitionState Region
                                tuple_318 = var_318
                                prev_state = self.table_17[tuple_318]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_318] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_327: Tuple[int, int]
                                    scan_index_327: int = 0
                                    scan_tuple_327_vec: List[Tuple[int, int]] = self.index_199[var_318]
                                    while scan_index_327 < len(scan_tuple_327_vec):
                                        scan_tuple_327 = scan_tuple_327_vec[scan_index_327]
                                        scan_index_327 += 1
                                        vec_327.append(scan_tuple_327)
                                    # Program VectorLoop Region
                                    vec_index327 = 0
                                    while vec_index327 < len(vec_327):
                                        var_328, var_329 = vec_327[vec_index327]
                                        vec_index327 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_329 = self._resolve_edgetype(var_329)
                                        tuple_318_328_329 = (var_318, var_328, var_329)
                                        prev_state = self.table_26[tuple_318_328_329]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_318_328_329] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_318, var_328, var_329)

                                    # Program TransitionState Region
                                    tuple_318_318 = (var_318, var_318)
                                    prev_state = self.table_6[tuple_318_318]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_318_318] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_318_318[1]].append(tuple_318_318[0])
                                            self.index_1029[tuple_318_318[0]].append(tuple_318_318[1])
                                        # Program VectorAppend Region
                                        vec_196.append((var_318, var_318))
                                    # Program VectorAppend Region
                                    vec_405.append(var_318)
                            # Program TupleCompare Region
                            if self.var_2 == var_320:
                                # Program TransitionState Region
                                tuple_2_323_318 = (self.var_2, var_323, var_318)
                                prev_state = self.table_56[tuple_2_323_318]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_323_318] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_2_323_318[1]].append((tuple_2_323_318[0], tuple_2_323_318[2]))
                                    # Program VectorAppend Region
                                    vec_381.append(var_323)
        # Program VectorClear Region
        del vec_316[:]
        vec_index316 = 0
        # Program VectorUnique Region
        vec_331 = list(set(vec_331))
        vec_index331 = 0
        # Program TableJoin Region
        while vec_index331 < len(vec_331):
            var_333 = vec_331[vec_index331]
            vec_index331 += 1
            if var_333 in self.index_334:
                if var_333 in self.index_267:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_333 = var_333
                    prev_state = self.table_17[tuple_333]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_333] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_335: Tuple[int, int]
                        scan_index_335: int = 0
                        scan_tuple_335_vec: List[Tuple[int, int]] = self.index_199[var_333]
                        while scan_index_335 < len(scan_tuple_335_vec):
                            scan_tuple_335 = scan_tuple_335_vec[scan_index_335]
                            scan_index_335 += 1
                            vec_335.append(scan_tuple_335)
                        # Program VectorLoop Region
                        vec_index335 = 0
                        while vec_index335 < len(vec_335):
                            var_336, var_337 = vec_335[vec_index335]
                            vec_index335 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_337 = self._resolve_edgetype(var_337)
                            tuple_333_336_337 = (var_333, var_336, var_337)
                            prev_state = self.table_26[tuple_333_336_337]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_333_336_337] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_333, var_336, var_337)

                        # Program TransitionState Region
                        tuple_333_333 = (var_333, var_333)
                        prev_state = self.table_6[tuple_333_333]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_333_333] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_333_333[1]].append(tuple_333_333[0])
                                self.index_1029[tuple_333_333[0]].append(tuple_333_333[1])
                            # Program VectorAppend Region
                            vec_196.append((var_333, var_333))
                        # Program VectorAppend Region
                        vec_405.append(var_333)
        # Program VectorClear Region
        del vec_331[:]
        vec_index331 = 0
        # Program VectorUnique Region
        vec_339 = list(set(vec_339))
        vec_index339 = 0
        # Program TableJoin Region
        while vec_index339 < len(vec_339):
            var_341 = vec_339[vec_index339]
            vec_index339 += 1
            if var_341 in self.index_267:
                tuple_340_1_index: int = 0
                tuple_340_1_vec: List[Tuple[int, int, int, int]] = self.index_342[var_341]
                while tuple_340_1_index < len(tuple_340_1_vec):
                    tuple_340_1 = tuple_340_1_vec[tuple_340_1_index]
                    tuple_340_1_index += 1
                    var_343 = tuple_340_1[0]
                    var_344 = tuple_340_1[1]
                    var_345 = tuple_340_1[2]
                    var_346 = tuple_340_1[3]
                    # Program TupleCompare Region
                    if (self.var_3, self.var_0, ) == (var_344, var_345, ):
                        # Program TransitionState Region
                        tuple_346_341_3 = (var_346, var_341, self.var_3)
                        prev_state = self.table_43[tuple_346_341_3]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_346_341_3] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_346_341_3[1]].append((tuple_346_341_3[0], tuple_346_341_3[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_341_346_3 = (var_341, var_346, self.var_3)
                            prev_state = self.table_26[tuple_341_346_3]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_341_346_3] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_341_346_3[0]].append((tuple_341_346_3[1], tuple_341_346_3[2]))
                                    self.index_1053[(tuple_341_346_3[0], tuple_341_346_3[1])].append(tuple_341_346_3[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_341)
                            if not ret:
                                # Program TransitionState Region
                                tuple_341_346_3 = (var_341, var_346, self.var_3)
                                prev_state = self.table_26[tuple_341_346_3]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_341_346_3] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_341_346_3[0]].append((tuple_341_346_3[1], tuple_341_346_3[2]))
                                        self.index_1053[(tuple_341_346_3[0], tuple_341_346_3[1])].append(tuple_341_346_3[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_346, var_341)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_346_341 = (var_346, var_341)
                                        prev_state = self.table_9[tuple_346_341]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_346_341] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_346_341[0]].append(tuple_346_341[1])
                                                self.index_1079[tuple_346_341[1]].append(tuple_346_341[0])
                                            # Program VectorAppend Region
                                            vec_411.append(var_346)
                            # Program VectorAppend Region
                            vec_369.append(var_341)
                            # Program VectorAppend Region
                            vec_405.append(var_341)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_3:
                                # Program TransitionState Region
                                tuple_341 = var_341
                                prev_state = self.table_17[tuple_341]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_341] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_350: Tuple[int, int]
                                    scan_index_350: int = 0
                                    scan_tuple_350_vec: List[Tuple[int, int]] = self.index_199[var_341]
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
                                        tuple_341_351_352 = (var_341, var_351, var_352)
                                        prev_state = self.table_26[tuple_341_351_352]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_341_351_352] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_341, var_351, var_352)

                                    # Program TransitionState Region
                                    tuple_341_341 = (var_341, var_341)
                                    prev_state = self.table_6[tuple_341_341]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_341_341] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_341_341[1]].append(tuple_341_341[0])
                                            self.index_1029[tuple_341_341[0]].append(tuple_341_341[1])
                                        # Program VectorAppend Region
                                        vec_196.append((var_341, var_341))
                                    # Program VectorAppend Region
                                    vec_405.append(var_341)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_3:
                                # Program TransitionState Region
                                tuple_2_346_341 = (self.var_2, var_346, var_341)
                                prev_state = self.table_56[tuple_2_346_341]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_346_341] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_2_346_341[1]].append((tuple_2_346_341[0], tuple_2_346_341[2]))
                                    # Program VectorAppend Region
                                    vec_381.append(var_346)
        # Program VectorClear Region
        del vec_339[:]
        vec_index339 = 0
        # Program VectorUnique Region
        vec_354 = list(set(vec_354))
        vec_index354 = 0
        # Program TableJoin Region
        while vec_index354 < len(vec_354):
            var_356 = vec_354[vec_index354]
            vec_index354 += 1
            if var_356 in self.index_267:
                tuple_355_1_index: int = 0
                tuple_355_1_vec: List[Tuple[int, int, int, int]] = self.index_357[var_356]
                while tuple_355_1_index < len(tuple_355_1_vec):
                    tuple_355_1 = tuple_355_1_vec[tuple_355_1_index]
                    tuple_355_1_index += 1
                    var_358 = tuple_355_1[0]
                    var_359 = tuple_355_1[1]
                    var_360 = tuple_355_1[2]
                    var_361 = tuple_355_1[3]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_360, var_359, ):
                        # Program TransitionState Region
                        tuple_361_356_0 = (var_361, var_356, self.var_0)
                        prev_state = self.table_43[tuple_361_356_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_361_356_0] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_361_356_0[1]].append((tuple_361_356_0[0], tuple_361_356_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_356_361_0 = (var_356, var_361, self.var_0)
                            prev_state = self.table_26[tuple_356_361_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_356_361_0] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_356_361_0[0]].append((tuple_356_361_0[1], tuple_356_361_0[2]))
                                    self.index_1053[(tuple_356_361_0[0], tuple_356_361_0[1])].append(tuple_356_361_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_356)
                            if not ret:
                                # Program TransitionState Region
                                tuple_356_361_0 = (var_356, var_361, self.var_0)
                                prev_state = self.table_26[tuple_356_361_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_356_361_0] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_356_361_0[0]].append((tuple_356_361_0[1], tuple_356_361_0[2]))
                                        self.index_1053[(tuple_356_361_0[0], tuple_356_361_0[1])].append(tuple_356_361_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_361, var_356)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_361_356 = (var_361, var_356)
                                        prev_state = self.table_9[tuple_361_356]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_361_356] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_361_356[0]].append(tuple_361_356[1])
                                                self.index_1079[tuple_361_356[1]].append(tuple_361_356[0])
                                            # Program VectorAppend Region
                                            vec_411.append(var_361)
                            # Program VectorAppend Region
                            vec_369.append(var_356)
                            # Program VectorAppend Region
                            vec_405.append(var_356)
                            # Program TransitionState Region
                            tuple_356 = var_356
                            prev_state = self.table_17[tuple_356]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_17[tuple_356] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_365: Tuple[int, int]
                                scan_index_365: int = 0
                                scan_tuple_365_vec: List[Tuple[int, int]] = self.index_199[var_356]
                                while scan_index_365 < len(scan_tuple_365_vec):
                                    scan_tuple_365 = scan_tuple_365_vec[scan_index_365]
                                    scan_index_365 += 1
                                    vec_365.append(scan_tuple_365)
                                # Program VectorLoop Region
                                vec_index365 = 0
                                while vec_index365 < len(vec_365):
                                    var_366, var_367 = vec_365[vec_index365]
                                    vec_index365 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_367 = self._resolve_edgetype(var_367)
                                    tuple_356_366_367 = (var_356, var_366, var_367)
                                    prev_state = self.table_26[tuple_356_366_367]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_356_366_367] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_203_(var_356, var_366, var_367)

                                # Program TransitionState Region
                                tuple_356_356 = (var_356, var_356)
                                prev_state = self.table_6[tuple_356_356]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_356_356] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_356_356[1]].append(tuple_356_356[0])
                                        self.index_1029[tuple_356_356[0]].append(tuple_356_356[1])
                                    # Program VectorAppend Region
                                    vec_196.append((var_356, var_356))
                                # Program VectorAppend Region
                                vec_405.append(var_356)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_361_356 = (self.var_0, var_361, var_356)
                                prev_state = self.table_56[tuple_0_361_356]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_361_356] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_0_361_356[1]].append((tuple_0_361_356[0], tuple_0_361_356[2]))
                                    # Program VectorAppend Region
                                    vec_381.append(var_361)
        # Program VectorClear Region
        del vec_354[:]
        vec_index354 = 0
        # Program VectorUnique Region
        vec_369 = list(set(vec_369))
        vec_index369 = 0
        # Program TableJoin Region
        while vec_index369 < len(vec_369):
            var_371 = vec_369[vec_index369]
            vec_index369 += 1
            tuple_370_0_index: int = 0
            tuple_370_0_vec: List[bytes] = self.index_372[var_371]
            while tuple_370_0_index < len(tuple_370_0_vec):
                tuple_370_0 = tuple_370_0_vec[tuple_370_0_index]
                tuple_370_0_index += 1
                var_374 = tuple_370_0
                tuple_370_1_index: int = 0
                tuple_370_1_vec: List[Tuple[int, int]] = self.index_373[var_371]
                while tuple_370_1_index < len(tuple_370_1_vec):
                    tuple_370_1 = tuple_370_1_vec[tuple_370_1_index]
                    tuple_370_1_index += 1
                    var_375 = tuple_370_1[0]
                    var_376 = tuple_370_1[1]
                    # Program TransitionState Region
                    tuple_371 = var_371
                    prev_state = self.table_17[tuple_371]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_371] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_377: Tuple[int, int]
                        scan_index_377: int = 0
                        scan_tuple_377_vec: List[Tuple[int, int]] = self.index_199[var_371]
                        while scan_index_377 < len(scan_tuple_377_vec):
                            scan_tuple_377 = scan_tuple_377_vec[scan_index_377]
                            scan_index_377 += 1
                            vec_377.append(scan_tuple_377)
                        # Program VectorLoop Region
                        vec_index377 = 0
                        while vec_index377 < len(vec_377):
                            var_378, var_379 = vec_377[vec_index377]
                            vec_index377 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_379 = self._resolve_edgetype(var_379)
                            tuple_371_378_379 = (var_371, var_378, var_379)
                            prev_state = self.table_26[tuple_371_378_379]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_371_378_379] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_371, var_378, var_379)

                        # Program TransitionState Region
                        tuple_371_371 = (var_371, var_371)
                        prev_state = self.table_6[tuple_371_371]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_371_371] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_371_371[1]].append(tuple_371_371[0])
                                self.index_1029[tuple_371_371[0]].append(tuple_371_371[1])
                            # Program VectorAppend Region
                            vec_196.append((var_371, var_371))
                        # Program VectorAppend Region
                        vec_405.append(var_371)
        # Program VectorClear Region
        del vec_369[:]
        vec_index369 = 0
        # Program VectorUnique Region
        vec_381 = list(set(vec_381))
        vec_index381 = 0
        # Program TableJoin Region
        while vec_index381 < len(vec_381):
            var_383 = vec_381[vec_index381]
            vec_index381 += 1
            tuple_382_0_index: int = 0
            tuple_382_0_vec: List[Tuple[int, bytes, bytes]] = self.index_384[var_383]
            while tuple_382_0_index < len(tuple_382_0_vec):
                tuple_382_0 = tuple_382_0_vec[tuple_382_0_index]
                tuple_382_0_index += 1
                var_386 = tuple_382_0[0]
                var_387 = tuple_382_0[1]
                var_388 = tuple_382_0[2]
                tuple_382_1_index: int = 0
                tuple_382_1_vec: List[Tuple[int, int]] = self.index_385[var_383]
                while tuple_382_1_index < len(tuple_382_1_vec):
                    tuple_382_1 = tuple_382_1_vec[tuple_382_1_index]
                    tuple_382_1_index += 1
                    var_389 = tuple_382_1[0]
                    var_390 = tuple_382_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_386, var_389, ):
                        # Program TransitionState Region
                        tuple_2_1_383_387_388_390 = (self.var_2, self.var_1, var_383, var_387, var_388, var_390)
                        prev_state = self.table_60[tuple_2_1_383_387_388_390]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_383_387_388_390] = 1 | 4
                            if not present_bit:
                                self.index_394[tuple_2_1_383_387_388_390[5]].append((tuple_2_1_383_387_388_390[0], tuple_2_1_383_387_388_390[1], tuple_2_1_383_387_388_390[2], tuple_2_1_383_387_388_390[3], tuple_2_1_383_387_388_390[4]))
                            # Program VectorAppend Region
                            vec_391.append(var_390)
        # Program VectorClear Region
        del vec_381[:]
        vec_index381 = 0
        # Program VectorUnique Region
        vec_391 = list(set(vec_391))
        vec_index391 = 0
        # Program TableJoin Region
        while vec_index391 < len(vec_391):
            var_393 = vec_391[vec_index391]
            vec_index391 += 1
            tuple_392_0_index: int = 0
            tuple_392_0_vec: List[bytes] = self.index_372[var_393]
            while tuple_392_0_index < len(tuple_392_0_vec):
                tuple_392_0 = tuple_392_0_vec[tuple_392_0_index]
                tuple_392_0_index += 1
                var_395 = tuple_392_0
                tuple_392_1_index: int = 0
                tuple_392_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_394[var_393]
                while tuple_392_1_index < len(tuple_392_1_vec):
                    tuple_392_1 = tuple_392_1_vec[tuple_392_1_index]
                    tuple_392_1_index += 1
                    var_396 = tuple_392_1[0]
                    var_397 = tuple_392_1[1]
                    var_398 = tuple_392_1[2]
                    var_399 = tuple_392_1[3]
                    var_400 = tuple_392_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_397, var_396, ):
                        # Program TransitionState Region
                        tuple_398 = var_398
                        prev_state = self.table_17[tuple_398]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_17[tuple_398] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_401: Tuple[int, int]
                            scan_index_401: int = 0
                            scan_tuple_401_vec: List[Tuple[int, int]] = self.index_199[var_398]
                            while scan_index_401 < len(scan_tuple_401_vec):
                                scan_tuple_401 = scan_tuple_401_vec[scan_index_401]
                                scan_index_401 += 1
                                vec_401.append(scan_tuple_401)
                            # Program VectorLoop Region
                            vec_index401 = 0
                            while vec_index401 < len(vec_401):
                                var_402, var_403 = vec_401[vec_index401]
                                vec_index401 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_403 = self._resolve_edgetype(var_403)
                                tuple_398_402_403 = (var_398, var_402, var_403)
                                prev_state = self.table_26[tuple_398_402_403]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_398_402_403] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_203_(var_398, var_402, var_403)

                            # Program TransitionState Region
                            tuple_398_398 = (var_398, var_398)
                            prev_state = self.table_6[tuple_398_398]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_398_398] = 1 | 4
                                if not present_bit:
                                    self.index_414[tuple_398_398[1]].append(tuple_398_398[0])
                                    self.index_1029[tuple_398_398[0]].append(tuple_398_398[1])
                                # Program VectorAppend Region
                                vec_196.append((var_398, var_398))
                            # Program VectorAppend Region
                            vec_405.append(var_398)
        # Program VectorClear Region
        del vec_391[:]
        vec_index391 = 0
        # Program VectorUnique Region
        vec_405 = list(set(vec_405))
        vec_index405 = 0
        # Program TableJoin Region
        while vec_index405 < len(vec_405):
            var_407 = vec_405[vec_index405]
            vec_index405 += 1
            tuple_406_0_index: int = 0
            tuple_406_0_vec: List[Tuple[int, int]] = self.index_373[var_407]
            while tuple_406_0_index < len(tuple_406_0_vec):
                tuple_406_0 = tuple_406_0_vec[tuple_406_0_index]
                tuple_406_0_index += 1
                var_409 = tuple_406_0[0]
                var_410 = tuple_406_0[1]
                if var_407 in self.index_408:
                    # Program TransitionState Region
                    tuple_409_407 = (var_409, var_407)
                    prev_state = self.table_12[tuple_409_407]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_409_407] = 1 | 4
                        if not present_bit:
                            self.index_433[tuple_409_407[1]].append(tuple_409_407[0])
                            self.index_1028[tuple_409_407[0]].append(tuple_409_407[1])
                        # Program VectorAppend Region
                        vec_430.append(var_407)
        # Program VectorClear Region
        del vec_405[:]
        vec_index405 = 0
        # Program VectorUnique Region
        vec_411 = list(set(vec_411))
        vec_index411 = 0
        # Program TableJoin Region
        while vec_index411 < len(vec_411):
            var_413 = vec_411[vec_index411]
            vec_index411 += 1
            tuple_412_0_index: int = 0
            tuple_412_0_vec: List[int] = self.index_414[var_413]
            while tuple_412_0_index < len(tuple_412_0_vec):
                tuple_412_0 = tuple_412_0_vec[tuple_412_0_index]
                tuple_412_0_index += 1
                var_416 = tuple_412_0
                tuple_412_1_index: int = 0
                tuple_412_1_vec: List[int] = self.index_415[var_413]
                while tuple_412_1_index < len(tuple_412_1_vec):
                    tuple_412_1 = tuple_412_1_vec[tuple_412_1_index]
                    tuple_412_1_index += 1
                    var_417 = tuple_412_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_1030_(var_416, var_413)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_1033_(var_413, var_417)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_426_(var_416, var_417)
                            if not ret:
                                # Program TransitionState Region
                                tuple_416_417 = (var_416, var_417)
                                prev_state = self.table_6[tuple_416_417]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_416_417] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_416_417[1]].append(tuple_416_417[0])
                                        self.index_1029[tuple_416_417[0]].append(tuple_416_417[1])
                                    # Program VectorAppend Region
                                    vec_196.append((var_416, var_417))
        # Program VectorClear Region
        del vec_411[:]
        vec_index411 = 0
        # Program VectorUnique Region
        vec_430 = list(set(vec_430))
        vec_index430 = 0
        # Program TableJoin Region
        while vec_index430 < len(vec_430):
            var_432 = vec_430[vec_index430]
            vec_index430 += 1
            tuple_431_0_index: int = 0
            tuple_431_0_vec: List[int] = self.index_433[var_432]
            while tuple_431_0_index < len(tuple_431_0_vec):
                tuple_431_0 = tuple_431_0_vec[tuple_431_0_index]
                tuple_431_0_index += 1
                var_434 = tuple_431_0
                tuple_431_1_index: int = 0
                tuple_431_1_vec: List[bytes] = self.index_372[var_432]
                while tuple_431_1_index < len(tuple_431_1_vec):
                    tuple_431_1 = tuple_431_1_vec[tuple_431_1_index]
                    tuple_431_1_index += 1
                    var_435 = tuple_431_1
                    # Program TransitionState Region
                    tuple_434 = var_434
                    prev_state = self.table_15[tuple_434]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_434] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_430[:]
        vec_index430 = 0
        # Induction Fixpoint Loop Region
        while len(vec_196):
            # Program Call Region
            param_198_0 = [vec_196]
            ret = self.proc_192_(param_198_0)
            vec_196 = param_198_0[0]

        vec_index196 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_196[:]
        vec_index196 = 0
        # Program Return Region
        return False

    def proc_192_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_193 = param_0[0]
        vec_index193: int = 0
        vec_436: List[Tuple[int, int]] = list()
        vec_index436: int = 0
        vec_439: List[int] = list()
        vec_index439: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_193, vec_436 = vec_436, vec_193
        # Program VectorLoop Region
        while vec_index436 < len(vec_436):
            var_437, var_438 = vec_436[vec_index436]
            vec_index436 += 1
            # Program VectorAppend Region
            vec_439.append(var_438)
        # Program VectorUnique Region
        vec_439 = list(set(vec_439))
        vec_index439 = 0
        # Program TableJoin Region
        while vec_index439 < len(vec_439):
            var_441 = vec_439[vec_index439]
            vec_index439 += 1
            tuple_440_0_index: int = 0
            tuple_440_0_vec: List[int] = self.index_414[var_441]
            while tuple_440_0_index < len(tuple_440_0_vec):
                tuple_440_0 = tuple_440_0_vec[tuple_440_0_index]
                tuple_440_0_index += 1
                var_442 = tuple_440_0
                tuple_440_1_index: int = 0
                tuple_440_1_vec: List[int] = self.index_415[var_441]
                while tuple_440_1_index < len(tuple_440_1_vec):
                    tuple_440_1 = tuple_440_1_vec[tuple_440_1_index]
                    tuple_440_1_index += 1
                    var_443 = tuple_440_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_1030_(var_442, var_441)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_1033_(var_441, var_443)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_426_(var_442, var_443)
                            if not ret:
                                # Program TransitionState Region
                                tuple_442_443 = (var_442, var_443)
                                prev_state = self.table_6[tuple_442_443]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_442_443] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_442_443[1]].append(tuple_442_443[0])
                                        self.index_1029[tuple_442_443[0]].append(tuple_442_443[1])
                                    # Program VectorAppend Region
                                    vec_193.append((var_442, var_443))
        # Program VectorClear Region
        del vec_439[:]
        vec_index439 = 0
        # Program VectorClear Region
        del vec_436[:]
        vec_index436 = 0
        # Program Return Region
        param_0[0] = vec_193
        return False

    def proc_203_(self, var_204: int, var_205: int, var_206: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_205_204 = (var_205, var_204)
        prev_state = self.table_9[tuple_205_204]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_9[tuple_205_204] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1114_(var_205, var_204)

            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1110_(var_205, var_204)

        # Program Return Region
        return False

    def proc_273_(self, var_274: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1091_(var_274)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_276_(self, var_277: int, var_278: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_9[(var_277, var_278)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_277_278 = (var_277, var_278)
            prev_state = self.table_9[tuple_277_278]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_9[tuple_277_278] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1049_(var_278, var_277)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_277_278 = (var_277, var_278)
                    prev_state = self.table_9[tuple_277_278]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_277_278] = 1 | 4
                        if not present_bit:
                            self.index_415[tuple_277_278[0]].append(tuple_277_278[1])
                            self.index_1079[tuple_277_278[1]].append(tuple_277_278[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False

    def proc_426_(self, var_427: int, var_428: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_427, var_428)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_427_428 = (var_427, var_428)
            prev_state = self.table_6[tuple_427_428]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_427_428] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1074_(var_427, var_428)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_427_428 = (var_427, var_428)
                    prev_state = self.table_6[tuple_427_428]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_427_428] = 1 | 4
                        if not present_bit:
                            self.index_414[tuple_427_428[1]].append(tuple_427_428[0])
                            self.index_1029[tuple_427_428[0]].append(tuple_427_428[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False

    def external_symbol_2(self, vec_450: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index450: int = 0
        vec_453: List[int] = list()
        vec_index453: int = 0
        vec_462: List[Tuple[int, int]] = list()
        vec_index462: int = 0
        vec_465: List[Tuple[int, int]] = list()
        vec_index465: int = 0
        vec_469: List[int] = list()
        vec_index469: int = 0
        vec_480: List[Tuple[int, int]] = list()
        vec_index480: int = 0
        vec_484: List[int] = list()
        vec_index484: int = 0
        vec_495: List[Tuple[int, int]] = list()
        vec_index495: int = 0
        vec_499: List[int] = list()
        vec_index499: int = 0
        vec_509: List[Tuple[int, int]] = list()
        vec_index509: int = 0
        vec_513: List[int] = list()
        vec_index513: int = 0
        vec_516: List[Tuple[int, int]] = list()
        vec_index516: int = 0
        vec_520: List[int] = list()
        vec_index520: int = 0
        vec_530: List[Tuple[int, int]] = list()
        vec_index530: int = 0
        vec_534: List[int] = list()
        vec_index534: int = 0
        vec_544: List[Tuple[int, int]] = list()
        vec_index544: int = 0
        vec_548: List[int] = list()
        vec_index548: int = 0
        vec_554: List[Tuple[int, int]] = list()
        vec_index554: int = 0
        vec_558: List[int] = list()
        vec_index558: int = 0
        vec_566: List[int] = list()
        vec_index566: int = 0
        vec_575: List[Tuple[int, int]] = list()
        vec_index575: int = 0
        vec_579: List[int] = list()
        vec_index579: int = 0
        vec_584: List[int] = list()
        vec_index584: int = 0
        vec_592: List[int] = list()
        vec_index592: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index450 = 0
        while vec_index450 < len(vec_450):
            var_451, var_452 = vec_450[vec_index450]
            vec_index450 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_451_452 = (var_451, var_452)
            prev_state = self.table_40[tuple_451_452]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_40[tuple_451_452] = 1 | 4
                if not present_bit:
                    self.index_372[tuple_451_452[0]].append(tuple_451_452[1])
                # Program Parallel Region
                # Program TransitionState Region
                tuple_451 = var_451
                prev_state = self.table_49[tuple_451]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_451] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_513.append(var_451)
                    # Program VectorAppend Region
                    vec_499.append(var_451)
                    # Program VectorAppend Region
                    vec_534.append(var_451)
                    # Program VectorAppend Region
                    vec_520.append(var_451)
                    # Program VectorAppend Region
                    vec_484.append(var_451)
                    # Program VectorAppend Region
                    vec_469.append(var_451)
                    # Program VectorAppend Region
                    vec_453.append(var_451)
                # Program VectorAppend Region
                vec_548.append(var_451)
                # Program VectorAppend Region
                vec_566.append(var_451)
                # Program VectorAppend Region
                vec_592.append(var_451)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_451_452 = (var_451, var_452)
            prev_state = self.table_40[tuple_451_452]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_40[tuple_451_452] = 1 | 4
                if not present_bit:
                    self.index_372[tuple_451_452[0]].append(tuple_451_452[1])
                # Program Parallel Region
                # Program TransitionState Region
                tuple_451 = var_451
                prev_state = self.table_49[tuple_451]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_451] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_513.append(var_451)
                    # Program VectorAppend Region
                    vec_499.append(var_451)
                    # Program VectorAppend Region
                    vec_534.append(var_451)
                    # Program VectorAppend Region
                    vec_520.append(var_451)
                    # Program VectorAppend Region
                    vec_484.append(var_451)
                    # Program VectorAppend Region
                    vec_469.append(var_451)
                    # Program VectorAppend Region
                    vec_453.append(var_451)
                # Program VectorAppend Region
                vec_548.append(var_451)
                # Program VectorAppend Region
                vec_566.append(var_451)
                # Program VectorAppend Region
                vec_592.append(var_451)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_451_452 = (var_451, var_452)
            prev_state = self.table_40[tuple_451_452]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_40[tuple_451_452] = 1 | 4
                if not present_bit:
                    self.index_372[tuple_451_452[0]].append(tuple_451_452[1])
                # Program Parallel Region
                # Program TransitionState Region
                tuple_451 = var_451
                prev_state = self.table_49[tuple_451]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_451] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_513.append(var_451)
                    # Program VectorAppend Region
                    vec_499.append(var_451)
                    # Program VectorAppend Region
                    vec_534.append(var_451)
                    # Program VectorAppend Region
                    vec_520.append(var_451)
                    # Program VectorAppend Region
                    vec_484.append(var_451)
                    # Program VectorAppend Region
                    vec_469.append(var_451)
                    # Program VectorAppend Region
                    vec_453.append(var_451)
                # Program VectorAppend Region
                vec_548.append(var_451)
                # Program VectorAppend Region
                vec_566.append(var_451)
                # Program VectorAppend Region
                vec_592.append(var_451)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_451_452 = (var_451, var_452)
            prev_state = self.table_40[tuple_451_452]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_40[tuple_451_452] = 1 | 4
                if not present_bit:
                    self.index_372[tuple_451_452[0]].append(tuple_451_452[1])
                # Program Parallel Region
                # Program TransitionState Region
                tuple_451 = var_451
                prev_state = self.table_49[tuple_451]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_49[tuple_451] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_513.append(var_451)
                    # Program VectorAppend Region
                    vec_499.append(var_451)
                    # Program VectorAppend Region
                    vec_534.append(var_451)
                    # Program VectorAppend Region
                    vec_520.append(var_451)
                    # Program VectorAppend Region
                    vec_484.append(var_451)
                    # Program VectorAppend Region
                    vec_469.append(var_451)
                    # Program VectorAppend Region
                    vec_453.append(var_451)
                # Program VectorAppend Region
                vec_548.append(var_451)
                # Program VectorAppend Region
                vec_566.append(var_451)
                # Program VectorAppend Region
                vec_592.append(var_451)
        # Program VectorUnique Region
        vec_453 = list(set(vec_453))
        vec_index453 = 0
        # Program TableJoin Region
        while vec_index453 < len(vec_453):
            var_455 = vec_453[vec_index453]
            vec_index453 += 1
            if var_455 in self.index_267:
                tuple_454_1_index: int = 0
                tuple_454_1_vec: List[Tuple[int, int, int]] = self.index_268[var_455]
                while tuple_454_1_index < len(tuple_454_1_vec):
                    tuple_454_1 = tuple_454_1_vec[tuple_454_1_index]
                    tuple_454_1_index += 1
                    var_456 = tuple_454_1[0]
                    var_457 = tuple_454_1[1]
                    var_458 = tuple_454_1[2]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_457, var_456, ):
                        # Program TransitionState Region
                        tuple_458_455_5 = (var_458, var_455, self.var_5)
                        prev_state = self.table_43[tuple_458_455_5]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_458_455_5] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_458_455_5[1]].append((tuple_458_455_5[0], tuple_458_455_5[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_455_458_5 = (var_455, var_458, self.var_5)
                            prev_state = self.table_26[tuple_455_458_5]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_455_458_5] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_455_458_5[0]].append((tuple_455_458_5[1], tuple_455_458_5[2]))
                                    self.index_1053[(tuple_455_458_5[0], tuple_455_458_5[1])].append(tuple_455_458_5[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_455)
                            if not ret:
                                # Program TransitionState Region
                                tuple_455_458_5 = (var_455, var_458, self.var_5)
                                prev_state = self.table_26[tuple_455_458_5]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_455_458_5] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_455_458_5[0]].append((tuple_455_458_5[1], tuple_455_458_5[2]))
                                        self.index_1053[(tuple_455_458_5[0], tuple_455_458_5[1])].append(tuple_455_458_5[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_458, var_455)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_458_455 = (var_458, var_455)
                                        prev_state = self.table_9[tuple_458_455]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_458_455] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_458_455[0]].append(tuple_458_455[1])
                                                self.index_1079[tuple_458_455[1]].append(tuple_458_455[0])
                                            # Program VectorAppend Region
                                            vec_584.append(var_458)
                            # Program VectorAppend Region
                            vec_548.append(var_455)
                            # Program VectorAppend Region
                            vec_579.append(var_455)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_5:
                                # Program TransitionState Region
                                tuple_455 = var_455
                                prev_state = self.table_17[tuple_455]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_455] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_465: Tuple[int, int]
                                    scan_index_465: int = 0
                                    scan_tuple_465_vec: List[Tuple[int, int]] = self.index_199[var_455]
                                    while scan_index_465 < len(scan_tuple_465_vec):
                                        scan_tuple_465 = scan_tuple_465_vec[scan_index_465]
                                        scan_index_465 += 1
                                        vec_465.append(scan_tuple_465)
                                    # Program VectorLoop Region
                                    vec_index465 = 0
                                    while vec_index465 < len(vec_465):
                                        var_466, var_467 = vec_465[vec_index465]
                                        vec_index465 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_467 = self._resolve_edgetype(var_467)
                                        tuple_455_466_467 = (var_455, var_466, var_467)
                                        prev_state = self.table_26[tuple_455_466_467]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_455_466_467] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_455, var_466, var_467)

                                    # Program TransitionState Region
                                    tuple_455_455 = (var_455, var_455)
                                    prev_state = self.table_6[tuple_455_455]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_455_455] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_455_455[1]].append(tuple_455_455[0])
                                            self.index_1029[tuple_455_455[0]].append(tuple_455_455[1])
                                        # Program VectorAppend Region
                                        vec_462.append((var_455, var_455))
                                    # Program VectorAppend Region
                                    vec_579.append(var_455)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_5:
                                # Program TransitionState Region
                                tuple_2_458_455 = (self.var_2, var_458, var_455)
                                prev_state = self.table_56[tuple_2_458_455]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_458_455] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_2_458_455[1]].append((tuple_2_458_455[0], tuple_2_458_455[2]))
                                    # Program VectorAppend Region
                                    vec_558.append(var_458)
        # Program VectorClear Region
        del vec_453[:]
        vec_index453 = 0
        # Program VectorUnique Region
        vec_469 = list(set(vec_469))
        vec_index469 = 0
        # Program TableJoin Region
        while vec_index469 < len(vec_469):
            var_471 = vec_469[vec_index469]
            vec_index469 += 1
            if var_471 in self.index_267:
                tuple_470_1_index: int = 0
                tuple_470_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_287[var_471]
                while tuple_470_1_index < len(tuple_470_1_vec):
                    tuple_470_1 = tuple_470_1_vec[tuple_470_1_index]
                    tuple_470_1_index += 1
                    var_472 = tuple_470_1[0]
                    var_473 = tuple_470_1[1]
                    var_474 = tuple_470_1[2]
                    var_475 = tuple_470_1[3]
                    var_476 = tuple_470_1[4]
                    # Program TupleCompare Region
                    if self.var_4 == var_472:
                        # Program TransitionState Region
                        tuple_474_471_0 = (var_474, var_471, self.var_0)
                        prev_state = self.table_43[tuple_474_471_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_474_471_0] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_474_471_0[1]].append((tuple_474_471_0[0], tuple_474_471_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_471_474_0 = (var_471, var_474, self.var_0)
                            prev_state = self.table_26[tuple_471_474_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_471_474_0] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_471_474_0[0]].append((tuple_471_474_0[1], tuple_471_474_0[2]))
                                    self.index_1053[(tuple_471_474_0[0], tuple_471_474_0[1])].append(tuple_471_474_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_471)
                            if not ret:
                                # Program TransitionState Region
                                tuple_471_474_0 = (var_471, var_474, self.var_0)
                                prev_state = self.table_26[tuple_471_474_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_471_474_0] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_471_474_0[0]].append((tuple_471_474_0[1], tuple_471_474_0[2]))
                                        self.index_1053[(tuple_471_474_0[0], tuple_471_474_0[1])].append(tuple_471_474_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_474, var_471)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_474_471 = (var_474, var_471)
                                        prev_state = self.table_9[tuple_474_471]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_474_471] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_474_471[0]].append(tuple_474_471[1])
                                                self.index_1079[tuple_474_471[1]].append(tuple_474_471[0])
                                            # Program VectorAppend Region
                                            vec_584.append(var_474)
                            # Program VectorAppend Region
                            vec_548.append(var_471)
                            # Program VectorAppend Region
                            vec_579.append(var_471)
                            # Program TransitionState Region
                            tuple_471 = var_471
                            prev_state = self.table_17[tuple_471]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_17[tuple_471] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_480: Tuple[int, int]
                                scan_index_480: int = 0
                                scan_tuple_480_vec: List[Tuple[int, int]] = self.index_199[var_471]
                                while scan_index_480 < len(scan_tuple_480_vec):
                                    scan_tuple_480 = scan_tuple_480_vec[scan_index_480]
                                    scan_index_480 += 1
                                    vec_480.append(scan_tuple_480)
                                # Program VectorLoop Region
                                vec_index480 = 0
                                while vec_index480 < len(vec_480):
                                    var_481, var_482 = vec_480[vec_index480]
                                    vec_index480 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_482 = self._resolve_edgetype(var_482)
                                    tuple_471_481_482 = (var_471, var_481, var_482)
                                    prev_state = self.table_26[tuple_471_481_482]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_471_481_482] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_203_(var_471, var_481, var_482)

                                # Program TransitionState Region
                                tuple_471_471 = (var_471, var_471)
                                prev_state = self.table_6[tuple_471_471]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_471_471] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_471_471[1]].append(tuple_471_471[0])
                                        self.index_1029[tuple_471_471[0]].append(tuple_471_471[1])
                                    # Program VectorAppend Region
                                    vec_462.append((var_471, var_471))
                                # Program VectorAppend Region
                                vec_579.append(var_471)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_474_471 = (self.var_0, var_474, var_471)
                                prev_state = self.table_56[tuple_0_474_471]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_474_471] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_0_474_471[1]].append((tuple_0_474_471[0], tuple_0_474_471[2]))
                                    # Program VectorAppend Region
                                    vec_558.append(var_474)
        # Program VectorClear Region
        del vec_469[:]
        vec_index469 = 0
        # Program VectorUnique Region
        vec_484 = list(set(vec_484))
        vec_index484 = 0
        # Program TableJoin Region
        while vec_index484 < len(vec_484):
            var_486 = vec_484[vec_index484]
            vec_index484 += 1
            if var_486 in self.index_267:
                tuple_485_1_index: int = 0
                tuple_485_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_303[var_486]
                while tuple_485_1_index < len(tuple_485_1_vec):
                    tuple_485_1 = tuple_485_1_vec[tuple_485_1_index]
                    tuple_485_1_index += 1
                    var_487 = tuple_485_1[0]
                    var_488 = tuple_485_1[1]
                    var_489 = tuple_485_1[2]
                    var_490 = tuple_485_1[3]
                    var_491 = tuple_485_1[4]
                    # Program TupleCompare Region
                    if self.var_1 == var_487:
                        # Program TransitionState Region
                        tuple_489_486_2 = (var_489, var_486, self.var_2)
                        prev_state = self.table_43[tuple_489_486_2]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_489_486_2] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_489_486_2[1]].append((tuple_489_486_2[0], tuple_489_486_2[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_486_489_2 = (var_486, var_489, self.var_2)
                            prev_state = self.table_26[tuple_486_489_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_486_489_2] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_486_489_2[0]].append((tuple_486_489_2[1], tuple_486_489_2[2]))
                                    self.index_1053[(tuple_486_489_2[0], tuple_486_489_2[1])].append(tuple_486_489_2[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_486)
                            if not ret:
                                # Program TransitionState Region
                                tuple_486_489_2 = (var_486, var_489, self.var_2)
                                prev_state = self.table_26[tuple_486_489_2]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_486_489_2] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_486_489_2[0]].append((tuple_486_489_2[1], tuple_486_489_2[2]))
                                        self.index_1053[(tuple_486_489_2[0], tuple_486_489_2[1])].append(tuple_486_489_2[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_489, var_486)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_489_486 = (var_489, var_486)
                                        prev_state = self.table_9[tuple_489_486]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_489_486] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_489_486[0]].append(tuple_489_486[1])
                                                self.index_1079[tuple_489_486[1]].append(tuple_489_486[0])
                                            # Program VectorAppend Region
                                            vec_584.append(var_489)
                            # Program VectorAppend Region
                            vec_548.append(var_486)
                            # Program VectorAppend Region
                            vec_579.append(var_486)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_486 = var_486
                                prev_state = self.table_17[tuple_486]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_486] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_495: Tuple[int, int]
                                    scan_index_495: int = 0
                                    scan_tuple_495_vec: List[Tuple[int, int]] = self.index_199[var_486]
                                    while scan_index_495 < len(scan_tuple_495_vec):
                                        scan_tuple_495 = scan_tuple_495_vec[scan_index_495]
                                        scan_index_495 += 1
                                        vec_495.append(scan_tuple_495)
                                    # Program VectorLoop Region
                                    vec_index495 = 0
                                    while vec_index495 < len(vec_495):
                                        var_496, var_497 = vec_495[vec_index495]
                                        vec_index495 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_497 = self._resolve_edgetype(var_497)
                                        tuple_486_496_497 = (var_486, var_496, var_497)
                                        prev_state = self.table_26[tuple_486_496_497]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_486_496_497] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_486, var_496, var_497)

                                    # Program TransitionState Region
                                    tuple_486_486 = (var_486, var_486)
                                    prev_state = self.table_6[tuple_486_486]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_486_486] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_486_486[1]].append(tuple_486_486[0])
                                            self.index_1029[tuple_486_486[0]].append(tuple_486_486[1])
                                        # Program VectorAppend Region
                                        vec_462.append((var_486, var_486))
                                    # Program VectorAppend Region
                                    vec_579.append(var_486)
                            # Program TransitionState Region
                            tuple_2_489_486 = (self.var_2, var_489, var_486)
                            prev_state = self.table_56[tuple_2_489_486]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_56[tuple_2_489_486] = 1 | 4
                                if not present_bit:
                                    self.index_385[tuple_2_489_486[1]].append((tuple_2_489_486[0], tuple_2_489_486[2]))
                                # Program VectorAppend Region
                                vec_558.append(var_489)
        # Program VectorClear Region
        del vec_484[:]
        vec_index484 = 0
        # Program VectorUnique Region
        vec_499 = list(set(vec_499))
        vec_index499 = 0
        # Program TableJoin Region
        while vec_index499 < len(vec_499):
            var_501 = vec_499[vec_index499]
            vec_index499 += 1
            tuple_500_0_index: int = 0
            tuple_500_0_vec: List[Tuple[int, int, int, int]] = self.index_319[var_501]
            while tuple_500_0_index < len(tuple_500_0_vec):
                tuple_500_0 = tuple_500_0_vec[tuple_500_0_index]
                tuple_500_0_index += 1
                var_502 = tuple_500_0[0]
                var_503 = tuple_500_0[1]
                var_504 = tuple_500_0[2]
                var_505 = tuple_500_0[3]
                if var_501 in self.index_267:
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_504, var_503, ):
                        # Program TransitionState Region
                        var_502 = self._resolve_edgetype(var_502)
                        tuple_505_501_502 = (var_505, var_501, var_502)
                        prev_state = self.table_43[tuple_505_501_502]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_505_501_502] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_505_501_502[1]].append((tuple_505_501_502[0], tuple_505_501_502[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            var_502 = self._resolve_edgetype(var_502)
                            tuple_501_505_502 = (var_501, var_505, var_502)
                            prev_state = self.table_26[tuple_501_505_502]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_501_505_502] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_501_505_502[0]].append((tuple_501_505_502[1], tuple_501_505_502[2]))
                                    self.index_1053[(tuple_501_505_502[0], tuple_501_505_502[1])].append(tuple_501_505_502[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_501)
                            if not ret:
                                # Program TransitionState Region
                                var_502 = self._resolve_edgetype(var_502)
                                tuple_501_505_502 = (var_501, var_505, var_502)
                                prev_state = self.table_26[tuple_501_505_502]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_501_505_502] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_501_505_502[0]].append((tuple_501_505_502[1], tuple_501_505_502[2]))
                                        self.index_1053[(tuple_501_505_502[0], tuple_501_505_502[1])].append(tuple_501_505_502[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_505, var_501)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_505_501 = (var_505, var_501)
                                        prev_state = self.table_9[tuple_505_501]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_505_501] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_505_501[0]].append(tuple_505_501[1])
                                                self.index_1079[tuple_505_501[1]].append(tuple_505_501[0])
                                            # Program VectorAppend Region
                                            vec_584.append(var_505)
                            # Program VectorAppend Region
                            vec_548.append(var_501)
                            # Program VectorAppend Region
                            vec_579.append(var_501)
                            # Program TupleCompare Region
                            if self.var_0 == var_502:
                                # Program TransitionState Region
                                tuple_501 = var_501
                                prev_state = self.table_17[tuple_501]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_501] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_509: Tuple[int, int]
                                    scan_index_509: int = 0
                                    scan_tuple_509_vec: List[Tuple[int, int]] = self.index_199[var_501]
                                    while scan_index_509 < len(scan_tuple_509_vec):
                                        scan_tuple_509 = scan_tuple_509_vec[scan_index_509]
                                        scan_index_509 += 1
                                        vec_509.append(scan_tuple_509)
                                    # Program VectorLoop Region
                                    vec_index509 = 0
                                    while vec_index509 < len(vec_509):
                                        var_510, var_511 = vec_509[vec_index509]
                                        vec_index509 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_511 = self._resolve_edgetype(var_511)
                                        tuple_501_510_511 = (var_501, var_510, var_511)
                                        prev_state = self.table_26[tuple_501_510_511]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_501_510_511] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_501, var_510, var_511)

                                    # Program TransitionState Region
                                    tuple_501_501 = (var_501, var_501)
                                    prev_state = self.table_6[tuple_501_501]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_501_501] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_501_501[1]].append(tuple_501_501[0])
                                            self.index_1029[tuple_501_501[0]].append(tuple_501_501[1])
                                        # Program VectorAppend Region
                                        vec_462.append((var_501, var_501))
                                    # Program VectorAppend Region
                                    vec_579.append(var_501)
                            # Program TupleCompare Region
                            if self.var_2 == var_502:
                                # Program TransitionState Region
                                tuple_2_505_501 = (self.var_2, var_505, var_501)
                                prev_state = self.table_56[tuple_2_505_501]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_505_501] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_2_505_501[1]].append((tuple_2_505_501[0], tuple_2_505_501[2]))
                                    # Program VectorAppend Region
                                    vec_558.append(var_505)
        # Program VectorClear Region
        del vec_499[:]
        vec_index499 = 0
        # Program VectorUnique Region
        vec_513 = list(set(vec_513))
        vec_index513 = 0
        # Program TableJoin Region
        while vec_index513 < len(vec_513):
            var_515 = vec_513[vec_index513]
            vec_index513 += 1
            if var_515 in self.index_334:
                if var_515 in self.index_267:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_515 = var_515
                    prev_state = self.table_17[tuple_515]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_515] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_516: Tuple[int, int]
                        scan_index_516: int = 0
                        scan_tuple_516_vec: List[Tuple[int, int]] = self.index_199[var_515]
                        while scan_index_516 < len(scan_tuple_516_vec):
                            scan_tuple_516 = scan_tuple_516_vec[scan_index_516]
                            scan_index_516 += 1
                            vec_516.append(scan_tuple_516)
                        # Program VectorLoop Region
                        vec_index516 = 0
                        while vec_index516 < len(vec_516):
                            var_517, var_518 = vec_516[vec_index516]
                            vec_index516 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_518 = self._resolve_edgetype(var_518)
                            tuple_515_517_518 = (var_515, var_517, var_518)
                            prev_state = self.table_26[tuple_515_517_518]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_515_517_518] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_515, var_517, var_518)

                        # Program TransitionState Region
                        tuple_515_515 = (var_515, var_515)
                        prev_state = self.table_6[tuple_515_515]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_515_515] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_515_515[1]].append(tuple_515_515[0])
                                self.index_1029[tuple_515_515[0]].append(tuple_515_515[1])
                            # Program VectorAppend Region
                            vec_462.append((var_515, var_515))
                        # Program VectorAppend Region
                        vec_579.append(var_515)
        # Program VectorClear Region
        del vec_513[:]
        vec_index513 = 0
        # Program VectorUnique Region
        vec_520 = list(set(vec_520))
        vec_index520 = 0
        # Program TableJoin Region
        while vec_index520 < len(vec_520):
            var_522 = vec_520[vec_index520]
            vec_index520 += 1
            if var_522 in self.index_267:
                tuple_521_1_index: int = 0
                tuple_521_1_vec: List[Tuple[int, int, int, int]] = self.index_342[var_522]
                while tuple_521_1_index < len(tuple_521_1_vec):
                    tuple_521_1 = tuple_521_1_vec[tuple_521_1_index]
                    tuple_521_1_index += 1
                    var_523 = tuple_521_1[0]
                    var_524 = tuple_521_1[1]
                    var_525 = tuple_521_1[2]
                    var_526 = tuple_521_1[3]
                    # Program TupleCompare Region
                    if (self.var_3, self.var_0, ) == (var_524, var_525, ):
                        # Program TransitionState Region
                        tuple_526_522_3 = (var_526, var_522, self.var_3)
                        prev_state = self.table_43[tuple_526_522_3]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_526_522_3] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_526_522_3[1]].append((tuple_526_522_3[0], tuple_526_522_3[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_522_526_3 = (var_522, var_526, self.var_3)
                            prev_state = self.table_26[tuple_522_526_3]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_522_526_3] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_522_526_3[0]].append((tuple_522_526_3[1], tuple_522_526_3[2]))
                                    self.index_1053[(tuple_522_526_3[0], tuple_522_526_3[1])].append(tuple_522_526_3[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_522)
                            if not ret:
                                # Program TransitionState Region
                                tuple_522_526_3 = (var_522, var_526, self.var_3)
                                prev_state = self.table_26[tuple_522_526_3]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_522_526_3] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_522_526_3[0]].append((tuple_522_526_3[1], tuple_522_526_3[2]))
                                        self.index_1053[(tuple_522_526_3[0], tuple_522_526_3[1])].append(tuple_522_526_3[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_526, var_522)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_526_522 = (var_526, var_522)
                                        prev_state = self.table_9[tuple_526_522]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_526_522] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_526_522[0]].append(tuple_526_522[1])
                                                self.index_1079[tuple_526_522[1]].append(tuple_526_522[0])
                                            # Program VectorAppend Region
                                            vec_584.append(var_526)
                            # Program VectorAppend Region
                            vec_548.append(var_522)
                            # Program VectorAppend Region
                            vec_579.append(var_522)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_3:
                                # Program TransitionState Region
                                tuple_522 = var_522
                                prev_state = self.table_17[tuple_522]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_522] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_530: Tuple[int, int]
                                    scan_index_530: int = 0
                                    scan_tuple_530_vec: List[Tuple[int, int]] = self.index_199[var_522]
                                    while scan_index_530 < len(scan_tuple_530_vec):
                                        scan_tuple_530 = scan_tuple_530_vec[scan_index_530]
                                        scan_index_530 += 1
                                        vec_530.append(scan_tuple_530)
                                    # Program VectorLoop Region
                                    vec_index530 = 0
                                    while vec_index530 < len(vec_530):
                                        var_531, var_532 = vec_530[vec_index530]
                                        vec_index530 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_532 = self._resolve_edgetype(var_532)
                                        tuple_522_531_532 = (var_522, var_531, var_532)
                                        prev_state = self.table_26[tuple_522_531_532]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_522_531_532] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_522, var_531, var_532)

                                    # Program TransitionState Region
                                    tuple_522_522 = (var_522, var_522)
                                    prev_state = self.table_6[tuple_522_522]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_522_522] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_522_522[1]].append(tuple_522_522[0])
                                            self.index_1029[tuple_522_522[0]].append(tuple_522_522[1])
                                        # Program VectorAppend Region
                                        vec_462.append((var_522, var_522))
                                    # Program VectorAppend Region
                                    vec_579.append(var_522)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_3:
                                # Program TransitionState Region
                                tuple_2_526_522 = (self.var_2, var_526, var_522)
                                prev_state = self.table_56[tuple_2_526_522]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_526_522] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_2_526_522[1]].append((tuple_2_526_522[0], tuple_2_526_522[2]))
                                    # Program VectorAppend Region
                                    vec_558.append(var_526)
        # Program VectorClear Region
        del vec_520[:]
        vec_index520 = 0
        # Program VectorUnique Region
        vec_534 = list(set(vec_534))
        vec_index534 = 0
        # Program TableJoin Region
        while vec_index534 < len(vec_534):
            var_536 = vec_534[vec_index534]
            vec_index534 += 1
            if var_536 in self.index_267:
                tuple_535_1_index: int = 0
                tuple_535_1_vec: List[Tuple[int, int, int, int]] = self.index_357[var_536]
                while tuple_535_1_index < len(tuple_535_1_vec):
                    tuple_535_1 = tuple_535_1_vec[tuple_535_1_index]
                    tuple_535_1_index += 1
                    var_537 = tuple_535_1[0]
                    var_538 = tuple_535_1[1]
                    var_539 = tuple_535_1[2]
                    var_540 = tuple_535_1[3]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_539, var_538, ):
                        # Program TransitionState Region
                        tuple_540_536_0 = (var_540, var_536, self.var_0)
                        prev_state = self.table_43[tuple_540_536_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_540_536_0] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_540_536_0[1]].append((tuple_540_536_0[0], tuple_540_536_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_536_540_0 = (var_536, var_540, self.var_0)
                            prev_state = self.table_26[tuple_536_540_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_536_540_0] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_536_540_0[0]].append((tuple_536_540_0[1], tuple_536_540_0[2]))
                                    self.index_1053[(tuple_536_540_0[0], tuple_536_540_0[1])].append(tuple_536_540_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_536)
                            if not ret:
                                # Program TransitionState Region
                                tuple_536_540_0 = (var_536, var_540, self.var_0)
                                prev_state = self.table_26[tuple_536_540_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_536_540_0] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_536_540_0[0]].append((tuple_536_540_0[1], tuple_536_540_0[2]))
                                        self.index_1053[(tuple_536_540_0[0], tuple_536_540_0[1])].append(tuple_536_540_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_540, var_536)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_540_536 = (var_540, var_536)
                                        prev_state = self.table_9[tuple_540_536]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_540_536] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_540_536[0]].append(tuple_540_536[1])
                                                self.index_1079[tuple_540_536[1]].append(tuple_540_536[0])
                                            # Program VectorAppend Region
                                            vec_584.append(var_540)
                            # Program VectorAppend Region
                            vec_548.append(var_536)
                            # Program VectorAppend Region
                            vec_579.append(var_536)
                            # Program TransitionState Region
                            tuple_536 = var_536
                            prev_state = self.table_17[tuple_536]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_17[tuple_536] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_544: Tuple[int, int]
                                scan_index_544: int = 0
                                scan_tuple_544_vec: List[Tuple[int, int]] = self.index_199[var_536]
                                while scan_index_544 < len(scan_tuple_544_vec):
                                    scan_tuple_544 = scan_tuple_544_vec[scan_index_544]
                                    scan_index_544 += 1
                                    vec_544.append(scan_tuple_544)
                                # Program VectorLoop Region
                                vec_index544 = 0
                                while vec_index544 < len(vec_544):
                                    var_545, var_546 = vec_544[vec_index544]
                                    vec_index544 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_546 = self._resolve_edgetype(var_546)
                                    tuple_536_545_546 = (var_536, var_545, var_546)
                                    prev_state = self.table_26[tuple_536_545_546]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_536_545_546] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_203_(var_536, var_545, var_546)

                                # Program TransitionState Region
                                tuple_536_536 = (var_536, var_536)
                                prev_state = self.table_6[tuple_536_536]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_536_536] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_536_536[1]].append(tuple_536_536[0])
                                        self.index_1029[tuple_536_536[0]].append(tuple_536_536[1])
                                    # Program VectorAppend Region
                                    vec_462.append((var_536, var_536))
                                # Program VectorAppend Region
                                vec_579.append(var_536)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_540_536 = (self.var_0, var_540, var_536)
                                prev_state = self.table_56[tuple_0_540_536]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_540_536] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_0_540_536[1]].append((tuple_0_540_536[0], tuple_0_540_536[2]))
                                    # Program VectorAppend Region
                                    vec_558.append(var_540)
        # Program VectorClear Region
        del vec_534[:]
        vec_index534 = 0
        # Program VectorUnique Region
        vec_548 = list(set(vec_548))
        vec_index548 = 0
        # Program TableJoin Region
        while vec_index548 < len(vec_548):
            var_550 = vec_548[vec_index548]
            vec_index548 += 1
            tuple_549_0_index: int = 0
            tuple_549_0_vec: List[bytes] = self.index_372[var_550]
            while tuple_549_0_index < len(tuple_549_0_vec):
                tuple_549_0 = tuple_549_0_vec[tuple_549_0_index]
                tuple_549_0_index += 1
                var_551 = tuple_549_0
                tuple_549_1_index: int = 0
                tuple_549_1_vec: List[Tuple[int, int]] = self.index_373[var_550]
                while tuple_549_1_index < len(tuple_549_1_vec):
                    tuple_549_1 = tuple_549_1_vec[tuple_549_1_index]
                    tuple_549_1_index += 1
                    var_552 = tuple_549_1[0]
                    var_553 = tuple_549_1[1]
                    # Program TransitionState Region
                    tuple_550 = var_550
                    prev_state = self.table_17[tuple_550]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_550] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_554: Tuple[int, int]
                        scan_index_554: int = 0
                        scan_tuple_554_vec: List[Tuple[int, int]] = self.index_199[var_550]
                        while scan_index_554 < len(scan_tuple_554_vec):
                            scan_tuple_554 = scan_tuple_554_vec[scan_index_554]
                            scan_index_554 += 1
                            vec_554.append(scan_tuple_554)
                        # Program VectorLoop Region
                        vec_index554 = 0
                        while vec_index554 < len(vec_554):
                            var_555, var_556 = vec_554[vec_index554]
                            vec_index554 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_556 = self._resolve_edgetype(var_556)
                            tuple_550_555_556 = (var_550, var_555, var_556)
                            prev_state = self.table_26[tuple_550_555_556]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_550_555_556] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_550, var_555, var_556)

                        # Program TransitionState Region
                        tuple_550_550 = (var_550, var_550)
                        prev_state = self.table_6[tuple_550_550]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_550_550] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_550_550[1]].append(tuple_550_550[0])
                                self.index_1029[tuple_550_550[0]].append(tuple_550_550[1])
                            # Program VectorAppend Region
                            vec_462.append((var_550, var_550))
                        # Program VectorAppend Region
                        vec_579.append(var_550)
        # Program VectorClear Region
        del vec_548[:]
        vec_index548 = 0
        # Program VectorUnique Region
        vec_558 = list(set(vec_558))
        vec_index558 = 0
        # Program TableJoin Region
        while vec_index558 < len(vec_558):
            var_560 = vec_558[vec_index558]
            vec_index558 += 1
            tuple_559_0_index: int = 0
            tuple_559_0_vec: List[Tuple[int, bytes, bytes]] = self.index_384[var_560]
            while tuple_559_0_index < len(tuple_559_0_vec):
                tuple_559_0 = tuple_559_0_vec[tuple_559_0_index]
                tuple_559_0_index += 1
                var_561 = tuple_559_0[0]
                var_562 = tuple_559_0[1]
                var_563 = tuple_559_0[2]
                tuple_559_1_index: int = 0
                tuple_559_1_vec: List[Tuple[int, int]] = self.index_385[var_560]
                while tuple_559_1_index < len(tuple_559_1_vec):
                    tuple_559_1 = tuple_559_1_vec[tuple_559_1_index]
                    tuple_559_1_index += 1
                    var_564 = tuple_559_1[0]
                    var_565 = tuple_559_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_561, var_564, ):
                        # Program TransitionState Region
                        tuple_2_1_560_562_563_565 = (self.var_2, self.var_1, var_560, var_562, var_563, var_565)
                        prev_state = self.table_60[tuple_2_1_560_562_563_565]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_560_562_563_565] = 1 | 4
                            if not present_bit:
                                self.index_394[tuple_2_1_560_562_563_565[5]].append((tuple_2_1_560_562_563_565[0], tuple_2_1_560_562_563_565[1], tuple_2_1_560_562_563_565[2], tuple_2_1_560_562_563_565[3], tuple_2_1_560_562_563_565[4]))
                            # Program VectorAppend Region
                            vec_566.append(var_565)
        # Program VectorClear Region
        del vec_558[:]
        vec_index558 = 0
        # Program VectorUnique Region
        vec_566 = list(set(vec_566))
        vec_index566 = 0
        # Program TableJoin Region
        while vec_index566 < len(vec_566):
            var_568 = vec_566[vec_index566]
            vec_index566 += 1
            tuple_567_0_index: int = 0
            tuple_567_0_vec: List[bytes] = self.index_372[var_568]
            while tuple_567_0_index < len(tuple_567_0_vec):
                tuple_567_0 = tuple_567_0_vec[tuple_567_0_index]
                tuple_567_0_index += 1
                var_569 = tuple_567_0
                tuple_567_1_index: int = 0
                tuple_567_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_394[var_568]
                while tuple_567_1_index < len(tuple_567_1_vec):
                    tuple_567_1 = tuple_567_1_vec[tuple_567_1_index]
                    tuple_567_1_index += 1
                    var_570 = tuple_567_1[0]
                    var_571 = tuple_567_1[1]
                    var_572 = tuple_567_1[2]
                    var_573 = tuple_567_1[3]
                    var_574 = tuple_567_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_571, var_570, ):
                        # Program TransitionState Region
                        tuple_572 = var_572
                        prev_state = self.table_17[tuple_572]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_17[tuple_572] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_575: Tuple[int, int]
                            scan_index_575: int = 0
                            scan_tuple_575_vec: List[Tuple[int, int]] = self.index_199[var_572]
                            while scan_index_575 < len(scan_tuple_575_vec):
                                scan_tuple_575 = scan_tuple_575_vec[scan_index_575]
                                scan_index_575 += 1
                                vec_575.append(scan_tuple_575)
                            # Program VectorLoop Region
                            vec_index575 = 0
                            while vec_index575 < len(vec_575):
                                var_576, var_577 = vec_575[vec_index575]
                                vec_index575 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_577 = self._resolve_edgetype(var_577)
                                tuple_572_576_577 = (var_572, var_576, var_577)
                                prev_state = self.table_26[tuple_572_576_577]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_572_576_577] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_203_(var_572, var_576, var_577)

                            # Program TransitionState Region
                            tuple_572_572 = (var_572, var_572)
                            prev_state = self.table_6[tuple_572_572]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_572_572] = 1 | 4
                                if not present_bit:
                                    self.index_414[tuple_572_572[1]].append(tuple_572_572[0])
                                    self.index_1029[tuple_572_572[0]].append(tuple_572_572[1])
                                # Program VectorAppend Region
                                vec_462.append((var_572, var_572))
                            # Program VectorAppend Region
                            vec_579.append(var_572)
        # Program VectorClear Region
        del vec_566[:]
        vec_index566 = 0
        # Program VectorUnique Region
        vec_579 = list(set(vec_579))
        vec_index579 = 0
        # Program TableJoin Region
        while vec_index579 < len(vec_579):
            var_581 = vec_579[vec_index579]
            vec_index579 += 1
            tuple_580_0_index: int = 0
            tuple_580_0_vec: List[Tuple[int, int]] = self.index_373[var_581]
            while tuple_580_0_index < len(tuple_580_0_vec):
                tuple_580_0 = tuple_580_0_vec[tuple_580_0_index]
                tuple_580_0_index += 1
                var_582 = tuple_580_0[0]
                var_583 = tuple_580_0[1]
                if var_581 in self.index_408:
                    # Program TransitionState Region
                    tuple_582_581 = (var_582, var_581)
                    prev_state = self.table_12[tuple_582_581]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_582_581] = 1 | 4
                        if not present_bit:
                            self.index_433[tuple_582_581[1]].append(tuple_582_581[0])
                            self.index_1028[tuple_582_581[0]].append(tuple_582_581[1])
                        # Program VectorAppend Region
                        vec_592.append(var_581)
        # Program VectorClear Region
        del vec_579[:]
        vec_index579 = 0
        # Program VectorUnique Region
        vec_584 = list(set(vec_584))
        vec_index584 = 0
        # Program TableJoin Region
        while vec_index584 < len(vec_584):
            var_586 = vec_584[vec_index584]
            vec_index584 += 1
            tuple_585_0_index: int = 0
            tuple_585_0_vec: List[int] = self.index_414[var_586]
            while tuple_585_0_index < len(tuple_585_0_vec):
                tuple_585_0 = tuple_585_0_vec[tuple_585_0_index]
                tuple_585_0_index += 1
                var_587 = tuple_585_0
                tuple_585_1_index: int = 0
                tuple_585_1_vec: List[int] = self.index_415[var_586]
                while tuple_585_1_index < len(tuple_585_1_vec):
                    tuple_585_1 = tuple_585_1_vec[tuple_585_1_index]
                    tuple_585_1_index += 1
                    var_588 = tuple_585_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_1030_(var_587, var_586)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_1033_(var_586, var_588)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_426_(var_587, var_588)
                            if not ret:
                                # Program TransitionState Region
                                tuple_587_588 = (var_587, var_588)
                                prev_state = self.table_6[tuple_587_588]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_587_588] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_587_588[1]].append(tuple_587_588[0])
                                        self.index_1029[tuple_587_588[0]].append(tuple_587_588[1])
                                    # Program VectorAppend Region
                                    vec_462.append((var_587, var_588))
        # Program VectorClear Region
        del vec_584[:]
        vec_index584 = 0
        # Program VectorUnique Region
        vec_592 = list(set(vec_592))
        vec_index592 = 0
        # Program TableJoin Region
        while vec_index592 < len(vec_592):
            var_594 = vec_592[vec_index592]
            vec_index592 += 1
            tuple_593_0_index: int = 0
            tuple_593_0_vec: List[int] = self.index_433[var_594]
            while tuple_593_0_index < len(tuple_593_0_vec):
                tuple_593_0 = tuple_593_0_vec[tuple_593_0_index]
                tuple_593_0_index += 1
                var_595 = tuple_593_0
                tuple_593_1_index: int = 0
                tuple_593_1_vec: List[bytes] = self.index_372[var_594]
                while tuple_593_1_index < len(tuple_593_1_vec):
                    tuple_593_1 = tuple_593_1_vec[tuple_593_1_index]
                    tuple_593_1_index += 1
                    var_596 = tuple_593_1
                    # Program TransitionState Region
                    tuple_595 = var_595
                    prev_state = self.table_15[tuple_595]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_595] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_592[:]
        vec_index592 = 0
        # Induction Fixpoint Loop Region
        while len(vec_462):
            # Program Call Region
            param_464_0 = [vec_462]
            ret = self.proc_192_(param_464_0)
            vec_462 = param_464_0[0]

        vec_index462 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_462[:]
        vec_index462 = 0
        # Program Return Region
        return False

    def entrypoint_1(self, vec_598: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index598: int = 0
        vec_600: List[int] = list()
        vec_index600: int = 0
        vec_603: List[Tuple[int, int]] = list()
        vec_index603: int = 0
        vec_606: List[Tuple[int, int]] = list()
        vec_index606: int = 0
        vec_610: List[int] = list()
        vec_index610: int = 0
        vec_615: List[int] = list()
        vec_index615: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index598 = 0
        while vec_index598 < len(vec_598):
            var_599 = vec_598[vec_index598]
            vec_index598 += 1
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_599 = var_599
            prev_state = self.table_47[tuple_599]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_47[tuple_599] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_600.append(var_599)
        # Program VectorUnique Region
        vec_600 = list(set(vec_600))
        vec_index600 = 0
        # Program TableJoin Region
        while vec_index600 < len(vec_600):
            var_602 = vec_600[vec_index600]
            vec_index600 += 1
            if var_602 in self.index_334:
                if var_602 in self.index_267:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_602 = var_602
                    prev_state = self.table_17[tuple_602]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_602] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_606: Tuple[int, int]
                        scan_index_606: int = 0
                        scan_tuple_606_vec: List[Tuple[int, int]] = self.index_199[var_602]
                        while scan_index_606 < len(scan_tuple_606_vec):
                            scan_tuple_606 = scan_tuple_606_vec[scan_index_606]
                            scan_index_606 += 1
                            vec_606.append(scan_tuple_606)
                        # Program VectorLoop Region
                        vec_index606 = 0
                        while vec_index606 < len(vec_606):
                            var_607, var_608 = vec_606[vec_index606]
                            vec_index606 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_608 = self._resolve_edgetype(var_608)
                            tuple_602_607_608 = (var_602, var_607, var_608)
                            prev_state = self.table_26[tuple_602_607_608]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_602_607_608] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_602, var_607, var_608)

                        # Program TransitionState Region
                        tuple_602_602 = (var_602, var_602)
                        prev_state = self.table_6[tuple_602_602]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_602_602] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_602_602[1]].append(tuple_602_602[0])
                                self.index_1029[tuple_602_602[0]].append(tuple_602_602[1])
                            # Program VectorAppend Region
                            vec_603.append((var_602, var_602))
                        # Program VectorAppend Region
                        vec_610.append(var_602)
        # Program VectorClear Region
        del vec_600[:]
        vec_index600 = 0
        # Program VectorUnique Region
        vec_610 = list(set(vec_610))
        vec_index610 = 0
        # Program TableJoin Region
        while vec_index610 < len(vec_610):
            var_612 = vec_610[vec_index610]
            vec_index610 += 1
            tuple_611_0_index: int = 0
            tuple_611_0_vec: List[Tuple[int, int]] = self.index_373[var_612]
            while tuple_611_0_index < len(tuple_611_0_vec):
                tuple_611_0 = tuple_611_0_vec[tuple_611_0_index]
                tuple_611_0_index += 1
                var_613 = tuple_611_0[0]
                var_614 = tuple_611_0[1]
                if var_612 in self.index_408:
                    # Program TransitionState Region
                    tuple_613_612 = (var_613, var_612)
                    prev_state = self.table_12[tuple_613_612]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_613_612] = 1 | 4
                        if not present_bit:
                            self.index_433[tuple_613_612[1]].append(tuple_613_612[0])
                            self.index_1028[tuple_613_612[0]].append(tuple_613_612[1])
                        # Program VectorAppend Region
                        vec_615.append(var_612)
        # Program VectorClear Region
        del vec_610[:]
        vec_index610 = 0
        # Program VectorUnique Region
        vec_615 = list(set(vec_615))
        vec_index615 = 0
        # Program TableJoin Region
        while vec_index615 < len(vec_615):
            var_617 = vec_615[vec_index615]
            vec_index615 += 1
            tuple_616_0_index: int = 0
            tuple_616_0_vec: List[int] = self.index_433[var_617]
            while tuple_616_0_index < len(tuple_616_0_vec):
                tuple_616_0 = tuple_616_0_vec[tuple_616_0_index]
                tuple_616_0_index += 1
                var_618 = tuple_616_0
                tuple_616_1_index: int = 0
                tuple_616_1_vec: List[bytes] = self.index_372[var_617]
                while tuple_616_1_index < len(tuple_616_1_vec):
                    tuple_616_1 = tuple_616_1_vec[tuple_616_1_index]
                    tuple_616_1_index += 1
                    var_619 = tuple_616_1
                    # Program TransitionState Region
                    tuple_618 = var_618
                    prev_state = self.table_15[tuple_618]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_618] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_615[:]
        vec_index615 = 0
        # Induction Fixpoint Loop Region
        while len(vec_603):
            # Program Call Region
            param_605_0 = [vec_603]
            ret = self.proc_192_(param_605_0)
            vec_603 = param_605_0[0]

        vec_index603 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_603[:]
        vec_index603 = 0
        # Program Return Region
        return False

    def constructor_function_1(self, vec_621: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index621: int = 0
        vec_623: List[int] = list()
        vec_index623: int = 0
        vec_629: List[Tuple[int, int]] = list()
        vec_index629: int = 0
        vec_632: List[Tuple[int, int]] = list()
        vec_index632: int = 0
        vec_636: List[int] = list()
        vec_index636: int = 0
        vec_641: List[int] = list()
        vec_index641: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index621 = 0
        while vec_index621 < len(vec_621):
            var_622 = vec_621[vec_index621]
            vec_index621 += 1
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_622 = var_622
            prev_state = self.table_67[tuple_622]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_67[tuple_622] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_623.append(var_622)
        # Program VectorUnique Region
        vec_623 = list(set(vec_623))
        vec_index623 = 0
        # Program TableJoin Region
        while vec_index623 < len(vec_623):
            var_625 = vec_623[vec_index623]
            vec_index623 += 1
            if var_625 in self.index_211:
                tuple_624_1_index: int = 0
                tuple_624_1_vec: List[Tuple[int, bytes, bytes]] = self.index_188[var_625]
                while tuple_624_1_index < len(tuple_624_1_vec):
                    tuple_624_1 = tuple_624_1_vec[tuple_624_1_index]
                    tuple_624_1_index += 1
                    var_626 = tuple_624_1[0]
                    var_627 = tuple_624_1[1]
                    var_628 = tuple_624_1[2]
                    # Program TransitionState Region
                    tuple_625 = var_625
                    prev_state = self.table_17[tuple_625]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_625] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_632: Tuple[int, int]
                        scan_index_632: int = 0
                        scan_tuple_632_vec: List[Tuple[int, int]] = self.index_199[var_625]
                        while scan_index_632 < len(scan_tuple_632_vec):
                            scan_tuple_632 = scan_tuple_632_vec[scan_index_632]
                            scan_index_632 += 1
                            vec_632.append(scan_tuple_632)
                        # Program VectorLoop Region
                        vec_index632 = 0
                        while vec_index632 < len(vec_632):
                            var_633, var_634 = vec_632[vec_index632]
                            vec_index632 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_634 = self._resolve_edgetype(var_634)
                            tuple_625_633_634 = (var_625, var_633, var_634)
                            prev_state = self.table_26[tuple_625_633_634]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_625_633_634] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_625, var_633, var_634)

                        # Program TransitionState Region
                        tuple_625_625 = (var_625, var_625)
                        prev_state = self.table_6[tuple_625_625]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_625_625] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_625_625[1]].append(tuple_625_625[0])
                                self.index_1029[tuple_625_625[0]].append(tuple_625_625[1])
                            # Program VectorAppend Region
                            vec_629.append((var_625, var_625))
                        # Program VectorAppend Region
                        vec_636.append(var_625)
        # Program VectorClear Region
        del vec_623[:]
        vec_index623 = 0
        # Program VectorUnique Region
        vec_636 = list(set(vec_636))
        vec_index636 = 0
        # Program TableJoin Region
        while vec_index636 < len(vec_636):
            var_638 = vec_636[vec_index636]
            vec_index636 += 1
            tuple_637_0_index: int = 0
            tuple_637_0_vec: List[Tuple[int, int]] = self.index_373[var_638]
            while tuple_637_0_index < len(tuple_637_0_vec):
                tuple_637_0 = tuple_637_0_vec[tuple_637_0_index]
                tuple_637_0_index += 1
                var_639 = tuple_637_0[0]
                var_640 = tuple_637_0[1]
                if var_638 in self.index_408:
                    # Program TransitionState Region
                    tuple_639_638 = (var_639, var_638)
                    prev_state = self.table_12[tuple_639_638]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_639_638] = 1 | 4
                        if not present_bit:
                            self.index_433[tuple_639_638[1]].append(tuple_639_638[0])
                            self.index_1028[tuple_639_638[0]].append(tuple_639_638[1])
                        # Program VectorAppend Region
                        vec_641.append(var_638)
        # Program VectorClear Region
        del vec_636[:]
        vec_index636 = 0
        # Program VectorUnique Region
        vec_641 = list(set(vec_641))
        vec_index641 = 0
        # Program TableJoin Region
        while vec_index641 < len(vec_641):
            var_643 = vec_641[vec_index641]
            vec_index641 += 1
            tuple_642_0_index: int = 0
            tuple_642_0_vec: List[int] = self.index_433[var_643]
            while tuple_642_0_index < len(tuple_642_0_vec):
                tuple_642_0 = tuple_642_0_vec[tuple_642_0_index]
                tuple_642_0_index += 1
                var_644 = tuple_642_0
                tuple_642_1_index: int = 0
                tuple_642_1_vec: List[bytes] = self.index_372[var_643]
                while tuple_642_1_index < len(tuple_642_1_vec):
                    tuple_642_1 = tuple_642_1_vec[tuple_642_1_index]
                    tuple_642_1_index += 1
                    var_645 = tuple_642_1
                    # Program TransitionState Region
                    tuple_644 = var_644
                    prev_state = self.table_15[tuple_644]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_644] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_641[:]
        vec_index641 = 0
        # Induction Fixpoint Loop Region
        while len(vec_629):
            # Program Call Region
            param_631_0 = [vec_629]
            ret = self.proc_192_(param_631_0)
            vec_629 = param_631_0[0]

        vec_index629 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_629[:]
        vec_index629 = 0
        # Program Return Region
        return False

    def destructor_function_1(self, vec_647: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index647: int = 0
        vec_649: List[int] = list()
        vec_index649: int = 0
        vec_655: List[Tuple[int, int]] = list()
        vec_index655: int = 0
        vec_658: List[Tuple[int, int]] = list()
        vec_index658: int = 0
        vec_662: List[int] = list()
        vec_index662: int = 0
        vec_667: List[int] = list()
        vec_index667: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index647 = 0
        while vec_index647 < len(vec_647):
            var_648 = vec_647[vec_index647]
            vec_index647 += 1
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_648 = var_648
            prev_state = self.table_69[tuple_648]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_69[tuple_648] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_649.append(var_648)
        # Program VectorUnique Region
        vec_649 = list(set(vec_649))
        vec_index649 = 0
        # Program TableJoin Region
        while vec_index649 < len(vec_649):
            var_651 = vec_649[vec_index649]
            vec_index649 += 1
            if var_651 in self.index_187:
                tuple_650_1_index: int = 0
                tuple_650_1_vec: List[Tuple[int, bytes, bytes]] = self.index_188[var_651]
                while tuple_650_1_index < len(tuple_650_1_vec):
                    tuple_650_1 = tuple_650_1_vec[tuple_650_1_index]
                    tuple_650_1_index += 1
                    var_652 = tuple_650_1[0]
                    var_653 = tuple_650_1[1]
                    var_654 = tuple_650_1[2]
                    # Program TransitionState Region
                    tuple_651 = var_651
                    prev_state = self.table_17[tuple_651]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_651] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_658: Tuple[int, int]
                        scan_index_658: int = 0
                        scan_tuple_658_vec: List[Tuple[int, int]] = self.index_199[var_651]
                        while scan_index_658 < len(scan_tuple_658_vec):
                            scan_tuple_658 = scan_tuple_658_vec[scan_index_658]
                            scan_index_658 += 1
                            vec_658.append(scan_tuple_658)
                        # Program VectorLoop Region
                        vec_index658 = 0
                        while vec_index658 < len(vec_658):
                            var_659, var_660 = vec_658[vec_index658]
                            vec_index658 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_660 = self._resolve_edgetype(var_660)
                            tuple_651_659_660 = (var_651, var_659, var_660)
                            prev_state = self.table_26[tuple_651_659_660]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_651_659_660] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_651, var_659, var_660)

                        # Program TransitionState Region
                        tuple_651_651 = (var_651, var_651)
                        prev_state = self.table_6[tuple_651_651]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_651_651] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_651_651[1]].append(tuple_651_651[0])
                                self.index_1029[tuple_651_651[0]].append(tuple_651_651[1])
                            # Program VectorAppend Region
                            vec_655.append((var_651, var_651))
                        # Program VectorAppend Region
                        vec_662.append(var_651)
        # Program VectorClear Region
        del vec_649[:]
        vec_index649 = 0
        # Program VectorUnique Region
        vec_662 = list(set(vec_662))
        vec_index662 = 0
        # Program TableJoin Region
        while vec_index662 < len(vec_662):
            var_664 = vec_662[vec_index662]
            vec_index662 += 1
            tuple_663_0_index: int = 0
            tuple_663_0_vec: List[Tuple[int, int]] = self.index_373[var_664]
            while tuple_663_0_index < len(tuple_663_0_vec):
                tuple_663_0 = tuple_663_0_vec[tuple_663_0_index]
                tuple_663_0_index += 1
                var_665 = tuple_663_0[0]
                var_666 = tuple_663_0[1]
                if var_664 in self.index_408:
                    # Program TransitionState Region
                    tuple_665_664 = (var_665, var_664)
                    prev_state = self.table_12[tuple_665_664]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_665_664] = 1 | 4
                        if not present_bit:
                            self.index_433[tuple_665_664[1]].append(tuple_665_664[0])
                            self.index_1028[tuple_665_664[0]].append(tuple_665_664[1])
                        # Program VectorAppend Region
                        vec_667.append(var_664)
        # Program VectorClear Region
        del vec_662[:]
        vec_index662 = 0
        # Program VectorUnique Region
        vec_667 = list(set(vec_667))
        vec_index667 = 0
        # Program TableJoin Region
        while vec_index667 < len(vec_667):
            var_669 = vec_667[vec_index667]
            vec_index667 += 1
            tuple_668_0_index: int = 0
            tuple_668_0_vec: List[int] = self.index_433[var_669]
            while tuple_668_0_index < len(tuple_668_0_vec):
                tuple_668_0 = tuple_668_0_vec[tuple_668_0_index]
                tuple_668_0_index += 1
                var_670 = tuple_668_0
                tuple_668_1_index: int = 0
                tuple_668_1_vec: List[bytes] = self.index_372[var_669]
                while tuple_668_1_index < len(tuple_668_1_vec):
                    tuple_668_1 = tuple_668_1_vec[tuple_668_1_index]
                    tuple_668_1_index += 1
                    var_671 = tuple_668_1
                    # Program TransitionState Region
                    tuple_670 = var_670
                    prev_state = self.table_15[tuple_670]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_670] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_667[:]
        vec_index667 = 0
        # Induction Fixpoint Loop Region
        while len(vec_655):
            # Program Call Region
            param_657_0 = [vec_655]
            ret = self.proc_192_(param_657_0)
            vec_655 = param_657_0[0]

        vec_index655 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_655[:]
        vec_index655 = 0
        # Program Return Region
        return False

    def raw_transfer_3(self, vec_673: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index673: int = 0
        vec_677: List[Tuple[int, int]] = list()
        vec_index677: int = 0
        vec_685: List[int] = list()
        vec_index685: int = 0
        vec_694: List[int] = list()
        vec_index694: int = 0
        vec_703: List[int] = list()
        vec_index703: int = 0
        vec_712: List[Tuple[int, int]] = list()
        vec_index712: int = 0
        vec_715: List[Tuple[int, int]] = list()
        vec_index715: int = 0
        vec_719: List[int] = list()
        vec_index719: int = 0
        vec_729: List[Tuple[int, int]] = list()
        vec_index729: int = 0
        vec_733: List[int] = list()
        vec_index733: int = 0
        vec_743: List[Tuple[int, int]] = list()
        vec_index743: int = 0
        vec_747: List[int] = list()
        vec_index747: int = 0
        vec_757: List[Tuple[int, int]] = list()
        vec_index757: int = 0
        vec_761: List[int] = list()
        vec_index761: int = 0
        vec_767: List[Tuple[int, int]] = list()
        vec_index767: int = 0
        vec_771: List[int] = list()
        vec_index771: int = 0
        vec_779: List[int] = list()
        vec_index779: int = 0
        vec_788: List[Tuple[int, int]] = list()
        vec_index788: int = 0
        vec_792: List[int] = list()
        vec_index792: int = 0
        vec_797: List[int] = list()
        vec_index797: int = 0
        vec_805: List[int] = list()
        vec_index805: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index673 = 0
        while vec_index673 < len(vec_673):
            var_674, var_675, var_676 = vec_673[vec_index673]
            vec_index673 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if var_676 != self.var_0:
                # Program TupleCompare Region
                if var_676 != self.var_3:
                    # Program TransitionState Region
                    var_676 = self._resolve_edgetype(var_676)
                    tuple_676_3_0_674_675 = (var_676, self.var_3, self.var_0, var_674, var_675)
                    prev_state = self.table_71[tuple_676_3_0_674_675]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_71[tuple_676_3_0_674_675] = 1 | 4
                        if not present_bit:
                            self.index_319[tuple_676_3_0_674_675[4]].append((tuple_676_3_0_674_675[0], tuple_676_3_0_674_675[1], tuple_676_3_0_674_675[2], tuple_676_3_0_674_675[3]))
                        # Program VectorAppend Region
                        vec_719.append(var_675)
            # Program TupleCompare Region
            if self.var_0 == var_676:
                # Program TransitionState Region
                tuple_0_674_675 = (self.var_0, var_674, var_675)
                prev_state = self.table_77[tuple_0_674_675]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_77[tuple_0_674_675] = 1 | 4
                    if not present_bit:
                        self.index_697[tuple_0_674_675[1]].append((tuple_0_674_675[0], tuple_0_674_675[2]))
                    # Program VectorAppend Region
                    vec_694.append(var_674)
            # Program TupleCompare Region
            if self.var_3 == var_676:
                # Program TransitionState Region
                tuple_3_674_675 = (self.var_3, var_674, var_675)
                prev_state = self.table_81[tuple_3_674_675]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_81[tuple_3_674_675] = 1 | 4
                    if not present_bit:
                        self.index_698[tuple_3_674_675[1]].append((tuple_3_674_675[0], tuple_3_674_675[2]))
                    # Program VectorAppend Region
                    vec_694.append(var_674)
            # Program TupleCompare Region
            if self.var_0 == var_676:
                # Program TransitionState Region
                tuple_0_674_675 = (self.var_0, var_674, var_675)
                prev_state = self.table_91[tuple_0_674_675]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_91[tuple_0_674_675] = 1 | 4
                    if not present_bit:
                        self.index_688[tuple_0_674_675[1]].append((tuple_0_674_675[0], tuple_0_674_675[2]))
                    # Program VectorAppend Region
                    vec_685.append(var_674)
            # Program TupleCompare Region
            if self.var_3 == var_676:
                # Program TransitionState Region
                tuple_3_674_675 = (self.var_3, var_674, var_675)
                prev_state = self.table_95[tuple_3_674_675]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_95[tuple_3_674_675] = 1 | 4
                    if not present_bit:
                        self.index_689[tuple_3_674_675[1]].append((tuple_3_674_675[0], tuple_3_674_675[2]))
                    # Program VectorAppend Region
                    vec_685.append(var_674)
            # Program TupleCompare Region
            if self.var_0 == var_676:
                # Program TransitionState Region
                tuple_0_674_675 = (self.var_0, var_674, var_675)
                prev_state = self.table_147[tuple_0_674_675]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_147[tuple_0_674_675] = 1 | 4
                    if not present_bit:
                        self.index_681[(tuple_0_674_675[1], tuple_0_674_675[2])].append(tuple_0_674_675[0])
                    # Program VectorAppend Region
                    vec_677.append((var_674, var_675))
            # Program TupleCompare Region
            if self.var_3 == var_676:
                # Program TransitionState Region
                tuple_3_674_675 = (self.var_3, var_674, var_675)
                prev_state = self.table_151[tuple_3_674_675]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_151[tuple_3_674_675] = 1 | 4
                    if not present_bit:
                        self.index_682[(tuple_3_674_675[1], tuple_3_674_675[2])].append(tuple_3_674_675[0])
                    # Program VectorAppend Region
                    vec_677.append((var_674, var_675))
        # Program VectorUnique Region
        vec_677 = list(set(vec_677))
        vec_index677 = 0
        # Program TableJoin Region
        while vec_index677 < len(vec_677):
            var_679, var_680 = vec_677[vec_index677]
            vec_index677 += 1
            tuple_678_0_index: int = 0
            tuple_678_0_vec: List[int] = self.index_681[(var_679, var_680)]
            while tuple_678_0_index < len(tuple_678_0_vec):
                tuple_678_0 = tuple_678_0_vec[tuple_678_0_index]
                tuple_678_0_index += 1
                var_683 = tuple_678_0
                tuple_678_1_index: int = 0
                tuple_678_1_vec: List[int] = self.index_682[(var_679, var_680)]
                while tuple_678_1_index < len(tuple_678_1_vec):
                    tuple_678_1 = tuple_678_1_vec[tuple_678_1_index]
                    tuple_678_1_index += 1
                    var_684 = tuple_678_1
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_683, var_684, ):
                        # Program TransitionState Region
                        tuple_3_0_679_680 = (self.var_3, self.var_0, var_679, var_680)
                        prev_state = self.table_155[tuple_3_0_679_680]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_155[tuple_3_0_679_680] = 1 | 4
                            if not present_bit:
                                self.index_268[tuple_3_0_679_680[3]].append((tuple_3_0_679_680[0], tuple_3_0_679_680[1], tuple_3_0_679_680[2]))
                            # Program VectorAppend Region
                            vec_703.append(var_680)
        # Program VectorClear Region
        del vec_677[:]
        vec_index677 = 0
        # Program VectorUnique Region
        vec_685 = list(set(vec_685))
        vec_index685 = 0
        # Program TableJoin Region
        while vec_index685 < len(vec_685):
            var_687 = vec_685[vec_index685]
            vec_index685 += 1
            tuple_686_0_index: int = 0
            tuple_686_0_vec: List[Tuple[int, int]] = self.index_688[var_687]
            while tuple_686_0_index < len(tuple_686_0_vec):
                tuple_686_0 = tuple_686_0_vec[tuple_686_0_index]
                tuple_686_0_index += 1
                var_690 = tuple_686_0[0]
                var_691 = tuple_686_0[1]
                tuple_686_1_index: int = 0
                tuple_686_1_vec: List[Tuple[int, int]] = self.index_689[var_687]
                while tuple_686_1_index < len(tuple_686_1_vec):
                    tuple_686_1 = tuple_686_1_vec[tuple_686_1_index]
                    tuple_686_1_index += 1
                    var_692 = tuple_686_1[0]
                    var_693 = tuple_686_1[1]
                    # Program TupleCompare Region
                    if (self.var_3, self.var_0, ) == (var_692, var_690, ):
                        # Program TupleCompare Region
                        if var_691 != var_693:
                            # Program TransitionState Region
                            tuple_691_693_3_0_687 = (var_691, var_693, self.var_3, self.var_0, var_687)
                            prev_state = self.table_99[tuple_691_693_3_0_687]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_99[tuple_691_693_3_0_687] = 1 | 4
                                if not present_bit:
                                    self.index_342[tuple_691_693_3_0_687[1]].append((tuple_691_693_3_0_687[0], tuple_691_693_3_0_687[2], tuple_691_693_3_0_687[3], tuple_691_693_3_0_687[4]))
                                # Program VectorAppend Region
                                vec_747.append(var_693)
        # Program VectorClear Region
        del vec_685[:]
        vec_index685 = 0
        # Program VectorUnique Region
        vec_694 = list(set(vec_694))
        vec_index694 = 0
        # Program TableJoin Region
        while vec_index694 < len(vec_694):
            var_696 = vec_694[vec_index694]
            vec_index694 += 1
            tuple_695_0_index: int = 0
            tuple_695_0_vec: List[Tuple[int, int]] = self.index_697[var_696]
            while tuple_695_0_index < len(tuple_695_0_vec):
                tuple_695_0 = tuple_695_0_vec[tuple_695_0_index]
                tuple_695_0_index += 1
                var_699 = tuple_695_0[0]
                var_700 = tuple_695_0[1]
                tuple_695_1_index: int = 0
                tuple_695_1_vec: List[Tuple[int, int]] = self.index_698[var_696]
                while tuple_695_1_index < len(tuple_695_1_vec):
                    tuple_695_1 = tuple_695_1_vec[tuple_695_1_index]
                    tuple_695_1_index += 1
                    var_701 = tuple_695_1[0]
                    var_702 = tuple_695_1[1]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_699, var_701, ):
                        # Program TupleCompare Region
                        if var_700 != var_702:
                            # Program TransitionState Region
                            tuple_700_702_3_0_696 = (var_700, var_702, self.var_3, self.var_0, var_696)
                            prev_state = self.table_85[tuple_700_702_3_0_696]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_85[tuple_700_702_3_0_696] = 1 | 4
                                if not present_bit:
                                    self.index_357[tuple_700_702_3_0_696[0]].append((tuple_700_702_3_0_696[1], tuple_700_702_3_0_696[2], tuple_700_702_3_0_696[3], tuple_700_702_3_0_696[4]))
                                # Program VectorAppend Region
                                vec_733.append(var_700)
        # Program VectorClear Region
        del vec_694[:]
        vec_index694 = 0
        # Program VectorUnique Region
        vec_703 = list(set(vec_703))
        vec_index703 = 0
        # Program TableJoin Region
        while vec_index703 < len(vec_703):
            var_705 = vec_703[vec_index703]
            vec_index703 += 1
            if var_705 in self.index_267:
                tuple_704_1_index: int = 0
                tuple_704_1_vec: List[Tuple[int, int, int]] = self.index_268[var_705]
                while tuple_704_1_index < len(tuple_704_1_vec):
                    tuple_704_1 = tuple_704_1_vec[tuple_704_1_index]
                    tuple_704_1_index += 1
                    var_706 = tuple_704_1[0]
                    var_707 = tuple_704_1[1]
                    var_708 = tuple_704_1[2]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_707, var_706, ):
                        # Program TransitionState Region
                        tuple_708_705_5 = (var_708, var_705, self.var_5)
                        prev_state = self.table_43[tuple_708_705_5]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_708_705_5] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_708_705_5[1]].append((tuple_708_705_5[0], tuple_708_705_5[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_705_708_5 = (var_705, var_708, self.var_5)
                            prev_state = self.table_26[tuple_705_708_5]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_705_708_5] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_705_708_5[0]].append((tuple_705_708_5[1], tuple_705_708_5[2]))
                                    self.index_1053[(tuple_705_708_5[0], tuple_705_708_5[1])].append(tuple_705_708_5[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_705)
                            if not ret:
                                # Program TransitionState Region
                                tuple_705_708_5 = (var_705, var_708, self.var_5)
                                prev_state = self.table_26[tuple_705_708_5]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_705_708_5] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_705_708_5[0]].append((tuple_705_708_5[1], tuple_705_708_5[2]))
                                        self.index_1053[(tuple_705_708_5[0], tuple_705_708_5[1])].append(tuple_705_708_5[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_708, var_705)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_708_705 = (var_708, var_705)
                                        prev_state = self.table_9[tuple_708_705]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_708_705] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_708_705[0]].append(tuple_708_705[1])
                                                self.index_1079[tuple_708_705[1]].append(tuple_708_705[0])
                                            # Program VectorAppend Region
                                            vec_797.append(var_708)
                            # Program VectorAppend Region
                            vec_761.append(var_705)
                            # Program VectorAppend Region
                            vec_792.append(var_705)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_5:
                                # Program TransitionState Region
                                tuple_705 = var_705
                                prev_state = self.table_17[tuple_705]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_705] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_715: Tuple[int, int]
                                    scan_index_715: int = 0
                                    scan_tuple_715_vec: List[Tuple[int, int]] = self.index_199[var_705]
                                    while scan_index_715 < len(scan_tuple_715_vec):
                                        scan_tuple_715 = scan_tuple_715_vec[scan_index_715]
                                        scan_index_715 += 1
                                        vec_715.append(scan_tuple_715)
                                    # Program VectorLoop Region
                                    vec_index715 = 0
                                    while vec_index715 < len(vec_715):
                                        var_716, var_717 = vec_715[vec_index715]
                                        vec_index715 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_717 = self._resolve_edgetype(var_717)
                                        tuple_705_716_717 = (var_705, var_716, var_717)
                                        prev_state = self.table_26[tuple_705_716_717]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_705_716_717] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_705, var_716, var_717)

                                    # Program TransitionState Region
                                    tuple_705_705 = (var_705, var_705)
                                    prev_state = self.table_6[tuple_705_705]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_705_705] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_705_705[1]].append(tuple_705_705[0])
                                            self.index_1029[tuple_705_705[0]].append(tuple_705_705[1])
                                        # Program VectorAppend Region
                                        vec_712.append((var_705, var_705))
                                    # Program VectorAppend Region
                                    vec_792.append(var_705)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_5:
                                # Program TransitionState Region
                                tuple_2_708_705 = (self.var_2, var_708, var_705)
                                prev_state = self.table_56[tuple_2_708_705]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_708_705] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_2_708_705[1]].append((tuple_2_708_705[0], tuple_2_708_705[2]))
                                    # Program VectorAppend Region
                                    vec_771.append(var_708)
        # Program VectorClear Region
        del vec_703[:]
        vec_index703 = 0
        # Program VectorUnique Region
        vec_719 = list(set(vec_719))
        vec_index719 = 0
        # Program TableJoin Region
        while vec_index719 < len(vec_719):
            var_721 = vec_719[vec_index719]
            vec_index719 += 1
            tuple_720_0_index: int = 0
            tuple_720_0_vec: List[Tuple[int, int, int, int]] = self.index_319[var_721]
            while tuple_720_0_index < len(tuple_720_0_vec):
                tuple_720_0 = tuple_720_0_vec[tuple_720_0_index]
                tuple_720_0_index += 1
                var_722 = tuple_720_0[0]
                var_723 = tuple_720_0[1]
                var_724 = tuple_720_0[2]
                var_725 = tuple_720_0[3]
                if var_721 in self.index_267:
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_724, var_723, ):
                        # Program TransitionState Region
                        var_722 = self._resolve_edgetype(var_722)
                        tuple_725_721_722 = (var_725, var_721, var_722)
                        prev_state = self.table_43[tuple_725_721_722]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_725_721_722] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_725_721_722[1]].append((tuple_725_721_722[0], tuple_725_721_722[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            var_722 = self._resolve_edgetype(var_722)
                            tuple_721_725_722 = (var_721, var_725, var_722)
                            prev_state = self.table_26[tuple_721_725_722]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_721_725_722] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_721_725_722[0]].append((tuple_721_725_722[1], tuple_721_725_722[2]))
                                    self.index_1053[(tuple_721_725_722[0], tuple_721_725_722[1])].append(tuple_721_725_722[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_721)
                            if not ret:
                                # Program TransitionState Region
                                var_722 = self._resolve_edgetype(var_722)
                                tuple_721_725_722 = (var_721, var_725, var_722)
                                prev_state = self.table_26[tuple_721_725_722]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_721_725_722] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_721_725_722[0]].append((tuple_721_725_722[1], tuple_721_725_722[2]))
                                        self.index_1053[(tuple_721_725_722[0], tuple_721_725_722[1])].append(tuple_721_725_722[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_725, var_721)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_725_721 = (var_725, var_721)
                                        prev_state = self.table_9[tuple_725_721]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_725_721] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_725_721[0]].append(tuple_725_721[1])
                                                self.index_1079[tuple_725_721[1]].append(tuple_725_721[0])
                                            # Program VectorAppend Region
                                            vec_797.append(var_725)
                            # Program VectorAppend Region
                            vec_761.append(var_721)
                            # Program VectorAppend Region
                            vec_792.append(var_721)
                            # Program TupleCompare Region
                            if self.var_0 == var_722:
                                # Program TransitionState Region
                                tuple_721 = var_721
                                prev_state = self.table_17[tuple_721]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_721] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_729: Tuple[int, int]
                                    scan_index_729: int = 0
                                    scan_tuple_729_vec: List[Tuple[int, int]] = self.index_199[var_721]
                                    while scan_index_729 < len(scan_tuple_729_vec):
                                        scan_tuple_729 = scan_tuple_729_vec[scan_index_729]
                                        scan_index_729 += 1
                                        vec_729.append(scan_tuple_729)
                                    # Program VectorLoop Region
                                    vec_index729 = 0
                                    while vec_index729 < len(vec_729):
                                        var_730, var_731 = vec_729[vec_index729]
                                        vec_index729 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_731 = self._resolve_edgetype(var_731)
                                        tuple_721_730_731 = (var_721, var_730, var_731)
                                        prev_state = self.table_26[tuple_721_730_731]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_721_730_731] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_721, var_730, var_731)

                                    # Program TransitionState Region
                                    tuple_721_721 = (var_721, var_721)
                                    prev_state = self.table_6[tuple_721_721]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_721_721] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_721_721[1]].append(tuple_721_721[0])
                                            self.index_1029[tuple_721_721[0]].append(tuple_721_721[1])
                                        # Program VectorAppend Region
                                        vec_712.append((var_721, var_721))
                                    # Program VectorAppend Region
                                    vec_792.append(var_721)
                            # Program TupleCompare Region
                            if self.var_2 == var_722:
                                # Program TransitionState Region
                                tuple_2_725_721 = (self.var_2, var_725, var_721)
                                prev_state = self.table_56[tuple_2_725_721]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_725_721] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_2_725_721[1]].append((tuple_2_725_721[0], tuple_2_725_721[2]))
                                    # Program VectorAppend Region
                                    vec_771.append(var_725)
        # Program VectorClear Region
        del vec_719[:]
        vec_index719 = 0
        # Program VectorUnique Region
        vec_733 = list(set(vec_733))
        vec_index733 = 0
        # Program TableJoin Region
        while vec_index733 < len(vec_733):
            var_735 = vec_733[vec_index733]
            vec_index733 += 1
            if var_735 in self.index_267:
                tuple_734_1_index: int = 0
                tuple_734_1_vec: List[Tuple[int, int, int, int]] = self.index_357[var_735]
                while tuple_734_1_index < len(tuple_734_1_vec):
                    tuple_734_1 = tuple_734_1_vec[tuple_734_1_index]
                    tuple_734_1_index += 1
                    var_736 = tuple_734_1[0]
                    var_737 = tuple_734_1[1]
                    var_738 = tuple_734_1[2]
                    var_739 = tuple_734_1[3]
                    # Program TupleCompare Region
                    if (self.var_0, self.var_3, ) == (var_738, var_737, ):
                        # Program TransitionState Region
                        tuple_739_735_0 = (var_739, var_735, self.var_0)
                        prev_state = self.table_43[tuple_739_735_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_739_735_0] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_739_735_0[1]].append((tuple_739_735_0[0], tuple_739_735_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_735_739_0 = (var_735, var_739, self.var_0)
                            prev_state = self.table_26[tuple_735_739_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_735_739_0] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_735_739_0[0]].append((tuple_735_739_0[1], tuple_735_739_0[2]))
                                    self.index_1053[(tuple_735_739_0[0], tuple_735_739_0[1])].append(tuple_735_739_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_735)
                            if not ret:
                                # Program TransitionState Region
                                tuple_735_739_0 = (var_735, var_739, self.var_0)
                                prev_state = self.table_26[tuple_735_739_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_735_739_0] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_735_739_0[0]].append((tuple_735_739_0[1], tuple_735_739_0[2]))
                                        self.index_1053[(tuple_735_739_0[0], tuple_735_739_0[1])].append(tuple_735_739_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_739, var_735)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_739_735 = (var_739, var_735)
                                        prev_state = self.table_9[tuple_739_735]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_739_735] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_739_735[0]].append(tuple_739_735[1])
                                                self.index_1079[tuple_739_735[1]].append(tuple_739_735[0])
                                            # Program VectorAppend Region
                                            vec_797.append(var_739)
                            # Program VectorAppend Region
                            vec_761.append(var_735)
                            # Program VectorAppend Region
                            vec_792.append(var_735)
                            # Program TransitionState Region
                            tuple_735 = var_735
                            prev_state = self.table_17[tuple_735]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_17[tuple_735] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_743: Tuple[int, int]
                                scan_index_743: int = 0
                                scan_tuple_743_vec: List[Tuple[int, int]] = self.index_199[var_735]
                                while scan_index_743 < len(scan_tuple_743_vec):
                                    scan_tuple_743 = scan_tuple_743_vec[scan_index_743]
                                    scan_index_743 += 1
                                    vec_743.append(scan_tuple_743)
                                # Program VectorLoop Region
                                vec_index743 = 0
                                while vec_index743 < len(vec_743):
                                    var_744, var_745 = vec_743[vec_index743]
                                    vec_index743 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_745 = self._resolve_edgetype(var_745)
                                    tuple_735_744_745 = (var_735, var_744, var_745)
                                    prev_state = self.table_26[tuple_735_744_745]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_735_744_745] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_203_(var_735, var_744, var_745)

                                # Program TransitionState Region
                                tuple_735_735 = (var_735, var_735)
                                prev_state = self.table_6[tuple_735_735]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_735_735] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_735_735[1]].append(tuple_735_735[0])
                                        self.index_1029[tuple_735_735[0]].append(tuple_735_735[1])
                                    # Program VectorAppend Region
                                    vec_712.append((var_735, var_735))
                                # Program VectorAppend Region
                                vec_792.append(var_735)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_739_735 = (self.var_0, var_739, var_735)
                                prev_state = self.table_56[tuple_0_739_735]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_739_735] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_0_739_735[1]].append((tuple_0_739_735[0], tuple_0_739_735[2]))
                                    # Program VectorAppend Region
                                    vec_771.append(var_739)
        # Program VectorClear Region
        del vec_733[:]
        vec_index733 = 0
        # Program VectorUnique Region
        vec_747 = list(set(vec_747))
        vec_index747 = 0
        # Program TableJoin Region
        while vec_index747 < len(vec_747):
            var_749 = vec_747[vec_index747]
            vec_index747 += 1
            if var_749 in self.index_267:
                tuple_748_1_index: int = 0
                tuple_748_1_vec: List[Tuple[int, int, int, int]] = self.index_342[var_749]
                while tuple_748_1_index < len(tuple_748_1_vec):
                    tuple_748_1 = tuple_748_1_vec[tuple_748_1_index]
                    tuple_748_1_index += 1
                    var_750 = tuple_748_1[0]
                    var_751 = tuple_748_1[1]
                    var_752 = tuple_748_1[2]
                    var_753 = tuple_748_1[3]
                    # Program TupleCompare Region
                    if (self.var_3, self.var_0, ) == (var_751, var_752, ):
                        # Program TransitionState Region
                        tuple_753_749_3 = (var_753, var_749, self.var_3)
                        prev_state = self.table_43[tuple_753_749_3]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_753_749_3] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_753_749_3[1]].append((tuple_753_749_3[0], tuple_753_749_3[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_749_753_3 = (var_749, var_753, self.var_3)
                            prev_state = self.table_26[tuple_749_753_3]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_749_753_3] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_749_753_3[0]].append((tuple_749_753_3[1], tuple_749_753_3[2]))
                                    self.index_1053[(tuple_749_753_3[0], tuple_749_753_3[1])].append(tuple_749_753_3[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_749)
                            if not ret:
                                # Program TransitionState Region
                                tuple_749_753_3 = (var_749, var_753, self.var_3)
                                prev_state = self.table_26[tuple_749_753_3]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_749_753_3] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_749_753_3[0]].append((tuple_749_753_3[1], tuple_749_753_3[2]))
                                        self.index_1053[(tuple_749_753_3[0], tuple_749_753_3[1])].append(tuple_749_753_3[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_753, var_749)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_753_749 = (var_753, var_749)
                                        prev_state = self.table_9[tuple_753_749]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_753_749] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_753_749[0]].append(tuple_753_749[1])
                                                self.index_1079[tuple_753_749[1]].append(tuple_753_749[0])
                                            # Program VectorAppend Region
                                            vec_797.append(var_753)
                            # Program VectorAppend Region
                            vec_761.append(var_749)
                            # Program VectorAppend Region
                            vec_792.append(var_749)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_3:
                                # Program TransitionState Region
                                tuple_749 = var_749
                                prev_state = self.table_17[tuple_749]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_749] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_757: Tuple[int, int]
                                    scan_index_757: int = 0
                                    scan_tuple_757_vec: List[Tuple[int, int]] = self.index_199[var_749]
                                    while scan_index_757 < len(scan_tuple_757_vec):
                                        scan_tuple_757 = scan_tuple_757_vec[scan_index_757]
                                        scan_index_757 += 1
                                        vec_757.append(scan_tuple_757)
                                    # Program VectorLoop Region
                                    vec_index757 = 0
                                    while vec_index757 < len(vec_757):
                                        var_758, var_759 = vec_757[vec_index757]
                                        vec_index757 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_759 = self._resolve_edgetype(var_759)
                                        tuple_749_758_759 = (var_749, var_758, var_759)
                                        prev_state = self.table_26[tuple_749_758_759]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_749_758_759] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_749, var_758, var_759)

                                    # Program TransitionState Region
                                    tuple_749_749 = (var_749, var_749)
                                    prev_state = self.table_6[tuple_749_749]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_749_749] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_749_749[1]].append(tuple_749_749[0])
                                            self.index_1029[tuple_749_749[0]].append(tuple_749_749[1])
                                        # Program VectorAppend Region
                                        vec_712.append((var_749, var_749))
                                    # Program VectorAppend Region
                                    vec_792.append(var_749)
                            # Program TupleCompare Region
                            if self.var_2 == self.var_3:
                                # Program TransitionState Region
                                tuple_2_753_749 = (self.var_2, var_753, var_749)
                                prev_state = self.table_56[tuple_2_753_749]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_2_753_749] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_2_753_749[1]].append((tuple_2_753_749[0], tuple_2_753_749[2]))
                                    # Program VectorAppend Region
                                    vec_771.append(var_753)
        # Program VectorClear Region
        del vec_747[:]
        vec_index747 = 0
        # Program VectorUnique Region
        vec_761 = list(set(vec_761))
        vec_index761 = 0
        # Program TableJoin Region
        while vec_index761 < len(vec_761):
            var_763 = vec_761[vec_index761]
            vec_index761 += 1
            tuple_762_0_index: int = 0
            tuple_762_0_vec: List[bytes] = self.index_372[var_763]
            while tuple_762_0_index < len(tuple_762_0_vec):
                tuple_762_0 = tuple_762_0_vec[tuple_762_0_index]
                tuple_762_0_index += 1
                var_764 = tuple_762_0
                tuple_762_1_index: int = 0
                tuple_762_1_vec: List[Tuple[int, int]] = self.index_373[var_763]
                while tuple_762_1_index < len(tuple_762_1_vec):
                    tuple_762_1 = tuple_762_1_vec[tuple_762_1_index]
                    tuple_762_1_index += 1
                    var_765 = tuple_762_1[0]
                    var_766 = tuple_762_1[1]
                    # Program TransitionState Region
                    tuple_763 = var_763
                    prev_state = self.table_17[tuple_763]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_763] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_767: Tuple[int, int]
                        scan_index_767: int = 0
                        scan_tuple_767_vec: List[Tuple[int, int]] = self.index_199[var_763]
                        while scan_index_767 < len(scan_tuple_767_vec):
                            scan_tuple_767 = scan_tuple_767_vec[scan_index_767]
                            scan_index_767 += 1
                            vec_767.append(scan_tuple_767)
                        # Program VectorLoop Region
                        vec_index767 = 0
                        while vec_index767 < len(vec_767):
                            var_768, var_769 = vec_767[vec_index767]
                            vec_index767 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_769 = self._resolve_edgetype(var_769)
                            tuple_763_768_769 = (var_763, var_768, var_769)
                            prev_state = self.table_26[tuple_763_768_769]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_763_768_769] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_763, var_768, var_769)

                        # Program TransitionState Region
                        tuple_763_763 = (var_763, var_763)
                        prev_state = self.table_6[tuple_763_763]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_763_763] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_763_763[1]].append(tuple_763_763[0])
                                self.index_1029[tuple_763_763[0]].append(tuple_763_763[1])
                            # Program VectorAppend Region
                            vec_712.append((var_763, var_763))
                        # Program VectorAppend Region
                        vec_792.append(var_763)
        # Program VectorClear Region
        del vec_761[:]
        vec_index761 = 0
        # Program VectorUnique Region
        vec_771 = list(set(vec_771))
        vec_index771 = 0
        # Program TableJoin Region
        while vec_index771 < len(vec_771):
            var_773 = vec_771[vec_index771]
            vec_index771 += 1
            tuple_772_0_index: int = 0
            tuple_772_0_vec: List[Tuple[int, bytes, bytes]] = self.index_384[var_773]
            while tuple_772_0_index < len(tuple_772_0_vec):
                tuple_772_0 = tuple_772_0_vec[tuple_772_0_index]
                tuple_772_0_index += 1
                var_774 = tuple_772_0[0]
                var_775 = tuple_772_0[1]
                var_776 = tuple_772_0[2]
                tuple_772_1_index: int = 0
                tuple_772_1_vec: List[Tuple[int, int]] = self.index_385[var_773]
                while tuple_772_1_index < len(tuple_772_1_vec):
                    tuple_772_1 = tuple_772_1_vec[tuple_772_1_index]
                    tuple_772_1_index += 1
                    var_777 = tuple_772_1[0]
                    var_778 = tuple_772_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_774, var_777, ):
                        # Program TransitionState Region
                        tuple_2_1_773_775_776_778 = (self.var_2, self.var_1, var_773, var_775, var_776, var_778)
                        prev_state = self.table_60[tuple_2_1_773_775_776_778]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_773_775_776_778] = 1 | 4
                            if not present_bit:
                                self.index_394[tuple_2_1_773_775_776_778[5]].append((tuple_2_1_773_775_776_778[0], tuple_2_1_773_775_776_778[1], tuple_2_1_773_775_776_778[2], tuple_2_1_773_775_776_778[3], tuple_2_1_773_775_776_778[4]))
                            # Program VectorAppend Region
                            vec_779.append(var_778)
        # Program VectorClear Region
        del vec_771[:]
        vec_index771 = 0
        # Program VectorUnique Region
        vec_779 = list(set(vec_779))
        vec_index779 = 0
        # Program TableJoin Region
        while vec_index779 < len(vec_779):
            var_781 = vec_779[vec_index779]
            vec_index779 += 1
            tuple_780_0_index: int = 0
            tuple_780_0_vec: List[bytes] = self.index_372[var_781]
            while tuple_780_0_index < len(tuple_780_0_vec):
                tuple_780_0 = tuple_780_0_vec[tuple_780_0_index]
                tuple_780_0_index += 1
                var_782 = tuple_780_0
                tuple_780_1_index: int = 0
                tuple_780_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_394[var_781]
                while tuple_780_1_index < len(tuple_780_1_vec):
                    tuple_780_1 = tuple_780_1_vec[tuple_780_1_index]
                    tuple_780_1_index += 1
                    var_783 = tuple_780_1[0]
                    var_784 = tuple_780_1[1]
                    var_785 = tuple_780_1[2]
                    var_786 = tuple_780_1[3]
                    var_787 = tuple_780_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_784, var_783, ):
                        # Program TransitionState Region
                        tuple_785 = var_785
                        prev_state = self.table_17[tuple_785]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_17[tuple_785] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_788: Tuple[int, int]
                            scan_index_788: int = 0
                            scan_tuple_788_vec: List[Tuple[int, int]] = self.index_199[var_785]
                            while scan_index_788 < len(scan_tuple_788_vec):
                                scan_tuple_788 = scan_tuple_788_vec[scan_index_788]
                                scan_index_788 += 1
                                vec_788.append(scan_tuple_788)
                            # Program VectorLoop Region
                            vec_index788 = 0
                            while vec_index788 < len(vec_788):
                                var_789, var_790 = vec_788[vec_index788]
                                vec_index788 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_790 = self._resolve_edgetype(var_790)
                                tuple_785_789_790 = (var_785, var_789, var_790)
                                prev_state = self.table_26[tuple_785_789_790]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_785_789_790] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_203_(var_785, var_789, var_790)

                            # Program TransitionState Region
                            tuple_785_785 = (var_785, var_785)
                            prev_state = self.table_6[tuple_785_785]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_785_785] = 1 | 4
                                if not present_bit:
                                    self.index_414[tuple_785_785[1]].append(tuple_785_785[0])
                                    self.index_1029[tuple_785_785[0]].append(tuple_785_785[1])
                                # Program VectorAppend Region
                                vec_712.append((var_785, var_785))
                            # Program VectorAppend Region
                            vec_792.append(var_785)
        # Program VectorClear Region
        del vec_779[:]
        vec_index779 = 0
        # Program VectorUnique Region
        vec_792 = list(set(vec_792))
        vec_index792 = 0
        # Program TableJoin Region
        while vec_index792 < len(vec_792):
            var_794 = vec_792[vec_index792]
            vec_index792 += 1
            tuple_793_0_index: int = 0
            tuple_793_0_vec: List[Tuple[int, int]] = self.index_373[var_794]
            while tuple_793_0_index < len(tuple_793_0_vec):
                tuple_793_0 = tuple_793_0_vec[tuple_793_0_index]
                tuple_793_0_index += 1
                var_795 = tuple_793_0[0]
                var_796 = tuple_793_0[1]
                if var_794 in self.index_408:
                    # Program TransitionState Region
                    tuple_795_794 = (var_795, var_794)
                    prev_state = self.table_12[tuple_795_794]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_795_794] = 1 | 4
                        if not present_bit:
                            self.index_433[tuple_795_794[1]].append(tuple_795_794[0])
                            self.index_1028[tuple_795_794[0]].append(tuple_795_794[1])
                        # Program VectorAppend Region
                        vec_805.append(var_794)
        # Program VectorClear Region
        del vec_792[:]
        vec_index792 = 0
        # Program VectorUnique Region
        vec_797 = list(set(vec_797))
        vec_index797 = 0
        # Program TableJoin Region
        while vec_index797 < len(vec_797):
            var_799 = vec_797[vec_index797]
            vec_index797 += 1
            tuple_798_0_index: int = 0
            tuple_798_0_vec: List[int] = self.index_414[var_799]
            while tuple_798_0_index < len(tuple_798_0_vec):
                tuple_798_0 = tuple_798_0_vec[tuple_798_0_index]
                tuple_798_0_index += 1
                var_800 = tuple_798_0
                tuple_798_1_index: int = 0
                tuple_798_1_vec: List[int] = self.index_415[var_799]
                while tuple_798_1_index < len(tuple_798_1_vec):
                    tuple_798_1 = tuple_798_1_vec[tuple_798_1_index]
                    tuple_798_1_index += 1
                    var_801 = tuple_798_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_1030_(var_800, var_799)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_1033_(var_799, var_801)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_426_(var_800, var_801)
                            if not ret:
                                # Program TransitionState Region
                                tuple_800_801 = (var_800, var_801)
                                prev_state = self.table_6[tuple_800_801]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_800_801] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_800_801[1]].append(tuple_800_801[0])
                                        self.index_1029[tuple_800_801[0]].append(tuple_800_801[1])
                                    # Program VectorAppend Region
                                    vec_712.append((var_800, var_801))
        # Program VectorClear Region
        del vec_797[:]
        vec_index797 = 0
        # Program VectorUnique Region
        vec_805 = list(set(vec_805))
        vec_index805 = 0
        # Program TableJoin Region
        while vec_index805 < len(vec_805):
            var_807 = vec_805[vec_index805]
            vec_index805 += 1
            tuple_806_0_index: int = 0
            tuple_806_0_vec: List[int] = self.index_433[var_807]
            while tuple_806_0_index < len(tuple_806_0_vec):
                tuple_806_0 = tuple_806_0_vec[tuple_806_0_index]
                tuple_806_0_index += 1
                var_808 = tuple_806_0
                tuple_806_1_index: int = 0
                tuple_806_1_vec: List[bytes] = self.index_372[var_807]
                while tuple_806_1_index < len(tuple_806_1_vec):
                    tuple_806_1 = tuple_806_1_vec[tuple_806_1_index]
                    tuple_806_1_index += 1
                    var_809 = tuple_806_1
                    # Program TransitionState Region
                    tuple_808 = var_808
                    prev_state = self.table_15[tuple_808]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_808] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_805[:]
        vec_index805 = 0
        # Induction Fixpoint Loop Region
        while len(vec_712):
            # Program Call Region
            param_714_0 = [vec_712]
            ret = self.proc_192_(param_714_0)
            vec_712 = param_714_0[0]

        vec_index712 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_712[:]
        vec_index712 = 0
        # Program Return Region
        return False

    def address_operand_2(self, vec_811: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index811: int = 0
        vec_814: List[int] = list()
        vec_index814: int = 0
        vec_821: List[int] = list()
        vec_index821: int = 0
        vec_828: List[int] = list()
        vec_index828: int = 0
        vec_836: List[int] = list()
        vec_index836: int = 0
        vec_844: List[int] = list()
        vec_index844: int = 0
        vec_855: List[Tuple[int, int]] = list()
        vec_index855: int = 0
        vec_858: List[Tuple[int, int]] = list()
        vec_index858: int = 0
        vec_862: List[int] = list()
        vec_index862: int = 0
        vec_873: List[Tuple[int, int]] = list()
        vec_index873: int = 0
        vec_877: List[int] = list()
        vec_index877: int = 0
        vec_883: List[Tuple[int, int]] = list()
        vec_index883: int = 0
        vec_887: List[int] = list()
        vec_index887: int = 0
        vec_895: List[int] = list()
        vec_index895: int = 0
        vec_904: List[Tuple[int, int]] = list()
        vec_index904: int = 0
        vec_908: List[int] = list()
        vec_index908: int = 0
        vec_913: List[int] = list()
        vec_index913: int = 0
        vec_921: List[int] = list()
        vec_index921: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index811 = 0
        while vec_index811 < len(vec_811):
            var_812, var_813 = vec_811[vec_index811]
            vec_index811 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_812_813 = (var_812, var_813)
            prev_state = self.table_110[tuple_812_813]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_110[tuple_812_813] = 1 | 4
                if not present_bit:
                    self.index_232[tuple_812_813[0]].append(tuple_812_813[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_821.append(var_812)
                # Program VectorAppend Region
                vec_814.append(var_812)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_812_813 = (var_812, var_813)
            prev_state = self.table_110[tuple_812_813]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_110[tuple_812_813] = 1 | 4
                if not present_bit:
                    self.index_232[tuple_812_813[0]].append(tuple_812_813[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_821.append(var_812)
                # Program VectorAppend Region
                vec_814.append(var_812)
        # Program VectorUnique Region
        vec_814 = list(set(vec_814))
        vec_index814 = 0
        # Program TableJoin Region
        while vec_index814 < len(vec_814):
            var_816 = vec_814[vec_index814]
            vec_index814 += 1
            tuple_815_0_index: int = 0
            tuple_815_0_vec: List[Tuple[int, bytes, bytes]] = self.index_231[var_816]
            while tuple_815_0_index < len(tuple_815_0_vec):
                tuple_815_0 = tuple_815_0_vec[tuple_815_0_index]
                tuple_815_0_index += 1
                var_817 = tuple_815_0[0]
                var_818 = tuple_815_0[1]
                var_819 = tuple_815_0[2]
                tuple_815_1_index: int = 0
                tuple_815_1_vec: List[int] = self.index_232[var_816]
                while tuple_815_1_index < len(tuple_815_1_vec):
                    tuple_815_1 = tuple_815_1_vec[tuple_815_1_index]
                    tuple_815_1_index += 1
                    var_820 = tuple_815_1
                    # Program TupleCompare Region
                    if self.var_4 == var_817:
                        # Program TransitionState Region
                        tuple_4_816_818_819_820 = (self.var_4, var_816, var_818, var_819, var_820)
                        prev_state = self.table_134[tuple_4_816_818_819_820]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_134[tuple_4_816_818_819_820] = 1 | 4
                            if not present_bit:
                                self.index_258[tuple_4_816_818_819_820[4]].append((tuple_4_816_818_819_820[0], tuple_4_816_818_819_820[1], tuple_4_816_818_819_820[2], tuple_4_816_818_819_820[3]))
                            # Program VectorAppend Region
                            vec_836.append(var_820)
        # Program VectorClear Region
        del vec_814[:]
        vec_index814 = 0
        # Program VectorUnique Region
        vec_821 = list(set(vec_821))
        vec_index821 = 0
        # Program TableJoin Region
        while vec_index821 < len(vec_821):
            var_823 = vec_821[vec_index821]
            vec_index821 += 1
            tuple_822_0_index: int = 0
            tuple_822_0_vec: List[Tuple[int, bytes, bytes]] = self.index_240[var_823]
            while tuple_822_0_index < len(tuple_822_0_vec):
                tuple_822_0 = tuple_822_0_vec[tuple_822_0_index]
                tuple_822_0_index += 1
                var_824 = tuple_822_0[0]
                var_825 = tuple_822_0[1]
                var_826 = tuple_822_0[2]
                tuple_822_1_index: int = 0
                tuple_822_1_vec: List[int] = self.index_232[var_823]
                while tuple_822_1_index < len(tuple_822_1_vec):
                    tuple_822_1 = tuple_822_1_vec[tuple_822_1_index]
                    tuple_822_1_index += 1
                    var_827 = tuple_822_1
                    # Program TupleCompare Region
                    if self.var_1 == var_824:
                        # Program TransitionState Region
                        tuple_1_823_825_826_827 = (self.var_1, var_823, var_825, var_826, var_827)
                        prev_state = self.table_116[tuple_1_823_825_826_827]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_116[tuple_1_823_825_826_827] = 1 | 4
                            if not present_bit:
                                self.index_249[tuple_1_823_825_826_827[4]].append((tuple_1_823_825_826_827[0], tuple_1_823_825_826_827[1], tuple_1_823_825_826_827[2], tuple_1_823_825_826_827[3]))
                            # Program VectorAppend Region
                            vec_828.append(var_827)
        # Program VectorClear Region
        del vec_821[:]
        vec_index821 = 0
        # Program VectorUnique Region
        vec_828 = list(set(vec_828))
        vec_index828 = 0
        # Program TableJoin Region
        while vec_index828 < len(vec_828):
            var_830 = vec_828[vec_index828]
            vec_index828 += 1
            tuple_829_0_index: int = 0
            tuple_829_0_vec: List[int] = self.index_248[var_830]
            while tuple_829_0_index < len(tuple_829_0_vec):
                tuple_829_0 = tuple_829_0_vec[tuple_829_0_index]
                tuple_829_0_index += 1
                var_831 = tuple_829_0
                tuple_829_1_index: int = 0
                tuple_829_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_249[var_830]
                while tuple_829_1_index < len(tuple_829_1_vec):
                    tuple_829_1 = tuple_829_1_vec[tuple_829_1_index]
                    tuple_829_1_index += 1
                    var_832 = tuple_829_1[0]
                    var_833 = tuple_829_1[1]
                    var_834 = tuple_829_1[2]
                    var_835 = tuple_829_1[3]
                    # Program TupleCompare Region
                    if self.var_1 == var_832:
                        # Program TransitionState Region
                        tuple_1_830_831_833_834_835 = (self.var_1, var_830, var_831, var_833, var_834, var_835)
                        prev_state = self.table_122[tuple_1_830_831_833_834_835]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_122[tuple_1_830_831_833_834_835] = 1 | 4
                            if not present_bit:
                                self.index_303[tuple_1_830_831_833_834_835[2]].append((tuple_1_830_831_833_834_835[0], tuple_1_830_831_833_834_835[1], tuple_1_830_831_833_834_835[3], tuple_1_830_831_833_834_835[4], tuple_1_830_831_833_834_835[5]))
                            # Program VectorAppend Region
                            vec_862.append(var_831)
        # Program VectorClear Region
        del vec_828[:]
        vec_index828 = 0
        # Program VectorUnique Region
        vec_836 = list(set(vec_836))
        vec_index836 = 0
        # Program TableJoin Region
        while vec_index836 < len(vec_836):
            var_838 = vec_836[vec_index836]
            vec_index836 += 1
            tuple_837_0_index: int = 0
            tuple_837_0_vec: List[int] = self.index_248[var_838]
            while tuple_837_0_index < len(tuple_837_0_vec):
                tuple_837_0 = tuple_837_0_vec[tuple_837_0_index]
                tuple_837_0_index += 1
                var_839 = tuple_837_0
                tuple_837_1_index: int = 0
                tuple_837_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_258[var_838]
                while tuple_837_1_index < len(tuple_837_1_vec):
                    tuple_837_1 = tuple_837_1_vec[tuple_837_1_index]
                    tuple_837_1_index += 1
                    var_840 = tuple_837_1[0]
                    var_841 = tuple_837_1[1]
                    var_842 = tuple_837_1[2]
                    var_843 = tuple_837_1[3]
                    # Program TupleCompare Region
                    if self.var_4 == var_840:
                        # Program TransitionState Region
                        tuple_4_838_839_841_842_843 = (self.var_4, var_838, var_839, var_841, var_842, var_843)
                        prev_state = self.table_140[tuple_4_838_839_841_842_843]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_140[tuple_4_838_839_841_842_843] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_4_838_839_841_842_843[2]].append((tuple_4_838_839_841_842_843[0], tuple_4_838_839_841_842_843[1], tuple_4_838_839_841_842_843[3], tuple_4_838_839_841_842_843[4], tuple_4_838_839_841_842_843[5]))
                            # Program VectorAppend Region
                            vec_844.append(var_839)
        # Program VectorClear Region
        del vec_836[:]
        vec_index836 = 0
        # Program VectorUnique Region
        vec_844 = list(set(vec_844))
        vec_index844 = 0
        # Program TableJoin Region
        while vec_index844 < len(vec_844):
            var_846 = vec_844[vec_index844]
            vec_index844 += 1
            if var_846 in self.index_267:
                tuple_845_1_index: int = 0
                tuple_845_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_287[var_846]
                while tuple_845_1_index < len(tuple_845_1_vec):
                    tuple_845_1 = tuple_845_1_vec[tuple_845_1_index]
                    tuple_845_1_index += 1
                    var_847 = tuple_845_1[0]
                    var_848 = tuple_845_1[1]
                    var_849 = tuple_845_1[2]
                    var_850 = tuple_845_1[3]
                    var_851 = tuple_845_1[4]
                    # Program TupleCompare Region
                    if self.var_4 == var_847:
                        # Program TransitionState Region
                        tuple_849_846_0 = (var_849, var_846, self.var_0)
                        prev_state = self.table_43[tuple_849_846_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_849_846_0] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_849_846_0[1]].append((tuple_849_846_0[0], tuple_849_846_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_846_849_0 = (var_846, var_849, self.var_0)
                            prev_state = self.table_26[tuple_846_849_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_846_849_0] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_846_849_0[0]].append((tuple_846_849_0[1], tuple_846_849_0[2]))
                                    self.index_1053[(tuple_846_849_0[0], tuple_846_849_0[1])].append(tuple_846_849_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_846)
                            if not ret:
                                # Program TransitionState Region
                                tuple_846_849_0 = (var_846, var_849, self.var_0)
                                prev_state = self.table_26[tuple_846_849_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_846_849_0] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_846_849_0[0]].append((tuple_846_849_0[1], tuple_846_849_0[2]))
                                        self.index_1053[(tuple_846_849_0[0], tuple_846_849_0[1])].append(tuple_846_849_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_849, var_846)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_849_846 = (var_849, var_846)
                                        prev_state = self.table_9[tuple_849_846]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_849_846] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_849_846[0]].append(tuple_849_846[1])
                                                self.index_1079[tuple_849_846[1]].append(tuple_849_846[0])
                                            # Program VectorAppend Region
                                            vec_913.append(var_849)
                            # Program VectorAppend Region
                            vec_877.append(var_846)
                            # Program VectorAppend Region
                            vec_908.append(var_846)
                            # Program TransitionState Region
                            tuple_846 = var_846
                            prev_state = self.table_17[tuple_846]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_17[tuple_846] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_858: Tuple[int, int]
                                scan_index_858: int = 0
                                scan_tuple_858_vec: List[Tuple[int, int]] = self.index_199[var_846]
                                while scan_index_858 < len(scan_tuple_858_vec):
                                    scan_tuple_858 = scan_tuple_858_vec[scan_index_858]
                                    scan_index_858 += 1
                                    vec_858.append(scan_tuple_858)
                                # Program VectorLoop Region
                                vec_index858 = 0
                                while vec_index858 < len(vec_858):
                                    var_859, var_860 = vec_858[vec_index858]
                                    vec_index858 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_860 = self._resolve_edgetype(var_860)
                                    tuple_846_859_860 = (var_846, var_859, var_860)
                                    prev_state = self.table_26[tuple_846_859_860]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_846_859_860] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_203_(var_846, var_859, var_860)

                                # Program TransitionState Region
                                tuple_846_846 = (var_846, var_846)
                                prev_state = self.table_6[tuple_846_846]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_846_846] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_846_846[1]].append(tuple_846_846[0])
                                        self.index_1029[tuple_846_846[0]].append(tuple_846_846[1])
                                    # Program VectorAppend Region
                                    vec_855.append((var_846, var_846))
                                # Program VectorAppend Region
                                vec_908.append(var_846)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_849_846 = (self.var_0, var_849, var_846)
                                prev_state = self.table_56[tuple_0_849_846]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_849_846] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_0_849_846[1]].append((tuple_0_849_846[0], tuple_0_849_846[2]))
                                    # Program VectorAppend Region
                                    vec_887.append(var_849)
        # Program VectorClear Region
        del vec_844[:]
        vec_index844 = 0
        # Program VectorUnique Region
        vec_862 = list(set(vec_862))
        vec_index862 = 0
        # Program TableJoin Region
        while vec_index862 < len(vec_862):
            var_864 = vec_862[vec_index862]
            vec_index862 += 1
            if var_864 in self.index_267:
                tuple_863_1_index: int = 0
                tuple_863_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_303[var_864]
                while tuple_863_1_index < len(tuple_863_1_vec):
                    tuple_863_1 = tuple_863_1_vec[tuple_863_1_index]
                    tuple_863_1_index += 1
                    var_865 = tuple_863_1[0]
                    var_866 = tuple_863_1[1]
                    var_867 = tuple_863_1[2]
                    var_868 = tuple_863_1[3]
                    var_869 = tuple_863_1[4]
                    # Program TupleCompare Region
                    if self.var_1 == var_865:
                        # Program TransitionState Region
                        tuple_867_864_2 = (var_867, var_864, self.var_2)
                        prev_state = self.table_43[tuple_867_864_2]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_867_864_2] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_867_864_2[1]].append((tuple_867_864_2[0], tuple_867_864_2[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_864_867_2 = (var_864, var_867, self.var_2)
                            prev_state = self.table_26[tuple_864_867_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_864_867_2] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_864_867_2[0]].append((tuple_864_867_2[1], tuple_864_867_2[2]))
                                    self.index_1053[(tuple_864_867_2[0], tuple_864_867_2[1])].append(tuple_864_867_2[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_864)
                            if not ret:
                                # Program TransitionState Region
                                tuple_864_867_2 = (var_864, var_867, self.var_2)
                                prev_state = self.table_26[tuple_864_867_2]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_864_867_2] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_864_867_2[0]].append((tuple_864_867_2[1], tuple_864_867_2[2]))
                                        self.index_1053[(tuple_864_867_2[0], tuple_864_867_2[1])].append(tuple_864_867_2[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_867, var_864)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_867_864 = (var_867, var_864)
                                        prev_state = self.table_9[tuple_867_864]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_867_864] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_867_864[0]].append(tuple_867_864[1])
                                                self.index_1079[tuple_867_864[1]].append(tuple_867_864[0])
                                            # Program VectorAppend Region
                                            vec_913.append(var_867)
                            # Program VectorAppend Region
                            vec_877.append(var_864)
                            # Program VectorAppend Region
                            vec_908.append(var_864)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_864 = var_864
                                prev_state = self.table_17[tuple_864]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_864] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_873: Tuple[int, int]
                                    scan_index_873: int = 0
                                    scan_tuple_873_vec: List[Tuple[int, int]] = self.index_199[var_864]
                                    while scan_index_873 < len(scan_tuple_873_vec):
                                        scan_tuple_873 = scan_tuple_873_vec[scan_index_873]
                                        scan_index_873 += 1
                                        vec_873.append(scan_tuple_873)
                                    # Program VectorLoop Region
                                    vec_index873 = 0
                                    while vec_index873 < len(vec_873):
                                        var_874, var_875 = vec_873[vec_index873]
                                        vec_index873 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_875 = self._resolve_edgetype(var_875)
                                        tuple_864_874_875 = (var_864, var_874, var_875)
                                        prev_state = self.table_26[tuple_864_874_875]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_864_874_875] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_864, var_874, var_875)

                                    # Program TransitionState Region
                                    tuple_864_864 = (var_864, var_864)
                                    prev_state = self.table_6[tuple_864_864]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_864_864] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_864_864[1]].append(tuple_864_864[0])
                                            self.index_1029[tuple_864_864[0]].append(tuple_864_864[1])
                                        # Program VectorAppend Region
                                        vec_855.append((var_864, var_864))
                                    # Program VectorAppend Region
                                    vec_908.append(var_864)
                            # Program TransitionState Region
                            tuple_2_867_864 = (self.var_2, var_867, var_864)
                            prev_state = self.table_56[tuple_2_867_864]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_56[tuple_2_867_864] = 1 | 4
                                if not present_bit:
                                    self.index_385[tuple_2_867_864[1]].append((tuple_2_867_864[0], tuple_2_867_864[2]))
                                # Program VectorAppend Region
                                vec_887.append(var_867)
        # Program VectorClear Region
        del vec_862[:]
        vec_index862 = 0
        # Program VectorUnique Region
        vec_877 = list(set(vec_877))
        vec_index877 = 0
        # Program TableJoin Region
        while vec_index877 < len(vec_877):
            var_879 = vec_877[vec_index877]
            vec_index877 += 1
            tuple_878_0_index: int = 0
            tuple_878_0_vec: List[bytes] = self.index_372[var_879]
            while tuple_878_0_index < len(tuple_878_0_vec):
                tuple_878_0 = tuple_878_0_vec[tuple_878_0_index]
                tuple_878_0_index += 1
                var_880 = tuple_878_0
                tuple_878_1_index: int = 0
                tuple_878_1_vec: List[Tuple[int, int]] = self.index_373[var_879]
                while tuple_878_1_index < len(tuple_878_1_vec):
                    tuple_878_1 = tuple_878_1_vec[tuple_878_1_index]
                    tuple_878_1_index += 1
                    var_881 = tuple_878_1[0]
                    var_882 = tuple_878_1[1]
                    # Program TransitionState Region
                    tuple_879 = var_879
                    prev_state = self.table_17[tuple_879]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_879] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_883: Tuple[int, int]
                        scan_index_883: int = 0
                        scan_tuple_883_vec: List[Tuple[int, int]] = self.index_199[var_879]
                        while scan_index_883 < len(scan_tuple_883_vec):
                            scan_tuple_883 = scan_tuple_883_vec[scan_index_883]
                            scan_index_883 += 1
                            vec_883.append(scan_tuple_883)
                        # Program VectorLoop Region
                        vec_index883 = 0
                        while vec_index883 < len(vec_883):
                            var_884, var_885 = vec_883[vec_index883]
                            vec_index883 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_885 = self._resolve_edgetype(var_885)
                            tuple_879_884_885 = (var_879, var_884, var_885)
                            prev_state = self.table_26[tuple_879_884_885]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_879_884_885] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_879, var_884, var_885)

                        # Program TransitionState Region
                        tuple_879_879 = (var_879, var_879)
                        prev_state = self.table_6[tuple_879_879]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_879_879] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_879_879[1]].append(tuple_879_879[0])
                                self.index_1029[tuple_879_879[0]].append(tuple_879_879[1])
                            # Program VectorAppend Region
                            vec_855.append((var_879, var_879))
                        # Program VectorAppend Region
                        vec_908.append(var_879)
        # Program VectorClear Region
        del vec_877[:]
        vec_index877 = 0
        # Program VectorUnique Region
        vec_887 = list(set(vec_887))
        vec_index887 = 0
        # Program TableJoin Region
        while vec_index887 < len(vec_887):
            var_889 = vec_887[vec_index887]
            vec_index887 += 1
            tuple_888_0_index: int = 0
            tuple_888_0_vec: List[Tuple[int, bytes, bytes]] = self.index_384[var_889]
            while tuple_888_0_index < len(tuple_888_0_vec):
                tuple_888_0 = tuple_888_0_vec[tuple_888_0_index]
                tuple_888_0_index += 1
                var_890 = tuple_888_0[0]
                var_891 = tuple_888_0[1]
                var_892 = tuple_888_0[2]
                tuple_888_1_index: int = 0
                tuple_888_1_vec: List[Tuple[int, int]] = self.index_385[var_889]
                while tuple_888_1_index < len(tuple_888_1_vec):
                    tuple_888_1 = tuple_888_1_vec[tuple_888_1_index]
                    tuple_888_1_index += 1
                    var_893 = tuple_888_1[0]
                    var_894 = tuple_888_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_890, var_893, ):
                        # Program TransitionState Region
                        tuple_2_1_889_891_892_894 = (self.var_2, self.var_1, var_889, var_891, var_892, var_894)
                        prev_state = self.table_60[tuple_2_1_889_891_892_894]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_889_891_892_894] = 1 | 4
                            if not present_bit:
                                self.index_394[tuple_2_1_889_891_892_894[5]].append((tuple_2_1_889_891_892_894[0], tuple_2_1_889_891_892_894[1], tuple_2_1_889_891_892_894[2], tuple_2_1_889_891_892_894[3], tuple_2_1_889_891_892_894[4]))
                            # Program VectorAppend Region
                            vec_895.append(var_894)
        # Program VectorClear Region
        del vec_887[:]
        vec_index887 = 0
        # Program VectorUnique Region
        vec_895 = list(set(vec_895))
        vec_index895 = 0
        # Program TableJoin Region
        while vec_index895 < len(vec_895):
            var_897 = vec_895[vec_index895]
            vec_index895 += 1
            tuple_896_0_index: int = 0
            tuple_896_0_vec: List[bytes] = self.index_372[var_897]
            while tuple_896_0_index < len(tuple_896_0_vec):
                tuple_896_0 = tuple_896_0_vec[tuple_896_0_index]
                tuple_896_0_index += 1
                var_898 = tuple_896_0
                tuple_896_1_index: int = 0
                tuple_896_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_394[var_897]
                while tuple_896_1_index < len(tuple_896_1_vec):
                    tuple_896_1 = tuple_896_1_vec[tuple_896_1_index]
                    tuple_896_1_index += 1
                    var_899 = tuple_896_1[0]
                    var_900 = tuple_896_1[1]
                    var_901 = tuple_896_1[2]
                    var_902 = tuple_896_1[3]
                    var_903 = tuple_896_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_900, var_899, ):
                        # Program TransitionState Region
                        tuple_901 = var_901
                        prev_state = self.table_17[tuple_901]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_17[tuple_901] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_904: Tuple[int, int]
                            scan_index_904: int = 0
                            scan_tuple_904_vec: List[Tuple[int, int]] = self.index_199[var_901]
                            while scan_index_904 < len(scan_tuple_904_vec):
                                scan_tuple_904 = scan_tuple_904_vec[scan_index_904]
                                scan_index_904 += 1
                                vec_904.append(scan_tuple_904)
                            # Program VectorLoop Region
                            vec_index904 = 0
                            while vec_index904 < len(vec_904):
                                var_905, var_906 = vec_904[vec_index904]
                                vec_index904 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_906 = self._resolve_edgetype(var_906)
                                tuple_901_905_906 = (var_901, var_905, var_906)
                                prev_state = self.table_26[tuple_901_905_906]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_901_905_906] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_203_(var_901, var_905, var_906)

                            # Program TransitionState Region
                            tuple_901_901 = (var_901, var_901)
                            prev_state = self.table_6[tuple_901_901]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_901_901] = 1 | 4
                                if not present_bit:
                                    self.index_414[tuple_901_901[1]].append(tuple_901_901[0])
                                    self.index_1029[tuple_901_901[0]].append(tuple_901_901[1])
                                # Program VectorAppend Region
                                vec_855.append((var_901, var_901))
                            # Program VectorAppend Region
                            vec_908.append(var_901)
        # Program VectorClear Region
        del vec_895[:]
        vec_index895 = 0
        # Program VectorUnique Region
        vec_908 = list(set(vec_908))
        vec_index908 = 0
        # Program TableJoin Region
        while vec_index908 < len(vec_908):
            var_910 = vec_908[vec_index908]
            vec_index908 += 1
            tuple_909_0_index: int = 0
            tuple_909_0_vec: List[Tuple[int, int]] = self.index_373[var_910]
            while tuple_909_0_index < len(tuple_909_0_vec):
                tuple_909_0 = tuple_909_0_vec[tuple_909_0_index]
                tuple_909_0_index += 1
                var_911 = tuple_909_0[0]
                var_912 = tuple_909_0[1]
                if var_910 in self.index_408:
                    # Program TransitionState Region
                    tuple_911_910 = (var_911, var_910)
                    prev_state = self.table_12[tuple_911_910]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_911_910] = 1 | 4
                        if not present_bit:
                            self.index_433[tuple_911_910[1]].append(tuple_911_910[0])
                            self.index_1028[tuple_911_910[0]].append(tuple_911_910[1])
                        # Program VectorAppend Region
                        vec_921.append(var_910)
        # Program VectorClear Region
        del vec_908[:]
        vec_index908 = 0
        # Program VectorUnique Region
        vec_913 = list(set(vec_913))
        vec_index913 = 0
        # Program TableJoin Region
        while vec_index913 < len(vec_913):
            var_915 = vec_913[vec_index913]
            vec_index913 += 1
            tuple_914_0_index: int = 0
            tuple_914_0_vec: List[int] = self.index_414[var_915]
            while tuple_914_0_index < len(tuple_914_0_vec):
                tuple_914_0 = tuple_914_0_vec[tuple_914_0_index]
                tuple_914_0_index += 1
                var_916 = tuple_914_0
                tuple_914_1_index: int = 0
                tuple_914_1_vec: List[int] = self.index_415[var_915]
                while tuple_914_1_index < len(tuple_914_1_vec):
                    tuple_914_1 = tuple_914_1_vec[tuple_914_1_index]
                    tuple_914_1_index += 1
                    var_917 = tuple_914_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_1030_(var_916, var_915)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_1033_(var_915, var_917)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_426_(var_916, var_917)
                            if not ret:
                                # Program TransitionState Region
                                tuple_916_917 = (var_916, var_917)
                                prev_state = self.table_6[tuple_916_917]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_916_917] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_916_917[1]].append(tuple_916_917[0])
                                        self.index_1029[tuple_916_917[0]].append(tuple_916_917[1])
                                    # Program VectorAppend Region
                                    vec_855.append((var_916, var_917))
        # Program VectorClear Region
        del vec_913[:]
        vec_index913 = 0
        # Program VectorUnique Region
        vec_921 = list(set(vec_921))
        vec_index921 = 0
        # Program TableJoin Region
        while vec_index921 < len(vec_921):
            var_923 = vec_921[vec_index921]
            vec_index921 += 1
            tuple_922_0_index: int = 0
            tuple_922_0_vec: List[int] = self.index_433[var_923]
            while tuple_922_0_index < len(tuple_922_0_vec):
                tuple_922_0 = tuple_922_0_vec[tuple_922_0_index]
                tuple_922_0_index += 1
                var_924 = tuple_922_0
                tuple_922_1_index: int = 0
                tuple_922_1_vec: List[bytes] = self.index_372[var_923]
                while tuple_922_1_index < len(tuple_922_1_vec):
                    tuple_922_1 = tuple_922_1_vec[tuple_922_1_index]
                    tuple_922_1_index += 1
                    var_925 = tuple_922_1
                    # Program TransitionState Region
                    tuple_924 = var_924
                    prev_state = self.table_15[tuple_924]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_924] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_921[:]
        vec_index921 = 0
        # Induction Fixpoint Loop Region
        while len(vec_855):
            # Program Call Region
            param_857_0 = [vec_855]
            ret = self.proc_192_(param_857_0)
            vec_855 = param_857_0[0]

        vec_index855 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_855[:]
        vec_index855 = 0
        # Program Return Region
        return False

    def relocation_2(self, vec_927: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index927: int = 0
        vec_930: List[int] = list()
        vec_index930: int = 0
        vec_938: List[int] = list()
        vec_index938: int = 0
        vec_946: List[int] = list()
        vec_index946: int = 0
        vec_957: List[Tuple[int, int]] = list()
        vec_index957: int = 0
        vec_960: List[Tuple[int, int]] = list()
        vec_index960: int = 0
        vec_964: List[int] = list()
        vec_index964: int = 0
        vec_975: List[Tuple[int, int]] = list()
        vec_index975: int = 0
        vec_979: List[int] = list()
        vec_index979: int = 0
        vec_985: List[Tuple[int, int]] = list()
        vec_index985: int = 0
        vec_989: List[int] = list()
        vec_index989: int = 0
        vec_997: List[int] = list()
        vec_index997: int = 0
        vec_1006: List[Tuple[int, int]] = list()
        vec_index1006: int = 0
        vec_1010: List[int] = list()
        vec_index1010: int = 0
        vec_1015: List[int] = list()
        vec_index1015: int = 0
        vec_1023: List[int] = list()
        vec_index1023: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index927 = 0
        while vec_index927 < len(vec_927):
            var_928, var_929 = vec_927[vec_index927]
            vec_index927 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_928_929 = (var_928, var_929)
            prev_state = self.table_113[tuple_928_929]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_113[tuple_928_929] = 1 | 4
                if not present_bit:
                    self.index_248[tuple_928_929[0]].append(tuple_928_929[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_938.append(var_928)
                # Program VectorAppend Region
                vec_930.append(var_928)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_928_929 = (var_928, var_929)
            prev_state = self.table_113[tuple_928_929]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_113[tuple_928_929] = 1 | 4
                if not present_bit:
                    self.index_248[tuple_928_929[0]].append(tuple_928_929[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_938.append(var_928)
                # Program VectorAppend Region
                vec_930.append(var_928)
        # Program VectorUnique Region
        vec_930 = list(set(vec_930))
        vec_index930 = 0
        # Program TableJoin Region
        while vec_index930 < len(vec_930):
            var_932 = vec_930[vec_index930]
            vec_index930 += 1
            tuple_931_0_index: int = 0
            tuple_931_0_vec: List[int] = self.index_248[var_932]
            while tuple_931_0_index < len(tuple_931_0_vec):
                tuple_931_0 = tuple_931_0_vec[tuple_931_0_index]
                tuple_931_0_index += 1
                var_933 = tuple_931_0
                tuple_931_1_index: int = 0
                tuple_931_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_258[var_932]
                while tuple_931_1_index < len(tuple_931_1_vec):
                    tuple_931_1 = tuple_931_1_vec[tuple_931_1_index]
                    tuple_931_1_index += 1
                    var_934 = tuple_931_1[0]
                    var_935 = tuple_931_1[1]
                    var_936 = tuple_931_1[2]
                    var_937 = tuple_931_1[3]
                    # Program TupleCompare Region
                    if self.var_4 == var_934:
                        # Program TransitionState Region
                        tuple_4_932_933_935_936_937 = (self.var_4, var_932, var_933, var_935, var_936, var_937)
                        prev_state = self.table_140[tuple_4_932_933_935_936_937]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_140[tuple_4_932_933_935_936_937] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_4_932_933_935_936_937[2]].append((tuple_4_932_933_935_936_937[0], tuple_4_932_933_935_936_937[1], tuple_4_932_933_935_936_937[3], tuple_4_932_933_935_936_937[4], tuple_4_932_933_935_936_937[5]))
                            # Program VectorAppend Region
                            vec_964.append(var_933)
        # Program VectorClear Region
        del vec_930[:]
        vec_index930 = 0
        # Program VectorUnique Region
        vec_938 = list(set(vec_938))
        vec_index938 = 0
        # Program TableJoin Region
        while vec_index938 < len(vec_938):
            var_940 = vec_938[vec_index938]
            vec_index938 += 1
            tuple_939_0_index: int = 0
            tuple_939_0_vec: List[int] = self.index_248[var_940]
            while tuple_939_0_index < len(tuple_939_0_vec):
                tuple_939_0 = tuple_939_0_vec[tuple_939_0_index]
                tuple_939_0_index += 1
                var_941 = tuple_939_0
                tuple_939_1_index: int = 0
                tuple_939_1_vec: List[Tuple[int, int, bytes, bytes]] = self.index_249[var_940]
                while tuple_939_1_index < len(tuple_939_1_vec):
                    tuple_939_1 = tuple_939_1_vec[tuple_939_1_index]
                    tuple_939_1_index += 1
                    var_942 = tuple_939_1[0]
                    var_943 = tuple_939_1[1]
                    var_944 = tuple_939_1[2]
                    var_945 = tuple_939_1[3]
                    # Program TupleCompare Region
                    if self.var_1 == var_942:
                        # Program TransitionState Region
                        tuple_1_940_941_943_944_945 = (self.var_1, var_940, var_941, var_943, var_944, var_945)
                        prev_state = self.table_122[tuple_1_940_941_943_944_945]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_122[tuple_1_940_941_943_944_945] = 1 | 4
                            if not present_bit:
                                self.index_303[tuple_1_940_941_943_944_945[2]].append((tuple_1_940_941_943_944_945[0], tuple_1_940_941_943_944_945[1], tuple_1_940_941_943_944_945[3], tuple_1_940_941_943_944_945[4], tuple_1_940_941_943_944_945[5]))
                            # Program VectorAppend Region
                            vec_946.append(var_941)
        # Program VectorClear Region
        del vec_938[:]
        vec_index938 = 0
        # Program VectorUnique Region
        vec_946 = list(set(vec_946))
        vec_index946 = 0
        # Program TableJoin Region
        while vec_index946 < len(vec_946):
            var_948 = vec_946[vec_index946]
            vec_index946 += 1
            if var_948 in self.index_267:
                tuple_947_1_index: int = 0
                tuple_947_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_303[var_948]
                while tuple_947_1_index < len(tuple_947_1_vec):
                    tuple_947_1 = tuple_947_1_vec[tuple_947_1_index]
                    tuple_947_1_index += 1
                    var_949 = tuple_947_1[0]
                    var_950 = tuple_947_1[1]
                    var_951 = tuple_947_1[2]
                    var_952 = tuple_947_1[3]
                    var_953 = tuple_947_1[4]
                    # Program TupleCompare Region
                    if self.var_1 == var_949:
                        # Program TransitionState Region
                        tuple_951_948_2 = (var_951, var_948, self.var_2)
                        prev_state = self.table_43[tuple_951_948_2]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_951_948_2] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_951_948_2[1]].append((tuple_951_948_2[0], tuple_951_948_2[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_948_951_2 = (var_948, var_951, self.var_2)
                            prev_state = self.table_26[tuple_948_951_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_948_951_2] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_948_951_2[0]].append((tuple_948_951_2[1], tuple_948_951_2[2]))
                                    self.index_1053[(tuple_948_951_2[0], tuple_948_951_2[1])].append(tuple_948_951_2[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_948)
                            if not ret:
                                # Program TransitionState Region
                                tuple_948_951_2 = (var_948, var_951, self.var_2)
                                prev_state = self.table_26[tuple_948_951_2]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_948_951_2] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_948_951_2[0]].append((tuple_948_951_2[1], tuple_948_951_2[2]))
                                        self.index_1053[(tuple_948_951_2[0], tuple_948_951_2[1])].append(tuple_948_951_2[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_951, var_948)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_951_948 = (var_951, var_948)
                                        prev_state = self.table_9[tuple_951_948]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_951_948] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_951_948[0]].append(tuple_951_948[1])
                                                self.index_1079[tuple_951_948[1]].append(tuple_951_948[0])
                                            # Program VectorAppend Region
                                            vec_1015.append(var_951)
                            # Program VectorAppend Region
                            vec_979.append(var_948)
                            # Program VectorAppend Region
                            vec_1010.append(var_948)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_948 = var_948
                                prev_state = self.table_17[tuple_948]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_948] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program Parallel Region
                                    # Program Series Region
                                    # Program TableScan Region
                                    scan_tuple_960: Tuple[int, int]
                                    scan_index_960: int = 0
                                    scan_tuple_960_vec: List[Tuple[int, int]] = self.index_199[var_948]
                                    while scan_index_960 < len(scan_tuple_960_vec):
                                        scan_tuple_960 = scan_tuple_960_vec[scan_index_960]
                                        scan_index_960 += 1
                                        vec_960.append(scan_tuple_960)
                                    # Program VectorLoop Region
                                    vec_index960 = 0
                                    while vec_index960 < len(vec_960):
                                        var_961, var_962 = vec_960[vec_index960]
                                        vec_index960 += 1
                                        # Program TransitionState Region
                                        # Remove from negated view
                                        var_962 = self._resolve_edgetype(var_962)
                                        tuple_948_961_962 = (var_948, var_961, var_962)
                                        prev_state = self.table_26[tuple_948_961_962]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 1:
                                            self.table_26[tuple_948_961_962] = 0 | 4
                                            # Program Call Region
                                            ret = self.proc_203_(var_948, var_961, var_962)

                                    # Program TransitionState Region
                                    tuple_948_948 = (var_948, var_948)
                                    prev_state = self.table_6[tuple_948_948]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_6[tuple_948_948] = 1 | 4
                                        if not present_bit:
                                            self.index_414[tuple_948_948[1]].append(tuple_948_948[0])
                                            self.index_1029[tuple_948_948[0]].append(tuple_948_948[1])
                                        # Program VectorAppend Region
                                        vec_957.append((var_948, var_948))
                                    # Program VectorAppend Region
                                    vec_1010.append(var_948)
                            # Program TransitionState Region
                            tuple_2_951_948 = (self.var_2, var_951, var_948)
                            prev_state = self.table_56[tuple_2_951_948]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_56[tuple_2_951_948] = 1 | 4
                                if not present_bit:
                                    self.index_385[tuple_2_951_948[1]].append((tuple_2_951_948[0], tuple_2_951_948[2]))
                                # Program VectorAppend Region
                                vec_989.append(var_951)
        # Program VectorClear Region
        del vec_946[:]
        vec_index946 = 0
        # Program VectorUnique Region
        vec_964 = list(set(vec_964))
        vec_index964 = 0
        # Program TableJoin Region
        while vec_index964 < len(vec_964):
            var_966 = vec_964[vec_index964]
            vec_index964 += 1
            if var_966 in self.index_267:
                tuple_965_1_index: int = 0
                tuple_965_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_287[var_966]
                while tuple_965_1_index < len(tuple_965_1_vec):
                    tuple_965_1 = tuple_965_1_vec[tuple_965_1_index]
                    tuple_965_1_index += 1
                    var_967 = tuple_965_1[0]
                    var_968 = tuple_965_1[1]
                    var_969 = tuple_965_1[2]
                    var_970 = tuple_965_1[3]
                    var_971 = tuple_965_1[4]
                    # Program TupleCompare Region
                    if self.var_4 == var_967:
                        # Program TransitionState Region
                        tuple_969_966_0 = (var_969, var_966, self.var_0)
                        prev_state = self.table_43[tuple_969_966_0]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_43[tuple_969_966_0] = 1 | 4
                            if not present_bit:
                                self.index_373[tuple_969_966_0[1]].append((tuple_969_966_0[0], tuple_969_966_0[2]))
                            # Program Parallel Region
                            # Program Series Region
                            # Program TransitionState Region
                            # Eager insert before negation to prevent race
                            tuple_966_969_0 = (var_966, var_969, self.var_0)
                            prev_state = self.table_26[tuple_966_969_0]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0:
                                self.table_26[tuple_966_969_0] = 2 | 4
                                if not present_bit:
                                    self.index_199[tuple_966_969_0[0]].append((tuple_966_969_0[1], tuple_966_969_0[2]))
                                    self.index_1053[(tuple_966_969_0[0], tuple_966_969_0[1])].append(tuple_966_969_0[2])
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                            ret = self.proc_273_(var_966)
                            if not ret:
                                # Program TransitionState Region
                                tuple_966_969_0 = (var_966, var_969, self.var_0)
                                prev_state = self.table_26[tuple_966_969_0]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_26[tuple_966_969_0] = 1 | 4
                                    if not present_bit:
                                        self.index_199[tuple_966_969_0[0]].append((tuple_966_969_0[1], tuple_966_969_0[2]))
                                        self.index_1053[(tuple_966_969_0[0], tuple_966_969_0[1])].append(tuple_966_969_0[2])
                                    # Program Call Region
                                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                    ret = self.proc_276_(var_969, var_966)
                                    if not ret:
                                        # Program TransitionState Region
                                        tuple_969_966 = (var_969, var_966)
                                        prev_state = self.table_9[tuple_969_966]
                                        state = prev_state & 3
                                        present_bit = prev_state & 4
                                        if state == 0 or state == 2:
                                            self.table_9[tuple_969_966] = 1 | 4
                                            if not present_bit:
                                                self.index_415[tuple_969_966[0]].append(tuple_969_966[1])
                                                self.index_1079[tuple_969_966[1]].append(tuple_969_966[0])
                                            # Program VectorAppend Region
                                            vec_1015.append(var_969)
                            # Program VectorAppend Region
                            vec_979.append(var_966)
                            # Program VectorAppend Region
                            vec_1010.append(var_966)
                            # Program TransitionState Region
                            tuple_966 = var_966
                            prev_state = self.table_17[tuple_966]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_17[tuple_966] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_975: Tuple[int, int]
                                scan_index_975: int = 0
                                scan_tuple_975_vec: List[Tuple[int, int]] = self.index_199[var_966]
                                while scan_index_975 < len(scan_tuple_975_vec):
                                    scan_tuple_975 = scan_tuple_975_vec[scan_index_975]
                                    scan_index_975 += 1
                                    vec_975.append(scan_tuple_975)
                                # Program VectorLoop Region
                                vec_index975 = 0
                                while vec_index975 < len(vec_975):
                                    var_976, var_977 = vec_975[vec_index975]
                                    vec_index975 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    var_977 = self._resolve_edgetype(var_977)
                                    tuple_966_976_977 = (var_966, var_976, var_977)
                                    prev_state = self.table_26[tuple_966_976_977]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_26[tuple_966_976_977] = 0 | 4
                                        # Program Call Region
                                        ret = self.proc_203_(var_966, var_976, var_977)

                                # Program TransitionState Region
                                tuple_966_966 = (var_966, var_966)
                                prev_state = self.table_6[tuple_966_966]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_966_966] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_966_966[1]].append(tuple_966_966[0])
                                        self.index_1029[tuple_966_966[0]].append(tuple_966_966[1])
                                    # Program VectorAppend Region
                                    vec_957.append((var_966, var_966))
                                # Program VectorAppend Region
                                vec_1010.append(var_966)
                            # Program TupleCompare Region
                            if self.var_0 == self.var_2:
                                # Program TransitionState Region
                                tuple_0_969_966 = (self.var_0, var_969, var_966)
                                prev_state = self.table_56[tuple_0_969_966]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_56[tuple_0_969_966] = 1 | 4
                                    if not present_bit:
                                        self.index_385[tuple_0_969_966[1]].append((tuple_0_969_966[0], tuple_0_969_966[2]))
                                    # Program VectorAppend Region
                                    vec_989.append(var_969)
        # Program VectorClear Region
        del vec_964[:]
        vec_index964 = 0
        # Program VectorUnique Region
        vec_979 = list(set(vec_979))
        vec_index979 = 0
        # Program TableJoin Region
        while vec_index979 < len(vec_979):
            var_981 = vec_979[vec_index979]
            vec_index979 += 1
            tuple_980_0_index: int = 0
            tuple_980_0_vec: List[bytes] = self.index_372[var_981]
            while tuple_980_0_index < len(tuple_980_0_vec):
                tuple_980_0 = tuple_980_0_vec[tuple_980_0_index]
                tuple_980_0_index += 1
                var_982 = tuple_980_0
                tuple_980_1_index: int = 0
                tuple_980_1_vec: List[Tuple[int, int]] = self.index_373[var_981]
                while tuple_980_1_index < len(tuple_980_1_vec):
                    tuple_980_1 = tuple_980_1_vec[tuple_980_1_index]
                    tuple_980_1_index += 1
                    var_983 = tuple_980_1[0]
                    var_984 = tuple_980_1[1]
                    # Program TransitionState Region
                    tuple_981 = var_981
                    prev_state = self.table_17[tuple_981]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_981] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_985: Tuple[int, int]
                        scan_index_985: int = 0
                        scan_tuple_985_vec: List[Tuple[int, int]] = self.index_199[var_981]
                        while scan_index_985 < len(scan_tuple_985_vec):
                            scan_tuple_985 = scan_tuple_985_vec[scan_index_985]
                            scan_index_985 += 1
                            vec_985.append(scan_tuple_985)
                        # Program VectorLoop Region
                        vec_index985 = 0
                        while vec_index985 < len(vec_985):
                            var_986, var_987 = vec_985[vec_index985]
                            vec_index985 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            var_987 = self._resolve_edgetype(var_987)
                            tuple_981_986_987 = (var_981, var_986, var_987)
                            prev_state = self.table_26[tuple_981_986_987]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_26[tuple_981_986_987] = 0 | 4
                                # Program Call Region
                                ret = self.proc_203_(var_981, var_986, var_987)

                        # Program TransitionState Region
                        tuple_981_981 = (var_981, var_981)
                        prev_state = self.table_6[tuple_981_981]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_981_981] = 1 | 4
                            if not present_bit:
                                self.index_414[tuple_981_981[1]].append(tuple_981_981[0])
                                self.index_1029[tuple_981_981[0]].append(tuple_981_981[1])
                            # Program VectorAppend Region
                            vec_957.append((var_981, var_981))
                        # Program VectorAppend Region
                        vec_1010.append(var_981)
        # Program VectorClear Region
        del vec_979[:]
        vec_index979 = 0
        # Program VectorUnique Region
        vec_989 = list(set(vec_989))
        vec_index989 = 0
        # Program TableJoin Region
        while vec_index989 < len(vec_989):
            var_991 = vec_989[vec_index989]
            vec_index989 += 1
            tuple_990_0_index: int = 0
            tuple_990_0_vec: List[Tuple[int, bytes, bytes]] = self.index_384[var_991]
            while tuple_990_0_index < len(tuple_990_0_vec):
                tuple_990_0 = tuple_990_0_vec[tuple_990_0_index]
                tuple_990_0_index += 1
                var_992 = tuple_990_0[0]
                var_993 = tuple_990_0[1]
                var_994 = tuple_990_0[2]
                tuple_990_1_index: int = 0
                tuple_990_1_vec: List[Tuple[int, int]] = self.index_385[var_991]
                while tuple_990_1_index < len(tuple_990_1_vec):
                    tuple_990_1 = tuple_990_1_vec[tuple_990_1_index]
                    tuple_990_1_index += 1
                    var_995 = tuple_990_1[0]
                    var_996 = tuple_990_1[1]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_992, var_995, ):
                        # Program TransitionState Region
                        tuple_2_1_991_993_994_996 = (self.var_2, self.var_1, var_991, var_993, var_994, var_996)
                        prev_state = self.table_60[tuple_2_1_991_993_994_996]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_60[tuple_2_1_991_993_994_996] = 1 | 4
                            if not present_bit:
                                self.index_394[tuple_2_1_991_993_994_996[5]].append((tuple_2_1_991_993_994_996[0], tuple_2_1_991_993_994_996[1], tuple_2_1_991_993_994_996[2], tuple_2_1_991_993_994_996[3], tuple_2_1_991_993_994_996[4]))
                            # Program VectorAppend Region
                            vec_997.append(var_996)
        # Program VectorClear Region
        del vec_989[:]
        vec_index989 = 0
        # Program VectorUnique Region
        vec_997 = list(set(vec_997))
        vec_index997 = 0
        # Program TableJoin Region
        while vec_index997 < len(vec_997):
            var_999 = vec_997[vec_index997]
            vec_index997 += 1
            tuple_998_0_index: int = 0
            tuple_998_0_vec: List[bytes] = self.index_372[var_999]
            while tuple_998_0_index < len(tuple_998_0_vec):
                tuple_998_0 = tuple_998_0_vec[tuple_998_0_index]
                tuple_998_0_index += 1
                var_1000 = tuple_998_0
                tuple_998_1_index: int = 0
                tuple_998_1_vec: List[Tuple[int, int, int, bytes, bytes]] = self.index_394[var_999]
                while tuple_998_1_index < len(tuple_998_1_vec):
                    tuple_998_1 = tuple_998_1_vec[tuple_998_1_index]
                    tuple_998_1_index += 1
                    var_1001 = tuple_998_1[0]
                    var_1002 = tuple_998_1[1]
                    var_1003 = tuple_998_1[2]
                    var_1004 = tuple_998_1[3]
                    var_1005 = tuple_998_1[4]
                    # Program TupleCompare Region
                    if (self.var_1, self.var_2, ) == (var_1002, var_1001, ):
                        # Program TransitionState Region
                        tuple_1003 = var_1003
                        prev_state = self.table_17[tuple_1003]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_17[tuple_1003] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_1006: Tuple[int, int]
                            scan_index_1006: int = 0
                            scan_tuple_1006_vec: List[Tuple[int, int]] = self.index_199[var_1003]
                            while scan_index_1006 < len(scan_tuple_1006_vec):
                                scan_tuple_1006 = scan_tuple_1006_vec[scan_index_1006]
                                scan_index_1006 += 1
                                vec_1006.append(scan_tuple_1006)
                            # Program VectorLoop Region
                            vec_index1006 = 0
                            while vec_index1006 < len(vec_1006):
                                var_1007, var_1008 = vec_1006[vec_index1006]
                                vec_index1006 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                var_1008 = self._resolve_edgetype(var_1008)
                                tuple_1003_1007_1008 = (var_1003, var_1007, var_1008)
                                prev_state = self.table_26[tuple_1003_1007_1008]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_26[tuple_1003_1007_1008] = 0 | 4
                                    # Program Call Region
                                    ret = self.proc_203_(var_1003, var_1007, var_1008)

                            # Program TransitionState Region
                            tuple_1003_1003 = (var_1003, var_1003)
                            prev_state = self.table_6[tuple_1003_1003]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_1003_1003] = 1 | 4
                                if not present_bit:
                                    self.index_414[tuple_1003_1003[1]].append(tuple_1003_1003[0])
                                    self.index_1029[tuple_1003_1003[0]].append(tuple_1003_1003[1])
                                # Program VectorAppend Region
                                vec_957.append((var_1003, var_1003))
                            # Program VectorAppend Region
                            vec_1010.append(var_1003)
        # Program VectorClear Region
        del vec_997[:]
        vec_index997 = 0
        # Program VectorUnique Region
        vec_1010 = list(set(vec_1010))
        vec_index1010 = 0
        # Program TableJoin Region
        while vec_index1010 < len(vec_1010):
            var_1012 = vec_1010[vec_index1010]
            vec_index1010 += 1
            tuple_1011_0_index: int = 0
            tuple_1011_0_vec: List[Tuple[int, int]] = self.index_373[var_1012]
            while tuple_1011_0_index < len(tuple_1011_0_vec):
                tuple_1011_0 = tuple_1011_0_vec[tuple_1011_0_index]
                tuple_1011_0_index += 1
                var_1013 = tuple_1011_0[0]
                var_1014 = tuple_1011_0[1]
                if var_1012 in self.index_408:
                    # Program TransitionState Region
                    tuple_1013_1012 = (var_1013, var_1012)
                    prev_state = self.table_12[tuple_1013_1012]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_12[tuple_1013_1012] = 1 | 4
                        if not present_bit:
                            self.index_433[tuple_1013_1012[1]].append(tuple_1013_1012[0])
                            self.index_1028[tuple_1013_1012[0]].append(tuple_1013_1012[1])
                        # Program VectorAppend Region
                        vec_1023.append(var_1012)
        # Program VectorClear Region
        del vec_1010[:]
        vec_index1010 = 0
        # Program VectorUnique Region
        vec_1015 = list(set(vec_1015))
        vec_index1015 = 0
        # Program TableJoin Region
        while vec_index1015 < len(vec_1015):
            var_1017 = vec_1015[vec_index1015]
            vec_index1015 += 1
            tuple_1016_0_index: int = 0
            tuple_1016_0_vec: List[int] = self.index_414[var_1017]
            while tuple_1016_0_index < len(tuple_1016_0_vec):
                tuple_1016_0 = tuple_1016_0_vec[tuple_1016_0_index]
                tuple_1016_0_index += 1
                var_1018 = tuple_1016_0
                tuple_1016_1_index: int = 0
                tuple_1016_1_vec: List[int] = self.index_415[var_1017]
                while tuple_1016_1_index < len(tuple_1016_1_vec):
                    tuple_1016_1 = tuple_1016_1_vec[tuple_1016_1_index]
                    tuple_1016_1_index += 1
                    var_1019 = tuple_1016_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_1030_(var_1018, var_1017)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_1033_(var_1017, var_1019)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_426_(var_1018, var_1019)
                            if not ret:
                                # Program TransitionState Region
                                tuple_1018_1019 = (var_1018, var_1019)
                                prev_state = self.table_6[tuple_1018_1019]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_1018_1019] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_1018_1019[1]].append(tuple_1018_1019[0])
                                        self.index_1029[tuple_1018_1019[0]].append(tuple_1018_1019[1])
                                    # Program VectorAppend Region
                                    vec_957.append((var_1018, var_1019))
        # Program VectorClear Region
        del vec_1015[:]
        vec_index1015 = 0
        # Program VectorUnique Region
        vec_1023 = list(set(vec_1023))
        vec_index1023 = 0
        # Program TableJoin Region
        while vec_index1023 < len(vec_1023):
            var_1025 = vec_1023[vec_index1023]
            vec_index1023 += 1
            tuple_1024_0_index: int = 0
            tuple_1024_0_vec: List[int] = self.index_433[var_1025]
            while tuple_1024_0_index < len(tuple_1024_0_vec):
                tuple_1024_0 = tuple_1024_0_vec[tuple_1024_0_index]
                tuple_1024_0_index += 1
                var_1026 = tuple_1024_0
                tuple_1024_1_index: int = 0
                tuple_1024_1_vec: List[bytes] = self.index_372[var_1025]
                while tuple_1024_1_index < len(tuple_1024_1_vec):
                    tuple_1024_1 = tuple_1024_1_vec[tuple_1024_1_index]
                    tuple_1024_1_index += 1
                    var_1027 = tuple_1024_1
                    # Program TransitionState Region
                    tuple_1026 = var_1026
                    prev_state = self.table_15[tuple_1026]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_1026] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_1023[:]
        vec_index1023 = 0
        # Induction Fixpoint Loop Region
        while len(vec_957):
            # Program Call Region
            param_959_0 = [vec_957]
            ret = self.proc_192_(param_959_0)
            vec_957 = param_959_0[0]

        vec_index957 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_957[:]
        vec_index957 = 0
        # Program Return Region
        return False

    def proc_1030_(self, var_1031: int, var_1032: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_1070_(var_1031, var_1032)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1033_(self, var_1034: int, var_1035: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_1037_(var_1034, var_1035)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1037_(self, var_1038: int, var_1039: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_9[(var_1038, var_1039)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_1038_1039 = (var_1038, var_1039)
            prev_state = self.table_9[tuple_1038_1039]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_9[tuple_1038_1039] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Union.cpp: BuildTopDownUnionChecker::call_preds
                ret = self.proc_1041_(var_1038, var_1039)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_1038_1039 = (var_1038, var_1039)
                    prev_state = self.table_9[tuple_1038_1039]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_1038_1039] = 1 | 4
                        if not present_bit:
                            self.index_415[tuple_1038_1039[0]].append(tuple_1038_1039[1])
                            self.index_1079[tuple_1038_1039[1]].append(tuple_1038_1039[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False

    def proc_1041_(self, var_1042: int, var_1043: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1045_(var_1042, var_1043)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1045_(self, var_1046: int, var_1047: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1049_(var_1047, var_1046)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1049_(self, var_1050: int, var_1051: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1054: List[int] = list()
        vec_index1054: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1054: int
        scan_index_1054: int = 0
        scan_tuple_1054_vec: List[int] = self.index_1053[var_1050, var_1051]
        while scan_index_1054 < len(scan_tuple_1054_vec):
            scan_tuple_1054 = scan_tuple_1054_vec[scan_index_1054]
            scan_index_1054 += 1
            vec_1054.append(scan_tuple_1054)
        # Program VectorLoop Region
        vec_index1054 = 0
        while vec_index1054 < len(vec_1054):
            var_1055 = vec_1054[vec_index1054]
            vec_index1054 += 1
            # Program CheckState Region
            state = self.table_26[(var_1050, var_1051, var_1055)] & 3
            if state == 0:
                # Program Return Region
                return False
            elif state == 1:
                # Program Series Region
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_273_(var_1050)
                if not ret:
                    # Program Return Region
                    return True
                # Program TransitionState Region
                var_1055 = self._resolve_edgetype(var_1055)
                tuple_1050_1051_1055 = (var_1050, var_1051, var_1055)
                prev_state = self.table_26[tuple_1050_1051_1055]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 1:
                    self.table_26[tuple_1050_1051_1055] = 0 | 4
            elif state == 2:
                # Program TransitionState Region
                var_1055 = self._resolve_edgetype(var_1055)
                tuple_1050_1051_1055 = (var_1050, var_1051, var_1055)
                prev_state = self.table_26[tuple_1050_1051_1055]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_26[tuple_1050_1051_1055] = 0 | 4
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                    ret = self.proc_273_(var_1050)
                    if not ret:
                        # Program Call Region
                        ret = self.proc_1060_(var_1051, var_1050, var_1055)
                        if ret:
                            # Program Return Region
                            return True
        # Program Return Region
        return False

    def proc_1060_(self, var_1061: int, var_1062: int, var_1063: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1065_(var_1061, var_1062, var_1063)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1065_(self, var_1066: int, var_1067: int, var_1068: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program CheckState Region
        state = self.table_43[(var_1066, var_1067, var_1068)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program Return Region
            return False

    def proc_1070_(self, var_1071: int, var_1072: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program CheckState Region
        state = self.table_6[(var_1071, var_1072)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program Return Region
            return False

    def proc_1074_(self, var_1075: int, var_1076: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1078: List[int] = list()
        vec_index1078: int = 0
        vec_1080: List[int] = list()
        vec_index1080: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1080: int
        scan_index_1080: int = 0
        scan_tuple_1080_vec: List[int] = self.index_1079[var_1076]
        while scan_index_1080 < len(scan_tuple_1080_vec):
            scan_tuple_1080 = scan_tuple_1080_vec[scan_index_1080]
            scan_index_1080 += 1
            vec_1080.append(scan_tuple_1080)
        # Program VectorLoop Region
        vec_index1080 = 0
        while vec_index1080 < len(vec_1080):
            var_1081 = vec_1080[vec_index1080]
            vec_index1080 += 1
            # Program VectorAppend Region
            vec_1078.append(var_1081)
        # Program VectorUnique Region
        vec_1078 = list(set(vec_1078))
        vec_index1078 = 0
        # Program TableJoin Region
        while vec_index1078 < len(vec_1078):
            var_1083 = vec_1078[vec_index1078]
            vec_index1078 += 1
            tuple_1082_0_index: int = 0
            tuple_1082_0_vec: List[int] = self.index_414[var_1083]
            while tuple_1082_0_index < len(tuple_1082_0_vec):
                tuple_1082_0 = tuple_1082_0_vec[tuple_1082_0_index]
                tuple_1082_0_index += 1
                var_1084 = tuple_1082_0
                tuple_1082_1_index: int = 0
                tuple_1082_1_vec: List[int] = self.index_415[var_1083]
                while tuple_1082_1_index < len(tuple_1082_1_vec):
                    tuple_1082_1 = tuple_1082_1_vec[tuple_1082_1_index]
                    tuple_1082_1_index += 1
                    var_1085 = tuple_1082_1
                    # Program TupleCompare Region
                    if (var_1075, var_1076, ) == (var_1084, var_1085, ):
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_1030_(var_1084, var_1083)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_1033_(var_1083, var_1085)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1078[:]
        vec_index1078 = 0
        # Program Return Region
        return False

    def proc_1091_(self, var_1092: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program CheckState Region
        state = self.table_17[var_1092] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program Return Region
            return False

    def proc_1110_(self, var_1111: int, var_1112: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Union.cpp: BuildTopDownUnionChecker::call_preds
        ret = self.proc_1041_(var_1111, var_1112)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1114_(self, var_1115: int, var_1116: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1118: List[int] = list()
        vec_index1118: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1118: int
        scan_index_1118: int = 0
        scan_tuple_1118_vec: List[int] = self.index_414[var_1115]
        while scan_index_1118 < len(scan_tuple_1118_vec):
            scan_tuple_1118 = scan_tuple_1118_vec[scan_index_1118]
            scan_index_1118 += 1
            vec_1118.append(scan_tuple_1118)
        # Program VectorLoop Region
        vec_index1118 = 0
        while vec_index1118 < len(vec_1118):
            var_1119 = vec_1118[vec_index1118]
            vec_index1118 += 1
            # Program Call Region
            ret = self.proc_1120_(var_1115, var_1119, var_1116)

        # Program Return Region
        return False

    def proc_1120_(self, var_1121: int, var_1122: int, var_1123: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1122_1123 = (var_1122, var_1123)
        prev_state = self.table_6[tuple_1122_1123]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_6[tuple_1122_1123] = 2 | 4
            # Program Call Region
            ret = self.proc_1133_(var_1122, var_1123)

        # Program Return Region
        return False

    def proc_1133_(self, var_1134: int, var_1135: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Union.cpp: CreateBottomUpUnionRemover
        ret = self.proc_1137_(var_1134, var_1135)
        if not ret:
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1150_(var_1134, var_1135)

            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1137_(var_1134, var_1135)

        # Program Return Region
        return False

    def proc_1137_(self, var_1138: int, var_1139: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1138_1139 = (var_1138, var_1139)
        prev_state = self.table_6[tuple_1138_1139]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_6[tuple_1138_1139] = 0 | 4
            # Program Parallel Region
            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_1157_(var_1138, var_1139)
            if ret:
                # Program Series Region
                # Program TransitionState Region
                tuple_1138_1139 = (var_1138, var_1139)
                prev_state = self.table_6[tuple_1138_1139]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_6[tuple_1138_1139] = 1 | 4
                    if not present_bit:
                        self.index_414[tuple_1138_1139[1]].append(tuple_1138_1139[0])
                        self.index_1029[tuple_1138_1139[0]].append(tuple_1138_1139[1])
                # Program Return Region
                return True
            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_1161_(var_1138, var_1139)
            if ret:
                # Program Series Region
                # Program TransitionState Region
                tuple_1138_1139 = (var_1138, var_1139)
                prev_state = self.table_6[tuple_1138_1139]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_6[tuple_1138_1139] = 1 | 4
                    if not present_bit:
                        self.index_414[tuple_1138_1139[1]].append(tuple_1138_1139[0])
                        self.index_1029[tuple_1138_1139[0]].append(tuple_1138_1139[1])
                # Program Return Region
                return True
        # Program Return Region
        return False

    def proc_1150_(self, var_1151: int, var_1152: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1154: List[int] = list()
        vec_index1154: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1154: int
        scan_index_1154: int = 0
        scan_tuple_1154_vec: List[int] = self.index_415[var_1152]
        while scan_index_1154 < len(scan_tuple_1154_vec):
            scan_tuple_1154 = scan_tuple_1154_vec[scan_index_1154]
            scan_index_1154 += 1
            vec_1154.append(scan_tuple_1154)
        # Program VectorLoop Region
        vec_index1154 = 0
        while vec_index1154 < len(vec_1154):
            var_1155 = vec_1154[vec_index1154]
            vec_index1154 += 1
            # Program Call Region
            ret = self.proc_1120_(var_1152, var_1151, var_1155)

        # Program Return Region
        return False

    def proc_1157_(self, var_1158: int, var_1159: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1174_(var_1158, var_1159)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1161_(self, var_1162: int, var_1163: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1165_(var_1162, var_1163)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1165_(self, var_1166: int, var_1167: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1169_(var_1166, var_1167)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1169_(self, var_1170: int, var_1171: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1074_(var_1170, var_1171)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1174_(self, var_1175: int, var_1176: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1178_(var_1175, var_1176)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def proc_1178_(self, var_1179: int, var_1180: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_273_(var_1180)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False

    def interproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_1028[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_12[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def function_instruction_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_1029[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_1030_(param_0, param_1):
                continue
            yield param_1

    def get_external_calls_f(self) -> Iterator[int]:
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

    def function_b(self, param_0: int) -> bool:
        state: int = 0
        tuple_index: int = 0
        if True:
            full_tuple = param_0
            state = self.table_17[full_tuple] & 3
            if state != 1:
                return False
            return True

    def function_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_17:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_17[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

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

    def intraproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_415[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_1033_(param_0, param_1):
                continue
            yield param_1

    def get_section_instructions_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_1036[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_23[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

