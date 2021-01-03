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
        self.index_290: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_756: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_9: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_799: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)

        self.table_13: DefaultDict[int, int] = defaultdict(int)

        self.table_15: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_752: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_18: DefaultDict[int, int] = defaultdict(int)
        self.index_280 = self.table_18

        self.table_20: DefaultDict[int, int] = defaultdict(int)

        self.table_22: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_760: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_25: DefaultDict[bytes, int] = defaultdict(int)

        self.table_27: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_116: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_30: DefaultDict[int, int] = defaultdict(int)
        self.index_256 = self.table_30

        self.table_32: DefaultDict[int, int] = defaultdict(int)
        self.index_257 = self.table_32

        self.table_34: DefaultDict[int, int] = defaultdict(int)
        self.index_175 = self.table_34

        self.table_36: DefaultDict[int, int] = defaultdict(int)
        self.index_157 = self.table_36

        self.table_38: DefaultDict[int, int] = defaultdict(int)
        self.index_151 = self.table_38

        self.table_40: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_265: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_43: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_270: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_46: DefaultDict[int, int] = defaultdict(int)
        self.index_137 = self.table_46

        self.table_48: DefaultDict[int, int] = defaultdict(int)
        self.index_115 = self.table_48

        self.table_50: DefaultDict[int, int] = defaultdict(int)
        self.index_114 = self.table_50

        self.table_52: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_291: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_778: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_55: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_156: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_59: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_220: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_62: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_504 = self.table_62
        self.index_509: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_65: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_505 = self.table_65
        self.index_510: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_68: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_208: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_71: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_146: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_74: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_183: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_77: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_202: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_80: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_244: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_83: DefaultDict[int, int] = defaultdict(int)
        self.index_145 = self.table_83

        self.table_85: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_184: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_88: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_232: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_91: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_190: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_94: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_279: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_97: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_285: DefaultDict[int, List[int]] = defaultdict(list)

        self.var_0: int = 5
        self.var_1: int = 2
        self.var_2: int = 1
        self.var_3: int = 6
        self.var_4: int = 6
        self.var_5: int = 0
        self.init_100_()

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

    def init_100_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False
        return False

    def section_3(self, vec_102: List[Tuple[bytes, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index102: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index102 = 0
        while vec_index102 < len(vec_102):
            var_103, var_104, var_105 = vec_102[vec_index102]
            vec_index102 += 1
            # Program TransitionState Region
            tuple_103 = var_103
            prev_state = self.table_25[tuple_103]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_25[tuple_103] = 1 | 4
                if not present_bit:
                    pass
        # Program Return Region
        return False
        return False

    def instruction_3(self, vec_107: List[Tuple[int, int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index107: int = 0
        vec_111: List[int] = list()
        vec_index111: int = 0
        vec_117: List[int] = list()
        vec_index117: int = 0
        vec_131: List[Tuple[int, int]] = list()
        vec_index131: int = 0
        vec_134: List[int] = list()
        vec_index134: int = 0
        vec_138: List[int] = list()
        vec_index138: int = 0
        vec_142: List[int] = list()
        vec_index142: int = 0
        vec_148: List[int] = list()
        vec_index148: int = 0
        vec_153: List[int] = list()
        vec_index153: int = 0
        vec_168: List[int] = list()
        vec_index168: int = 0
        vec_172: List[int] = list()
        vec_index172: int = 0
        vec_176: List[int] = list()
        vec_index176: int = 0
        vec_180: List[int] = list()
        vec_index180: int = 0
        vec_187: List[int] = list()
        vec_index187: int = 0
        vec_195: List[int] = list()
        vec_index195: int = 0
        vec_199: List[int] = list()
        vec_index199: int = 0
        vec_205: List[int] = list()
        vec_index205: int = 0
        vec_213: List[int] = list()
        vec_index213: int = 0
        vec_217: List[int] = list()
        vec_index217: int = 0
        vec_225: List[int] = list()
        vec_index225: int = 0
        vec_229: List[int] = list()
        vec_index229: int = 0
        vec_237: List[int] = list()
        vec_index237: int = 0
        vec_241: List[int] = list()
        vec_index241: int = 0
        vec_249: List[int] = list()
        vec_index249: int = 0
        vec_253: List[int] = list()
        vec_index253: int = 0
        vec_258: List[int] = list()
        vec_index258: int = 0
        vec_262: List[int] = list()
        vec_index262: int = 0
        vec_267: List[int] = list()
        vec_index267: int = 0
        vec_272: List[int] = list()
        vec_index272: int = 0
        vec_276: List[int] = list()
        vec_index276: int = 0
        vec_282: List[int] = list()
        vec_index282: int = 0
        vec_287: List[int] = list()
        vec_index287: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index107 = 0
        while vec_index107 < len(vec_107):
            var_108, var_109, var_110 = vec_107[vec_index107]
            vec_index107 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_108 = var_108
            prev_state = self.table_48[tuple_108]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_48[tuple_108] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_36[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_172.append(var_108)
                    # Program VectorAppend Region
                    vec_153.append(var_108)
                    # Program VectorAppend Region
                    vec_217.append(var_108)
                    # Program VectorAppend Region
                    vec_205.append(var_108)
                    # Program VectorAppend Region
                    vec_241.append(var_108)
                    # Program VectorAppend Region
                    vec_229.append(var_108)
                    # Program VectorAppend Region
                    vec_187.append(var_108)
                # Program VectorAppend Region
                vec_134.append(var_108)
                # Program VectorAppend Region
                vec_111.append(var_108)
            # Program TupleCompare Region
            if self.var_1 == var_109:
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_38[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_38[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_262.append(var_108)
                    # Program VectorAppend Region
                    vec_148.append(var_108)
            # Program TupleCompare Region
            if self.var_4 == var_109:
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_83[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_83[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_142.append(var_108)
            # Program TransitionState Region
            tuple_108 = var_108
            prev_state = self.table_20[tuple_108]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_20[tuple_108] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_108 = var_108
            prev_state = self.table_48[tuple_108]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_48[tuple_108] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_36[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_172.append(var_108)
                    # Program VectorAppend Region
                    vec_153.append(var_108)
                    # Program VectorAppend Region
                    vec_217.append(var_108)
                    # Program VectorAppend Region
                    vec_205.append(var_108)
                    # Program VectorAppend Region
                    vec_241.append(var_108)
                    # Program VectorAppend Region
                    vec_229.append(var_108)
                    # Program VectorAppend Region
                    vec_187.append(var_108)
                # Program VectorAppend Region
                vec_134.append(var_108)
                # Program VectorAppend Region
                vec_111.append(var_108)
            # Program TupleCompare Region
            if self.var_1 == var_109:
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_38[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_38[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_262.append(var_108)
                    # Program VectorAppend Region
                    vec_148.append(var_108)
            # Program TransitionState Region
            tuple_108 = var_108
            prev_state = self.table_48[tuple_108]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_48[tuple_108] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_36[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_172.append(var_108)
                    # Program VectorAppend Region
                    vec_153.append(var_108)
                    # Program VectorAppend Region
                    vec_217.append(var_108)
                    # Program VectorAppend Region
                    vec_205.append(var_108)
                    # Program VectorAppend Region
                    vec_241.append(var_108)
                    # Program VectorAppend Region
                    vec_229.append(var_108)
                    # Program VectorAppend Region
                    vec_187.append(var_108)
                # Program VectorAppend Region
                vec_134.append(var_108)
                # Program VectorAppend Region
                vec_111.append(var_108)
            # Program TupleCompare Region
            if self.var_1 == var_109:
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_38[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_38[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_262.append(var_108)
                    # Program VectorAppend Region
                    vec_148.append(var_108)
            # Program TransitionState Region
            tuple_108 = var_108
            prev_state = self.table_48[tuple_108]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_48[tuple_108] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_36[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_172.append(var_108)
                    # Program VectorAppend Region
                    vec_153.append(var_108)
                    # Program VectorAppend Region
                    vec_217.append(var_108)
                    # Program VectorAppend Region
                    vec_205.append(var_108)
                    # Program VectorAppend Region
                    vec_241.append(var_108)
                    # Program VectorAppend Region
                    vec_229.append(var_108)
                    # Program VectorAppend Region
                    vec_187.append(var_108)
                # Program VectorAppend Region
                vec_134.append(var_108)
                # Program VectorAppend Region
                vec_111.append(var_108)
            # Program TupleCompare Region
            if self.var_1 == var_109:
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_38[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_38[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_262.append(var_108)
                    # Program VectorAppend Region
                    vec_148.append(var_108)
            # Program TransitionState Region
            tuple_108 = var_108
            prev_state = self.table_48[tuple_108]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_48[tuple_108] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_36[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_172.append(var_108)
                    # Program VectorAppend Region
                    vec_153.append(var_108)
                    # Program VectorAppend Region
                    vec_217.append(var_108)
                    # Program VectorAppend Region
                    vec_205.append(var_108)
                    # Program VectorAppend Region
                    vec_241.append(var_108)
                    # Program VectorAppend Region
                    vec_229.append(var_108)
                    # Program VectorAppend Region
                    vec_187.append(var_108)
                # Program VectorAppend Region
                vec_134.append(var_108)
                # Program VectorAppend Region
                vec_111.append(var_108)
            # Program TupleCompare Region
            if self.var_1 == var_109:
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_38[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_38[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_262.append(var_108)
                    # Program VectorAppend Region
                    vec_148.append(var_108)
            # Program TransitionState Region
            tuple_108 = var_108
            prev_state = self.table_48[tuple_108]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_48[tuple_108] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_36[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_172.append(var_108)
                    # Program VectorAppend Region
                    vec_153.append(var_108)
                    # Program VectorAppend Region
                    vec_217.append(var_108)
                    # Program VectorAppend Region
                    vec_205.append(var_108)
                    # Program VectorAppend Region
                    vec_241.append(var_108)
                    # Program VectorAppend Region
                    vec_229.append(var_108)
                    # Program VectorAppend Region
                    vec_187.append(var_108)
                # Program VectorAppend Region
                vec_134.append(var_108)
                # Program VectorAppend Region
                vec_111.append(var_108)
            # Program TupleCompare Region
            if self.var_1 == var_109:
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_38[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_38[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_262.append(var_108)
                    # Program VectorAppend Region
                    vec_148.append(var_108)
            # Program TransitionState Region
            tuple_108 = var_108
            prev_state = self.table_48[tuple_108]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_48[tuple_108] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_36[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_172.append(var_108)
                    # Program VectorAppend Region
                    vec_153.append(var_108)
                    # Program VectorAppend Region
                    vec_217.append(var_108)
                    # Program VectorAppend Region
                    vec_205.append(var_108)
                    # Program VectorAppend Region
                    vec_241.append(var_108)
                    # Program VectorAppend Region
                    vec_229.append(var_108)
                    # Program VectorAppend Region
                    vec_187.append(var_108)
                # Program VectorAppend Region
                vec_134.append(var_108)
                # Program VectorAppend Region
                vec_111.append(var_108)
            # Program TupleCompare Region
            if self.var_1 == var_109:
                # Program TransitionState Region
                tuple_108 = var_108
                prev_state = self.table_38[tuple_108]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_38[tuple_108] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_262.append(var_108)
                    # Program VectorAppend Region
                    vec_148.append(var_108)
        # Program VectorUnique Region
        vec_111 = list(set(vec_111))
        vec_index111 = 0
        # Program TableJoin Region
        while vec_index111 < len(vec_111):
            var_113 = vec_111[vec_index111]
            vec_index111 += 1
            if var_113 in self.index_114:
                if var_113 in self.index_115:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_113 = var_113
                    prev_state = self.table_18[tuple_113]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_113] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_276.append(var_113)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_117: int
                        scan_index_117: int = 0
                        scan_tuple_117_vec: List[int] = self.index_116[var_113]
                        while scan_index_117 < len(scan_tuple_117_vec):
                            scan_tuple_117 = scan_tuple_117_vec[scan_index_117]
                            scan_index_117 += 1
                            vec_117.append(scan_tuple_117)
                        # Program VectorLoop Region
                        vec_index117 = 0
                        while vec_index117 < len(vec_117):
                            var_118 = vec_117[vec_index117]
                            vec_index117 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_113_118 = (var_113, var_118)
                            prev_state = self.table_27[tuple_113_118]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_113_118] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_113, var_118)

                                # Program Call Region
                                ret = self.proc_123_(var_113, var_118)

                        # Program TransitionState Region
                        tuple_113_113 = (var_113, var_113)
                        prev_state = self.table_6[tuple_113_113]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_113_113] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_113_113[1]].append(tuple_113_113[0])
                                self.index_756[tuple_113_113[0]].append(tuple_113_113[1])
                            # Program VectorAppend Region
                            vec_131.append((var_113, var_113))
        # Program VectorClear Region
        del vec_111[:]
        vec_index111 = 0
        # Program VectorUnique Region
        vec_134 = list(set(vec_134))
        vec_index134 = 0
        # Program TableJoin Region
        while vec_index134 < len(vec_134):
            var_136 = vec_134[vec_index134]
            vec_index134 += 1
            if var_136 in self.index_137:
                if var_136 in self.index_115:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_136 = var_136
                    prev_state = self.table_18[tuple_136]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_136] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_276.append(var_136)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_138: int
                        scan_index_138: int = 0
                        scan_tuple_138_vec: List[int] = self.index_116[var_136]
                        while scan_index_138 < len(scan_tuple_138_vec):
                            scan_tuple_138 = scan_tuple_138_vec[scan_index_138]
                            scan_index_138 += 1
                            vec_138.append(scan_tuple_138)
                        # Program VectorLoop Region
                        vec_index138 = 0
                        while vec_index138 < len(vec_138):
                            var_139 = vec_138[vec_index138]
                            vec_index138 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_136_139 = (var_136, var_139)
                            prev_state = self.table_27[tuple_136_139]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_136_139] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_136, var_139)

                                # Program Call Region
                                ret = self.proc_123_(var_136, var_139)

                        # Program TransitionState Region
                        tuple_136_136 = (var_136, var_136)
                        prev_state = self.table_6[tuple_136_136]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_136_136] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_136_136[1]].append(tuple_136_136[0])
                                self.index_756[tuple_136_136[0]].append(tuple_136_136[1])
                            # Program VectorAppend Region
                            vec_131.append((var_136, var_136))
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
            if var_144 in self.index_145:
                tuple_143_1_index: int = 0
                tuple_143_1_vec: List[int] = self.index_146[var_144]
                while tuple_143_1_index < len(tuple_143_1_vec):
                    tuple_143_1 = tuple_143_1_vec[tuple_143_1_index]
                    tuple_143_1_index += 1
                    var_147 = tuple_143_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_144_147 = (var_144, var_147)
                    prev_state = self.table_85[tuple_144_147]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_85[tuple_144_147] = 1 | 4
                        if not present_bit:
                            self.index_184[tuple_144_147[1]].append(tuple_144_147[0])
                        # Program VectorAppend Region
                        vec_180.append(var_147)
        # Program VectorClear Region
        del vec_142[:]
        vec_index142 = 0
        # Program VectorUnique Region
        vec_148 = list(set(vec_148))
        vec_index148 = 0
        # Program TableJoin Region
        while vec_index148 < len(vec_148):
            var_150 = vec_148[vec_index148]
            vec_index148 += 1
            if var_150 in self.index_151:
                tuple_149_1_index: int = 0
                tuple_149_1_vec: List[int] = self.index_146[var_150]
                while tuple_149_1_index < len(tuple_149_1_vec):
                    tuple_149_1 = tuple_149_1_vec[tuple_149_1_index]
                    tuple_149_1_index += 1
                    var_152 = tuple_149_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_150_152 = (var_150, var_152)
                    prev_state = self.table_77[tuple_150_152]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_77[tuple_150_152] = 1 | 4
                        if not present_bit:
                            self.index_202[tuple_150_152[1]].append(tuple_150_152[0])
                        # Program VectorAppend Region
                        vec_199.append(var_152)
        # Program VectorClear Region
        del vec_148[:]
        vec_index148 = 0
        # Program VectorUnique Region
        vec_153 = list(set(vec_153))
        vec_index153 = 0
        # Program TableJoin Region
        while vec_index153 < len(vec_153):
            var_155 = vec_153[vec_index153]
            vec_index153 += 1
            tuple_154_0_index: int = 0
            tuple_154_0_vec: List[Tuple[int, int]] = self.index_156[var_155]
            while tuple_154_0_index < len(tuple_154_0_vec):
                tuple_154_0 = tuple_154_0_vec[tuple_154_0_index]
                tuple_154_0_index += 1
                var_158 = tuple_154_0[0]
                var_159 = tuple_154_0[1]
                if var_155 in self.index_157:
                    # Program TransitionState Region
                    var_158 = self._resolve_edgetype(var_158)
                    tuple_159_155_158 = (var_159, var_155, var_158)
                    prev_state = self.table_9[tuple_159_155_158]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_159_155_158] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_159_155_158[0], tuple_159_155_158[1])].append(tuple_159_155_158[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_155_159 = (var_155, var_159)
                        prev_state = self.table_27[tuple_155_159]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_155_159] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_155_159[0]].append(tuple_155_159[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_155)
                        if not ret:
                            # Program TransitionState Region
                            tuple_155_159 = (var_155, var_159)
                            prev_state = self.table_27[tuple_155_159]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_155_159] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_155_159[0]].append(tuple_155_159[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_159, var_155)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_159_155 = (var_159, var_155)
                                    prev_state = self.table_52[tuple_159_155]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_159_155] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_159_155[0]].append(tuple_159_155[1])
                                            self.index_778[tuple_159_155[1]].append(tuple_159_155[0])
                                        # Program VectorAppend Region
                                        vec_287.append(var_159)
                                # Program TransitionState Region
                                tuple_159_155 = (var_159, var_155)
                                prev_state = self.table_15[tuple_159_155]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_159_155] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_159_155[0]].append(tuple_159_155[1])
                        # Program TransitionState Region
                        tuple_159_155 = (var_159, var_155)
                        prev_state = self.table_94[tuple_159_155]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_159_155] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_159_155[1]].append(tuple_159_155[0])
                            # Program VectorAppend Region
                            vec_276.append(var_155)
                        # Program TransitionState Region
                        tuple_155 = var_155
                        prev_state = self.table_32[tuple_155]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_155] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_253.append(var_155)
                        # Program TupleCompare Region
                        if self.var_0 == var_158:
                            # Program TransitionState Region
                            tuple_155 = var_155
                            prev_state = self.table_18[tuple_155]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_155] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_276.append(var_155)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_168: int
                                scan_index_168: int = 0
                                scan_tuple_168_vec: List[int] = self.index_116[var_155]
                                while scan_index_168 < len(scan_tuple_168_vec):
                                    scan_tuple_168 = scan_tuple_168_vec[scan_index_168]
                                    scan_index_168 += 1
                                    vec_168.append(scan_tuple_168)
                                # Program VectorLoop Region
                                vec_index168 = 0
                                while vec_index168 < len(vec_168):
                                    var_169 = vec_168[vec_index168]
                                    vec_index168 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_155_169 = (var_155, var_169)
                                    prev_state = self.table_27[tuple_155_169]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_155_169] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_155, var_169)

                                        # Program Call Region
                                        ret = self.proc_123_(var_155, var_169)

                                # Program TransitionState Region
                                tuple_155_155 = (var_155, var_155)
                                prev_state = self.table_6[tuple_155_155]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_155_155] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_155_155[1]].append(tuple_155_155[0])
                                        self.index_756[tuple_155_155[0]].append(tuple_155_155[1])
                                    # Program VectorAppend Region
                                    vec_131.append((var_155, var_155))
                        # Program TupleCompare Region
                        if self.var_2 == var_158:
                            # Program TransitionState Region
                            tuple_159_155 = (var_159, var_155)
                            prev_state = self.table_40[tuple_159_155]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_159_155] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_159_155[0]].append(tuple_159_155[1])
                                # Program VectorAppend Region
                                vec_262.append(var_159)
        # Program VectorClear Region
        del vec_153[:]
        vec_index153 = 0
        # Program VectorUnique Region
        vec_172 = list(set(vec_172))
        vec_index172 = 0
        # Program TableJoin Region
        while vec_index172 < len(vec_172):
            var_174 = vec_172[vec_index172]
            vec_index172 += 1
            if var_174 in self.index_175:
                if var_174 in self.index_157:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_174 = var_174
                    prev_state = self.table_18[tuple_174]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_174] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_276.append(var_174)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_176: int
                        scan_index_176: int = 0
                        scan_tuple_176_vec: List[int] = self.index_116[var_174]
                        while scan_index_176 < len(scan_tuple_176_vec):
                            scan_tuple_176 = scan_tuple_176_vec[scan_index_176]
                            scan_index_176 += 1
                            vec_176.append(scan_tuple_176)
                        # Program VectorLoop Region
                        vec_index176 = 0
                        while vec_index176 < len(vec_176):
                            var_177 = vec_176[vec_index176]
                            vec_index176 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_174_177 = (var_174, var_177)
                            prev_state = self.table_27[tuple_174_177]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_174_177] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_174, var_177)

                                # Program Call Region
                                ret = self.proc_123_(var_174, var_177)

                        # Program TransitionState Region
                        tuple_174_174 = (var_174, var_174)
                        prev_state = self.table_6[tuple_174_174]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_174_174] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_174_174[1]].append(tuple_174_174[0])
                                self.index_756[tuple_174_174[0]].append(tuple_174_174[1])
                            # Program VectorAppend Region
                            vec_131.append((var_174, var_174))
        # Program VectorClear Region
        del vec_172[:]
        vec_index172 = 0
        # Program VectorUnique Region
        vec_180 = list(set(vec_180))
        vec_index180 = 0
        # Program TableJoin Region
        while vec_index180 < len(vec_180):
            var_182 = vec_180[vec_index180]
            vec_index180 += 1
            tuple_181_0_index: int = 0
            tuple_181_0_vec: List[int] = self.index_183[var_182]
            while tuple_181_0_index < len(tuple_181_0_vec):
                tuple_181_0 = tuple_181_0_vec[tuple_181_0_index]
                tuple_181_0_index += 1
                var_185 = tuple_181_0
                tuple_181_1_index: int = 0
                tuple_181_1_vec: List[int] = self.index_184[var_182]
                while tuple_181_1_index < len(tuple_181_1_vec):
                    tuple_181_1 = tuple_181_1_vec[tuple_181_1_index]
                    tuple_181_1_index += 1
                    var_186 = tuple_181_1
                    # Program TransitionState Region
                    tuple_185_186 = (var_185, var_186)
                    prev_state = self.table_88[tuple_185_186]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_88[tuple_185_186] = 1 | 4
                        if not present_bit:
                            self.index_232[tuple_185_186[0]].append(tuple_185_186[1])
                        # Program VectorAppend Region
                        vec_229.append(var_185)
        # Program VectorClear Region
        del vec_180[:]
        vec_index180 = 0
        # Program VectorUnique Region
        vec_187 = list(set(vec_187))
        vec_index187 = 0
        # Program TableJoin Region
        while vec_index187 < len(vec_187):
            var_189 = vec_187[vec_index187]
            vec_index187 += 1
            if var_189 in self.index_157:
                tuple_188_1_index: int = 0
                tuple_188_1_vec: List[int] = self.index_190[var_189]
                while tuple_188_1_index < len(tuple_188_1_vec):
                    tuple_188_1 = tuple_188_1_vec[tuple_188_1_index]
                    tuple_188_1_index += 1
                    var_191 = tuple_188_1
                    # Program TransitionState Region
                    tuple_191_189_5 = (var_191, var_189, self.var_5)
                    prev_state = self.table_9[tuple_191_189_5]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_191_189_5] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_191_189_5[0], tuple_191_189_5[1])].append(tuple_191_189_5[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_189_191 = (var_189, var_191)
                        prev_state = self.table_27[tuple_189_191]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_189_191] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_189_191[0]].append(tuple_189_191[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_189)
                        if not ret:
                            # Program TransitionState Region
                            tuple_189_191 = (var_189, var_191)
                            prev_state = self.table_27[tuple_189_191]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_189_191] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_189_191[0]].append(tuple_189_191[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_191, var_189)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_191_189 = (var_191, var_189)
                                    prev_state = self.table_52[tuple_191_189]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_191_189] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_191_189[0]].append(tuple_191_189[1])
                                            self.index_778[tuple_191_189[1]].append(tuple_191_189[0])
                                        # Program VectorAppend Region
                                        vec_287.append(var_191)
                                # Program TransitionState Region
                                tuple_191_189 = (var_191, var_189)
                                prev_state = self.table_15[tuple_191_189]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_191_189] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_191_189[0]].append(tuple_191_189[1])
                        # Program TransitionState Region
                        tuple_191_189 = (var_191, var_189)
                        prev_state = self.table_94[tuple_191_189]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_191_189] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_191_189[1]].append(tuple_191_189[0])
                            # Program VectorAppend Region
                            vec_276.append(var_189)
                        # Program TransitionState Region
                        tuple_189 = var_189
                        prev_state = self.table_32[tuple_189]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_189] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_253.append(var_189)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_5:
                            # Program TransitionState Region
                            tuple_189 = var_189
                            prev_state = self.table_18[tuple_189]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_189] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_276.append(var_189)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_195: int
                                scan_index_195: int = 0
                                scan_tuple_195_vec: List[int] = self.index_116[var_189]
                                while scan_index_195 < len(scan_tuple_195_vec):
                                    scan_tuple_195 = scan_tuple_195_vec[scan_index_195]
                                    scan_index_195 += 1
                                    vec_195.append(scan_tuple_195)
                                # Program VectorLoop Region
                                vec_index195 = 0
                                while vec_index195 < len(vec_195):
                                    var_196 = vec_195[vec_index195]
                                    vec_index195 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_189_196 = (var_189, var_196)
                                    prev_state = self.table_27[tuple_189_196]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_189_196] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_189, var_196)

                                        # Program Call Region
                                        ret = self.proc_123_(var_189, var_196)

                                # Program TransitionState Region
                                tuple_189_189 = (var_189, var_189)
                                prev_state = self.table_6[tuple_189_189]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_189_189] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_189_189[1]].append(tuple_189_189[0])
                                        self.index_756[tuple_189_189[0]].append(tuple_189_189[1])
                                    # Program VectorAppend Region
                                    vec_131.append((var_189, var_189))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_5:
                            # Program TransitionState Region
                            tuple_191_189 = (var_191, var_189)
                            prev_state = self.table_40[tuple_191_189]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_191_189] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_191_189[0]].append(tuple_191_189[1])
                                # Program VectorAppend Region
                                vec_262.append(var_191)
        # Program VectorClear Region
        del vec_187[:]
        vec_index187 = 0
        # Program VectorUnique Region
        vec_199 = list(set(vec_199))
        vec_index199 = 0
        # Program TableJoin Region
        while vec_index199 < len(vec_199):
            var_201 = vec_199[vec_index199]
            vec_index199 += 1
            tuple_200_0_index: int = 0
            tuple_200_0_vec: List[int] = self.index_183[var_201]
            while tuple_200_0_index < len(tuple_200_0_vec):
                tuple_200_0 = tuple_200_0_vec[tuple_200_0_index]
                tuple_200_0_index += 1
                var_203 = tuple_200_0
                tuple_200_1_index: int = 0
                tuple_200_1_vec: List[int] = self.index_202[var_201]
                while tuple_200_1_index < len(tuple_200_1_vec):
                    tuple_200_1 = tuple_200_1_vec[tuple_200_1_index]
                    tuple_200_1_index += 1
                    var_204 = tuple_200_1
                    # Program TransitionState Region
                    tuple_203_204 = (var_203, var_204)
                    prev_state = self.table_80[tuple_203_204]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_80[tuple_203_204] = 1 | 4
                        if not present_bit:
                            self.index_244[tuple_203_204[0]].append(tuple_203_204[1])
                        # Program VectorAppend Region
                        vec_241.append(var_203)
        # Program VectorClear Region
        del vec_199[:]
        vec_index199 = 0
        # Program VectorUnique Region
        vec_205 = list(set(vec_205))
        vec_index205 = 0
        # Program TableJoin Region
        while vec_index205 < len(vec_205):
            var_207 = vec_205[vec_index205]
            vec_index205 += 1
            if var_207 in self.index_157:
                tuple_206_1_index: int = 0
                tuple_206_1_vec: List[int] = self.index_208[var_207]
                while tuple_206_1_index < len(tuple_206_1_vec):
                    tuple_206_1 = tuple_206_1_vec[tuple_206_1_index]
                    tuple_206_1_index += 1
                    var_209 = tuple_206_1
                    # Program TransitionState Region
                    tuple_209_207_3 = (var_209, var_207, self.var_3)
                    prev_state = self.table_9[tuple_209_207_3]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_209_207_3] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_209_207_3[0], tuple_209_207_3[1])].append(tuple_209_207_3[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_207_209 = (var_207, var_209)
                        prev_state = self.table_27[tuple_207_209]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_207_209] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_207_209[0]].append(tuple_207_209[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_207)
                        if not ret:
                            # Program TransitionState Region
                            tuple_207_209 = (var_207, var_209)
                            prev_state = self.table_27[tuple_207_209]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_207_209] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_207_209[0]].append(tuple_207_209[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_209, var_207)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_209_207 = (var_209, var_207)
                                    prev_state = self.table_52[tuple_209_207]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_209_207] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_209_207[0]].append(tuple_209_207[1])
                                            self.index_778[tuple_209_207[1]].append(tuple_209_207[0])
                                        # Program VectorAppend Region
                                        vec_287.append(var_209)
                                # Program TransitionState Region
                                tuple_209_207 = (var_209, var_207)
                                prev_state = self.table_15[tuple_209_207]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_209_207] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_209_207[0]].append(tuple_209_207[1])
                        # Program TransitionState Region
                        tuple_209_207 = (var_209, var_207)
                        prev_state = self.table_94[tuple_209_207]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_209_207] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_209_207[1]].append(tuple_209_207[0])
                            # Program VectorAppend Region
                            vec_276.append(var_207)
                        # Program TransitionState Region
                        tuple_207 = var_207
                        prev_state = self.table_32[tuple_207]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_207] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_253.append(var_207)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_3:
                            # Program TransitionState Region
                            tuple_207 = var_207
                            prev_state = self.table_18[tuple_207]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_207] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_276.append(var_207)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_213: int
                                scan_index_213: int = 0
                                scan_tuple_213_vec: List[int] = self.index_116[var_207]
                                while scan_index_213 < len(scan_tuple_213_vec):
                                    scan_tuple_213 = scan_tuple_213_vec[scan_index_213]
                                    scan_index_213 += 1
                                    vec_213.append(scan_tuple_213)
                                # Program VectorLoop Region
                                vec_index213 = 0
                                while vec_index213 < len(vec_213):
                                    var_214 = vec_213[vec_index213]
                                    vec_index213 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_207_214 = (var_207, var_214)
                                    prev_state = self.table_27[tuple_207_214]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_207_214] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_207, var_214)

                                        # Program Call Region
                                        ret = self.proc_123_(var_207, var_214)

                                # Program TransitionState Region
                                tuple_207_207 = (var_207, var_207)
                                prev_state = self.table_6[tuple_207_207]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_207_207] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_207_207[1]].append(tuple_207_207[0])
                                        self.index_756[tuple_207_207[0]].append(tuple_207_207[1])
                                    # Program VectorAppend Region
                                    vec_131.append((var_207, var_207))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_3:
                            # Program TransitionState Region
                            tuple_209_207 = (var_209, var_207)
                            prev_state = self.table_40[tuple_209_207]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_209_207] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_209_207[0]].append(tuple_209_207[1])
                                # Program VectorAppend Region
                                vec_262.append(var_209)
        # Program VectorClear Region
        del vec_205[:]
        vec_index205 = 0
        # Program VectorUnique Region
        vec_217 = list(set(vec_217))
        vec_index217 = 0
        # Program TableJoin Region
        while vec_index217 < len(vec_217):
            var_219 = vec_217[vec_index217]
            vec_index217 += 1
            if var_219 in self.index_157:
                tuple_218_1_index: int = 0
                tuple_218_1_vec: List[int] = self.index_220[var_219]
                while tuple_218_1_index < len(tuple_218_1_vec):
                    tuple_218_1 = tuple_218_1_vec[tuple_218_1_index]
                    tuple_218_1_index += 1
                    var_221 = tuple_218_1
                    # Program TransitionState Region
                    tuple_221_219_0 = (var_221, var_219, self.var_0)
                    prev_state = self.table_9[tuple_221_219_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_221_219_0] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_221_219_0[0], tuple_221_219_0[1])].append(tuple_221_219_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_219_221 = (var_219, var_221)
                        prev_state = self.table_27[tuple_219_221]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_219_221] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_219_221[0]].append(tuple_219_221[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_219)
                        if not ret:
                            # Program TransitionState Region
                            tuple_219_221 = (var_219, var_221)
                            prev_state = self.table_27[tuple_219_221]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_219_221] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_219_221[0]].append(tuple_219_221[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_221, var_219)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_221_219 = (var_221, var_219)
                                    prev_state = self.table_52[tuple_221_219]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_221_219] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_221_219[0]].append(tuple_221_219[1])
                                            self.index_778[tuple_221_219[1]].append(tuple_221_219[0])
                                        # Program VectorAppend Region
                                        vec_287.append(var_221)
                                # Program TransitionState Region
                                tuple_221_219 = (var_221, var_219)
                                prev_state = self.table_15[tuple_221_219]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_221_219] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_221_219[0]].append(tuple_221_219[1])
                        # Program TransitionState Region
                        tuple_221_219 = (var_221, var_219)
                        prev_state = self.table_94[tuple_221_219]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_221_219] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_221_219[1]].append(tuple_221_219[0])
                            # Program VectorAppend Region
                            vec_276.append(var_219)
                        # Program TransitionState Region
                        tuple_219 = var_219
                        prev_state = self.table_32[tuple_219]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_219] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_253.append(var_219)
                        # Program TransitionState Region
                        tuple_219 = var_219
                        prev_state = self.table_18[tuple_219]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_219] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_276.append(var_219)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_225: int
                            scan_index_225: int = 0
                            scan_tuple_225_vec: List[int] = self.index_116[var_219]
                            while scan_index_225 < len(scan_tuple_225_vec):
                                scan_tuple_225 = scan_tuple_225_vec[scan_index_225]
                                scan_index_225 += 1
                                vec_225.append(scan_tuple_225)
                            # Program VectorLoop Region
                            vec_index225 = 0
                            while vec_index225 < len(vec_225):
                                var_226 = vec_225[vec_index225]
                                vec_index225 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_219_226 = (var_219, var_226)
                                prev_state = self.table_27[tuple_219_226]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_219_226] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_119_(var_219, var_226)

                                    # Program Call Region
                                    ret = self.proc_123_(var_219, var_226)

                            # Program TransitionState Region
                            tuple_219_219 = (var_219, var_219)
                            prev_state = self.table_6[tuple_219_219]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_219_219] = 1 | 4
                                if not present_bit:
                                    self.index_290[tuple_219_219[1]].append(tuple_219_219[0])
                                    self.index_756[tuple_219_219[0]].append(tuple_219_219[1])
                                # Program VectorAppend Region
                                vec_131.append((var_219, var_219))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_221_219 = (var_221, var_219)
                            prev_state = self.table_40[tuple_221_219]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_221_219] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_221_219[0]].append(tuple_221_219[1])
                                # Program VectorAppend Region
                                vec_262.append(var_221)
        # Program VectorClear Region
        del vec_217[:]
        vec_index217 = 0
        # Program VectorUnique Region
        vec_229 = list(set(vec_229))
        vec_index229 = 0
        # Program TableJoin Region
        while vec_index229 < len(vec_229):
            var_231 = vec_229[vec_index229]
            vec_index229 += 1
            if var_231 in self.index_157:
                tuple_230_1_index: int = 0
                tuple_230_1_vec: List[int] = self.index_232[var_231]
                while tuple_230_1_index < len(tuple_230_1_vec):
                    tuple_230_1 = tuple_230_1_vec[tuple_230_1_index]
                    tuple_230_1_index += 1
                    var_233 = tuple_230_1
                    # Program TransitionState Region
                    tuple_233_231_0 = (var_233, var_231, self.var_0)
                    prev_state = self.table_9[tuple_233_231_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_233_231_0] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_233_231_0[0], tuple_233_231_0[1])].append(tuple_233_231_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_231_233 = (var_231, var_233)
                        prev_state = self.table_27[tuple_231_233]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_231_233] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_231_233[0]].append(tuple_231_233[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_231)
                        if not ret:
                            # Program TransitionState Region
                            tuple_231_233 = (var_231, var_233)
                            prev_state = self.table_27[tuple_231_233]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_231_233] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_231_233[0]].append(tuple_231_233[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_233, var_231)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_233_231 = (var_233, var_231)
                                    prev_state = self.table_52[tuple_233_231]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_233_231] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_233_231[0]].append(tuple_233_231[1])
                                            self.index_778[tuple_233_231[1]].append(tuple_233_231[0])
                                        # Program VectorAppend Region
                                        vec_287.append(var_233)
                                # Program TransitionState Region
                                tuple_233_231 = (var_233, var_231)
                                prev_state = self.table_15[tuple_233_231]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_233_231] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_233_231[0]].append(tuple_233_231[1])
                        # Program TransitionState Region
                        tuple_233_231 = (var_233, var_231)
                        prev_state = self.table_94[tuple_233_231]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_233_231] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_233_231[1]].append(tuple_233_231[0])
                            # Program VectorAppend Region
                            vec_276.append(var_231)
                        # Program TransitionState Region
                        tuple_231 = var_231
                        prev_state = self.table_32[tuple_231]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_231] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_253.append(var_231)
                        # Program TransitionState Region
                        tuple_231 = var_231
                        prev_state = self.table_18[tuple_231]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_231] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_276.append(var_231)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_237: int
                            scan_index_237: int = 0
                            scan_tuple_237_vec: List[int] = self.index_116[var_231]
                            while scan_index_237 < len(scan_tuple_237_vec):
                                scan_tuple_237 = scan_tuple_237_vec[scan_index_237]
                                scan_index_237 += 1
                                vec_237.append(scan_tuple_237)
                            # Program VectorLoop Region
                            vec_index237 = 0
                            while vec_index237 < len(vec_237):
                                var_238 = vec_237[vec_index237]
                                vec_index237 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_231_238 = (var_231, var_238)
                                prev_state = self.table_27[tuple_231_238]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_231_238] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_119_(var_231, var_238)

                                    # Program Call Region
                                    ret = self.proc_123_(var_231, var_238)

                            # Program TransitionState Region
                            tuple_231_231 = (var_231, var_231)
                            prev_state = self.table_6[tuple_231_231]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_231_231] = 1 | 4
                                if not present_bit:
                                    self.index_290[tuple_231_231[1]].append(tuple_231_231[0])
                                    self.index_756[tuple_231_231[0]].append(tuple_231_231[1])
                                # Program VectorAppend Region
                                vec_131.append((var_231, var_231))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_233_231 = (var_233, var_231)
                            prev_state = self.table_40[tuple_233_231]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_233_231] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_233_231[0]].append(tuple_233_231[1])
                                # Program VectorAppend Region
                                vec_262.append(var_233)
        # Program VectorClear Region
        del vec_229[:]
        vec_index229 = 0
        # Program VectorUnique Region
        vec_241 = list(set(vec_241))
        vec_index241 = 0
        # Program TableJoin Region
        while vec_index241 < len(vec_241):
            var_243 = vec_241[vec_index241]
            vec_index241 += 1
            if var_243 in self.index_157:
                tuple_242_1_index: int = 0
                tuple_242_1_vec: List[int] = self.index_244[var_243]
                while tuple_242_1_index < len(tuple_242_1_vec):
                    tuple_242_1 = tuple_242_1_vec[tuple_242_1_index]
                    tuple_242_1_index += 1
                    var_245 = tuple_242_1
                    # Program TransitionState Region
                    tuple_245_243_2 = (var_245, var_243, self.var_2)
                    prev_state = self.table_9[tuple_245_243_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_245_243_2] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_245_243_2[0], tuple_245_243_2[1])].append(tuple_245_243_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_243_245 = (var_243, var_245)
                        prev_state = self.table_27[tuple_243_245]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_243_245] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_243_245[0]].append(tuple_243_245[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_243)
                        if not ret:
                            # Program TransitionState Region
                            tuple_243_245 = (var_243, var_245)
                            prev_state = self.table_27[tuple_243_245]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_243_245] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_243_245[0]].append(tuple_243_245[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_245, var_243)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_245_243 = (var_245, var_243)
                                    prev_state = self.table_52[tuple_245_243]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_245_243] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_245_243[0]].append(tuple_245_243[1])
                                            self.index_778[tuple_245_243[1]].append(tuple_245_243[0])
                                        # Program VectorAppend Region
                                        vec_287.append(var_245)
                                # Program TransitionState Region
                                tuple_245_243 = (var_245, var_243)
                                prev_state = self.table_15[tuple_245_243]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_245_243] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_245_243[0]].append(tuple_245_243[1])
                        # Program TransitionState Region
                        tuple_245_243 = (var_245, var_243)
                        prev_state = self.table_94[tuple_245_243]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_245_243] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_245_243[1]].append(tuple_245_243[0])
                            # Program VectorAppend Region
                            vec_276.append(var_243)
                        # Program TransitionState Region
                        tuple_243 = var_243
                        prev_state = self.table_32[tuple_243]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_243] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_253.append(var_243)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_243 = var_243
                            prev_state = self.table_18[tuple_243]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_243] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_276.append(var_243)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_249: int
                                scan_index_249: int = 0
                                scan_tuple_249_vec: List[int] = self.index_116[var_243]
                                while scan_index_249 < len(scan_tuple_249_vec):
                                    scan_tuple_249 = scan_tuple_249_vec[scan_index_249]
                                    scan_index_249 += 1
                                    vec_249.append(scan_tuple_249)
                                # Program VectorLoop Region
                                vec_index249 = 0
                                while vec_index249 < len(vec_249):
                                    var_250 = vec_249[vec_index249]
                                    vec_index249 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_243_250 = (var_243, var_250)
                                    prev_state = self.table_27[tuple_243_250]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_243_250] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_243, var_250)

                                        # Program Call Region
                                        ret = self.proc_123_(var_243, var_250)

                                # Program TransitionState Region
                                tuple_243_243 = (var_243, var_243)
                                prev_state = self.table_6[tuple_243_243]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_243_243] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_243_243[1]].append(tuple_243_243[0])
                                        self.index_756[tuple_243_243[0]].append(tuple_243_243[1])
                                    # Program VectorAppend Region
                                    vec_131.append((var_243, var_243))
                        # Program TransitionState Region
                        tuple_245_243 = (var_245, var_243)
                        prev_state = self.table_40[tuple_245_243]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_245_243] = 1 | 4
                            if not present_bit:
                                self.index_265[tuple_245_243[0]].append(tuple_245_243[1])
                            # Program VectorAppend Region
                            vec_262.append(var_245)
        # Program VectorClear Region
        del vec_241[:]
        vec_index241 = 0
        # Program VectorUnique Region
        vec_253 = list(set(vec_253))
        vec_index253 = 0
        # Program TableJoin Region
        while vec_index253 < len(vec_253):
            var_255 = vec_253[vec_index253]
            vec_index253 += 1
            if var_255 in self.index_256:
                if var_255 in self.index_257:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_255 = var_255
                    prev_state = self.table_18[tuple_255]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_255] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_276.append(var_255)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_258: int
                        scan_index_258: int = 0
                        scan_tuple_258_vec: List[int] = self.index_116[var_255]
                        while scan_index_258 < len(scan_tuple_258_vec):
                            scan_tuple_258 = scan_tuple_258_vec[scan_index_258]
                            scan_index_258 += 1
                            vec_258.append(scan_tuple_258)
                        # Program VectorLoop Region
                        vec_index258 = 0
                        while vec_index258 < len(vec_258):
                            var_259 = vec_258[vec_index258]
                            vec_index258 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_255_259 = (var_255, var_259)
                            prev_state = self.table_27[tuple_255_259]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_255_259] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_255, var_259)

                                # Program Call Region
                                ret = self.proc_123_(var_255, var_259)

                        # Program TransitionState Region
                        tuple_255_255 = (var_255, var_255)
                        prev_state = self.table_6[tuple_255_255]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_255_255] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_255_255[1]].append(tuple_255_255[0])
                                self.index_756[tuple_255_255[0]].append(tuple_255_255[1])
                            # Program VectorAppend Region
                            vec_131.append((var_255, var_255))
        # Program VectorClear Region
        del vec_253[:]
        vec_index253 = 0
        # Program VectorUnique Region
        vec_262 = list(set(vec_262))
        vec_index262 = 0
        # Program TableJoin Region
        while vec_index262 < len(vec_262):
            var_264 = vec_262[vec_index262]
            vec_index262 += 1
            if var_264 in self.index_151:
                tuple_263_1_index: int = 0
                tuple_263_1_vec: List[int] = self.index_265[var_264]
                while tuple_263_1_index < len(tuple_263_1_vec):
                    tuple_263_1 = tuple_263_1_vec[tuple_263_1_index]
                    tuple_263_1_index += 1
                    var_266 = tuple_263_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_264_266 = (var_264, var_266)
                    prev_state = self.table_43[tuple_264_266]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_43[tuple_264_266] = 1 | 4
                        if not present_bit:
                            self.index_270[tuple_264_266[1]].append(tuple_264_266[0])
                        # Program VectorAppend Region
                        vec_267.append(var_266)
        # Program VectorClear Region
        del vec_262[:]
        vec_index262 = 0
        # Program VectorUnique Region
        vec_267 = list(set(vec_267))
        vec_index267 = 0
        # Program TableJoin Region
        while vec_index267 < len(vec_267):
            var_269 = vec_267[vec_index267]
            vec_index267 += 1
            if var_269 in self.index_256:
                tuple_268_1_index: int = 0
                tuple_268_1_vec: List[int] = self.index_270[var_269]
                while tuple_268_1_index < len(tuple_268_1_vec):
                    tuple_268_1 = tuple_268_1_vec[tuple_268_1_index]
                    tuple_268_1_index += 1
                    var_271 = tuple_268_1
                    # Program TransitionState Region
                    tuple_271 = var_271
                    prev_state = self.table_18[tuple_271]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_271] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_276.append(var_271)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_272: int
                        scan_index_272: int = 0
                        scan_tuple_272_vec: List[int] = self.index_116[var_271]
                        while scan_index_272 < len(scan_tuple_272_vec):
                            scan_tuple_272 = scan_tuple_272_vec[scan_index_272]
                            scan_index_272 += 1
                            vec_272.append(scan_tuple_272)
                        # Program VectorLoop Region
                        vec_index272 = 0
                        while vec_index272 < len(vec_272):
                            var_273 = vec_272[vec_index272]
                            vec_index272 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_271_273 = (var_271, var_273)
                            prev_state = self.table_27[tuple_271_273]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_271_273] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_271, var_273)

                                # Program Call Region
                                ret = self.proc_123_(var_271, var_273)

                        # Program TransitionState Region
                        tuple_271_271 = (var_271, var_271)
                        prev_state = self.table_6[tuple_271_271]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_271_271] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_271_271[1]].append(tuple_271_271[0])
                                self.index_756[tuple_271_271[0]].append(tuple_271_271[1])
                            # Program VectorAppend Region
                            vec_131.append((var_271, var_271))
        # Program VectorClear Region
        del vec_267[:]
        vec_index267 = 0
        # Program VectorUnique Region
        vec_276 = list(set(vec_276))
        vec_index276 = 0
        # Program TableJoin Region
        while vec_index276 < len(vec_276):
            var_278 = vec_276[vec_index276]
            vec_index276 += 1
            tuple_277_0_index: int = 0
            tuple_277_0_vec: List[int] = self.index_279[var_278]
            while tuple_277_0_index < len(tuple_277_0_vec):
                tuple_277_0 = tuple_277_0_vec[tuple_277_0_index]
                tuple_277_0_index += 1
                var_281 = tuple_277_0
                if var_278 in self.index_280:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_281_278 = (var_281, var_278)
                    prev_state = self.table_97[tuple_281_278]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_281_278] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_281_278[1]].append(tuple_281_278[0])
                        # Program VectorAppend Region
                        vec_282.append(var_278)
                    # Program TransitionState Region
                    tuple_281_278 = (var_281, var_278)
                    prev_state = self.table_22[tuple_281_278]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_281_278] = 1 | 4
                        if not present_bit:
                            self.index_760[tuple_281_278[0]].append(tuple_281_278[1])
        # Program VectorClear Region
        del vec_276[:]
        vec_index276 = 0
        # Program VectorUnique Region
        vec_282 = list(set(vec_282))
        vec_index282 = 0
        # Program TableJoin Region
        while vec_index282 < len(vec_282):
            var_284 = vec_282[vec_index282]
            vec_index282 += 1
            tuple_283_0_index: int = 0
            tuple_283_0_vec: List[int] = self.index_285[var_284]
            while tuple_283_0_index < len(tuple_283_0_vec):
                tuple_283_0 = tuple_283_0_vec[tuple_283_0_index]
                tuple_283_0_index += 1
                var_286 = tuple_283_0
                if var_284 in self.index_256:
                    # Program TransitionState Region
                    tuple_286 = var_286
                    prev_state = self.table_13[tuple_286]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_286] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_282[:]
        vec_index282 = 0
        # Program VectorUnique Region
        vec_287 = list(set(vec_287))
        vec_index287 = 0
        # Program TableJoin Region
        while vec_index287 < len(vec_287):
            var_289 = vec_287[vec_index287]
            vec_index287 += 1
            tuple_288_0_index: int = 0
            tuple_288_0_vec: List[int] = self.index_290[var_289]
            while tuple_288_0_index < len(tuple_288_0_vec):
                tuple_288_0 = tuple_288_0_vec[tuple_288_0_index]
                tuple_288_0_index += 1
                var_292 = tuple_288_0
                tuple_288_1_index: int = 0
                tuple_288_1_vec: List[int] = self.index_291[var_289]
                while tuple_288_1_index < len(tuple_288_1_vec):
                    tuple_288_1 = tuple_288_1_vec[tuple_288_1_index]
                    tuple_288_1_index += 1
                    var_293 = tuple_288_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_294_(var_292, var_289)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_164_(var_289, var_293)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_299_(var_292, var_293)
                            if not ret:
                                # Program TransitionState Region
                                tuple_292_293 = (var_292, var_293)
                                prev_state = self.table_6[tuple_292_293]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_292_293] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_292_293[1]].append(tuple_292_293[0])
                                        self.index_756[tuple_292_293[0]].append(tuple_292_293[1])
                                    # Program VectorAppend Region
                                    vec_131.append((var_292, var_293))
        # Program VectorClear Region
        del vec_287[:]
        vec_index287 = 0
        # Induction Fixpoint Loop Region
        while len(vec_131):
            # Program Call Region
            param_133_0 = [vec_131]
            ret = self.proc_127_(param_133_0)
            vec_131 = param_133_0[0]

        vec_index131 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_131[:]
        vec_index131 = 0
        # Program Return Region
        return False
        return False

    def proc_119_(self, var_120: int, var_121: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_121_120 = (var_121, var_120)
        prev_state = self.table_52[tuple_121_120]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_52[tuple_121_120] = 2 | 4
            # Program Call Region
            ret = self.proc_822_(var_121, var_120)

        # Program Return Region
        return False
        return False

    def proc_123_(self, var_124: int, var_125: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_125_124 = (var_125, var_124)
        prev_state = self.table_15[tuple_125_124]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_15[tuple_125_124] = 2 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_787_(var_124, var_125)

        # Program Return Region
        return False
        return False

    def proc_127_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_128 = param_0[0]
        vec_index128: int = 0
        vec_303: List[Tuple[int, int]] = list()
        vec_index303: int = 0
        vec_306: List[int] = list()
        vec_index306: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_128, vec_303 = vec_303, vec_128
        # Program VectorLoop Region
        while vec_index303 < len(vec_303):
            var_304, var_305 = vec_303[vec_index303]
            vec_index303 += 1
            # Program VectorAppend Region
            vec_306.append(var_305)
        # Program VectorUnique Region
        vec_306 = list(set(vec_306))
        vec_index306 = 0
        # Program TableJoin Region
        while vec_index306 < len(vec_306):
            var_308 = vec_306[vec_index306]
            vec_index306 += 1
            tuple_307_0_index: int = 0
            tuple_307_0_vec: List[int] = self.index_290[var_308]
            while tuple_307_0_index < len(tuple_307_0_vec):
                tuple_307_0 = tuple_307_0_vec[tuple_307_0_index]
                tuple_307_0_index += 1
                var_309 = tuple_307_0
                tuple_307_1_index: int = 0
                tuple_307_1_vec: List[int] = self.index_291[var_308]
                while tuple_307_1_index < len(tuple_307_1_vec):
                    tuple_307_1 = tuple_307_1_vec[tuple_307_1_index]
                    tuple_307_1_index += 1
                    var_310 = tuple_307_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_294_(var_309, var_308)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_164_(var_308, var_310)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_299_(var_309, var_310)
                            if not ret:
                                # Program TransitionState Region
                                tuple_309_310 = (var_309, var_310)
                                prev_state = self.table_6[tuple_309_310]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_309_310] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_309_310[1]].append(tuple_309_310[0])
                                        self.index_756[tuple_309_310[0]].append(tuple_309_310[1])
                                    # Program VectorAppend Region
                                    vec_128.append((var_309, var_310))
        # Program VectorClear Region
        del vec_306[:]
        vec_index306 = 0
        # Program VectorClear Region
        del vec_303[:]
        vec_index303 = 0
        # Program Return Region
        param_0[0] = vec_128
        return False
        return False

    def proc_161_(self, var_162: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_18[var_162] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_162 = var_162
            prev_state = self.table_18[tuple_162]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_18[tuple_162] = 0 | 4
        # Program Return Region
        return False
        return False

    def proc_164_(self, var_165: int, var_166: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_52[(var_165, var_166)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_165_166 = (var_165, var_166)
            prev_state = self.table_52[tuple_165_166]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_52[tuple_165_166] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_787_(var_166, var_165)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_165_166 = (var_165, var_166)
                    prev_state = self.table_52[tuple_165_166]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_52[tuple_165_166] = 1 | 4
                        if not present_bit:
                            self.index_291[tuple_165_166[0]].append(tuple_165_166[1])
                            self.index_778[tuple_165_166[1]].append(tuple_165_166[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_294_(self, var_295: int, var_296: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_295, var_296)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_295_296 = (var_295, var_296)
            prev_state = self.table_6[tuple_295_296]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_295_296] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_803_(var_295, var_296)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_295_296 = (var_295, var_296)
                    prev_state = self.table_6[tuple_295_296]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_295_296] = 1 | 4
                        if not present_bit:
                            self.index_290[tuple_295_296[1]].append(tuple_295_296[0])
                            self.index_756[tuple_295_296[0]].append(tuple_295_296[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_299_(self, var_300: int, var_301: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_300, var_301)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_300_301 = (var_300, var_301)
            prev_state = self.table_6[tuple_300_301]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_300_301] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_773_(var_300, var_301)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_300_301 = (var_300, var_301)
                    prev_state = self.table_6[tuple_300_301]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_300_301] = 1 | 4
                        if not present_bit:
                            self.index_290[tuple_300_301[1]].append(tuple_300_301[0])
                            self.index_756[tuple_300_301[0]].append(tuple_300_301[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def external_symbol_2(self, vec_317: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index317: int = 0
        vec_320: List[int] = list()
        vec_index320: int = 0
        vec_328: List[int] = list()
        vec_index328: int = 0
        vec_332: List[Tuple[int, int]] = list()
        vec_index332: int = 0
        vec_335: List[int] = list()
        vec_index335: int = 0
        vec_338: List[int] = list()
        vec_index338: int = 0
        vec_342: List[int] = list()
        vec_index342: int = 0
        vec_349: List[int] = list()
        vec_index349: int = 0
        vec_353: List[int] = list()
        vec_index353: int = 0
        vec_360: List[int] = list()
        vec_index360: int = 0
        vec_364: List[int] = list()
        vec_index364: int = 0
        vec_371: List[int] = list()
        vec_index371: int = 0
        vec_375: List[int] = list()
        vec_index375: int = 0
        vec_382: List[int] = list()
        vec_index382: int = 0
        vec_386: List[int] = list()
        vec_index386: int = 0
        vec_393: List[int] = list()
        vec_index393: int = 0
        vec_397: List[int] = list()
        vec_index397: int = 0
        vec_400: List[int] = list()
        vec_index400: int = 0
        vec_404: List[int] = list()
        vec_index404: int = 0
        vec_408: List[int] = list()
        vec_index408: int = 0
        vec_412: List[int] = list()
        vec_index412: int = 0
        vec_416: List[int] = list()
        vec_index416: int = 0
        vec_420: List[int] = list()
        vec_index420: int = 0
        vec_428: List[int] = list()
        vec_index428: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index317 = 0
        while vec_index317 < len(vec_317):
            var_318, var_319 = vec_317[vec_index317]
            vec_index317 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_318 = var_318
            prev_state = self.table_30[tuple_318]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_318] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_318 = var_318
                prev_state = self.table_36[tuple_318]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_318] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_335.append(var_318)
                    # Program VectorAppend Region
                    vec_320.append(var_318)
                    # Program VectorAppend Region
                    vec_364.append(var_318)
                    # Program VectorAppend Region
                    vec_353.append(var_318)
                    # Program VectorAppend Region
                    vec_386.append(var_318)
                    # Program VectorAppend Region
                    vec_375.append(var_318)
                    # Program VectorAppend Region
                    vec_342.append(var_318)
                # Program VectorAppend Region
                vec_397.append(var_318)
                # Program VectorAppend Region
                vec_408.append(var_318)
                # Program VectorAppend Region
                vec_428.append(var_318)
            # Program TransitionState Region
            tuple_318 = var_318
            prev_state = self.table_30[tuple_318]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_318] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_318 = var_318
                prev_state = self.table_36[tuple_318]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_318] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_335.append(var_318)
                    # Program VectorAppend Region
                    vec_320.append(var_318)
                    # Program VectorAppend Region
                    vec_364.append(var_318)
                    # Program VectorAppend Region
                    vec_353.append(var_318)
                    # Program VectorAppend Region
                    vec_386.append(var_318)
                    # Program VectorAppend Region
                    vec_375.append(var_318)
                    # Program VectorAppend Region
                    vec_342.append(var_318)
                # Program VectorAppend Region
                vec_397.append(var_318)
                # Program VectorAppend Region
                vec_408.append(var_318)
                # Program VectorAppend Region
                vec_428.append(var_318)
            # Program TransitionState Region
            tuple_318 = var_318
            prev_state = self.table_30[tuple_318]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_318] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_318 = var_318
                prev_state = self.table_36[tuple_318]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_318] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_335.append(var_318)
                    # Program VectorAppend Region
                    vec_320.append(var_318)
                    # Program VectorAppend Region
                    vec_364.append(var_318)
                    # Program VectorAppend Region
                    vec_353.append(var_318)
                    # Program VectorAppend Region
                    vec_386.append(var_318)
                    # Program VectorAppend Region
                    vec_375.append(var_318)
                    # Program VectorAppend Region
                    vec_342.append(var_318)
                # Program VectorAppend Region
                vec_397.append(var_318)
                # Program VectorAppend Region
                vec_408.append(var_318)
                # Program VectorAppend Region
                vec_428.append(var_318)
            # Program TransitionState Region
            tuple_318 = var_318
            prev_state = self.table_30[tuple_318]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_30[tuple_318] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_318 = var_318
                prev_state = self.table_36[tuple_318]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_36[tuple_318] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_335.append(var_318)
                    # Program VectorAppend Region
                    vec_320.append(var_318)
                    # Program VectorAppend Region
                    vec_364.append(var_318)
                    # Program VectorAppend Region
                    vec_353.append(var_318)
                    # Program VectorAppend Region
                    vec_386.append(var_318)
                    # Program VectorAppend Region
                    vec_375.append(var_318)
                    # Program VectorAppend Region
                    vec_342.append(var_318)
                # Program VectorAppend Region
                vec_397.append(var_318)
                # Program VectorAppend Region
                vec_408.append(var_318)
                # Program VectorAppend Region
                vec_428.append(var_318)
        # Program VectorUnique Region
        vec_320 = list(set(vec_320))
        vec_index320 = 0
        # Program TableJoin Region
        while vec_index320 < len(vec_320):
            var_322 = vec_320[vec_index320]
            vec_index320 += 1
            tuple_321_0_index: int = 0
            tuple_321_0_vec: List[Tuple[int, int]] = self.index_156[var_322]
            while tuple_321_0_index < len(tuple_321_0_vec):
                tuple_321_0 = tuple_321_0_vec[tuple_321_0_index]
                tuple_321_0_index += 1
                var_323 = tuple_321_0[0]
                var_324 = tuple_321_0[1]
                if var_322 in self.index_157:
                    # Program TransitionState Region
                    var_323 = self._resolve_edgetype(var_323)
                    tuple_324_322_323 = (var_324, var_322, var_323)
                    prev_state = self.table_9[tuple_324_322_323]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_324_322_323] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_324_322_323[0], tuple_324_322_323[1])].append(tuple_324_322_323[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_322_324 = (var_322, var_324)
                        prev_state = self.table_27[tuple_322_324]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_322_324] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_322_324[0]].append(tuple_322_324[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_322)
                        if not ret:
                            # Program TransitionState Region
                            tuple_322_324 = (var_322, var_324)
                            prev_state = self.table_27[tuple_322_324]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_322_324] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_322_324[0]].append(tuple_322_324[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_324, var_322)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_324_322 = (var_324, var_322)
                                    prev_state = self.table_52[tuple_324_322]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_324_322] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_324_322[0]].append(tuple_324_322[1])
                                            self.index_778[tuple_324_322[1]].append(tuple_324_322[0])
                                        # Program VectorAppend Region
                                        vec_420.append(var_324)
                                # Program TransitionState Region
                                tuple_324_322 = (var_324, var_322)
                                prev_state = self.table_15[tuple_324_322]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_324_322] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_324_322[0]].append(tuple_324_322[1])
                        # Program TransitionState Region
                        tuple_324_322 = (var_324, var_322)
                        prev_state = self.table_94[tuple_324_322]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_324_322] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_324_322[1]].append(tuple_324_322[0])
                            # Program VectorAppend Region
                            vec_416.append(var_322)
                        # Program TransitionState Region
                        tuple_322 = var_322
                        prev_state = self.table_32[tuple_322]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_322] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_397.append(var_322)
                        # Program TupleCompare Region
                        if self.var_0 == var_323:
                            # Program TransitionState Region
                            tuple_322 = var_322
                            prev_state = self.table_18[tuple_322]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_322] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_416.append(var_322)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_328: int
                                scan_index_328: int = 0
                                scan_tuple_328_vec: List[int] = self.index_116[var_322]
                                while scan_index_328 < len(scan_tuple_328_vec):
                                    scan_tuple_328 = scan_tuple_328_vec[scan_index_328]
                                    scan_index_328 += 1
                                    vec_328.append(scan_tuple_328)
                                # Program VectorLoop Region
                                vec_index328 = 0
                                while vec_index328 < len(vec_328):
                                    var_329 = vec_328[vec_index328]
                                    vec_index328 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_322_329 = (var_322, var_329)
                                    prev_state = self.table_27[tuple_322_329]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_322_329] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_322, var_329)

                                        # Program Call Region
                                        ret = self.proc_123_(var_322, var_329)

                                # Program TransitionState Region
                                tuple_322_322 = (var_322, var_322)
                                prev_state = self.table_6[tuple_322_322]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_322_322] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_322_322[1]].append(tuple_322_322[0])
                                        self.index_756[tuple_322_322[0]].append(tuple_322_322[1])
                                    # Program VectorAppend Region
                                    vec_332.append((var_322, var_322))
                        # Program TupleCompare Region
                        if self.var_2 == var_323:
                            # Program TransitionState Region
                            tuple_324_322 = (var_324, var_322)
                            prev_state = self.table_40[tuple_324_322]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_324_322] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_324_322[0]].append(tuple_324_322[1])
                                # Program VectorAppend Region
                                vec_404.append(var_324)
        # Program VectorClear Region
        del vec_320[:]
        vec_index320 = 0
        # Program VectorUnique Region
        vec_335 = list(set(vec_335))
        vec_index335 = 0
        # Program TableJoin Region
        while vec_index335 < len(vec_335):
            var_337 = vec_335[vec_index335]
            vec_index335 += 1
            if var_337 in self.index_175:
                if var_337 in self.index_157:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_337 = var_337
                    prev_state = self.table_18[tuple_337]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_337] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_416.append(var_337)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_338: int
                        scan_index_338: int = 0
                        scan_tuple_338_vec: List[int] = self.index_116[var_337]
                        while scan_index_338 < len(scan_tuple_338_vec):
                            scan_tuple_338 = scan_tuple_338_vec[scan_index_338]
                            scan_index_338 += 1
                            vec_338.append(scan_tuple_338)
                        # Program VectorLoop Region
                        vec_index338 = 0
                        while vec_index338 < len(vec_338):
                            var_339 = vec_338[vec_index338]
                            vec_index338 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_337_339 = (var_337, var_339)
                            prev_state = self.table_27[tuple_337_339]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_337_339] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_337, var_339)

                                # Program Call Region
                                ret = self.proc_123_(var_337, var_339)

                        # Program TransitionState Region
                        tuple_337_337 = (var_337, var_337)
                        prev_state = self.table_6[tuple_337_337]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_337_337] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_337_337[1]].append(tuple_337_337[0])
                                self.index_756[tuple_337_337[0]].append(tuple_337_337[1])
                            # Program VectorAppend Region
                            vec_332.append((var_337, var_337))
        # Program VectorClear Region
        del vec_335[:]
        vec_index335 = 0
        # Program VectorUnique Region
        vec_342 = list(set(vec_342))
        vec_index342 = 0
        # Program TableJoin Region
        while vec_index342 < len(vec_342):
            var_344 = vec_342[vec_index342]
            vec_index342 += 1
            if var_344 in self.index_157:
                tuple_343_1_index: int = 0
                tuple_343_1_vec: List[int] = self.index_190[var_344]
                while tuple_343_1_index < len(tuple_343_1_vec):
                    tuple_343_1 = tuple_343_1_vec[tuple_343_1_index]
                    tuple_343_1_index += 1
                    var_345 = tuple_343_1
                    # Program TransitionState Region
                    tuple_345_344_5 = (var_345, var_344, self.var_5)
                    prev_state = self.table_9[tuple_345_344_5]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_345_344_5] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_345_344_5[0], tuple_345_344_5[1])].append(tuple_345_344_5[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_344_345 = (var_344, var_345)
                        prev_state = self.table_27[tuple_344_345]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_344_345] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_344_345[0]].append(tuple_344_345[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_344)
                        if not ret:
                            # Program TransitionState Region
                            tuple_344_345 = (var_344, var_345)
                            prev_state = self.table_27[tuple_344_345]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_344_345] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_344_345[0]].append(tuple_344_345[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_345, var_344)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_345_344 = (var_345, var_344)
                                    prev_state = self.table_52[tuple_345_344]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_345_344] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_345_344[0]].append(tuple_345_344[1])
                                            self.index_778[tuple_345_344[1]].append(tuple_345_344[0])
                                        # Program VectorAppend Region
                                        vec_420.append(var_345)
                                # Program TransitionState Region
                                tuple_345_344 = (var_345, var_344)
                                prev_state = self.table_15[tuple_345_344]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_345_344] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_345_344[0]].append(tuple_345_344[1])
                        # Program TransitionState Region
                        tuple_345_344 = (var_345, var_344)
                        prev_state = self.table_94[tuple_345_344]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_345_344] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_345_344[1]].append(tuple_345_344[0])
                            # Program VectorAppend Region
                            vec_416.append(var_344)
                        # Program TransitionState Region
                        tuple_344 = var_344
                        prev_state = self.table_32[tuple_344]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_344] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_397.append(var_344)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_5:
                            # Program TransitionState Region
                            tuple_344 = var_344
                            prev_state = self.table_18[tuple_344]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_344] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_416.append(var_344)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_349: int
                                scan_index_349: int = 0
                                scan_tuple_349_vec: List[int] = self.index_116[var_344]
                                while scan_index_349 < len(scan_tuple_349_vec):
                                    scan_tuple_349 = scan_tuple_349_vec[scan_index_349]
                                    scan_index_349 += 1
                                    vec_349.append(scan_tuple_349)
                                # Program VectorLoop Region
                                vec_index349 = 0
                                while vec_index349 < len(vec_349):
                                    var_350 = vec_349[vec_index349]
                                    vec_index349 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_344_350 = (var_344, var_350)
                                    prev_state = self.table_27[tuple_344_350]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_344_350] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_344, var_350)

                                        # Program Call Region
                                        ret = self.proc_123_(var_344, var_350)

                                # Program TransitionState Region
                                tuple_344_344 = (var_344, var_344)
                                prev_state = self.table_6[tuple_344_344]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_344_344] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_344_344[1]].append(tuple_344_344[0])
                                        self.index_756[tuple_344_344[0]].append(tuple_344_344[1])
                                    # Program VectorAppend Region
                                    vec_332.append((var_344, var_344))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_5:
                            # Program TransitionState Region
                            tuple_345_344 = (var_345, var_344)
                            prev_state = self.table_40[tuple_345_344]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_345_344] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_345_344[0]].append(tuple_345_344[1])
                                # Program VectorAppend Region
                                vec_404.append(var_345)
        # Program VectorClear Region
        del vec_342[:]
        vec_index342 = 0
        # Program VectorUnique Region
        vec_353 = list(set(vec_353))
        vec_index353 = 0
        # Program TableJoin Region
        while vec_index353 < len(vec_353):
            var_355 = vec_353[vec_index353]
            vec_index353 += 1
            if var_355 in self.index_157:
                tuple_354_1_index: int = 0
                tuple_354_1_vec: List[int] = self.index_208[var_355]
                while tuple_354_1_index < len(tuple_354_1_vec):
                    tuple_354_1 = tuple_354_1_vec[tuple_354_1_index]
                    tuple_354_1_index += 1
                    var_356 = tuple_354_1
                    # Program TransitionState Region
                    tuple_356_355_3 = (var_356, var_355, self.var_3)
                    prev_state = self.table_9[tuple_356_355_3]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_356_355_3] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_356_355_3[0], tuple_356_355_3[1])].append(tuple_356_355_3[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_355_356 = (var_355, var_356)
                        prev_state = self.table_27[tuple_355_356]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_355_356] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_355_356[0]].append(tuple_355_356[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_355)
                        if not ret:
                            # Program TransitionState Region
                            tuple_355_356 = (var_355, var_356)
                            prev_state = self.table_27[tuple_355_356]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_355_356] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_355_356[0]].append(tuple_355_356[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_356, var_355)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_356_355 = (var_356, var_355)
                                    prev_state = self.table_52[tuple_356_355]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_356_355] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_356_355[0]].append(tuple_356_355[1])
                                            self.index_778[tuple_356_355[1]].append(tuple_356_355[0])
                                        # Program VectorAppend Region
                                        vec_420.append(var_356)
                                # Program TransitionState Region
                                tuple_356_355 = (var_356, var_355)
                                prev_state = self.table_15[tuple_356_355]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_356_355] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_356_355[0]].append(tuple_356_355[1])
                        # Program TransitionState Region
                        tuple_356_355 = (var_356, var_355)
                        prev_state = self.table_94[tuple_356_355]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_356_355] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_356_355[1]].append(tuple_356_355[0])
                            # Program VectorAppend Region
                            vec_416.append(var_355)
                        # Program TransitionState Region
                        tuple_355 = var_355
                        prev_state = self.table_32[tuple_355]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_355] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_397.append(var_355)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_3:
                            # Program TransitionState Region
                            tuple_355 = var_355
                            prev_state = self.table_18[tuple_355]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_355] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_416.append(var_355)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_360: int
                                scan_index_360: int = 0
                                scan_tuple_360_vec: List[int] = self.index_116[var_355]
                                while scan_index_360 < len(scan_tuple_360_vec):
                                    scan_tuple_360 = scan_tuple_360_vec[scan_index_360]
                                    scan_index_360 += 1
                                    vec_360.append(scan_tuple_360)
                                # Program VectorLoop Region
                                vec_index360 = 0
                                while vec_index360 < len(vec_360):
                                    var_361 = vec_360[vec_index360]
                                    vec_index360 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_355_361 = (var_355, var_361)
                                    prev_state = self.table_27[tuple_355_361]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_355_361] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_355, var_361)

                                        # Program Call Region
                                        ret = self.proc_123_(var_355, var_361)

                                # Program TransitionState Region
                                tuple_355_355 = (var_355, var_355)
                                prev_state = self.table_6[tuple_355_355]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_355_355] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_355_355[1]].append(tuple_355_355[0])
                                        self.index_756[tuple_355_355[0]].append(tuple_355_355[1])
                                    # Program VectorAppend Region
                                    vec_332.append((var_355, var_355))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_3:
                            # Program TransitionState Region
                            tuple_356_355 = (var_356, var_355)
                            prev_state = self.table_40[tuple_356_355]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_356_355] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_356_355[0]].append(tuple_356_355[1])
                                # Program VectorAppend Region
                                vec_404.append(var_356)
        # Program VectorClear Region
        del vec_353[:]
        vec_index353 = 0
        # Program VectorUnique Region
        vec_364 = list(set(vec_364))
        vec_index364 = 0
        # Program TableJoin Region
        while vec_index364 < len(vec_364):
            var_366 = vec_364[vec_index364]
            vec_index364 += 1
            if var_366 in self.index_157:
                tuple_365_1_index: int = 0
                tuple_365_1_vec: List[int] = self.index_220[var_366]
                while tuple_365_1_index < len(tuple_365_1_vec):
                    tuple_365_1 = tuple_365_1_vec[tuple_365_1_index]
                    tuple_365_1_index += 1
                    var_367 = tuple_365_1
                    # Program TransitionState Region
                    tuple_367_366_0 = (var_367, var_366, self.var_0)
                    prev_state = self.table_9[tuple_367_366_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_367_366_0] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_367_366_0[0], tuple_367_366_0[1])].append(tuple_367_366_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_366_367 = (var_366, var_367)
                        prev_state = self.table_27[tuple_366_367]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_366_367] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_366_367[0]].append(tuple_366_367[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_366)
                        if not ret:
                            # Program TransitionState Region
                            tuple_366_367 = (var_366, var_367)
                            prev_state = self.table_27[tuple_366_367]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_366_367] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_366_367[0]].append(tuple_366_367[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_367, var_366)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_367_366 = (var_367, var_366)
                                    prev_state = self.table_52[tuple_367_366]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_367_366] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_367_366[0]].append(tuple_367_366[1])
                                            self.index_778[tuple_367_366[1]].append(tuple_367_366[0])
                                        # Program VectorAppend Region
                                        vec_420.append(var_367)
                                # Program TransitionState Region
                                tuple_367_366 = (var_367, var_366)
                                prev_state = self.table_15[tuple_367_366]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_367_366] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_367_366[0]].append(tuple_367_366[1])
                        # Program TransitionState Region
                        tuple_367_366 = (var_367, var_366)
                        prev_state = self.table_94[tuple_367_366]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_367_366] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_367_366[1]].append(tuple_367_366[0])
                            # Program VectorAppend Region
                            vec_416.append(var_366)
                        # Program TransitionState Region
                        tuple_366 = var_366
                        prev_state = self.table_32[tuple_366]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_366] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_397.append(var_366)
                        # Program TransitionState Region
                        tuple_366 = var_366
                        prev_state = self.table_18[tuple_366]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_366] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_416.append(var_366)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_371: int
                            scan_index_371: int = 0
                            scan_tuple_371_vec: List[int] = self.index_116[var_366]
                            while scan_index_371 < len(scan_tuple_371_vec):
                                scan_tuple_371 = scan_tuple_371_vec[scan_index_371]
                                scan_index_371 += 1
                                vec_371.append(scan_tuple_371)
                            # Program VectorLoop Region
                            vec_index371 = 0
                            while vec_index371 < len(vec_371):
                                var_372 = vec_371[vec_index371]
                                vec_index371 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_366_372 = (var_366, var_372)
                                prev_state = self.table_27[tuple_366_372]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_366_372] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_119_(var_366, var_372)

                                    # Program Call Region
                                    ret = self.proc_123_(var_366, var_372)

                            # Program TransitionState Region
                            tuple_366_366 = (var_366, var_366)
                            prev_state = self.table_6[tuple_366_366]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_366_366] = 1 | 4
                                if not present_bit:
                                    self.index_290[tuple_366_366[1]].append(tuple_366_366[0])
                                    self.index_756[tuple_366_366[0]].append(tuple_366_366[1])
                                # Program VectorAppend Region
                                vec_332.append((var_366, var_366))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_367_366 = (var_367, var_366)
                            prev_state = self.table_40[tuple_367_366]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_367_366] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_367_366[0]].append(tuple_367_366[1])
                                # Program VectorAppend Region
                                vec_404.append(var_367)
        # Program VectorClear Region
        del vec_364[:]
        vec_index364 = 0
        # Program VectorUnique Region
        vec_375 = list(set(vec_375))
        vec_index375 = 0
        # Program TableJoin Region
        while vec_index375 < len(vec_375):
            var_377 = vec_375[vec_index375]
            vec_index375 += 1
            if var_377 in self.index_157:
                tuple_376_1_index: int = 0
                tuple_376_1_vec: List[int] = self.index_232[var_377]
                while tuple_376_1_index < len(tuple_376_1_vec):
                    tuple_376_1 = tuple_376_1_vec[tuple_376_1_index]
                    tuple_376_1_index += 1
                    var_378 = tuple_376_1
                    # Program TransitionState Region
                    tuple_378_377_0 = (var_378, var_377, self.var_0)
                    prev_state = self.table_9[tuple_378_377_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_378_377_0] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_378_377_0[0], tuple_378_377_0[1])].append(tuple_378_377_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_377_378 = (var_377, var_378)
                        prev_state = self.table_27[tuple_377_378]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_377_378] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_377_378[0]].append(tuple_377_378[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_377)
                        if not ret:
                            # Program TransitionState Region
                            tuple_377_378 = (var_377, var_378)
                            prev_state = self.table_27[tuple_377_378]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_377_378] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_377_378[0]].append(tuple_377_378[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_378, var_377)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_378_377 = (var_378, var_377)
                                    prev_state = self.table_52[tuple_378_377]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_378_377] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_378_377[0]].append(tuple_378_377[1])
                                            self.index_778[tuple_378_377[1]].append(tuple_378_377[0])
                                        # Program VectorAppend Region
                                        vec_420.append(var_378)
                                # Program TransitionState Region
                                tuple_378_377 = (var_378, var_377)
                                prev_state = self.table_15[tuple_378_377]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_378_377] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_378_377[0]].append(tuple_378_377[1])
                        # Program TransitionState Region
                        tuple_378_377 = (var_378, var_377)
                        prev_state = self.table_94[tuple_378_377]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_378_377] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_378_377[1]].append(tuple_378_377[0])
                            # Program VectorAppend Region
                            vec_416.append(var_377)
                        # Program TransitionState Region
                        tuple_377 = var_377
                        prev_state = self.table_32[tuple_377]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_377] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_397.append(var_377)
                        # Program TransitionState Region
                        tuple_377 = var_377
                        prev_state = self.table_18[tuple_377]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_377] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_416.append(var_377)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_382: int
                            scan_index_382: int = 0
                            scan_tuple_382_vec: List[int] = self.index_116[var_377]
                            while scan_index_382 < len(scan_tuple_382_vec):
                                scan_tuple_382 = scan_tuple_382_vec[scan_index_382]
                                scan_index_382 += 1
                                vec_382.append(scan_tuple_382)
                            # Program VectorLoop Region
                            vec_index382 = 0
                            while vec_index382 < len(vec_382):
                                var_383 = vec_382[vec_index382]
                                vec_index382 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_377_383 = (var_377, var_383)
                                prev_state = self.table_27[tuple_377_383]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_377_383] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_119_(var_377, var_383)

                                    # Program Call Region
                                    ret = self.proc_123_(var_377, var_383)

                            # Program TransitionState Region
                            tuple_377_377 = (var_377, var_377)
                            prev_state = self.table_6[tuple_377_377]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_377_377] = 1 | 4
                                if not present_bit:
                                    self.index_290[tuple_377_377[1]].append(tuple_377_377[0])
                                    self.index_756[tuple_377_377[0]].append(tuple_377_377[1])
                                # Program VectorAppend Region
                                vec_332.append((var_377, var_377))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_378_377 = (var_378, var_377)
                            prev_state = self.table_40[tuple_378_377]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_378_377] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_378_377[0]].append(tuple_378_377[1])
                                # Program VectorAppend Region
                                vec_404.append(var_378)
        # Program VectorClear Region
        del vec_375[:]
        vec_index375 = 0
        # Program VectorUnique Region
        vec_386 = list(set(vec_386))
        vec_index386 = 0
        # Program TableJoin Region
        while vec_index386 < len(vec_386):
            var_388 = vec_386[vec_index386]
            vec_index386 += 1
            if var_388 in self.index_157:
                tuple_387_1_index: int = 0
                tuple_387_1_vec: List[int] = self.index_244[var_388]
                while tuple_387_1_index < len(tuple_387_1_vec):
                    tuple_387_1 = tuple_387_1_vec[tuple_387_1_index]
                    tuple_387_1_index += 1
                    var_389 = tuple_387_1
                    # Program TransitionState Region
                    tuple_389_388_2 = (var_389, var_388, self.var_2)
                    prev_state = self.table_9[tuple_389_388_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_389_388_2] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_389_388_2[0], tuple_389_388_2[1])].append(tuple_389_388_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_388_389 = (var_388, var_389)
                        prev_state = self.table_27[tuple_388_389]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_388_389] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_388_389[0]].append(tuple_388_389[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_388)
                        if not ret:
                            # Program TransitionState Region
                            tuple_388_389 = (var_388, var_389)
                            prev_state = self.table_27[tuple_388_389]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_388_389] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_388_389[0]].append(tuple_388_389[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_389, var_388)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_389_388 = (var_389, var_388)
                                    prev_state = self.table_52[tuple_389_388]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_389_388] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_389_388[0]].append(tuple_389_388[1])
                                            self.index_778[tuple_389_388[1]].append(tuple_389_388[0])
                                        # Program VectorAppend Region
                                        vec_420.append(var_389)
                                # Program TransitionState Region
                                tuple_389_388 = (var_389, var_388)
                                prev_state = self.table_15[tuple_389_388]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_389_388] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_389_388[0]].append(tuple_389_388[1])
                        # Program TransitionState Region
                        tuple_389_388 = (var_389, var_388)
                        prev_state = self.table_94[tuple_389_388]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_389_388] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_389_388[1]].append(tuple_389_388[0])
                            # Program VectorAppend Region
                            vec_416.append(var_388)
                        # Program TransitionState Region
                        tuple_388 = var_388
                        prev_state = self.table_32[tuple_388]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_388] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_397.append(var_388)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_388 = var_388
                            prev_state = self.table_18[tuple_388]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_388] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_416.append(var_388)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_393: int
                                scan_index_393: int = 0
                                scan_tuple_393_vec: List[int] = self.index_116[var_388]
                                while scan_index_393 < len(scan_tuple_393_vec):
                                    scan_tuple_393 = scan_tuple_393_vec[scan_index_393]
                                    scan_index_393 += 1
                                    vec_393.append(scan_tuple_393)
                                # Program VectorLoop Region
                                vec_index393 = 0
                                while vec_index393 < len(vec_393):
                                    var_394 = vec_393[vec_index393]
                                    vec_index393 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_388_394 = (var_388, var_394)
                                    prev_state = self.table_27[tuple_388_394]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_388_394] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_388, var_394)

                                        # Program Call Region
                                        ret = self.proc_123_(var_388, var_394)

                                # Program TransitionState Region
                                tuple_388_388 = (var_388, var_388)
                                prev_state = self.table_6[tuple_388_388]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_388_388] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_388_388[1]].append(tuple_388_388[0])
                                        self.index_756[tuple_388_388[0]].append(tuple_388_388[1])
                                    # Program VectorAppend Region
                                    vec_332.append((var_388, var_388))
                        # Program TransitionState Region
                        tuple_389_388 = (var_389, var_388)
                        prev_state = self.table_40[tuple_389_388]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_389_388] = 1 | 4
                            if not present_bit:
                                self.index_265[tuple_389_388[0]].append(tuple_389_388[1])
                            # Program VectorAppend Region
                            vec_404.append(var_389)
        # Program VectorClear Region
        del vec_386[:]
        vec_index386 = 0
        # Program VectorUnique Region
        vec_397 = list(set(vec_397))
        vec_index397 = 0
        # Program TableJoin Region
        while vec_index397 < len(vec_397):
            var_399 = vec_397[vec_index397]
            vec_index397 += 1
            if var_399 in self.index_256:
                if var_399 in self.index_257:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_399 = var_399
                    prev_state = self.table_18[tuple_399]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_399] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_416.append(var_399)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_400: int
                        scan_index_400: int = 0
                        scan_tuple_400_vec: List[int] = self.index_116[var_399]
                        while scan_index_400 < len(scan_tuple_400_vec):
                            scan_tuple_400 = scan_tuple_400_vec[scan_index_400]
                            scan_index_400 += 1
                            vec_400.append(scan_tuple_400)
                        # Program VectorLoop Region
                        vec_index400 = 0
                        while vec_index400 < len(vec_400):
                            var_401 = vec_400[vec_index400]
                            vec_index400 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_399_401 = (var_399, var_401)
                            prev_state = self.table_27[tuple_399_401]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_399_401] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_399, var_401)

                                # Program Call Region
                                ret = self.proc_123_(var_399, var_401)

                        # Program TransitionState Region
                        tuple_399_399 = (var_399, var_399)
                        prev_state = self.table_6[tuple_399_399]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_399_399] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_399_399[1]].append(tuple_399_399[0])
                                self.index_756[tuple_399_399[0]].append(tuple_399_399[1])
                            # Program VectorAppend Region
                            vec_332.append((var_399, var_399))
        # Program VectorClear Region
        del vec_397[:]
        vec_index397 = 0
        # Program VectorUnique Region
        vec_404 = list(set(vec_404))
        vec_index404 = 0
        # Program TableJoin Region
        while vec_index404 < len(vec_404):
            var_406 = vec_404[vec_index404]
            vec_index404 += 1
            if var_406 in self.index_151:
                tuple_405_1_index: int = 0
                tuple_405_1_vec: List[int] = self.index_265[var_406]
                while tuple_405_1_index < len(tuple_405_1_vec):
                    tuple_405_1 = tuple_405_1_vec[tuple_405_1_index]
                    tuple_405_1_index += 1
                    var_407 = tuple_405_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_406_407 = (var_406, var_407)
                    prev_state = self.table_43[tuple_406_407]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_43[tuple_406_407] = 1 | 4
                        if not present_bit:
                            self.index_270[tuple_406_407[1]].append(tuple_406_407[0])
                        # Program VectorAppend Region
                        vec_408.append(var_407)
        # Program VectorClear Region
        del vec_404[:]
        vec_index404 = 0
        # Program VectorUnique Region
        vec_408 = list(set(vec_408))
        vec_index408 = 0
        # Program TableJoin Region
        while vec_index408 < len(vec_408):
            var_410 = vec_408[vec_index408]
            vec_index408 += 1
            if var_410 in self.index_256:
                tuple_409_1_index: int = 0
                tuple_409_1_vec: List[int] = self.index_270[var_410]
                while tuple_409_1_index < len(tuple_409_1_vec):
                    tuple_409_1 = tuple_409_1_vec[tuple_409_1_index]
                    tuple_409_1_index += 1
                    var_411 = tuple_409_1
                    # Program TransitionState Region
                    tuple_411 = var_411
                    prev_state = self.table_18[tuple_411]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_411] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_416.append(var_411)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_412: int
                        scan_index_412: int = 0
                        scan_tuple_412_vec: List[int] = self.index_116[var_411]
                        while scan_index_412 < len(scan_tuple_412_vec):
                            scan_tuple_412 = scan_tuple_412_vec[scan_index_412]
                            scan_index_412 += 1
                            vec_412.append(scan_tuple_412)
                        # Program VectorLoop Region
                        vec_index412 = 0
                        while vec_index412 < len(vec_412):
                            var_413 = vec_412[vec_index412]
                            vec_index412 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_411_413 = (var_411, var_413)
                            prev_state = self.table_27[tuple_411_413]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_411_413] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_411, var_413)

                                # Program Call Region
                                ret = self.proc_123_(var_411, var_413)

                        # Program TransitionState Region
                        tuple_411_411 = (var_411, var_411)
                        prev_state = self.table_6[tuple_411_411]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_411_411] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_411_411[1]].append(tuple_411_411[0])
                                self.index_756[tuple_411_411[0]].append(tuple_411_411[1])
                            # Program VectorAppend Region
                            vec_332.append((var_411, var_411))
        # Program VectorClear Region
        del vec_408[:]
        vec_index408 = 0
        # Program VectorUnique Region
        vec_416 = list(set(vec_416))
        vec_index416 = 0
        # Program TableJoin Region
        while vec_index416 < len(vec_416):
            var_418 = vec_416[vec_index416]
            vec_index416 += 1
            tuple_417_0_index: int = 0
            tuple_417_0_vec: List[int] = self.index_279[var_418]
            while tuple_417_0_index < len(tuple_417_0_vec):
                tuple_417_0 = tuple_417_0_vec[tuple_417_0_index]
                tuple_417_0_index += 1
                var_419 = tuple_417_0
                if var_418 in self.index_280:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_419_418 = (var_419, var_418)
                    prev_state = self.table_97[tuple_419_418]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_419_418] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_419_418[1]].append(tuple_419_418[0])
                        # Program VectorAppend Region
                        vec_428.append(var_418)
                    # Program TransitionState Region
                    tuple_419_418 = (var_419, var_418)
                    prev_state = self.table_22[tuple_419_418]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_419_418] = 1 | 4
                        if not present_bit:
                            self.index_760[tuple_419_418[0]].append(tuple_419_418[1])
        # Program VectorClear Region
        del vec_416[:]
        vec_index416 = 0
        # Program VectorUnique Region
        vec_420 = list(set(vec_420))
        vec_index420 = 0
        # Program TableJoin Region
        while vec_index420 < len(vec_420):
            var_422 = vec_420[vec_index420]
            vec_index420 += 1
            tuple_421_0_index: int = 0
            tuple_421_0_vec: List[int] = self.index_290[var_422]
            while tuple_421_0_index < len(tuple_421_0_vec):
                tuple_421_0 = tuple_421_0_vec[tuple_421_0_index]
                tuple_421_0_index += 1
                var_423 = tuple_421_0
                tuple_421_1_index: int = 0
                tuple_421_1_vec: List[int] = self.index_291[var_422]
                while tuple_421_1_index < len(tuple_421_1_vec):
                    tuple_421_1 = tuple_421_1_vec[tuple_421_1_index]
                    tuple_421_1_index += 1
                    var_424 = tuple_421_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_294_(var_423, var_422)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_164_(var_422, var_424)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_299_(var_423, var_424)
                            if not ret:
                                # Program TransitionState Region
                                tuple_423_424 = (var_423, var_424)
                                prev_state = self.table_6[tuple_423_424]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_423_424] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_423_424[1]].append(tuple_423_424[0])
                                        self.index_756[tuple_423_424[0]].append(tuple_423_424[1])
                                    # Program VectorAppend Region
                                    vec_332.append((var_423, var_424))
        # Program VectorClear Region
        del vec_420[:]
        vec_index420 = 0
        # Program VectorUnique Region
        vec_428 = list(set(vec_428))
        vec_index428 = 0
        # Program TableJoin Region
        while vec_index428 < len(vec_428):
            var_430 = vec_428[vec_index428]
            vec_index428 += 1
            tuple_429_0_index: int = 0
            tuple_429_0_vec: List[int] = self.index_285[var_430]
            while tuple_429_0_index < len(tuple_429_0_vec):
                tuple_429_0 = tuple_429_0_vec[tuple_429_0_index]
                tuple_429_0_index += 1
                var_431 = tuple_429_0
                if var_430 in self.index_256:
                    # Program TransitionState Region
                    tuple_431 = var_431
                    prev_state = self.table_13[tuple_431]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_431] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_428[:]
        vec_index428 = 0
        # Induction Fixpoint Loop Region
        while len(vec_332):
            # Program Call Region
            param_334_0 = [vec_332]
            ret = self.proc_127_(param_334_0)
            vec_332 = param_334_0[0]

        vec_index332 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_332[:]
        vec_index332 = 0
        # Program Return Region
        return False
        return False

    def entrypoint_1(self, vec_433: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index433: int = 0
        vec_435: List[int] = list()
        vec_index435: int = 0
        vec_438: List[int] = list()
        vec_index438: int = 0
        vec_442: List[Tuple[int, int]] = list()
        vec_index442: int = 0
        vec_445: List[int] = list()
        vec_index445: int = 0
        vec_449: List[int] = list()
        vec_index449: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index433 = 0
        while vec_index433 < len(vec_433):
            var_434 = vec_433[vec_index433]
            vec_index433 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_434 = var_434
            prev_state = self.table_34[tuple_434]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_34[tuple_434] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_435.append(var_434)
        # Program VectorUnique Region
        vec_435 = list(set(vec_435))
        vec_index435 = 0
        # Program TableJoin Region
        while vec_index435 < len(vec_435):
            var_437 = vec_435[vec_index435]
            vec_index435 += 1
            if var_437 in self.index_175:
                if var_437 in self.index_157:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
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
                        vec_445.append(var_437)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_438: int
                        scan_index_438: int = 0
                        scan_tuple_438_vec: List[int] = self.index_116[var_437]
                        while scan_index_438 < len(scan_tuple_438_vec):
                            scan_tuple_438 = scan_tuple_438_vec[scan_index_438]
                            scan_index_438 += 1
                            vec_438.append(scan_tuple_438)
                        # Program VectorLoop Region
                        vec_index438 = 0
                        while vec_index438 < len(vec_438):
                            var_439 = vec_438[vec_index438]
                            vec_index438 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_437_439 = (var_437, var_439)
                            prev_state = self.table_27[tuple_437_439]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_437_439] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_437, var_439)

                                # Program Call Region
                                ret = self.proc_123_(var_437, var_439)

                        # Program TransitionState Region
                        tuple_437_437 = (var_437, var_437)
                        prev_state = self.table_6[tuple_437_437]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_437_437] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_437_437[1]].append(tuple_437_437[0])
                                self.index_756[tuple_437_437[0]].append(tuple_437_437[1])
                            # Program VectorAppend Region
                            vec_442.append((var_437, var_437))
        # Program VectorClear Region
        del vec_435[:]
        vec_index435 = 0
        # Program VectorUnique Region
        vec_445 = list(set(vec_445))
        vec_index445 = 0
        # Program TableJoin Region
        while vec_index445 < len(vec_445):
            var_447 = vec_445[vec_index445]
            vec_index445 += 1
            tuple_446_0_index: int = 0
            tuple_446_0_vec: List[int] = self.index_279[var_447]
            while tuple_446_0_index < len(tuple_446_0_vec):
                tuple_446_0 = tuple_446_0_vec[tuple_446_0_index]
                tuple_446_0_index += 1
                var_448 = tuple_446_0
                if var_447 in self.index_280:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_448_447 = (var_448, var_447)
                    prev_state = self.table_97[tuple_448_447]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_448_447] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_448_447[1]].append(tuple_448_447[0])
                        # Program VectorAppend Region
                        vec_449.append(var_447)
                    # Program TransitionState Region
                    tuple_448_447 = (var_448, var_447)
                    prev_state = self.table_22[tuple_448_447]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_448_447] = 1 | 4
                        if not present_bit:
                            self.index_760[tuple_448_447[0]].append(tuple_448_447[1])
        # Program VectorClear Region
        del vec_445[:]
        vec_index445 = 0
        # Program VectorUnique Region
        vec_449 = list(set(vec_449))
        vec_index449 = 0
        # Program TableJoin Region
        while vec_index449 < len(vec_449):
            var_451 = vec_449[vec_index449]
            vec_index449 += 1
            tuple_450_0_index: int = 0
            tuple_450_0_vec: List[int] = self.index_285[var_451]
            while tuple_450_0_index < len(tuple_450_0_vec):
                tuple_450_0 = tuple_450_0_vec[tuple_450_0_index]
                tuple_450_0_index += 1
                var_452 = tuple_450_0
                if var_451 in self.index_256:
                    # Program TransitionState Region
                    tuple_452 = var_452
                    prev_state = self.table_13[tuple_452]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_452] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_449[:]
        vec_index449 = 0
        # Induction Fixpoint Loop Region
        while len(vec_442):
            # Program Call Region
            param_444_0 = [vec_442]
            ret = self.proc_127_(param_444_0)
            vec_442 = param_444_0[0]

        vec_index442 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_442[:]
        vec_index442 = 0
        # Program Return Region
        return False
        return False

    def constructor_function_1(self, vec_454: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index454: int = 0
        vec_456: List[int] = list()
        vec_index456: int = 0
        vec_459: List[int] = list()
        vec_index459: int = 0
        vec_463: List[Tuple[int, int]] = list()
        vec_index463: int = 0
        vec_466: List[int] = list()
        vec_index466: int = 0
        vec_470: List[int] = list()
        vec_index470: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index454 = 0
        while vec_index454 < len(vec_454):
            var_455 = vec_454[vec_index454]
            vec_index454 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_455 = var_455
            prev_state = self.table_46[tuple_455]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_46[tuple_455] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_456.append(var_455)
        # Program VectorUnique Region
        vec_456 = list(set(vec_456))
        vec_index456 = 0
        # Program TableJoin Region
        while vec_index456 < len(vec_456):
            var_458 = vec_456[vec_index456]
            vec_index456 += 1
            if var_458 in self.index_137:
                if var_458 in self.index_115:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_458 = var_458
                    prev_state = self.table_18[tuple_458]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_458] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_466.append(var_458)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_459: int
                        scan_index_459: int = 0
                        scan_tuple_459_vec: List[int] = self.index_116[var_458]
                        while scan_index_459 < len(scan_tuple_459_vec):
                            scan_tuple_459 = scan_tuple_459_vec[scan_index_459]
                            scan_index_459 += 1
                            vec_459.append(scan_tuple_459)
                        # Program VectorLoop Region
                        vec_index459 = 0
                        while vec_index459 < len(vec_459):
                            var_460 = vec_459[vec_index459]
                            vec_index459 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_458_460 = (var_458, var_460)
                            prev_state = self.table_27[tuple_458_460]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_458_460] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_458, var_460)

                                # Program Call Region
                                ret = self.proc_123_(var_458, var_460)

                        # Program TransitionState Region
                        tuple_458_458 = (var_458, var_458)
                        prev_state = self.table_6[tuple_458_458]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_458_458] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_458_458[1]].append(tuple_458_458[0])
                                self.index_756[tuple_458_458[0]].append(tuple_458_458[1])
                            # Program VectorAppend Region
                            vec_463.append((var_458, var_458))
        # Program VectorClear Region
        del vec_456[:]
        vec_index456 = 0
        # Program VectorUnique Region
        vec_466 = list(set(vec_466))
        vec_index466 = 0
        # Program TableJoin Region
        while vec_index466 < len(vec_466):
            var_468 = vec_466[vec_index466]
            vec_index466 += 1
            tuple_467_0_index: int = 0
            tuple_467_0_vec: List[int] = self.index_279[var_468]
            while tuple_467_0_index < len(tuple_467_0_vec):
                tuple_467_0 = tuple_467_0_vec[tuple_467_0_index]
                tuple_467_0_index += 1
                var_469 = tuple_467_0
                if var_468 in self.index_280:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_469_468 = (var_469, var_468)
                    prev_state = self.table_97[tuple_469_468]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_469_468] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_469_468[1]].append(tuple_469_468[0])
                        # Program VectorAppend Region
                        vec_470.append(var_468)
                    # Program TransitionState Region
                    tuple_469_468 = (var_469, var_468)
                    prev_state = self.table_22[tuple_469_468]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_469_468] = 1 | 4
                        if not present_bit:
                            self.index_760[tuple_469_468[0]].append(tuple_469_468[1])
        # Program VectorClear Region
        del vec_466[:]
        vec_index466 = 0
        # Program VectorUnique Region
        vec_470 = list(set(vec_470))
        vec_index470 = 0
        # Program TableJoin Region
        while vec_index470 < len(vec_470):
            var_472 = vec_470[vec_index470]
            vec_index470 += 1
            tuple_471_0_index: int = 0
            tuple_471_0_vec: List[int] = self.index_285[var_472]
            while tuple_471_0_index < len(tuple_471_0_vec):
                tuple_471_0 = tuple_471_0_vec[tuple_471_0_index]
                tuple_471_0_index += 1
                var_473 = tuple_471_0
                if var_472 in self.index_256:
                    # Program TransitionState Region
                    tuple_473 = var_473
                    prev_state = self.table_13[tuple_473]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_473] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_470[:]
        vec_index470 = 0
        # Induction Fixpoint Loop Region
        while len(vec_463):
            # Program Call Region
            param_465_0 = [vec_463]
            ret = self.proc_127_(param_465_0)
            vec_463 = param_465_0[0]

        vec_index463 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_463[:]
        vec_index463 = 0
        # Program Return Region
        return False
        return False

    def destructor_function_1(self, vec_475: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index475: int = 0
        vec_477: List[int] = list()
        vec_index477: int = 0
        vec_480: List[int] = list()
        vec_index480: int = 0
        vec_484: List[Tuple[int, int]] = list()
        vec_index484: int = 0
        vec_487: List[int] = list()
        vec_index487: int = 0
        vec_491: List[int] = list()
        vec_index491: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index475 = 0
        while vec_index475 < len(vec_475):
            var_476 = vec_475[vec_index475]
            vec_index475 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_476 = var_476
            prev_state = self.table_50[tuple_476]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_50[tuple_476] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_477.append(var_476)
        # Program VectorUnique Region
        vec_477 = list(set(vec_477))
        vec_index477 = 0
        # Program TableJoin Region
        while vec_index477 < len(vec_477):
            var_479 = vec_477[vec_index477]
            vec_index477 += 1
            if var_479 in self.index_114:
                if var_479 in self.index_115:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_479 = var_479
                    prev_state = self.table_18[tuple_479]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_479] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_487.append(var_479)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_480: int
                        scan_index_480: int = 0
                        scan_tuple_480_vec: List[int] = self.index_116[var_479]
                        while scan_index_480 < len(scan_tuple_480_vec):
                            scan_tuple_480 = scan_tuple_480_vec[scan_index_480]
                            scan_index_480 += 1
                            vec_480.append(scan_tuple_480)
                        # Program VectorLoop Region
                        vec_index480 = 0
                        while vec_index480 < len(vec_480):
                            var_481 = vec_480[vec_index480]
                            vec_index480 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_479_481 = (var_479, var_481)
                            prev_state = self.table_27[tuple_479_481]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_479_481] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_479, var_481)

                                # Program Call Region
                                ret = self.proc_123_(var_479, var_481)

                        # Program TransitionState Region
                        tuple_479_479 = (var_479, var_479)
                        prev_state = self.table_6[tuple_479_479]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_479_479] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_479_479[1]].append(tuple_479_479[0])
                                self.index_756[tuple_479_479[0]].append(tuple_479_479[1])
                            # Program VectorAppend Region
                            vec_484.append((var_479, var_479))
        # Program VectorClear Region
        del vec_477[:]
        vec_index477 = 0
        # Program VectorUnique Region
        vec_487 = list(set(vec_487))
        vec_index487 = 0
        # Program TableJoin Region
        while vec_index487 < len(vec_487):
            var_489 = vec_487[vec_index487]
            vec_index487 += 1
            tuple_488_0_index: int = 0
            tuple_488_0_vec: List[int] = self.index_279[var_489]
            while tuple_488_0_index < len(tuple_488_0_vec):
                tuple_488_0 = tuple_488_0_vec[tuple_488_0_index]
                tuple_488_0_index += 1
                var_490 = tuple_488_0
                if var_489 in self.index_280:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_490_489 = (var_490, var_489)
                    prev_state = self.table_97[tuple_490_489]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_490_489] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_490_489[1]].append(tuple_490_489[0])
                        # Program VectorAppend Region
                        vec_491.append(var_489)
                    # Program TransitionState Region
                    tuple_490_489 = (var_490, var_489)
                    prev_state = self.table_22[tuple_490_489]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_490_489] = 1 | 4
                        if not present_bit:
                            self.index_760[tuple_490_489[0]].append(tuple_490_489[1])
        # Program VectorClear Region
        del vec_487[:]
        vec_index487 = 0
        # Program VectorUnique Region
        vec_491 = list(set(vec_491))
        vec_index491 = 0
        # Program TableJoin Region
        while vec_index491 < len(vec_491):
            var_493 = vec_491[vec_index491]
            vec_index491 += 1
            tuple_492_0_index: int = 0
            tuple_492_0_vec: List[int] = self.index_285[var_493]
            while tuple_492_0_index < len(tuple_492_0_vec):
                tuple_492_0 = tuple_492_0_vec[tuple_492_0_index]
                tuple_492_0_index += 1
                var_494 = tuple_492_0
                if var_493 in self.index_256:
                    # Program TransitionState Region
                    tuple_494 = var_494
                    prev_state = self.table_13[tuple_494]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_494] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_491[:]
        vec_index491 = 0
        # Induction Fixpoint Loop Region
        while len(vec_484):
            # Program Call Region
            param_486_0 = [vec_484]
            ret = self.proc_127_(param_486_0)
            vec_484 = param_486_0[0]

        vec_index484 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_484[:]
        vec_index484 = 0
        # Program Return Region
        return False
        return False

    def raw_transfer_3(self, vec_496: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index496: int = 0
        vec_500: List[Tuple[int, int]] = list()
        vec_index500: int = 0
        vec_506: List[int] = list()
        vec_index506: int = 0
        vec_513: List[int] = list()
        vec_index513: int = 0
        vec_521: List[int] = list()
        vec_index521: int = 0
        vec_525: List[Tuple[int, int]] = list()
        vec_index525: int = 0
        vec_528: List[int] = list()
        vec_index528: int = 0
        vec_535: List[int] = list()
        vec_index535: int = 0
        vec_539: List[int] = list()
        vec_index539: int = 0
        vec_546: List[int] = list()
        vec_index546: int = 0
        vec_550: List[int] = list()
        vec_index550: int = 0
        vec_557: List[int] = list()
        vec_index557: int = 0
        vec_561: List[int] = list()
        vec_index561: int = 0
        vec_564: List[int] = list()
        vec_index564: int = 0
        vec_568: List[int] = list()
        vec_index568: int = 0
        vec_572: List[int] = list()
        vec_index572: int = 0
        vec_576: List[int] = list()
        vec_index576: int = 0
        vec_580: List[int] = list()
        vec_index580: int = 0
        vec_584: List[int] = list()
        vec_index584: int = 0
        vec_588: List[int] = list()
        vec_index588: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index496 = 0
        while vec_index496 < len(vec_496):
            var_497, var_498, var_499 = vec_496[vec_index496]
            vec_index496 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if var_499 != self.var_0:
                # Program TupleCompare Region
                if var_499 != self.var_3:
                    # Program TransitionState Region
                    var_499 = self._resolve_edgetype(var_499)
                    tuple_499_497_498 = (var_499, var_497, var_498)
                    prev_state = self.table_55[tuple_499_497_498]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_55[tuple_499_497_498] = 1 | 4
                        if not present_bit:
                            self.index_156[tuple_499_497_498[2]].append((tuple_499_497_498[0], tuple_499_497_498[1]))
                        # Program VectorAppend Region
                        vec_513.append(var_498)
            # Program TupleCompare Region
            if self.var_0 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_62[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_62[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_509[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_3 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_65[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_65[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_510[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_0 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_62[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_62[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_509[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_3 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_65[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_65[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_510[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_0 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_62[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_62[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_509[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_3 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_65[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_65[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_510[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_0 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_62[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_62[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_509[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_3 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_65[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_65[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_510[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_0 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_62[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_62[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_509[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_3 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_65[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_65[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_510[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_0 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_62[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_62[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_509[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_3 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_65[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_65[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_510[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_0 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_62[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_62[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_509[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
            # Program TupleCompare Region
            if self.var_3 == var_499:
                # Program TransitionState Region
                tuple_497_498 = (var_497, var_498)
                prev_state = self.table_65[tuple_497_498]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_65[tuple_497_498] = 1 | 4
                    if not present_bit:
                        self.index_510[tuple_497_498[0]].append(tuple_497_498[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_506.append(var_497)
                    # Program VectorAppend Region
                    vec_500.append((var_497, var_498))
        # Program VectorUnique Region
        vec_500 = list(set(vec_500))
        vec_index500 = 0
        # Program TableJoin Region
        while vec_index500 < len(vec_500):
            var_502, var_503 = vec_500[vec_index500]
            vec_index500 += 1
            if (var_502, var_503) in self.index_504:
                if (var_502, var_503) in self.index_505:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_502_503 = (var_502, var_503)
                    prev_state = self.table_91[tuple_502_503]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_91[tuple_502_503] = 1 | 4
                        if not present_bit:
                            self.index_190[tuple_502_503[1]].append(tuple_502_503[0])
                        # Program VectorAppend Region
                        vec_528.append(var_503)
        # Program VectorClear Region
        del vec_500[:]
        vec_index500 = 0
        # Program VectorUnique Region
        vec_506 = list(set(vec_506))
        vec_index506 = 0
        # Program TableJoin Region
        while vec_index506 < len(vec_506):
            var_508 = vec_506[vec_index506]
            vec_index506 += 1
            tuple_507_0_index: int = 0
            tuple_507_0_vec: List[int] = self.index_509[var_508]
            while tuple_507_0_index < len(tuple_507_0_vec):
                tuple_507_0 = tuple_507_0_vec[tuple_507_0_index]
                tuple_507_0_index += 1
                var_511 = tuple_507_0
                tuple_507_1_index: int = 0
                tuple_507_1_vec: List[int] = self.index_510[var_508]
                while tuple_507_1_index < len(tuple_507_1_vec):
                    tuple_507_1 = tuple_507_1_vec[tuple_507_1_index]
                    tuple_507_1_index += 1
                    var_512 = tuple_507_1
                    # Program TupleCompare Region
                    if var_511 != var_512:
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_512_508 = (var_512, var_508)
                        prev_state = self.table_68[tuple_512_508]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_68[tuple_512_508] = 1 | 4
                            if not present_bit:
                                self.index_208[tuple_512_508[0]].append(tuple_512_508[1])
                            # Program VectorAppend Region
                            vec_550.append(var_512)
                        # Program TransitionState Region
                        tuple_511_508 = (var_511, var_508)
                        prev_state = self.table_59[tuple_511_508]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_59[tuple_511_508] = 1 | 4
                            if not present_bit:
                                self.index_220[tuple_511_508[0]].append(tuple_511_508[1])
                            # Program VectorAppend Region
                            vec_539.append(var_511)
        # Program VectorClear Region
        del vec_506[:]
        vec_index506 = 0
        # Program VectorUnique Region
        vec_513 = list(set(vec_513))
        vec_index513 = 0
        # Program TableJoin Region
        while vec_index513 < len(vec_513):
            var_515 = vec_513[vec_index513]
            vec_index513 += 1
            tuple_514_0_index: int = 0
            tuple_514_0_vec: List[Tuple[int, int]] = self.index_156[var_515]
            while tuple_514_0_index < len(tuple_514_0_vec):
                tuple_514_0 = tuple_514_0_vec[tuple_514_0_index]
                tuple_514_0_index += 1
                var_516 = tuple_514_0[0]
                var_517 = tuple_514_0[1]
                if var_515 in self.index_157:
                    # Program TransitionState Region
                    var_516 = self._resolve_edgetype(var_516)
                    tuple_517_515_516 = (var_517, var_515, var_516)
                    prev_state = self.table_9[tuple_517_515_516]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_517_515_516] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_517_515_516[0], tuple_517_515_516[1])].append(tuple_517_515_516[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_515_517 = (var_515, var_517)
                        prev_state = self.table_27[tuple_515_517]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_515_517] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_515_517[0]].append(tuple_515_517[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_515)
                        if not ret:
                            # Program TransitionState Region
                            tuple_515_517 = (var_515, var_517)
                            prev_state = self.table_27[tuple_515_517]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_515_517] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_515_517[0]].append(tuple_515_517[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_517, var_515)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_517_515 = (var_517, var_515)
                                    prev_state = self.table_52[tuple_517_515]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_517_515] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_517_515[0]].append(tuple_517_515[1])
                                            self.index_778[tuple_517_515[1]].append(tuple_517_515[0])
                                        # Program VectorAppend Region
                                        vec_588.append(var_517)
                                # Program TransitionState Region
                                tuple_517_515 = (var_517, var_515)
                                prev_state = self.table_15[tuple_517_515]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_517_515] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_517_515[0]].append(tuple_517_515[1])
                        # Program TransitionState Region
                        tuple_517_515 = (var_517, var_515)
                        prev_state = self.table_94[tuple_517_515]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_517_515] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_517_515[1]].append(tuple_517_515[0])
                            # Program VectorAppend Region
                            vec_580.append(var_515)
                        # Program TransitionState Region
                        tuple_515 = var_515
                        prev_state = self.table_32[tuple_515]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_515] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_561.append(var_515)
                        # Program TupleCompare Region
                        if self.var_0 == var_516:
                            # Program TransitionState Region
                            tuple_515 = var_515
                            prev_state = self.table_18[tuple_515]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_515] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_580.append(var_515)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_521: int
                                scan_index_521: int = 0
                                scan_tuple_521_vec: List[int] = self.index_116[var_515]
                                while scan_index_521 < len(scan_tuple_521_vec):
                                    scan_tuple_521 = scan_tuple_521_vec[scan_index_521]
                                    scan_index_521 += 1
                                    vec_521.append(scan_tuple_521)
                                # Program VectorLoop Region
                                vec_index521 = 0
                                while vec_index521 < len(vec_521):
                                    var_522 = vec_521[vec_index521]
                                    vec_index521 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_515_522 = (var_515, var_522)
                                    prev_state = self.table_27[tuple_515_522]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_515_522] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_515, var_522)

                                        # Program Call Region
                                        ret = self.proc_123_(var_515, var_522)

                                # Program TransitionState Region
                                tuple_515_515 = (var_515, var_515)
                                prev_state = self.table_6[tuple_515_515]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_515_515] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_515_515[1]].append(tuple_515_515[0])
                                        self.index_756[tuple_515_515[0]].append(tuple_515_515[1])
                                    # Program VectorAppend Region
                                    vec_525.append((var_515, var_515))
                        # Program TupleCompare Region
                        if self.var_2 == var_516:
                            # Program TransitionState Region
                            tuple_517_515 = (var_517, var_515)
                            prev_state = self.table_40[tuple_517_515]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_517_515] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_517_515[0]].append(tuple_517_515[1])
                                # Program VectorAppend Region
                                vec_568.append(var_517)
        # Program VectorClear Region
        del vec_513[:]
        vec_index513 = 0
        # Program VectorUnique Region
        vec_528 = list(set(vec_528))
        vec_index528 = 0
        # Program TableJoin Region
        while vec_index528 < len(vec_528):
            var_530 = vec_528[vec_index528]
            vec_index528 += 1
            if var_530 in self.index_157:
                tuple_529_1_index: int = 0
                tuple_529_1_vec: List[int] = self.index_190[var_530]
                while tuple_529_1_index < len(tuple_529_1_vec):
                    tuple_529_1 = tuple_529_1_vec[tuple_529_1_index]
                    tuple_529_1_index += 1
                    var_531 = tuple_529_1
                    # Program TransitionState Region
                    tuple_531_530_5 = (var_531, var_530, self.var_5)
                    prev_state = self.table_9[tuple_531_530_5]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_531_530_5] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_531_530_5[0], tuple_531_530_5[1])].append(tuple_531_530_5[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_530_531 = (var_530, var_531)
                        prev_state = self.table_27[tuple_530_531]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_530_531] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_530_531[0]].append(tuple_530_531[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_530)
                        if not ret:
                            # Program TransitionState Region
                            tuple_530_531 = (var_530, var_531)
                            prev_state = self.table_27[tuple_530_531]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_530_531] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_530_531[0]].append(tuple_530_531[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_531, var_530)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_531_530 = (var_531, var_530)
                                    prev_state = self.table_52[tuple_531_530]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_531_530] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_531_530[0]].append(tuple_531_530[1])
                                            self.index_778[tuple_531_530[1]].append(tuple_531_530[0])
                                        # Program VectorAppend Region
                                        vec_588.append(var_531)
                                # Program TransitionState Region
                                tuple_531_530 = (var_531, var_530)
                                prev_state = self.table_15[tuple_531_530]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_531_530] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_531_530[0]].append(tuple_531_530[1])
                        # Program TransitionState Region
                        tuple_531_530 = (var_531, var_530)
                        prev_state = self.table_94[tuple_531_530]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_531_530] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_531_530[1]].append(tuple_531_530[0])
                            # Program VectorAppend Region
                            vec_580.append(var_530)
                        # Program TransitionState Region
                        tuple_530 = var_530
                        prev_state = self.table_32[tuple_530]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_530] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_561.append(var_530)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_5:
                            # Program TransitionState Region
                            tuple_530 = var_530
                            prev_state = self.table_18[tuple_530]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_530] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_580.append(var_530)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_535: int
                                scan_index_535: int = 0
                                scan_tuple_535_vec: List[int] = self.index_116[var_530]
                                while scan_index_535 < len(scan_tuple_535_vec):
                                    scan_tuple_535 = scan_tuple_535_vec[scan_index_535]
                                    scan_index_535 += 1
                                    vec_535.append(scan_tuple_535)
                                # Program VectorLoop Region
                                vec_index535 = 0
                                while vec_index535 < len(vec_535):
                                    var_536 = vec_535[vec_index535]
                                    vec_index535 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_530_536 = (var_530, var_536)
                                    prev_state = self.table_27[tuple_530_536]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_530_536] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_530, var_536)

                                        # Program Call Region
                                        ret = self.proc_123_(var_530, var_536)

                                # Program TransitionState Region
                                tuple_530_530 = (var_530, var_530)
                                prev_state = self.table_6[tuple_530_530]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_530_530] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_530_530[1]].append(tuple_530_530[0])
                                        self.index_756[tuple_530_530[0]].append(tuple_530_530[1])
                                    # Program VectorAppend Region
                                    vec_525.append((var_530, var_530))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_5:
                            # Program TransitionState Region
                            tuple_531_530 = (var_531, var_530)
                            prev_state = self.table_40[tuple_531_530]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_531_530] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_531_530[0]].append(tuple_531_530[1])
                                # Program VectorAppend Region
                                vec_568.append(var_531)
        # Program VectorClear Region
        del vec_528[:]
        vec_index528 = 0
        # Program VectorUnique Region
        vec_539 = list(set(vec_539))
        vec_index539 = 0
        # Program TableJoin Region
        while vec_index539 < len(vec_539):
            var_541 = vec_539[vec_index539]
            vec_index539 += 1
            if var_541 in self.index_157:
                tuple_540_1_index: int = 0
                tuple_540_1_vec: List[int] = self.index_220[var_541]
                while tuple_540_1_index < len(tuple_540_1_vec):
                    tuple_540_1 = tuple_540_1_vec[tuple_540_1_index]
                    tuple_540_1_index += 1
                    var_542 = tuple_540_1
                    # Program TransitionState Region
                    tuple_542_541_0 = (var_542, var_541, self.var_0)
                    prev_state = self.table_9[tuple_542_541_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_542_541_0] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_542_541_0[0], tuple_542_541_0[1])].append(tuple_542_541_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_541_542 = (var_541, var_542)
                        prev_state = self.table_27[tuple_541_542]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_541_542] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_541_542[0]].append(tuple_541_542[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_541)
                        if not ret:
                            # Program TransitionState Region
                            tuple_541_542 = (var_541, var_542)
                            prev_state = self.table_27[tuple_541_542]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_541_542] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_541_542[0]].append(tuple_541_542[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_542, var_541)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_542_541 = (var_542, var_541)
                                    prev_state = self.table_52[tuple_542_541]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_542_541] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_542_541[0]].append(tuple_542_541[1])
                                            self.index_778[tuple_542_541[1]].append(tuple_542_541[0])
                                        # Program VectorAppend Region
                                        vec_588.append(var_542)
                                # Program TransitionState Region
                                tuple_542_541 = (var_542, var_541)
                                prev_state = self.table_15[tuple_542_541]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_542_541] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_542_541[0]].append(tuple_542_541[1])
                        # Program TransitionState Region
                        tuple_542_541 = (var_542, var_541)
                        prev_state = self.table_94[tuple_542_541]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_542_541] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_542_541[1]].append(tuple_542_541[0])
                            # Program VectorAppend Region
                            vec_580.append(var_541)
                        # Program TransitionState Region
                        tuple_541 = var_541
                        prev_state = self.table_32[tuple_541]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_541] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_561.append(var_541)
                        # Program TransitionState Region
                        tuple_541 = var_541
                        prev_state = self.table_18[tuple_541]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_541] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_580.append(var_541)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_546: int
                            scan_index_546: int = 0
                            scan_tuple_546_vec: List[int] = self.index_116[var_541]
                            while scan_index_546 < len(scan_tuple_546_vec):
                                scan_tuple_546 = scan_tuple_546_vec[scan_index_546]
                                scan_index_546 += 1
                                vec_546.append(scan_tuple_546)
                            # Program VectorLoop Region
                            vec_index546 = 0
                            while vec_index546 < len(vec_546):
                                var_547 = vec_546[vec_index546]
                                vec_index546 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_541_547 = (var_541, var_547)
                                prev_state = self.table_27[tuple_541_547]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_541_547] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_119_(var_541, var_547)

                                    # Program Call Region
                                    ret = self.proc_123_(var_541, var_547)

                            # Program TransitionState Region
                            tuple_541_541 = (var_541, var_541)
                            prev_state = self.table_6[tuple_541_541]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_541_541] = 1 | 4
                                if not present_bit:
                                    self.index_290[tuple_541_541[1]].append(tuple_541_541[0])
                                    self.index_756[tuple_541_541[0]].append(tuple_541_541[1])
                                # Program VectorAppend Region
                                vec_525.append((var_541, var_541))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_542_541 = (var_542, var_541)
                            prev_state = self.table_40[tuple_542_541]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_542_541] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_542_541[0]].append(tuple_542_541[1])
                                # Program VectorAppend Region
                                vec_568.append(var_542)
        # Program VectorClear Region
        del vec_539[:]
        vec_index539 = 0
        # Program VectorUnique Region
        vec_550 = list(set(vec_550))
        vec_index550 = 0
        # Program TableJoin Region
        while vec_index550 < len(vec_550):
            var_552 = vec_550[vec_index550]
            vec_index550 += 1
            if var_552 in self.index_157:
                tuple_551_1_index: int = 0
                tuple_551_1_vec: List[int] = self.index_208[var_552]
                while tuple_551_1_index < len(tuple_551_1_vec):
                    tuple_551_1 = tuple_551_1_vec[tuple_551_1_index]
                    tuple_551_1_index += 1
                    var_553 = tuple_551_1
                    # Program TransitionState Region
                    tuple_553_552_3 = (var_553, var_552, self.var_3)
                    prev_state = self.table_9[tuple_553_552_3]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_553_552_3] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_553_552_3[0], tuple_553_552_3[1])].append(tuple_553_552_3[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_552_553 = (var_552, var_553)
                        prev_state = self.table_27[tuple_552_553]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_552_553] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_552_553[0]].append(tuple_552_553[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_552)
                        if not ret:
                            # Program TransitionState Region
                            tuple_552_553 = (var_552, var_553)
                            prev_state = self.table_27[tuple_552_553]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_552_553] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_552_553[0]].append(tuple_552_553[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_553, var_552)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_553_552 = (var_553, var_552)
                                    prev_state = self.table_52[tuple_553_552]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_553_552] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_553_552[0]].append(tuple_553_552[1])
                                            self.index_778[tuple_553_552[1]].append(tuple_553_552[0])
                                        # Program VectorAppend Region
                                        vec_588.append(var_553)
                                # Program TransitionState Region
                                tuple_553_552 = (var_553, var_552)
                                prev_state = self.table_15[tuple_553_552]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_553_552] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_553_552[0]].append(tuple_553_552[1])
                        # Program TransitionState Region
                        tuple_553_552 = (var_553, var_552)
                        prev_state = self.table_94[tuple_553_552]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_553_552] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_553_552[1]].append(tuple_553_552[0])
                            # Program VectorAppend Region
                            vec_580.append(var_552)
                        # Program TransitionState Region
                        tuple_552 = var_552
                        prev_state = self.table_32[tuple_552]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_552] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_561.append(var_552)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_3:
                            # Program TransitionState Region
                            tuple_552 = var_552
                            prev_state = self.table_18[tuple_552]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_552] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_580.append(var_552)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_557: int
                                scan_index_557: int = 0
                                scan_tuple_557_vec: List[int] = self.index_116[var_552]
                                while scan_index_557 < len(scan_tuple_557_vec):
                                    scan_tuple_557 = scan_tuple_557_vec[scan_index_557]
                                    scan_index_557 += 1
                                    vec_557.append(scan_tuple_557)
                                # Program VectorLoop Region
                                vec_index557 = 0
                                while vec_index557 < len(vec_557):
                                    var_558 = vec_557[vec_index557]
                                    vec_index557 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_552_558 = (var_552, var_558)
                                    prev_state = self.table_27[tuple_552_558]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_552_558] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_552, var_558)

                                        # Program Call Region
                                        ret = self.proc_123_(var_552, var_558)

                                # Program TransitionState Region
                                tuple_552_552 = (var_552, var_552)
                                prev_state = self.table_6[tuple_552_552]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_552_552] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_552_552[1]].append(tuple_552_552[0])
                                        self.index_756[tuple_552_552[0]].append(tuple_552_552[1])
                                    # Program VectorAppend Region
                                    vec_525.append((var_552, var_552))
                        # Program TupleCompare Region
                        if self.var_2 == self.var_3:
                            # Program TransitionState Region
                            tuple_553_552 = (var_553, var_552)
                            prev_state = self.table_40[tuple_553_552]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_553_552] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_553_552[0]].append(tuple_553_552[1])
                                # Program VectorAppend Region
                                vec_568.append(var_553)
        # Program VectorClear Region
        del vec_550[:]
        vec_index550 = 0
        # Program VectorUnique Region
        vec_561 = list(set(vec_561))
        vec_index561 = 0
        # Program TableJoin Region
        while vec_index561 < len(vec_561):
            var_563 = vec_561[vec_index561]
            vec_index561 += 1
            if var_563 in self.index_256:
                if var_563 in self.index_257:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_563 = var_563
                    prev_state = self.table_18[tuple_563]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_563] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_580.append(var_563)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_564: int
                        scan_index_564: int = 0
                        scan_tuple_564_vec: List[int] = self.index_116[var_563]
                        while scan_index_564 < len(scan_tuple_564_vec):
                            scan_tuple_564 = scan_tuple_564_vec[scan_index_564]
                            scan_index_564 += 1
                            vec_564.append(scan_tuple_564)
                        # Program VectorLoop Region
                        vec_index564 = 0
                        while vec_index564 < len(vec_564):
                            var_565 = vec_564[vec_index564]
                            vec_index564 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_563_565 = (var_563, var_565)
                            prev_state = self.table_27[tuple_563_565]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_563_565] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_563, var_565)

                                # Program Call Region
                                ret = self.proc_123_(var_563, var_565)

                        # Program TransitionState Region
                        tuple_563_563 = (var_563, var_563)
                        prev_state = self.table_6[tuple_563_563]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_563_563] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_563_563[1]].append(tuple_563_563[0])
                                self.index_756[tuple_563_563[0]].append(tuple_563_563[1])
                            # Program VectorAppend Region
                            vec_525.append((var_563, var_563))
        # Program VectorClear Region
        del vec_561[:]
        vec_index561 = 0
        # Program VectorUnique Region
        vec_568 = list(set(vec_568))
        vec_index568 = 0
        # Program TableJoin Region
        while vec_index568 < len(vec_568):
            var_570 = vec_568[vec_index568]
            vec_index568 += 1
            if var_570 in self.index_151:
                tuple_569_1_index: int = 0
                tuple_569_1_vec: List[int] = self.index_265[var_570]
                while tuple_569_1_index < len(tuple_569_1_vec):
                    tuple_569_1 = tuple_569_1_vec[tuple_569_1_index]
                    tuple_569_1_index += 1
                    var_571 = tuple_569_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_570_571 = (var_570, var_571)
                    prev_state = self.table_43[tuple_570_571]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_43[tuple_570_571] = 1 | 4
                        if not present_bit:
                            self.index_270[tuple_570_571[1]].append(tuple_570_571[0])
                        # Program VectorAppend Region
                        vec_572.append(var_571)
        # Program VectorClear Region
        del vec_568[:]
        vec_index568 = 0
        # Program VectorUnique Region
        vec_572 = list(set(vec_572))
        vec_index572 = 0
        # Program TableJoin Region
        while vec_index572 < len(vec_572):
            var_574 = vec_572[vec_index572]
            vec_index572 += 1
            if var_574 in self.index_256:
                tuple_573_1_index: int = 0
                tuple_573_1_vec: List[int] = self.index_270[var_574]
                while tuple_573_1_index < len(tuple_573_1_vec):
                    tuple_573_1 = tuple_573_1_vec[tuple_573_1_index]
                    tuple_573_1_index += 1
                    var_575 = tuple_573_1
                    # Program TransitionState Region
                    tuple_575 = var_575
                    prev_state = self.table_18[tuple_575]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_575] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_580.append(var_575)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_576: int
                        scan_index_576: int = 0
                        scan_tuple_576_vec: List[int] = self.index_116[var_575]
                        while scan_index_576 < len(scan_tuple_576_vec):
                            scan_tuple_576 = scan_tuple_576_vec[scan_index_576]
                            scan_index_576 += 1
                            vec_576.append(scan_tuple_576)
                        # Program VectorLoop Region
                        vec_index576 = 0
                        while vec_index576 < len(vec_576):
                            var_577 = vec_576[vec_index576]
                            vec_index576 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_575_577 = (var_575, var_577)
                            prev_state = self.table_27[tuple_575_577]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_575_577] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_575, var_577)

                                # Program Call Region
                                ret = self.proc_123_(var_575, var_577)

                        # Program TransitionState Region
                        tuple_575_575 = (var_575, var_575)
                        prev_state = self.table_6[tuple_575_575]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_575_575] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_575_575[1]].append(tuple_575_575[0])
                                self.index_756[tuple_575_575[0]].append(tuple_575_575[1])
                            # Program VectorAppend Region
                            vec_525.append((var_575, var_575))
        # Program VectorClear Region
        del vec_572[:]
        vec_index572 = 0
        # Program VectorUnique Region
        vec_580 = list(set(vec_580))
        vec_index580 = 0
        # Program TableJoin Region
        while vec_index580 < len(vec_580):
            var_582 = vec_580[vec_index580]
            vec_index580 += 1
            tuple_581_0_index: int = 0
            tuple_581_0_vec: List[int] = self.index_279[var_582]
            while tuple_581_0_index < len(tuple_581_0_vec):
                tuple_581_0 = tuple_581_0_vec[tuple_581_0_index]
                tuple_581_0_index += 1
                var_583 = tuple_581_0
                if var_582 in self.index_280:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_583_582 = (var_583, var_582)
                    prev_state = self.table_97[tuple_583_582]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_583_582] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_583_582[1]].append(tuple_583_582[0])
                        # Program VectorAppend Region
                        vec_584.append(var_582)
                    # Program TransitionState Region
                    tuple_583_582 = (var_583, var_582)
                    prev_state = self.table_22[tuple_583_582]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_583_582] = 1 | 4
                        if not present_bit:
                            self.index_760[tuple_583_582[0]].append(tuple_583_582[1])
        # Program VectorClear Region
        del vec_580[:]
        vec_index580 = 0
        # Program VectorUnique Region
        vec_584 = list(set(vec_584))
        vec_index584 = 0
        # Program TableJoin Region
        while vec_index584 < len(vec_584):
            var_586 = vec_584[vec_index584]
            vec_index584 += 1
            tuple_585_0_index: int = 0
            tuple_585_0_vec: List[int] = self.index_285[var_586]
            while tuple_585_0_index < len(tuple_585_0_vec):
                tuple_585_0 = tuple_585_0_vec[tuple_585_0_index]
                tuple_585_0_index += 1
                var_587 = tuple_585_0
                if var_586 in self.index_256:
                    # Program TransitionState Region
                    tuple_587 = var_587
                    prev_state = self.table_13[tuple_587]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_587] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_584[:]
        vec_index584 = 0
        # Program VectorUnique Region
        vec_588 = list(set(vec_588))
        vec_index588 = 0
        # Program TableJoin Region
        while vec_index588 < len(vec_588):
            var_590 = vec_588[vec_index588]
            vec_index588 += 1
            tuple_589_0_index: int = 0
            tuple_589_0_vec: List[int] = self.index_290[var_590]
            while tuple_589_0_index < len(tuple_589_0_vec):
                tuple_589_0 = tuple_589_0_vec[tuple_589_0_index]
                tuple_589_0_index += 1
                var_591 = tuple_589_0
                tuple_589_1_index: int = 0
                tuple_589_1_vec: List[int] = self.index_291[var_590]
                while tuple_589_1_index < len(tuple_589_1_vec):
                    tuple_589_1 = tuple_589_1_vec[tuple_589_1_index]
                    tuple_589_1_index += 1
                    var_592 = tuple_589_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_294_(var_591, var_590)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_164_(var_590, var_592)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_299_(var_591, var_592)
                            if not ret:
                                # Program TransitionState Region
                                tuple_591_592 = (var_591, var_592)
                                prev_state = self.table_6[tuple_591_592]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_591_592] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_591_592[1]].append(tuple_591_592[0])
                                        self.index_756[tuple_591_592[0]].append(tuple_591_592[1])
                                    # Program VectorAppend Region
                                    vec_525.append((var_591, var_592))
        # Program VectorClear Region
        del vec_588[:]
        vec_index588 = 0
        # Induction Fixpoint Loop Region
        while len(vec_525):
            # Program Call Region
            param_527_0 = [vec_525]
            ret = self.proc_127_(param_527_0)
            vec_525 = param_527_0[0]

        vec_index525 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_525[:]
        vec_index525 = 0
        # Program Return Region
        return False
        return False

    def address_operand_2(self, vec_597: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index597: int = 0
        vec_600: List[int] = list()
        vec_index600: int = 0
        vec_604: List[int] = list()
        vec_index604: int = 0
        vec_608: List[int] = list()
        vec_index608: int = 0
        vec_613: List[int] = list()
        vec_index613: int = 0
        vec_618: List[int] = list()
        vec_index618: int = 0
        vec_625: List[int] = list()
        vec_index625: int = 0
        vec_629: List[Tuple[int, int]] = list()
        vec_index629: int = 0
        vec_632: List[int] = list()
        vec_index632: int = 0
        vec_639: List[int] = list()
        vec_index639: int = 0
        vec_643: List[int] = list()
        vec_index643: int = 0
        vec_646: List[int] = list()
        vec_index646: int = 0
        vec_650: List[int] = list()
        vec_index650: int = 0
        vec_654: List[int] = list()
        vec_index654: int = 0
        vec_658: List[int] = list()
        vec_index658: int = 0
        vec_662: List[int] = list()
        vec_index662: int = 0
        vec_666: List[int] = list()
        vec_index666: int = 0
        vec_670: List[int] = list()
        vec_index670: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index597 = 0
        while vec_index597 < len(vec_597):
            var_598, var_599 = vec_597[vec_index597]
            vec_index597 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_598_599 = (var_598, var_599)
            prev_state = self.table_71[tuple_598_599]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_71[tuple_598_599] = 1 | 4
                if not present_bit:
                    self.index_146[tuple_598_599[0]].append(tuple_598_599[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_604.append(var_598)
                # Program VectorAppend Region
                vec_600.append(var_598)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_598_599 = (var_598, var_599)
            prev_state = self.table_71[tuple_598_599]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_71[tuple_598_599] = 1 | 4
                if not present_bit:
                    self.index_146[tuple_598_599[0]].append(tuple_598_599[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_604.append(var_598)
                # Program VectorAppend Region
                vec_600.append(var_598)
        # Program VectorUnique Region
        vec_600 = list(set(vec_600))
        vec_index600 = 0
        # Program TableJoin Region
        while vec_index600 < len(vec_600):
            var_602 = vec_600[vec_index600]
            vec_index600 += 1
            if var_602 in self.index_145:
                tuple_601_1_index: int = 0
                tuple_601_1_vec: List[int] = self.index_146[var_602]
                while tuple_601_1_index < len(tuple_601_1_vec):
                    tuple_601_1 = tuple_601_1_vec[tuple_601_1_index]
                    tuple_601_1_index += 1
                    var_603 = tuple_601_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_602_603 = (var_602, var_603)
                    prev_state = self.table_85[tuple_602_603]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_85[tuple_602_603] = 1 | 4
                        if not present_bit:
                            self.index_184[tuple_602_603[1]].append(tuple_602_603[0])
                        # Program VectorAppend Region
                        vec_608.append(var_603)
        # Program VectorClear Region
        del vec_600[:]
        vec_index600 = 0
        # Program VectorUnique Region
        vec_604 = list(set(vec_604))
        vec_index604 = 0
        # Program TableJoin Region
        while vec_index604 < len(vec_604):
            var_606 = vec_604[vec_index604]
            vec_index604 += 1
            if var_606 in self.index_151:
                tuple_605_1_index: int = 0
                tuple_605_1_vec: List[int] = self.index_146[var_606]
                while tuple_605_1_index < len(tuple_605_1_vec):
                    tuple_605_1 = tuple_605_1_vec[tuple_605_1_index]
                    tuple_605_1_index += 1
                    var_607 = tuple_605_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_606_607 = (var_606, var_607)
                    prev_state = self.table_77[tuple_606_607]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_77[tuple_606_607] = 1 | 4
                        if not present_bit:
                            self.index_202[tuple_606_607[1]].append(tuple_606_607[0])
                        # Program VectorAppend Region
                        vec_613.append(var_607)
        # Program VectorClear Region
        del vec_604[:]
        vec_index604 = 0
        # Program VectorUnique Region
        vec_608 = list(set(vec_608))
        vec_index608 = 0
        # Program TableJoin Region
        while vec_index608 < len(vec_608):
            var_610 = vec_608[vec_index608]
            vec_index608 += 1
            tuple_609_0_index: int = 0
            tuple_609_0_vec: List[int] = self.index_183[var_610]
            while tuple_609_0_index < len(tuple_609_0_vec):
                tuple_609_0 = tuple_609_0_vec[tuple_609_0_index]
                tuple_609_0_index += 1
                var_611 = tuple_609_0
                tuple_609_1_index: int = 0
                tuple_609_1_vec: List[int] = self.index_184[var_610]
                while tuple_609_1_index < len(tuple_609_1_vec):
                    tuple_609_1 = tuple_609_1_vec[tuple_609_1_index]
                    tuple_609_1_index += 1
                    var_612 = tuple_609_1
                    # Program TransitionState Region
                    tuple_611_612 = (var_611, var_612)
                    prev_state = self.table_88[tuple_611_612]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_88[tuple_611_612] = 1 | 4
                        if not present_bit:
                            self.index_232[tuple_611_612[0]].append(tuple_611_612[1])
                        # Program VectorAppend Region
                        vec_618.append(var_611)
        # Program VectorClear Region
        del vec_608[:]
        vec_index608 = 0
        # Program VectorUnique Region
        vec_613 = list(set(vec_613))
        vec_index613 = 0
        # Program TableJoin Region
        while vec_index613 < len(vec_613):
            var_615 = vec_613[vec_index613]
            vec_index613 += 1
            tuple_614_0_index: int = 0
            tuple_614_0_vec: List[int] = self.index_183[var_615]
            while tuple_614_0_index < len(tuple_614_0_vec):
                tuple_614_0 = tuple_614_0_vec[tuple_614_0_index]
                tuple_614_0_index += 1
                var_616 = tuple_614_0
                tuple_614_1_index: int = 0
                tuple_614_1_vec: List[int] = self.index_202[var_615]
                while tuple_614_1_index < len(tuple_614_1_vec):
                    tuple_614_1 = tuple_614_1_vec[tuple_614_1_index]
                    tuple_614_1_index += 1
                    var_617 = tuple_614_1
                    # Program TransitionState Region
                    tuple_616_617 = (var_616, var_617)
                    prev_state = self.table_80[tuple_616_617]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_80[tuple_616_617] = 1 | 4
                        if not present_bit:
                            self.index_244[tuple_616_617[0]].append(tuple_616_617[1])
                        # Program VectorAppend Region
                        vec_632.append(var_616)
        # Program VectorClear Region
        del vec_613[:]
        vec_index613 = 0
        # Program VectorUnique Region
        vec_618 = list(set(vec_618))
        vec_index618 = 0
        # Program TableJoin Region
        while vec_index618 < len(vec_618):
            var_620 = vec_618[vec_index618]
            vec_index618 += 1
            if var_620 in self.index_157:
                tuple_619_1_index: int = 0
                tuple_619_1_vec: List[int] = self.index_232[var_620]
                while tuple_619_1_index < len(tuple_619_1_vec):
                    tuple_619_1 = tuple_619_1_vec[tuple_619_1_index]
                    tuple_619_1_index += 1
                    var_621 = tuple_619_1
                    # Program TransitionState Region
                    tuple_621_620_0 = (var_621, var_620, self.var_0)
                    prev_state = self.table_9[tuple_621_620_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_621_620_0] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_621_620_0[0], tuple_621_620_0[1])].append(tuple_621_620_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_620_621 = (var_620, var_621)
                        prev_state = self.table_27[tuple_620_621]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_620_621] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_620_621[0]].append(tuple_620_621[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_620)
                        if not ret:
                            # Program TransitionState Region
                            tuple_620_621 = (var_620, var_621)
                            prev_state = self.table_27[tuple_620_621]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_620_621] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_620_621[0]].append(tuple_620_621[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_621, var_620)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_621_620 = (var_621, var_620)
                                    prev_state = self.table_52[tuple_621_620]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_621_620] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_621_620[0]].append(tuple_621_620[1])
                                            self.index_778[tuple_621_620[1]].append(tuple_621_620[0])
                                        # Program VectorAppend Region
                                        vec_670.append(var_621)
                                # Program TransitionState Region
                                tuple_621_620 = (var_621, var_620)
                                prev_state = self.table_15[tuple_621_620]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_621_620] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_621_620[0]].append(tuple_621_620[1])
                        # Program TransitionState Region
                        tuple_621_620 = (var_621, var_620)
                        prev_state = self.table_94[tuple_621_620]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_621_620] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_621_620[1]].append(tuple_621_620[0])
                            # Program VectorAppend Region
                            vec_662.append(var_620)
                        # Program TransitionState Region
                        tuple_620 = var_620
                        prev_state = self.table_32[tuple_620]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_620] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_643.append(var_620)
                        # Program TransitionState Region
                        tuple_620 = var_620
                        prev_state = self.table_18[tuple_620]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_620] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_662.append(var_620)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_625: int
                            scan_index_625: int = 0
                            scan_tuple_625_vec: List[int] = self.index_116[var_620]
                            while scan_index_625 < len(scan_tuple_625_vec):
                                scan_tuple_625 = scan_tuple_625_vec[scan_index_625]
                                scan_index_625 += 1
                                vec_625.append(scan_tuple_625)
                            # Program VectorLoop Region
                            vec_index625 = 0
                            while vec_index625 < len(vec_625):
                                var_626 = vec_625[vec_index625]
                                vec_index625 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_620_626 = (var_620, var_626)
                                prev_state = self.table_27[tuple_620_626]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_620_626] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_119_(var_620, var_626)

                                    # Program Call Region
                                    ret = self.proc_123_(var_620, var_626)

                            # Program TransitionState Region
                            tuple_620_620 = (var_620, var_620)
                            prev_state = self.table_6[tuple_620_620]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_620_620] = 1 | 4
                                if not present_bit:
                                    self.index_290[tuple_620_620[1]].append(tuple_620_620[0])
                                    self.index_756[tuple_620_620[0]].append(tuple_620_620[1])
                                # Program VectorAppend Region
                                vec_629.append((var_620, var_620))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_621_620 = (var_621, var_620)
                            prev_state = self.table_40[tuple_621_620]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_621_620] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_621_620[0]].append(tuple_621_620[1])
                                # Program VectorAppend Region
                                vec_650.append(var_621)
        # Program VectorClear Region
        del vec_618[:]
        vec_index618 = 0
        # Program VectorUnique Region
        vec_632 = list(set(vec_632))
        vec_index632 = 0
        # Program TableJoin Region
        while vec_index632 < len(vec_632):
            var_634 = vec_632[vec_index632]
            vec_index632 += 1
            if var_634 in self.index_157:
                tuple_633_1_index: int = 0
                tuple_633_1_vec: List[int] = self.index_244[var_634]
                while tuple_633_1_index < len(tuple_633_1_vec):
                    tuple_633_1 = tuple_633_1_vec[tuple_633_1_index]
                    tuple_633_1_index += 1
                    var_635 = tuple_633_1
                    # Program TransitionState Region
                    tuple_635_634_2 = (var_635, var_634, self.var_2)
                    prev_state = self.table_9[tuple_635_634_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_635_634_2] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_635_634_2[0], tuple_635_634_2[1])].append(tuple_635_634_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_634_635 = (var_634, var_635)
                        prev_state = self.table_27[tuple_634_635]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_634_635] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_634_635[0]].append(tuple_634_635[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_634)
                        if not ret:
                            # Program TransitionState Region
                            tuple_634_635 = (var_634, var_635)
                            prev_state = self.table_27[tuple_634_635]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_634_635] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_634_635[0]].append(tuple_634_635[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_635, var_634)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_635_634 = (var_635, var_634)
                                    prev_state = self.table_52[tuple_635_634]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_635_634] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_635_634[0]].append(tuple_635_634[1])
                                            self.index_778[tuple_635_634[1]].append(tuple_635_634[0])
                                        # Program VectorAppend Region
                                        vec_670.append(var_635)
                                # Program TransitionState Region
                                tuple_635_634 = (var_635, var_634)
                                prev_state = self.table_15[tuple_635_634]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_635_634] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_635_634[0]].append(tuple_635_634[1])
                        # Program TransitionState Region
                        tuple_635_634 = (var_635, var_634)
                        prev_state = self.table_94[tuple_635_634]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_635_634] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_635_634[1]].append(tuple_635_634[0])
                            # Program VectorAppend Region
                            vec_662.append(var_634)
                        # Program TransitionState Region
                        tuple_634 = var_634
                        prev_state = self.table_32[tuple_634]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_634] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_643.append(var_634)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_634 = var_634
                            prev_state = self.table_18[tuple_634]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_634] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_662.append(var_634)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_639: int
                                scan_index_639: int = 0
                                scan_tuple_639_vec: List[int] = self.index_116[var_634]
                                while scan_index_639 < len(scan_tuple_639_vec):
                                    scan_tuple_639 = scan_tuple_639_vec[scan_index_639]
                                    scan_index_639 += 1
                                    vec_639.append(scan_tuple_639)
                                # Program VectorLoop Region
                                vec_index639 = 0
                                while vec_index639 < len(vec_639):
                                    var_640 = vec_639[vec_index639]
                                    vec_index639 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_634_640 = (var_634, var_640)
                                    prev_state = self.table_27[tuple_634_640]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_634_640] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_634, var_640)

                                        # Program Call Region
                                        ret = self.proc_123_(var_634, var_640)

                                # Program TransitionState Region
                                tuple_634_634 = (var_634, var_634)
                                prev_state = self.table_6[tuple_634_634]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_634_634] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_634_634[1]].append(tuple_634_634[0])
                                        self.index_756[tuple_634_634[0]].append(tuple_634_634[1])
                                    # Program VectorAppend Region
                                    vec_629.append((var_634, var_634))
                        # Program TransitionState Region
                        tuple_635_634 = (var_635, var_634)
                        prev_state = self.table_40[tuple_635_634]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_635_634] = 1 | 4
                            if not present_bit:
                                self.index_265[tuple_635_634[0]].append(tuple_635_634[1])
                            # Program VectorAppend Region
                            vec_650.append(var_635)
        # Program VectorClear Region
        del vec_632[:]
        vec_index632 = 0
        # Program VectorUnique Region
        vec_643 = list(set(vec_643))
        vec_index643 = 0
        # Program TableJoin Region
        while vec_index643 < len(vec_643):
            var_645 = vec_643[vec_index643]
            vec_index643 += 1
            if var_645 in self.index_256:
                if var_645 in self.index_257:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_645 = var_645
                    prev_state = self.table_18[tuple_645]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_645] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_662.append(var_645)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_646: int
                        scan_index_646: int = 0
                        scan_tuple_646_vec: List[int] = self.index_116[var_645]
                        while scan_index_646 < len(scan_tuple_646_vec):
                            scan_tuple_646 = scan_tuple_646_vec[scan_index_646]
                            scan_index_646 += 1
                            vec_646.append(scan_tuple_646)
                        # Program VectorLoop Region
                        vec_index646 = 0
                        while vec_index646 < len(vec_646):
                            var_647 = vec_646[vec_index646]
                            vec_index646 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_645_647 = (var_645, var_647)
                            prev_state = self.table_27[tuple_645_647]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_645_647] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_645, var_647)

                                # Program Call Region
                                ret = self.proc_123_(var_645, var_647)

                        # Program TransitionState Region
                        tuple_645_645 = (var_645, var_645)
                        prev_state = self.table_6[tuple_645_645]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_645_645] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_645_645[1]].append(tuple_645_645[0])
                                self.index_756[tuple_645_645[0]].append(tuple_645_645[1])
                            # Program VectorAppend Region
                            vec_629.append((var_645, var_645))
        # Program VectorClear Region
        del vec_643[:]
        vec_index643 = 0
        # Program VectorUnique Region
        vec_650 = list(set(vec_650))
        vec_index650 = 0
        # Program TableJoin Region
        while vec_index650 < len(vec_650):
            var_652 = vec_650[vec_index650]
            vec_index650 += 1
            if var_652 in self.index_151:
                tuple_651_1_index: int = 0
                tuple_651_1_vec: List[int] = self.index_265[var_652]
                while tuple_651_1_index < len(tuple_651_1_vec):
                    tuple_651_1 = tuple_651_1_vec[tuple_651_1_index]
                    tuple_651_1_index += 1
                    var_653 = tuple_651_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_652_653 = (var_652, var_653)
                    prev_state = self.table_43[tuple_652_653]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_43[tuple_652_653] = 1 | 4
                        if not present_bit:
                            self.index_270[tuple_652_653[1]].append(tuple_652_653[0])
                        # Program VectorAppend Region
                        vec_654.append(var_653)
        # Program VectorClear Region
        del vec_650[:]
        vec_index650 = 0
        # Program VectorUnique Region
        vec_654 = list(set(vec_654))
        vec_index654 = 0
        # Program TableJoin Region
        while vec_index654 < len(vec_654):
            var_656 = vec_654[vec_index654]
            vec_index654 += 1
            if var_656 in self.index_256:
                tuple_655_1_index: int = 0
                tuple_655_1_vec: List[int] = self.index_270[var_656]
                while tuple_655_1_index < len(tuple_655_1_vec):
                    tuple_655_1 = tuple_655_1_vec[tuple_655_1_index]
                    tuple_655_1_index += 1
                    var_657 = tuple_655_1
                    # Program TransitionState Region
                    tuple_657 = var_657
                    prev_state = self.table_18[tuple_657]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_657] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_662.append(var_657)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_658: int
                        scan_index_658: int = 0
                        scan_tuple_658_vec: List[int] = self.index_116[var_657]
                        while scan_index_658 < len(scan_tuple_658_vec):
                            scan_tuple_658 = scan_tuple_658_vec[scan_index_658]
                            scan_index_658 += 1
                            vec_658.append(scan_tuple_658)
                        # Program VectorLoop Region
                        vec_index658 = 0
                        while vec_index658 < len(vec_658):
                            var_659 = vec_658[vec_index658]
                            vec_index658 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_657_659 = (var_657, var_659)
                            prev_state = self.table_27[tuple_657_659]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_657_659] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_657, var_659)

                                # Program Call Region
                                ret = self.proc_123_(var_657, var_659)

                        # Program TransitionState Region
                        tuple_657_657 = (var_657, var_657)
                        prev_state = self.table_6[tuple_657_657]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_657_657] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_657_657[1]].append(tuple_657_657[0])
                                self.index_756[tuple_657_657[0]].append(tuple_657_657[1])
                            # Program VectorAppend Region
                            vec_629.append((var_657, var_657))
        # Program VectorClear Region
        del vec_654[:]
        vec_index654 = 0
        # Program VectorUnique Region
        vec_662 = list(set(vec_662))
        vec_index662 = 0
        # Program TableJoin Region
        while vec_index662 < len(vec_662):
            var_664 = vec_662[vec_index662]
            vec_index662 += 1
            tuple_663_0_index: int = 0
            tuple_663_0_vec: List[int] = self.index_279[var_664]
            while tuple_663_0_index < len(tuple_663_0_vec):
                tuple_663_0 = tuple_663_0_vec[tuple_663_0_index]
                tuple_663_0_index += 1
                var_665 = tuple_663_0
                if var_664 in self.index_280:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_665_664 = (var_665, var_664)
                    prev_state = self.table_97[tuple_665_664]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_665_664] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_665_664[1]].append(tuple_665_664[0])
                        # Program VectorAppend Region
                        vec_666.append(var_664)
                    # Program TransitionState Region
                    tuple_665_664 = (var_665, var_664)
                    prev_state = self.table_22[tuple_665_664]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_665_664] = 1 | 4
                        if not present_bit:
                            self.index_760[tuple_665_664[0]].append(tuple_665_664[1])
        # Program VectorClear Region
        del vec_662[:]
        vec_index662 = 0
        # Program VectorUnique Region
        vec_666 = list(set(vec_666))
        vec_index666 = 0
        # Program TableJoin Region
        while vec_index666 < len(vec_666):
            var_668 = vec_666[vec_index666]
            vec_index666 += 1
            tuple_667_0_index: int = 0
            tuple_667_0_vec: List[int] = self.index_285[var_668]
            while tuple_667_0_index < len(tuple_667_0_vec):
                tuple_667_0 = tuple_667_0_vec[tuple_667_0_index]
                tuple_667_0_index += 1
                var_669 = tuple_667_0
                if var_668 in self.index_256:
                    # Program TransitionState Region
                    tuple_669 = var_669
                    prev_state = self.table_13[tuple_669]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_669] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_666[:]
        vec_index666 = 0
        # Program VectorUnique Region
        vec_670 = list(set(vec_670))
        vec_index670 = 0
        # Program TableJoin Region
        while vec_index670 < len(vec_670):
            var_672 = vec_670[vec_index670]
            vec_index670 += 1
            tuple_671_0_index: int = 0
            tuple_671_0_vec: List[int] = self.index_290[var_672]
            while tuple_671_0_index < len(tuple_671_0_vec):
                tuple_671_0 = tuple_671_0_vec[tuple_671_0_index]
                tuple_671_0_index += 1
                var_673 = tuple_671_0
                tuple_671_1_index: int = 0
                tuple_671_1_vec: List[int] = self.index_291[var_672]
                while tuple_671_1_index < len(tuple_671_1_vec):
                    tuple_671_1 = tuple_671_1_vec[tuple_671_1_index]
                    tuple_671_1_index += 1
                    var_674 = tuple_671_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_294_(var_673, var_672)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_164_(var_672, var_674)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_299_(var_673, var_674)
                            if not ret:
                                # Program TransitionState Region
                                tuple_673_674 = (var_673, var_674)
                                prev_state = self.table_6[tuple_673_674]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_673_674] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_673_674[1]].append(tuple_673_674[0])
                                        self.index_756[tuple_673_674[0]].append(tuple_673_674[1])
                                    # Program VectorAppend Region
                                    vec_629.append((var_673, var_674))
        # Program VectorClear Region
        del vec_670[:]
        vec_index670 = 0
        # Induction Fixpoint Loop Region
        while len(vec_629):
            # Program Call Region
            param_631_0 = [vec_629]
            ret = self.proc_127_(param_631_0)
            vec_629 = param_631_0[0]

        vec_index629 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_629[:]
        vec_index629 = 0
        # Program Return Region
        return False
        return False

    def relocation_2(self, vec_679: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index679: int = 0
        vec_682: List[int] = list()
        vec_index682: int = 0
        vec_687: List[int] = list()
        vec_index687: int = 0
        vec_692: List[int] = list()
        vec_index692: int = 0
        vec_699: List[int] = list()
        vec_index699: int = 0
        vec_703: List[Tuple[int, int]] = list()
        vec_index703: int = 0
        vec_706: List[int] = list()
        vec_index706: int = 0
        vec_713: List[int] = list()
        vec_index713: int = 0
        vec_717: List[int] = list()
        vec_index717: int = 0
        vec_720: List[int] = list()
        vec_index720: int = 0
        vec_724: List[int] = list()
        vec_index724: int = 0
        vec_728: List[int] = list()
        vec_index728: int = 0
        vec_732: List[int] = list()
        vec_index732: int = 0
        vec_736: List[int] = list()
        vec_index736: int = 0
        vec_740: List[int] = list()
        vec_index740: int = 0
        vec_744: List[int] = list()
        vec_index744: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index679 = 0
        while vec_index679 < len(vec_679):
            var_680, var_681 = vec_679[vec_index679]
            vec_index679 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_680_681 = (var_680, var_681)
            prev_state = self.table_74[tuple_680_681]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_74[tuple_680_681] = 1 | 4
                if not present_bit:
                    self.index_183[tuple_680_681[0]].append(tuple_680_681[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_687.append(var_680)
                # Program VectorAppend Region
                vec_682.append(var_680)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_680_681 = (var_680, var_681)
            prev_state = self.table_74[tuple_680_681]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_74[tuple_680_681] = 1 | 4
                if not present_bit:
                    self.index_183[tuple_680_681[0]].append(tuple_680_681[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_687.append(var_680)
                # Program VectorAppend Region
                vec_682.append(var_680)
        # Program VectorUnique Region
        vec_682 = list(set(vec_682))
        vec_index682 = 0
        # Program TableJoin Region
        while vec_index682 < len(vec_682):
            var_684 = vec_682[vec_index682]
            vec_index682 += 1
            tuple_683_0_index: int = 0
            tuple_683_0_vec: List[int] = self.index_183[var_684]
            while tuple_683_0_index < len(tuple_683_0_vec):
                tuple_683_0 = tuple_683_0_vec[tuple_683_0_index]
                tuple_683_0_index += 1
                var_685 = tuple_683_0
                tuple_683_1_index: int = 0
                tuple_683_1_vec: List[int] = self.index_184[var_684]
                while tuple_683_1_index < len(tuple_683_1_vec):
                    tuple_683_1 = tuple_683_1_vec[tuple_683_1_index]
                    tuple_683_1_index += 1
                    var_686 = tuple_683_1
                    # Program TransitionState Region
                    tuple_685_686 = (var_685, var_686)
                    prev_state = self.table_88[tuple_685_686]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_88[tuple_685_686] = 1 | 4
                        if not present_bit:
                            self.index_232[tuple_685_686[0]].append(tuple_685_686[1])
                        # Program VectorAppend Region
                        vec_692.append(var_685)
        # Program VectorClear Region
        del vec_682[:]
        vec_index682 = 0
        # Program VectorUnique Region
        vec_687 = list(set(vec_687))
        vec_index687 = 0
        # Program TableJoin Region
        while vec_index687 < len(vec_687):
            var_689 = vec_687[vec_index687]
            vec_index687 += 1
            tuple_688_0_index: int = 0
            tuple_688_0_vec: List[int] = self.index_183[var_689]
            while tuple_688_0_index < len(tuple_688_0_vec):
                tuple_688_0 = tuple_688_0_vec[tuple_688_0_index]
                tuple_688_0_index += 1
                var_690 = tuple_688_0
                tuple_688_1_index: int = 0
                tuple_688_1_vec: List[int] = self.index_202[var_689]
                while tuple_688_1_index < len(tuple_688_1_vec):
                    tuple_688_1 = tuple_688_1_vec[tuple_688_1_index]
                    tuple_688_1_index += 1
                    var_691 = tuple_688_1
                    # Program TransitionState Region
                    tuple_690_691 = (var_690, var_691)
                    prev_state = self.table_80[tuple_690_691]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_80[tuple_690_691] = 1 | 4
                        if not present_bit:
                            self.index_244[tuple_690_691[0]].append(tuple_690_691[1])
                        # Program VectorAppend Region
                        vec_706.append(var_690)
        # Program VectorClear Region
        del vec_687[:]
        vec_index687 = 0
        # Program VectorUnique Region
        vec_692 = list(set(vec_692))
        vec_index692 = 0
        # Program TableJoin Region
        while vec_index692 < len(vec_692):
            var_694 = vec_692[vec_index692]
            vec_index692 += 1
            if var_694 in self.index_157:
                tuple_693_1_index: int = 0
                tuple_693_1_vec: List[int] = self.index_232[var_694]
                while tuple_693_1_index < len(tuple_693_1_vec):
                    tuple_693_1 = tuple_693_1_vec[tuple_693_1_index]
                    tuple_693_1_index += 1
                    var_695 = tuple_693_1
                    # Program TransitionState Region
                    tuple_695_694_0 = (var_695, var_694, self.var_0)
                    prev_state = self.table_9[tuple_695_694_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_695_694_0] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_695_694_0[0], tuple_695_694_0[1])].append(tuple_695_694_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_694_695 = (var_694, var_695)
                        prev_state = self.table_27[tuple_694_695]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_694_695] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_694_695[0]].append(tuple_694_695[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_694)
                        if not ret:
                            # Program TransitionState Region
                            tuple_694_695 = (var_694, var_695)
                            prev_state = self.table_27[tuple_694_695]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_694_695] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_694_695[0]].append(tuple_694_695[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_695, var_694)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_695_694 = (var_695, var_694)
                                    prev_state = self.table_52[tuple_695_694]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_695_694] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_695_694[0]].append(tuple_695_694[1])
                                            self.index_778[tuple_695_694[1]].append(tuple_695_694[0])
                                        # Program VectorAppend Region
                                        vec_744.append(var_695)
                                # Program TransitionState Region
                                tuple_695_694 = (var_695, var_694)
                                prev_state = self.table_15[tuple_695_694]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_695_694] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_695_694[0]].append(tuple_695_694[1])
                        # Program TransitionState Region
                        tuple_695_694 = (var_695, var_694)
                        prev_state = self.table_94[tuple_695_694]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_695_694] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_695_694[1]].append(tuple_695_694[0])
                            # Program VectorAppend Region
                            vec_736.append(var_694)
                        # Program TransitionState Region
                        tuple_694 = var_694
                        prev_state = self.table_32[tuple_694]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_694] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_717.append(var_694)
                        # Program TransitionState Region
                        tuple_694 = var_694
                        prev_state = self.table_18[tuple_694]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_694] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program VectorAppend Region
                            vec_736.append(var_694)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_699: int
                            scan_index_699: int = 0
                            scan_tuple_699_vec: List[int] = self.index_116[var_694]
                            while scan_index_699 < len(scan_tuple_699_vec):
                                scan_tuple_699 = scan_tuple_699_vec[scan_index_699]
                                scan_index_699 += 1
                                vec_699.append(scan_tuple_699)
                            # Program VectorLoop Region
                            vec_index699 = 0
                            while vec_index699 < len(vec_699):
                                var_700 = vec_699[vec_index699]
                                vec_index699 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_694_700 = (var_694, var_700)
                                prev_state = self.table_27[tuple_694_700]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_27[tuple_694_700] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_119_(var_694, var_700)

                                    # Program Call Region
                                    ret = self.proc_123_(var_694, var_700)

                            # Program TransitionState Region
                            tuple_694_694 = (var_694, var_694)
                            prev_state = self.table_6[tuple_694_694]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_694_694] = 1 | 4
                                if not present_bit:
                                    self.index_290[tuple_694_694[1]].append(tuple_694_694[0])
                                    self.index_756[tuple_694_694[0]].append(tuple_694_694[1])
                                # Program VectorAppend Region
                                vec_703.append((var_694, var_694))
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_695_694 = (var_695, var_694)
                            prev_state = self.table_40[tuple_695_694]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_40[tuple_695_694] = 1 | 4
                                if not present_bit:
                                    self.index_265[tuple_695_694[0]].append(tuple_695_694[1])
                                # Program VectorAppend Region
                                vec_724.append(var_695)
        # Program VectorClear Region
        del vec_692[:]
        vec_index692 = 0
        # Program VectorUnique Region
        vec_706 = list(set(vec_706))
        vec_index706 = 0
        # Program TableJoin Region
        while vec_index706 < len(vec_706):
            var_708 = vec_706[vec_index706]
            vec_index706 += 1
            if var_708 in self.index_157:
                tuple_707_1_index: int = 0
                tuple_707_1_vec: List[int] = self.index_244[var_708]
                while tuple_707_1_index < len(tuple_707_1_vec):
                    tuple_707_1 = tuple_707_1_vec[tuple_707_1_index]
                    tuple_707_1_index += 1
                    var_709 = tuple_707_1
                    # Program TransitionState Region
                    tuple_709_708_2 = (var_709, var_708, self.var_2)
                    prev_state = self.table_9[tuple_709_708_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_709_708_2] = 1 | 4
                        if not present_bit:
                            self.index_799[(tuple_709_708_2[0], tuple_709_708_2[1])].append(tuple_709_708_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_708_709 = (var_708, var_709)
                        prev_state = self.table_27[tuple_708_709]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_27[tuple_708_709] = 2 | 4
                            if not present_bit:
                                self.index_116[tuple_708_709[0]].append(tuple_708_709[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_161_(var_708)
                        if not ret:
                            # Program TransitionState Region
                            tuple_708_709 = (var_708, var_709)
                            prev_state = self.table_27[tuple_708_709]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_27[tuple_708_709] = 1 | 4
                                if not present_bit:
                                    self.index_116[tuple_708_709[0]].append(tuple_708_709[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_164_(var_709, var_708)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_709_708 = (var_709, var_708)
                                    prev_state = self.table_52[tuple_709_708]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_52[tuple_709_708] = 1 | 4
                                        if not present_bit:
                                            self.index_291[tuple_709_708[0]].append(tuple_709_708[1])
                                            self.index_778[tuple_709_708[1]].append(tuple_709_708[0])
                                        # Program VectorAppend Region
                                        vec_744.append(var_709)
                                # Program TransitionState Region
                                tuple_709_708 = (var_709, var_708)
                                prev_state = self.table_15[tuple_709_708]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_709_708] = 1 | 4
                                    if not present_bit:
                                        self.index_752[tuple_709_708[0]].append(tuple_709_708[1])
                        # Program TransitionState Region
                        tuple_709_708 = (var_709, var_708)
                        prev_state = self.table_94[tuple_709_708]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_94[tuple_709_708] = 1 | 4
                            if not present_bit:
                                self.index_279[tuple_709_708[1]].append(tuple_709_708[0])
                            # Program VectorAppend Region
                            vec_736.append(var_708)
                        # Program TransitionState Region
                        tuple_708 = var_708
                        prev_state = self.table_32[tuple_708]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_32[tuple_708] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_717.append(var_708)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_708 = var_708
                            prev_state = self.table_18[tuple_708]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_708] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program VectorAppend Region
                                vec_736.append(var_708)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_713: int
                                scan_index_713: int = 0
                                scan_tuple_713_vec: List[int] = self.index_116[var_708]
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
                                    tuple_708_714 = (var_708, var_714)
                                    prev_state = self.table_27[tuple_708_714]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_27[tuple_708_714] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_119_(var_708, var_714)

                                        # Program Call Region
                                        ret = self.proc_123_(var_708, var_714)

                                # Program TransitionState Region
                                tuple_708_708 = (var_708, var_708)
                                prev_state = self.table_6[tuple_708_708]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_708_708] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_708_708[1]].append(tuple_708_708[0])
                                        self.index_756[tuple_708_708[0]].append(tuple_708_708[1])
                                    # Program VectorAppend Region
                                    vec_703.append((var_708, var_708))
                        # Program TransitionState Region
                        tuple_709_708 = (var_709, var_708)
                        prev_state = self.table_40[tuple_709_708]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_709_708] = 1 | 4
                            if not present_bit:
                                self.index_265[tuple_709_708[0]].append(tuple_709_708[1])
                            # Program VectorAppend Region
                            vec_724.append(var_709)
        # Program VectorClear Region
        del vec_706[:]
        vec_index706 = 0
        # Program VectorUnique Region
        vec_717 = list(set(vec_717))
        vec_index717 = 0
        # Program TableJoin Region
        while vec_index717 < len(vec_717):
            var_719 = vec_717[vec_index717]
            vec_index717 += 1
            if var_719 in self.index_256:
                if var_719 in self.index_257:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_719 = var_719
                    prev_state = self.table_18[tuple_719]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_719] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_736.append(var_719)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_720: int
                        scan_index_720: int = 0
                        scan_tuple_720_vec: List[int] = self.index_116[var_719]
                        while scan_index_720 < len(scan_tuple_720_vec):
                            scan_tuple_720 = scan_tuple_720_vec[scan_index_720]
                            scan_index_720 += 1
                            vec_720.append(scan_tuple_720)
                        # Program VectorLoop Region
                        vec_index720 = 0
                        while vec_index720 < len(vec_720):
                            var_721 = vec_720[vec_index720]
                            vec_index720 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_719_721 = (var_719, var_721)
                            prev_state = self.table_27[tuple_719_721]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_719_721] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_719, var_721)

                                # Program Call Region
                                ret = self.proc_123_(var_719, var_721)

                        # Program TransitionState Region
                        tuple_719_719 = (var_719, var_719)
                        prev_state = self.table_6[tuple_719_719]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_719_719] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_719_719[1]].append(tuple_719_719[0])
                                self.index_756[tuple_719_719[0]].append(tuple_719_719[1])
                            # Program VectorAppend Region
                            vec_703.append((var_719, var_719))
        # Program VectorClear Region
        del vec_717[:]
        vec_index717 = 0
        # Program VectorUnique Region
        vec_724 = list(set(vec_724))
        vec_index724 = 0
        # Program TableJoin Region
        while vec_index724 < len(vec_724):
            var_726 = vec_724[vec_index724]
            vec_index724 += 1
            if var_726 in self.index_151:
                tuple_725_1_index: int = 0
                tuple_725_1_vec: List[int] = self.index_265[var_726]
                while tuple_725_1_index < len(tuple_725_1_vec):
                    tuple_725_1 = tuple_725_1_vec[tuple_725_1_index]
                    tuple_725_1_index += 1
                    var_727 = tuple_725_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_726_727 = (var_726, var_727)
                    prev_state = self.table_43[tuple_726_727]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_43[tuple_726_727] = 1 | 4
                        if not present_bit:
                            self.index_270[tuple_726_727[1]].append(tuple_726_727[0])
                        # Program VectorAppend Region
                        vec_728.append(var_727)
        # Program VectorClear Region
        del vec_724[:]
        vec_index724 = 0
        # Program VectorUnique Region
        vec_728 = list(set(vec_728))
        vec_index728 = 0
        # Program TableJoin Region
        while vec_index728 < len(vec_728):
            var_730 = vec_728[vec_index728]
            vec_index728 += 1
            if var_730 in self.index_256:
                tuple_729_1_index: int = 0
                tuple_729_1_vec: List[int] = self.index_270[var_730]
                while tuple_729_1_index < len(tuple_729_1_vec):
                    tuple_729_1 = tuple_729_1_vec[tuple_729_1_index]
                    tuple_729_1_index += 1
                    var_731 = tuple_729_1
                    # Program TransitionState Region
                    tuple_731 = var_731
                    prev_state = self.table_18[tuple_731]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_731] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_736.append(var_731)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_732: int
                        scan_index_732: int = 0
                        scan_tuple_732_vec: List[int] = self.index_116[var_731]
                        while scan_index_732 < len(scan_tuple_732_vec):
                            scan_tuple_732 = scan_tuple_732_vec[scan_index_732]
                            scan_index_732 += 1
                            vec_732.append(scan_tuple_732)
                        # Program VectorLoop Region
                        vec_index732 = 0
                        while vec_index732 < len(vec_732):
                            var_733 = vec_732[vec_index732]
                            vec_index732 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_731_733 = (var_731, var_733)
                            prev_state = self.table_27[tuple_731_733]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_27[tuple_731_733] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_119_(var_731, var_733)

                                # Program Call Region
                                ret = self.proc_123_(var_731, var_733)

                        # Program TransitionState Region
                        tuple_731_731 = (var_731, var_731)
                        prev_state = self.table_6[tuple_731_731]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_731_731] = 1 | 4
                            if not present_bit:
                                self.index_290[tuple_731_731[1]].append(tuple_731_731[0])
                                self.index_756[tuple_731_731[0]].append(tuple_731_731[1])
                            # Program VectorAppend Region
                            vec_703.append((var_731, var_731))
        # Program VectorClear Region
        del vec_728[:]
        vec_index728 = 0
        # Program VectorUnique Region
        vec_736 = list(set(vec_736))
        vec_index736 = 0
        # Program TableJoin Region
        while vec_index736 < len(vec_736):
            var_738 = vec_736[vec_index736]
            vec_index736 += 1
            tuple_737_0_index: int = 0
            tuple_737_0_vec: List[int] = self.index_279[var_738]
            while tuple_737_0_index < len(tuple_737_0_vec):
                tuple_737_0 = tuple_737_0_vec[tuple_737_0_index]
                tuple_737_0_index += 1
                var_739 = tuple_737_0
                if var_738 in self.index_280:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_739_738 = (var_739, var_738)
                    prev_state = self.table_97[tuple_739_738]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_739_738] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_739_738[1]].append(tuple_739_738[0])
                        # Program VectorAppend Region
                        vec_740.append(var_738)
                    # Program TransitionState Region
                    tuple_739_738 = (var_739, var_738)
                    prev_state = self.table_22[tuple_739_738]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_22[tuple_739_738] = 1 | 4
                        if not present_bit:
                            self.index_760[tuple_739_738[0]].append(tuple_739_738[1])
        # Program VectorClear Region
        del vec_736[:]
        vec_index736 = 0
        # Program VectorUnique Region
        vec_740 = list(set(vec_740))
        vec_index740 = 0
        # Program TableJoin Region
        while vec_index740 < len(vec_740):
            var_742 = vec_740[vec_index740]
            vec_index740 += 1
            tuple_741_0_index: int = 0
            tuple_741_0_vec: List[int] = self.index_285[var_742]
            while tuple_741_0_index < len(tuple_741_0_vec):
                tuple_741_0 = tuple_741_0_vec[tuple_741_0_index]
                tuple_741_0_index += 1
                var_743 = tuple_741_0
                if var_742 in self.index_256:
                    # Program TransitionState Region
                    tuple_743 = var_743
                    prev_state = self.table_13[tuple_743]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_743] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_740[:]
        vec_index740 = 0
        # Program VectorUnique Region
        vec_744 = list(set(vec_744))
        vec_index744 = 0
        # Program TableJoin Region
        while vec_index744 < len(vec_744):
            var_746 = vec_744[vec_index744]
            vec_index744 += 1
            tuple_745_0_index: int = 0
            tuple_745_0_vec: List[int] = self.index_290[var_746]
            while tuple_745_0_index < len(tuple_745_0_vec):
                tuple_745_0 = tuple_745_0_vec[tuple_745_0_index]
                tuple_745_0_index += 1
                var_747 = tuple_745_0
                tuple_745_1_index: int = 0
                tuple_745_1_vec: List[int] = self.index_291[var_746]
                while tuple_745_1_index < len(tuple_745_1_vec):
                    tuple_745_1 = tuple_745_1_vec[tuple_745_1_index]
                    tuple_745_1_index += 1
                    var_748 = tuple_745_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_294_(var_747, var_746)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_164_(var_746, var_748)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_299_(var_747, var_748)
                            if not ret:
                                # Program TransitionState Region
                                tuple_747_748 = (var_747, var_748)
                                prev_state = self.table_6[tuple_747_748]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_747_748] = 1 | 4
                                    if not present_bit:
                                        self.index_290[tuple_747_748[1]].append(tuple_747_748[0])
                                        self.index_756[tuple_747_748[0]].append(tuple_747_748[1])
                                    # Program VectorAppend Region
                                    vec_703.append((var_747, var_748))
        # Program VectorClear Region
        del vec_744[:]
        vec_index744 = 0
        # Induction Fixpoint Loop Region
        while len(vec_703):
            # Program Call Region
            param_705_0 = [vec_703]
            ret = self.proc_127_(param_705_0)
            vec_703 = param_705_0[0]

        vec_index703 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_703[:]
        vec_index703 = 0
        # Program Return Region
        return False
        return False

    def proc_753_(self, var_754: int, var_755: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[(var_754, var_755)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_754_755 = (var_754, var_755)
            prev_state = self.table_15[tuple_754_755]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_754_755] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker::call_pred
                ret = self.proc_787_(var_755, var_754)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_754_755 = (var_754, var_755)
                    prev_state = self.table_15[tuple_754_755]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_754_755] = 1 | 4
                        if not present_bit:
                            self.index_752[tuple_754_755[0]].append(tuple_754_755[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_757_(self, var_758: int, var_759: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_761_(var_758, var_759)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_761_(self, var_762: int, var_763: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_762, var_763)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_762_763 = (var_762, var_763)
            prev_state = self.table_6[tuple_762_763]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_762_763] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_769_(var_762, var_763)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_762_763 = (var_762, var_763)
                    prev_state = self.table_6[tuple_762_763]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_762_763] = 1 | 4
                        if not present_bit:
                            self.index_290[tuple_762_763[1]].append(tuple_762_763[0])
                            self.index_756[tuple_762_763[0]].append(tuple_762_763[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_769_(self, var_770: int, var_771: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_773_(var_770, var_771)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_773_(self, var_774: int, var_775: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_777: List[int] = list()
        vec_index777: int = 0
        vec_779: List[int] = list()
        vec_index779: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_779: int
        scan_index_779: int = 0
        scan_tuple_779_vec: List[int] = self.index_778[var_775]
        while scan_index_779 < len(scan_tuple_779_vec):
            scan_tuple_779 = scan_tuple_779_vec[scan_index_779]
            scan_index_779 += 1
            vec_779.append(scan_tuple_779)
        # Program VectorLoop Region
        vec_index779 = 0
        while vec_index779 < len(vec_779):
            var_780 = vec_779[vec_index779]
            vec_index779 += 1
            # Program VectorAppend Region
            vec_777.append(var_780)
        # Program VectorUnique Region
        vec_777 = list(set(vec_777))
        vec_index777 = 0
        # Program TableJoin Region
        while vec_index777 < len(vec_777):
            var_782 = vec_777[vec_index777]
            vec_index777 += 1
            tuple_781_0_index: int = 0
            tuple_781_0_vec: List[int] = self.index_290[var_782]
            while tuple_781_0_index < len(tuple_781_0_vec):
                tuple_781_0 = tuple_781_0_vec[tuple_781_0_index]
                tuple_781_0_index += 1
                var_783 = tuple_781_0
                tuple_781_1_index: int = 0
                tuple_781_1_vec: List[int] = self.index_291[var_782]
                while tuple_781_1_index < len(tuple_781_1_vec):
                    tuple_781_1 = tuple_781_1_vec[tuple_781_1_index]
                    tuple_781_1_index += 1
                    var_784 = tuple_781_1
                    # Program TupleCompare Region
                    if (var_774, var_775, ) == (var_783, var_784, ):
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_294_(var_783, var_782)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_164_(var_782, var_784)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_777[:]
        vec_index777 = 0
        # Program Return Region
        return False
        return False

    def proc_787_(self, var_788: int, var_789: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_27[(var_788, var_789)] & 3
        if state == 1:
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_161_(var_788)
            if not ret:
                # Program Return Region
                return True
            # Program TransitionState Region
            tuple_788_789 = (var_788, var_789)
            prev_state = self.table_27[tuple_788_789]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 1:
                self.table_27[tuple_788_789] = 0 | 4
        elif state == 2:
            # Program TransitionState Region
            tuple_788_789 = (var_788, var_789)
            prev_state = self.table_27[tuple_788_789]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_27[tuple_788_789] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_161_(var_788)
                if not ret:
                    # Program Call Region
                    ret = self.proc_795_(var_789, var_788)
                    if ret:
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_795_(self, var_796: int, var_797: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_800: List[int] = list()
        vec_index800: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_800: int
        scan_index_800: int = 0
        scan_tuple_800_vec: List[int] = self.index_799[var_796, var_797]
        while scan_index_800 < len(scan_tuple_800_vec):
            scan_tuple_800 = scan_tuple_800_vec[scan_index_800]
            scan_index_800 += 1
            vec_800.append(scan_tuple_800)
        # Program VectorLoop Region
        vec_index800 = 0
        while vec_index800 < len(vec_800):
            var_801 = vec_800[vec_index800]
            vec_index800 += 1
            # Program CheckState Region
            state = self.table_9[(var_796, var_797, var_801)] & 3
            if state == 1:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_803_(self, var_804: int, var_805: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_804_805 = (var_804, var_805)
        prev_state = self.table_6[tuple_804_805]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_6[tuple_804_805] = 0 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_769_(var_804, var_805)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_822_(self, var_823: int, var_824: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_826: List[int] = list()
        vec_index826: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_826: int
        scan_index_826: int = 0
        scan_tuple_826_vec: List[int] = self.index_290[var_823]
        while scan_index_826 < len(scan_tuple_826_vec):
            scan_tuple_826 = scan_tuple_826_vec[scan_index_826]
            scan_index_826 += 1
            vec_826.append(scan_tuple_826)
        # Program VectorLoop Region
        vec_index826 = 0
        while vec_index826 < len(vec_826):
            var_827 = vec_826[vec_index826]
            vec_index826 += 1
            # Program Call Region
            ret = self.proc_828_(var_823, var_827, var_824)

        # Program Return Region
        return False
        return False

    def proc_828_(self, var_829: int, var_830: int, var_831: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_830_831 = (var_830, var_831)
        prev_state = self.table_6[tuple_830_831]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_6[tuple_830_831] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_846_(var_830, var_831)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_803_(var_830, var_831)

        # Program Return Region
        return False
        return False

    def proc_846_(self, var_847: int, var_848: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_850: List[int] = list()
        vec_index850: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_850: int
        scan_index_850: int = 0
        scan_tuple_850_vec: List[int] = self.index_291[var_848]
        while scan_index_850 < len(scan_tuple_850_vec):
            scan_tuple_850 = scan_tuple_850_vec[scan_index_850]
            scan_index_850 += 1
            vec_850.append(scan_tuple_850)
        # Program VectorLoop Region
        vec_index850 = 0
        while vec_index850 < len(vec_850):
            var_851 = vec_850[vec_index850]
            vec_index850 += 1
            # Program Call Region
            ret = self.proc_828_(var_848, var_847, var_851)

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
        tuple_vec: List[int] = self.index_752[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_753_(param_0, param_1):
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
        tuple_vec: List[int] = self.index_756[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_757_(param_0, param_1):
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
        tuple_vec: List[int] = self.index_760[param_0]
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

