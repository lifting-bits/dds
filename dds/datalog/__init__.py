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
        self.index_350: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_948: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_9: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_991: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)

        self.table_13: DefaultDict[int, int] = defaultdict(int)

        self.table_15: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_944: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_18: DefaultDict[int, int] = defaultdict(int)
        self.index_340 = self.table_18

        self.table_20: DefaultDict[int, int] = defaultdict(int)

        self.table_22: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_952: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_25: DefaultDict[bytes, int] = defaultdict(int)

        self.table_27: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_128: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_30: DefaultDict[int, int] = defaultdict(int)
        self.index_235 = self.table_30

        self.table_32: DefaultDict[int, int] = defaultdict(int)
        self.index_217 = self.table_32

        self.table_34: DefaultDict[int, int] = defaultdict(int)
        self.index_197 = self.table_34

        self.table_36: DefaultDict[int, int] = defaultdict(int)
        self.index_127 = self.table_36

        self.table_38: DefaultDict[int, int] = defaultdict(int)
        self.index_189 = self.table_38

        self.table_40: DefaultDict[int, int] = defaultdict(int)
        self.index_181 = self.table_40

        self.table_42: DefaultDict[int, int] = defaultdict(int)
        self.index_173 = self.table_42

        self.table_44: DefaultDict[int, int] = defaultdict(int)
        self.index_165 = self.table_44

        self.table_46: DefaultDict[int, int] = defaultdict(int)
        self.index_157 = self.table_46

        self.table_48: DefaultDict[int, int] = defaultdict(int)
        self.index_149 = self.table_48

        self.table_50: DefaultDict[int, int] = defaultdict(int)
        self.index_126 = self.table_50

        self.table_52: DefaultDict[int, int] = defaultdict(int)
        self.index_316 = self.table_52

        self.table_54: DefaultDict[int, int] = defaultdict(int)
        self.index_317 = self.table_54

        self.table_56: DefaultDict[int, int] = defaultdict(int)
        self.index_211 = self.table_56

        self.table_58: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_325: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_61: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_330: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_64: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_351: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_970: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_67: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_216: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_71: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_280: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_74: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_696 = self.table_74
        self.index_701: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_77: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_697 = self.table_77
        self.index_702: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_80: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_268: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_83: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_206: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_86: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_243: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_89: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_262: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_92: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_304: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_95: DefaultDict[int, int] = defaultdict(int)
        self.index_205 = self.table_95

        self.table_97: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_244: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_100: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_292: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_103: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_250: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_106: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_339: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_109: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_345: DefaultDict[int, List[int]] = defaultdict(list)

        self.var_0: int = 5
        self.var_1: int = 2
        self.var_2: int = 1
        self.var_3: int = 6
        self.var_4: int = 6
        self.var_5: int = 0
        self.init_112_()

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

    def init_112_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False
        return False

    def section_3(self, vec_114: List[Tuple[bytes, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index114: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index114 = 0
        while vec_index114 < len(vec_114):
            var_115, var_116, var_117 = vec_114[vec_index114]
            vec_index114 += 1
            # Program TransitionState Region
            tuple_115 = var_115
            prev_state = self.table_25[tuple_115]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_25[tuple_115] = 1 | 4
                if not present_bit:
                    pass
        # Program Return Region
        return False
        return False

    def instruction_3(self, vec_119: List[Tuple[int, int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index119: int = 0
        vec_123: List[int] = list()
        vec_index123: int = 0
        vec_129: List[int] = list()
        vec_index129: int = 0
        vec_143: List[Tuple[int, int]] = list()
        vec_index143: int = 0
        vec_146: List[int] = list()
        vec_index146: int = 0
        vec_150: List[int] = list()
        vec_index150: int = 0
        vec_154: List[int] = list()
        vec_index154: int = 0
        vec_158: List[int] = list()
        vec_index158: int = 0
        vec_162: List[int] = list()
        vec_index162: int = 0
        vec_166: List[int] = list()
        vec_index166: int = 0
        vec_170: List[int] = list()
        vec_index170: int = 0
        vec_174: List[int] = list()
        vec_index174: int = 0
        vec_178: List[int] = list()
        vec_index178: int = 0
        vec_182: List[int] = list()
        vec_index182: int = 0
        vec_186: List[int] = list()
        vec_index186: int = 0
        vec_190: List[int] = list()
        vec_index190: int = 0
        vec_194: List[int] = list()
        vec_index194: int = 0
        vec_198: List[int] = list()
        vec_index198: int = 0
        vec_202: List[int] = list()
        vec_index202: int = 0
        vec_208: List[int] = list()
        vec_index208: int = 0
        vec_213: List[int] = list()
        vec_index213: int = 0
        vec_228: List[int] = list()
        vec_index228: int = 0
        vec_232: List[int] = list()
        vec_index232: int = 0
        vec_236: List[int] = list()
        vec_index236: int = 0
        vec_240: List[int] = list()
        vec_index240: int = 0
        vec_247: List[int] = list()
        vec_index247: int = 0
        vec_255: List[int] = list()
        vec_index255: int = 0
        vec_259: List[int] = list()
        vec_index259: int = 0
        vec_265: List[int] = list()
        vec_index265: int = 0
        vec_273: List[int] = list()
        vec_index273: int = 0
        vec_277: List[int] = list()
        vec_index277: int = 0
        vec_285: List[int] = list()
        vec_index285: int = 0
        vec_289: List[int] = list()
        vec_index289: int = 0
        vec_297: List[int] = list()
        vec_index297: int = 0
        vec_301: List[int] = list()
        vec_index301: int = 0
        vec_309: List[int] = list()
        vec_index309: int = 0
        vec_313: List[int] = list()
        vec_index313: int = 0
        vec_318: List[int] = list()
        vec_index318: int = 0
        vec_322: List[int] = list()
        vec_index322: int = 0
        vec_327: List[int] = list()
        vec_index327: int = 0
        vec_332: List[int] = list()
        vec_index332: int = 0
        vec_336: List[int] = list()
        vec_index336: int = 0
        vec_342: List[int] = list()
        vec_index342: int = 0
        vec_347: List[int] = list()
        vec_index347: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index119 = 0
        while vec_index119 < len(vec_119):
            var_120, var_121, var_122 = vec_119[vec_index119]
            vec_index119 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TupleCompare Region
            if self.var_4 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_95[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_95[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_202.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_20[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_20[tuple_120] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
            # Program TransitionState Region
            tuple_120 = var_120
            prev_state = self.table_36[tuple_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_120] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_32[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_120)
                    # Program VectorAppend Region
                    vec_213.append(var_120)
                    # Program VectorAppend Region
                    vec_277.append(var_120)
                    # Program VectorAppend Region
                    vec_265.append(var_120)
                    # Program VectorAppend Region
                    vec_301.append(var_120)
                    # Program VectorAppend Region
                    vec_289.append(var_120)
                    # Program VectorAppend Region
                    vec_247.append(var_120)
                # Program VectorAppend Region
                vec_194.append(var_120)
                # Program VectorAppend Region
                vec_186.append(var_120)
                # Program VectorAppend Region
                vec_178.append(var_120)
                # Program VectorAppend Region
                vec_170.append(var_120)
                # Program VectorAppend Region
                vec_162.append(var_120)
                # Program VectorAppend Region
                vec_154.append(var_120)
                # Program VectorAppend Region
                vec_146.append(var_120)
                # Program VectorAppend Region
                vec_123.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_121:
                # Program TransitionState Region
                tuple_120 = var_120
                prev_state = self.table_56[tuple_120]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_56[tuple_120] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_322.append(var_120)
                    # Program VectorAppend Region
                    vec_208.append(var_120)
        # Program VectorUnique Region
        vec_123 = list(set(vec_123))
        vec_index123 = 0
        # Program TableJoin Region
        while vec_index123 < len(vec_123):
            var_125 = vec_123[vec_index123]
            vec_index123 += 1
            if var_125 in self.index_126:
                if var_125 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_125 = var_125
                    prev_state = self.table_18[tuple_125]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_125] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_125)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_129: int
                        scan_index_129: int = 0
                        scan_tuple_129_vec: List[int] = self.index_128[var_125]
                        while scan_index_129 < len(scan_tuple_129_vec):
                            scan_tuple_129 = scan_tuple_129_vec[scan_index_129]
                            scan_index_129 += 1
                            vec_129.append(scan_tuple_129)
                        # Program VectorLoop Region
                        vec_index129 = 0
                        while vec_index129 < len(vec_129):
                            var_130 = vec_129[vec_index129]
                            vec_index129 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_125_130 = (var_125, var_130)
                            prev_state = self.table_27[tuple_125_130]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_125_130] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_125, var_130)

                                # Program Call Region
                                ret = self.proc_135_(var_125, var_130)

                        # Program TransitionState Region
                        tuple_125_125 = (var_125, var_125)
                        prev_state = self.table_6[tuple_125_125]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_125_125] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_125_125[1]].append(tuple_125_125[0])
                                self.index_948[tuple_125_125[0]].append(tuple_125_125[1])
                            # Program VectorAppend Region
                            vec_143.append((var_125, var_125))
        # Program VectorClear Region
        del vec_123[:]
        vec_index123 = 0
        # Program VectorUnique Region
        vec_146 = list(set(vec_146))
        vec_index146 = 0
        # Program TableJoin Region
        while vec_index146 < len(vec_146):
            var_148 = vec_146[vec_index146]
            vec_index146 += 1
            if var_148 in self.index_149:
                if var_148 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_148 = var_148
                    prev_state = self.table_18[tuple_148]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_148] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_148)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_150: int
                        scan_index_150: int = 0
                        scan_tuple_150_vec: List[int] = self.index_128[var_148]
                        while scan_index_150 < len(scan_tuple_150_vec):
                            scan_tuple_150 = scan_tuple_150_vec[scan_index_150]
                            scan_index_150 += 1
                            vec_150.append(scan_tuple_150)
                        # Program VectorLoop Region
                        vec_index150 = 0
                        while vec_index150 < len(vec_150):
                            var_151 = vec_150[vec_index150]
                            vec_index150 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_148_151 = (var_148, var_151)
                            prev_state = self.table_27[tuple_148_151]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_148_151] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_148, var_151)

                                # Program Call Region
                                ret = self.proc_135_(var_148, var_151)

                        # Program TransitionState Region
                        tuple_148_148 = (var_148, var_148)
                        prev_state = self.table_6[tuple_148_148]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_148_148] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_148_148[1]].append(tuple_148_148[0])
                                self.index_948[tuple_148_148[0]].append(tuple_148_148[1])
                            # Program VectorAppend Region
                            vec_143.append((var_148, var_148))
        # Program VectorClear Region
        del vec_146[:]
        vec_index146 = 0
        # Program VectorUnique Region
        vec_154 = list(set(vec_154))
        vec_index154 = 0
        # Program TableJoin Region
        while vec_index154 < len(vec_154):
            var_156 = vec_154[vec_index154]
            vec_index154 += 1
            if var_156 in self.index_157:
                if var_156 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_156 = var_156
                    prev_state = self.table_18[tuple_156]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_156] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_156)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_158: int
                        scan_index_158: int = 0
                        scan_tuple_158_vec: List[int] = self.index_128[var_156]
                        while scan_index_158 < len(scan_tuple_158_vec):
                            scan_tuple_158 = scan_tuple_158_vec[scan_index_158]
                            scan_index_158 += 1
                            vec_158.append(scan_tuple_158)
                        # Program VectorLoop Region
                        vec_index158 = 0
                        while vec_index158 < len(vec_158):
                            var_159 = vec_158[vec_index158]
                            vec_index158 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_156_159 = (var_156, var_159)
                            prev_state = self.table_27[tuple_156_159]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_156_159] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_156, var_159)

                                # Program Call Region
                                ret = self.proc_135_(var_156, var_159)

                        # Program TransitionState Region
                        tuple_156_156 = (var_156, var_156)
                        prev_state = self.table_6[tuple_156_156]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_156_156] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_156_156[1]].append(tuple_156_156[0])
                                self.index_948[tuple_156_156[0]].append(tuple_156_156[1])
                            # Program VectorAppend Region
                            vec_143.append((var_156, var_156))
        # Program VectorClear Region
        del vec_154[:]
        vec_index154 = 0
        # Program VectorUnique Region
        vec_162 = list(set(vec_162))
        vec_index162 = 0
        # Program TableJoin Region
        while vec_index162 < len(vec_162):
            var_164 = vec_162[vec_index162]
            vec_index162 += 1
            if var_164 in self.index_165:
                if var_164 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_164 = var_164
                    prev_state = self.table_18[tuple_164]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_164] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_164)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_166: int
                        scan_index_166: int = 0
                        scan_tuple_166_vec: List[int] = self.index_128[var_164]
                        while scan_index_166 < len(scan_tuple_166_vec):
                            scan_tuple_166 = scan_tuple_166_vec[scan_index_166]
                            scan_index_166 += 1
                            vec_166.append(scan_tuple_166)
                        # Program VectorLoop Region
                        vec_index166 = 0
                        while vec_index166 < len(vec_166):
                            var_167 = vec_166[vec_index166]
                            vec_index166 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_164_167 = (var_164, var_167)
                            prev_state = self.table_27[tuple_164_167]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_164_167] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_164, var_167)

                                # Program Call Region
                                ret = self.proc_135_(var_164, var_167)

                        # Program TransitionState Region
                        tuple_164_164 = (var_164, var_164)
                        prev_state = self.table_6[tuple_164_164]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_164_164] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_164_164[1]].append(tuple_164_164[0])
                                self.index_948[tuple_164_164[0]].append(tuple_164_164[1])
                            # Program VectorAppend Region
                            vec_143.append((var_164, var_164))
        # Program VectorClear Region
        del vec_162[:]
        vec_index162 = 0
        # Program VectorUnique Region
        vec_170 = list(set(vec_170))
        vec_index170 = 0
        # Program TableJoin Region
        while vec_index170 < len(vec_170):
            var_172 = vec_170[vec_index170]
            vec_index170 += 1
            if var_172 in self.index_173:
                if var_172 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_172 = var_172
                    prev_state = self.table_18[tuple_172]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_172] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_172)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_174: int
                        scan_index_174: int = 0
                        scan_tuple_174_vec: List[int] = self.index_128[var_172]
                        while scan_index_174 < len(scan_tuple_174_vec):
                            scan_tuple_174 = scan_tuple_174_vec[scan_index_174]
                            scan_index_174 += 1
                            vec_174.append(scan_tuple_174)
                        # Program VectorLoop Region
                        vec_index174 = 0
                        while vec_index174 < len(vec_174):
                            var_175 = vec_174[vec_index174]
                            vec_index174 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_172_175 = (var_172, var_175)
                            prev_state = self.table_27[tuple_172_175]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_172_175] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_172, var_175)

                                # Program Call Region
                                ret = self.proc_135_(var_172, var_175)

                        # Program TransitionState Region
                        tuple_172_172 = (var_172, var_172)
                        prev_state = self.table_6[tuple_172_172]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_172_172] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_172_172[1]].append(tuple_172_172[0])
                                self.index_948[tuple_172_172[0]].append(tuple_172_172[1])
                            # Program VectorAppend Region
                            vec_143.append((var_172, var_172))
        # Program VectorClear Region
        del vec_170[:]
        vec_index170 = 0
        # Program VectorUnique Region
        vec_178 = list(set(vec_178))
        vec_index178 = 0
        # Program TableJoin Region
        while vec_index178 < len(vec_178):
            var_180 = vec_178[vec_index178]
            vec_index178 += 1
            if var_180 in self.index_181:
                if var_180 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_180 = var_180
                    prev_state = self.table_18[tuple_180]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_180] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_180)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_182: int
                        scan_index_182: int = 0
                        scan_tuple_182_vec: List[int] = self.index_128[var_180]
                        while scan_index_182 < len(scan_tuple_182_vec):
                            scan_tuple_182 = scan_tuple_182_vec[scan_index_182]
                            scan_index_182 += 1
                            vec_182.append(scan_tuple_182)
                        # Program VectorLoop Region
                        vec_index182 = 0
                        while vec_index182 < len(vec_182):
                            var_183 = vec_182[vec_index182]
                            vec_index182 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_180_183 = (var_180, var_183)
                            prev_state = self.table_27[tuple_180_183]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_180_183] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_180, var_183)

                                # Program Call Region
                                ret = self.proc_135_(var_180, var_183)

                        # Program TransitionState Region
                        tuple_180_180 = (var_180, var_180)
                        prev_state = self.table_6[tuple_180_180]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_180_180] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_180_180[1]].append(tuple_180_180[0])
                                self.index_948[tuple_180_180[0]].append(tuple_180_180[1])
                            # Program VectorAppend Region
                            vec_143.append((var_180, var_180))
        # Program VectorClear Region
        del vec_178[:]
        vec_index178 = 0
        # Program VectorUnique Region
        vec_186 = list(set(vec_186))
        vec_index186 = 0
        # Program TableJoin Region
        while vec_index186 < len(vec_186):
            var_188 = vec_186[vec_index186]
            vec_index186 += 1
            if var_188 in self.index_189:
                if var_188 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_188 = var_188
                    prev_state = self.table_18[tuple_188]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_188] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_188)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_190: int
                        scan_index_190: int = 0
                        scan_tuple_190_vec: List[int] = self.index_128[var_188]
                        while scan_index_190 < len(scan_tuple_190_vec):
                            scan_tuple_190 = scan_tuple_190_vec[scan_index_190]
                            scan_index_190 += 1
                            vec_190.append(scan_tuple_190)
                        # Program VectorLoop Region
                        vec_index190 = 0
                        while vec_index190 < len(vec_190):
                            var_191 = vec_190[vec_index190]
                            vec_index190 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_188_191 = (var_188, var_191)
                            prev_state = self.table_27[tuple_188_191]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_188_191] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_188, var_191)

                                # Program Call Region
                                ret = self.proc_135_(var_188, var_191)

                        # Program TransitionState Region
                        tuple_188_188 = (var_188, var_188)
                        prev_state = self.table_6[tuple_188_188]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_188_188] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_188_188[1]].append(tuple_188_188[0])
                                self.index_948[tuple_188_188[0]].append(tuple_188_188[1])
                            # Program VectorAppend Region
                            vec_143.append((var_188, var_188))
        # Program VectorClear Region
        del vec_186[:]
        vec_index186 = 0
        # Program VectorUnique Region
        vec_194 = list(set(vec_194))
        vec_index194 = 0
        # Program TableJoin Region
        while vec_index194 < len(vec_194):
            var_196 = vec_194[vec_index194]
            vec_index194 += 1
            if var_196 in self.index_197:
                if var_196 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_196 = var_196
                    prev_state = self.table_18[tuple_196]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_196] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_196)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_198: int
                        scan_index_198: int = 0
                        scan_tuple_198_vec: List[int] = self.index_128[var_196]
                        while scan_index_198 < len(scan_tuple_198_vec):
                            scan_tuple_198 = scan_tuple_198_vec[scan_index_198]
                            scan_index_198 += 1
                            vec_198.append(scan_tuple_198)
                        # Program VectorLoop Region
                        vec_index198 = 0
                        while vec_index198 < len(vec_198):
                            var_199 = vec_198[vec_index198]
                            vec_index198 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_196_199 = (var_196, var_199)
                            prev_state = self.table_27[tuple_196_199]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_196_199] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_196, var_199)

                                # Program Call Region
                                ret = self.proc_135_(var_196, var_199)

                        # Program TransitionState Region
                        tuple_196_196 = (var_196, var_196)
                        prev_state = self.table_6[tuple_196_196]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_196_196] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_196_196[1]].append(tuple_196_196[0])
                                self.index_948[tuple_196_196[0]].append(tuple_196_196[1])
                            # Program VectorAppend Region
                            vec_143.append((var_196, var_196))
        # Program VectorClear Region
        del vec_194[:]
        vec_index194 = 0
        # Program VectorUnique Region
        vec_202 = list(set(vec_202))
        vec_index202 = 0
        # Program TableJoin Region
        while vec_index202 < len(vec_202):
            var_204 = vec_202[vec_index202]
            vec_index202 += 1
            if var_204 in self.index_205:
                tuple_203_1_index: int = 0
                tuple_203_1_vec: List[int] = self.index_206[var_204]
                while tuple_203_1_index < len(tuple_203_1_vec):
                    tuple_203_1 = tuple_203_1_vec[tuple_203_1_index]
                    tuple_203_1_index += 1
                    var_207 = tuple_203_1
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_204_207 = (var_204, var_207)
                    prev_state = self.table_97[tuple_204_207]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_204_207] = 1 | 4
                        if not present_bit:
                            self.index_244[tuple_204_207[1]].append(tuple_204_207[0])
                        # Program VectorAppend Region
                        vec_240.append(var_207)
        # Program VectorClear Region
        del vec_202[:]
        vec_index202 = 0
        # Program VectorUnique Region
        vec_208 = list(set(vec_208))
        vec_index208 = 0
        # Program TableJoin Region
        while vec_index208 < len(vec_208):
            var_210 = vec_208[vec_index208]
            vec_index208 += 1
            if var_210 in self.index_211:
                tuple_209_1_index: int = 0
                tuple_209_1_vec: List[int] = self.index_206[var_210]
                while tuple_209_1_index < len(tuple_209_1_vec):
                    tuple_209_1 = tuple_209_1_vec[tuple_209_1_index]
                    tuple_209_1_index += 1
                    var_212 = tuple_209_1
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_210_212 = (var_210, var_212)
                    prev_state = self.table_89[tuple_210_212]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_89[tuple_210_212] = 1 | 4
                        if not present_bit:
                            self.index_262[tuple_210_212[1]].append(tuple_210_212[0])
                        # Program VectorAppend Region
                        vec_259.append(var_212)
        # Program VectorClear Region
        del vec_208[:]
        vec_index208 = 0
        # Program VectorUnique Region
        vec_213 = list(set(vec_213))
        vec_index213 = 0
        # Program TableJoin Region
        while vec_index213 < len(vec_213):
            var_215 = vec_213[vec_index213]
            vec_index213 += 1
            tuple_214_0_index: int = 0
            tuple_214_0_vec: List[Tuple[int, int]] = self.index_216[var_215]
            while tuple_214_0_index < len(tuple_214_0_vec):
                tuple_214_0 = tuple_214_0_vec[tuple_214_0_index]
                tuple_214_0_index += 1
                var_218 = tuple_214_0[0]
                var_219 = tuple_214_0[1]
                if var_215 in self.index_217:
                    # Program TransitionState Region
                    var_218 = self._resolve_edgetype(var_218)
                    tuple_219_215_218 = (var_219, var_215, var_218)
                    prev_state = self.table_9[tuple_219_215_218]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_219_215_218] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_219_215_218[0], tuple_219_215_218[1])].append(tuple_219_215_218[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_215_219 = (var_215, var_219)
                        prev_state = self.table_27[tuple_215_219]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_215_219] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_215_219[0]].append(tuple_215_219[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_215)
                        if not ret:
                            # Program TransitionState Region
                            tuple_215_219 = (var_215, var_219)
                            prev_state = self.table_27[tuple_215_219]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_215_219] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_215_219[0]].append(tuple_215_219[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_219, var_215)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_219_215 = (var_219, var_215)
                                    prev_state = self.table_64[tuple_219_215]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_219_215] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_219_215[0]].append(tuple_219_215[1])
                                            self.index_970[tuple_219_215[1]].append(tuple_219_215[0])
                                        # Program VectorAppend Region
                                        vec_347.append(var_219)
                                # Program TransitionState Region
                                tuple_219_215 = (var_219, var_215)
                                prev_state = self.table_15[tuple_219_215]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_219_215] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_219_215[0]].append(tuple_219_215[1])
                        # Program TransitionState Region
                        tuple_219_215 = (var_219, var_215)
                        prev_state = self.table_106[tuple_219_215]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_219_215] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_219_215[1]].append(tuple_219_215[0])
                            # Program VectorAppend Region
                            vec_336.append(var_215)
                        # Program TransitionState Region
                        tuple_215 = var_215
                        prev_state = self.table_54[tuple_215]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_215] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_313.append(var_215)
                        # Program TupleCompare Region
                        if self.var_0 == var_218:
                            # Program TransitionState Region
                            tuple_215 = var_215
                            prev_state = self.table_18[tuple_215]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_215] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_336.append(var_215)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_228: int
                                scan_index_228: int = 0
                                scan_tuple_228_vec: List[int] = self.index_128[var_215]
                                while scan_index_228 < len(scan_tuple_228_vec):
                                    scan_tuple_228 = scan_tuple_228_vec[scan_index_228]
                                    scan_index_228 += 1
                                    vec_228.append(scan_tuple_228)
                                # Program VectorLoop Region
                                vec_index228 = 0
                                while vec_index228 < len(vec_228):
                                    var_229 = vec_228[vec_index228]
                                    vec_index228 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_215_229 = (var_215, var_229)
                                    prev_state = self.table_27[tuple_215_229]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_215_229] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_215, var_229)

                                        # Program Call Region
                                        ret = self.proc_135_(var_215, var_229)

                                # Program TransitionState Region
                                tuple_215_215 = (var_215, var_215)
                                prev_state = self.table_6[tuple_215_215]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_215_215] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_215_215[1]].append(tuple_215_215[0])
                                        self.index_948[tuple_215_215[0]].append(tuple_215_215[1])
                                    # Program VectorAppend Region
                                    vec_143.append((var_215, var_215))
                        # Program TupleCompare Region
                        if self.var_2 == var_218:
                            # Program TransitionState Region
                            tuple_219_215 = (var_219, var_215)
                            prev_state = self.table_58[tuple_219_215]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_219_215] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_219_215[0]].append(tuple_219_215[1])
                                # Program VectorAppend Region
                                vec_322.append(var_219)
        # Program VectorClear Region
        del vec_213[:]
        vec_index213 = 0
        # Program VectorUnique Region
        vec_232 = list(set(vec_232))
        vec_index232 = 0
        # Program TableJoin Region
        while vec_index232 < len(vec_232):
            var_234 = vec_232[vec_index232]
            vec_index232 += 1
            if var_234 in self.index_235:
                if var_234 in self.index_217:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_234 = var_234
                    prev_state = self.table_18[tuple_234]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_234] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_234)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_236: int
                        scan_index_236: int = 0
                        scan_tuple_236_vec: List[int] = self.index_128[var_234]
                        while scan_index_236 < len(scan_tuple_236_vec):
                            scan_tuple_236 = scan_tuple_236_vec[scan_index_236]
                            scan_index_236 += 1
                            vec_236.append(scan_tuple_236)
                        # Program VectorLoop Region
                        vec_index236 = 0
                        while vec_index236 < len(vec_236):
                            var_237 = vec_236[vec_index236]
                            vec_index236 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_234_237 = (var_234, var_237)
                            prev_state = self.table_27[tuple_234_237]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_234_237] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_234, var_237)

                                # Program Call Region
                                ret = self.proc_135_(var_234, var_237)

                        # Program TransitionState Region
                        tuple_234_234 = (var_234, var_234)
                        prev_state = self.table_6[tuple_234_234]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_234_234] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_234_234[1]].append(tuple_234_234[0])
                                self.index_948[tuple_234_234[0]].append(tuple_234_234[1])
                            # Program VectorAppend Region
                            vec_143.append((var_234, var_234))
        # Program VectorClear Region
        del vec_232[:]
        vec_index232 = 0
        # Program VectorUnique Region
        vec_240 = list(set(vec_240))
        vec_index240 = 0
        # Program TableJoin Region
        while vec_index240 < len(vec_240):
            var_242 = vec_240[vec_index240]
            vec_index240 += 1
            tuple_241_0_index: int = 0
            tuple_241_0_vec: List[int] = self.index_243[var_242]
            while tuple_241_0_index < len(tuple_241_0_vec):
                tuple_241_0 = tuple_241_0_vec[tuple_241_0_index]
                tuple_241_0_index += 1
                var_245 = tuple_241_0
                tuple_241_1_index: int = 0
                tuple_241_1_vec: List[int] = self.index_244[var_242]
                while tuple_241_1_index < len(tuple_241_1_vec):
                    tuple_241_1 = tuple_241_1_vec[tuple_241_1_index]
                    tuple_241_1_index += 1
                    var_246 = tuple_241_1
                    # Program TransitionState Region
                    tuple_245_246 = (var_245, var_246)
                    prev_state = self.table_100[tuple_245_246]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_100[tuple_245_246] = 1 | 4
                        if not present_bit:
                            self.index_292[tuple_245_246[0]].append(tuple_245_246[1])
                        # Program VectorAppend Region
                        vec_289.append(var_245)
        # Program VectorClear Region
        del vec_240[:]
        vec_index240 = 0
        # Program VectorUnique Region
        vec_247 = list(set(vec_247))
        vec_index247 = 0
        # Program TableJoin Region
        while vec_index247 < len(vec_247):
            var_249 = vec_247[vec_index247]
            vec_index247 += 1
            if var_249 in self.index_217:
                tuple_248_1_index: int = 0
                tuple_248_1_vec: List[int] = self.index_250[var_249]
                while tuple_248_1_index < len(tuple_248_1_vec):
                    tuple_248_1 = tuple_248_1_vec[tuple_248_1_index]
                    tuple_248_1_index += 1
                    var_251 = tuple_248_1
                    # Program TransitionState Region
                    tuple_251_249_5 = (var_251, var_249, self.var_5)
                    prev_state = self.table_9[tuple_251_249_5]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_251_249_5] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_251_249_5[0], tuple_251_249_5[1])].append(tuple_251_249_5[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_249_251 = (var_249, var_251)
                        prev_state = self.table_27[tuple_249_251]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_249_251] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_249_251[0]].append(tuple_249_251[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_249)
                        if not ret:
                            # Program TransitionState Region
                            tuple_249_251 = (var_249, var_251)
                            prev_state = self.table_27[tuple_249_251]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_249_251] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_249_251[0]].append(tuple_249_251[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_251, var_249)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_251_249 = (var_251, var_249)
                                    prev_state = self.table_64[tuple_251_249]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_251_249] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_251_249[0]].append(tuple_251_249[1])
                                            self.index_970[tuple_251_249[1]].append(tuple_251_249[0])
                                        # Program VectorAppend Region
                                        vec_347.append(var_251)
                                # Program TransitionState Region
                                tuple_251_249 = (var_251, var_249)
                                prev_state = self.table_15[tuple_251_249]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_251_249] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_251_249[0]].append(tuple_251_249[1])
                        # Program TransitionState Region
                        tuple_251_249 = (var_251, var_249)
                        prev_state = self.table_106[tuple_251_249]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_251_249] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_251_249[1]].append(tuple_251_249[0])
                            # Program VectorAppend Region
                            vec_336.append(var_249)
                        # Program TransitionState Region
                        tuple_249 = var_249
                        prev_state = self.table_54[tuple_249]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_249] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_313.append(var_249)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_5:
                            # Program TransitionState Region
                            tuple_249 = var_249
                            prev_state = self.table_18[tuple_249]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_249] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_336.append(var_249)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_255: int
                                scan_index_255: int = 0
                                scan_tuple_255_vec: List[int] = self.index_128[var_249]
                                while scan_index_255 < len(scan_tuple_255_vec):
                                    scan_tuple_255 = scan_tuple_255_vec[scan_index_255]
                                    scan_index_255 += 1
                                    vec_255.append(scan_tuple_255)
                                # Program VectorLoop Region
                                vec_index255 = 0
                                while vec_index255 < len(vec_255):
                                    var_256 = vec_255[vec_index255]
                                    vec_index255 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_249_256 = (var_249, var_256)
                                    prev_state = self.table_27[tuple_249_256]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_249_256] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_249, var_256)

                                        # Program Call Region
                                        ret = self.proc_135_(var_249, var_256)

                                # Program TransitionState Region
                                tuple_249_249 = (var_249, var_249)
                                prev_state = self.table_6[tuple_249_249]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_249_249] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_249_249[1]].append(tuple_249_249[0])
                                        self.index_948[tuple_249_249[0]].append(tuple_249_249[1])
                                    # Program VectorAppend Region
                                    vec_143.append((var_249, var_249))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_5:
                            # Program TransitionState Region
                            tuple_251_249 = (var_251, var_249)
                            prev_state = self.table_58[tuple_251_249]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_251_249] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_251_249[0]].append(tuple_251_249[1])
                                # Program VectorAppend Region
                                vec_322.append(var_251)
        # Program VectorClear Region
        del vec_247[:]
        vec_index247 = 0
        # Program VectorUnique Region
        vec_259 = list(set(vec_259))
        vec_index259 = 0
        # Program TableJoin Region
        while vec_index259 < len(vec_259):
            var_261 = vec_259[vec_index259]
            vec_index259 += 1
            tuple_260_0_index: int = 0
            tuple_260_0_vec: List[int] = self.index_243[var_261]
            while tuple_260_0_index < len(tuple_260_0_vec):
                tuple_260_0 = tuple_260_0_vec[tuple_260_0_index]
                tuple_260_0_index += 1
                var_263 = tuple_260_0
                tuple_260_1_index: int = 0
                tuple_260_1_vec: List[int] = self.index_262[var_261]
                while tuple_260_1_index < len(tuple_260_1_vec):
                    tuple_260_1 = tuple_260_1_vec[tuple_260_1_index]
                    tuple_260_1_index += 1
                    var_264 = tuple_260_1
                    # Program TransitionState Region
                    tuple_263_264 = (var_263, var_264)
                    prev_state = self.table_92[tuple_263_264]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_92[tuple_263_264] = 1 | 4
                        if not present_bit:
                            self.index_304[tuple_263_264[0]].append(tuple_263_264[1])
                        # Program VectorAppend Region
                        vec_301.append(var_263)
        # Program VectorClear Region
        del vec_259[:]
        vec_index259 = 0
        # Program VectorUnique Region
        vec_265 = list(set(vec_265))
        vec_index265 = 0
        # Program TableJoin Region
        while vec_index265 < len(vec_265):
            var_267 = vec_265[vec_index265]
            vec_index265 += 1
            if var_267 in self.index_217:
                tuple_266_1_index: int = 0
                tuple_266_1_vec: List[int] = self.index_268[var_267]
                while tuple_266_1_index < len(tuple_266_1_vec):
                    tuple_266_1 = tuple_266_1_vec[tuple_266_1_index]
                    tuple_266_1_index += 1
                    var_269 = tuple_266_1
                    # Program TransitionState Region
                    tuple_269_267_3 = (var_269, var_267, self.var_3)
                    prev_state = self.table_9[tuple_269_267_3]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_269_267_3] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_269_267_3[0], tuple_269_267_3[1])].append(tuple_269_267_3[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_267_269 = (var_267, var_269)
                        prev_state = self.table_27[tuple_267_269]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_267_269] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_267_269[0]].append(tuple_267_269[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_267)
                        if not ret:
                            # Program TransitionState Region
                            tuple_267_269 = (var_267, var_269)
                            prev_state = self.table_27[tuple_267_269]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_267_269] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_267_269[0]].append(tuple_267_269[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_269, var_267)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_269_267 = (var_269, var_267)
                                    prev_state = self.table_64[tuple_269_267]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_269_267] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_269_267[0]].append(tuple_269_267[1])
                                            self.index_970[tuple_269_267[1]].append(tuple_269_267[0])
                                        # Program VectorAppend Region
                                        vec_347.append(var_269)
                                # Program TransitionState Region
                                tuple_269_267 = (var_269, var_267)
                                prev_state = self.table_15[tuple_269_267]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_269_267] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_269_267[0]].append(tuple_269_267[1])
                        # Program TransitionState Region
                        tuple_269_267 = (var_269, var_267)
                        prev_state = self.table_106[tuple_269_267]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_269_267] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_269_267[1]].append(tuple_269_267[0])
                            # Program VectorAppend Region
                            vec_336.append(var_267)
                        # Program TransitionState Region
                        tuple_267 = var_267
                        prev_state = self.table_54[tuple_267]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_267] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_313.append(var_267)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_3:
                            # Program TransitionState Region
                            tuple_267 = var_267
                            prev_state = self.table_18[tuple_267]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_267] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_336.append(var_267)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_273: int
                                scan_index_273: int = 0
                                scan_tuple_273_vec: List[int] = self.index_128[var_267]
                                while scan_index_273 < len(scan_tuple_273_vec):
                                    scan_tuple_273 = scan_tuple_273_vec[scan_index_273]
                                    scan_index_273 += 1
                                    vec_273.append(scan_tuple_273)
                                # Program VectorLoop Region
                                vec_index273 = 0
                                while vec_index273 < len(vec_273):
                                    var_274 = vec_273[vec_index273]
                                    vec_index273 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_267_274 = (var_267, var_274)
                                    prev_state = self.table_27[tuple_267_274]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_267_274] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_267, var_274)

                                        # Program Call Region
                                        ret = self.proc_135_(var_267, var_274)

                                # Program TransitionState Region
                                tuple_267_267 = (var_267, var_267)
                                prev_state = self.table_6[tuple_267_267]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_267_267] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_267_267[1]].append(tuple_267_267[0])
                                        self.index_948[tuple_267_267[0]].append(tuple_267_267[1])
                                    # Program VectorAppend Region
                                    vec_143.append((var_267, var_267))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_3:
                            # Program TransitionState Region
                            tuple_269_267 = (var_269, var_267)
                            prev_state = self.table_58[tuple_269_267]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_269_267] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_269_267[0]].append(tuple_269_267[1])
                                # Program VectorAppend Region
                                vec_322.append(var_269)
        # Program VectorClear Region
        del vec_265[:]
        vec_index265 = 0
        # Program VectorUnique Region
        vec_277 = list(set(vec_277))
        vec_index277 = 0
        # Program TableJoin Region
        while vec_index277 < len(vec_277):
            var_279 = vec_277[vec_index277]
            vec_index277 += 1
            if var_279 in self.index_217:
                tuple_278_1_index: int = 0
                tuple_278_1_vec: List[int] = self.index_280[var_279]
                while tuple_278_1_index < len(tuple_278_1_vec):
                    tuple_278_1 = tuple_278_1_vec[tuple_278_1_index]
                    tuple_278_1_index += 1
                    var_281 = tuple_278_1
                    # Program TransitionState Region
                    tuple_281_279_0 = (var_281, var_279, self.var_0)
                    prev_state = self.table_9[tuple_281_279_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_281_279_0] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_281_279_0[0], tuple_281_279_0[1])].append(tuple_281_279_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_279_281 = (var_279, var_281)
                        prev_state = self.table_27[tuple_279_281]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_279_281] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_279_281[0]].append(tuple_279_281[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_279)
                        if not ret:
                            # Program TransitionState Region
                            tuple_279_281 = (var_279, var_281)
                            prev_state = self.table_27[tuple_279_281]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_279_281] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_279_281[0]].append(tuple_279_281[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_281, var_279)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_281_279 = (var_281, var_279)
                                    prev_state = self.table_64[tuple_281_279]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_281_279] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_281_279[0]].append(tuple_281_279[1])
                                            self.index_970[tuple_281_279[1]].append(tuple_281_279[0])
                                        # Program VectorAppend Region
                                        vec_347.append(var_281)
                                # Program TransitionState Region
                                tuple_281_279 = (var_281, var_279)
                                prev_state = self.table_15[tuple_281_279]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_281_279] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_281_279[0]].append(tuple_281_279[1])
                        # Program TransitionState Region
                        tuple_281_279 = (var_281, var_279)
                        prev_state = self.table_106[tuple_281_279]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_281_279] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_281_279[1]].append(tuple_281_279[0])
                            # Program VectorAppend Region
                            vec_336.append(var_279)
                        # Program TransitionState Region
                        tuple_279 = var_279
                        prev_state = self.table_54[tuple_279]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_279] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_313.append(var_279)
                        # Program TransitionState Region
                        tuple_279 = var_279
                        prev_state = self.table_18[tuple_279]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_279] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_336.append(var_279)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_285: int
                            scan_index_285: int = 0
                            scan_tuple_285_vec: List[int] = self.index_128[var_279]
                            while scan_index_285 < len(scan_tuple_285_vec):
                                scan_tuple_285 = scan_tuple_285_vec[scan_index_285]
                                scan_index_285 += 1
                                vec_285.append(scan_tuple_285)
                            # Program VectorLoop Region
                            vec_index285 = 0
                            while vec_index285 < len(vec_285):
                                var_286 = vec_285[vec_index285]
                                vec_index285 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_279_286 = (var_279, var_286)
                                prev_state = self.table_27[tuple_279_286]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_279_286] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_131_(var_279, var_286)

                                    # Program Call Region
                                    ret = self.proc_135_(var_279, var_286)

                            # Program TransitionState Region
                            tuple_279_279 = (var_279, var_279)
                            prev_state = self.table_6[tuple_279_279]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_279_279] = 1 | 4
                                if not present_bit:
                                    self.index_350[tuple_279_279[1]].append(tuple_279_279[0])
                                    self.index_948[tuple_279_279[0]].append(tuple_279_279[1])
                                # Program VectorAppend Region
                                vec_143.append((var_279, var_279))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_281_279 = (var_281, var_279)
                            prev_state = self.table_58[tuple_281_279]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_281_279] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_281_279[0]].append(tuple_281_279[1])
                                # Program VectorAppend Region
                                vec_322.append(var_281)
        # Program VectorClear Region
        del vec_277[:]
        vec_index277 = 0
        # Program VectorUnique Region
        vec_289 = list(set(vec_289))
        vec_index289 = 0
        # Program TableJoin Region
        while vec_index289 < len(vec_289):
            var_291 = vec_289[vec_index289]
            vec_index289 += 1
            if var_291 in self.index_217:
                tuple_290_1_index: int = 0
                tuple_290_1_vec: List[int] = self.index_292[var_291]
                while tuple_290_1_index < len(tuple_290_1_vec):
                    tuple_290_1 = tuple_290_1_vec[tuple_290_1_index]
                    tuple_290_1_index += 1
                    var_293 = tuple_290_1
                    # Program TransitionState Region
                    tuple_293_291_0 = (var_293, var_291, self.var_0)
                    prev_state = self.table_9[tuple_293_291_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_293_291_0] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_293_291_0[0], tuple_293_291_0[1])].append(tuple_293_291_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_291_293 = (var_291, var_293)
                        prev_state = self.table_27[tuple_291_293]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_291_293] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_291_293[0]].append(tuple_291_293[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_291)
                        if not ret:
                            # Program TransitionState Region
                            tuple_291_293 = (var_291, var_293)
                            prev_state = self.table_27[tuple_291_293]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_291_293] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_291_293[0]].append(tuple_291_293[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_293, var_291)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_293_291 = (var_293, var_291)
                                    prev_state = self.table_64[tuple_293_291]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_293_291] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_293_291[0]].append(tuple_293_291[1])
                                            self.index_970[tuple_293_291[1]].append(tuple_293_291[0])
                                        # Program VectorAppend Region
                                        vec_347.append(var_293)
                                # Program TransitionState Region
                                tuple_293_291 = (var_293, var_291)
                                prev_state = self.table_15[tuple_293_291]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_293_291] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_293_291[0]].append(tuple_293_291[1])
                        # Program TransitionState Region
                        tuple_293_291 = (var_293, var_291)
                        prev_state = self.table_106[tuple_293_291]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_293_291] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_293_291[1]].append(tuple_293_291[0])
                            # Program VectorAppend Region
                            vec_336.append(var_291)
                        # Program TransitionState Region
                        tuple_291 = var_291
                        prev_state = self.table_54[tuple_291]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_291] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_313.append(var_291)
                        # Program TransitionState Region
                        tuple_291 = var_291
                        prev_state = self.table_18[tuple_291]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_291] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_336.append(var_291)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_297: int
                            scan_index_297: int = 0
                            scan_tuple_297_vec: List[int] = self.index_128[var_291]
                            while scan_index_297 < len(scan_tuple_297_vec):
                                scan_tuple_297 = scan_tuple_297_vec[scan_index_297]
                                scan_index_297 += 1
                                vec_297.append(scan_tuple_297)
                            # Program VectorLoop Region
                            vec_index297 = 0
                            while vec_index297 < len(vec_297):
                                var_298 = vec_297[vec_index297]
                                vec_index297 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_291_298 = (var_291, var_298)
                                prev_state = self.table_27[tuple_291_298]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_291_298] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_131_(var_291, var_298)

                                    # Program Call Region
                                    ret = self.proc_135_(var_291, var_298)

                            # Program TransitionState Region
                            tuple_291_291 = (var_291, var_291)
                            prev_state = self.table_6[tuple_291_291]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_291_291] = 1 | 4
                                if not present_bit:
                                    self.index_350[tuple_291_291[1]].append(tuple_291_291[0])
                                    self.index_948[tuple_291_291[0]].append(tuple_291_291[1])
                                # Program VectorAppend Region
                                vec_143.append((var_291, var_291))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_293_291 = (var_293, var_291)
                            prev_state = self.table_58[tuple_293_291]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_293_291] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_293_291[0]].append(tuple_293_291[1])
                                # Program VectorAppend Region
                                vec_322.append(var_293)
        # Program VectorClear Region
        del vec_289[:]
        vec_index289 = 0
        # Program VectorUnique Region
        vec_301 = list(set(vec_301))
        vec_index301 = 0
        # Program TableJoin Region
        while vec_index301 < len(vec_301):
            var_303 = vec_301[vec_index301]
            vec_index301 += 1
            if var_303 in self.index_217:
                tuple_302_1_index: int = 0
                tuple_302_1_vec: List[int] = self.index_304[var_303]
                while tuple_302_1_index < len(tuple_302_1_vec):
                    tuple_302_1 = tuple_302_1_vec[tuple_302_1_index]
                    tuple_302_1_index += 1
                    var_305 = tuple_302_1
                    # Program TransitionState Region
                    tuple_305_303_2 = (var_305, var_303, self.var_2)
                    prev_state = self.table_9[tuple_305_303_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_305_303_2] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_305_303_2[0], tuple_305_303_2[1])].append(tuple_305_303_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_303_305 = (var_303, var_305)
                        prev_state = self.table_27[tuple_303_305]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_303_305] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_303_305[0]].append(tuple_303_305[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_303)
                        if not ret:
                            # Program TransitionState Region
                            tuple_303_305 = (var_303, var_305)
                            prev_state = self.table_27[tuple_303_305]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_303_305] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_303_305[0]].append(tuple_303_305[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_305, var_303)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_305_303 = (var_305, var_303)
                                    prev_state = self.table_64[tuple_305_303]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_305_303] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_305_303[0]].append(tuple_305_303[1])
                                            self.index_970[tuple_305_303[1]].append(tuple_305_303[0])
                                        # Program VectorAppend Region
                                        vec_347.append(var_305)
                                # Program TransitionState Region
                                tuple_305_303 = (var_305, var_303)
                                prev_state = self.table_15[tuple_305_303]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_305_303] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_305_303[0]].append(tuple_305_303[1])
                        # Program TransitionState Region
                        tuple_305_303 = (var_305, var_303)
                        prev_state = self.table_106[tuple_305_303]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_305_303] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_305_303[1]].append(tuple_305_303[0])
                            # Program VectorAppend Region
                            vec_336.append(var_303)
                        # Program TransitionState Region
                        tuple_303 = var_303
                        prev_state = self.table_54[tuple_303]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_303] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_313.append(var_303)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_303 = var_303
                            prev_state = self.table_18[tuple_303]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_303] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_336.append(var_303)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_309: int
                                scan_index_309: int = 0
                                scan_tuple_309_vec: List[int] = self.index_128[var_303]
                                while scan_index_309 < len(scan_tuple_309_vec):
                                    scan_tuple_309 = scan_tuple_309_vec[scan_index_309]
                                    scan_index_309 += 1
                                    vec_309.append(scan_tuple_309)
                                # Program VectorLoop Region
                                vec_index309 = 0
                                while vec_index309 < len(vec_309):
                                    var_310 = vec_309[vec_index309]
                                    vec_index309 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_303_310 = (var_303, var_310)
                                    prev_state = self.table_27[tuple_303_310]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_303_310] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_303, var_310)

                                        # Program Call Region
                                        ret = self.proc_135_(var_303, var_310)

                                # Program TransitionState Region
                                tuple_303_303 = (var_303, var_303)
                                prev_state = self.table_6[tuple_303_303]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_303_303] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_303_303[1]].append(tuple_303_303[0])
                                        self.index_948[tuple_303_303[0]].append(tuple_303_303[1])
                                    # Program VectorAppend Region
                                    vec_143.append((var_303, var_303))
                        # Program TransitionState Region
                        tuple_305_303 = (var_305, var_303)
                        prev_state = self.table_58[tuple_305_303]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_58[tuple_305_303] = 1 | 4
                            if not present_bit:
                                self.index_325[tuple_305_303[0]].append(tuple_305_303[1])
                            # Program VectorAppend Region
                            vec_322.append(var_305)
        # Program VectorClear Region
        del vec_301[:]
        vec_index301 = 0
        # Program VectorUnique Region
        vec_313 = list(set(vec_313))
        vec_index313 = 0
        # Program TableJoin Region
        while vec_index313 < len(vec_313):
            var_315 = vec_313[vec_index313]
            vec_index313 += 1
            if var_315 in self.index_316:
                if var_315 in self.index_317:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_315 = var_315
                    prev_state = self.table_18[tuple_315]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_315] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_315)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_318: int
                        scan_index_318: int = 0
                        scan_tuple_318_vec: List[int] = self.index_128[var_315]
                        while scan_index_318 < len(scan_tuple_318_vec):
                            scan_tuple_318 = scan_tuple_318_vec[scan_index_318]
                            scan_index_318 += 1
                            vec_318.append(scan_tuple_318)
                        # Program VectorLoop Region
                        vec_index318 = 0
                        while vec_index318 < len(vec_318):
                            var_319 = vec_318[vec_index318]
                            vec_index318 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_315_319 = (var_315, var_319)
                            prev_state = self.table_27[tuple_315_319]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_315_319] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_315, var_319)

                                # Program Call Region
                                ret = self.proc_135_(var_315, var_319)

                        # Program TransitionState Region
                        tuple_315_315 = (var_315, var_315)
                        prev_state = self.table_6[tuple_315_315]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_315_315] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_315_315[1]].append(tuple_315_315[0])
                                self.index_948[tuple_315_315[0]].append(tuple_315_315[1])
                            # Program VectorAppend Region
                            vec_143.append((var_315, var_315))
        # Program VectorClear Region
        del vec_313[:]
        vec_index313 = 0
        # Program VectorUnique Region
        vec_322 = list(set(vec_322))
        vec_index322 = 0
        # Program TableJoin Region
        while vec_index322 < len(vec_322):
            var_324 = vec_322[vec_index322]
            vec_index322 += 1
            if var_324 in self.index_211:
                tuple_323_1_index: int = 0
                tuple_323_1_vec: List[int] = self.index_325[var_324]
                while tuple_323_1_index < len(tuple_323_1_vec):
                    tuple_323_1 = tuple_323_1_vec[tuple_323_1_index]
                    tuple_323_1_index += 1
                    var_326 = tuple_323_1
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_324_326 = (var_324, var_326)
                    prev_state = self.table_61[tuple_324_326]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_61[tuple_324_326] = 1 | 4
                        if not present_bit:
                            self.index_330[tuple_324_326[1]].append(tuple_324_326[0])
                        # Program VectorAppend Region
                        vec_327.append(var_326)
        # Program VectorClear Region
        del vec_322[:]
        vec_index322 = 0
        # Program VectorUnique Region
        vec_327 = list(set(vec_327))
        vec_index327 = 0
        # Program TableJoin Region
        while vec_index327 < len(vec_327):
            var_329 = vec_327[vec_index327]
            vec_index327 += 1
            if var_329 in self.index_316:
                tuple_328_1_index: int = 0
                tuple_328_1_vec: List[int] = self.index_330[var_329]
                while tuple_328_1_index < len(tuple_328_1_vec):
                    tuple_328_1 = tuple_328_1_vec[tuple_328_1_index]
                    tuple_328_1_index += 1
                    var_331 = tuple_328_1
                    # Program TransitionState Region
                    tuple_331 = var_331
                    prev_state = self.table_18[tuple_331]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_331] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_336.append(var_331)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_332: int
                        scan_index_332: int = 0
                        scan_tuple_332_vec: List[int] = self.index_128[var_331]
                        while scan_index_332 < len(scan_tuple_332_vec):
                            scan_tuple_332 = scan_tuple_332_vec[scan_index_332]
                            scan_index_332 += 1
                            vec_332.append(scan_tuple_332)
                        # Program VectorLoop Region
                        vec_index332 = 0
                        while vec_index332 < len(vec_332):
                            var_333 = vec_332[vec_index332]
                            vec_index332 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_331_333 = (var_331, var_333)
                            prev_state = self.table_27[tuple_331_333]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_331_333] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_331, var_333)

                                # Program Call Region
                                ret = self.proc_135_(var_331, var_333)

                        # Program TransitionState Region
                        tuple_331_331 = (var_331, var_331)
                        prev_state = self.table_6[tuple_331_331]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_331_331] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_331_331[1]].append(tuple_331_331[0])
                                self.index_948[tuple_331_331[0]].append(tuple_331_331[1])
                            # Program VectorAppend Region
                            vec_143.append((var_331, var_331))
        # Program VectorClear Region
        del vec_327[:]
        vec_index327 = 0
        # Program VectorUnique Region
        vec_336 = list(set(vec_336))
        vec_index336 = 0
        # Program TableJoin Region
        while vec_index336 < len(vec_336):
            var_338 = vec_336[vec_index336]
            vec_index336 += 1
            tuple_337_0_index: int = 0
            tuple_337_0_vec: List[int] = self.index_339[var_338]
            while tuple_337_0_index < len(tuple_337_0_vec):
                tuple_337_0 = tuple_337_0_vec[tuple_337_0_index]
                tuple_337_0_index += 1
                var_341 = tuple_337_0
                if var_338 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_341_338 = (var_341, var_338)
                    prev_state = self.table_109[tuple_341_338]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_341_338] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_341_338[1]].append(tuple_341_338[0])
                        # Program VectorAppend Region
                        vec_342.append(var_338)
                    # Program TransitionState Region
                    tuple_341_338 = (var_341, var_338)
                    prev_state = self.table_22[tuple_341_338]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_341_338] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_341_338[0]].append(tuple_341_338[1])
        # Program VectorClear Region
        del vec_336[:]
        vec_index336 = 0
        # Program VectorUnique Region
        vec_342 = list(set(vec_342))
        vec_index342 = 0
        # Program TableJoin Region
        while vec_index342 < len(vec_342):
            var_344 = vec_342[vec_index342]
            vec_index342 += 1
            tuple_343_0_index: int = 0
            tuple_343_0_vec: List[int] = self.index_345[var_344]
            while tuple_343_0_index < len(tuple_343_0_vec):
                tuple_343_0 = tuple_343_0_vec[tuple_343_0_index]
                tuple_343_0_index += 1
                var_346 = tuple_343_0
                if var_344 in self.index_316:
                    # Program TransitionState Region
                    tuple_346 = var_346
                    prev_state = self.table_13[tuple_346]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_346] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_342[:]
        vec_index342 = 0
        # Program VectorUnique Region
        vec_347 = list(set(vec_347))
        vec_index347 = 0
        # Program TableJoin Region
        while vec_index347 < len(vec_347):
            var_349 = vec_347[vec_index347]
            vec_index347 += 1
            tuple_348_0_index: int = 0
            tuple_348_0_vec: List[int] = self.index_350[var_349]
            while tuple_348_0_index < len(tuple_348_0_vec):
                tuple_348_0 = tuple_348_0_vec[tuple_348_0_index]
                tuple_348_0_index += 1
                var_352 = tuple_348_0
                tuple_348_1_index: int = 0
                tuple_348_1_vec: List[int] = self.index_351[var_349]
                while tuple_348_1_index < len(tuple_348_1_vec):
                    tuple_348_1 = tuple_348_1_vec[tuple_348_1_index]
                    tuple_348_1_index += 1
                    var_353 = tuple_348_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_354_(var_352, var_349)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_224_(var_349, var_353)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_359_(var_352, var_353)
                            if not ret:
                                # Program TransitionState Region
                                tuple_352_353 = (var_352, var_353)
                                prev_state = self.table_6[tuple_352_353]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_352_353] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_352_353[1]].append(tuple_352_353[0])
                                        self.index_948[tuple_352_353[0]].append(tuple_352_353[1])
                                    # Program VectorAppend Region
                                    vec_143.append((var_352, var_353))
        # Program VectorClear Region
        del vec_347[:]
        vec_index347 = 0
        # Induction Fixpoint Loop Region
        while len(vec_143):
            # Program Call Region
            param_145_0 = [vec_143]
            ret = self.proc_139_(param_145_0)
            vec_143 = param_145_0[0]

        vec_index143 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_143[:]
        vec_index143 = 0
        # Program Return Region
        return False
        return False

    def proc_131_(self, var_132: int, var_133: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_133_132 = (var_133, var_132)
        prev_state = self.table_64[tuple_133_132]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_64[tuple_133_132] = 2 | 4
            # Program Call Region
            ret = self.proc_1014_(var_133, var_132)

        # Program Return Region
        return False
        return False

    def proc_135_(self, var_136: int, var_137: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_137_136 = (var_137, var_136)
        prev_state = self.table_15[tuple_137_136]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_15[tuple_137_136] = 2 | 4
            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_979_(var_136, var_137)

        # Program Return Region
        return False
        return False

    def proc_139_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_140 = param_0[0]
        vec_index140: int = 0
        vec_363: List[Tuple[int, int]] = list()
        vec_index363: int = 0
        vec_366: List[int] = list()
        vec_index366: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_140, vec_363 = vec_363, vec_140
        # Program VectorLoop Region
        while vec_index363 < len(vec_363):
            var_364, var_365 = vec_363[vec_index363]
            vec_index363 += 1
            # Program VectorAppend Region
            vec_366.append(var_365)
        # Program VectorUnique Region
        vec_366 = list(set(vec_366))
        vec_index366 = 0
        # Program TableJoin Region
        while vec_index366 < len(vec_366):
            var_368 = vec_366[vec_index366]
            vec_index366 += 1
            tuple_367_0_index: int = 0
            tuple_367_0_vec: List[int] = self.index_350[var_368]
            while tuple_367_0_index < len(tuple_367_0_vec):
                tuple_367_0 = tuple_367_0_vec[tuple_367_0_index]
                tuple_367_0_index += 1
                var_369 = tuple_367_0
                tuple_367_1_index: int = 0
                tuple_367_1_vec: List[int] = self.index_351[var_368]
                while tuple_367_1_index < len(tuple_367_1_vec):
                    tuple_367_1 = tuple_367_1_vec[tuple_367_1_index]
                    tuple_367_1_index += 1
                    var_370 = tuple_367_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_354_(var_369, var_368)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_224_(var_368, var_370)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_359_(var_369, var_370)
                            if not ret:
                                # Program TransitionState Region
                                tuple_369_370 = (var_369, var_370)
                                prev_state = self.table_6[tuple_369_370]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_369_370] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_369_370[1]].append(tuple_369_370[0])
                                        self.index_948[tuple_369_370[0]].append(tuple_369_370[1])
                                    # Program VectorAppend Region
                                    vec_140.append((var_369, var_370))
        # Program VectorClear Region
        del vec_366[:]
        vec_index366 = 0
        # Program VectorClear Region
        del vec_363[:]
        vec_index363 = 0
        # Program Return Region
        param_0[0] = vec_140
        return False
        return False

    def proc_221_(self, var_222: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_18[var_222] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_222 = var_222
            prev_state = self.table_18[tuple_222]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_18[tuple_222] = 0 | 4
        # Program Return Region
        return False
        return False

    def proc_224_(self, var_225: int, var_226: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_64[(var_225, var_226)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_225_226 = (var_225, var_226)
            prev_state = self.table_64[tuple_225_226]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_64[tuple_225_226] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_979_(var_226, var_225)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_225_226 = (var_225, var_226)
                    prev_state = self.table_64[tuple_225_226]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_64[tuple_225_226] = 1 | 4
                        if not present_bit:
                            self.index_351[tuple_225_226[0]].append(tuple_225_226[1])
                            self.index_970[tuple_225_226[1]].append(tuple_225_226[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_354_(self, var_355: int, var_356: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_355, var_356)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_355_356 = (var_355, var_356)
            prev_state = self.table_6[tuple_355_356]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_355_356] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_995_(var_355, var_356)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_355_356 = (var_355, var_356)
                    prev_state = self.table_6[tuple_355_356]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_355_356] = 1 | 4
                        if not present_bit:
                            self.index_350[tuple_355_356[1]].append(tuple_355_356[0])
                            self.index_948[tuple_355_356[0]].append(tuple_355_356[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_359_(self, var_360: int, var_361: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_360, var_361)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_360_361 = (var_360, var_361)
            prev_state = self.table_6[tuple_360_361]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_360_361] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_965_(var_360, var_361)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_360_361 = (var_360, var_361)
                    prev_state = self.table_6[tuple_360_361]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_360_361] = 1 | 4
                        if not present_bit:
                            self.index_350[tuple_360_361[1]].append(tuple_360_361[0])
                            self.index_948[tuple_360_361[0]].append(tuple_360_361[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def external_symbol_2(self, vec_377: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index377: int = 0
        vec_380: List[int] = list()
        vec_index380: int = 0
        vec_388: List[int] = list()
        vec_index388: int = 0
        vec_392: List[Tuple[int, int]] = list()
        vec_index392: int = 0
        vec_395: List[int] = list()
        vec_index395: int = 0
        vec_398: List[int] = list()
        vec_index398: int = 0
        vec_402: List[int] = list()
        vec_index402: int = 0
        vec_409: List[int] = list()
        vec_index409: int = 0
        vec_413: List[int] = list()
        vec_index413: int = 0
        vec_420: List[int] = list()
        vec_index420: int = 0
        vec_424: List[int] = list()
        vec_index424: int = 0
        vec_431: List[int] = list()
        vec_index431: int = 0
        vec_435: List[int] = list()
        vec_index435: int = 0
        vec_442: List[int] = list()
        vec_index442: int = 0
        vec_446: List[int] = list()
        vec_index446: int = 0
        vec_453: List[int] = list()
        vec_index453: int = 0
        vec_457: List[int] = list()
        vec_index457: int = 0
        vec_460: List[int] = list()
        vec_index460: int = 0
        vec_464: List[int] = list()
        vec_index464: int = 0
        vec_468: List[int] = list()
        vec_index468: int = 0
        vec_472: List[int] = list()
        vec_index472: int = 0
        vec_476: List[int] = list()
        vec_index476: int = 0
        vec_480: List[int] = list()
        vec_index480: int = 0
        vec_488: List[int] = list()
        vec_index488: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index377 = 0
        while vec_index377 < len(vec_377):
            var_378, var_379 = vec_377[vec_index377]
            vec_index377 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_378 = var_378
            prev_state = self.table_52[tuple_378]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_52[tuple_378] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_378 = var_378
                prev_state = self.table_32[tuple_378]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_378] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_395.append(var_378)
                    # Program VectorAppend Region
                    vec_380.append(var_378)
                    # Program VectorAppend Region
                    vec_424.append(var_378)
                    # Program VectorAppend Region
                    vec_413.append(var_378)
                    # Program VectorAppend Region
                    vec_446.append(var_378)
                    # Program VectorAppend Region
                    vec_435.append(var_378)
                    # Program VectorAppend Region
                    vec_402.append(var_378)
                # Program VectorAppend Region
                vec_457.append(var_378)
                # Program VectorAppend Region
                vec_468.append(var_378)
                # Program VectorAppend Region
                vec_488.append(var_378)
            # Program TransitionState Region
            tuple_378 = var_378
            prev_state = self.table_52[tuple_378]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_52[tuple_378] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_378 = var_378
                prev_state = self.table_32[tuple_378]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_378] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_395.append(var_378)
                    # Program VectorAppend Region
                    vec_380.append(var_378)
                    # Program VectorAppend Region
                    vec_424.append(var_378)
                    # Program VectorAppend Region
                    vec_413.append(var_378)
                    # Program VectorAppend Region
                    vec_446.append(var_378)
                    # Program VectorAppend Region
                    vec_435.append(var_378)
                    # Program VectorAppend Region
                    vec_402.append(var_378)
                # Program VectorAppend Region
                vec_457.append(var_378)
                # Program VectorAppend Region
                vec_468.append(var_378)
                # Program VectorAppend Region
                vec_488.append(var_378)
            # Program TransitionState Region
            tuple_378 = var_378
            prev_state = self.table_52[tuple_378]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_52[tuple_378] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_378 = var_378
                prev_state = self.table_32[tuple_378]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_378] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_395.append(var_378)
                    # Program VectorAppend Region
                    vec_380.append(var_378)
                    # Program VectorAppend Region
                    vec_424.append(var_378)
                    # Program VectorAppend Region
                    vec_413.append(var_378)
                    # Program VectorAppend Region
                    vec_446.append(var_378)
                    # Program VectorAppend Region
                    vec_435.append(var_378)
                    # Program VectorAppend Region
                    vec_402.append(var_378)
                # Program VectorAppend Region
                vec_457.append(var_378)
                # Program VectorAppend Region
                vec_468.append(var_378)
                # Program VectorAppend Region
                vec_488.append(var_378)
            # Program TransitionState Region
            tuple_378 = var_378
            prev_state = self.table_52[tuple_378]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_52[tuple_378] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_378 = var_378
                prev_state = self.table_32[tuple_378]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_32[tuple_378] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_395.append(var_378)
                    # Program VectorAppend Region
                    vec_380.append(var_378)
                    # Program VectorAppend Region
                    vec_424.append(var_378)
                    # Program VectorAppend Region
                    vec_413.append(var_378)
                    # Program VectorAppend Region
                    vec_446.append(var_378)
                    # Program VectorAppend Region
                    vec_435.append(var_378)
                    # Program VectorAppend Region
                    vec_402.append(var_378)
                # Program VectorAppend Region
                vec_457.append(var_378)
                # Program VectorAppend Region
                vec_468.append(var_378)
                # Program VectorAppend Region
                vec_488.append(var_378)
        # Program VectorUnique Region
        vec_380 = list(set(vec_380))
        vec_index380 = 0
        # Program TableJoin Region
        while vec_index380 < len(vec_380):
            var_382 = vec_380[vec_index380]
            vec_index380 += 1
            tuple_381_0_index: int = 0
            tuple_381_0_vec: List[Tuple[int, int]] = self.index_216[var_382]
            while tuple_381_0_index < len(tuple_381_0_vec):
                tuple_381_0 = tuple_381_0_vec[tuple_381_0_index]
                tuple_381_0_index += 1
                var_383 = tuple_381_0[0]
                var_384 = tuple_381_0[1]
                if var_382 in self.index_217:
                    # Program TransitionState Region
                    var_383 = self._resolve_edgetype(var_383)
                    tuple_384_382_383 = (var_384, var_382, var_383)
                    prev_state = self.table_9[tuple_384_382_383]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_384_382_383] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_384_382_383[0], tuple_384_382_383[1])].append(tuple_384_382_383[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_382_384 = (var_382, var_384)
                        prev_state = self.table_27[tuple_382_384]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_382_384] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_382_384[0]].append(tuple_382_384[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_382)
                        if not ret:
                            # Program TransitionState Region
                            tuple_382_384 = (var_382, var_384)
                            prev_state = self.table_27[tuple_382_384]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_382_384] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_382_384[0]].append(tuple_382_384[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_384, var_382)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_384_382 = (var_384, var_382)
                                    prev_state = self.table_64[tuple_384_382]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_384_382] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_384_382[0]].append(tuple_384_382[1])
                                            self.index_970[tuple_384_382[1]].append(tuple_384_382[0])
                                        # Program VectorAppend Region
                                        vec_480.append(var_384)
                                # Program TransitionState Region
                                tuple_384_382 = (var_384, var_382)
                                prev_state = self.table_15[tuple_384_382]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_384_382] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_384_382[0]].append(tuple_384_382[1])
                        # Program TransitionState Region
                        tuple_384_382 = (var_384, var_382)
                        prev_state = self.table_106[tuple_384_382]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_384_382] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_384_382[1]].append(tuple_384_382[0])
                            # Program VectorAppend Region
                            vec_476.append(var_382)
                        # Program TransitionState Region
                        tuple_382 = var_382
                        prev_state = self.table_54[tuple_382]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_382] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_457.append(var_382)
                        # Program TupleCompare Region
                        if self.var_0 == var_383:
                            # Program TransitionState Region
                            tuple_382 = var_382
                            prev_state = self.table_18[tuple_382]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_382] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_476.append(var_382)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_388: int
                                scan_index_388: int = 0
                                scan_tuple_388_vec: List[int] = self.index_128[var_382]
                                while scan_index_388 < len(scan_tuple_388_vec):
                                    scan_tuple_388 = scan_tuple_388_vec[scan_index_388]
                                    scan_index_388 += 1
                                    vec_388.append(scan_tuple_388)
                                # Program VectorLoop Region
                                vec_index388 = 0
                                while vec_index388 < len(vec_388):
                                    var_389 = vec_388[vec_index388]
                                    vec_index388 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_382_389 = (var_382, var_389)
                                    prev_state = self.table_27[tuple_382_389]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_382_389] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_382, var_389)

                                        # Program Call Region
                                        ret = self.proc_135_(var_382, var_389)

                                # Program TransitionState Region
                                tuple_382_382 = (var_382, var_382)
                                prev_state = self.table_6[tuple_382_382]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_382_382] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_382_382[1]].append(tuple_382_382[0])
                                        self.index_948[tuple_382_382[0]].append(tuple_382_382[1])
                                    # Program VectorAppend Region
                                    vec_392.append((var_382, var_382))
                        # Program TupleCompare Region
                        if self.var_2 == var_383:
                            # Program TransitionState Region
                            tuple_384_382 = (var_384, var_382)
                            prev_state = self.table_58[tuple_384_382]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_384_382] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_384_382[0]].append(tuple_384_382[1])
                                # Program VectorAppend Region
                                vec_464.append(var_384)
        # Program VectorClear Region
        del vec_380[:]
        vec_index380 = 0
        # Program VectorUnique Region
        vec_395 = list(set(vec_395))
        vec_index395 = 0
        # Program TableJoin Region
        while vec_index395 < len(vec_395):
            var_397 = vec_395[vec_index395]
            vec_index395 += 1
            if var_397 in self.index_235:
                if var_397 in self.index_217:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_397 = var_397
                    prev_state = self.table_18[tuple_397]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_397] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_476.append(var_397)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_398: int
                        scan_index_398: int = 0
                        scan_tuple_398_vec: List[int] = self.index_128[var_397]
                        while scan_index_398 < len(scan_tuple_398_vec):
                            scan_tuple_398 = scan_tuple_398_vec[scan_index_398]
                            scan_index_398 += 1
                            vec_398.append(scan_tuple_398)
                        # Program VectorLoop Region
                        vec_index398 = 0
                        while vec_index398 < len(vec_398):
                            var_399 = vec_398[vec_index398]
                            vec_index398 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_397_399 = (var_397, var_399)
                            prev_state = self.table_27[tuple_397_399]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_397_399] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_397, var_399)

                                # Program Call Region
                                ret = self.proc_135_(var_397, var_399)

                        # Program TransitionState Region
                        tuple_397_397 = (var_397, var_397)
                        prev_state = self.table_6[tuple_397_397]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_397_397] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_397_397[1]].append(tuple_397_397[0])
                                self.index_948[tuple_397_397[0]].append(tuple_397_397[1])
                            # Program VectorAppend Region
                            vec_392.append((var_397, var_397))
        # Program VectorClear Region
        del vec_395[:]
        vec_index395 = 0
        # Program VectorUnique Region
        vec_402 = list(set(vec_402))
        vec_index402 = 0
        # Program TableJoin Region
        while vec_index402 < len(vec_402):
            var_404 = vec_402[vec_index402]
            vec_index402 += 1
            if var_404 in self.index_217:
                tuple_403_1_index: int = 0
                tuple_403_1_vec: List[int] = self.index_250[var_404]
                while tuple_403_1_index < len(tuple_403_1_vec):
                    tuple_403_1 = tuple_403_1_vec[tuple_403_1_index]
                    tuple_403_1_index += 1
                    var_405 = tuple_403_1
                    # Program TransitionState Region
                    tuple_405_404_5 = (var_405, var_404, self.var_5)
                    prev_state = self.table_9[tuple_405_404_5]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_405_404_5] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_405_404_5[0], tuple_405_404_5[1])].append(tuple_405_404_5[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_404_405 = (var_404, var_405)
                        prev_state = self.table_27[tuple_404_405]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_404_405] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_404_405[0]].append(tuple_404_405[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_404)
                        if not ret:
                            # Program TransitionState Region
                            tuple_404_405 = (var_404, var_405)
                            prev_state = self.table_27[tuple_404_405]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_404_405] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_404_405[0]].append(tuple_404_405[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_405, var_404)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_405_404 = (var_405, var_404)
                                    prev_state = self.table_64[tuple_405_404]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_405_404] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_405_404[0]].append(tuple_405_404[1])
                                            self.index_970[tuple_405_404[1]].append(tuple_405_404[0])
                                        # Program VectorAppend Region
                                        vec_480.append(var_405)
                                # Program TransitionState Region
                                tuple_405_404 = (var_405, var_404)
                                prev_state = self.table_15[tuple_405_404]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_405_404] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_405_404[0]].append(tuple_405_404[1])
                        # Program TransitionState Region
                        tuple_405_404 = (var_405, var_404)
                        prev_state = self.table_106[tuple_405_404]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_405_404] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_405_404[1]].append(tuple_405_404[0])
                            # Program VectorAppend Region
                            vec_476.append(var_404)
                        # Program TransitionState Region
                        tuple_404 = var_404
                        prev_state = self.table_54[tuple_404]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_404] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_457.append(var_404)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_5:
                            # Program TransitionState Region
                            tuple_404 = var_404
                            prev_state = self.table_18[tuple_404]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_404] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_476.append(var_404)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_409: int
                                scan_index_409: int = 0
                                scan_tuple_409_vec: List[int] = self.index_128[var_404]
                                while scan_index_409 < len(scan_tuple_409_vec):
                                    scan_tuple_409 = scan_tuple_409_vec[scan_index_409]
                                    scan_index_409 += 1
                                    vec_409.append(scan_tuple_409)
                                # Program VectorLoop Region
                                vec_index409 = 0
                                while vec_index409 < len(vec_409):
                                    var_410 = vec_409[vec_index409]
                                    vec_index409 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_404_410 = (var_404, var_410)
                                    prev_state = self.table_27[tuple_404_410]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_404_410] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_404, var_410)

                                        # Program Call Region
                                        ret = self.proc_135_(var_404, var_410)

                                # Program TransitionState Region
                                tuple_404_404 = (var_404, var_404)
                                prev_state = self.table_6[tuple_404_404]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_404_404] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_404_404[1]].append(tuple_404_404[0])
                                        self.index_948[tuple_404_404[0]].append(tuple_404_404[1])
                                    # Program VectorAppend Region
                                    vec_392.append((var_404, var_404))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_5:
                            # Program TransitionState Region
                            tuple_405_404 = (var_405, var_404)
                            prev_state = self.table_58[tuple_405_404]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_405_404] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_405_404[0]].append(tuple_405_404[1])
                                # Program VectorAppend Region
                                vec_464.append(var_405)
        # Program VectorClear Region
        del vec_402[:]
        vec_index402 = 0
        # Program VectorUnique Region
        vec_413 = list(set(vec_413))
        vec_index413 = 0
        # Program TableJoin Region
        while vec_index413 < len(vec_413):
            var_415 = vec_413[vec_index413]
            vec_index413 += 1
            if var_415 in self.index_217:
                tuple_414_1_index: int = 0
                tuple_414_1_vec: List[int] = self.index_268[var_415]
                while tuple_414_1_index < len(tuple_414_1_vec):
                    tuple_414_1 = tuple_414_1_vec[tuple_414_1_index]
                    tuple_414_1_index += 1
                    var_416 = tuple_414_1
                    # Program TransitionState Region
                    tuple_416_415_3 = (var_416, var_415, self.var_3)
                    prev_state = self.table_9[tuple_416_415_3]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_416_415_3] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_416_415_3[0], tuple_416_415_3[1])].append(tuple_416_415_3[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_415_416 = (var_415, var_416)
                        prev_state = self.table_27[tuple_415_416]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_415_416] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_415_416[0]].append(tuple_415_416[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_415)
                        if not ret:
                            # Program TransitionState Region
                            tuple_415_416 = (var_415, var_416)
                            prev_state = self.table_27[tuple_415_416]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_415_416] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_415_416[0]].append(tuple_415_416[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_416, var_415)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_416_415 = (var_416, var_415)
                                    prev_state = self.table_64[tuple_416_415]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_416_415] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_416_415[0]].append(tuple_416_415[1])
                                            self.index_970[tuple_416_415[1]].append(tuple_416_415[0])
                                        # Program VectorAppend Region
                                        vec_480.append(var_416)
                                # Program TransitionState Region
                                tuple_416_415 = (var_416, var_415)
                                prev_state = self.table_15[tuple_416_415]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_416_415] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_416_415[0]].append(tuple_416_415[1])
                        # Program TransitionState Region
                        tuple_416_415 = (var_416, var_415)
                        prev_state = self.table_106[tuple_416_415]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_416_415] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_416_415[1]].append(tuple_416_415[0])
                            # Program VectorAppend Region
                            vec_476.append(var_415)
                        # Program TransitionState Region
                        tuple_415 = var_415
                        prev_state = self.table_54[tuple_415]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_415] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_457.append(var_415)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_3:
                            # Program TransitionState Region
                            tuple_415 = var_415
                            prev_state = self.table_18[tuple_415]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_415] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_476.append(var_415)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_420: int
                                scan_index_420: int = 0
                                scan_tuple_420_vec: List[int] = self.index_128[var_415]
                                while scan_index_420 < len(scan_tuple_420_vec):
                                    scan_tuple_420 = scan_tuple_420_vec[scan_index_420]
                                    scan_index_420 += 1
                                    vec_420.append(scan_tuple_420)
                                # Program VectorLoop Region
                                vec_index420 = 0
                                while vec_index420 < len(vec_420):
                                    var_421 = vec_420[vec_index420]
                                    vec_index420 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_415_421 = (var_415, var_421)
                                    prev_state = self.table_27[tuple_415_421]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_415_421] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_415, var_421)

                                        # Program Call Region
                                        ret = self.proc_135_(var_415, var_421)

                                # Program TransitionState Region
                                tuple_415_415 = (var_415, var_415)
                                prev_state = self.table_6[tuple_415_415]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_415_415] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_415_415[1]].append(tuple_415_415[0])
                                        self.index_948[tuple_415_415[0]].append(tuple_415_415[1])
                                    # Program VectorAppend Region
                                    vec_392.append((var_415, var_415))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_3:
                            # Program TransitionState Region
                            tuple_416_415 = (var_416, var_415)
                            prev_state = self.table_58[tuple_416_415]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_416_415] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_416_415[0]].append(tuple_416_415[1])
                                # Program VectorAppend Region
                                vec_464.append(var_416)
        # Program VectorClear Region
        del vec_413[:]
        vec_index413 = 0
        # Program VectorUnique Region
        vec_424 = list(set(vec_424))
        vec_index424 = 0
        # Program TableJoin Region
        while vec_index424 < len(vec_424):
            var_426 = vec_424[vec_index424]
            vec_index424 += 1
            if var_426 in self.index_217:
                tuple_425_1_index: int = 0
                tuple_425_1_vec: List[int] = self.index_280[var_426]
                while tuple_425_1_index < len(tuple_425_1_vec):
                    tuple_425_1 = tuple_425_1_vec[tuple_425_1_index]
                    tuple_425_1_index += 1
                    var_427 = tuple_425_1
                    # Program TransitionState Region
                    tuple_427_426_0 = (var_427, var_426, self.var_0)
                    prev_state = self.table_9[tuple_427_426_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_427_426_0] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_427_426_0[0], tuple_427_426_0[1])].append(tuple_427_426_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_426_427 = (var_426, var_427)
                        prev_state = self.table_27[tuple_426_427]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_426_427] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_426_427[0]].append(tuple_426_427[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_426)
                        if not ret:
                            # Program TransitionState Region
                            tuple_426_427 = (var_426, var_427)
                            prev_state = self.table_27[tuple_426_427]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_426_427] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_426_427[0]].append(tuple_426_427[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_427, var_426)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_427_426 = (var_427, var_426)
                                    prev_state = self.table_64[tuple_427_426]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_427_426] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_427_426[0]].append(tuple_427_426[1])
                                            self.index_970[tuple_427_426[1]].append(tuple_427_426[0])
                                        # Program VectorAppend Region
                                        vec_480.append(var_427)
                                # Program TransitionState Region
                                tuple_427_426 = (var_427, var_426)
                                prev_state = self.table_15[tuple_427_426]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_427_426] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_427_426[0]].append(tuple_427_426[1])
                        # Program TransitionState Region
                        tuple_427_426 = (var_427, var_426)
                        prev_state = self.table_106[tuple_427_426]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_427_426] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_427_426[1]].append(tuple_427_426[0])
                            # Program VectorAppend Region
                            vec_476.append(var_426)
                        # Program TransitionState Region
                        tuple_426 = var_426
                        prev_state = self.table_54[tuple_426]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_426] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_457.append(var_426)
                        # Program TransitionState Region
                        tuple_426 = var_426
                        prev_state = self.table_18[tuple_426]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_426] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_476.append(var_426)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_431: int
                            scan_index_431: int = 0
                            scan_tuple_431_vec: List[int] = self.index_128[var_426]
                            while scan_index_431 < len(scan_tuple_431_vec):
                                scan_tuple_431 = scan_tuple_431_vec[scan_index_431]
                                scan_index_431 += 1
                                vec_431.append(scan_tuple_431)
                            # Program VectorLoop Region
                            vec_index431 = 0
                            while vec_index431 < len(vec_431):
                                var_432 = vec_431[vec_index431]
                                vec_index431 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_426_432 = (var_426, var_432)
                                prev_state = self.table_27[tuple_426_432]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_426_432] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_131_(var_426, var_432)

                                    # Program Call Region
                                    ret = self.proc_135_(var_426, var_432)

                            # Program TransitionState Region
                            tuple_426_426 = (var_426, var_426)
                            prev_state = self.table_6[tuple_426_426]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_426_426] = 1 | 4
                                if not present_bit:
                                    self.index_350[tuple_426_426[1]].append(tuple_426_426[0])
                                    self.index_948[tuple_426_426[0]].append(tuple_426_426[1])
                                # Program VectorAppend Region
                                vec_392.append((var_426, var_426))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_427_426 = (var_427, var_426)
                            prev_state = self.table_58[tuple_427_426]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_427_426] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_427_426[0]].append(tuple_427_426[1])
                                # Program VectorAppend Region
                                vec_464.append(var_427)
        # Program VectorClear Region
        del vec_424[:]
        vec_index424 = 0
        # Program VectorUnique Region
        vec_435 = list(set(vec_435))
        vec_index435 = 0
        # Program TableJoin Region
        while vec_index435 < len(vec_435):
            var_437 = vec_435[vec_index435]
            vec_index435 += 1
            if var_437 in self.index_217:
                tuple_436_1_index: int = 0
                tuple_436_1_vec: List[int] = self.index_292[var_437]
                while tuple_436_1_index < len(tuple_436_1_vec):
                    tuple_436_1 = tuple_436_1_vec[tuple_436_1_index]
                    tuple_436_1_index += 1
                    var_438 = tuple_436_1
                    # Program TransitionState Region
                    tuple_438_437_0 = (var_438, var_437, self.var_0)
                    prev_state = self.table_9[tuple_438_437_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_438_437_0] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_438_437_0[0], tuple_438_437_0[1])].append(tuple_438_437_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_437_438 = (var_437, var_438)
                        prev_state = self.table_27[tuple_437_438]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_437_438] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_437_438[0]].append(tuple_437_438[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_437)
                        if not ret:
                            # Program TransitionState Region
                            tuple_437_438 = (var_437, var_438)
                            prev_state = self.table_27[tuple_437_438]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_437_438] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_437_438[0]].append(tuple_437_438[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_438, var_437)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_438_437 = (var_438, var_437)
                                    prev_state = self.table_64[tuple_438_437]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_438_437] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_438_437[0]].append(tuple_438_437[1])
                                            self.index_970[tuple_438_437[1]].append(tuple_438_437[0])
                                        # Program VectorAppend Region
                                        vec_480.append(var_438)
                                # Program TransitionState Region
                                tuple_438_437 = (var_438, var_437)
                                prev_state = self.table_15[tuple_438_437]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_438_437] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_438_437[0]].append(tuple_438_437[1])
                        # Program TransitionState Region
                        tuple_438_437 = (var_438, var_437)
                        prev_state = self.table_106[tuple_438_437]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_438_437] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_438_437[1]].append(tuple_438_437[0])
                            # Program VectorAppend Region
                            vec_476.append(var_437)
                        # Program TransitionState Region
                        tuple_437 = var_437
                        prev_state = self.table_54[tuple_437]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_437] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_457.append(var_437)
                        # Program TransitionState Region
                        tuple_437 = var_437
                        prev_state = self.table_18[tuple_437]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_437] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_476.append(var_437)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_442: int
                            scan_index_442: int = 0
                            scan_tuple_442_vec: List[int] = self.index_128[var_437]
                            while scan_index_442 < len(scan_tuple_442_vec):
                                scan_tuple_442 = scan_tuple_442_vec[scan_index_442]
                                scan_index_442 += 1
                                vec_442.append(scan_tuple_442)
                            # Program VectorLoop Region
                            vec_index442 = 0
                            while vec_index442 < len(vec_442):
                                var_443 = vec_442[vec_index442]
                                vec_index442 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_437_443 = (var_437, var_443)
                                prev_state = self.table_27[tuple_437_443]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_437_443] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_131_(var_437, var_443)

                                    # Program Call Region
                                    ret = self.proc_135_(var_437, var_443)

                            # Program TransitionState Region
                            tuple_437_437 = (var_437, var_437)
                            prev_state = self.table_6[tuple_437_437]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_437_437] = 1 | 4
                                if not present_bit:
                                    self.index_350[tuple_437_437[1]].append(tuple_437_437[0])
                                    self.index_948[tuple_437_437[0]].append(tuple_437_437[1])
                                # Program VectorAppend Region
                                vec_392.append((var_437, var_437))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_438_437 = (var_438, var_437)
                            prev_state = self.table_58[tuple_438_437]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_438_437] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_438_437[0]].append(tuple_438_437[1])
                                # Program VectorAppend Region
                                vec_464.append(var_438)
        # Program VectorClear Region
        del vec_435[:]
        vec_index435 = 0
        # Program VectorUnique Region
        vec_446 = list(set(vec_446))
        vec_index446 = 0
        # Program TableJoin Region
        while vec_index446 < len(vec_446):
            var_448 = vec_446[vec_index446]
            vec_index446 += 1
            if var_448 in self.index_217:
                tuple_447_1_index: int = 0
                tuple_447_1_vec: List[int] = self.index_304[var_448]
                while tuple_447_1_index < len(tuple_447_1_vec):
                    tuple_447_1 = tuple_447_1_vec[tuple_447_1_index]
                    tuple_447_1_index += 1
                    var_449 = tuple_447_1
                    # Program TransitionState Region
                    tuple_449_448_2 = (var_449, var_448, self.var_2)
                    prev_state = self.table_9[tuple_449_448_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_449_448_2] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_449_448_2[0], tuple_449_448_2[1])].append(tuple_449_448_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_448_449 = (var_448, var_449)
                        prev_state = self.table_27[tuple_448_449]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_448_449] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_448_449[0]].append(tuple_448_449[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_448)
                        if not ret:
                            # Program TransitionState Region
                            tuple_448_449 = (var_448, var_449)
                            prev_state = self.table_27[tuple_448_449]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_448_449] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_448_449[0]].append(tuple_448_449[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_449, var_448)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_449_448 = (var_449, var_448)
                                    prev_state = self.table_64[tuple_449_448]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_449_448] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_449_448[0]].append(tuple_449_448[1])
                                            self.index_970[tuple_449_448[1]].append(tuple_449_448[0])
                                        # Program VectorAppend Region
                                        vec_480.append(var_449)
                                # Program TransitionState Region
                                tuple_449_448 = (var_449, var_448)
                                prev_state = self.table_15[tuple_449_448]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_449_448] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_449_448[0]].append(tuple_449_448[1])
                        # Program TransitionState Region
                        tuple_449_448 = (var_449, var_448)
                        prev_state = self.table_106[tuple_449_448]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_449_448] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_449_448[1]].append(tuple_449_448[0])
                            # Program VectorAppend Region
                            vec_476.append(var_448)
                        # Program TransitionState Region
                        tuple_448 = var_448
                        prev_state = self.table_54[tuple_448]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_448] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_457.append(var_448)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_448 = var_448
                            prev_state = self.table_18[tuple_448]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_448] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_476.append(var_448)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_453: int
                                scan_index_453: int = 0
                                scan_tuple_453_vec: List[int] = self.index_128[var_448]
                                while scan_index_453 < len(scan_tuple_453_vec):
                                    scan_tuple_453 = scan_tuple_453_vec[scan_index_453]
                                    scan_index_453 += 1
                                    vec_453.append(scan_tuple_453)
                                # Program VectorLoop Region
                                vec_index453 = 0
                                while vec_index453 < len(vec_453):
                                    var_454 = vec_453[vec_index453]
                                    vec_index453 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_448_454 = (var_448, var_454)
                                    prev_state = self.table_27[tuple_448_454]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_448_454] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_448, var_454)

                                        # Program Call Region
                                        ret = self.proc_135_(var_448, var_454)

                                # Program TransitionState Region
                                tuple_448_448 = (var_448, var_448)
                                prev_state = self.table_6[tuple_448_448]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_448_448] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_448_448[1]].append(tuple_448_448[0])
                                        self.index_948[tuple_448_448[0]].append(tuple_448_448[1])
                                    # Program VectorAppend Region
                                    vec_392.append((var_448, var_448))
                        # Program TransitionState Region
                        tuple_449_448 = (var_449, var_448)
                        prev_state = self.table_58[tuple_449_448]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_58[tuple_449_448] = 1 | 4
                            if not present_bit:
                                self.index_325[tuple_449_448[0]].append(tuple_449_448[1])
                            # Program VectorAppend Region
                            vec_464.append(var_449)
        # Program VectorClear Region
        del vec_446[:]
        vec_index446 = 0
        # Program VectorUnique Region
        vec_457 = list(set(vec_457))
        vec_index457 = 0
        # Program TableJoin Region
        while vec_index457 < len(vec_457):
            var_459 = vec_457[vec_index457]
            vec_index457 += 1
            if var_459 in self.index_316:
                if var_459 in self.index_317:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_459 = var_459
                    prev_state = self.table_18[tuple_459]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_459] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_476.append(var_459)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_460: int
                        scan_index_460: int = 0
                        scan_tuple_460_vec: List[int] = self.index_128[var_459]
                        while scan_index_460 < len(scan_tuple_460_vec):
                            scan_tuple_460 = scan_tuple_460_vec[scan_index_460]
                            scan_index_460 += 1
                            vec_460.append(scan_tuple_460)
                        # Program VectorLoop Region
                        vec_index460 = 0
                        while vec_index460 < len(vec_460):
                            var_461 = vec_460[vec_index460]
                            vec_index460 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_459_461 = (var_459, var_461)
                            prev_state = self.table_27[tuple_459_461]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_459_461] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_459, var_461)

                                # Program Call Region
                                ret = self.proc_135_(var_459, var_461)

                        # Program TransitionState Region
                        tuple_459_459 = (var_459, var_459)
                        prev_state = self.table_6[tuple_459_459]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_459_459] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_459_459[1]].append(tuple_459_459[0])
                                self.index_948[tuple_459_459[0]].append(tuple_459_459[1])
                            # Program VectorAppend Region
                            vec_392.append((var_459, var_459))
        # Program VectorClear Region
        del vec_457[:]
        vec_index457 = 0
        # Program VectorUnique Region
        vec_464 = list(set(vec_464))
        vec_index464 = 0
        # Program TableJoin Region
        while vec_index464 < len(vec_464):
            var_466 = vec_464[vec_index464]
            vec_index464 += 1
            if var_466 in self.index_211:
                tuple_465_1_index: int = 0
                tuple_465_1_vec: List[int] = self.index_325[var_466]
                while tuple_465_1_index < len(tuple_465_1_vec):
                    tuple_465_1 = tuple_465_1_vec[tuple_465_1_index]
                    tuple_465_1_index += 1
                    var_467 = tuple_465_1
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_466_467 = (var_466, var_467)
                    prev_state = self.table_61[tuple_466_467]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_61[tuple_466_467] = 1 | 4
                        if not present_bit:
                            self.index_330[tuple_466_467[1]].append(tuple_466_467[0])
                        # Program VectorAppend Region
                        vec_468.append(var_467)
        # Program VectorClear Region
        del vec_464[:]
        vec_index464 = 0
        # Program VectorUnique Region
        vec_468 = list(set(vec_468))
        vec_index468 = 0
        # Program TableJoin Region
        while vec_index468 < len(vec_468):
            var_470 = vec_468[vec_index468]
            vec_index468 += 1
            if var_470 in self.index_316:
                tuple_469_1_index: int = 0
                tuple_469_1_vec: List[int] = self.index_330[var_470]
                while tuple_469_1_index < len(tuple_469_1_vec):
                    tuple_469_1 = tuple_469_1_vec[tuple_469_1_index]
                    tuple_469_1_index += 1
                    var_471 = tuple_469_1
                    # Program TransitionState Region
                    tuple_471 = var_471
                    prev_state = self.table_18[tuple_471]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_471] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_476.append(var_471)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_472: int
                        scan_index_472: int = 0
                        scan_tuple_472_vec: List[int] = self.index_128[var_471]
                        while scan_index_472 < len(scan_tuple_472_vec):
                            scan_tuple_472 = scan_tuple_472_vec[scan_index_472]
                            scan_index_472 += 1
                            vec_472.append(scan_tuple_472)
                        # Program VectorLoop Region
                        vec_index472 = 0
                        while vec_index472 < len(vec_472):
                            var_473 = vec_472[vec_index472]
                            vec_index472 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_471_473 = (var_471, var_473)
                            prev_state = self.table_27[tuple_471_473]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_471_473] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_471, var_473)

                                # Program Call Region
                                ret = self.proc_135_(var_471, var_473)

                        # Program TransitionState Region
                        tuple_471_471 = (var_471, var_471)
                        prev_state = self.table_6[tuple_471_471]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_471_471] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_471_471[1]].append(tuple_471_471[0])
                                self.index_948[tuple_471_471[0]].append(tuple_471_471[1])
                            # Program VectorAppend Region
                            vec_392.append((var_471, var_471))
        # Program VectorClear Region
        del vec_468[:]
        vec_index468 = 0
        # Program VectorUnique Region
        vec_476 = list(set(vec_476))
        vec_index476 = 0
        # Program TableJoin Region
        while vec_index476 < len(vec_476):
            var_478 = vec_476[vec_index476]
            vec_index476 += 1
            tuple_477_0_index: int = 0
            tuple_477_0_vec: List[int] = self.index_339[var_478]
            while tuple_477_0_index < len(tuple_477_0_vec):
                tuple_477_0 = tuple_477_0_vec[tuple_477_0_index]
                tuple_477_0_index += 1
                var_479 = tuple_477_0
                if var_478 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_479_478 = (var_479, var_478)
                    prev_state = self.table_109[tuple_479_478]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_479_478] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_479_478[1]].append(tuple_479_478[0])
                        # Program VectorAppend Region
                        vec_488.append(var_478)
                    # Program TransitionState Region
                    tuple_479_478 = (var_479, var_478)
                    prev_state = self.table_22[tuple_479_478]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_479_478] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_479_478[0]].append(tuple_479_478[1])
        # Program VectorClear Region
        del vec_476[:]
        vec_index476 = 0
        # Program VectorUnique Region
        vec_480 = list(set(vec_480))
        vec_index480 = 0
        # Program TableJoin Region
        while vec_index480 < len(vec_480):
            var_482 = vec_480[vec_index480]
            vec_index480 += 1
            tuple_481_0_index: int = 0
            tuple_481_0_vec: List[int] = self.index_350[var_482]
            while tuple_481_0_index < len(tuple_481_0_vec):
                tuple_481_0 = tuple_481_0_vec[tuple_481_0_index]
                tuple_481_0_index += 1
                var_483 = tuple_481_0
                tuple_481_1_index: int = 0
                tuple_481_1_vec: List[int] = self.index_351[var_482]
                while tuple_481_1_index < len(tuple_481_1_vec):
                    tuple_481_1 = tuple_481_1_vec[tuple_481_1_index]
                    tuple_481_1_index += 1
                    var_484 = tuple_481_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_354_(var_483, var_482)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_224_(var_482, var_484)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_359_(var_483, var_484)
                            if not ret:
                                # Program TransitionState Region
                                tuple_483_484 = (var_483, var_484)
                                prev_state = self.table_6[tuple_483_484]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_483_484] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_483_484[1]].append(tuple_483_484[0])
                                        self.index_948[tuple_483_484[0]].append(tuple_483_484[1])
                                    # Program VectorAppend Region
                                    vec_392.append((var_483, var_484))
        # Program VectorClear Region
        del vec_480[:]
        vec_index480 = 0
        # Program VectorUnique Region
        vec_488 = list(set(vec_488))
        vec_index488 = 0
        # Program TableJoin Region
        while vec_index488 < len(vec_488):
            var_490 = vec_488[vec_index488]
            vec_index488 += 1
            tuple_489_0_index: int = 0
            tuple_489_0_vec: List[int] = self.index_345[var_490]
            while tuple_489_0_index < len(tuple_489_0_vec):
                tuple_489_0 = tuple_489_0_vec[tuple_489_0_index]
                tuple_489_0_index += 1
                var_491 = tuple_489_0
                if var_490 in self.index_316:
                    # Program TransitionState Region
                    tuple_491 = var_491
                    prev_state = self.table_13[tuple_491]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_491] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_488[:]
        vec_index488 = 0
        # Induction Fixpoint Loop Region
        while len(vec_392):
            # Program Call Region
            param_394_0 = [vec_392]
            ret = self.proc_139_(param_394_0)
            vec_392 = param_394_0[0]

        vec_index392 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_392[:]
        vec_index392 = 0
        # Program Return Region
        return False
        return False

    def entrypoint_1(self, vec_493: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index493: int = 0
        vec_495: List[int] = list()
        vec_index495: int = 0
        vec_498: List[int] = list()
        vec_index498: int = 0
        vec_502: List[Tuple[int, int]] = list()
        vec_index502: int = 0
        vec_505: List[int] = list()
        vec_index505: int = 0
        vec_509: List[int] = list()
        vec_index509: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index493 = 0
        while vec_index493 < len(vec_493):
            var_494 = vec_493[vec_index493]
            vec_index493 += 1
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_494 = var_494
            prev_state = self.table_30[tuple_494]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_494] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_495.append(var_494)
        # Program VectorUnique Region
        vec_495 = list(set(vec_495))
        vec_index495 = 0
        # Program TableJoin Region
        while vec_index495 < len(vec_495):
            var_497 = vec_495[vec_index495]
            vec_index495 += 1
            if var_497 in self.index_235:
                if var_497 in self.index_217:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_497 = var_497
                    prev_state = self.table_18[tuple_497]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_497] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_505.append(var_497)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_498: int
                        scan_index_498: int = 0
                        scan_tuple_498_vec: List[int] = self.index_128[var_497]
                        while scan_index_498 < len(scan_tuple_498_vec):
                            scan_tuple_498 = scan_tuple_498_vec[scan_index_498]
                            scan_index_498 += 1
                            vec_498.append(scan_tuple_498)
                        # Program VectorLoop Region
                        vec_index498 = 0
                        while vec_index498 < len(vec_498):
                            var_499 = vec_498[vec_index498]
                            vec_index498 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_497_499 = (var_497, var_499)
                            prev_state = self.table_27[tuple_497_499]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_497_499] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_497, var_499)

                                # Program Call Region
                                ret = self.proc_135_(var_497, var_499)

                        # Program TransitionState Region
                        tuple_497_497 = (var_497, var_497)
                        prev_state = self.table_6[tuple_497_497]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_497_497] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_497_497[1]].append(tuple_497_497[0])
                                self.index_948[tuple_497_497[0]].append(tuple_497_497[1])
                            # Program VectorAppend Region
                            vec_502.append((var_497, var_497))
        # Program VectorClear Region
        del vec_495[:]
        vec_index495 = 0
        # Program VectorUnique Region
        vec_505 = list(set(vec_505))
        vec_index505 = 0
        # Program TableJoin Region
        while vec_index505 < len(vec_505):
            var_507 = vec_505[vec_index505]
            vec_index505 += 1
            tuple_506_0_index: int = 0
            tuple_506_0_vec: List[int] = self.index_339[var_507]
            while tuple_506_0_index < len(tuple_506_0_vec):
                tuple_506_0 = tuple_506_0_vec[tuple_506_0_index]
                tuple_506_0_index += 1
                var_508 = tuple_506_0
                if var_507 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_508_507 = (var_508, var_507)
                    prev_state = self.table_109[tuple_508_507]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_508_507] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_508_507[1]].append(tuple_508_507[0])
                        # Program VectorAppend Region
                        vec_509.append(var_507)
                    # Program TransitionState Region
                    tuple_508_507 = (var_508, var_507)
                    prev_state = self.table_22[tuple_508_507]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_508_507] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_508_507[0]].append(tuple_508_507[1])
        # Program VectorClear Region
        del vec_505[:]
        vec_index505 = 0
        # Program VectorUnique Region
        vec_509 = list(set(vec_509))
        vec_index509 = 0
        # Program TableJoin Region
        while vec_index509 < len(vec_509):
            var_511 = vec_509[vec_index509]
            vec_index509 += 1
            tuple_510_0_index: int = 0
            tuple_510_0_vec: List[int] = self.index_345[var_511]
            while tuple_510_0_index < len(tuple_510_0_vec):
                tuple_510_0 = tuple_510_0_vec[tuple_510_0_index]
                tuple_510_0_index += 1
                var_512 = tuple_510_0
                if var_511 in self.index_316:
                    # Program TransitionState Region
                    tuple_512 = var_512
                    prev_state = self.table_13[tuple_512]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_512] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_509[:]
        vec_index509 = 0
        # Induction Fixpoint Loop Region
        while len(vec_502):
            # Program Call Region
            param_504_0 = [vec_502]
            ret = self.proc_139_(param_504_0)
            vec_502 = param_504_0[0]

        vec_index502 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_502[:]
        vec_index502 = 0
        # Program Return Region
        return False
        return False

    def constructor_function_1(self, vec_514: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index514: int = 0
        vec_516: List[int] = list()
        vec_index516: int = 0
        vec_519: List[int] = list()
        vec_index519: int = 0
        vec_523: List[Tuple[int, int]] = list()
        vec_index523: int = 0
        vec_526: List[int] = list()
        vec_index526: int = 0
        vec_530: List[int] = list()
        vec_index530: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index514 = 0
        while vec_index514 < len(vec_514):
            var_515 = vec_514[vec_index514]
            vec_index514 += 1
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_515 = var_515
            prev_state = self.table_34[tuple_515]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_34[tuple_515] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_516.append(var_515)
        # Program VectorUnique Region
        vec_516 = list(set(vec_516))
        vec_index516 = 0
        # Program TableJoin Region
        while vec_index516 < len(vec_516):
            var_518 = vec_516[vec_index516]
            vec_index516 += 1
            if var_518 in self.index_197:
                if var_518 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_518 = var_518
                    prev_state = self.table_18[tuple_518]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_518] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_526.append(var_518)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_519: int
                        scan_index_519: int = 0
                        scan_tuple_519_vec: List[int] = self.index_128[var_518]
                        while scan_index_519 < len(scan_tuple_519_vec):
                            scan_tuple_519 = scan_tuple_519_vec[scan_index_519]
                            scan_index_519 += 1
                            vec_519.append(scan_tuple_519)
                        # Program VectorLoop Region
                        vec_index519 = 0
                        while vec_index519 < len(vec_519):
                            var_520 = vec_519[vec_index519]
                            vec_index519 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_518_520 = (var_518, var_520)
                            prev_state = self.table_27[tuple_518_520]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_518_520] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_518, var_520)

                                # Program Call Region
                                ret = self.proc_135_(var_518, var_520)

                        # Program TransitionState Region
                        tuple_518_518 = (var_518, var_518)
                        prev_state = self.table_6[tuple_518_518]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_518_518] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_518_518[1]].append(tuple_518_518[0])
                                self.index_948[tuple_518_518[0]].append(tuple_518_518[1])
                            # Program VectorAppend Region
                            vec_523.append((var_518, var_518))
        # Program VectorClear Region
        del vec_516[:]
        vec_index516 = 0
        # Program VectorUnique Region
        vec_526 = list(set(vec_526))
        vec_index526 = 0
        # Program TableJoin Region
        while vec_index526 < len(vec_526):
            var_528 = vec_526[vec_index526]
            vec_index526 += 1
            tuple_527_0_index: int = 0
            tuple_527_0_vec: List[int] = self.index_339[var_528]
            while tuple_527_0_index < len(tuple_527_0_vec):
                tuple_527_0 = tuple_527_0_vec[tuple_527_0_index]
                tuple_527_0_index += 1
                var_529 = tuple_527_0
                if var_528 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_529_528 = (var_529, var_528)
                    prev_state = self.table_109[tuple_529_528]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_529_528] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_529_528[1]].append(tuple_529_528[0])
                        # Program VectorAppend Region
                        vec_530.append(var_528)
                    # Program TransitionState Region
                    tuple_529_528 = (var_529, var_528)
                    prev_state = self.table_22[tuple_529_528]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_529_528] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_529_528[0]].append(tuple_529_528[1])
        # Program VectorClear Region
        del vec_526[:]
        vec_index526 = 0
        # Program VectorUnique Region
        vec_530 = list(set(vec_530))
        vec_index530 = 0
        # Program TableJoin Region
        while vec_index530 < len(vec_530):
            var_532 = vec_530[vec_index530]
            vec_index530 += 1
            tuple_531_0_index: int = 0
            tuple_531_0_vec: List[int] = self.index_345[var_532]
            while tuple_531_0_index < len(tuple_531_0_vec):
                tuple_531_0 = tuple_531_0_vec[tuple_531_0_index]
                tuple_531_0_index += 1
                var_533 = tuple_531_0
                if var_532 in self.index_316:
                    # Program TransitionState Region
                    tuple_533 = var_533
                    prev_state = self.table_13[tuple_533]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_533] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_530[:]
        vec_index530 = 0
        # Induction Fixpoint Loop Region
        while len(vec_523):
            # Program Call Region
            param_525_0 = [vec_523]
            ret = self.proc_139_(param_525_0)
            vec_523 = param_525_0[0]

        vec_index523 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_523[:]
        vec_index523 = 0
        # Program Return Region
        return False
        return False

    def destructor_function_1(self, vec_535: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index535: int = 0
        vec_537: List[int] = list()
        vec_index537: int = 0
        vec_540: List[int] = list()
        vec_index540: int = 0
        vec_544: List[Tuple[int, int]] = list()
        vec_index544: int = 0
        vec_547: List[int] = list()
        vec_index547: int = 0
        vec_551: List[int] = list()
        vec_index551: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index535 = 0
        while vec_index535 < len(vec_535):
            var_536 = vec_535[vec_index535]
            vec_index535 += 1
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_536 = var_536
            prev_state = self.table_38[tuple_536]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_536] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_537.append(var_536)
        # Program VectorUnique Region
        vec_537 = list(set(vec_537))
        vec_index537 = 0
        # Program TableJoin Region
        while vec_index537 < len(vec_537):
            var_539 = vec_537[vec_index537]
            vec_index537 += 1
            if var_539 in self.index_189:
                if var_539 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_539 = var_539
                    prev_state = self.table_18[tuple_539]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_539] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_547.append(var_539)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_540: int
                        scan_index_540: int = 0
                        scan_tuple_540_vec: List[int] = self.index_128[var_539]
                        while scan_index_540 < len(scan_tuple_540_vec):
                            scan_tuple_540 = scan_tuple_540_vec[scan_index_540]
                            scan_index_540 += 1
                            vec_540.append(scan_tuple_540)
                        # Program VectorLoop Region
                        vec_index540 = 0
                        while vec_index540 < len(vec_540):
                            var_541 = vec_540[vec_index540]
                            vec_index540 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_539_541 = (var_539, var_541)
                            prev_state = self.table_27[tuple_539_541]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_539_541] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_539, var_541)

                                # Program Call Region
                                ret = self.proc_135_(var_539, var_541)

                        # Program TransitionState Region
                        tuple_539_539 = (var_539, var_539)
                        prev_state = self.table_6[tuple_539_539]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_539_539] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_539_539[1]].append(tuple_539_539[0])
                                self.index_948[tuple_539_539[0]].append(tuple_539_539[1])
                            # Program VectorAppend Region
                            vec_544.append((var_539, var_539))
        # Program VectorClear Region
        del vec_537[:]
        vec_index537 = 0
        # Program VectorUnique Region
        vec_547 = list(set(vec_547))
        vec_index547 = 0
        # Program TableJoin Region
        while vec_index547 < len(vec_547):
            var_549 = vec_547[vec_index547]
            vec_index547 += 1
            tuple_548_0_index: int = 0
            tuple_548_0_vec: List[int] = self.index_339[var_549]
            while tuple_548_0_index < len(tuple_548_0_vec):
                tuple_548_0 = tuple_548_0_vec[tuple_548_0_index]
                tuple_548_0_index += 1
                var_550 = tuple_548_0
                if var_549 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_550_549 = (var_550, var_549)
                    prev_state = self.table_109[tuple_550_549]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_550_549] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_550_549[1]].append(tuple_550_549[0])
                        # Program VectorAppend Region
                        vec_551.append(var_549)
                    # Program TransitionState Region
                    tuple_550_549 = (var_550, var_549)
                    prev_state = self.table_22[tuple_550_549]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_550_549] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_550_549[0]].append(tuple_550_549[1])
        # Program VectorClear Region
        del vec_547[:]
        vec_index547 = 0
        # Program VectorUnique Region
        vec_551 = list(set(vec_551))
        vec_index551 = 0
        # Program TableJoin Region
        while vec_index551 < len(vec_551):
            var_553 = vec_551[vec_index551]
            vec_index551 += 1
            tuple_552_0_index: int = 0
            tuple_552_0_vec: List[int] = self.index_345[var_553]
            while tuple_552_0_index < len(tuple_552_0_vec):
                tuple_552_0 = tuple_552_0_vec[tuple_552_0_index]
                tuple_552_0_index += 1
                var_554 = tuple_552_0
                if var_553 in self.index_316:
                    # Program TransitionState Region
                    tuple_554 = var_554
                    prev_state = self.table_13[tuple_554]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_554] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_551[:]
        vec_index551 = 0
        # Induction Fixpoint Loop Region
        while len(vec_544):
            # Program Call Region
            param_546_0 = [vec_544]
            ret = self.proc_139_(param_546_0)
            vec_544 = param_546_0[0]

        vec_index544 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_544[:]
        vec_index544 = 0
        # Program Return Region
        return False
        return False

    def imported_function_2(self, vec_556: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index556: int = 0
        vec_559: List[int] = list()
        vec_index559: int = 0
        vec_562: List[int] = list()
        vec_index562: int = 0
        vec_566: List[Tuple[int, int]] = list()
        vec_index566: int = 0
        vec_569: List[int] = list()
        vec_index569: int = 0
        vec_573: List[int] = list()
        vec_index573: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index556 = 0
        while vec_index556 < len(vec_556):
            var_557, var_558 = vec_556[vec_index556]
            vec_index556 += 1
            # Program TransitionState Region
            tuple_557 = var_557
            prev_state = self.table_40[tuple_557]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_40[tuple_557] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_559.append(var_557)
        # Program VectorUnique Region
        vec_559 = list(set(vec_559))
        vec_index559 = 0
        # Program TableJoin Region
        while vec_index559 < len(vec_559):
            var_561 = vec_559[vec_index559]
            vec_index559 += 1
            if var_561 in self.index_181:
                if var_561 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_561 = var_561
                    prev_state = self.table_18[tuple_561]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_561] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_569.append(var_561)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_562: int
                        scan_index_562: int = 0
                        scan_tuple_562_vec: List[int] = self.index_128[var_561]
                        while scan_index_562 < len(scan_tuple_562_vec):
                            scan_tuple_562 = scan_tuple_562_vec[scan_index_562]
                            scan_index_562 += 1
                            vec_562.append(scan_tuple_562)
                        # Program VectorLoop Region
                        vec_index562 = 0
                        while vec_index562 < len(vec_562):
                            var_563 = vec_562[vec_index562]
                            vec_index562 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_561_563 = (var_561, var_563)
                            prev_state = self.table_27[tuple_561_563]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_561_563] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_561, var_563)

                                # Program Call Region
                                ret = self.proc_135_(var_561, var_563)

                        # Program TransitionState Region
                        tuple_561_561 = (var_561, var_561)
                        prev_state = self.table_6[tuple_561_561]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_561_561] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_561_561[1]].append(tuple_561_561[0])
                                self.index_948[tuple_561_561[0]].append(tuple_561_561[1])
                            # Program VectorAppend Region
                            vec_566.append((var_561, var_561))
        # Program VectorClear Region
        del vec_559[:]
        vec_index559 = 0
        # Program VectorUnique Region
        vec_569 = list(set(vec_569))
        vec_index569 = 0
        # Program TableJoin Region
        while vec_index569 < len(vec_569):
            var_571 = vec_569[vec_index569]
            vec_index569 += 1
            tuple_570_0_index: int = 0
            tuple_570_0_vec: List[int] = self.index_339[var_571]
            while tuple_570_0_index < len(tuple_570_0_vec):
                tuple_570_0 = tuple_570_0_vec[tuple_570_0_index]
                tuple_570_0_index += 1
                var_572 = tuple_570_0
                if var_571 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_572_571 = (var_572, var_571)
                    prev_state = self.table_109[tuple_572_571]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_572_571] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_572_571[1]].append(tuple_572_571[0])
                        # Program VectorAppend Region
                        vec_573.append(var_571)
                    # Program TransitionState Region
                    tuple_572_571 = (var_572, var_571)
                    prev_state = self.table_22[tuple_572_571]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_572_571] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_572_571[0]].append(tuple_572_571[1])
        # Program VectorClear Region
        del vec_569[:]
        vec_index569 = 0
        # Program VectorUnique Region
        vec_573 = list(set(vec_573))
        vec_index573 = 0
        # Program TableJoin Region
        while vec_index573 < len(vec_573):
            var_575 = vec_573[vec_index573]
            vec_index573 += 1
            tuple_574_0_index: int = 0
            tuple_574_0_vec: List[int] = self.index_345[var_575]
            while tuple_574_0_index < len(tuple_574_0_vec):
                tuple_574_0 = tuple_574_0_vec[tuple_574_0_index]
                tuple_574_0_index += 1
                var_576 = tuple_574_0
                if var_575 in self.index_316:
                    # Program TransitionState Region
                    tuple_576 = var_576
                    prev_state = self.table_13[tuple_576]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_576] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_573[:]
        vec_index573 = 0
        # Induction Fixpoint Loop Region
        while len(vec_566):
            # Program Call Region
            param_568_0 = [vec_566]
            ret = self.proc_139_(param_568_0)
            vec_566 = param_568_0[0]

        vec_index566 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_566[:]
        vec_index566 = 0
        # Program Return Region
        return False
        return False

    def exported_function_2(self, vec_578: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index578: int = 0
        vec_581: List[int] = list()
        vec_index581: int = 0
        vec_584: List[int] = list()
        vec_index584: int = 0
        vec_588: List[Tuple[int, int]] = list()
        vec_index588: int = 0
        vec_591: List[int] = list()
        vec_index591: int = 0
        vec_595: List[int] = list()
        vec_index595: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index578 = 0
        while vec_index578 < len(vec_578):
            var_579, var_580 = vec_578[vec_index578]
            vec_index578 += 1
            # Program TransitionState Region
            tuple_579 = var_579
            prev_state = self.table_42[tuple_579]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_42[tuple_579] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_581.append(var_579)
        # Program VectorUnique Region
        vec_581 = list(set(vec_581))
        vec_index581 = 0
        # Program TableJoin Region
        while vec_index581 < len(vec_581):
            var_583 = vec_581[vec_index581]
            vec_index581 += 1
            if var_583 in self.index_173:
                if var_583 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_583 = var_583
                    prev_state = self.table_18[tuple_583]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_583] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_591.append(var_583)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_584: int
                        scan_index_584: int = 0
                        scan_tuple_584_vec: List[int] = self.index_128[var_583]
                        while scan_index_584 < len(scan_tuple_584_vec):
                            scan_tuple_584 = scan_tuple_584_vec[scan_index_584]
                            scan_index_584 += 1
                            vec_584.append(scan_tuple_584)
                        # Program VectorLoop Region
                        vec_index584 = 0
                        while vec_index584 < len(vec_584):
                            var_585 = vec_584[vec_index584]
                            vec_index584 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_583_585 = (var_583, var_585)
                            prev_state = self.table_27[tuple_583_585]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_583_585] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_583, var_585)

                                # Program Call Region
                                ret = self.proc_135_(var_583, var_585)

                        # Program TransitionState Region
                        tuple_583_583 = (var_583, var_583)
                        prev_state = self.table_6[tuple_583_583]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_583_583] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_583_583[1]].append(tuple_583_583[0])
                                self.index_948[tuple_583_583[0]].append(tuple_583_583[1])
                            # Program VectorAppend Region
                            vec_588.append((var_583, var_583))
        # Program VectorClear Region
        del vec_581[:]
        vec_index581 = 0
        # Program VectorUnique Region
        vec_591 = list(set(vec_591))
        vec_index591 = 0
        # Program TableJoin Region
        while vec_index591 < len(vec_591):
            var_593 = vec_591[vec_index591]
            vec_index591 += 1
            tuple_592_0_index: int = 0
            tuple_592_0_vec: List[int] = self.index_339[var_593]
            while tuple_592_0_index < len(tuple_592_0_vec):
                tuple_592_0 = tuple_592_0_vec[tuple_592_0_index]
                tuple_592_0_index += 1
                var_594 = tuple_592_0
                if var_593 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_594_593 = (var_594, var_593)
                    prev_state = self.table_109[tuple_594_593]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_594_593] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_594_593[1]].append(tuple_594_593[0])
                        # Program VectorAppend Region
                        vec_595.append(var_593)
                    # Program TransitionState Region
                    tuple_594_593 = (var_594, var_593)
                    prev_state = self.table_22[tuple_594_593]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_594_593] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_594_593[0]].append(tuple_594_593[1])
        # Program VectorClear Region
        del vec_591[:]
        vec_index591 = 0
        # Program VectorUnique Region
        vec_595 = list(set(vec_595))
        vec_index595 = 0
        # Program TableJoin Region
        while vec_index595 < len(vec_595):
            var_597 = vec_595[vec_index595]
            vec_index595 += 1
            tuple_596_0_index: int = 0
            tuple_596_0_vec: List[int] = self.index_345[var_597]
            while tuple_596_0_index < len(tuple_596_0_vec):
                tuple_596_0 = tuple_596_0_vec[tuple_596_0_index]
                tuple_596_0_index += 1
                var_598 = tuple_596_0
                if var_597 in self.index_316:
                    # Program TransitionState Region
                    tuple_598 = var_598
                    prev_state = self.table_13[tuple_598]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_598] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_595[:]
        vec_index595 = 0
        # Induction Fixpoint Loop Region
        while len(vec_588):
            # Program Call Region
            param_590_0 = [vec_588]
            ret = self.proc_139_(param_590_0)
            vec_588 = param_590_0[0]

        vec_index588 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_588[:]
        vec_index588 = 0
        # Program Return Region
        return False
        return False

    def local_function_2(self, vec_600: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index600: int = 0
        vec_603: List[int] = list()
        vec_index603: int = 0
        vec_606: List[int] = list()
        vec_index606: int = 0
        vec_610: List[Tuple[int, int]] = list()
        vec_index610: int = 0
        vec_613: List[int] = list()
        vec_index613: int = 0
        vec_617: List[int] = list()
        vec_index617: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index600 = 0
        while vec_index600 < len(vec_600):
            var_601, var_602 = vec_600[vec_index600]
            vec_index600 += 1
            # Program TransitionState Region
            tuple_601 = var_601
            prev_state = self.table_44[tuple_601]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_44[tuple_601] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_603.append(var_601)
        # Program VectorUnique Region
        vec_603 = list(set(vec_603))
        vec_index603 = 0
        # Program TableJoin Region
        while vec_index603 < len(vec_603):
            var_605 = vec_603[vec_index603]
            vec_index603 += 1
            if var_605 in self.index_165:
                if var_605 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_605 = var_605
                    prev_state = self.table_18[tuple_605]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_605] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_613.append(var_605)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_606: int
                        scan_index_606: int = 0
                        scan_tuple_606_vec: List[int] = self.index_128[var_605]
                        while scan_index_606 < len(scan_tuple_606_vec):
                            scan_tuple_606 = scan_tuple_606_vec[scan_index_606]
                            scan_index_606 += 1
                            vec_606.append(scan_tuple_606)
                        # Program VectorLoop Region
                        vec_index606 = 0
                        while vec_index606 < len(vec_606):
                            var_607 = vec_606[vec_index606]
                            vec_index606 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_605_607 = (var_605, var_607)
                            prev_state = self.table_27[tuple_605_607]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_605_607] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_605, var_607)

                                # Program Call Region
                                ret = self.proc_135_(var_605, var_607)

                        # Program TransitionState Region
                        tuple_605_605 = (var_605, var_605)
                        prev_state = self.table_6[tuple_605_605]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_605_605] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_605_605[1]].append(tuple_605_605[0])
                                self.index_948[tuple_605_605[0]].append(tuple_605_605[1])
                            # Program VectorAppend Region
                            vec_610.append((var_605, var_605))
        # Program VectorClear Region
        del vec_603[:]
        vec_index603 = 0
        # Program VectorUnique Region
        vec_613 = list(set(vec_613))
        vec_index613 = 0
        # Program TableJoin Region
        while vec_index613 < len(vec_613):
            var_615 = vec_613[vec_index613]
            vec_index613 += 1
            tuple_614_0_index: int = 0
            tuple_614_0_vec: List[int] = self.index_339[var_615]
            while tuple_614_0_index < len(tuple_614_0_vec):
                tuple_614_0 = tuple_614_0_vec[tuple_614_0_index]
                tuple_614_0_index += 1
                var_616 = tuple_614_0
                if var_615 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_616_615 = (var_616, var_615)
                    prev_state = self.table_109[tuple_616_615]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_616_615] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_616_615[1]].append(tuple_616_615[0])
                        # Program VectorAppend Region
                        vec_617.append(var_615)
                    # Program TransitionState Region
                    tuple_616_615 = (var_616, var_615)
                    prev_state = self.table_22[tuple_616_615]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_616_615] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_616_615[0]].append(tuple_616_615[1])
        # Program VectorClear Region
        del vec_613[:]
        vec_index613 = 0
        # Program VectorUnique Region
        vec_617 = list(set(vec_617))
        vec_index617 = 0
        # Program TableJoin Region
        while vec_index617 < len(vec_617):
            var_619 = vec_617[vec_index617]
            vec_index617 += 1
            tuple_618_0_index: int = 0
            tuple_618_0_vec: List[int] = self.index_345[var_619]
            while tuple_618_0_index < len(tuple_618_0_vec):
                tuple_618_0 = tuple_618_0_vec[tuple_618_0_index]
                tuple_618_0_index += 1
                var_620 = tuple_618_0
                if var_619 in self.index_316:
                    # Program TransitionState Region
                    tuple_620 = var_620
                    prev_state = self.table_13[tuple_620]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_620] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_617[:]
        vec_index617 = 0
        # Induction Fixpoint Loop Region
        while len(vec_610):
            # Program Call Region
            param_612_0 = [vec_610]
            ret = self.proc_139_(param_612_0)
            vec_610 = param_612_0[0]

        vec_index610 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_610[:]
        vec_index610 = 0
        # Program Return Region
        return False
        return False

    def imported_symbol_2(self, vec_622: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index622: int = 0
        vec_625: List[int] = list()
        vec_index625: int = 0
        vec_628: List[int] = list()
        vec_index628: int = 0
        vec_632: List[Tuple[int, int]] = list()
        vec_index632: int = 0
        vec_635: List[int] = list()
        vec_index635: int = 0
        vec_639: List[int] = list()
        vec_index639: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index622 = 0
        while vec_index622 < len(vec_622):
            var_623, var_624 = vec_622[vec_index622]
            vec_index622 += 1
            # Program TransitionState Region
            tuple_623 = var_623
            prev_state = self.table_46[tuple_623]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_46[tuple_623] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_625.append(var_623)
        # Program VectorUnique Region
        vec_625 = list(set(vec_625))
        vec_index625 = 0
        # Program TableJoin Region
        while vec_index625 < len(vec_625):
            var_627 = vec_625[vec_index625]
            vec_index625 += 1
            if var_627 in self.index_157:
                if var_627 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_627 = var_627
                    prev_state = self.table_18[tuple_627]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_627] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_635.append(var_627)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_628: int
                        scan_index_628: int = 0
                        scan_tuple_628_vec: List[int] = self.index_128[var_627]
                        while scan_index_628 < len(scan_tuple_628_vec):
                            scan_tuple_628 = scan_tuple_628_vec[scan_index_628]
                            scan_index_628 += 1
                            vec_628.append(scan_tuple_628)
                        # Program VectorLoop Region
                        vec_index628 = 0
                        while vec_index628 < len(vec_628):
                            var_629 = vec_628[vec_index628]
                            vec_index628 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_627_629 = (var_627, var_629)
                            prev_state = self.table_27[tuple_627_629]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_627_629] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_627, var_629)

                                # Program Call Region
                                ret = self.proc_135_(var_627, var_629)

                        # Program TransitionState Region
                        tuple_627_627 = (var_627, var_627)
                        prev_state = self.table_6[tuple_627_627]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_627_627] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_627_627[1]].append(tuple_627_627[0])
                                self.index_948[tuple_627_627[0]].append(tuple_627_627[1])
                            # Program VectorAppend Region
                            vec_632.append((var_627, var_627))
        # Program VectorClear Region
        del vec_625[:]
        vec_index625 = 0
        # Program VectorUnique Region
        vec_635 = list(set(vec_635))
        vec_index635 = 0
        # Program TableJoin Region
        while vec_index635 < len(vec_635):
            var_637 = vec_635[vec_index635]
            vec_index635 += 1
            tuple_636_0_index: int = 0
            tuple_636_0_vec: List[int] = self.index_339[var_637]
            while tuple_636_0_index < len(tuple_636_0_vec):
                tuple_636_0 = tuple_636_0_vec[tuple_636_0_index]
                tuple_636_0_index += 1
                var_638 = tuple_636_0
                if var_637 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_638_637 = (var_638, var_637)
                    prev_state = self.table_109[tuple_638_637]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_638_637] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_638_637[1]].append(tuple_638_637[0])
                        # Program VectorAppend Region
                        vec_639.append(var_637)
                    # Program TransitionState Region
                    tuple_638_637 = (var_638, var_637)
                    prev_state = self.table_22[tuple_638_637]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_638_637] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_638_637[0]].append(tuple_638_637[1])
        # Program VectorClear Region
        del vec_635[:]
        vec_index635 = 0
        # Program VectorUnique Region
        vec_639 = list(set(vec_639))
        vec_index639 = 0
        # Program TableJoin Region
        while vec_index639 < len(vec_639):
            var_641 = vec_639[vec_index639]
            vec_index639 += 1
            tuple_640_0_index: int = 0
            tuple_640_0_vec: List[int] = self.index_345[var_641]
            while tuple_640_0_index < len(tuple_640_0_vec):
                tuple_640_0 = tuple_640_0_vec[tuple_640_0_index]
                tuple_640_0_index += 1
                var_642 = tuple_640_0
                if var_641 in self.index_316:
                    # Program TransitionState Region
                    tuple_642 = var_642
                    prev_state = self.table_13[tuple_642]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_642] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_639[:]
        vec_index639 = 0
        # Induction Fixpoint Loop Region
        while len(vec_632):
            # Program Call Region
            param_634_0 = [vec_632]
            ret = self.proc_139_(param_634_0)
            vec_632 = param_634_0[0]

        vec_index632 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_632[:]
        vec_index632 = 0
        # Program Return Region
        return False
        return False

    def exported_symbol_2(self, vec_644: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index644: int = 0
        vec_647: List[int] = list()
        vec_index647: int = 0
        vec_650: List[int] = list()
        vec_index650: int = 0
        vec_654: List[Tuple[int, int]] = list()
        vec_index654: int = 0
        vec_657: List[int] = list()
        vec_index657: int = 0
        vec_661: List[int] = list()
        vec_index661: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index644 = 0
        while vec_index644 < len(vec_644):
            var_645, var_646 = vec_644[vec_index644]
            vec_index644 += 1
            # Program TransitionState Region
            tuple_645 = var_645
            prev_state = self.table_48[tuple_645]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_48[tuple_645] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_647.append(var_645)
        # Program VectorUnique Region
        vec_647 = list(set(vec_647))
        vec_index647 = 0
        # Program TableJoin Region
        while vec_index647 < len(vec_647):
            var_649 = vec_647[vec_index647]
            vec_index647 += 1
            if var_649 in self.index_149:
                if var_649 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_649 = var_649
                    prev_state = self.table_18[tuple_649]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_649] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_657.append(var_649)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_650: int
                        scan_index_650: int = 0
                        scan_tuple_650_vec: List[int] = self.index_128[var_649]
                        while scan_index_650 < len(scan_tuple_650_vec):
                            scan_tuple_650 = scan_tuple_650_vec[scan_index_650]
                            scan_index_650 += 1
                            vec_650.append(scan_tuple_650)
                        # Program VectorLoop Region
                        vec_index650 = 0
                        while vec_index650 < len(vec_650):
                            var_651 = vec_650[vec_index650]
                            vec_index650 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_649_651 = (var_649, var_651)
                            prev_state = self.table_27[tuple_649_651]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_649_651] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_649, var_651)

                                # Program Call Region
                                ret = self.proc_135_(var_649, var_651)

                        # Program TransitionState Region
                        tuple_649_649 = (var_649, var_649)
                        prev_state = self.table_6[tuple_649_649]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_649_649] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_649_649[1]].append(tuple_649_649[0])
                                self.index_948[tuple_649_649[0]].append(tuple_649_649[1])
                            # Program VectorAppend Region
                            vec_654.append((var_649, var_649))
        # Program VectorClear Region
        del vec_647[:]
        vec_index647 = 0
        # Program VectorUnique Region
        vec_657 = list(set(vec_657))
        vec_index657 = 0
        # Program TableJoin Region
        while vec_index657 < len(vec_657):
            var_659 = vec_657[vec_index657]
            vec_index657 += 1
            tuple_658_0_index: int = 0
            tuple_658_0_vec: List[int] = self.index_339[var_659]
            while tuple_658_0_index < len(tuple_658_0_vec):
                tuple_658_0 = tuple_658_0_vec[tuple_658_0_index]
                tuple_658_0_index += 1
                var_660 = tuple_658_0
                if var_659 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_660_659 = (var_660, var_659)
                    prev_state = self.table_109[tuple_660_659]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_660_659] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_660_659[1]].append(tuple_660_659[0])
                        # Program VectorAppend Region
                        vec_661.append(var_659)
                    # Program TransitionState Region
                    tuple_660_659 = (var_660, var_659)
                    prev_state = self.table_22[tuple_660_659]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_660_659] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_660_659[0]].append(tuple_660_659[1])
        # Program VectorClear Region
        del vec_657[:]
        vec_index657 = 0
        # Program VectorUnique Region
        vec_661 = list(set(vec_661))
        vec_index661 = 0
        # Program TableJoin Region
        while vec_index661 < len(vec_661):
            var_663 = vec_661[vec_index661]
            vec_index661 += 1
            tuple_662_0_index: int = 0
            tuple_662_0_vec: List[int] = self.index_345[var_663]
            while tuple_662_0_index < len(tuple_662_0_vec):
                tuple_662_0 = tuple_662_0_vec[tuple_662_0_index]
                tuple_662_0_index += 1
                var_664 = tuple_662_0
                if var_663 in self.index_316:
                    # Program TransitionState Region
                    tuple_664 = var_664
                    prev_state = self.table_13[tuple_664]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_664] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_661[:]
        vec_index661 = 0
        # Induction Fixpoint Loop Region
        while len(vec_654):
            # Program Call Region
            param_656_0 = [vec_654]
            ret = self.proc_139_(param_656_0)
            vec_654 = param_656_0[0]

        vec_index654 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_654[:]
        vec_index654 = 0
        # Program Return Region
        return False
        return False

    def local_symbol_2(self, vec_666: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index666: int = 0
        vec_669: List[int] = list()
        vec_index669: int = 0
        vec_672: List[int] = list()
        vec_index672: int = 0
        vec_676: List[Tuple[int, int]] = list()
        vec_index676: int = 0
        vec_679: List[int] = list()
        vec_index679: int = 0
        vec_683: List[int] = list()
        vec_index683: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index666 = 0
        while vec_index666 < len(vec_666):
            var_667, var_668 = vec_666[vec_index666]
            vec_index666 += 1
            # Program TransitionState Region
            tuple_667 = var_667
            prev_state = self.table_50[tuple_667]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_50[tuple_667] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_669.append(var_667)
        # Program VectorUnique Region
        vec_669 = list(set(vec_669))
        vec_index669 = 0
        # Program TableJoin Region
        while vec_index669 < len(vec_669):
            var_671 = vec_669[vec_index669]
            vec_index669 += 1
            if var_671 in self.index_126:
                if var_671 in self.index_127:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_671 = var_671
                    prev_state = self.table_18[tuple_671]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_671] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_679.append(var_671)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_672: int
                        scan_index_672: int = 0
                        scan_tuple_672_vec: List[int] = self.index_128[var_671]
                        while scan_index_672 < len(scan_tuple_672_vec):
                            scan_tuple_672 = scan_tuple_672_vec[scan_index_672]
                            scan_index_672 += 1
                            vec_672.append(scan_tuple_672)
                        # Program VectorLoop Region
                        vec_index672 = 0
                        while vec_index672 < len(vec_672):
                            var_673 = vec_672[vec_index672]
                            vec_index672 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_671_673 = (var_671, var_673)
                            prev_state = self.table_27[tuple_671_673]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_671_673] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_671, var_673)

                                # Program Call Region
                                ret = self.proc_135_(var_671, var_673)

                        # Program TransitionState Region
                        tuple_671_671 = (var_671, var_671)
                        prev_state = self.table_6[tuple_671_671]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_671_671] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_671_671[1]].append(tuple_671_671[0])
                                self.index_948[tuple_671_671[0]].append(tuple_671_671[1])
                            # Program VectorAppend Region
                            vec_676.append((var_671, var_671))
        # Program VectorClear Region
        del vec_669[:]
        vec_index669 = 0
        # Program VectorUnique Region
        vec_679 = list(set(vec_679))
        vec_index679 = 0
        # Program TableJoin Region
        while vec_index679 < len(vec_679):
            var_681 = vec_679[vec_index679]
            vec_index679 += 1
            tuple_680_0_index: int = 0
            tuple_680_0_vec: List[int] = self.index_339[var_681]
            while tuple_680_0_index < len(tuple_680_0_vec):
                tuple_680_0 = tuple_680_0_vec[tuple_680_0_index]
                tuple_680_0_index += 1
                var_682 = tuple_680_0
                if var_681 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_682_681 = (var_682, var_681)
                    prev_state = self.table_109[tuple_682_681]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_682_681] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_682_681[1]].append(tuple_682_681[0])
                        # Program VectorAppend Region
                        vec_683.append(var_681)
                    # Program TransitionState Region
                    tuple_682_681 = (var_682, var_681)
                    prev_state = self.table_22[tuple_682_681]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_682_681] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_682_681[0]].append(tuple_682_681[1])
        # Program VectorClear Region
        del vec_679[:]
        vec_index679 = 0
        # Program VectorUnique Region
        vec_683 = list(set(vec_683))
        vec_index683 = 0
        # Program TableJoin Region
        while vec_index683 < len(vec_683):
            var_685 = vec_683[vec_index683]
            vec_index683 += 1
            tuple_684_0_index: int = 0
            tuple_684_0_vec: List[int] = self.index_345[var_685]
            while tuple_684_0_index < len(tuple_684_0_vec):
                tuple_684_0 = tuple_684_0_vec[tuple_684_0_index]
                tuple_684_0_index += 1
                var_686 = tuple_684_0
                if var_685 in self.index_316:
                    # Program TransitionState Region
                    tuple_686 = var_686
                    prev_state = self.table_13[tuple_686]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_686] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_683[:]
        vec_index683 = 0
        # Induction Fixpoint Loop Region
        while len(vec_676):
            # Program Call Region
            param_678_0 = [vec_676]
            ret = self.proc_139_(param_678_0)
            vec_676 = param_678_0[0]

        vec_index676 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_676[:]
        vec_index676 = 0
        # Program Return Region
        return False
        return False

    def raw_transfer_3(self, vec_688: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index688: int = 0
        vec_692: List[Tuple[int, int]] = list()
        vec_index692: int = 0
        vec_698: List[int] = list()
        vec_index698: int = 0
        vec_705: List[int] = list()
        vec_index705: int = 0
        vec_713: List[int] = list()
        vec_index713: int = 0
        vec_717: List[Tuple[int, int]] = list()
        vec_index717: int = 0
        vec_720: List[int] = list()
        vec_index720: int = 0
        vec_727: List[int] = list()
        vec_index727: int = 0
        vec_731: List[int] = list()
        vec_index731: int = 0
        vec_738: List[int] = list()
        vec_index738: int = 0
        vec_742: List[int] = list()
        vec_index742: int = 0
        vec_749: List[int] = list()
        vec_index749: int = 0
        vec_753: List[int] = list()
        vec_index753: int = 0
        vec_756: List[int] = list()
        vec_index756: int = 0
        vec_760: List[int] = list()
        vec_index760: int = 0
        vec_764: List[int] = list()
        vec_index764: int = 0
        vec_768: List[int] = list()
        vec_index768: int = 0
        vec_772: List[int] = list()
        vec_index772: int = 0
        vec_776: List[int] = list()
        vec_index776: int = 0
        vec_780: List[int] = list()
        vec_index780: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index688 = 0
        while vec_index688 < len(vec_688):
            var_689, var_690, var_691 = vec_688[vec_index688]
            vec_index688 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if var_691 != self.var_0:
                # Program TupleCompare Region
                if var_691 != self.var_3:
                    # Program TransitionState Region
                    var_691 = self._resolve_edgetype(var_691)
                    tuple_691_689_690 = (var_691, var_689, var_690)
                    prev_state = self.table_67[tuple_691_689_690]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_67[tuple_691_689_690] = 1 | 4
                        if not present_bit:
                            self.index_216[tuple_691_689_690[2]].append((tuple_691_689_690[0], tuple_691_689_690[1]))
                        # Program VectorAppend Region
                        vec_705.append(var_690)
            # Program TupleCompare Region
            if self.var_0 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_74[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_74[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_701[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_3 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_77[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_77[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_702[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_0 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_74[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_74[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_701[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_3 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_77[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_77[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_702[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_0 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_74[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_74[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_701[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_3 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_77[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_77[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_702[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_0 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_74[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_74[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_701[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_3 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_77[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_77[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_702[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_0 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_74[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_74[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_701[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_3 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_77[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_77[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_702[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_0 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_74[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_74[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_701[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_3 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_77[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_77[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_702[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_0 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_74[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_74[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_701[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
            # Program TupleCompare Region
            if self.var_3 == var_691:
                # Program TransitionState Region
                tuple_689_690 = (var_689, var_690)
                prev_state = self.table_77[tuple_689_690]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_77[tuple_689_690] = 1 | 4
                    if not present_bit:
                        self.index_702[tuple_689_690[0]].append(tuple_689_690[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_698.append(var_689)
                    # Program VectorAppend Region
                    vec_692.append((var_689, var_690))
        # Program VectorUnique Region
        vec_692 = list(set(vec_692))
        vec_index692 = 0
        # Program TableJoin Region
        while vec_index692 < len(vec_692):
            var_694, var_695 = vec_692[vec_index692]
            vec_index692 += 1
            if (var_694, var_695) in self.index_696:
                if (var_694, var_695) in self.index_697:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_694_695 = (var_694, var_695)
                    prev_state = self.table_103[tuple_694_695]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_103[tuple_694_695] = 1 | 4
                        if not present_bit:
                            self.index_250[tuple_694_695[1]].append(tuple_694_695[0])
                        # Program VectorAppend Region
                        vec_720.append(var_695)
        # Program VectorClear Region
        del vec_692[:]
        vec_index692 = 0
        # Program VectorUnique Region
        vec_698 = list(set(vec_698))
        vec_index698 = 0
        # Program TableJoin Region
        while vec_index698 < len(vec_698):
            var_700 = vec_698[vec_index698]
            vec_index698 += 1
            tuple_699_0_index: int = 0
            tuple_699_0_vec: List[int] = self.index_701[var_700]
            while tuple_699_0_index < len(tuple_699_0_vec):
                tuple_699_0 = tuple_699_0_vec[tuple_699_0_index]
                tuple_699_0_index += 1
                var_703 = tuple_699_0
                tuple_699_1_index: int = 0
                tuple_699_1_vec: List[int] = self.index_702[var_700]
                while tuple_699_1_index < len(tuple_699_1_vec):
                    tuple_699_1 = tuple_699_1_vec[tuple_699_1_index]
                    tuple_699_1_index += 1
                    var_704 = tuple_699_1
                    # Program TupleCompare Region
                    if var_703 != var_704:
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_703_700 = (var_703, var_700)
                        prev_state = self.table_71[tuple_703_700]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_71[tuple_703_700] = 1 | 4
                            if not present_bit:
                                self.index_280[tuple_703_700[0]].append(tuple_703_700[1])
                            # Program VectorAppend Region
                            vec_742.append(var_703)
                        # Program TransitionState Region
                        tuple_704_700 = (var_704, var_700)
                        prev_state = self.table_80[tuple_704_700]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_80[tuple_704_700] = 1 | 4
                            if not present_bit:
                                self.index_268[tuple_704_700[0]].append(tuple_704_700[1])
                            # Program VectorAppend Region
                            vec_731.append(var_704)
        # Program VectorClear Region
        del vec_698[:]
        vec_index698 = 0
        # Program VectorUnique Region
        vec_705 = list(set(vec_705))
        vec_index705 = 0
        # Program TableJoin Region
        while vec_index705 < len(vec_705):
            var_707 = vec_705[vec_index705]
            vec_index705 += 1
            tuple_706_0_index: int = 0
            tuple_706_0_vec: List[Tuple[int, int]] = self.index_216[var_707]
            while tuple_706_0_index < len(tuple_706_0_vec):
                tuple_706_0 = tuple_706_0_vec[tuple_706_0_index]
                tuple_706_0_index += 1
                var_708 = tuple_706_0[0]
                var_709 = tuple_706_0[1]
                if var_707 in self.index_217:
                    # Program TransitionState Region
                    var_708 = self._resolve_edgetype(var_708)
                    tuple_709_707_708 = (var_709, var_707, var_708)
                    prev_state = self.table_9[tuple_709_707_708]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_709_707_708] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_709_707_708[0], tuple_709_707_708[1])].append(tuple_709_707_708[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_707_709 = (var_707, var_709)
                        prev_state = self.table_27[tuple_707_709]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_707_709] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_707_709[0]].append(tuple_707_709[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_707)
                        if not ret:
                            # Program TransitionState Region
                            tuple_707_709 = (var_707, var_709)
                            prev_state = self.table_27[tuple_707_709]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_707_709] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_707_709[0]].append(tuple_707_709[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_709, var_707)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_709_707 = (var_709, var_707)
                                    prev_state = self.table_64[tuple_709_707]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_709_707] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_709_707[0]].append(tuple_709_707[1])
                                            self.index_970[tuple_709_707[1]].append(tuple_709_707[0])
                                        # Program VectorAppend Region
                                        vec_780.append(var_709)
                                # Program TransitionState Region
                                tuple_709_707 = (var_709, var_707)
                                prev_state = self.table_15[tuple_709_707]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_709_707] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_709_707[0]].append(tuple_709_707[1])
                        # Program TransitionState Region
                        tuple_709_707 = (var_709, var_707)
                        prev_state = self.table_106[tuple_709_707]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_709_707] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_709_707[1]].append(tuple_709_707[0])
                            # Program VectorAppend Region
                            vec_772.append(var_707)
                        # Program TransitionState Region
                        tuple_707 = var_707
                        prev_state = self.table_54[tuple_707]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_707] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_753.append(var_707)
                        # Program TupleCompare Region
                        if self.var_0 == var_708:
                            # Program TransitionState Region
                            tuple_707 = var_707
                            prev_state = self.table_18[tuple_707]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_707] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_772.append(var_707)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_713: int
                                scan_index_713: int = 0
                                scan_tuple_713_vec: List[int] = self.index_128[var_707]
                                while scan_index_713 < len(scan_tuple_713_vec):
                                    scan_tuple_713 = scan_tuple_713_vec[scan_index_713]
                                    scan_index_713 += 1
                                    vec_713.append(scan_tuple_713)
                                # Program VectorLoop Region
                                vec_index713 = 0
                                while vec_index713 < len(vec_713):
                                    var_714 = vec_713[vec_index713]
                                    vec_index713 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_707_714 = (var_707, var_714)
                                    prev_state = self.table_27[tuple_707_714]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_707_714] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_707, var_714)

                                        # Program Call Region
                                        ret = self.proc_135_(var_707, var_714)

                                # Program TransitionState Region
                                tuple_707_707 = (var_707, var_707)
                                prev_state = self.table_6[tuple_707_707]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_707_707] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_707_707[1]].append(tuple_707_707[0])
                                        self.index_948[tuple_707_707[0]].append(tuple_707_707[1])
                                    # Program VectorAppend Region
                                    vec_717.append((var_707, var_707))
                        # Program TupleCompare Region
                        if self.var_2 == var_708:
                            # Program TransitionState Region
                            tuple_709_707 = (var_709, var_707)
                            prev_state = self.table_58[tuple_709_707]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_709_707] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_709_707[0]].append(tuple_709_707[1])
                                # Program VectorAppend Region
                                vec_760.append(var_709)
        # Program VectorClear Region
        del vec_705[:]
        vec_index705 = 0
        # Program VectorUnique Region
        vec_720 = list(set(vec_720))
        vec_index720 = 0
        # Program TableJoin Region
        while vec_index720 < len(vec_720):
            var_722 = vec_720[vec_index720]
            vec_index720 += 1
            if var_722 in self.index_217:
                tuple_721_1_index: int = 0
                tuple_721_1_vec: List[int] = self.index_250[var_722]
                while tuple_721_1_index < len(tuple_721_1_vec):
                    tuple_721_1 = tuple_721_1_vec[tuple_721_1_index]
                    tuple_721_1_index += 1
                    var_723 = tuple_721_1
                    # Program TransitionState Region
                    tuple_723_722_5 = (var_723, var_722, self.var_5)
                    prev_state = self.table_9[tuple_723_722_5]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_723_722_5] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_723_722_5[0], tuple_723_722_5[1])].append(tuple_723_722_5[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_722_723 = (var_722, var_723)
                        prev_state = self.table_27[tuple_722_723]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_722_723] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_722_723[0]].append(tuple_722_723[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_722)
                        if not ret:
                            # Program TransitionState Region
                            tuple_722_723 = (var_722, var_723)
                            prev_state = self.table_27[tuple_722_723]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_722_723] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_722_723[0]].append(tuple_722_723[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_723, var_722)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_723_722 = (var_723, var_722)
                                    prev_state = self.table_64[tuple_723_722]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_723_722] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_723_722[0]].append(tuple_723_722[1])
                                            self.index_970[tuple_723_722[1]].append(tuple_723_722[0])
                                        # Program VectorAppend Region
                                        vec_780.append(var_723)
                                # Program TransitionState Region
                                tuple_723_722 = (var_723, var_722)
                                prev_state = self.table_15[tuple_723_722]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_723_722] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_723_722[0]].append(tuple_723_722[1])
                        # Program TransitionState Region
                        tuple_723_722 = (var_723, var_722)
                        prev_state = self.table_106[tuple_723_722]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_723_722] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_723_722[1]].append(tuple_723_722[0])
                            # Program VectorAppend Region
                            vec_772.append(var_722)
                        # Program TransitionState Region
                        tuple_722 = var_722
                        prev_state = self.table_54[tuple_722]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_722] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_753.append(var_722)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_5:
                            # Program TransitionState Region
                            tuple_722 = var_722
                            prev_state = self.table_18[tuple_722]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_722] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_772.append(var_722)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_727: int
                                scan_index_727: int = 0
                                scan_tuple_727_vec: List[int] = self.index_128[var_722]
                                while scan_index_727 < len(scan_tuple_727_vec):
                                    scan_tuple_727 = scan_tuple_727_vec[scan_index_727]
                                    scan_index_727 += 1
                                    vec_727.append(scan_tuple_727)
                                # Program VectorLoop Region
                                vec_index727 = 0
                                while vec_index727 < len(vec_727):
                                    var_728 = vec_727[vec_index727]
                                    vec_index727 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_722_728 = (var_722, var_728)
                                    prev_state = self.table_27[tuple_722_728]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_722_728] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_722, var_728)

                                        # Program Call Region
                                        ret = self.proc_135_(var_722, var_728)

                                # Program TransitionState Region
                                tuple_722_722 = (var_722, var_722)
                                prev_state = self.table_6[tuple_722_722]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_722_722] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_722_722[1]].append(tuple_722_722[0])
                                        self.index_948[tuple_722_722[0]].append(tuple_722_722[1])
                                    # Program VectorAppend Region
                                    vec_717.append((var_722, var_722))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_5:
                            # Program TransitionState Region
                            tuple_723_722 = (var_723, var_722)
                            prev_state = self.table_58[tuple_723_722]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_723_722] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_723_722[0]].append(tuple_723_722[1])
                                # Program VectorAppend Region
                                vec_760.append(var_723)
        # Program VectorClear Region
        del vec_720[:]
        vec_index720 = 0
        # Program VectorUnique Region
        vec_731 = list(set(vec_731))
        vec_index731 = 0
        # Program TableJoin Region
        while vec_index731 < len(vec_731):
            var_733 = vec_731[vec_index731]
            vec_index731 += 1
            if var_733 in self.index_217:
                tuple_732_1_index: int = 0
                tuple_732_1_vec: List[int] = self.index_268[var_733]
                while tuple_732_1_index < len(tuple_732_1_vec):
                    tuple_732_1 = tuple_732_1_vec[tuple_732_1_index]
                    tuple_732_1_index += 1
                    var_734 = tuple_732_1
                    # Program TransitionState Region
                    tuple_734_733_3 = (var_734, var_733, self.var_3)
                    prev_state = self.table_9[tuple_734_733_3]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_734_733_3] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_734_733_3[0], tuple_734_733_3[1])].append(tuple_734_733_3[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_733_734 = (var_733, var_734)
                        prev_state = self.table_27[tuple_733_734]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_733_734] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_733_734[0]].append(tuple_733_734[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_733)
                        if not ret:
                            # Program TransitionState Region
                            tuple_733_734 = (var_733, var_734)
                            prev_state = self.table_27[tuple_733_734]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_733_734] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_733_734[0]].append(tuple_733_734[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_734, var_733)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_734_733 = (var_734, var_733)
                                    prev_state = self.table_64[tuple_734_733]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_734_733] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_734_733[0]].append(tuple_734_733[1])
                                            self.index_970[tuple_734_733[1]].append(tuple_734_733[0])
                                        # Program VectorAppend Region
                                        vec_780.append(var_734)
                                # Program TransitionState Region
                                tuple_734_733 = (var_734, var_733)
                                prev_state = self.table_15[tuple_734_733]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_734_733] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_734_733[0]].append(tuple_734_733[1])
                        # Program TransitionState Region
                        tuple_734_733 = (var_734, var_733)
                        prev_state = self.table_106[tuple_734_733]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_734_733] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_734_733[1]].append(tuple_734_733[0])
                            # Program VectorAppend Region
                            vec_772.append(var_733)
                        # Program TransitionState Region
                        tuple_733 = var_733
                        prev_state = self.table_54[tuple_733]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_733] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_753.append(var_733)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_3:
                            # Program TransitionState Region
                            tuple_733 = var_733
                            prev_state = self.table_18[tuple_733]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_733] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_772.append(var_733)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_738: int
                                scan_index_738: int = 0
                                scan_tuple_738_vec: List[int] = self.index_128[var_733]
                                while scan_index_738 < len(scan_tuple_738_vec):
                                    scan_tuple_738 = scan_tuple_738_vec[scan_index_738]
                                    scan_index_738 += 1
                                    vec_738.append(scan_tuple_738)
                                # Program VectorLoop Region
                                vec_index738 = 0
                                while vec_index738 < len(vec_738):
                                    var_739 = vec_738[vec_index738]
                                    vec_index738 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_733_739 = (var_733, var_739)
                                    prev_state = self.table_27[tuple_733_739]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_733_739] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_733, var_739)

                                        # Program Call Region
                                        ret = self.proc_135_(var_733, var_739)

                                # Program TransitionState Region
                                tuple_733_733 = (var_733, var_733)
                                prev_state = self.table_6[tuple_733_733]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_733_733] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_733_733[1]].append(tuple_733_733[0])
                                        self.index_948[tuple_733_733[0]].append(tuple_733_733[1])
                                    # Program VectorAppend Region
                                    vec_717.append((var_733, var_733))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_3:
                            # Program TransitionState Region
                            tuple_734_733 = (var_734, var_733)
                            prev_state = self.table_58[tuple_734_733]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_734_733] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_734_733[0]].append(tuple_734_733[1])
                                # Program VectorAppend Region
                                vec_760.append(var_734)
        # Program VectorClear Region
        del vec_731[:]
        vec_index731 = 0
        # Program VectorUnique Region
        vec_742 = list(set(vec_742))
        vec_index742 = 0
        # Program TableJoin Region
        while vec_index742 < len(vec_742):
            var_744 = vec_742[vec_index742]
            vec_index742 += 1
            if var_744 in self.index_217:
                tuple_743_1_index: int = 0
                tuple_743_1_vec: List[int] = self.index_280[var_744]
                while tuple_743_1_index < len(tuple_743_1_vec):
                    tuple_743_1 = tuple_743_1_vec[tuple_743_1_index]
                    tuple_743_1_index += 1
                    var_745 = tuple_743_1
                    # Program TransitionState Region
                    tuple_745_744_0 = (var_745, var_744, self.var_0)
                    prev_state = self.table_9[tuple_745_744_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_745_744_0] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_745_744_0[0], tuple_745_744_0[1])].append(tuple_745_744_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_744_745 = (var_744, var_745)
                        prev_state = self.table_27[tuple_744_745]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_744_745] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_744_745[0]].append(tuple_744_745[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_744)
                        if not ret:
                            # Program TransitionState Region
                            tuple_744_745 = (var_744, var_745)
                            prev_state = self.table_27[tuple_744_745]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_744_745] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_744_745[0]].append(tuple_744_745[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_745, var_744)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_745_744 = (var_745, var_744)
                                    prev_state = self.table_64[tuple_745_744]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_745_744] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_745_744[0]].append(tuple_745_744[1])
                                            self.index_970[tuple_745_744[1]].append(tuple_745_744[0])
                                        # Program VectorAppend Region
                                        vec_780.append(var_745)
                                # Program TransitionState Region
                                tuple_745_744 = (var_745, var_744)
                                prev_state = self.table_15[tuple_745_744]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_745_744] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_745_744[0]].append(tuple_745_744[1])
                        # Program TransitionState Region
                        tuple_745_744 = (var_745, var_744)
                        prev_state = self.table_106[tuple_745_744]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_745_744] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_745_744[1]].append(tuple_745_744[0])
                            # Program VectorAppend Region
                            vec_772.append(var_744)
                        # Program TransitionState Region
                        tuple_744 = var_744
                        prev_state = self.table_54[tuple_744]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_744] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_753.append(var_744)
                        # Program TransitionState Region
                        tuple_744 = var_744
                        prev_state = self.table_18[tuple_744]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_744] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_772.append(var_744)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_749: int
                            scan_index_749: int = 0
                            scan_tuple_749_vec: List[int] = self.index_128[var_744]
                            while scan_index_749 < len(scan_tuple_749_vec):
                                scan_tuple_749 = scan_tuple_749_vec[scan_index_749]
                                scan_index_749 += 1
                                vec_749.append(scan_tuple_749)
                            # Program VectorLoop Region
                            vec_index749 = 0
                            while vec_index749 < len(vec_749):
                                var_750 = vec_749[vec_index749]
                                vec_index749 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_744_750 = (var_744, var_750)
                                prev_state = self.table_27[tuple_744_750]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_744_750] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_131_(var_744, var_750)

                                    # Program Call Region
                                    ret = self.proc_135_(var_744, var_750)

                            # Program TransitionState Region
                            tuple_744_744 = (var_744, var_744)
                            prev_state = self.table_6[tuple_744_744]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_744_744] = 1 | 4
                                if not present_bit:
                                    self.index_350[tuple_744_744[1]].append(tuple_744_744[0])
                                    self.index_948[tuple_744_744[0]].append(tuple_744_744[1])
                                # Program VectorAppend Region
                                vec_717.append((var_744, var_744))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_745_744 = (var_745, var_744)
                            prev_state = self.table_58[tuple_745_744]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_745_744] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_745_744[0]].append(tuple_745_744[1])
                                # Program VectorAppend Region
                                vec_760.append(var_745)
        # Program VectorClear Region
        del vec_742[:]
        vec_index742 = 0
        # Program VectorUnique Region
        vec_753 = list(set(vec_753))
        vec_index753 = 0
        # Program TableJoin Region
        while vec_index753 < len(vec_753):
            var_755 = vec_753[vec_index753]
            vec_index753 += 1
            if var_755 in self.index_316:
                if var_755 in self.index_317:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_755 = var_755
                    prev_state = self.table_18[tuple_755]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_755] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_772.append(var_755)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_756: int
                        scan_index_756: int = 0
                        scan_tuple_756_vec: List[int] = self.index_128[var_755]
                        while scan_index_756 < len(scan_tuple_756_vec):
                            scan_tuple_756 = scan_tuple_756_vec[scan_index_756]
                            scan_index_756 += 1
                            vec_756.append(scan_tuple_756)
                        # Program VectorLoop Region
                        vec_index756 = 0
                        while vec_index756 < len(vec_756):
                            var_757 = vec_756[vec_index756]
                            vec_index756 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_755_757 = (var_755, var_757)
                            prev_state = self.table_27[tuple_755_757]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_755_757] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_755, var_757)

                                # Program Call Region
                                ret = self.proc_135_(var_755, var_757)

                        # Program TransitionState Region
                        tuple_755_755 = (var_755, var_755)
                        prev_state = self.table_6[tuple_755_755]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_755_755] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_755_755[1]].append(tuple_755_755[0])
                                self.index_948[tuple_755_755[0]].append(tuple_755_755[1])
                            # Program VectorAppend Region
                            vec_717.append((var_755, var_755))
        # Program VectorClear Region
        del vec_753[:]
        vec_index753 = 0
        # Program VectorUnique Region
        vec_760 = list(set(vec_760))
        vec_index760 = 0
        # Program TableJoin Region
        while vec_index760 < len(vec_760):
            var_762 = vec_760[vec_index760]
            vec_index760 += 1
            if var_762 in self.index_211:
                tuple_761_1_index: int = 0
                tuple_761_1_vec: List[int] = self.index_325[var_762]
                while tuple_761_1_index < len(tuple_761_1_vec):
                    tuple_761_1 = tuple_761_1_vec[tuple_761_1_index]
                    tuple_761_1_index += 1
                    var_763 = tuple_761_1
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_762_763 = (var_762, var_763)
                    prev_state = self.table_61[tuple_762_763]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_61[tuple_762_763] = 1 | 4
                        if not present_bit:
                            self.index_330[tuple_762_763[1]].append(tuple_762_763[0])
                        # Program VectorAppend Region
                        vec_764.append(var_763)
        # Program VectorClear Region
        del vec_760[:]
        vec_index760 = 0
        # Program VectorUnique Region
        vec_764 = list(set(vec_764))
        vec_index764 = 0
        # Program TableJoin Region
        while vec_index764 < len(vec_764):
            var_766 = vec_764[vec_index764]
            vec_index764 += 1
            if var_766 in self.index_316:
                tuple_765_1_index: int = 0
                tuple_765_1_vec: List[int] = self.index_330[var_766]
                while tuple_765_1_index < len(tuple_765_1_vec):
                    tuple_765_1 = tuple_765_1_vec[tuple_765_1_index]
                    tuple_765_1_index += 1
                    var_767 = tuple_765_1
                    # Program TransitionState Region
                    tuple_767 = var_767
                    prev_state = self.table_18[tuple_767]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_767] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_772.append(var_767)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_768: int
                        scan_index_768: int = 0
                        scan_tuple_768_vec: List[int] = self.index_128[var_767]
                        while scan_index_768 < len(scan_tuple_768_vec):
                            scan_tuple_768 = scan_tuple_768_vec[scan_index_768]
                            scan_index_768 += 1
                            vec_768.append(scan_tuple_768)
                        # Program VectorLoop Region
                        vec_index768 = 0
                        while vec_index768 < len(vec_768):
                            var_769 = vec_768[vec_index768]
                            vec_index768 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_767_769 = (var_767, var_769)
                            prev_state = self.table_27[tuple_767_769]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_767_769] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_767, var_769)

                                # Program Call Region
                                ret = self.proc_135_(var_767, var_769)

                        # Program TransitionState Region
                        tuple_767_767 = (var_767, var_767)
                        prev_state = self.table_6[tuple_767_767]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_767_767] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_767_767[1]].append(tuple_767_767[0])
                                self.index_948[tuple_767_767[0]].append(tuple_767_767[1])
                            # Program VectorAppend Region
                            vec_717.append((var_767, var_767))
        # Program VectorClear Region
        del vec_764[:]
        vec_index764 = 0
        # Program VectorUnique Region
        vec_772 = list(set(vec_772))
        vec_index772 = 0
        # Program TableJoin Region
        while vec_index772 < len(vec_772):
            var_774 = vec_772[vec_index772]
            vec_index772 += 1
            tuple_773_0_index: int = 0
            tuple_773_0_vec: List[int] = self.index_339[var_774]
            while tuple_773_0_index < len(tuple_773_0_vec):
                tuple_773_0 = tuple_773_0_vec[tuple_773_0_index]
                tuple_773_0_index += 1
                var_775 = tuple_773_0
                if var_774 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_775_774 = (var_775, var_774)
                    prev_state = self.table_109[tuple_775_774]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_775_774] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_775_774[1]].append(tuple_775_774[0])
                        # Program VectorAppend Region
                        vec_776.append(var_774)
                    # Program TransitionState Region
                    tuple_775_774 = (var_775, var_774)
                    prev_state = self.table_22[tuple_775_774]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_775_774] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_775_774[0]].append(tuple_775_774[1])
        # Program VectorClear Region
        del vec_772[:]
        vec_index772 = 0
        # Program VectorUnique Region
        vec_776 = list(set(vec_776))
        vec_index776 = 0
        # Program TableJoin Region
        while vec_index776 < len(vec_776):
            var_778 = vec_776[vec_index776]
            vec_index776 += 1
            tuple_777_0_index: int = 0
            tuple_777_0_vec: List[int] = self.index_345[var_778]
            while tuple_777_0_index < len(tuple_777_0_vec):
                tuple_777_0 = tuple_777_0_vec[tuple_777_0_index]
                tuple_777_0_index += 1
                var_779 = tuple_777_0
                if var_778 in self.index_316:
                    # Program TransitionState Region
                    tuple_779 = var_779
                    prev_state = self.table_13[tuple_779]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_779] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_776[:]
        vec_index776 = 0
        # Program VectorUnique Region
        vec_780 = list(set(vec_780))
        vec_index780 = 0
        # Program TableJoin Region
        while vec_index780 < len(vec_780):
            var_782 = vec_780[vec_index780]
            vec_index780 += 1
            tuple_781_0_index: int = 0
            tuple_781_0_vec: List[int] = self.index_350[var_782]
            while tuple_781_0_index < len(tuple_781_0_vec):
                tuple_781_0 = tuple_781_0_vec[tuple_781_0_index]
                tuple_781_0_index += 1
                var_783 = tuple_781_0
                tuple_781_1_index: int = 0
                tuple_781_1_vec: List[int] = self.index_351[var_782]
                while tuple_781_1_index < len(tuple_781_1_vec):
                    tuple_781_1 = tuple_781_1_vec[tuple_781_1_index]
                    tuple_781_1_index += 1
                    var_784 = tuple_781_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_354_(var_783, var_782)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_224_(var_782, var_784)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_359_(var_783, var_784)
                            if not ret:
                                # Program TransitionState Region
                                tuple_783_784 = (var_783, var_784)
                                prev_state = self.table_6[tuple_783_784]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_783_784] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_783_784[1]].append(tuple_783_784[0])
                                        self.index_948[tuple_783_784[0]].append(tuple_783_784[1])
                                    # Program VectorAppend Region
                                    vec_717.append((var_783, var_784))
        # Program VectorClear Region
        del vec_780[:]
        vec_index780 = 0
        # Induction Fixpoint Loop Region
        while len(vec_717):
            # Program Call Region
            param_719_0 = [vec_717]
            ret = self.proc_139_(param_719_0)
            vec_717 = param_719_0[0]

        vec_index717 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_717[:]
        vec_index717 = 0
        # Program Return Region
        return False
        return False

    def address_operand_2(self, vec_789: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index789: int = 0
        vec_792: List[int] = list()
        vec_index792: int = 0
        vec_796: List[int] = list()
        vec_index796: int = 0
        vec_800: List[int] = list()
        vec_index800: int = 0
        vec_805: List[int] = list()
        vec_index805: int = 0
        vec_810: List[int] = list()
        vec_index810: int = 0
        vec_817: List[int] = list()
        vec_index817: int = 0
        vec_821: List[Tuple[int, int]] = list()
        vec_index821: int = 0
        vec_824: List[int] = list()
        vec_index824: int = 0
        vec_831: List[int] = list()
        vec_index831: int = 0
        vec_835: List[int] = list()
        vec_index835: int = 0
        vec_838: List[int] = list()
        vec_index838: int = 0
        vec_842: List[int] = list()
        vec_index842: int = 0
        vec_846: List[int] = list()
        vec_index846: int = 0
        vec_850: List[int] = list()
        vec_index850: int = 0
        vec_854: List[int] = list()
        vec_index854: int = 0
        vec_858: List[int] = list()
        vec_index858: int = 0
        vec_862: List[int] = list()
        vec_index862: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index789 = 0
        while vec_index789 < len(vec_789):
            var_790, var_791 = vec_789[vec_index789]
            vec_index789 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_790_791 = (var_790, var_791)
            prev_state = self.table_83[tuple_790_791]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_83[tuple_790_791] = 1 | 4
                if not present_bit:
                    self.index_206[tuple_790_791[0]].append(tuple_790_791[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_796.append(var_790)
                # Program VectorAppend Region
                vec_792.append(var_790)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_790_791 = (var_790, var_791)
            prev_state = self.table_83[tuple_790_791]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_83[tuple_790_791] = 1 | 4
                if not present_bit:
                    self.index_206[tuple_790_791[0]].append(tuple_790_791[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_796.append(var_790)
                # Program VectorAppend Region
                vec_792.append(var_790)
        # Program VectorUnique Region
        vec_792 = list(set(vec_792))
        vec_index792 = 0
        # Program TableJoin Region
        while vec_index792 < len(vec_792):
            var_794 = vec_792[vec_index792]
            vec_index792 += 1
            if var_794 in self.index_205:
                tuple_793_1_index: int = 0
                tuple_793_1_vec: List[int] = self.index_206[var_794]
                while tuple_793_1_index < len(tuple_793_1_vec):
                    tuple_793_1 = tuple_793_1_vec[tuple_793_1_index]
                    tuple_793_1_index += 1
                    var_795 = tuple_793_1
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_794_795 = (var_794, var_795)
                    prev_state = self.table_97[tuple_794_795]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_794_795] = 1 | 4
                        if not present_bit:
                            self.index_244[tuple_794_795[1]].append(tuple_794_795[0])
                        # Program VectorAppend Region
                        vec_800.append(var_795)
        # Program VectorClear Region
        del vec_792[:]
        vec_index792 = 0
        # Program VectorUnique Region
        vec_796 = list(set(vec_796))
        vec_index796 = 0
        # Program TableJoin Region
        while vec_index796 < len(vec_796):
            var_798 = vec_796[vec_index796]
            vec_index796 += 1
            if var_798 in self.index_211:
                tuple_797_1_index: int = 0
                tuple_797_1_vec: List[int] = self.index_206[var_798]
                while tuple_797_1_index < len(tuple_797_1_vec):
                    tuple_797_1 = tuple_797_1_vec[tuple_797_1_index]
                    tuple_797_1_index += 1
                    var_799 = tuple_797_1
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_798_799 = (var_798, var_799)
                    prev_state = self.table_89[tuple_798_799]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_89[tuple_798_799] = 1 | 4
                        if not present_bit:
                            self.index_262[tuple_798_799[1]].append(tuple_798_799[0])
                        # Program VectorAppend Region
                        vec_805.append(var_799)
        # Program VectorClear Region
        del vec_796[:]
        vec_index796 = 0
        # Program VectorUnique Region
        vec_800 = list(set(vec_800))
        vec_index800 = 0
        # Program TableJoin Region
        while vec_index800 < len(vec_800):
            var_802 = vec_800[vec_index800]
            vec_index800 += 1
            tuple_801_0_index: int = 0
            tuple_801_0_vec: List[int] = self.index_243[var_802]
            while tuple_801_0_index < len(tuple_801_0_vec):
                tuple_801_0 = tuple_801_0_vec[tuple_801_0_index]
                tuple_801_0_index += 1
                var_803 = tuple_801_0
                tuple_801_1_index: int = 0
                tuple_801_1_vec: List[int] = self.index_244[var_802]
                while tuple_801_1_index < len(tuple_801_1_vec):
                    tuple_801_1 = tuple_801_1_vec[tuple_801_1_index]
                    tuple_801_1_index += 1
                    var_804 = tuple_801_1
                    # Program TransitionState Region
                    tuple_803_804 = (var_803, var_804)
                    prev_state = self.table_100[tuple_803_804]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_100[tuple_803_804] = 1 | 4
                        if not present_bit:
                            self.index_292[tuple_803_804[0]].append(tuple_803_804[1])
                        # Program VectorAppend Region
                        vec_810.append(var_803)
        # Program VectorClear Region
        del vec_800[:]
        vec_index800 = 0
        # Program VectorUnique Region
        vec_805 = list(set(vec_805))
        vec_index805 = 0
        # Program TableJoin Region
        while vec_index805 < len(vec_805):
            var_807 = vec_805[vec_index805]
            vec_index805 += 1
            tuple_806_0_index: int = 0
            tuple_806_0_vec: List[int] = self.index_243[var_807]
            while tuple_806_0_index < len(tuple_806_0_vec):
                tuple_806_0 = tuple_806_0_vec[tuple_806_0_index]
                tuple_806_0_index += 1
                var_808 = tuple_806_0
                tuple_806_1_index: int = 0
                tuple_806_1_vec: List[int] = self.index_262[var_807]
                while tuple_806_1_index < len(tuple_806_1_vec):
                    tuple_806_1 = tuple_806_1_vec[tuple_806_1_index]
                    tuple_806_1_index += 1
                    var_809 = tuple_806_1
                    # Program TransitionState Region
                    tuple_808_809 = (var_808, var_809)
                    prev_state = self.table_92[tuple_808_809]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_92[tuple_808_809] = 1 | 4
                        if not present_bit:
                            self.index_304[tuple_808_809[0]].append(tuple_808_809[1])
                        # Program VectorAppend Region
                        vec_824.append(var_808)
        # Program VectorClear Region
        del vec_805[:]
        vec_index805 = 0
        # Program VectorUnique Region
        vec_810 = list(set(vec_810))
        vec_index810 = 0
        # Program TableJoin Region
        while vec_index810 < len(vec_810):
            var_812 = vec_810[vec_index810]
            vec_index810 += 1
            if var_812 in self.index_217:
                tuple_811_1_index: int = 0
                tuple_811_1_vec: List[int] = self.index_292[var_812]
                while tuple_811_1_index < len(tuple_811_1_vec):
                    tuple_811_1 = tuple_811_1_vec[tuple_811_1_index]
                    tuple_811_1_index += 1
                    var_813 = tuple_811_1
                    # Program TransitionState Region
                    tuple_813_812_0 = (var_813, var_812, self.var_0)
                    prev_state = self.table_9[tuple_813_812_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_813_812_0] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_813_812_0[0], tuple_813_812_0[1])].append(tuple_813_812_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_812_813 = (var_812, var_813)
                        prev_state = self.table_27[tuple_812_813]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_812_813] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_812_813[0]].append(tuple_812_813[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_812)
                        if not ret:
                            # Program TransitionState Region
                            tuple_812_813 = (var_812, var_813)
                            prev_state = self.table_27[tuple_812_813]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_812_813] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_812_813[0]].append(tuple_812_813[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_813, var_812)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_813_812 = (var_813, var_812)
                                    prev_state = self.table_64[tuple_813_812]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_813_812] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_813_812[0]].append(tuple_813_812[1])
                                            self.index_970[tuple_813_812[1]].append(tuple_813_812[0])
                                        # Program VectorAppend Region
                                        vec_862.append(var_813)
                                # Program TransitionState Region
                                tuple_813_812 = (var_813, var_812)
                                prev_state = self.table_15[tuple_813_812]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_813_812] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_813_812[0]].append(tuple_813_812[1])
                        # Program TransitionState Region
                        tuple_813_812 = (var_813, var_812)
                        prev_state = self.table_106[tuple_813_812]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_813_812] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_813_812[1]].append(tuple_813_812[0])
                            # Program VectorAppend Region
                            vec_854.append(var_812)
                        # Program TransitionState Region
                        tuple_812 = var_812
                        prev_state = self.table_54[tuple_812]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_812] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_835.append(var_812)
                        # Program TransitionState Region
                        tuple_812 = var_812
                        prev_state = self.table_18[tuple_812]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_812] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_854.append(var_812)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_817: int
                            scan_index_817: int = 0
                            scan_tuple_817_vec: List[int] = self.index_128[var_812]
                            while scan_index_817 < len(scan_tuple_817_vec):
                                scan_tuple_817 = scan_tuple_817_vec[scan_index_817]
                                scan_index_817 += 1
                                vec_817.append(scan_tuple_817)
                            # Program VectorLoop Region
                            vec_index817 = 0
                            while vec_index817 < len(vec_817):
                                var_818 = vec_817[vec_index817]
                                vec_index817 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_812_818 = (var_812, var_818)
                                prev_state = self.table_27[tuple_812_818]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_812_818] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_131_(var_812, var_818)

                                    # Program Call Region
                                    ret = self.proc_135_(var_812, var_818)

                            # Program TransitionState Region
                            tuple_812_812 = (var_812, var_812)
                            prev_state = self.table_6[tuple_812_812]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_812_812] = 1 | 4
                                if not present_bit:
                                    self.index_350[tuple_812_812[1]].append(tuple_812_812[0])
                                    self.index_948[tuple_812_812[0]].append(tuple_812_812[1])
                                # Program VectorAppend Region
                                vec_821.append((var_812, var_812))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_813_812 = (var_813, var_812)
                            prev_state = self.table_58[tuple_813_812]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_813_812] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_813_812[0]].append(tuple_813_812[1])
                                # Program VectorAppend Region
                                vec_842.append(var_813)
        # Program VectorClear Region
        del vec_810[:]
        vec_index810 = 0
        # Program VectorUnique Region
        vec_824 = list(set(vec_824))
        vec_index824 = 0
        # Program TableJoin Region
        while vec_index824 < len(vec_824):
            var_826 = vec_824[vec_index824]
            vec_index824 += 1
            if var_826 in self.index_217:
                tuple_825_1_index: int = 0
                tuple_825_1_vec: List[int] = self.index_304[var_826]
                while tuple_825_1_index < len(tuple_825_1_vec):
                    tuple_825_1 = tuple_825_1_vec[tuple_825_1_index]
                    tuple_825_1_index += 1
                    var_827 = tuple_825_1
                    # Program TransitionState Region
                    tuple_827_826_2 = (var_827, var_826, self.var_2)
                    prev_state = self.table_9[tuple_827_826_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_827_826_2] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_827_826_2[0], tuple_827_826_2[1])].append(tuple_827_826_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_826_827 = (var_826, var_827)
                        prev_state = self.table_27[tuple_826_827]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_826_827] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_826_827[0]].append(tuple_826_827[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_826)
                        if not ret:
                            # Program TransitionState Region
                            tuple_826_827 = (var_826, var_827)
                            prev_state = self.table_27[tuple_826_827]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_826_827] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_826_827[0]].append(tuple_826_827[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_827, var_826)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_827_826 = (var_827, var_826)
                                    prev_state = self.table_64[tuple_827_826]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_827_826] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_827_826[0]].append(tuple_827_826[1])
                                            self.index_970[tuple_827_826[1]].append(tuple_827_826[0])
                                        # Program VectorAppend Region
                                        vec_862.append(var_827)
                                # Program TransitionState Region
                                tuple_827_826 = (var_827, var_826)
                                prev_state = self.table_15[tuple_827_826]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_827_826] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_827_826[0]].append(tuple_827_826[1])
                        # Program TransitionState Region
                        tuple_827_826 = (var_827, var_826)
                        prev_state = self.table_106[tuple_827_826]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_827_826] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_827_826[1]].append(tuple_827_826[0])
                            # Program VectorAppend Region
                            vec_854.append(var_826)
                        # Program TransitionState Region
                        tuple_826 = var_826
                        prev_state = self.table_54[tuple_826]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_826] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_835.append(var_826)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_826 = var_826
                            prev_state = self.table_18[tuple_826]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_826] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_854.append(var_826)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_831: int
                                scan_index_831: int = 0
                                scan_tuple_831_vec: List[int] = self.index_128[var_826]
                                while scan_index_831 < len(scan_tuple_831_vec):
                                    scan_tuple_831 = scan_tuple_831_vec[scan_index_831]
                                    scan_index_831 += 1
                                    vec_831.append(scan_tuple_831)
                                # Program VectorLoop Region
                                vec_index831 = 0
                                while vec_index831 < len(vec_831):
                                    var_832 = vec_831[vec_index831]
                                    vec_index831 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_826_832 = (var_826, var_832)
                                    prev_state = self.table_27[tuple_826_832]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_826_832] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_826, var_832)

                                        # Program Call Region
                                        ret = self.proc_135_(var_826, var_832)

                                # Program TransitionState Region
                                tuple_826_826 = (var_826, var_826)
                                prev_state = self.table_6[tuple_826_826]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_826_826] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_826_826[1]].append(tuple_826_826[0])
                                        self.index_948[tuple_826_826[0]].append(tuple_826_826[1])
                                    # Program VectorAppend Region
                                    vec_821.append((var_826, var_826))
                        # Program TransitionState Region
                        tuple_827_826 = (var_827, var_826)
                        prev_state = self.table_58[tuple_827_826]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_58[tuple_827_826] = 1 | 4
                            if not present_bit:
                                self.index_325[tuple_827_826[0]].append(tuple_827_826[1])
                            # Program VectorAppend Region
                            vec_842.append(var_827)
        # Program VectorClear Region
        del vec_824[:]
        vec_index824 = 0
        # Program VectorUnique Region
        vec_835 = list(set(vec_835))
        vec_index835 = 0
        # Program TableJoin Region
        while vec_index835 < len(vec_835):
            var_837 = vec_835[vec_index835]
            vec_index835 += 1
            if var_837 in self.index_316:
                if var_837 in self.index_317:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_837 = var_837
                    prev_state = self.table_18[tuple_837]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_837] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_854.append(var_837)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_838: int
                        scan_index_838: int = 0
                        scan_tuple_838_vec: List[int] = self.index_128[var_837]
                        while scan_index_838 < len(scan_tuple_838_vec):
                            scan_tuple_838 = scan_tuple_838_vec[scan_index_838]
                            scan_index_838 += 1
                            vec_838.append(scan_tuple_838)
                        # Program VectorLoop Region
                        vec_index838 = 0
                        while vec_index838 < len(vec_838):
                            var_839 = vec_838[vec_index838]
                            vec_index838 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_837_839 = (var_837, var_839)
                            prev_state = self.table_27[tuple_837_839]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_837_839] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_837, var_839)

                                # Program Call Region
                                ret = self.proc_135_(var_837, var_839)

                        # Program TransitionState Region
                        tuple_837_837 = (var_837, var_837)
                        prev_state = self.table_6[tuple_837_837]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_837_837] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_837_837[1]].append(tuple_837_837[0])
                                self.index_948[tuple_837_837[0]].append(tuple_837_837[1])
                            # Program VectorAppend Region
                            vec_821.append((var_837, var_837))
        # Program VectorClear Region
        del vec_835[:]
        vec_index835 = 0
        # Program VectorUnique Region
        vec_842 = list(set(vec_842))
        vec_index842 = 0
        # Program TableJoin Region
        while vec_index842 < len(vec_842):
            var_844 = vec_842[vec_index842]
            vec_index842 += 1
            if var_844 in self.index_211:
                tuple_843_1_index: int = 0
                tuple_843_1_vec: List[int] = self.index_325[var_844]
                while tuple_843_1_index < len(tuple_843_1_vec):
                    tuple_843_1 = tuple_843_1_vec[tuple_843_1_index]
                    tuple_843_1_index += 1
                    var_845 = tuple_843_1
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_844_845 = (var_844, var_845)
                    prev_state = self.table_61[tuple_844_845]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_61[tuple_844_845] = 1 | 4
                        if not present_bit:
                            self.index_330[tuple_844_845[1]].append(tuple_844_845[0])
                        # Program VectorAppend Region
                        vec_846.append(var_845)
        # Program VectorClear Region
        del vec_842[:]
        vec_index842 = 0
        # Program VectorUnique Region
        vec_846 = list(set(vec_846))
        vec_index846 = 0
        # Program TableJoin Region
        while vec_index846 < len(vec_846):
            var_848 = vec_846[vec_index846]
            vec_index846 += 1
            if var_848 in self.index_316:
                tuple_847_1_index: int = 0
                tuple_847_1_vec: List[int] = self.index_330[var_848]
                while tuple_847_1_index < len(tuple_847_1_vec):
                    tuple_847_1 = tuple_847_1_vec[tuple_847_1_index]
                    tuple_847_1_index += 1
                    var_849 = tuple_847_1
                    # Program TransitionState Region
                    tuple_849 = var_849
                    prev_state = self.table_18[tuple_849]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_849] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_854.append(var_849)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_850: int
                        scan_index_850: int = 0
                        scan_tuple_850_vec: List[int] = self.index_128[var_849]
                        while scan_index_850 < len(scan_tuple_850_vec):
                            scan_tuple_850 = scan_tuple_850_vec[scan_index_850]
                            scan_index_850 += 1
                            vec_850.append(scan_tuple_850)
                        # Program VectorLoop Region
                        vec_index850 = 0
                        while vec_index850 < len(vec_850):
                            var_851 = vec_850[vec_index850]
                            vec_index850 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_849_851 = (var_849, var_851)
                            prev_state = self.table_27[tuple_849_851]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_849_851] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_849, var_851)

                                # Program Call Region
                                ret = self.proc_135_(var_849, var_851)

                        # Program TransitionState Region
                        tuple_849_849 = (var_849, var_849)
                        prev_state = self.table_6[tuple_849_849]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_849_849] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_849_849[1]].append(tuple_849_849[0])
                                self.index_948[tuple_849_849[0]].append(tuple_849_849[1])
                            # Program VectorAppend Region
                            vec_821.append((var_849, var_849))
        # Program VectorClear Region
        del vec_846[:]
        vec_index846 = 0
        # Program VectorUnique Region
        vec_854 = list(set(vec_854))
        vec_index854 = 0
        # Program TableJoin Region
        while vec_index854 < len(vec_854):
            var_856 = vec_854[vec_index854]
            vec_index854 += 1
            tuple_855_0_index: int = 0
            tuple_855_0_vec: List[int] = self.index_339[var_856]
            while tuple_855_0_index < len(tuple_855_0_vec):
                tuple_855_0 = tuple_855_0_vec[tuple_855_0_index]
                tuple_855_0_index += 1
                var_857 = tuple_855_0
                if var_856 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_857_856 = (var_857, var_856)
                    prev_state = self.table_109[tuple_857_856]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_857_856] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_857_856[1]].append(tuple_857_856[0])
                        # Program VectorAppend Region
                        vec_858.append(var_856)
                    # Program TransitionState Region
                    tuple_857_856 = (var_857, var_856)
                    prev_state = self.table_22[tuple_857_856]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_857_856] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_857_856[0]].append(tuple_857_856[1])
        # Program VectorClear Region
        del vec_854[:]
        vec_index854 = 0
        # Program VectorUnique Region
        vec_858 = list(set(vec_858))
        vec_index858 = 0
        # Program TableJoin Region
        while vec_index858 < len(vec_858):
            var_860 = vec_858[vec_index858]
            vec_index858 += 1
            tuple_859_0_index: int = 0
            tuple_859_0_vec: List[int] = self.index_345[var_860]
            while tuple_859_0_index < len(tuple_859_0_vec):
                tuple_859_0 = tuple_859_0_vec[tuple_859_0_index]
                tuple_859_0_index += 1
                var_861 = tuple_859_0
                if var_860 in self.index_316:
                    # Program TransitionState Region
                    tuple_861 = var_861
                    prev_state = self.table_13[tuple_861]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_861] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_858[:]
        vec_index858 = 0
        # Program VectorUnique Region
        vec_862 = list(set(vec_862))
        vec_index862 = 0
        # Program TableJoin Region
        while vec_index862 < len(vec_862):
            var_864 = vec_862[vec_index862]
            vec_index862 += 1
            tuple_863_0_index: int = 0
            tuple_863_0_vec: List[int] = self.index_350[var_864]
            while tuple_863_0_index < len(tuple_863_0_vec):
                tuple_863_0 = tuple_863_0_vec[tuple_863_0_index]
                tuple_863_0_index += 1
                var_865 = tuple_863_0
                tuple_863_1_index: int = 0
                tuple_863_1_vec: List[int] = self.index_351[var_864]
                while tuple_863_1_index < len(tuple_863_1_vec):
                    tuple_863_1 = tuple_863_1_vec[tuple_863_1_index]
                    tuple_863_1_index += 1
                    var_866 = tuple_863_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_354_(var_865, var_864)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_224_(var_864, var_866)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_359_(var_865, var_866)
                            if not ret:
                                # Program TransitionState Region
                                tuple_865_866 = (var_865, var_866)
                                prev_state = self.table_6[tuple_865_866]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_865_866] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_865_866[1]].append(tuple_865_866[0])
                                        self.index_948[tuple_865_866[0]].append(tuple_865_866[1])
                                    # Program VectorAppend Region
                                    vec_821.append((var_865, var_866))
        # Program VectorClear Region
        del vec_862[:]
        vec_index862 = 0
        # Induction Fixpoint Loop Region
        while len(vec_821):
            # Program Call Region
            param_823_0 = [vec_821]
            ret = self.proc_139_(param_823_0)
            vec_821 = param_823_0[0]

        vec_index821 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_821[:]
        vec_index821 = 0
        # Program Return Region
        return False
        return False

    def relocation_2(self, vec_871: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index871: int = 0
        vec_874: List[int] = list()
        vec_index874: int = 0
        vec_879: List[int] = list()
        vec_index879: int = 0
        vec_884: List[int] = list()
        vec_index884: int = 0
        vec_891: List[int] = list()
        vec_index891: int = 0
        vec_895: List[Tuple[int, int]] = list()
        vec_index895: int = 0
        vec_898: List[int] = list()
        vec_index898: int = 0
        vec_905: List[int] = list()
        vec_index905: int = 0
        vec_909: List[int] = list()
        vec_index909: int = 0
        vec_912: List[int] = list()
        vec_index912: int = 0
        vec_916: List[int] = list()
        vec_index916: int = 0
        vec_920: List[int] = list()
        vec_index920: int = 0
        vec_924: List[int] = list()
        vec_index924: int = 0
        vec_928: List[int] = list()
        vec_index928: int = 0
        vec_932: List[int] = list()
        vec_index932: int = 0
        vec_936: List[int] = list()
        vec_index936: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index871 = 0
        while vec_index871 < len(vec_871):
            var_872, var_873 = vec_871[vec_index871]
            vec_index871 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_872_873 = (var_872, var_873)
            prev_state = self.table_86[tuple_872_873]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_86[tuple_872_873] = 1 | 4
                if not present_bit:
                    self.index_243[tuple_872_873[0]].append(tuple_872_873[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_879.append(var_872)
                # Program VectorAppend Region
                vec_874.append(var_872)
            # Program TransitionState Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_872_873 = (var_872, var_873)
            prev_state = self.table_86[tuple_872_873]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_86[tuple_872_873] = 1 | 4
                if not present_bit:
                    self.index_243[tuple_872_873[0]].append(tuple_872_873[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_879.append(var_872)
                # Program VectorAppend Region
                vec_874.append(var_872)
        # Program VectorUnique Region
        vec_874 = list(set(vec_874))
        vec_index874 = 0
        # Program TableJoin Region
        while vec_index874 < len(vec_874):
            var_876 = vec_874[vec_index874]
            vec_index874 += 1
            tuple_875_0_index: int = 0
            tuple_875_0_vec: List[int] = self.index_243[var_876]
            while tuple_875_0_index < len(tuple_875_0_vec):
                tuple_875_0 = tuple_875_0_vec[tuple_875_0_index]
                tuple_875_0_index += 1
                var_877 = tuple_875_0
                tuple_875_1_index: int = 0
                tuple_875_1_vec: List[int] = self.index_244[var_876]
                while tuple_875_1_index < len(tuple_875_1_vec):
                    tuple_875_1 = tuple_875_1_vec[tuple_875_1_index]
                    tuple_875_1_index += 1
                    var_878 = tuple_875_1
                    # Program TransitionState Region
                    tuple_877_878 = (var_877, var_878)
                    prev_state = self.table_100[tuple_877_878]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_100[tuple_877_878] = 1 | 4
                        if not present_bit:
                            self.index_292[tuple_877_878[0]].append(tuple_877_878[1])
                        # Program VectorAppend Region
                        vec_884.append(var_877)
        # Program VectorClear Region
        del vec_874[:]
        vec_index874 = 0
        # Program VectorUnique Region
        vec_879 = list(set(vec_879))
        vec_index879 = 0
        # Program TableJoin Region
        while vec_index879 < len(vec_879):
            var_881 = vec_879[vec_index879]
            vec_index879 += 1
            tuple_880_0_index: int = 0
            tuple_880_0_vec: List[int] = self.index_243[var_881]
            while tuple_880_0_index < len(tuple_880_0_vec):
                tuple_880_0 = tuple_880_0_vec[tuple_880_0_index]
                tuple_880_0_index += 1
                var_882 = tuple_880_0
                tuple_880_1_index: int = 0
                tuple_880_1_vec: List[int] = self.index_262[var_881]
                while tuple_880_1_index < len(tuple_880_1_vec):
                    tuple_880_1 = tuple_880_1_vec[tuple_880_1_index]
                    tuple_880_1_index += 1
                    var_883 = tuple_880_1
                    # Program TransitionState Region
                    tuple_882_883 = (var_882, var_883)
                    prev_state = self.table_92[tuple_882_883]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_92[tuple_882_883] = 1 | 4
                        if not present_bit:
                            self.index_304[tuple_882_883[0]].append(tuple_882_883[1])
                        # Program VectorAppend Region
                        vec_898.append(var_882)
        # Program VectorClear Region
        del vec_879[:]
        vec_index879 = 0
        # Program VectorUnique Region
        vec_884 = list(set(vec_884))
        vec_index884 = 0
        # Program TableJoin Region
        while vec_index884 < len(vec_884):
            var_886 = vec_884[vec_index884]
            vec_index884 += 1
            if var_886 in self.index_217:
                tuple_885_1_index: int = 0
                tuple_885_1_vec: List[int] = self.index_292[var_886]
                while tuple_885_1_index < len(tuple_885_1_vec):
                    tuple_885_1 = tuple_885_1_vec[tuple_885_1_index]
                    tuple_885_1_index += 1
                    var_887 = tuple_885_1
                    # Program TransitionState Region
                    tuple_887_886_0 = (var_887, var_886, self.var_0)
                    prev_state = self.table_9[tuple_887_886_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_887_886_0] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_887_886_0[0], tuple_887_886_0[1])].append(tuple_887_886_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_886_887 = (var_886, var_887)
                        prev_state = self.table_27[tuple_886_887]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_886_887] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_886_887[0]].append(tuple_886_887[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_886)
                        if not ret:
                            # Program TransitionState Region
                            tuple_886_887 = (var_886, var_887)
                            prev_state = self.table_27[tuple_886_887]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_886_887] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_886_887[0]].append(tuple_886_887[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_887, var_886)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_887_886 = (var_887, var_886)
                                    prev_state = self.table_64[tuple_887_886]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_887_886] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_887_886[0]].append(tuple_887_886[1])
                                            self.index_970[tuple_887_886[1]].append(tuple_887_886[0])
                                        # Program VectorAppend Region
                                        vec_936.append(var_887)
                                # Program TransitionState Region
                                tuple_887_886 = (var_887, var_886)
                                prev_state = self.table_15[tuple_887_886]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_887_886] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_887_886[0]].append(tuple_887_886[1])
                        # Program TransitionState Region
                        tuple_887_886 = (var_887, var_886)
                        prev_state = self.table_106[tuple_887_886]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_887_886] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_887_886[1]].append(tuple_887_886[0])
                            # Program VectorAppend Region
                            vec_928.append(var_886)
                        # Program TransitionState Region
                        tuple_886 = var_886
                        prev_state = self.table_54[tuple_886]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_886] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_909.append(var_886)
                        # Program TransitionState Region
                        tuple_886 = var_886
                        prev_state = self.table_18[tuple_886]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_886] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_928.append(var_886)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_891: int
                            scan_index_891: int = 0
                            scan_tuple_891_vec: List[int] = self.index_128[var_886]
                            while scan_index_891 < len(scan_tuple_891_vec):
                                scan_tuple_891 = scan_tuple_891_vec[scan_index_891]
                                scan_index_891 += 1
                                vec_891.append(scan_tuple_891)
                            # Program VectorLoop Region
                            vec_index891 = 0
                            while vec_index891 < len(vec_891):
                                var_892 = vec_891[vec_index891]
                                vec_index891 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_886_892 = (var_886, var_892)
                                prev_state = self.table_27[tuple_886_892]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_886_892] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_131_(var_886, var_892)

                                    # Program Call Region
                                    ret = self.proc_135_(var_886, var_892)

                            # Program TransitionState Region
                            tuple_886_886 = (var_886, var_886)
                            prev_state = self.table_6[tuple_886_886]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_886_886] = 1 | 4
                                if not present_bit:
                                    self.index_350[tuple_886_886[1]].append(tuple_886_886[0])
                                    self.index_948[tuple_886_886[0]].append(tuple_886_886[1])
                                # Program VectorAppend Region
                                vec_895.append((var_886, var_886))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_887_886 = (var_887, var_886)
                            prev_state = self.table_58[tuple_887_886]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_58[tuple_887_886] = 1 | 4
                                if not present_bit:
                                    self.index_325[tuple_887_886[0]].append(tuple_887_886[1])
                                # Program VectorAppend Region
                                vec_916.append(var_887)
        # Program VectorClear Region
        del vec_884[:]
        vec_index884 = 0
        # Program VectorUnique Region
        vec_898 = list(set(vec_898))
        vec_index898 = 0
        # Program TableJoin Region
        while vec_index898 < len(vec_898):
            var_900 = vec_898[vec_index898]
            vec_index898 += 1
            if var_900 in self.index_217:
                tuple_899_1_index: int = 0
                tuple_899_1_vec: List[int] = self.index_304[var_900]
                while tuple_899_1_index < len(tuple_899_1_vec):
                    tuple_899_1 = tuple_899_1_vec[tuple_899_1_index]
                    tuple_899_1_index += 1
                    var_901 = tuple_899_1
                    # Program TransitionState Region
                    tuple_901_900_2 = (var_901, var_900, self.var_2)
                    prev_state = self.table_9[tuple_901_900_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_901_900_2] = 1 | 4
                        if not present_bit:
                            self.index_991[(tuple_901_900_2[0], tuple_901_900_2[1])].append(tuple_901_900_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_900_901 = (var_900, var_901)
                        prev_state = self.table_27[tuple_900_901]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_900_901] = 2 | 4
                            if not present_bit:
                                self.index_128[tuple_900_901[0]].append(tuple_900_901[1])
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_221_(var_900)
                        if not ret:
                            # Program TransitionState Region
                            tuple_900_901 = (var_900, var_901)
                            prev_state = self.table_27[tuple_900_901]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_900_901] = 1 | 4
                                if not present_bit:
                                    self.index_128[tuple_900_901[0]].append(tuple_900_901[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_224_(var_901, var_900)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_901_900 = (var_901, var_900)
                                    prev_state = self.table_64[tuple_901_900]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_64[tuple_901_900] = 1 | 4
                                        if not present_bit:
                                            self.index_351[tuple_901_900[0]].append(tuple_901_900[1])
                                            self.index_970[tuple_901_900[1]].append(tuple_901_900[0])
                                        # Program VectorAppend Region
                                        vec_936.append(var_901)
                                # Program TransitionState Region
                                tuple_901_900 = (var_901, var_900)
                                prev_state = self.table_15[tuple_901_900]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_901_900] = 1 | 4
                                    if not present_bit:
                                        self.index_944[tuple_901_900[0]].append(tuple_901_900[1])
                        # Program TransitionState Region
                        tuple_901_900 = (var_901, var_900)
                        prev_state = self.table_106[tuple_901_900]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_106[tuple_901_900] = 1 | 4
                            if not present_bit:
                                self.index_339[tuple_901_900[1]].append(tuple_901_900[0])
                            # Program VectorAppend Region
                            vec_928.append(var_900)
                        # Program TransitionState Region
                        tuple_900 = var_900
                        prev_state = self.table_54[tuple_900]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_54[tuple_900] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_909.append(var_900)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_900 = var_900
                            prev_state = self.table_18[tuple_900]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_900] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_928.append(var_900)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_905: int
                                scan_index_905: int = 0
                                scan_tuple_905_vec: List[int] = self.index_128[var_900]
                                while scan_index_905 < len(scan_tuple_905_vec):
                                    scan_tuple_905 = scan_tuple_905_vec[scan_index_905]
                                    scan_index_905 += 1
                                    vec_905.append(scan_tuple_905)
                                # Program VectorLoop Region
                                vec_index905 = 0
                                while vec_index905 < len(vec_905):
                                    var_906 = vec_905[vec_index905]
                                    vec_index905 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_900_906 = (var_900, var_906)
                                    prev_state = self.table_27[tuple_900_906]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_900_906] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_131_(var_900, var_906)

                                        # Program Call Region
                                        ret = self.proc_135_(var_900, var_906)

                                # Program TransitionState Region
                                tuple_900_900 = (var_900, var_900)
                                prev_state = self.table_6[tuple_900_900]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_900_900] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_900_900[1]].append(tuple_900_900[0])
                                        self.index_948[tuple_900_900[0]].append(tuple_900_900[1])
                                    # Program VectorAppend Region
                                    vec_895.append((var_900, var_900))
                        # Program TransitionState Region
                        tuple_901_900 = (var_901, var_900)
                        prev_state = self.table_58[tuple_901_900]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_58[tuple_901_900] = 1 | 4
                            if not present_bit:
                                self.index_325[tuple_901_900[0]].append(tuple_901_900[1])
                            # Program VectorAppend Region
                            vec_916.append(var_901)
        # Program VectorClear Region
        del vec_898[:]
        vec_index898 = 0
        # Program VectorUnique Region
        vec_909 = list(set(vec_909))
        vec_index909 = 0
        # Program TableJoin Region
        while vec_index909 < len(vec_909):
            var_911 = vec_909[vec_index909]
            vec_index909 += 1
            if var_911 in self.index_316:
                if var_911 in self.index_317:
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_911 = var_911
                    prev_state = self.table_18[tuple_911]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_911] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_928.append(var_911)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_912: int
                        scan_index_912: int = 0
                        scan_tuple_912_vec: List[int] = self.index_128[var_911]
                        while scan_index_912 < len(scan_tuple_912_vec):
                            scan_tuple_912 = scan_tuple_912_vec[scan_index_912]
                            scan_index_912 += 1
                            vec_912.append(scan_tuple_912)
                        # Program VectorLoop Region
                        vec_index912 = 0
                        while vec_index912 < len(vec_912):
                            var_913 = vec_912[vec_index912]
                            vec_index912 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_911_913 = (var_911, var_913)
                            prev_state = self.table_27[tuple_911_913]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_911_913] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_911, var_913)

                                # Program Call Region
                                ret = self.proc_135_(var_911, var_913)

                        # Program TransitionState Region
                        tuple_911_911 = (var_911, var_911)
                        prev_state = self.table_6[tuple_911_911]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_911_911] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_911_911[1]].append(tuple_911_911[0])
                                self.index_948[tuple_911_911[0]].append(tuple_911_911[1])
                            # Program VectorAppend Region
                            vec_895.append((var_911, var_911))
        # Program VectorClear Region
        del vec_909[:]
        vec_index909 = 0
        # Program VectorUnique Region
        vec_916 = list(set(vec_916))
        vec_index916 = 0
        # Program TableJoin Region
        while vec_index916 < len(vec_916):
            var_918 = vec_916[vec_index916]
            vec_index916 += 1
            if var_918 in self.index_211:
                tuple_917_1_index: int = 0
                tuple_917_1_vec: List[int] = self.index_325[var_918]
                while tuple_917_1_index < len(tuple_917_1_vec):
                    tuple_917_1 = tuple_917_1_vec[tuple_917_1_index]
                    tuple_917_1_index += 1
                    var_919 = tuple_917_1
                    # Program TransitionState Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_918_919 = (var_918, var_919)
                    prev_state = self.table_61[tuple_918_919]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_61[tuple_918_919] = 1 | 4
                        if not present_bit:
                            self.index_330[tuple_918_919[1]].append(tuple_918_919[0])
                        # Program VectorAppend Region
                        vec_920.append(var_919)
        # Program VectorClear Region
        del vec_916[:]
        vec_index916 = 0
        # Program VectorUnique Region
        vec_920 = list(set(vec_920))
        vec_index920 = 0
        # Program TableJoin Region
        while vec_index920 < len(vec_920):
            var_922 = vec_920[vec_index920]
            vec_index920 += 1
            if var_922 in self.index_316:
                tuple_921_1_index: int = 0
                tuple_921_1_vec: List[int] = self.index_330[var_922]
                while tuple_921_1_index < len(tuple_921_1_vec):
                    tuple_921_1 = tuple_921_1_vec[tuple_921_1_index]
                    tuple_921_1_index += 1
                    var_923 = tuple_921_1
                    # Program TransitionState Region
                    tuple_923 = var_923
                    prev_state = self.table_18[tuple_923]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_923] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_928.append(var_923)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_924: int
                        scan_index_924: int = 0
                        scan_tuple_924_vec: List[int] = self.index_128[var_923]
                        while scan_index_924 < len(scan_tuple_924_vec):
                            scan_tuple_924 = scan_tuple_924_vec[scan_index_924]
                            scan_index_924 += 1
                            vec_924.append(scan_tuple_924)
                        # Program VectorLoop Region
                        vec_index924 = 0
                        while vec_index924 < len(vec_924):
                            var_925 = vec_924[vec_index924]
                            vec_index924 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_923_925 = (var_923, var_925)
                            prev_state = self.table_27[tuple_923_925]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_923_925] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_131_(var_923, var_925)

                                # Program Call Region
                                ret = self.proc_135_(var_923, var_925)

                        # Program TransitionState Region
                        tuple_923_923 = (var_923, var_923)
                        prev_state = self.table_6[tuple_923_923]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_923_923] = 1 | 4
                            if not present_bit:
                                self.index_350[tuple_923_923[1]].append(tuple_923_923[0])
                                self.index_948[tuple_923_923[0]].append(tuple_923_923[1])
                            # Program VectorAppend Region
                            vec_895.append((var_923, var_923))
        # Program VectorClear Region
        del vec_920[:]
        vec_index920 = 0
        # Program VectorUnique Region
        vec_928 = list(set(vec_928))
        vec_index928 = 0
        # Program TableJoin Region
        while vec_index928 < len(vec_928):
            var_930 = vec_928[vec_index928]
            vec_index928 += 1
            tuple_929_0_index: int = 0
            tuple_929_0_vec: List[int] = self.index_339[var_930]
            while tuple_929_0_index < len(tuple_929_0_vec):
                tuple_929_0 = tuple_929_0_vec[tuple_929_0_index]
                tuple_929_0_index += 1
                var_931 = tuple_929_0
                if var_930 in self.index_340:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_931_930 = (var_931, var_930)
                    prev_state = self.table_109[tuple_931_930]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_931_930] = 1 | 4
                        if not present_bit:
                            self.index_345[tuple_931_930[1]].append(tuple_931_930[0])
                        # Program VectorAppend Region
                        vec_932.append(var_930)
                    # Program TransitionState Region
                    tuple_931_930 = (var_931, var_930)
                    prev_state = self.table_22[tuple_931_930]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_931_930] = 1 | 4
                        if not present_bit:
                            self.index_952[tuple_931_930[0]].append(tuple_931_930[1])
        # Program VectorClear Region
        del vec_928[:]
        vec_index928 = 0
        # Program VectorUnique Region
        vec_932 = list(set(vec_932))
        vec_index932 = 0
        # Program TableJoin Region
        while vec_index932 < len(vec_932):
            var_934 = vec_932[vec_index932]
            vec_index932 += 1
            tuple_933_0_index: int = 0
            tuple_933_0_vec: List[int] = self.index_345[var_934]
            while tuple_933_0_index < len(tuple_933_0_vec):
                tuple_933_0 = tuple_933_0_vec[tuple_933_0_index]
                tuple_933_0_index += 1
                var_935 = tuple_933_0
                if var_934 in self.index_316:
                    # Program TransitionState Region
                    tuple_935 = var_935
                    prev_state = self.table_13[tuple_935]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_935] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_932[:]
        vec_index932 = 0
        # Program VectorUnique Region
        vec_936 = list(set(vec_936))
        vec_index936 = 0
        # Program TableJoin Region
        while vec_index936 < len(vec_936):
            var_938 = vec_936[vec_index936]
            vec_index936 += 1
            tuple_937_0_index: int = 0
            tuple_937_0_vec: List[int] = self.index_350[var_938]
            while tuple_937_0_index < len(tuple_937_0_vec):
                tuple_937_0 = tuple_937_0_vec[tuple_937_0_index]
                tuple_937_0_index += 1
                var_939 = tuple_937_0
                tuple_937_1_index: int = 0
                tuple_937_1_vec: List[int] = self.index_351[var_938]
                while tuple_937_1_index < len(tuple_937_1_vec):
                    tuple_937_1 = tuple_937_1_vec[tuple_937_1_index]
                    tuple_937_1_index += 1
                    var_940 = tuple_937_1
                    # Program Call Region
                    # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_354_(var_939, var_938)
                    if ret:
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_224_(var_938, var_940)
                        if ret:
                            # Program Call Region
                            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_359_(var_939, var_940)
                            if not ret:
                                # Program TransitionState Region
                                tuple_939_940 = (var_939, var_940)
                                prev_state = self.table_6[tuple_939_940]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_939_940] = 1 | 4
                                    if not present_bit:
                                        self.index_350[tuple_939_940[1]].append(tuple_939_940[0])
                                        self.index_948[tuple_939_940[0]].append(tuple_939_940[1])
                                    # Program VectorAppend Region
                                    vec_895.append((var_939, var_940))
        # Program VectorClear Region
        del vec_936[:]
        vec_index936 = 0
        # Induction Fixpoint Loop Region
        while len(vec_895):
            # Program Call Region
            param_897_0 = [vec_895]
            ret = self.proc_139_(param_897_0)
            vec_895 = param_897_0[0]

        vec_index895 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_895[:]
        vec_index895 = 0
        # Program Return Region
        return False
        return False

    def proc_945_(self, var_946: int, var_947: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[(var_946, var_947)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_946_947 = (var_946, var_947)
            prev_state = self.table_15[tuple_946_947]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_946_947] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker::call_pred
                ret = self.proc_979_(var_947, var_946)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_946_947 = (var_946, var_947)
                    prev_state = self.table_15[tuple_946_947]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_946_947] = 1 | 4
                        if not present_bit:
                            self.index_944[tuple_946_947[0]].append(tuple_946_947[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_949_(self, var_950: int, var_951: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_953_(var_950, var_951)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_953_(self, var_954: int, var_955: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_954, var_955)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_954_955 = (var_954, var_955)
            prev_state = self.table_6[tuple_954_955]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_954_955] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_961_(var_954, var_955)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_954_955 = (var_954, var_955)
                    prev_state = self.table_6[tuple_954_955]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_954_955] = 1 | 4
                        if not present_bit:
                            self.index_350[tuple_954_955[1]].append(tuple_954_955[0])
                            self.index_948[tuple_954_955[0]].append(tuple_954_955[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_961_(self, var_962: int, var_963: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_965_(var_962, var_963)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_965_(self, var_966: int, var_967: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_969: List[int] = list()
        vec_index969: int = 0
        vec_971: List[int] = list()
        vec_index971: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_971: int
        scan_index_971: int = 0
        scan_tuple_971_vec: List[int] = self.index_970[var_967]
        while scan_index_971 < len(scan_tuple_971_vec):
            scan_tuple_971 = scan_tuple_971_vec[scan_index_971]
            scan_index_971 += 1
            vec_971.append(scan_tuple_971)
        # Program VectorLoop Region
        vec_index971 = 0
        while vec_index971 < len(vec_971):
            var_972 = vec_971[vec_index971]
            vec_index971 += 1
            # Program VectorAppend Region
            vec_969.append(var_972)
        # Program VectorUnique Region
        vec_969 = list(set(vec_969))
        vec_index969 = 0
        # Program TableJoin Region
        while vec_index969 < len(vec_969):
            var_974 = vec_969[vec_index969]
            vec_index969 += 1
            tuple_973_0_index: int = 0
            tuple_973_0_vec: List[int] = self.index_350[var_974]
            while tuple_973_0_index < len(tuple_973_0_vec):
                tuple_973_0 = tuple_973_0_vec[tuple_973_0_index]
                tuple_973_0_index += 1
                var_975 = tuple_973_0
                tuple_973_1_index: int = 0
                tuple_973_1_vec: List[int] = self.index_351[var_974]
                while tuple_973_1_index < len(tuple_973_1_vec):
                    tuple_973_1 = tuple_973_1_vec[tuple_973_1_index]
                    tuple_973_1_index += 1
                    var_976 = tuple_973_1
                    # Program TupleCompare Region
                    if (var_966, var_967, ) == (var_975, var_976, ):
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_354_(var_975, var_974)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_224_(var_974, var_976)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_969[:]
        vec_index969 = 0
        # Program Return Region
        return False
        return False

    def proc_979_(self, var_980: int, var_981: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_27[(var_980, var_981)] & 3
        if state == 1:
            # Program Series Region
            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_221_(var_980)
            if not ret:
                # Program Return Region
                return True
            # Program TransitionState Region
            tuple_980_981 = (var_980, var_981)
            prev_state = self.table_27[tuple_980_981]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 1:
                self.table_27[tuple_980_981] = 0 | 4
        elif state == 2:
            # Program TransitionState Region
            tuple_980_981 = (var_980, var_981)
            prev_state = self.table_27[tuple_980_981]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_27[tuple_980_981] = 0 | 4
                # Program Call Region
                # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_221_(var_980)
                if not ret:
                    # Program Call Region
                    ret = self.proc_987_(var_981, var_980)
                    if ret:
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_987_(self, var_988: int, var_989: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_992: List[int] = list()
        vec_index992: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_992: int
        scan_index_992: int = 0
        scan_tuple_992_vec: List[int] = self.index_991[var_988, var_989]
        while scan_index_992 < len(scan_tuple_992_vec):
            scan_tuple_992 = scan_tuple_992_vec[scan_index_992]
            scan_index_992 += 1
            vec_992.append(scan_tuple_992)
        # Program VectorLoop Region
        vec_index992 = 0
        while vec_index992 < len(vec_992):
            var_993 = vec_992[vec_index992]
            vec_index992 += 1
            # Program CheckState Region
            state = self.table_9[(var_988, var_989, var_993)] & 3
            if state == 1:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_995_(self, var_996: int, var_997: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_996_997 = (var_996, var_997)
        prev_state = self.table_6[tuple_996_997]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_6[tuple_996_997] = 0 | 4
            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_961_(var_996, var_997)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1014_(self, var_1015: int, var_1016: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1018: List[int] = list()
        vec_index1018: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1018: int
        scan_index_1018: int = 0
        scan_tuple_1018_vec: List[int] = self.index_350[var_1015]
        while scan_index_1018 < len(scan_tuple_1018_vec):
            scan_tuple_1018 = scan_tuple_1018_vec[scan_index_1018]
            scan_index_1018 += 1
            vec_1018.append(scan_tuple_1018)
        # Program VectorLoop Region
        vec_index1018 = 0
        while vec_index1018 < len(vec_1018):
            var_1019 = vec_1018[vec_index1018]
            vec_index1018 += 1
            # Program Call Region
            ret = self.proc_1020_(var_1015, var_1019, var_1016)

        # Program Return Region
        return False
        return False

    def proc_1020_(self, var_1021: int, var_1022: int, var_1023: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1022_1023 = (var_1022, var_1023)
        prev_state = self.table_6[tuple_1022_1023]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_6[tuple_1022_1023] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1038_(var_1022, var_1023)

            # Program Call Region
            # /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/Steve/Desktop/TrailOfBits/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_995_(var_1022, var_1023)

        # Program Return Region
        return False
        return False

    def proc_1038_(self, var_1039: int, var_1040: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1042: List[int] = list()
        vec_index1042: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1042: int
        scan_index_1042: int = 0
        scan_tuple_1042_vec: List[int] = self.index_351[var_1040]
        while scan_index_1042 < len(scan_tuple_1042_vec):
            scan_tuple_1042 = scan_tuple_1042_vec[scan_index_1042]
            scan_index_1042 += 1
            vec_1042.append(scan_tuple_1042)
        # Program VectorLoop Region
        vec_index1042 = 0
        while vec_index1042 < len(vec_1042):
            var_1043 = vec_1042[vec_index1042]
            vec_index1042 += 1
            # Program Call Region
            ret = self.proc_1020_(var_1040, var_1039, var_1043)

        # Program Return Region
        return False
        return False

    def get_external_calls_f(self) -> Iterator[int]:
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

    def intraproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_944[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_945_(param_0, param_1):
                continue
            yield param_1

    def function_b(self, param_0: int) -> bool:
        state: int = 0
        tuple_index: int = 0
        if True:
            full_tuple = param_0
            state = self.table_18[full_tuple] & 3
            if state != 1:
                return False
            return True

    def function_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_18:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_18[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def function_instruction_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_948[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_949_(param_0, param_1):
                continue
            yield param_1

    def get_instructions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_20:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_20[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def interproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_952[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_22[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

    def get_sections_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_25:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_25[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

