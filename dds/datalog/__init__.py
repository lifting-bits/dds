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
        self.index_287: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_707: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_9: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_729: DefaultDict[Tuple[int, int], List[int]] = defaultdict(list)

        self.table_13: DefaultDict[int, int] = defaultdict(int)

        self.table_15: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_711: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_18: DefaultDict[int, int] = defaultdict(int)
        self.index_277 = self.table_18

        self.table_20: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_715: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_23: DefaultDict[bytes, int] = defaultdict(int)

        self.table_25: DefaultDict[int, int] = defaultdict(int)

        self.table_27: DefaultDict[Tuple[bytes, int], int] = defaultdict(int)
        self.index_716: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_30: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_158: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_33: DefaultDict[bytes, int] = defaultdict(int)
        self.index_112 = self.table_33

        self.table_35: DefaultDict[Tuple[int, bytes], int] = defaultdict(int)
        self.index_113: DefaultDict[bytes, List[int]] = defaultdict(list)

        self.table_38: DefaultDict[int, int] = defaultdict(int)
        self.index_253 = self.table_38

        self.table_40: DefaultDict[int, int] = defaultdict(int)
        self.index_254 = self.table_40

        self.table_42: DefaultDict[int, int] = defaultdict(int)
        self.index_172 = self.table_42

        self.table_44: DefaultDict[int, int] = defaultdict(int)
        self.index_140 = self.table_44

        self.table_46: DefaultDict[int, int] = defaultdict(int)
        self.index_134 = self.table_46

        self.table_48: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_262: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_51: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_267: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_54: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_288: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_749: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_57: DefaultDict[Tuple[int, int, int], int] = defaultdict(int)
        self.index_139: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        self.table_61: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_217: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_64: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_459 = self.table_64
        self.index_464: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_67: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_460 = self.table_67
        self.index_465: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_70: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_205: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_73: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_129: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_76: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_180: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_79: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_199: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_82: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_241: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_85: DefaultDict[int, int] = defaultdict(int)
        self.index_128 = self.table_85

        self.table_87: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_181: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_90: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_229: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_93: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_187: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_96: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_276: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_99: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_282: DefaultDict[int, List[int]] = defaultdict(list)

        self.var_0: int = 5
        self.var_1: int = 2
        self.var_2: int = 1
        self.var_3: int = 6
        self.var_4: int = 6
        self.var_5: int = 0
        self.init_102_()

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

    def init_102_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False
        return False

    def section_4(self, vec_104: List[Tuple[bytes, int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index104: int = 0
        vec_109: List[bytes] = list()
        vec_index109: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index104 = 0
        while vec_index104 < len(vec_104):
            var_105, var_106, var_107, var_108 = vec_104[vec_index104]
            vec_index104 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_105 = var_105
            prev_state = self.table_33[tuple_105]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_33[tuple_105] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_109.append(var_105)
            # Program TransitionState Region
            tuple_105 = var_105
            prev_state = self.table_23[tuple_105]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_23[tuple_105] = 1 | 4
                if not present_bit:
                    pass
        # Program VectorUnique Region
        vec_109 = list(set(vec_109))
        vec_index109 = 0
        # Program TableJoin Region
        while vec_index109 < len(vec_109):
            var_111 = vec_109[vec_index109]
            vec_index109 += 1
            if var_111 in self.index_112:
                tuple_110_1_index: int = 0
                tuple_110_1_vec: List[int] = self.index_113[var_111]
                while tuple_110_1_index < len(tuple_110_1_vec):
                    tuple_110_1 = tuple_110_1_vec[tuple_110_1_index]
                    tuple_110_1_index += 1
                    var_114 = tuple_110_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_111_114 = (var_111, var_114)
                    prev_state = self.table_27[tuple_111_114]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_27[tuple_111_114] = 1 | 4
                        if not present_bit:
                            self.index_716[tuple_111_114[0]].append(tuple_111_114[1])
        # Program VectorClear Region
        del vec_109[:]
        vec_index109 = 0
        # Program Return Region
        return False
        return False

    def instruction_4(self, vec_116: List[Tuple[int, int, bytes, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index116: int = 0
        vec_121: List[bytes] = list()
        vec_index121: int = 0
        vec_125: List[int] = list()
        vec_index125: int = 0
        vec_131: List[int] = list()
        vec_index131: int = 0
        vec_136: List[int] = list()
        vec_index136: int = 0
        vec_155: List[Tuple[int, int]] = list()
        vec_index155: int = 0
        vec_159: List[int] = list()
        vec_index159: int = 0
        vec_169: List[int] = list()
        vec_index169: int = 0
        vec_173: List[int] = list()
        vec_index173: int = 0
        vec_177: List[int] = list()
        vec_index177: int = 0
        vec_184: List[int] = list()
        vec_index184: int = 0
        vec_192: List[int] = list()
        vec_index192: int = 0
        vec_196: List[int] = list()
        vec_index196: int = 0
        vec_202: List[int] = list()
        vec_index202: int = 0
        vec_210: List[int] = list()
        vec_index210: int = 0
        vec_214: List[int] = list()
        vec_index214: int = 0
        vec_222: List[int] = list()
        vec_index222: int = 0
        vec_226: List[int] = list()
        vec_index226: int = 0
        vec_234: List[int] = list()
        vec_index234: int = 0
        vec_238: List[int] = list()
        vec_index238: int = 0
        vec_246: List[int] = list()
        vec_index246: int = 0
        vec_250: List[int] = list()
        vec_index250: int = 0
        vec_255: List[int] = list()
        vec_index255: int = 0
        vec_259: List[int] = list()
        vec_index259: int = 0
        vec_264: List[int] = list()
        vec_index264: int = 0
        vec_269: List[int] = list()
        vec_index269: int = 0
        vec_273: List[int] = list()
        vec_index273: int = 0
        vec_279: List[int] = list()
        vec_index279: int = 0
        vec_284: List[int] = list()
        vec_index284: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index116 = 0
        while vec_index116 < len(vec_116):
            var_117, var_118, var_119, var_120 = vec_116[vec_index116]
            vec_index116 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_117 = var_117
            prev_state = self.table_44[tuple_117]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_44[tuple_117] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_169.append(var_117)
                # Program VectorAppend Region
                vec_136.append(var_117)
                # Program VectorAppend Region
                vec_214.append(var_117)
                # Program VectorAppend Region
                vec_202.append(var_117)
                # Program VectorAppend Region
                vec_238.append(var_117)
                # Program VectorAppend Region
                vec_226.append(var_117)
                # Program VectorAppend Region
                vec_184.append(var_117)
            # Program TransitionState Region
            tuple_117_120 = (var_117, var_120)
            prev_state = self.table_35[tuple_117_120]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_35[tuple_117_120] = 1 | 4
                if not present_bit:
                    self.index_113[tuple_117_120[1]].append(tuple_117_120[0])
                # Program VectorAppend Region
                vec_121.append(var_120)
            # Program TupleCompare Region
            if self.var_1 == var_118:
                # Program TransitionState Region
                tuple_117 = var_117
                prev_state = self.table_46[tuple_117]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_46[tuple_117] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_259.append(var_117)
                    # Program VectorAppend Region
                    vec_131.append(var_117)
            # Program TupleCompare Region
            if self.var_4 == var_118:
                # Program TransitionState Region
                tuple_117 = var_117
                prev_state = self.table_85[tuple_117]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_85[tuple_117] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_125.append(var_117)
            # Program TransitionState Region
            tuple_117 = var_117
            prev_state = self.table_25[tuple_117]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_25[tuple_117] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_117 = var_117
            prev_state = self.table_44[tuple_117]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_44[tuple_117] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_169.append(var_117)
                # Program VectorAppend Region
                vec_136.append(var_117)
                # Program VectorAppend Region
                vec_214.append(var_117)
                # Program VectorAppend Region
                vec_202.append(var_117)
                # Program VectorAppend Region
                vec_238.append(var_117)
                # Program VectorAppend Region
                vec_226.append(var_117)
                # Program VectorAppend Region
                vec_184.append(var_117)
            # Program TupleCompare Region
            if self.var_1 == var_118:
                # Program TransitionState Region
                tuple_117 = var_117
                prev_state = self.table_46[tuple_117]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_46[tuple_117] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_259.append(var_117)
                    # Program VectorAppend Region
                    vec_131.append(var_117)
            # Program TransitionState Region
            tuple_117 = var_117
            prev_state = self.table_44[tuple_117]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_44[tuple_117] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_169.append(var_117)
                # Program VectorAppend Region
                vec_136.append(var_117)
                # Program VectorAppend Region
                vec_214.append(var_117)
                # Program VectorAppend Region
                vec_202.append(var_117)
                # Program VectorAppend Region
                vec_238.append(var_117)
                # Program VectorAppend Region
                vec_226.append(var_117)
                # Program VectorAppend Region
                vec_184.append(var_117)
            # Program TupleCompare Region
            if self.var_1 == var_118:
                # Program TransitionState Region
                tuple_117 = var_117
                prev_state = self.table_46[tuple_117]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_46[tuple_117] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_259.append(var_117)
                    # Program VectorAppend Region
                    vec_131.append(var_117)
            # Program TransitionState Region
            tuple_117 = var_117
            prev_state = self.table_44[tuple_117]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_44[tuple_117] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_169.append(var_117)
                # Program VectorAppend Region
                vec_136.append(var_117)
                # Program VectorAppend Region
                vec_214.append(var_117)
                # Program VectorAppend Region
                vec_202.append(var_117)
                # Program VectorAppend Region
                vec_238.append(var_117)
                # Program VectorAppend Region
                vec_226.append(var_117)
                # Program VectorAppend Region
                vec_184.append(var_117)
            # Program TupleCompare Region
            if self.var_1 == var_118:
                # Program TransitionState Region
                tuple_117 = var_117
                prev_state = self.table_46[tuple_117]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_46[tuple_117] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_259.append(var_117)
                    # Program VectorAppend Region
                    vec_131.append(var_117)
            # Program TransitionState Region
            tuple_117 = var_117
            prev_state = self.table_44[tuple_117]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_44[tuple_117] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_169.append(var_117)
                # Program VectorAppend Region
                vec_136.append(var_117)
                # Program VectorAppend Region
                vec_214.append(var_117)
                # Program VectorAppend Region
                vec_202.append(var_117)
                # Program VectorAppend Region
                vec_238.append(var_117)
                # Program VectorAppend Region
                vec_226.append(var_117)
                # Program VectorAppend Region
                vec_184.append(var_117)
            # Program TupleCompare Region
            if self.var_1 == var_118:
                # Program TransitionState Region
                tuple_117 = var_117
                prev_state = self.table_46[tuple_117]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_46[tuple_117] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_259.append(var_117)
                    # Program VectorAppend Region
                    vec_131.append(var_117)
            # Program TransitionState Region
            tuple_117 = var_117
            prev_state = self.table_44[tuple_117]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_44[tuple_117] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program VectorAppend Region
                vec_169.append(var_117)
                # Program VectorAppend Region
                vec_136.append(var_117)
                # Program VectorAppend Region
                vec_214.append(var_117)
                # Program VectorAppend Region
                vec_202.append(var_117)
                # Program VectorAppend Region
                vec_238.append(var_117)
                # Program VectorAppend Region
                vec_226.append(var_117)
                # Program VectorAppend Region
                vec_184.append(var_117)
            # Program TupleCompare Region
            if self.var_1 == var_118:
                # Program TransitionState Region
                tuple_117 = var_117
                prev_state = self.table_46[tuple_117]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_46[tuple_117] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_259.append(var_117)
                    # Program VectorAppend Region
                    vec_131.append(var_117)
        # Program VectorUnique Region
        vec_121 = list(set(vec_121))
        vec_index121 = 0
        # Program TableJoin Region
        while vec_index121 < len(vec_121):
            var_123 = vec_121[vec_index121]
            vec_index121 += 1
            if var_123 in self.index_112:
                tuple_122_1_index: int = 0
                tuple_122_1_vec: List[int] = self.index_113[var_123]
                while tuple_122_1_index < len(tuple_122_1_vec):
                    tuple_122_1 = tuple_122_1_vec[tuple_122_1_index]
                    tuple_122_1_index += 1
                    var_124 = tuple_122_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_123_124 = (var_123, var_124)
                    prev_state = self.table_27[tuple_123_124]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_27[tuple_123_124] = 1 | 4
                        if not present_bit:
                            self.index_716[tuple_123_124[0]].append(tuple_123_124[1])
        # Program VectorClear Region
        del vec_121[:]
        vec_index121 = 0
        # Program VectorUnique Region
        vec_125 = list(set(vec_125))
        vec_index125 = 0
        # Program TableJoin Region
        while vec_index125 < len(vec_125):
            var_127 = vec_125[vec_index125]
            vec_index125 += 1
            if var_127 in self.index_128:
                tuple_126_1_index: int = 0
                tuple_126_1_vec: List[int] = self.index_129[var_127]
                while tuple_126_1_index < len(tuple_126_1_vec):
                    tuple_126_1 = tuple_126_1_vec[tuple_126_1_index]
                    tuple_126_1_index += 1
                    var_130 = tuple_126_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_127_130 = (var_127, var_130)
                    prev_state = self.table_87[tuple_127_130]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_87[tuple_127_130] = 1 | 4
                        if not present_bit:
                            self.index_181[tuple_127_130[1]].append(tuple_127_130[0])
                        # Program VectorAppend Region
                        vec_177.append(var_130)
        # Program VectorClear Region
        del vec_125[:]
        vec_index125 = 0
        # Program VectorUnique Region
        vec_131 = list(set(vec_131))
        vec_index131 = 0
        # Program TableJoin Region
        while vec_index131 < len(vec_131):
            var_133 = vec_131[vec_index131]
            vec_index131 += 1
            if var_133 in self.index_134:
                tuple_132_1_index: int = 0
                tuple_132_1_vec: List[int] = self.index_129[var_133]
                while tuple_132_1_index < len(tuple_132_1_vec):
                    tuple_132_1 = tuple_132_1_vec[tuple_132_1_index]
                    tuple_132_1_index += 1
                    var_135 = tuple_132_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_133_135 = (var_133, var_135)
                    prev_state = self.table_79[tuple_133_135]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_79[tuple_133_135] = 1 | 4
                        if not present_bit:
                            self.index_199[tuple_133_135[1]].append(tuple_133_135[0])
                        # Program VectorAppend Region
                        vec_196.append(var_135)
        # Program VectorClear Region
        del vec_131[:]
        vec_index131 = 0
        # Program VectorUnique Region
        vec_136 = list(set(vec_136))
        vec_index136 = 0
        # Program TableJoin Region
        while vec_index136 < len(vec_136):
            var_138 = vec_136[vec_index136]
            vec_index136 += 1
            tuple_137_0_index: int = 0
            tuple_137_0_vec: List[Tuple[int, int]] = self.index_139[var_138]
            while tuple_137_0_index < len(tuple_137_0_vec):
                tuple_137_0 = tuple_137_0_vec[tuple_137_0_index]
                tuple_137_0_index += 1
                var_141 = tuple_137_0[0]
                var_142 = tuple_137_0[1]
                if var_138 in self.index_140:
                    # Program TransitionState Region
                    var_141 = self._resolve_edgetype(var_141)
                    tuple_142_138_141 = (var_142, var_138, var_141)
                    prev_state = self.table_9[tuple_142_138_141]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_142_138_141] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_142_138_141[0], tuple_142_138_141[1])].append(tuple_142_138_141[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_138_142 = (var_138, var_142)
                        prev_state = self.table_30[tuple_138_142]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_138_142] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_138_142[0]].append(tuple_138_142[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_138)
                        if not ret:
                            # Program TransitionState Region
                            tuple_138_142 = (var_138, var_142)
                            prev_state = self.table_30[tuple_138_142]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_138_142] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_138_142[0]].append(tuple_138_142[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_142, var_138)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_142_138 = (var_142, var_138)
                                    prev_state = self.table_54[tuple_142_138]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_142_138] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_142_138[0]].append(tuple_142_138[1])
                                            self.index_749[tuple_142_138[1]].append(tuple_142_138[0])
                                        # Program VectorAppend Region
                                        vec_284.append(var_142)
                                # Program TransitionState Region
                                tuple_142_138 = (var_142, var_138)
                                prev_state = self.table_15[tuple_142_138]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_142_138] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_142_138[0]].append(tuple_142_138[1])
                        # Program TransitionState Region
                        tuple_142_138 = (var_142, var_138)
                        prev_state = self.table_96[tuple_142_138]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_142_138] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_142_138[1]].append(tuple_142_138[0])
                            # Program VectorAppend Region
                            vec_273.append(var_138)
                        # Program TransitionState Region
                        tuple_138 = var_138
                        prev_state = self.table_40[tuple_138]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_138] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_250.append(var_138)
                        # Program TupleCompare Region
                        if self.var_0 == var_141:
                            # Program TransitionState Region
                            tuple_138 = var_138
                            prev_state = self.table_18[tuple_138]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_138] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_138_138 = (var_138, var_138)
                                prev_state = self.table_6[tuple_138_138]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_138_138] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_138_138[1]].append(tuple_138_138[0])
                                        self.index_707[tuple_138_138[0]].append(tuple_138_138[1])
                                    # Program VectorAppend Region
                                    vec_155.append((var_138, var_138))
                                # Program VectorAppend Region
                                vec_273.append(var_138)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_159: int
                                scan_index_159: int = 0
                                scan_tuple_159_vec: List[int] = self.index_158[var_138]
                                while scan_index_159 < len(scan_tuple_159_vec):
                                    scan_tuple_159 = scan_tuple_159_vec[scan_index_159]
                                    scan_index_159 += 1
                                    vec_159.append(scan_tuple_159)
                                # Program VectorLoop Region
                                vec_index159 = 0
                                while vec_index159 < len(vec_159):
                                    var_160 = vec_159[vec_index159]
                                    vec_index159 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_138_160 = (var_138, var_160)
                                    prev_state = self.table_30[tuple_138_160]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_138_160] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_138, var_160)

                                        # Program Call Region
                                        ret = self.proc_165_(var_138, var_160)

                        # Program TupleCompare Region
                        if self.var_2 == var_141:
                            # Program TransitionState Region
                            tuple_142_138 = (var_142, var_138)
                            prev_state = self.table_48[tuple_142_138]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_142_138] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_142_138[0]].append(tuple_142_138[1])
                                # Program VectorAppend Region
                                vec_259.append(var_142)
        # Program VectorClear Region
        del vec_136[:]
        vec_index136 = 0
        # Program VectorUnique Region
        vec_169 = list(set(vec_169))
        vec_index169 = 0
        # Program TableJoin Region
        while vec_index169 < len(vec_169):
            var_171 = vec_169[vec_index169]
            vec_index169 += 1
            if var_171 in self.index_172:
                if var_171 in self.index_140:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_171 = var_171
                    prev_state = self.table_18[tuple_171]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_171] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_171_171 = (var_171, var_171)
                        prev_state = self.table_6[tuple_171_171]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_171_171] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_171_171[1]].append(tuple_171_171[0])
                                self.index_707[tuple_171_171[0]].append(tuple_171_171[1])
                            # Program VectorAppend Region
                            vec_155.append((var_171, var_171))
                        # Program VectorAppend Region
                        vec_273.append(var_171)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_173: int
                        scan_index_173: int = 0
                        scan_tuple_173_vec: List[int] = self.index_158[var_171]
                        while scan_index_173 < len(scan_tuple_173_vec):
                            scan_tuple_173 = scan_tuple_173_vec[scan_index_173]
                            scan_index_173 += 1
                            vec_173.append(scan_tuple_173)
                        # Program VectorLoop Region
                        vec_index173 = 0
                        while vec_index173 < len(vec_173):
                            var_174 = vec_173[vec_index173]
                            vec_index173 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_171_174 = (var_171, var_174)
                            prev_state = self.table_30[tuple_171_174]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_171_174] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_171, var_174)

                                # Program Call Region
                                ret = self.proc_165_(var_171, var_174)

        # Program VectorClear Region
        del vec_169[:]
        vec_index169 = 0
        # Program VectorUnique Region
        vec_177 = list(set(vec_177))
        vec_index177 = 0
        # Program TableJoin Region
        while vec_index177 < len(vec_177):
            var_179 = vec_177[vec_index177]
            vec_index177 += 1
            tuple_178_0_index: int = 0
            tuple_178_0_vec: List[int] = self.index_180[var_179]
            while tuple_178_0_index < len(tuple_178_0_vec):
                tuple_178_0 = tuple_178_0_vec[tuple_178_0_index]
                tuple_178_0_index += 1
                var_182 = tuple_178_0
                tuple_178_1_index: int = 0
                tuple_178_1_vec: List[int] = self.index_181[var_179]
                while tuple_178_1_index < len(tuple_178_1_vec):
                    tuple_178_1 = tuple_178_1_vec[tuple_178_1_index]
                    tuple_178_1_index += 1
                    var_183 = tuple_178_1
                    # Program TransitionState Region
                    tuple_182_183 = (var_182, var_183)
                    prev_state = self.table_90[tuple_182_183]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_90[tuple_182_183] = 1 | 4
                        if not present_bit:
                            self.index_229[tuple_182_183[0]].append(tuple_182_183[1])
                        # Program VectorAppend Region
                        vec_226.append(var_182)
        # Program VectorClear Region
        del vec_177[:]
        vec_index177 = 0
        # Program VectorUnique Region
        vec_184 = list(set(vec_184))
        vec_index184 = 0
        # Program TableJoin Region
        while vec_index184 < len(vec_184):
            var_186 = vec_184[vec_index184]
            vec_index184 += 1
            if var_186 in self.index_140:
                tuple_185_1_index: int = 0
                tuple_185_1_vec: List[int] = self.index_187[var_186]
                while tuple_185_1_index < len(tuple_185_1_vec):
                    tuple_185_1 = tuple_185_1_vec[tuple_185_1_index]
                    tuple_185_1_index += 1
                    var_188 = tuple_185_1
                    # Program TransitionState Region
                    tuple_188_186_5 = (var_188, var_186, self.var_5)
                    prev_state = self.table_9[tuple_188_186_5]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_188_186_5] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_188_186_5[0], tuple_188_186_5[1])].append(tuple_188_186_5[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_186_188 = (var_186, var_188)
                        prev_state = self.table_30[tuple_186_188]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_186_188] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_186_188[0]].append(tuple_186_188[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_186)
                        if not ret:
                            # Program TransitionState Region
                            tuple_186_188 = (var_186, var_188)
                            prev_state = self.table_30[tuple_186_188]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_186_188] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_186_188[0]].append(tuple_186_188[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_188, var_186)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_188_186 = (var_188, var_186)
                                    prev_state = self.table_54[tuple_188_186]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_188_186] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_188_186[0]].append(tuple_188_186[1])
                                            self.index_749[tuple_188_186[1]].append(tuple_188_186[0])
                                        # Program VectorAppend Region
                                        vec_284.append(var_188)
                                # Program TransitionState Region
                                tuple_188_186 = (var_188, var_186)
                                prev_state = self.table_15[tuple_188_186]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_188_186] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_188_186[0]].append(tuple_188_186[1])
                        # Program TransitionState Region
                        tuple_188_186 = (var_188, var_186)
                        prev_state = self.table_96[tuple_188_186]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_188_186] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_188_186[1]].append(tuple_188_186[0])
                            # Program VectorAppend Region
                            vec_273.append(var_186)
                        # Program TransitionState Region
                        tuple_186 = var_186
                        prev_state = self.table_40[tuple_186]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_186] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_250.append(var_186)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_5:
                            # Program TransitionState Region
                            tuple_186 = var_186
                            prev_state = self.table_18[tuple_186]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_186] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_186_186 = (var_186, var_186)
                                prev_state = self.table_6[tuple_186_186]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_186_186] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_186_186[1]].append(tuple_186_186[0])
                                        self.index_707[tuple_186_186[0]].append(tuple_186_186[1])
                                    # Program VectorAppend Region
                                    vec_155.append((var_186, var_186))
                                # Program VectorAppend Region
                                vec_273.append(var_186)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_192: int
                                scan_index_192: int = 0
                                scan_tuple_192_vec: List[int] = self.index_158[var_186]
                                while scan_index_192 < len(scan_tuple_192_vec):
                                    scan_tuple_192 = scan_tuple_192_vec[scan_index_192]
                                    scan_index_192 += 1
                                    vec_192.append(scan_tuple_192)
                                # Program VectorLoop Region
                                vec_index192 = 0
                                while vec_index192 < len(vec_192):
                                    var_193 = vec_192[vec_index192]
                                    vec_index192 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_186_193 = (var_186, var_193)
                                    prev_state = self.table_30[tuple_186_193]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_186_193] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_186, var_193)

                                        # Program Call Region
                                        ret = self.proc_165_(var_186, var_193)

                        # Program TupleCompare Region
                        if self.var_2 == self.var_5:
                            # Program TransitionState Region
                            tuple_188_186 = (var_188, var_186)
                            prev_state = self.table_48[tuple_188_186]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_188_186] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_188_186[0]].append(tuple_188_186[1])
                                # Program VectorAppend Region
                                vec_259.append(var_188)
        # Program VectorClear Region
        del vec_184[:]
        vec_index184 = 0
        # Program VectorUnique Region
        vec_196 = list(set(vec_196))
        vec_index196 = 0
        # Program TableJoin Region
        while vec_index196 < len(vec_196):
            var_198 = vec_196[vec_index196]
            vec_index196 += 1
            tuple_197_0_index: int = 0
            tuple_197_0_vec: List[int] = self.index_180[var_198]
            while tuple_197_0_index < len(tuple_197_0_vec):
                tuple_197_0 = tuple_197_0_vec[tuple_197_0_index]
                tuple_197_0_index += 1
                var_200 = tuple_197_0
                tuple_197_1_index: int = 0
                tuple_197_1_vec: List[int] = self.index_199[var_198]
                while tuple_197_1_index < len(tuple_197_1_vec):
                    tuple_197_1 = tuple_197_1_vec[tuple_197_1_index]
                    tuple_197_1_index += 1
                    var_201 = tuple_197_1
                    # Program TransitionState Region
                    tuple_200_201 = (var_200, var_201)
                    prev_state = self.table_82[tuple_200_201]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_82[tuple_200_201] = 1 | 4
                        if not present_bit:
                            self.index_241[tuple_200_201[0]].append(tuple_200_201[1])
                        # Program VectorAppend Region
                        vec_238.append(var_200)
        # Program VectorClear Region
        del vec_196[:]
        vec_index196 = 0
        # Program VectorUnique Region
        vec_202 = list(set(vec_202))
        vec_index202 = 0
        # Program TableJoin Region
        while vec_index202 < len(vec_202):
            var_204 = vec_202[vec_index202]
            vec_index202 += 1
            if var_204 in self.index_140:
                tuple_203_1_index: int = 0
                tuple_203_1_vec: List[int] = self.index_205[var_204]
                while tuple_203_1_index < len(tuple_203_1_vec):
                    tuple_203_1 = tuple_203_1_vec[tuple_203_1_index]
                    tuple_203_1_index += 1
                    var_206 = tuple_203_1
                    # Program TransitionState Region
                    tuple_206_204_3 = (var_206, var_204, self.var_3)
                    prev_state = self.table_9[tuple_206_204_3]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_206_204_3] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_206_204_3[0], tuple_206_204_3[1])].append(tuple_206_204_3[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_204_206 = (var_204, var_206)
                        prev_state = self.table_30[tuple_204_206]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_204_206] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_204_206[0]].append(tuple_204_206[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_204)
                        if not ret:
                            # Program TransitionState Region
                            tuple_204_206 = (var_204, var_206)
                            prev_state = self.table_30[tuple_204_206]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_204_206] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_204_206[0]].append(tuple_204_206[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_206, var_204)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_206_204 = (var_206, var_204)
                                    prev_state = self.table_54[tuple_206_204]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_206_204] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_206_204[0]].append(tuple_206_204[1])
                                            self.index_749[tuple_206_204[1]].append(tuple_206_204[0])
                                        # Program VectorAppend Region
                                        vec_284.append(var_206)
                                # Program TransitionState Region
                                tuple_206_204 = (var_206, var_204)
                                prev_state = self.table_15[tuple_206_204]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_206_204] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_206_204[0]].append(tuple_206_204[1])
                        # Program TransitionState Region
                        tuple_206_204 = (var_206, var_204)
                        prev_state = self.table_96[tuple_206_204]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_206_204] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_206_204[1]].append(tuple_206_204[0])
                            # Program VectorAppend Region
                            vec_273.append(var_204)
                        # Program TransitionState Region
                        tuple_204 = var_204
                        prev_state = self.table_40[tuple_204]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_204] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_250.append(var_204)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_3:
                            # Program TransitionState Region
                            tuple_204 = var_204
                            prev_state = self.table_18[tuple_204]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_204] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_204_204 = (var_204, var_204)
                                prev_state = self.table_6[tuple_204_204]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_204_204] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_204_204[1]].append(tuple_204_204[0])
                                        self.index_707[tuple_204_204[0]].append(tuple_204_204[1])
                                    # Program VectorAppend Region
                                    vec_155.append((var_204, var_204))
                                # Program VectorAppend Region
                                vec_273.append(var_204)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_210: int
                                scan_index_210: int = 0
                                scan_tuple_210_vec: List[int] = self.index_158[var_204]
                                while scan_index_210 < len(scan_tuple_210_vec):
                                    scan_tuple_210 = scan_tuple_210_vec[scan_index_210]
                                    scan_index_210 += 1
                                    vec_210.append(scan_tuple_210)
                                # Program VectorLoop Region
                                vec_index210 = 0
                                while vec_index210 < len(vec_210):
                                    var_211 = vec_210[vec_index210]
                                    vec_index210 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_204_211 = (var_204, var_211)
                                    prev_state = self.table_30[tuple_204_211]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_204_211] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_204, var_211)

                                        # Program Call Region
                                        ret = self.proc_165_(var_204, var_211)

                        # Program TupleCompare Region
                        if self.var_2 == self.var_3:
                            # Program TransitionState Region
                            tuple_206_204 = (var_206, var_204)
                            prev_state = self.table_48[tuple_206_204]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_206_204] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_206_204[0]].append(tuple_206_204[1])
                                # Program VectorAppend Region
                                vec_259.append(var_206)
        # Program VectorClear Region
        del vec_202[:]
        vec_index202 = 0
        # Program VectorUnique Region
        vec_214 = list(set(vec_214))
        vec_index214 = 0
        # Program TableJoin Region
        while vec_index214 < len(vec_214):
            var_216 = vec_214[vec_index214]
            vec_index214 += 1
            if var_216 in self.index_140:
                tuple_215_1_index: int = 0
                tuple_215_1_vec: List[int] = self.index_217[var_216]
                while tuple_215_1_index < len(tuple_215_1_vec):
                    tuple_215_1 = tuple_215_1_vec[tuple_215_1_index]
                    tuple_215_1_index += 1
                    var_218 = tuple_215_1
                    # Program TransitionState Region
                    tuple_218_216_0 = (var_218, var_216, self.var_0)
                    prev_state = self.table_9[tuple_218_216_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_218_216_0] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_218_216_0[0], tuple_218_216_0[1])].append(tuple_218_216_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_216_218 = (var_216, var_218)
                        prev_state = self.table_30[tuple_216_218]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_216_218] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_216_218[0]].append(tuple_216_218[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_216)
                        if not ret:
                            # Program TransitionState Region
                            tuple_216_218 = (var_216, var_218)
                            prev_state = self.table_30[tuple_216_218]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_216_218] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_216_218[0]].append(tuple_216_218[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_218, var_216)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_218_216 = (var_218, var_216)
                                    prev_state = self.table_54[tuple_218_216]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_218_216] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_218_216[0]].append(tuple_218_216[1])
                                            self.index_749[tuple_218_216[1]].append(tuple_218_216[0])
                                        # Program VectorAppend Region
                                        vec_284.append(var_218)
                                # Program TransitionState Region
                                tuple_218_216 = (var_218, var_216)
                                prev_state = self.table_15[tuple_218_216]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_218_216] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_218_216[0]].append(tuple_218_216[1])
                        # Program TransitionState Region
                        tuple_218_216 = (var_218, var_216)
                        prev_state = self.table_96[tuple_218_216]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_218_216] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_218_216[1]].append(tuple_218_216[0])
                            # Program VectorAppend Region
                            vec_273.append(var_216)
                        # Program TransitionState Region
                        tuple_216 = var_216
                        prev_state = self.table_40[tuple_216]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_216] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_250.append(var_216)
                        # Program TransitionState Region
                        tuple_216 = var_216
                        prev_state = self.table_18[tuple_216]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_216] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program TransitionState Region
                            tuple_216_216 = (var_216, var_216)
                            prev_state = self.table_6[tuple_216_216]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_216_216] = 1 | 4
                                if not present_bit:
                                    self.index_287[tuple_216_216[1]].append(tuple_216_216[0])
                                    self.index_707[tuple_216_216[0]].append(tuple_216_216[1])
                                # Program VectorAppend Region
                                vec_155.append((var_216, var_216))
                            # Program VectorAppend Region
                            vec_273.append(var_216)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_222: int
                            scan_index_222: int = 0
                            scan_tuple_222_vec: List[int] = self.index_158[var_216]
                            while scan_index_222 < len(scan_tuple_222_vec):
                                scan_tuple_222 = scan_tuple_222_vec[scan_index_222]
                                scan_index_222 += 1
                                vec_222.append(scan_tuple_222)
                            # Program VectorLoop Region
                            vec_index222 = 0
                            while vec_index222 < len(vec_222):
                                var_223 = vec_222[vec_index222]
                                vec_index222 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_216_223 = (var_216, var_223)
                                prev_state = self.table_30[tuple_216_223]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_30[tuple_216_223] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_161_(var_216, var_223)

                                    # Program Call Region
                                    ret = self.proc_165_(var_216, var_223)

                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_218_216 = (var_218, var_216)
                            prev_state = self.table_48[tuple_218_216]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_218_216] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_218_216[0]].append(tuple_218_216[1])
                                # Program VectorAppend Region
                                vec_259.append(var_218)
        # Program VectorClear Region
        del vec_214[:]
        vec_index214 = 0
        # Program VectorUnique Region
        vec_226 = list(set(vec_226))
        vec_index226 = 0
        # Program TableJoin Region
        while vec_index226 < len(vec_226):
            var_228 = vec_226[vec_index226]
            vec_index226 += 1
            if var_228 in self.index_140:
                tuple_227_1_index: int = 0
                tuple_227_1_vec: List[int] = self.index_229[var_228]
                while tuple_227_1_index < len(tuple_227_1_vec):
                    tuple_227_1 = tuple_227_1_vec[tuple_227_1_index]
                    tuple_227_1_index += 1
                    var_230 = tuple_227_1
                    # Program TransitionState Region
                    tuple_230_228_0 = (var_230, var_228, self.var_0)
                    prev_state = self.table_9[tuple_230_228_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_230_228_0] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_230_228_0[0], tuple_230_228_0[1])].append(tuple_230_228_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_228_230 = (var_228, var_230)
                        prev_state = self.table_30[tuple_228_230]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_228_230] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_228_230[0]].append(tuple_228_230[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_228)
                        if not ret:
                            # Program TransitionState Region
                            tuple_228_230 = (var_228, var_230)
                            prev_state = self.table_30[tuple_228_230]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_228_230] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_228_230[0]].append(tuple_228_230[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_230, var_228)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_230_228 = (var_230, var_228)
                                    prev_state = self.table_54[tuple_230_228]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_230_228] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_230_228[0]].append(tuple_230_228[1])
                                            self.index_749[tuple_230_228[1]].append(tuple_230_228[0])
                                        # Program VectorAppend Region
                                        vec_284.append(var_230)
                                # Program TransitionState Region
                                tuple_230_228 = (var_230, var_228)
                                prev_state = self.table_15[tuple_230_228]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_230_228] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_230_228[0]].append(tuple_230_228[1])
                        # Program TransitionState Region
                        tuple_230_228 = (var_230, var_228)
                        prev_state = self.table_96[tuple_230_228]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_230_228] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_230_228[1]].append(tuple_230_228[0])
                            # Program VectorAppend Region
                            vec_273.append(var_228)
                        # Program TransitionState Region
                        tuple_228 = var_228
                        prev_state = self.table_40[tuple_228]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_228] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_250.append(var_228)
                        # Program TransitionState Region
                        tuple_228 = var_228
                        prev_state = self.table_18[tuple_228]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_228] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program TransitionState Region
                            tuple_228_228 = (var_228, var_228)
                            prev_state = self.table_6[tuple_228_228]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_228_228] = 1 | 4
                                if not present_bit:
                                    self.index_287[tuple_228_228[1]].append(tuple_228_228[0])
                                    self.index_707[tuple_228_228[0]].append(tuple_228_228[1])
                                # Program VectorAppend Region
                                vec_155.append((var_228, var_228))
                            # Program VectorAppend Region
                            vec_273.append(var_228)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_234: int
                            scan_index_234: int = 0
                            scan_tuple_234_vec: List[int] = self.index_158[var_228]
                            while scan_index_234 < len(scan_tuple_234_vec):
                                scan_tuple_234 = scan_tuple_234_vec[scan_index_234]
                                scan_index_234 += 1
                                vec_234.append(scan_tuple_234)
                            # Program VectorLoop Region
                            vec_index234 = 0
                            while vec_index234 < len(vec_234):
                                var_235 = vec_234[vec_index234]
                                vec_index234 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_228_235 = (var_228, var_235)
                                prev_state = self.table_30[tuple_228_235]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_30[tuple_228_235] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_161_(var_228, var_235)

                                    # Program Call Region
                                    ret = self.proc_165_(var_228, var_235)

                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_230_228 = (var_230, var_228)
                            prev_state = self.table_48[tuple_230_228]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_230_228] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_230_228[0]].append(tuple_230_228[1])
                                # Program VectorAppend Region
                                vec_259.append(var_230)
        # Program VectorClear Region
        del vec_226[:]
        vec_index226 = 0
        # Program VectorUnique Region
        vec_238 = list(set(vec_238))
        vec_index238 = 0
        # Program TableJoin Region
        while vec_index238 < len(vec_238):
            var_240 = vec_238[vec_index238]
            vec_index238 += 1
            if var_240 in self.index_140:
                tuple_239_1_index: int = 0
                tuple_239_1_vec: List[int] = self.index_241[var_240]
                while tuple_239_1_index < len(tuple_239_1_vec):
                    tuple_239_1 = tuple_239_1_vec[tuple_239_1_index]
                    tuple_239_1_index += 1
                    var_242 = tuple_239_1
                    # Program TransitionState Region
                    tuple_242_240_2 = (var_242, var_240, self.var_2)
                    prev_state = self.table_9[tuple_242_240_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_242_240_2] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_242_240_2[0], tuple_242_240_2[1])].append(tuple_242_240_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_240_242 = (var_240, var_242)
                        prev_state = self.table_30[tuple_240_242]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_240_242] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_240_242[0]].append(tuple_240_242[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_240)
                        if not ret:
                            # Program TransitionState Region
                            tuple_240_242 = (var_240, var_242)
                            prev_state = self.table_30[tuple_240_242]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_240_242] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_240_242[0]].append(tuple_240_242[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_242, var_240)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_242_240 = (var_242, var_240)
                                    prev_state = self.table_54[tuple_242_240]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_242_240] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_242_240[0]].append(tuple_242_240[1])
                                            self.index_749[tuple_242_240[1]].append(tuple_242_240[0])
                                        # Program VectorAppend Region
                                        vec_284.append(var_242)
                                # Program TransitionState Region
                                tuple_242_240 = (var_242, var_240)
                                prev_state = self.table_15[tuple_242_240]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_242_240] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_242_240[0]].append(tuple_242_240[1])
                        # Program TransitionState Region
                        tuple_242_240 = (var_242, var_240)
                        prev_state = self.table_96[tuple_242_240]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_242_240] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_242_240[1]].append(tuple_242_240[0])
                            # Program VectorAppend Region
                            vec_273.append(var_240)
                        # Program TransitionState Region
                        tuple_240 = var_240
                        prev_state = self.table_40[tuple_240]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_240] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_250.append(var_240)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_240 = var_240
                            prev_state = self.table_18[tuple_240]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_240] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_240_240 = (var_240, var_240)
                                prev_state = self.table_6[tuple_240_240]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_240_240] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_240_240[1]].append(tuple_240_240[0])
                                        self.index_707[tuple_240_240[0]].append(tuple_240_240[1])
                                    # Program VectorAppend Region
                                    vec_155.append((var_240, var_240))
                                # Program VectorAppend Region
                                vec_273.append(var_240)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_246: int
                                scan_index_246: int = 0
                                scan_tuple_246_vec: List[int] = self.index_158[var_240]
                                while scan_index_246 < len(scan_tuple_246_vec):
                                    scan_tuple_246 = scan_tuple_246_vec[scan_index_246]
                                    scan_index_246 += 1
                                    vec_246.append(scan_tuple_246)
                                # Program VectorLoop Region
                                vec_index246 = 0
                                while vec_index246 < len(vec_246):
                                    var_247 = vec_246[vec_index246]
                                    vec_index246 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_240_247 = (var_240, var_247)
                                    prev_state = self.table_30[tuple_240_247]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_240_247] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_240, var_247)

                                        # Program Call Region
                                        ret = self.proc_165_(var_240, var_247)

                        # Program TransitionState Region
                        tuple_242_240 = (var_242, var_240)
                        prev_state = self.table_48[tuple_242_240]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_48[tuple_242_240] = 1 | 4
                            if not present_bit:
                                self.index_262[tuple_242_240[0]].append(tuple_242_240[1])
                            # Program VectorAppend Region
                            vec_259.append(var_242)
        # Program VectorClear Region
        del vec_238[:]
        vec_index238 = 0
        # Program VectorUnique Region
        vec_250 = list(set(vec_250))
        vec_index250 = 0
        # Program TableJoin Region
        while vec_index250 < len(vec_250):
            var_252 = vec_250[vec_index250]
            vec_index250 += 1
            if var_252 in self.index_253:
                if var_252 in self.index_254:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_252 = var_252
                    prev_state = self.table_18[tuple_252]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_252] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_252_252 = (var_252, var_252)
                        prev_state = self.table_6[tuple_252_252]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_252_252] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_252_252[1]].append(tuple_252_252[0])
                                self.index_707[tuple_252_252[0]].append(tuple_252_252[1])
                            # Program VectorAppend Region
                            vec_155.append((var_252, var_252))
                        # Program VectorAppend Region
                        vec_273.append(var_252)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_255: int
                        scan_index_255: int = 0
                        scan_tuple_255_vec: List[int] = self.index_158[var_252]
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
                            tuple_252_256 = (var_252, var_256)
                            prev_state = self.table_30[tuple_252_256]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_252_256] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_252, var_256)

                                # Program Call Region
                                ret = self.proc_165_(var_252, var_256)

        # Program VectorClear Region
        del vec_250[:]
        vec_index250 = 0
        # Program VectorUnique Region
        vec_259 = list(set(vec_259))
        vec_index259 = 0
        # Program TableJoin Region
        while vec_index259 < len(vec_259):
            var_261 = vec_259[vec_index259]
            vec_index259 += 1
            if var_261 in self.index_134:
                tuple_260_1_index: int = 0
                tuple_260_1_vec: List[int] = self.index_262[var_261]
                while tuple_260_1_index < len(tuple_260_1_vec):
                    tuple_260_1 = tuple_260_1_vec[tuple_260_1_index]
                    tuple_260_1_index += 1
                    var_263 = tuple_260_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_261_263 = (var_261, var_263)
                    prev_state = self.table_51[tuple_261_263]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_261_263] = 1 | 4
                        if not present_bit:
                            self.index_267[tuple_261_263[1]].append(tuple_261_263[0])
                        # Program VectorAppend Region
                        vec_264.append(var_263)
        # Program VectorClear Region
        del vec_259[:]
        vec_index259 = 0
        # Program VectorUnique Region
        vec_264 = list(set(vec_264))
        vec_index264 = 0
        # Program TableJoin Region
        while vec_index264 < len(vec_264):
            var_266 = vec_264[vec_index264]
            vec_index264 += 1
            if var_266 in self.index_253:
                tuple_265_1_index: int = 0
                tuple_265_1_vec: List[int] = self.index_267[var_266]
                while tuple_265_1_index < len(tuple_265_1_vec):
                    tuple_265_1 = tuple_265_1_vec[tuple_265_1_index]
                    tuple_265_1_index += 1
                    var_268 = tuple_265_1
                    # Program TransitionState Region
                    tuple_268 = var_268
                    prev_state = self.table_18[tuple_268]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_268] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_268_268 = (var_268, var_268)
                        prev_state = self.table_6[tuple_268_268]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_268_268] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_268_268[1]].append(tuple_268_268[0])
                                self.index_707[tuple_268_268[0]].append(tuple_268_268[1])
                            # Program VectorAppend Region
                            vec_155.append((var_268, var_268))
                        # Program VectorAppend Region
                        vec_273.append(var_268)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_269: int
                        scan_index_269: int = 0
                        scan_tuple_269_vec: List[int] = self.index_158[var_268]
                        while scan_index_269 < len(scan_tuple_269_vec):
                            scan_tuple_269 = scan_tuple_269_vec[scan_index_269]
                            scan_index_269 += 1
                            vec_269.append(scan_tuple_269)
                        # Program VectorLoop Region
                        vec_index269 = 0
                        while vec_index269 < len(vec_269):
                            var_270 = vec_269[vec_index269]
                            vec_index269 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_268_270 = (var_268, var_270)
                            prev_state = self.table_30[tuple_268_270]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_268_270] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_268, var_270)

                                # Program Call Region
                                ret = self.proc_165_(var_268, var_270)

        # Program VectorClear Region
        del vec_264[:]
        vec_index264 = 0
        # Program VectorUnique Region
        vec_273 = list(set(vec_273))
        vec_index273 = 0
        # Program TableJoin Region
        while vec_index273 < len(vec_273):
            var_275 = vec_273[vec_index273]
            vec_index273 += 1
            tuple_274_0_index: int = 0
            tuple_274_0_vec: List[int] = self.index_276[var_275]
            while tuple_274_0_index < len(tuple_274_0_vec):
                tuple_274_0 = tuple_274_0_vec[tuple_274_0_index]
                tuple_274_0_index += 1
                var_278 = tuple_274_0
                if var_275 in self.index_277:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_278_275 = (var_278, var_275)
                    prev_state = self.table_99[tuple_278_275]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_99[tuple_278_275] = 1 | 4
                        if not present_bit:
                            self.index_282[tuple_278_275[1]].append(tuple_278_275[0])
                        # Program VectorAppend Region
                        vec_279.append(var_275)
                    # Program TransitionState Region
                    tuple_278_275 = (var_278, var_275)
                    prev_state = self.table_20[tuple_278_275]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_278_275] = 1 | 4
                        if not present_bit:
                            self.index_715[tuple_278_275[0]].append(tuple_278_275[1])
        # Program VectorClear Region
        del vec_273[:]
        vec_index273 = 0
        # Program VectorUnique Region
        vec_279 = list(set(vec_279))
        vec_index279 = 0
        # Program TableJoin Region
        while vec_index279 < len(vec_279):
            var_281 = vec_279[vec_index279]
            vec_index279 += 1
            tuple_280_0_index: int = 0
            tuple_280_0_vec: List[int] = self.index_282[var_281]
            while tuple_280_0_index < len(tuple_280_0_vec):
                tuple_280_0 = tuple_280_0_vec[tuple_280_0_index]
                tuple_280_0_index += 1
                var_283 = tuple_280_0
                if var_281 in self.index_253:
                    # Program TransitionState Region
                    tuple_283 = var_283
                    prev_state = self.table_13[tuple_283]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_283] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_279[:]
        vec_index279 = 0
        # Program VectorUnique Region
        vec_284 = list(set(vec_284))
        vec_index284 = 0
        # Program TableJoin Region
        while vec_index284 < len(vec_284):
            var_286 = vec_284[vec_index284]
            vec_index284 += 1
            tuple_285_0_index: int = 0
            tuple_285_0_vec: List[int] = self.index_287[var_286]
            while tuple_285_0_index < len(tuple_285_0_vec):
                tuple_285_0 = tuple_285_0_vec[tuple_285_0_index]
                tuple_285_0_index += 1
                var_289 = tuple_285_0
                tuple_285_1_index: int = 0
                tuple_285_1_vec: List[int] = self.index_288[var_286]
                while tuple_285_1_index < len(tuple_285_1_vec):
                    tuple_285_1 = tuple_285_1_vec[tuple_285_1_index]
                    tuple_285_1_index += 1
                    var_290 = tuple_285_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_291_(var_289, var_286)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_147_(var_286, var_290)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_296_(var_289, var_290)
                            if not ret:
                                # Program TransitionState Region
                                tuple_289_290 = (var_289, var_290)
                                prev_state = self.table_6[tuple_289_290]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_289_290] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_289_290[1]].append(tuple_289_290[0])
                                        self.index_707[tuple_289_290[0]].append(tuple_289_290[1])
                                    # Program VectorAppend Region
                                    vec_155.append((var_289, var_290))
        # Program VectorClear Region
        del vec_284[:]
        vec_index284 = 0
        # Induction Fixpoint Loop Region
        while len(vec_155):
            # Program Call Region
            param_157_0 = [vec_155]
            ret = self.proc_151_(param_157_0)
            vec_155 = param_157_0[0]

        vec_index155 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_155[:]
        vec_index155 = 0
        # Program Return Region
        return False
        return False

    def proc_144_(self, var_145: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_18[var_145] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_145 = var_145
            prev_state = self.table_18[tuple_145]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_18[tuple_145] = 0 | 4
        # Program Return Region
        return False
        return False

    def proc_147_(self, var_148: int, var_149: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_54[(var_148, var_149)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_148_149 = (var_148, var_149)
            prev_state = self.table_54[tuple_148_149]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_54[tuple_148_149] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_717_(var_149, var_148)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_148_149 = (var_148, var_149)
                    prev_state = self.table_54[tuple_148_149]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_54[tuple_148_149] = 1 | 4
                        if not present_bit:
                            self.index_288[tuple_148_149[0]].append(tuple_148_149[1])
                            self.index_749[tuple_148_149[1]].append(tuple_148_149[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_151_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_152 = param_0[0]
        vec_index152: int = 0
        vec_300: List[Tuple[int, int]] = list()
        vec_index300: int = 0
        vec_303: List[int] = list()
        vec_index303: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_152, vec_300 = vec_300, vec_152
        # Program VectorLoop Region
        while vec_index300 < len(vec_300):
            var_301, var_302 = vec_300[vec_index300]
            vec_index300 += 1
            # Program VectorAppend Region
            vec_303.append(var_302)
        # Program VectorUnique Region
        vec_303 = list(set(vec_303))
        vec_index303 = 0
        # Program TableJoin Region
        while vec_index303 < len(vec_303):
            var_305 = vec_303[vec_index303]
            vec_index303 += 1
            tuple_304_0_index: int = 0
            tuple_304_0_vec: List[int] = self.index_287[var_305]
            while tuple_304_0_index < len(tuple_304_0_vec):
                tuple_304_0 = tuple_304_0_vec[tuple_304_0_index]
                tuple_304_0_index += 1
                var_306 = tuple_304_0
                tuple_304_1_index: int = 0
                tuple_304_1_vec: List[int] = self.index_288[var_305]
                while tuple_304_1_index < len(tuple_304_1_vec):
                    tuple_304_1 = tuple_304_1_vec[tuple_304_1_index]
                    tuple_304_1_index += 1
                    var_307 = tuple_304_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_291_(var_306, var_305)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_147_(var_305, var_307)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_296_(var_306, var_307)
                            if not ret:
                                # Program TransitionState Region
                                tuple_306_307 = (var_306, var_307)
                                prev_state = self.table_6[tuple_306_307]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_306_307] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_306_307[1]].append(tuple_306_307[0])
                                        self.index_707[tuple_306_307[0]].append(tuple_306_307[1])
                                    # Program VectorAppend Region
                                    vec_152.append((var_306, var_307))
        # Program VectorClear Region
        del vec_303[:]
        vec_index303 = 0
        # Program VectorClear Region
        del vec_300[:]
        vec_index300 = 0
        # Program Return Region
        param_0[0] = vec_152
        return False
        return False

    def proc_161_(self, var_162: int, var_163: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_163_162 = (var_163, var_162)
        prev_state = self.table_54[tuple_163_162]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_54[tuple_163_162] = 2 | 4
            # Program Call Region
            ret = self.proc_778_(var_163, var_162)

        # Program Return Region
        return False
        return False

    def proc_165_(self, var_166: int, var_167: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_167_166 = (var_167, var_166)
        prev_state = self.table_15[tuple_167_166]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_15[tuple_167_166] = 2 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_717_(var_166, var_167)

        # Program Return Region
        return False
        return False

    def proc_291_(self, var_292: int, var_293: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_292, var_293)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_292_293 = (var_292, var_293)
            prev_state = self.table_6[tuple_292_293]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_292_293] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_759_(var_292, var_293)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_292_293 = (var_292, var_293)
                    prev_state = self.table_6[tuple_292_293]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_292_293] = 1 | 4
                        if not present_bit:
                            self.index_287[tuple_292_293[1]].append(tuple_292_293[0])
                            self.index_707[tuple_292_293[0]].append(tuple_292_293[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_296_(self, var_297: int, var_298: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_297, var_298)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_297_298 = (var_297, var_298)
            prev_state = self.table_6[tuple_297_298]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_297_298] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_744_(var_297, var_298)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_297_298 = (var_297, var_298)
                    prev_state = self.table_6[tuple_297_298]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_297_298] = 1 | 4
                        if not present_bit:
                            self.index_287[tuple_297_298[1]].append(tuple_297_298[0])
                            self.index_707[tuple_297_298[0]].append(tuple_297_298[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def external_symbol_2(self, vec_314: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index314: int = 0
        vec_317: List[int] = list()
        vec_index317: int = 0
        vec_325: List[Tuple[int, int]] = list()
        vec_index325: int = 0
        vec_328: List[int] = list()
        vec_index328: int = 0
        vec_332: List[int] = list()
        vec_index332: int = 0
        vec_335: List[int] = list()
        vec_index335: int = 0
        vec_339: List[int] = list()
        vec_index339: int = 0
        vec_346: List[int] = list()
        vec_index346: int = 0
        vec_350: List[int] = list()
        vec_index350: int = 0
        vec_357: List[int] = list()
        vec_index357: int = 0
        vec_361: List[int] = list()
        vec_index361: int = 0
        vec_368: List[int] = list()
        vec_index368: int = 0
        vec_372: List[int] = list()
        vec_index372: int = 0
        vec_379: List[int] = list()
        vec_index379: int = 0
        vec_383: List[int] = list()
        vec_index383: int = 0
        vec_390: List[int] = list()
        vec_index390: int = 0
        vec_394: List[int] = list()
        vec_index394: int = 0
        vec_397: List[int] = list()
        vec_index397: int = 0
        vec_401: List[int] = list()
        vec_index401: int = 0
        vec_405: List[int] = list()
        vec_index405: int = 0
        vec_409: List[int] = list()
        vec_index409: int = 0
        vec_413: List[int] = list()
        vec_index413: int = 0
        vec_417: List[int] = list()
        vec_index417: int = 0
        vec_425: List[int] = list()
        vec_index425: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index314 = 0
        while vec_index314 < len(vec_314):
            var_315, var_316 = vec_314[vec_index314]
            vec_index314 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_315 = var_315
            prev_state = self.table_38[tuple_315]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_315] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_315 = var_315
                prev_state = self.table_44[tuple_315]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_44[tuple_315] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_332.append(var_315)
                    # Program VectorAppend Region
                    vec_317.append(var_315)
                    # Program VectorAppend Region
                    vec_361.append(var_315)
                    # Program VectorAppend Region
                    vec_350.append(var_315)
                    # Program VectorAppend Region
                    vec_383.append(var_315)
                    # Program VectorAppend Region
                    vec_372.append(var_315)
                    # Program VectorAppend Region
                    vec_339.append(var_315)
                # Program VectorAppend Region
                vec_394.append(var_315)
                # Program VectorAppend Region
                vec_405.append(var_315)
                # Program VectorAppend Region
                vec_425.append(var_315)
            # Program TransitionState Region
            tuple_315 = var_315
            prev_state = self.table_38[tuple_315]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_315] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_315 = var_315
                prev_state = self.table_44[tuple_315]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_44[tuple_315] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_332.append(var_315)
                    # Program VectorAppend Region
                    vec_317.append(var_315)
                    # Program VectorAppend Region
                    vec_361.append(var_315)
                    # Program VectorAppend Region
                    vec_350.append(var_315)
                    # Program VectorAppend Region
                    vec_383.append(var_315)
                    # Program VectorAppend Region
                    vec_372.append(var_315)
                    # Program VectorAppend Region
                    vec_339.append(var_315)
                # Program VectorAppend Region
                vec_394.append(var_315)
                # Program VectorAppend Region
                vec_405.append(var_315)
                # Program VectorAppend Region
                vec_425.append(var_315)
            # Program TransitionState Region
            tuple_315 = var_315
            prev_state = self.table_38[tuple_315]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_315] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_315 = var_315
                prev_state = self.table_44[tuple_315]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_44[tuple_315] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_332.append(var_315)
                    # Program VectorAppend Region
                    vec_317.append(var_315)
                    # Program VectorAppend Region
                    vec_361.append(var_315)
                    # Program VectorAppend Region
                    vec_350.append(var_315)
                    # Program VectorAppend Region
                    vec_383.append(var_315)
                    # Program VectorAppend Region
                    vec_372.append(var_315)
                    # Program VectorAppend Region
                    vec_339.append(var_315)
                # Program VectorAppend Region
                vec_394.append(var_315)
                # Program VectorAppend Region
                vec_405.append(var_315)
                # Program VectorAppend Region
                vec_425.append(var_315)
            # Program TransitionState Region
            tuple_315 = var_315
            prev_state = self.table_38[tuple_315]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_38[tuple_315] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_315 = var_315
                prev_state = self.table_44[tuple_315]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_44[tuple_315] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_332.append(var_315)
                    # Program VectorAppend Region
                    vec_317.append(var_315)
                    # Program VectorAppend Region
                    vec_361.append(var_315)
                    # Program VectorAppend Region
                    vec_350.append(var_315)
                    # Program VectorAppend Region
                    vec_383.append(var_315)
                    # Program VectorAppend Region
                    vec_372.append(var_315)
                    # Program VectorAppend Region
                    vec_339.append(var_315)
                # Program VectorAppend Region
                vec_394.append(var_315)
                # Program VectorAppend Region
                vec_405.append(var_315)
                # Program VectorAppend Region
                vec_425.append(var_315)
        # Program VectorUnique Region
        vec_317 = list(set(vec_317))
        vec_index317 = 0
        # Program TableJoin Region
        while vec_index317 < len(vec_317):
            var_319 = vec_317[vec_index317]
            vec_index317 += 1
            tuple_318_0_index: int = 0
            tuple_318_0_vec: List[Tuple[int, int]] = self.index_139[var_319]
            while tuple_318_0_index < len(tuple_318_0_vec):
                tuple_318_0 = tuple_318_0_vec[tuple_318_0_index]
                tuple_318_0_index += 1
                var_320 = tuple_318_0[0]
                var_321 = tuple_318_0[1]
                if var_319 in self.index_140:
                    # Program TransitionState Region
                    var_320 = self._resolve_edgetype(var_320)
                    tuple_321_319_320 = (var_321, var_319, var_320)
                    prev_state = self.table_9[tuple_321_319_320]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_321_319_320] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_321_319_320[0], tuple_321_319_320[1])].append(tuple_321_319_320[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_319_321 = (var_319, var_321)
                        prev_state = self.table_30[tuple_319_321]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_319_321] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_319_321[0]].append(tuple_319_321[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_319)
                        if not ret:
                            # Program TransitionState Region
                            tuple_319_321 = (var_319, var_321)
                            prev_state = self.table_30[tuple_319_321]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_319_321] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_319_321[0]].append(tuple_319_321[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_321, var_319)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_321_319 = (var_321, var_319)
                                    prev_state = self.table_54[tuple_321_319]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_321_319] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_321_319[0]].append(tuple_321_319[1])
                                            self.index_749[tuple_321_319[1]].append(tuple_321_319[0])
                                        # Program VectorAppend Region
                                        vec_417.append(var_321)
                                # Program TransitionState Region
                                tuple_321_319 = (var_321, var_319)
                                prev_state = self.table_15[tuple_321_319]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_321_319] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_321_319[0]].append(tuple_321_319[1])
                        # Program TransitionState Region
                        tuple_321_319 = (var_321, var_319)
                        prev_state = self.table_96[tuple_321_319]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_321_319] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_321_319[1]].append(tuple_321_319[0])
                            # Program VectorAppend Region
                            vec_413.append(var_319)
                        # Program TransitionState Region
                        tuple_319 = var_319
                        prev_state = self.table_40[tuple_319]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_319] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_394.append(var_319)
                        # Program TupleCompare Region
                        if self.var_0 == var_320:
                            # Program TransitionState Region
                            tuple_319 = var_319
                            prev_state = self.table_18[tuple_319]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_319] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_319_319 = (var_319, var_319)
                                prev_state = self.table_6[tuple_319_319]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_319_319] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_319_319[1]].append(tuple_319_319[0])
                                        self.index_707[tuple_319_319[0]].append(tuple_319_319[1])
                                    # Program VectorAppend Region
                                    vec_325.append((var_319, var_319))
                                # Program VectorAppend Region
                                vec_413.append(var_319)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_328: int
                                scan_index_328: int = 0
                                scan_tuple_328_vec: List[int] = self.index_158[var_319]
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
                                    tuple_319_329 = (var_319, var_329)
                                    prev_state = self.table_30[tuple_319_329]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_319_329] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_319, var_329)

                                        # Program Call Region
                                        ret = self.proc_165_(var_319, var_329)

                        # Program TupleCompare Region
                        if self.var_2 == var_320:
                            # Program TransitionState Region
                            tuple_321_319 = (var_321, var_319)
                            prev_state = self.table_48[tuple_321_319]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_321_319] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_321_319[0]].append(tuple_321_319[1])
                                # Program VectorAppend Region
                                vec_401.append(var_321)
        # Program VectorClear Region
        del vec_317[:]
        vec_index317 = 0
        # Program VectorUnique Region
        vec_332 = list(set(vec_332))
        vec_index332 = 0
        # Program TableJoin Region
        while vec_index332 < len(vec_332):
            var_334 = vec_332[vec_index332]
            vec_index332 += 1
            if var_334 in self.index_172:
                if var_334 in self.index_140:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_334 = var_334
                    prev_state = self.table_18[tuple_334]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_334] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_334_334 = (var_334, var_334)
                        prev_state = self.table_6[tuple_334_334]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_334_334] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_334_334[1]].append(tuple_334_334[0])
                                self.index_707[tuple_334_334[0]].append(tuple_334_334[1])
                            # Program VectorAppend Region
                            vec_325.append((var_334, var_334))
                        # Program VectorAppend Region
                        vec_413.append(var_334)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_335: int
                        scan_index_335: int = 0
                        scan_tuple_335_vec: List[int] = self.index_158[var_334]
                        while scan_index_335 < len(scan_tuple_335_vec):
                            scan_tuple_335 = scan_tuple_335_vec[scan_index_335]
                            scan_index_335 += 1
                            vec_335.append(scan_tuple_335)
                        # Program VectorLoop Region
                        vec_index335 = 0
                        while vec_index335 < len(vec_335):
                            var_336 = vec_335[vec_index335]
                            vec_index335 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_334_336 = (var_334, var_336)
                            prev_state = self.table_30[tuple_334_336]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_334_336] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_334, var_336)

                                # Program Call Region
                                ret = self.proc_165_(var_334, var_336)

        # Program VectorClear Region
        del vec_332[:]
        vec_index332 = 0
        # Program VectorUnique Region
        vec_339 = list(set(vec_339))
        vec_index339 = 0
        # Program TableJoin Region
        while vec_index339 < len(vec_339):
            var_341 = vec_339[vec_index339]
            vec_index339 += 1
            if var_341 in self.index_140:
                tuple_340_1_index: int = 0
                tuple_340_1_vec: List[int] = self.index_187[var_341]
                while tuple_340_1_index < len(tuple_340_1_vec):
                    tuple_340_1 = tuple_340_1_vec[tuple_340_1_index]
                    tuple_340_1_index += 1
                    var_342 = tuple_340_1
                    # Program TransitionState Region
                    tuple_342_341_5 = (var_342, var_341, self.var_5)
                    prev_state = self.table_9[tuple_342_341_5]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_342_341_5] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_342_341_5[0], tuple_342_341_5[1])].append(tuple_342_341_5[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_341_342 = (var_341, var_342)
                        prev_state = self.table_30[tuple_341_342]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_341_342] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_341_342[0]].append(tuple_341_342[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_341)
                        if not ret:
                            # Program TransitionState Region
                            tuple_341_342 = (var_341, var_342)
                            prev_state = self.table_30[tuple_341_342]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_341_342] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_341_342[0]].append(tuple_341_342[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_342, var_341)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_342_341 = (var_342, var_341)
                                    prev_state = self.table_54[tuple_342_341]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_342_341] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_342_341[0]].append(tuple_342_341[1])
                                            self.index_749[tuple_342_341[1]].append(tuple_342_341[0])
                                        # Program VectorAppend Region
                                        vec_417.append(var_342)
                                # Program TransitionState Region
                                tuple_342_341 = (var_342, var_341)
                                prev_state = self.table_15[tuple_342_341]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_342_341] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_342_341[0]].append(tuple_342_341[1])
                        # Program TransitionState Region
                        tuple_342_341 = (var_342, var_341)
                        prev_state = self.table_96[tuple_342_341]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_342_341] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_342_341[1]].append(tuple_342_341[0])
                            # Program VectorAppend Region
                            vec_413.append(var_341)
                        # Program TransitionState Region
                        tuple_341 = var_341
                        prev_state = self.table_40[tuple_341]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_341] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_394.append(var_341)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_5:
                            # Program TransitionState Region
                            tuple_341 = var_341
                            prev_state = self.table_18[tuple_341]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_341] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_341_341 = (var_341, var_341)
                                prev_state = self.table_6[tuple_341_341]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_341_341] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_341_341[1]].append(tuple_341_341[0])
                                        self.index_707[tuple_341_341[0]].append(tuple_341_341[1])
                                    # Program VectorAppend Region
                                    vec_325.append((var_341, var_341))
                                # Program VectorAppend Region
                                vec_413.append(var_341)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_346: int
                                scan_index_346: int = 0
                                scan_tuple_346_vec: List[int] = self.index_158[var_341]
                                while scan_index_346 < len(scan_tuple_346_vec):
                                    scan_tuple_346 = scan_tuple_346_vec[scan_index_346]
                                    scan_index_346 += 1
                                    vec_346.append(scan_tuple_346)
                                # Program VectorLoop Region
                                vec_index346 = 0
                                while vec_index346 < len(vec_346):
                                    var_347 = vec_346[vec_index346]
                                    vec_index346 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_341_347 = (var_341, var_347)
                                    prev_state = self.table_30[tuple_341_347]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_341_347] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_341, var_347)

                                        # Program Call Region
                                        ret = self.proc_165_(var_341, var_347)

                        # Program TupleCompare Region
                        if self.var_2 == self.var_5:
                            # Program TransitionState Region
                            tuple_342_341 = (var_342, var_341)
                            prev_state = self.table_48[tuple_342_341]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_342_341] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_342_341[0]].append(tuple_342_341[1])
                                # Program VectorAppend Region
                                vec_401.append(var_342)
        # Program VectorClear Region
        del vec_339[:]
        vec_index339 = 0
        # Program VectorUnique Region
        vec_350 = list(set(vec_350))
        vec_index350 = 0
        # Program TableJoin Region
        while vec_index350 < len(vec_350):
            var_352 = vec_350[vec_index350]
            vec_index350 += 1
            if var_352 in self.index_140:
                tuple_351_1_index: int = 0
                tuple_351_1_vec: List[int] = self.index_205[var_352]
                while tuple_351_1_index < len(tuple_351_1_vec):
                    tuple_351_1 = tuple_351_1_vec[tuple_351_1_index]
                    tuple_351_1_index += 1
                    var_353 = tuple_351_1
                    # Program TransitionState Region
                    tuple_353_352_3 = (var_353, var_352, self.var_3)
                    prev_state = self.table_9[tuple_353_352_3]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_353_352_3] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_353_352_3[0], tuple_353_352_3[1])].append(tuple_353_352_3[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_352_353 = (var_352, var_353)
                        prev_state = self.table_30[tuple_352_353]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_352_353] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_352_353[0]].append(tuple_352_353[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_352)
                        if not ret:
                            # Program TransitionState Region
                            tuple_352_353 = (var_352, var_353)
                            prev_state = self.table_30[tuple_352_353]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_352_353] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_352_353[0]].append(tuple_352_353[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_353, var_352)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_353_352 = (var_353, var_352)
                                    prev_state = self.table_54[tuple_353_352]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_353_352] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_353_352[0]].append(tuple_353_352[1])
                                            self.index_749[tuple_353_352[1]].append(tuple_353_352[0])
                                        # Program VectorAppend Region
                                        vec_417.append(var_353)
                                # Program TransitionState Region
                                tuple_353_352 = (var_353, var_352)
                                prev_state = self.table_15[tuple_353_352]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_353_352] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_353_352[0]].append(tuple_353_352[1])
                        # Program TransitionState Region
                        tuple_353_352 = (var_353, var_352)
                        prev_state = self.table_96[tuple_353_352]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_353_352] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_353_352[1]].append(tuple_353_352[0])
                            # Program VectorAppend Region
                            vec_413.append(var_352)
                        # Program TransitionState Region
                        tuple_352 = var_352
                        prev_state = self.table_40[tuple_352]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_352] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_394.append(var_352)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_3:
                            # Program TransitionState Region
                            tuple_352 = var_352
                            prev_state = self.table_18[tuple_352]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_352] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_352_352 = (var_352, var_352)
                                prev_state = self.table_6[tuple_352_352]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_352_352] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_352_352[1]].append(tuple_352_352[0])
                                        self.index_707[tuple_352_352[0]].append(tuple_352_352[1])
                                    # Program VectorAppend Region
                                    vec_325.append((var_352, var_352))
                                # Program VectorAppend Region
                                vec_413.append(var_352)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_357: int
                                scan_index_357: int = 0
                                scan_tuple_357_vec: List[int] = self.index_158[var_352]
                                while scan_index_357 < len(scan_tuple_357_vec):
                                    scan_tuple_357 = scan_tuple_357_vec[scan_index_357]
                                    scan_index_357 += 1
                                    vec_357.append(scan_tuple_357)
                                # Program VectorLoop Region
                                vec_index357 = 0
                                while vec_index357 < len(vec_357):
                                    var_358 = vec_357[vec_index357]
                                    vec_index357 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_352_358 = (var_352, var_358)
                                    prev_state = self.table_30[tuple_352_358]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_352_358] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_352, var_358)

                                        # Program Call Region
                                        ret = self.proc_165_(var_352, var_358)

                        # Program TupleCompare Region
                        if self.var_2 == self.var_3:
                            # Program TransitionState Region
                            tuple_353_352 = (var_353, var_352)
                            prev_state = self.table_48[tuple_353_352]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_353_352] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_353_352[0]].append(tuple_353_352[1])
                                # Program VectorAppend Region
                                vec_401.append(var_353)
        # Program VectorClear Region
        del vec_350[:]
        vec_index350 = 0
        # Program VectorUnique Region
        vec_361 = list(set(vec_361))
        vec_index361 = 0
        # Program TableJoin Region
        while vec_index361 < len(vec_361):
            var_363 = vec_361[vec_index361]
            vec_index361 += 1
            if var_363 in self.index_140:
                tuple_362_1_index: int = 0
                tuple_362_1_vec: List[int] = self.index_217[var_363]
                while tuple_362_1_index < len(tuple_362_1_vec):
                    tuple_362_1 = tuple_362_1_vec[tuple_362_1_index]
                    tuple_362_1_index += 1
                    var_364 = tuple_362_1
                    # Program TransitionState Region
                    tuple_364_363_0 = (var_364, var_363, self.var_0)
                    prev_state = self.table_9[tuple_364_363_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_364_363_0] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_364_363_0[0], tuple_364_363_0[1])].append(tuple_364_363_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_363_364 = (var_363, var_364)
                        prev_state = self.table_30[tuple_363_364]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_363_364] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_363_364[0]].append(tuple_363_364[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_363)
                        if not ret:
                            # Program TransitionState Region
                            tuple_363_364 = (var_363, var_364)
                            prev_state = self.table_30[tuple_363_364]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_363_364] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_363_364[0]].append(tuple_363_364[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_364, var_363)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_364_363 = (var_364, var_363)
                                    prev_state = self.table_54[tuple_364_363]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_364_363] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_364_363[0]].append(tuple_364_363[1])
                                            self.index_749[tuple_364_363[1]].append(tuple_364_363[0])
                                        # Program VectorAppend Region
                                        vec_417.append(var_364)
                                # Program TransitionState Region
                                tuple_364_363 = (var_364, var_363)
                                prev_state = self.table_15[tuple_364_363]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_364_363] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_364_363[0]].append(tuple_364_363[1])
                        # Program TransitionState Region
                        tuple_364_363 = (var_364, var_363)
                        prev_state = self.table_96[tuple_364_363]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_364_363] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_364_363[1]].append(tuple_364_363[0])
                            # Program VectorAppend Region
                            vec_413.append(var_363)
                        # Program TransitionState Region
                        tuple_363 = var_363
                        prev_state = self.table_40[tuple_363]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_363] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_394.append(var_363)
                        # Program TransitionState Region
                        tuple_363 = var_363
                        prev_state = self.table_18[tuple_363]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_363] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program TransitionState Region
                            tuple_363_363 = (var_363, var_363)
                            prev_state = self.table_6[tuple_363_363]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_363_363] = 1 | 4
                                if not present_bit:
                                    self.index_287[tuple_363_363[1]].append(tuple_363_363[0])
                                    self.index_707[tuple_363_363[0]].append(tuple_363_363[1])
                                # Program VectorAppend Region
                                vec_325.append((var_363, var_363))
                            # Program VectorAppend Region
                            vec_413.append(var_363)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_368: int
                            scan_index_368: int = 0
                            scan_tuple_368_vec: List[int] = self.index_158[var_363]
                            while scan_index_368 < len(scan_tuple_368_vec):
                                scan_tuple_368 = scan_tuple_368_vec[scan_index_368]
                                scan_index_368 += 1
                                vec_368.append(scan_tuple_368)
                            # Program VectorLoop Region
                            vec_index368 = 0
                            while vec_index368 < len(vec_368):
                                var_369 = vec_368[vec_index368]
                                vec_index368 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_363_369 = (var_363, var_369)
                                prev_state = self.table_30[tuple_363_369]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_30[tuple_363_369] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_161_(var_363, var_369)

                                    # Program Call Region
                                    ret = self.proc_165_(var_363, var_369)

                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_364_363 = (var_364, var_363)
                            prev_state = self.table_48[tuple_364_363]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_364_363] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_364_363[0]].append(tuple_364_363[1])
                                # Program VectorAppend Region
                                vec_401.append(var_364)
        # Program VectorClear Region
        del vec_361[:]
        vec_index361 = 0
        # Program VectorUnique Region
        vec_372 = list(set(vec_372))
        vec_index372 = 0
        # Program TableJoin Region
        while vec_index372 < len(vec_372):
            var_374 = vec_372[vec_index372]
            vec_index372 += 1
            if var_374 in self.index_140:
                tuple_373_1_index: int = 0
                tuple_373_1_vec: List[int] = self.index_229[var_374]
                while tuple_373_1_index < len(tuple_373_1_vec):
                    tuple_373_1 = tuple_373_1_vec[tuple_373_1_index]
                    tuple_373_1_index += 1
                    var_375 = tuple_373_1
                    # Program TransitionState Region
                    tuple_375_374_0 = (var_375, var_374, self.var_0)
                    prev_state = self.table_9[tuple_375_374_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_375_374_0] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_375_374_0[0], tuple_375_374_0[1])].append(tuple_375_374_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_374_375 = (var_374, var_375)
                        prev_state = self.table_30[tuple_374_375]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_374_375] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_374_375[0]].append(tuple_374_375[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_374)
                        if not ret:
                            # Program TransitionState Region
                            tuple_374_375 = (var_374, var_375)
                            prev_state = self.table_30[tuple_374_375]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_374_375] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_374_375[0]].append(tuple_374_375[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_375, var_374)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_375_374 = (var_375, var_374)
                                    prev_state = self.table_54[tuple_375_374]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_375_374] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_375_374[0]].append(tuple_375_374[1])
                                            self.index_749[tuple_375_374[1]].append(tuple_375_374[0])
                                        # Program VectorAppend Region
                                        vec_417.append(var_375)
                                # Program TransitionState Region
                                tuple_375_374 = (var_375, var_374)
                                prev_state = self.table_15[tuple_375_374]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_375_374] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_375_374[0]].append(tuple_375_374[1])
                        # Program TransitionState Region
                        tuple_375_374 = (var_375, var_374)
                        prev_state = self.table_96[tuple_375_374]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_375_374] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_375_374[1]].append(tuple_375_374[0])
                            # Program VectorAppend Region
                            vec_413.append(var_374)
                        # Program TransitionState Region
                        tuple_374 = var_374
                        prev_state = self.table_40[tuple_374]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_374] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_394.append(var_374)
                        # Program TransitionState Region
                        tuple_374 = var_374
                        prev_state = self.table_18[tuple_374]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_374] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program TransitionState Region
                            tuple_374_374 = (var_374, var_374)
                            prev_state = self.table_6[tuple_374_374]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_374_374] = 1 | 4
                                if not present_bit:
                                    self.index_287[tuple_374_374[1]].append(tuple_374_374[0])
                                    self.index_707[tuple_374_374[0]].append(tuple_374_374[1])
                                # Program VectorAppend Region
                                vec_325.append((var_374, var_374))
                            # Program VectorAppend Region
                            vec_413.append(var_374)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_379: int
                            scan_index_379: int = 0
                            scan_tuple_379_vec: List[int] = self.index_158[var_374]
                            while scan_index_379 < len(scan_tuple_379_vec):
                                scan_tuple_379 = scan_tuple_379_vec[scan_index_379]
                                scan_index_379 += 1
                                vec_379.append(scan_tuple_379)
                            # Program VectorLoop Region
                            vec_index379 = 0
                            while vec_index379 < len(vec_379):
                                var_380 = vec_379[vec_index379]
                                vec_index379 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_374_380 = (var_374, var_380)
                                prev_state = self.table_30[tuple_374_380]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_30[tuple_374_380] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_161_(var_374, var_380)

                                    # Program Call Region
                                    ret = self.proc_165_(var_374, var_380)

                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_375_374 = (var_375, var_374)
                            prev_state = self.table_48[tuple_375_374]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_375_374] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_375_374[0]].append(tuple_375_374[1])
                                # Program VectorAppend Region
                                vec_401.append(var_375)
        # Program VectorClear Region
        del vec_372[:]
        vec_index372 = 0
        # Program VectorUnique Region
        vec_383 = list(set(vec_383))
        vec_index383 = 0
        # Program TableJoin Region
        while vec_index383 < len(vec_383):
            var_385 = vec_383[vec_index383]
            vec_index383 += 1
            if var_385 in self.index_140:
                tuple_384_1_index: int = 0
                tuple_384_1_vec: List[int] = self.index_241[var_385]
                while tuple_384_1_index < len(tuple_384_1_vec):
                    tuple_384_1 = tuple_384_1_vec[tuple_384_1_index]
                    tuple_384_1_index += 1
                    var_386 = tuple_384_1
                    # Program TransitionState Region
                    tuple_386_385_2 = (var_386, var_385, self.var_2)
                    prev_state = self.table_9[tuple_386_385_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_386_385_2] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_386_385_2[0], tuple_386_385_2[1])].append(tuple_386_385_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_385_386 = (var_385, var_386)
                        prev_state = self.table_30[tuple_385_386]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_385_386] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_385_386[0]].append(tuple_385_386[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_385)
                        if not ret:
                            # Program TransitionState Region
                            tuple_385_386 = (var_385, var_386)
                            prev_state = self.table_30[tuple_385_386]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_385_386] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_385_386[0]].append(tuple_385_386[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_386, var_385)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_386_385 = (var_386, var_385)
                                    prev_state = self.table_54[tuple_386_385]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_386_385] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_386_385[0]].append(tuple_386_385[1])
                                            self.index_749[tuple_386_385[1]].append(tuple_386_385[0])
                                        # Program VectorAppend Region
                                        vec_417.append(var_386)
                                # Program TransitionState Region
                                tuple_386_385 = (var_386, var_385)
                                prev_state = self.table_15[tuple_386_385]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_386_385] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_386_385[0]].append(tuple_386_385[1])
                        # Program TransitionState Region
                        tuple_386_385 = (var_386, var_385)
                        prev_state = self.table_96[tuple_386_385]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_386_385] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_386_385[1]].append(tuple_386_385[0])
                            # Program VectorAppend Region
                            vec_413.append(var_385)
                        # Program TransitionState Region
                        tuple_385 = var_385
                        prev_state = self.table_40[tuple_385]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_385] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_394.append(var_385)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_385 = var_385
                            prev_state = self.table_18[tuple_385]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_385] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_385_385 = (var_385, var_385)
                                prev_state = self.table_6[tuple_385_385]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_385_385] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_385_385[1]].append(tuple_385_385[0])
                                        self.index_707[tuple_385_385[0]].append(tuple_385_385[1])
                                    # Program VectorAppend Region
                                    vec_325.append((var_385, var_385))
                                # Program VectorAppend Region
                                vec_413.append(var_385)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_390: int
                                scan_index_390: int = 0
                                scan_tuple_390_vec: List[int] = self.index_158[var_385]
                                while scan_index_390 < len(scan_tuple_390_vec):
                                    scan_tuple_390 = scan_tuple_390_vec[scan_index_390]
                                    scan_index_390 += 1
                                    vec_390.append(scan_tuple_390)
                                # Program VectorLoop Region
                                vec_index390 = 0
                                while vec_index390 < len(vec_390):
                                    var_391 = vec_390[vec_index390]
                                    vec_index390 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_385_391 = (var_385, var_391)
                                    prev_state = self.table_30[tuple_385_391]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_385_391] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_385, var_391)

                                        # Program Call Region
                                        ret = self.proc_165_(var_385, var_391)

                        # Program TransitionState Region
                        tuple_386_385 = (var_386, var_385)
                        prev_state = self.table_48[tuple_386_385]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_48[tuple_386_385] = 1 | 4
                            if not present_bit:
                                self.index_262[tuple_386_385[0]].append(tuple_386_385[1])
                            # Program VectorAppend Region
                            vec_401.append(var_386)
        # Program VectorClear Region
        del vec_383[:]
        vec_index383 = 0
        # Program VectorUnique Region
        vec_394 = list(set(vec_394))
        vec_index394 = 0
        # Program TableJoin Region
        while vec_index394 < len(vec_394):
            var_396 = vec_394[vec_index394]
            vec_index394 += 1
            if var_396 in self.index_253:
                if var_396 in self.index_254:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_396 = var_396
                    prev_state = self.table_18[tuple_396]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_396] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_396_396 = (var_396, var_396)
                        prev_state = self.table_6[tuple_396_396]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_396_396] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_396_396[1]].append(tuple_396_396[0])
                                self.index_707[tuple_396_396[0]].append(tuple_396_396[1])
                            # Program VectorAppend Region
                            vec_325.append((var_396, var_396))
                        # Program VectorAppend Region
                        vec_413.append(var_396)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_397: int
                        scan_index_397: int = 0
                        scan_tuple_397_vec: List[int] = self.index_158[var_396]
                        while scan_index_397 < len(scan_tuple_397_vec):
                            scan_tuple_397 = scan_tuple_397_vec[scan_index_397]
                            scan_index_397 += 1
                            vec_397.append(scan_tuple_397)
                        # Program VectorLoop Region
                        vec_index397 = 0
                        while vec_index397 < len(vec_397):
                            var_398 = vec_397[vec_index397]
                            vec_index397 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_396_398 = (var_396, var_398)
                            prev_state = self.table_30[tuple_396_398]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_396_398] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_396, var_398)

                                # Program Call Region
                                ret = self.proc_165_(var_396, var_398)

        # Program VectorClear Region
        del vec_394[:]
        vec_index394 = 0
        # Program VectorUnique Region
        vec_401 = list(set(vec_401))
        vec_index401 = 0
        # Program TableJoin Region
        while vec_index401 < len(vec_401):
            var_403 = vec_401[vec_index401]
            vec_index401 += 1
            if var_403 in self.index_134:
                tuple_402_1_index: int = 0
                tuple_402_1_vec: List[int] = self.index_262[var_403]
                while tuple_402_1_index < len(tuple_402_1_vec):
                    tuple_402_1 = tuple_402_1_vec[tuple_402_1_index]
                    tuple_402_1_index += 1
                    var_404 = tuple_402_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_403_404 = (var_403, var_404)
                    prev_state = self.table_51[tuple_403_404]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_403_404] = 1 | 4
                        if not present_bit:
                            self.index_267[tuple_403_404[1]].append(tuple_403_404[0])
                        # Program VectorAppend Region
                        vec_405.append(var_404)
        # Program VectorClear Region
        del vec_401[:]
        vec_index401 = 0
        # Program VectorUnique Region
        vec_405 = list(set(vec_405))
        vec_index405 = 0
        # Program TableJoin Region
        while vec_index405 < len(vec_405):
            var_407 = vec_405[vec_index405]
            vec_index405 += 1
            if var_407 in self.index_253:
                tuple_406_1_index: int = 0
                tuple_406_1_vec: List[int] = self.index_267[var_407]
                while tuple_406_1_index < len(tuple_406_1_vec):
                    tuple_406_1 = tuple_406_1_vec[tuple_406_1_index]
                    tuple_406_1_index += 1
                    var_408 = tuple_406_1
                    # Program TransitionState Region
                    tuple_408 = var_408
                    prev_state = self.table_18[tuple_408]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_408] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_408_408 = (var_408, var_408)
                        prev_state = self.table_6[tuple_408_408]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_408_408] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_408_408[1]].append(tuple_408_408[0])
                                self.index_707[tuple_408_408[0]].append(tuple_408_408[1])
                            # Program VectorAppend Region
                            vec_325.append((var_408, var_408))
                        # Program VectorAppend Region
                        vec_413.append(var_408)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_409: int
                        scan_index_409: int = 0
                        scan_tuple_409_vec: List[int] = self.index_158[var_408]
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
                            tuple_408_410 = (var_408, var_410)
                            prev_state = self.table_30[tuple_408_410]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_408_410] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_408, var_410)

                                # Program Call Region
                                ret = self.proc_165_(var_408, var_410)

        # Program VectorClear Region
        del vec_405[:]
        vec_index405 = 0
        # Program VectorUnique Region
        vec_413 = list(set(vec_413))
        vec_index413 = 0
        # Program TableJoin Region
        while vec_index413 < len(vec_413):
            var_415 = vec_413[vec_index413]
            vec_index413 += 1
            tuple_414_0_index: int = 0
            tuple_414_0_vec: List[int] = self.index_276[var_415]
            while tuple_414_0_index < len(tuple_414_0_vec):
                tuple_414_0 = tuple_414_0_vec[tuple_414_0_index]
                tuple_414_0_index += 1
                var_416 = tuple_414_0
                if var_415 in self.index_277:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_416_415 = (var_416, var_415)
                    prev_state = self.table_99[tuple_416_415]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_99[tuple_416_415] = 1 | 4
                        if not present_bit:
                            self.index_282[tuple_416_415[1]].append(tuple_416_415[0])
                        # Program VectorAppend Region
                        vec_425.append(var_415)
                    # Program TransitionState Region
                    tuple_416_415 = (var_416, var_415)
                    prev_state = self.table_20[tuple_416_415]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_416_415] = 1 | 4
                        if not present_bit:
                            self.index_715[tuple_416_415[0]].append(tuple_416_415[1])
        # Program VectorClear Region
        del vec_413[:]
        vec_index413 = 0
        # Program VectorUnique Region
        vec_417 = list(set(vec_417))
        vec_index417 = 0
        # Program TableJoin Region
        while vec_index417 < len(vec_417):
            var_419 = vec_417[vec_index417]
            vec_index417 += 1
            tuple_418_0_index: int = 0
            tuple_418_0_vec: List[int] = self.index_287[var_419]
            while tuple_418_0_index < len(tuple_418_0_vec):
                tuple_418_0 = tuple_418_0_vec[tuple_418_0_index]
                tuple_418_0_index += 1
                var_420 = tuple_418_0
                tuple_418_1_index: int = 0
                tuple_418_1_vec: List[int] = self.index_288[var_419]
                while tuple_418_1_index < len(tuple_418_1_vec):
                    tuple_418_1 = tuple_418_1_vec[tuple_418_1_index]
                    tuple_418_1_index += 1
                    var_421 = tuple_418_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_291_(var_420, var_419)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_147_(var_419, var_421)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_296_(var_420, var_421)
                            if not ret:
                                # Program TransitionState Region
                                tuple_420_421 = (var_420, var_421)
                                prev_state = self.table_6[tuple_420_421]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_420_421] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_420_421[1]].append(tuple_420_421[0])
                                        self.index_707[tuple_420_421[0]].append(tuple_420_421[1])
                                    # Program VectorAppend Region
                                    vec_325.append((var_420, var_421))
        # Program VectorClear Region
        del vec_417[:]
        vec_index417 = 0
        # Program VectorUnique Region
        vec_425 = list(set(vec_425))
        vec_index425 = 0
        # Program TableJoin Region
        while vec_index425 < len(vec_425):
            var_427 = vec_425[vec_index425]
            vec_index425 += 1
            tuple_426_0_index: int = 0
            tuple_426_0_vec: List[int] = self.index_282[var_427]
            while tuple_426_0_index < len(tuple_426_0_vec):
                tuple_426_0 = tuple_426_0_vec[tuple_426_0_index]
                tuple_426_0_index += 1
                var_428 = tuple_426_0
                if var_427 in self.index_253:
                    # Program TransitionState Region
                    tuple_428 = var_428
                    prev_state = self.table_13[tuple_428]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_428] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_425[:]
        vec_index425 = 0
        # Induction Fixpoint Loop Region
        while len(vec_325):
            # Program Call Region
            param_327_0 = [vec_325]
            ret = self.proc_151_(param_327_0)
            vec_325 = param_327_0[0]

        vec_index325 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_325[:]
        vec_index325 = 0
        # Program Return Region
        return False
        return False

    def entrypoint_1(self, vec_430: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index430: int = 0
        vec_432: List[int] = list()
        vec_index432: int = 0
        vec_435: List[Tuple[int, int]] = list()
        vec_index435: int = 0
        vec_438: List[int] = list()
        vec_index438: int = 0
        vec_442: List[int] = list()
        vec_index442: int = 0
        vec_446: List[int] = list()
        vec_index446: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index430 = 0
        while vec_index430 < len(vec_430):
            var_431 = vec_430[vec_index430]
            vec_index430 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_431 = var_431
            prev_state = self.table_42[tuple_431]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_42[tuple_431] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_432.append(var_431)
        # Program VectorUnique Region
        vec_432 = list(set(vec_432))
        vec_index432 = 0
        # Program TableJoin Region
        while vec_index432 < len(vec_432):
            var_434 = vec_432[vec_index432]
            vec_index432 += 1
            if var_434 in self.index_172:
                if var_434 in self.index_140:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_434 = var_434
                    prev_state = self.table_18[tuple_434]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_434] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_434_434 = (var_434, var_434)
                        prev_state = self.table_6[tuple_434_434]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_434_434] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_434_434[1]].append(tuple_434_434[0])
                                self.index_707[tuple_434_434[0]].append(tuple_434_434[1])
                            # Program VectorAppend Region
                            vec_435.append((var_434, var_434))
                        # Program VectorAppend Region
                        vec_442.append(var_434)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_438: int
                        scan_index_438: int = 0
                        scan_tuple_438_vec: List[int] = self.index_158[var_434]
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
                            tuple_434_439 = (var_434, var_439)
                            prev_state = self.table_30[tuple_434_439]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_434_439] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_434, var_439)

                                # Program Call Region
                                ret = self.proc_165_(var_434, var_439)

        # Program VectorClear Region
        del vec_432[:]
        vec_index432 = 0
        # Program VectorUnique Region
        vec_442 = list(set(vec_442))
        vec_index442 = 0
        # Program TableJoin Region
        while vec_index442 < len(vec_442):
            var_444 = vec_442[vec_index442]
            vec_index442 += 1
            tuple_443_0_index: int = 0
            tuple_443_0_vec: List[int] = self.index_276[var_444]
            while tuple_443_0_index < len(tuple_443_0_vec):
                tuple_443_0 = tuple_443_0_vec[tuple_443_0_index]
                tuple_443_0_index += 1
                var_445 = tuple_443_0
                if var_444 in self.index_277:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_445_444 = (var_445, var_444)
                    prev_state = self.table_99[tuple_445_444]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_99[tuple_445_444] = 1 | 4
                        if not present_bit:
                            self.index_282[tuple_445_444[1]].append(tuple_445_444[0])
                        # Program VectorAppend Region
                        vec_446.append(var_444)
                    # Program TransitionState Region
                    tuple_445_444 = (var_445, var_444)
                    prev_state = self.table_20[tuple_445_444]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_445_444] = 1 | 4
                        if not present_bit:
                            self.index_715[tuple_445_444[0]].append(tuple_445_444[1])
        # Program VectorClear Region
        del vec_442[:]
        vec_index442 = 0
        # Program VectorUnique Region
        vec_446 = list(set(vec_446))
        vec_index446 = 0
        # Program TableJoin Region
        while vec_index446 < len(vec_446):
            var_448 = vec_446[vec_index446]
            vec_index446 += 1
            tuple_447_0_index: int = 0
            tuple_447_0_vec: List[int] = self.index_282[var_448]
            while tuple_447_0_index < len(tuple_447_0_vec):
                tuple_447_0 = tuple_447_0_vec[tuple_447_0_index]
                tuple_447_0_index += 1
                var_449 = tuple_447_0
                if var_448 in self.index_253:
                    # Program TransitionState Region
                    tuple_449 = var_449
                    prev_state = self.table_13[tuple_449]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_449] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_446[:]
        vec_index446 = 0
        # Induction Fixpoint Loop Region
        while len(vec_435):
            # Program Call Region
            param_437_0 = [vec_435]
            ret = self.proc_151_(param_437_0)
            vec_435 = param_437_0[0]

        vec_index435 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_435[:]
        vec_index435 = 0
        # Program Return Region
        return False
        return False

    def raw_transfer_3(self, vec_451: List[Tuple[int, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index451: int = 0
        vec_455: List[Tuple[int, int]] = list()
        vec_index455: int = 0
        vec_461: List[int] = list()
        vec_index461: int = 0
        vec_468: List[int] = list()
        vec_index468: int = 0
        vec_476: List[Tuple[int, int]] = list()
        vec_index476: int = 0
        vec_479: List[int] = list()
        vec_index479: int = 0
        vec_483: List[int] = list()
        vec_index483: int = 0
        vec_490: List[int] = list()
        vec_index490: int = 0
        vec_494: List[int] = list()
        vec_index494: int = 0
        vec_501: List[int] = list()
        vec_index501: int = 0
        vec_505: List[int] = list()
        vec_index505: int = 0
        vec_512: List[int] = list()
        vec_index512: int = 0
        vec_516: List[int] = list()
        vec_index516: int = 0
        vec_519: List[int] = list()
        vec_index519: int = 0
        vec_523: List[int] = list()
        vec_index523: int = 0
        vec_527: List[int] = list()
        vec_index527: int = 0
        vec_531: List[int] = list()
        vec_index531: int = 0
        vec_535: List[int] = list()
        vec_index535: int = 0
        vec_539: List[int] = list()
        vec_index539: int = 0
        vec_543: List[int] = list()
        vec_index543: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index451 = 0
        while vec_index451 < len(vec_451):
            var_452, var_453, var_454 = vec_451[vec_index451]
            vec_index451 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if var_454 != self.var_0:
                # Program TupleCompare Region
                if var_454 != self.var_3:
                    # Program TransitionState Region
                    var_454 = self._resolve_edgetype(var_454)
                    tuple_454_452_453 = (var_454, var_452, var_453)
                    prev_state = self.table_57[tuple_454_452_453]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_57[tuple_454_452_453] = 1 | 4
                        if not present_bit:
                            self.index_139[tuple_454_452_453[2]].append((tuple_454_452_453[0], tuple_454_452_453[1]))
                        # Program VectorAppend Region
                        vec_468.append(var_453)
            # Program TupleCompare Region
            if self.var_0 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_64[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_64[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_464[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_3 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_67[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_67[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_465[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_0 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_64[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_64[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_464[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_3 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_67[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_67[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_465[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_0 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_64[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_64[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_464[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_3 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_67[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_67[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_465[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_0 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_64[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_64[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_464[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_3 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_67[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_67[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_465[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_0 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_64[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_64[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_464[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_3 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_67[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_67[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_465[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_0 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_64[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_64[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_464[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_3 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_67[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_67[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_465[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_0 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_64[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_64[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_464[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
            # Program TupleCompare Region
            if self.var_3 == var_454:
                # Program TransitionState Region
                tuple_452_453 = (var_452, var_453)
                prev_state = self.table_67[tuple_452_453]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_67[tuple_452_453] = 1 | 4
                    if not present_bit:
                        self.index_465[tuple_452_453[0]].append(tuple_452_453[1])
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_461.append(var_452)
                    # Program VectorAppend Region
                    vec_455.append((var_452, var_453))
        # Program VectorUnique Region
        vec_455 = list(set(vec_455))
        vec_index455 = 0
        # Program TableJoin Region
        while vec_index455 < len(vec_455):
            var_457, var_458 = vec_455[vec_index455]
            vec_index455 += 1
            if (var_457, var_458) in self.index_459:
                if (var_457, var_458) in self.index_460:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_457_458 = (var_457, var_458)
                    prev_state = self.table_93[tuple_457_458]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_93[tuple_457_458] = 1 | 4
                        if not present_bit:
                            self.index_187[tuple_457_458[1]].append(tuple_457_458[0])
                        # Program VectorAppend Region
                        vec_483.append(var_458)
        # Program VectorClear Region
        del vec_455[:]
        vec_index455 = 0
        # Program VectorUnique Region
        vec_461 = list(set(vec_461))
        vec_index461 = 0
        # Program TableJoin Region
        while vec_index461 < len(vec_461):
            var_463 = vec_461[vec_index461]
            vec_index461 += 1
            tuple_462_0_index: int = 0
            tuple_462_0_vec: List[int] = self.index_464[var_463]
            while tuple_462_0_index < len(tuple_462_0_vec):
                tuple_462_0 = tuple_462_0_vec[tuple_462_0_index]
                tuple_462_0_index += 1
                var_466 = tuple_462_0
                tuple_462_1_index: int = 0
                tuple_462_1_vec: List[int] = self.index_465[var_463]
                while tuple_462_1_index < len(tuple_462_1_vec):
                    tuple_462_1 = tuple_462_1_vec[tuple_462_1_index]
                    tuple_462_1_index += 1
                    var_467 = tuple_462_1
                    # Program TupleCompare Region
                    if var_466 != var_467:
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_466_463 = (var_466, var_463)
                        prev_state = self.table_61[tuple_466_463]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_61[tuple_466_463] = 1 | 4
                            if not present_bit:
                                self.index_217[tuple_466_463[0]].append(tuple_466_463[1])
                            # Program VectorAppend Region
                            vec_505.append(var_466)
                        # Program TransitionState Region
                        tuple_467_463 = (var_467, var_463)
                        prev_state = self.table_70[tuple_467_463]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_70[tuple_467_463] = 1 | 4
                            if not present_bit:
                                self.index_205[tuple_467_463[0]].append(tuple_467_463[1])
                            # Program VectorAppend Region
                            vec_494.append(var_467)
        # Program VectorClear Region
        del vec_461[:]
        vec_index461 = 0
        # Program VectorUnique Region
        vec_468 = list(set(vec_468))
        vec_index468 = 0
        # Program TableJoin Region
        while vec_index468 < len(vec_468):
            var_470 = vec_468[vec_index468]
            vec_index468 += 1
            tuple_469_0_index: int = 0
            tuple_469_0_vec: List[Tuple[int, int]] = self.index_139[var_470]
            while tuple_469_0_index < len(tuple_469_0_vec):
                tuple_469_0 = tuple_469_0_vec[tuple_469_0_index]
                tuple_469_0_index += 1
                var_471 = tuple_469_0[0]
                var_472 = tuple_469_0[1]
                if var_470 in self.index_140:
                    # Program TransitionState Region
                    var_471 = self._resolve_edgetype(var_471)
                    tuple_472_470_471 = (var_472, var_470, var_471)
                    prev_state = self.table_9[tuple_472_470_471]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_472_470_471] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_472_470_471[0], tuple_472_470_471[1])].append(tuple_472_470_471[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_470_472 = (var_470, var_472)
                        prev_state = self.table_30[tuple_470_472]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_470_472] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_470_472[0]].append(tuple_470_472[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_470)
                        if not ret:
                            # Program TransitionState Region
                            tuple_470_472 = (var_470, var_472)
                            prev_state = self.table_30[tuple_470_472]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_470_472] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_470_472[0]].append(tuple_470_472[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_472, var_470)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_472_470 = (var_472, var_470)
                                    prev_state = self.table_54[tuple_472_470]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_472_470] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_472_470[0]].append(tuple_472_470[1])
                                            self.index_749[tuple_472_470[1]].append(tuple_472_470[0])
                                        # Program VectorAppend Region
                                        vec_543.append(var_472)
                                # Program TransitionState Region
                                tuple_472_470 = (var_472, var_470)
                                prev_state = self.table_15[tuple_472_470]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_472_470] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_472_470[0]].append(tuple_472_470[1])
                        # Program TransitionState Region
                        tuple_472_470 = (var_472, var_470)
                        prev_state = self.table_96[tuple_472_470]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_472_470] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_472_470[1]].append(tuple_472_470[0])
                            # Program VectorAppend Region
                            vec_535.append(var_470)
                        # Program TransitionState Region
                        tuple_470 = var_470
                        prev_state = self.table_40[tuple_470]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_470] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_516.append(var_470)
                        # Program TupleCompare Region
                        if self.var_0 == var_471:
                            # Program TransitionState Region
                            tuple_470 = var_470
                            prev_state = self.table_18[tuple_470]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_470] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_470_470 = (var_470, var_470)
                                prev_state = self.table_6[tuple_470_470]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_470_470] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_470_470[1]].append(tuple_470_470[0])
                                        self.index_707[tuple_470_470[0]].append(tuple_470_470[1])
                                    # Program VectorAppend Region
                                    vec_476.append((var_470, var_470))
                                # Program VectorAppend Region
                                vec_535.append(var_470)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_479: int
                                scan_index_479: int = 0
                                scan_tuple_479_vec: List[int] = self.index_158[var_470]
                                while scan_index_479 < len(scan_tuple_479_vec):
                                    scan_tuple_479 = scan_tuple_479_vec[scan_index_479]
                                    scan_index_479 += 1
                                    vec_479.append(scan_tuple_479)
                                # Program VectorLoop Region
                                vec_index479 = 0
                                while vec_index479 < len(vec_479):
                                    var_480 = vec_479[vec_index479]
                                    vec_index479 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_470_480 = (var_470, var_480)
                                    prev_state = self.table_30[tuple_470_480]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_470_480] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_470, var_480)

                                        # Program Call Region
                                        ret = self.proc_165_(var_470, var_480)

                        # Program TupleCompare Region
                        if self.var_2 == var_471:
                            # Program TransitionState Region
                            tuple_472_470 = (var_472, var_470)
                            prev_state = self.table_48[tuple_472_470]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_472_470] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_472_470[0]].append(tuple_472_470[1])
                                # Program VectorAppend Region
                                vec_523.append(var_472)
        # Program VectorClear Region
        del vec_468[:]
        vec_index468 = 0
        # Program VectorUnique Region
        vec_483 = list(set(vec_483))
        vec_index483 = 0
        # Program TableJoin Region
        while vec_index483 < len(vec_483):
            var_485 = vec_483[vec_index483]
            vec_index483 += 1
            if var_485 in self.index_140:
                tuple_484_1_index: int = 0
                tuple_484_1_vec: List[int] = self.index_187[var_485]
                while tuple_484_1_index < len(tuple_484_1_vec):
                    tuple_484_1 = tuple_484_1_vec[tuple_484_1_index]
                    tuple_484_1_index += 1
                    var_486 = tuple_484_1
                    # Program TransitionState Region
                    tuple_486_485_5 = (var_486, var_485, self.var_5)
                    prev_state = self.table_9[tuple_486_485_5]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_486_485_5] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_486_485_5[0], tuple_486_485_5[1])].append(tuple_486_485_5[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_485_486 = (var_485, var_486)
                        prev_state = self.table_30[tuple_485_486]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_485_486] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_485_486[0]].append(tuple_485_486[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_485)
                        if not ret:
                            # Program TransitionState Region
                            tuple_485_486 = (var_485, var_486)
                            prev_state = self.table_30[tuple_485_486]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_485_486] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_485_486[0]].append(tuple_485_486[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_486, var_485)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_486_485 = (var_486, var_485)
                                    prev_state = self.table_54[tuple_486_485]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_486_485] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_486_485[0]].append(tuple_486_485[1])
                                            self.index_749[tuple_486_485[1]].append(tuple_486_485[0])
                                        # Program VectorAppend Region
                                        vec_543.append(var_486)
                                # Program TransitionState Region
                                tuple_486_485 = (var_486, var_485)
                                prev_state = self.table_15[tuple_486_485]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_486_485] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_486_485[0]].append(tuple_486_485[1])
                        # Program TransitionState Region
                        tuple_486_485 = (var_486, var_485)
                        prev_state = self.table_96[tuple_486_485]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_486_485] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_486_485[1]].append(tuple_486_485[0])
                            # Program VectorAppend Region
                            vec_535.append(var_485)
                        # Program TransitionState Region
                        tuple_485 = var_485
                        prev_state = self.table_40[tuple_485]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_485] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_516.append(var_485)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_5:
                            # Program TransitionState Region
                            tuple_485 = var_485
                            prev_state = self.table_18[tuple_485]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_485] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_485_485 = (var_485, var_485)
                                prev_state = self.table_6[tuple_485_485]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_485_485] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_485_485[1]].append(tuple_485_485[0])
                                        self.index_707[tuple_485_485[0]].append(tuple_485_485[1])
                                    # Program VectorAppend Region
                                    vec_476.append((var_485, var_485))
                                # Program VectorAppend Region
                                vec_535.append(var_485)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_490: int
                                scan_index_490: int = 0
                                scan_tuple_490_vec: List[int] = self.index_158[var_485]
                                while scan_index_490 < len(scan_tuple_490_vec):
                                    scan_tuple_490 = scan_tuple_490_vec[scan_index_490]
                                    scan_index_490 += 1
                                    vec_490.append(scan_tuple_490)
                                # Program VectorLoop Region
                                vec_index490 = 0
                                while vec_index490 < len(vec_490):
                                    var_491 = vec_490[vec_index490]
                                    vec_index490 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_485_491 = (var_485, var_491)
                                    prev_state = self.table_30[tuple_485_491]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_485_491] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_485, var_491)

                                        # Program Call Region
                                        ret = self.proc_165_(var_485, var_491)

                        # Program TupleCompare Region
                        if self.var_2 == self.var_5:
                            # Program TransitionState Region
                            tuple_486_485 = (var_486, var_485)
                            prev_state = self.table_48[tuple_486_485]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_486_485] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_486_485[0]].append(tuple_486_485[1])
                                # Program VectorAppend Region
                                vec_523.append(var_486)
        # Program VectorClear Region
        del vec_483[:]
        vec_index483 = 0
        # Program VectorUnique Region
        vec_494 = list(set(vec_494))
        vec_index494 = 0
        # Program TableJoin Region
        while vec_index494 < len(vec_494):
            var_496 = vec_494[vec_index494]
            vec_index494 += 1
            if var_496 in self.index_140:
                tuple_495_1_index: int = 0
                tuple_495_1_vec: List[int] = self.index_205[var_496]
                while tuple_495_1_index < len(tuple_495_1_vec):
                    tuple_495_1 = tuple_495_1_vec[tuple_495_1_index]
                    tuple_495_1_index += 1
                    var_497 = tuple_495_1
                    # Program TransitionState Region
                    tuple_497_496_3 = (var_497, var_496, self.var_3)
                    prev_state = self.table_9[tuple_497_496_3]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_497_496_3] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_497_496_3[0], tuple_497_496_3[1])].append(tuple_497_496_3[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_496_497 = (var_496, var_497)
                        prev_state = self.table_30[tuple_496_497]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_496_497] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_496_497[0]].append(tuple_496_497[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_496)
                        if not ret:
                            # Program TransitionState Region
                            tuple_496_497 = (var_496, var_497)
                            prev_state = self.table_30[tuple_496_497]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_496_497] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_496_497[0]].append(tuple_496_497[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_497, var_496)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_497_496 = (var_497, var_496)
                                    prev_state = self.table_54[tuple_497_496]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_497_496] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_497_496[0]].append(tuple_497_496[1])
                                            self.index_749[tuple_497_496[1]].append(tuple_497_496[0])
                                        # Program VectorAppend Region
                                        vec_543.append(var_497)
                                # Program TransitionState Region
                                tuple_497_496 = (var_497, var_496)
                                prev_state = self.table_15[tuple_497_496]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_497_496] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_497_496[0]].append(tuple_497_496[1])
                        # Program TransitionState Region
                        tuple_497_496 = (var_497, var_496)
                        prev_state = self.table_96[tuple_497_496]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_497_496] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_497_496[1]].append(tuple_497_496[0])
                            # Program VectorAppend Region
                            vec_535.append(var_496)
                        # Program TransitionState Region
                        tuple_496 = var_496
                        prev_state = self.table_40[tuple_496]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_496] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_516.append(var_496)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_3:
                            # Program TransitionState Region
                            tuple_496 = var_496
                            prev_state = self.table_18[tuple_496]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_496] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_496_496 = (var_496, var_496)
                                prev_state = self.table_6[tuple_496_496]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_496_496] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_496_496[1]].append(tuple_496_496[0])
                                        self.index_707[tuple_496_496[0]].append(tuple_496_496[1])
                                    # Program VectorAppend Region
                                    vec_476.append((var_496, var_496))
                                # Program VectorAppend Region
                                vec_535.append(var_496)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_501: int
                                scan_index_501: int = 0
                                scan_tuple_501_vec: List[int] = self.index_158[var_496]
                                while scan_index_501 < len(scan_tuple_501_vec):
                                    scan_tuple_501 = scan_tuple_501_vec[scan_index_501]
                                    scan_index_501 += 1
                                    vec_501.append(scan_tuple_501)
                                # Program VectorLoop Region
                                vec_index501 = 0
                                while vec_index501 < len(vec_501):
                                    var_502 = vec_501[vec_index501]
                                    vec_index501 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_496_502 = (var_496, var_502)
                                    prev_state = self.table_30[tuple_496_502]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_496_502] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_496, var_502)

                                        # Program Call Region
                                        ret = self.proc_165_(var_496, var_502)

                        # Program TupleCompare Region
                        if self.var_2 == self.var_3:
                            # Program TransitionState Region
                            tuple_497_496 = (var_497, var_496)
                            prev_state = self.table_48[tuple_497_496]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_497_496] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_497_496[0]].append(tuple_497_496[1])
                                # Program VectorAppend Region
                                vec_523.append(var_497)
        # Program VectorClear Region
        del vec_494[:]
        vec_index494 = 0
        # Program VectorUnique Region
        vec_505 = list(set(vec_505))
        vec_index505 = 0
        # Program TableJoin Region
        while vec_index505 < len(vec_505):
            var_507 = vec_505[vec_index505]
            vec_index505 += 1
            if var_507 in self.index_140:
                tuple_506_1_index: int = 0
                tuple_506_1_vec: List[int] = self.index_217[var_507]
                while tuple_506_1_index < len(tuple_506_1_vec):
                    tuple_506_1 = tuple_506_1_vec[tuple_506_1_index]
                    tuple_506_1_index += 1
                    var_508 = tuple_506_1
                    # Program TransitionState Region
                    tuple_508_507_0 = (var_508, var_507, self.var_0)
                    prev_state = self.table_9[tuple_508_507_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_508_507_0] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_508_507_0[0], tuple_508_507_0[1])].append(tuple_508_507_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_507_508 = (var_507, var_508)
                        prev_state = self.table_30[tuple_507_508]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_507_508] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_507_508[0]].append(tuple_507_508[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_507)
                        if not ret:
                            # Program TransitionState Region
                            tuple_507_508 = (var_507, var_508)
                            prev_state = self.table_30[tuple_507_508]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_507_508] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_507_508[0]].append(tuple_507_508[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_508, var_507)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_508_507 = (var_508, var_507)
                                    prev_state = self.table_54[tuple_508_507]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_508_507] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_508_507[0]].append(tuple_508_507[1])
                                            self.index_749[tuple_508_507[1]].append(tuple_508_507[0])
                                        # Program VectorAppend Region
                                        vec_543.append(var_508)
                                # Program TransitionState Region
                                tuple_508_507 = (var_508, var_507)
                                prev_state = self.table_15[tuple_508_507]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_508_507] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_508_507[0]].append(tuple_508_507[1])
                        # Program TransitionState Region
                        tuple_508_507 = (var_508, var_507)
                        prev_state = self.table_96[tuple_508_507]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_508_507] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_508_507[1]].append(tuple_508_507[0])
                            # Program VectorAppend Region
                            vec_535.append(var_507)
                        # Program TransitionState Region
                        tuple_507 = var_507
                        prev_state = self.table_40[tuple_507]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_507] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_516.append(var_507)
                        # Program TransitionState Region
                        tuple_507 = var_507
                        prev_state = self.table_18[tuple_507]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_507] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program TransitionState Region
                            tuple_507_507 = (var_507, var_507)
                            prev_state = self.table_6[tuple_507_507]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_507_507] = 1 | 4
                                if not present_bit:
                                    self.index_287[tuple_507_507[1]].append(tuple_507_507[0])
                                    self.index_707[tuple_507_507[0]].append(tuple_507_507[1])
                                # Program VectorAppend Region
                                vec_476.append((var_507, var_507))
                            # Program VectorAppend Region
                            vec_535.append(var_507)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_512: int
                            scan_index_512: int = 0
                            scan_tuple_512_vec: List[int] = self.index_158[var_507]
                            while scan_index_512 < len(scan_tuple_512_vec):
                                scan_tuple_512 = scan_tuple_512_vec[scan_index_512]
                                scan_index_512 += 1
                                vec_512.append(scan_tuple_512)
                            # Program VectorLoop Region
                            vec_index512 = 0
                            while vec_index512 < len(vec_512):
                                var_513 = vec_512[vec_index512]
                                vec_index512 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_507_513 = (var_507, var_513)
                                prev_state = self.table_30[tuple_507_513]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_30[tuple_507_513] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_161_(var_507, var_513)

                                    # Program Call Region
                                    ret = self.proc_165_(var_507, var_513)

                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_508_507 = (var_508, var_507)
                            prev_state = self.table_48[tuple_508_507]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_508_507] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_508_507[0]].append(tuple_508_507[1])
                                # Program VectorAppend Region
                                vec_523.append(var_508)
        # Program VectorClear Region
        del vec_505[:]
        vec_index505 = 0
        # Program VectorUnique Region
        vec_516 = list(set(vec_516))
        vec_index516 = 0
        # Program TableJoin Region
        while vec_index516 < len(vec_516):
            var_518 = vec_516[vec_index516]
            vec_index516 += 1
            if var_518 in self.index_253:
                if var_518 in self.index_254:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_518 = var_518
                    prev_state = self.table_18[tuple_518]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_518] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_518_518 = (var_518, var_518)
                        prev_state = self.table_6[tuple_518_518]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_518_518] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_518_518[1]].append(tuple_518_518[0])
                                self.index_707[tuple_518_518[0]].append(tuple_518_518[1])
                            # Program VectorAppend Region
                            vec_476.append((var_518, var_518))
                        # Program VectorAppend Region
                        vec_535.append(var_518)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_519: int
                        scan_index_519: int = 0
                        scan_tuple_519_vec: List[int] = self.index_158[var_518]
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
                            prev_state = self.table_30[tuple_518_520]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_518_520] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_518, var_520)

                                # Program Call Region
                                ret = self.proc_165_(var_518, var_520)

        # Program VectorClear Region
        del vec_516[:]
        vec_index516 = 0
        # Program VectorUnique Region
        vec_523 = list(set(vec_523))
        vec_index523 = 0
        # Program TableJoin Region
        while vec_index523 < len(vec_523):
            var_525 = vec_523[vec_index523]
            vec_index523 += 1
            if var_525 in self.index_134:
                tuple_524_1_index: int = 0
                tuple_524_1_vec: List[int] = self.index_262[var_525]
                while tuple_524_1_index < len(tuple_524_1_vec):
                    tuple_524_1 = tuple_524_1_vec[tuple_524_1_index]
                    tuple_524_1_index += 1
                    var_526 = tuple_524_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_525_526 = (var_525, var_526)
                    prev_state = self.table_51[tuple_525_526]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_525_526] = 1 | 4
                        if not present_bit:
                            self.index_267[tuple_525_526[1]].append(tuple_525_526[0])
                        # Program VectorAppend Region
                        vec_527.append(var_526)
        # Program VectorClear Region
        del vec_523[:]
        vec_index523 = 0
        # Program VectorUnique Region
        vec_527 = list(set(vec_527))
        vec_index527 = 0
        # Program TableJoin Region
        while vec_index527 < len(vec_527):
            var_529 = vec_527[vec_index527]
            vec_index527 += 1
            if var_529 in self.index_253:
                tuple_528_1_index: int = 0
                tuple_528_1_vec: List[int] = self.index_267[var_529]
                while tuple_528_1_index < len(tuple_528_1_vec):
                    tuple_528_1 = tuple_528_1_vec[tuple_528_1_index]
                    tuple_528_1_index += 1
                    var_530 = tuple_528_1
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
                        # Program TransitionState Region
                        tuple_530_530 = (var_530, var_530)
                        prev_state = self.table_6[tuple_530_530]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_530_530] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_530_530[1]].append(tuple_530_530[0])
                                self.index_707[tuple_530_530[0]].append(tuple_530_530[1])
                            # Program VectorAppend Region
                            vec_476.append((var_530, var_530))
                        # Program VectorAppend Region
                        vec_535.append(var_530)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_531: int
                        scan_index_531: int = 0
                        scan_tuple_531_vec: List[int] = self.index_158[var_530]
                        while scan_index_531 < len(scan_tuple_531_vec):
                            scan_tuple_531 = scan_tuple_531_vec[scan_index_531]
                            scan_index_531 += 1
                            vec_531.append(scan_tuple_531)
                        # Program VectorLoop Region
                        vec_index531 = 0
                        while vec_index531 < len(vec_531):
                            var_532 = vec_531[vec_index531]
                            vec_index531 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_530_532 = (var_530, var_532)
                            prev_state = self.table_30[tuple_530_532]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_530_532] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_530, var_532)

                                # Program Call Region
                                ret = self.proc_165_(var_530, var_532)

        # Program VectorClear Region
        del vec_527[:]
        vec_index527 = 0
        # Program VectorUnique Region
        vec_535 = list(set(vec_535))
        vec_index535 = 0
        # Program TableJoin Region
        while vec_index535 < len(vec_535):
            var_537 = vec_535[vec_index535]
            vec_index535 += 1
            tuple_536_0_index: int = 0
            tuple_536_0_vec: List[int] = self.index_276[var_537]
            while tuple_536_0_index < len(tuple_536_0_vec):
                tuple_536_0 = tuple_536_0_vec[tuple_536_0_index]
                tuple_536_0_index += 1
                var_538 = tuple_536_0
                if var_537 in self.index_277:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_538_537 = (var_538, var_537)
                    prev_state = self.table_99[tuple_538_537]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_99[tuple_538_537] = 1 | 4
                        if not present_bit:
                            self.index_282[tuple_538_537[1]].append(tuple_538_537[0])
                        # Program VectorAppend Region
                        vec_539.append(var_537)
                    # Program TransitionState Region
                    tuple_538_537 = (var_538, var_537)
                    prev_state = self.table_20[tuple_538_537]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_538_537] = 1 | 4
                        if not present_bit:
                            self.index_715[tuple_538_537[0]].append(tuple_538_537[1])
        # Program VectorClear Region
        del vec_535[:]
        vec_index535 = 0
        # Program VectorUnique Region
        vec_539 = list(set(vec_539))
        vec_index539 = 0
        # Program TableJoin Region
        while vec_index539 < len(vec_539):
            var_541 = vec_539[vec_index539]
            vec_index539 += 1
            tuple_540_0_index: int = 0
            tuple_540_0_vec: List[int] = self.index_282[var_541]
            while tuple_540_0_index < len(tuple_540_0_vec):
                tuple_540_0 = tuple_540_0_vec[tuple_540_0_index]
                tuple_540_0_index += 1
                var_542 = tuple_540_0
                if var_541 in self.index_253:
                    # Program TransitionState Region
                    tuple_542 = var_542
                    prev_state = self.table_13[tuple_542]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_542] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_539[:]
        vec_index539 = 0
        # Program VectorUnique Region
        vec_543 = list(set(vec_543))
        vec_index543 = 0
        # Program TableJoin Region
        while vec_index543 < len(vec_543):
            var_545 = vec_543[vec_index543]
            vec_index543 += 1
            tuple_544_0_index: int = 0
            tuple_544_0_vec: List[int] = self.index_287[var_545]
            while tuple_544_0_index < len(tuple_544_0_vec):
                tuple_544_0 = tuple_544_0_vec[tuple_544_0_index]
                tuple_544_0_index += 1
                var_546 = tuple_544_0
                tuple_544_1_index: int = 0
                tuple_544_1_vec: List[int] = self.index_288[var_545]
                while tuple_544_1_index < len(tuple_544_1_vec):
                    tuple_544_1 = tuple_544_1_vec[tuple_544_1_index]
                    tuple_544_1_index += 1
                    var_547 = tuple_544_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_291_(var_546, var_545)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_147_(var_545, var_547)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_296_(var_546, var_547)
                            if not ret:
                                # Program TransitionState Region
                                tuple_546_547 = (var_546, var_547)
                                prev_state = self.table_6[tuple_546_547]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_546_547] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_546_547[1]].append(tuple_546_547[0])
                                        self.index_707[tuple_546_547[0]].append(tuple_546_547[1])
                                    # Program VectorAppend Region
                                    vec_476.append((var_546, var_547))
        # Program VectorClear Region
        del vec_543[:]
        vec_index543 = 0
        # Induction Fixpoint Loop Region
        while len(vec_476):
            # Program Call Region
            param_478_0 = [vec_476]
            ret = self.proc_151_(param_478_0)
            vec_476 = param_478_0[0]

        vec_index476 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_476[:]
        vec_index476 = 0
        # Program Return Region
        return False
        return False

    def address_operand_2(self, vec_552: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index552: int = 0
        vec_555: List[int] = list()
        vec_index555: int = 0
        vec_559: List[int] = list()
        vec_index559: int = 0
        vec_563: List[int] = list()
        vec_index563: int = 0
        vec_568: List[int] = list()
        vec_index568: int = 0
        vec_573: List[int] = list()
        vec_index573: int = 0
        vec_580: List[Tuple[int, int]] = list()
        vec_index580: int = 0
        vec_583: List[int] = list()
        vec_index583: int = 0
        vec_587: List[int] = list()
        vec_index587: int = 0
        vec_594: List[int] = list()
        vec_index594: int = 0
        vec_598: List[int] = list()
        vec_index598: int = 0
        vec_601: List[int] = list()
        vec_index601: int = 0
        vec_605: List[int] = list()
        vec_index605: int = 0
        vec_609: List[int] = list()
        vec_index609: int = 0
        vec_613: List[int] = list()
        vec_index613: int = 0
        vec_617: List[int] = list()
        vec_index617: int = 0
        vec_621: List[int] = list()
        vec_index621: int = 0
        vec_625: List[int] = list()
        vec_index625: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index552 = 0
        while vec_index552 < len(vec_552):
            var_553, var_554 = vec_552[vec_index552]
            vec_index552 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_553_554 = (var_553, var_554)
            prev_state = self.table_73[tuple_553_554]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_73[tuple_553_554] = 1 | 4
                if not present_bit:
                    self.index_129[tuple_553_554[0]].append(tuple_553_554[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_559.append(var_553)
                # Program VectorAppend Region
                vec_555.append(var_553)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_553_554 = (var_553, var_554)
            prev_state = self.table_73[tuple_553_554]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_73[tuple_553_554] = 1 | 4
                if not present_bit:
                    self.index_129[tuple_553_554[0]].append(tuple_553_554[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_559.append(var_553)
                # Program VectorAppend Region
                vec_555.append(var_553)
        # Program VectorUnique Region
        vec_555 = list(set(vec_555))
        vec_index555 = 0
        # Program TableJoin Region
        while vec_index555 < len(vec_555):
            var_557 = vec_555[vec_index555]
            vec_index555 += 1
            if var_557 in self.index_128:
                tuple_556_1_index: int = 0
                tuple_556_1_vec: List[int] = self.index_129[var_557]
                while tuple_556_1_index < len(tuple_556_1_vec):
                    tuple_556_1 = tuple_556_1_vec[tuple_556_1_index]
                    tuple_556_1_index += 1
                    var_558 = tuple_556_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_557_558 = (var_557, var_558)
                    prev_state = self.table_87[tuple_557_558]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_87[tuple_557_558] = 1 | 4
                        if not present_bit:
                            self.index_181[tuple_557_558[1]].append(tuple_557_558[0])
                        # Program VectorAppend Region
                        vec_563.append(var_558)
        # Program VectorClear Region
        del vec_555[:]
        vec_index555 = 0
        # Program VectorUnique Region
        vec_559 = list(set(vec_559))
        vec_index559 = 0
        # Program TableJoin Region
        while vec_index559 < len(vec_559):
            var_561 = vec_559[vec_index559]
            vec_index559 += 1
            if var_561 in self.index_134:
                tuple_560_1_index: int = 0
                tuple_560_1_vec: List[int] = self.index_129[var_561]
                while tuple_560_1_index < len(tuple_560_1_vec):
                    tuple_560_1 = tuple_560_1_vec[tuple_560_1_index]
                    tuple_560_1_index += 1
                    var_562 = tuple_560_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_561_562 = (var_561, var_562)
                    prev_state = self.table_79[tuple_561_562]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_79[tuple_561_562] = 1 | 4
                        if not present_bit:
                            self.index_199[tuple_561_562[1]].append(tuple_561_562[0])
                        # Program VectorAppend Region
                        vec_568.append(var_562)
        # Program VectorClear Region
        del vec_559[:]
        vec_index559 = 0
        # Program VectorUnique Region
        vec_563 = list(set(vec_563))
        vec_index563 = 0
        # Program TableJoin Region
        while vec_index563 < len(vec_563):
            var_565 = vec_563[vec_index563]
            vec_index563 += 1
            tuple_564_0_index: int = 0
            tuple_564_0_vec: List[int] = self.index_180[var_565]
            while tuple_564_0_index < len(tuple_564_0_vec):
                tuple_564_0 = tuple_564_0_vec[tuple_564_0_index]
                tuple_564_0_index += 1
                var_566 = tuple_564_0
                tuple_564_1_index: int = 0
                tuple_564_1_vec: List[int] = self.index_181[var_565]
                while tuple_564_1_index < len(tuple_564_1_vec):
                    tuple_564_1 = tuple_564_1_vec[tuple_564_1_index]
                    tuple_564_1_index += 1
                    var_567 = tuple_564_1
                    # Program TransitionState Region
                    tuple_566_567 = (var_566, var_567)
                    prev_state = self.table_90[tuple_566_567]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_90[tuple_566_567] = 1 | 4
                        if not present_bit:
                            self.index_229[tuple_566_567[0]].append(tuple_566_567[1])
                        # Program VectorAppend Region
                        vec_573.append(var_566)
        # Program VectorClear Region
        del vec_563[:]
        vec_index563 = 0
        # Program VectorUnique Region
        vec_568 = list(set(vec_568))
        vec_index568 = 0
        # Program TableJoin Region
        while vec_index568 < len(vec_568):
            var_570 = vec_568[vec_index568]
            vec_index568 += 1
            tuple_569_0_index: int = 0
            tuple_569_0_vec: List[int] = self.index_180[var_570]
            while tuple_569_0_index < len(tuple_569_0_vec):
                tuple_569_0 = tuple_569_0_vec[tuple_569_0_index]
                tuple_569_0_index += 1
                var_571 = tuple_569_0
                tuple_569_1_index: int = 0
                tuple_569_1_vec: List[int] = self.index_199[var_570]
                while tuple_569_1_index < len(tuple_569_1_vec):
                    tuple_569_1 = tuple_569_1_vec[tuple_569_1_index]
                    tuple_569_1_index += 1
                    var_572 = tuple_569_1
                    # Program TransitionState Region
                    tuple_571_572 = (var_571, var_572)
                    prev_state = self.table_82[tuple_571_572]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_82[tuple_571_572] = 1 | 4
                        if not present_bit:
                            self.index_241[tuple_571_572[0]].append(tuple_571_572[1])
                        # Program VectorAppend Region
                        vec_587.append(var_571)
        # Program VectorClear Region
        del vec_568[:]
        vec_index568 = 0
        # Program VectorUnique Region
        vec_573 = list(set(vec_573))
        vec_index573 = 0
        # Program TableJoin Region
        while vec_index573 < len(vec_573):
            var_575 = vec_573[vec_index573]
            vec_index573 += 1
            if var_575 in self.index_140:
                tuple_574_1_index: int = 0
                tuple_574_1_vec: List[int] = self.index_229[var_575]
                while tuple_574_1_index < len(tuple_574_1_vec):
                    tuple_574_1 = tuple_574_1_vec[tuple_574_1_index]
                    tuple_574_1_index += 1
                    var_576 = tuple_574_1
                    # Program TransitionState Region
                    tuple_576_575_0 = (var_576, var_575, self.var_0)
                    prev_state = self.table_9[tuple_576_575_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_576_575_0] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_576_575_0[0], tuple_576_575_0[1])].append(tuple_576_575_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_575_576 = (var_575, var_576)
                        prev_state = self.table_30[tuple_575_576]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_575_576] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_575_576[0]].append(tuple_575_576[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_575)
                        if not ret:
                            # Program TransitionState Region
                            tuple_575_576 = (var_575, var_576)
                            prev_state = self.table_30[tuple_575_576]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_575_576] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_575_576[0]].append(tuple_575_576[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_576, var_575)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_576_575 = (var_576, var_575)
                                    prev_state = self.table_54[tuple_576_575]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_576_575] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_576_575[0]].append(tuple_576_575[1])
                                            self.index_749[tuple_576_575[1]].append(tuple_576_575[0])
                                        # Program VectorAppend Region
                                        vec_625.append(var_576)
                                # Program TransitionState Region
                                tuple_576_575 = (var_576, var_575)
                                prev_state = self.table_15[tuple_576_575]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_576_575] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_576_575[0]].append(tuple_576_575[1])
                        # Program TransitionState Region
                        tuple_576_575 = (var_576, var_575)
                        prev_state = self.table_96[tuple_576_575]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_576_575] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_576_575[1]].append(tuple_576_575[0])
                            # Program VectorAppend Region
                            vec_617.append(var_575)
                        # Program TransitionState Region
                        tuple_575 = var_575
                        prev_state = self.table_40[tuple_575]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_575] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_598.append(var_575)
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
                            # Program TransitionState Region
                            tuple_575_575 = (var_575, var_575)
                            prev_state = self.table_6[tuple_575_575]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_575_575] = 1 | 4
                                if not present_bit:
                                    self.index_287[tuple_575_575[1]].append(tuple_575_575[0])
                                    self.index_707[tuple_575_575[0]].append(tuple_575_575[1])
                                # Program VectorAppend Region
                                vec_580.append((var_575, var_575))
                            # Program VectorAppend Region
                            vec_617.append(var_575)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_583: int
                            scan_index_583: int = 0
                            scan_tuple_583_vec: List[int] = self.index_158[var_575]
                            while scan_index_583 < len(scan_tuple_583_vec):
                                scan_tuple_583 = scan_tuple_583_vec[scan_index_583]
                                scan_index_583 += 1
                                vec_583.append(scan_tuple_583)
                            # Program VectorLoop Region
                            vec_index583 = 0
                            while vec_index583 < len(vec_583):
                                var_584 = vec_583[vec_index583]
                                vec_index583 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_575_584 = (var_575, var_584)
                                prev_state = self.table_30[tuple_575_584]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_30[tuple_575_584] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_161_(var_575, var_584)

                                    # Program Call Region
                                    ret = self.proc_165_(var_575, var_584)

                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_576_575 = (var_576, var_575)
                            prev_state = self.table_48[tuple_576_575]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_576_575] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_576_575[0]].append(tuple_576_575[1])
                                # Program VectorAppend Region
                                vec_605.append(var_576)
        # Program VectorClear Region
        del vec_573[:]
        vec_index573 = 0
        # Program VectorUnique Region
        vec_587 = list(set(vec_587))
        vec_index587 = 0
        # Program TableJoin Region
        while vec_index587 < len(vec_587):
            var_589 = vec_587[vec_index587]
            vec_index587 += 1
            if var_589 in self.index_140:
                tuple_588_1_index: int = 0
                tuple_588_1_vec: List[int] = self.index_241[var_589]
                while tuple_588_1_index < len(tuple_588_1_vec):
                    tuple_588_1 = tuple_588_1_vec[tuple_588_1_index]
                    tuple_588_1_index += 1
                    var_590 = tuple_588_1
                    # Program TransitionState Region
                    tuple_590_589_2 = (var_590, var_589, self.var_2)
                    prev_state = self.table_9[tuple_590_589_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_590_589_2] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_590_589_2[0], tuple_590_589_2[1])].append(tuple_590_589_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_589_590 = (var_589, var_590)
                        prev_state = self.table_30[tuple_589_590]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_589_590] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_589_590[0]].append(tuple_589_590[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_589)
                        if not ret:
                            # Program TransitionState Region
                            tuple_589_590 = (var_589, var_590)
                            prev_state = self.table_30[tuple_589_590]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_589_590] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_589_590[0]].append(tuple_589_590[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_590, var_589)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_590_589 = (var_590, var_589)
                                    prev_state = self.table_54[tuple_590_589]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_590_589] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_590_589[0]].append(tuple_590_589[1])
                                            self.index_749[tuple_590_589[1]].append(tuple_590_589[0])
                                        # Program VectorAppend Region
                                        vec_625.append(var_590)
                                # Program TransitionState Region
                                tuple_590_589 = (var_590, var_589)
                                prev_state = self.table_15[tuple_590_589]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_590_589] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_590_589[0]].append(tuple_590_589[1])
                        # Program TransitionState Region
                        tuple_590_589 = (var_590, var_589)
                        prev_state = self.table_96[tuple_590_589]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_590_589] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_590_589[1]].append(tuple_590_589[0])
                            # Program VectorAppend Region
                            vec_617.append(var_589)
                        # Program TransitionState Region
                        tuple_589 = var_589
                        prev_state = self.table_40[tuple_589]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_589] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_598.append(var_589)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_589 = var_589
                            prev_state = self.table_18[tuple_589]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_589] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_589_589 = (var_589, var_589)
                                prev_state = self.table_6[tuple_589_589]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_589_589] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_589_589[1]].append(tuple_589_589[0])
                                        self.index_707[tuple_589_589[0]].append(tuple_589_589[1])
                                    # Program VectorAppend Region
                                    vec_580.append((var_589, var_589))
                                # Program VectorAppend Region
                                vec_617.append(var_589)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_594: int
                                scan_index_594: int = 0
                                scan_tuple_594_vec: List[int] = self.index_158[var_589]
                                while scan_index_594 < len(scan_tuple_594_vec):
                                    scan_tuple_594 = scan_tuple_594_vec[scan_index_594]
                                    scan_index_594 += 1
                                    vec_594.append(scan_tuple_594)
                                # Program VectorLoop Region
                                vec_index594 = 0
                                while vec_index594 < len(vec_594):
                                    var_595 = vec_594[vec_index594]
                                    vec_index594 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_589_595 = (var_589, var_595)
                                    prev_state = self.table_30[tuple_589_595]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_589_595] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_589, var_595)

                                        # Program Call Region
                                        ret = self.proc_165_(var_589, var_595)

                        # Program TransitionState Region
                        tuple_590_589 = (var_590, var_589)
                        prev_state = self.table_48[tuple_590_589]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_48[tuple_590_589] = 1 | 4
                            if not present_bit:
                                self.index_262[tuple_590_589[0]].append(tuple_590_589[1])
                            # Program VectorAppend Region
                            vec_605.append(var_590)
        # Program VectorClear Region
        del vec_587[:]
        vec_index587 = 0
        # Program VectorUnique Region
        vec_598 = list(set(vec_598))
        vec_index598 = 0
        # Program TableJoin Region
        while vec_index598 < len(vec_598):
            var_600 = vec_598[vec_index598]
            vec_index598 += 1
            if var_600 in self.index_253:
                if var_600 in self.index_254:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_600 = var_600
                    prev_state = self.table_18[tuple_600]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_600] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_600_600 = (var_600, var_600)
                        prev_state = self.table_6[tuple_600_600]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_600_600] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_600_600[1]].append(tuple_600_600[0])
                                self.index_707[tuple_600_600[0]].append(tuple_600_600[1])
                            # Program VectorAppend Region
                            vec_580.append((var_600, var_600))
                        # Program VectorAppend Region
                        vec_617.append(var_600)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_601: int
                        scan_index_601: int = 0
                        scan_tuple_601_vec: List[int] = self.index_158[var_600]
                        while scan_index_601 < len(scan_tuple_601_vec):
                            scan_tuple_601 = scan_tuple_601_vec[scan_index_601]
                            scan_index_601 += 1
                            vec_601.append(scan_tuple_601)
                        # Program VectorLoop Region
                        vec_index601 = 0
                        while vec_index601 < len(vec_601):
                            var_602 = vec_601[vec_index601]
                            vec_index601 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_600_602 = (var_600, var_602)
                            prev_state = self.table_30[tuple_600_602]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_600_602] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_600, var_602)

                                # Program Call Region
                                ret = self.proc_165_(var_600, var_602)

        # Program VectorClear Region
        del vec_598[:]
        vec_index598 = 0
        # Program VectorUnique Region
        vec_605 = list(set(vec_605))
        vec_index605 = 0
        # Program TableJoin Region
        while vec_index605 < len(vec_605):
            var_607 = vec_605[vec_index605]
            vec_index605 += 1
            if var_607 in self.index_134:
                tuple_606_1_index: int = 0
                tuple_606_1_vec: List[int] = self.index_262[var_607]
                while tuple_606_1_index < len(tuple_606_1_vec):
                    tuple_606_1 = tuple_606_1_vec[tuple_606_1_index]
                    tuple_606_1_index += 1
                    var_608 = tuple_606_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_607_608 = (var_607, var_608)
                    prev_state = self.table_51[tuple_607_608]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_607_608] = 1 | 4
                        if not present_bit:
                            self.index_267[tuple_607_608[1]].append(tuple_607_608[0])
                        # Program VectorAppend Region
                        vec_609.append(var_608)
        # Program VectorClear Region
        del vec_605[:]
        vec_index605 = 0
        # Program VectorUnique Region
        vec_609 = list(set(vec_609))
        vec_index609 = 0
        # Program TableJoin Region
        while vec_index609 < len(vec_609):
            var_611 = vec_609[vec_index609]
            vec_index609 += 1
            if var_611 in self.index_253:
                tuple_610_1_index: int = 0
                tuple_610_1_vec: List[int] = self.index_267[var_611]
                while tuple_610_1_index < len(tuple_610_1_vec):
                    tuple_610_1 = tuple_610_1_vec[tuple_610_1_index]
                    tuple_610_1_index += 1
                    var_612 = tuple_610_1
                    # Program TransitionState Region
                    tuple_612 = var_612
                    prev_state = self.table_18[tuple_612]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_612] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_612_612 = (var_612, var_612)
                        prev_state = self.table_6[tuple_612_612]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_612_612] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_612_612[1]].append(tuple_612_612[0])
                                self.index_707[tuple_612_612[0]].append(tuple_612_612[1])
                            # Program VectorAppend Region
                            vec_580.append((var_612, var_612))
                        # Program VectorAppend Region
                        vec_617.append(var_612)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_613: int
                        scan_index_613: int = 0
                        scan_tuple_613_vec: List[int] = self.index_158[var_612]
                        while scan_index_613 < len(scan_tuple_613_vec):
                            scan_tuple_613 = scan_tuple_613_vec[scan_index_613]
                            scan_index_613 += 1
                            vec_613.append(scan_tuple_613)
                        # Program VectorLoop Region
                        vec_index613 = 0
                        while vec_index613 < len(vec_613):
                            var_614 = vec_613[vec_index613]
                            vec_index613 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_612_614 = (var_612, var_614)
                            prev_state = self.table_30[tuple_612_614]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_612_614] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_612, var_614)

                                # Program Call Region
                                ret = self.proc_165_(var_612, var_614)

        # Program VectorClear Region
        del vec_609[:]
        vec_index609 = 0
        # Program VectorUnique Region
        vec_617 = list(set(vec_617))
        vec_index617 = 0
        # Program TableJoin Region
        while vec_index617 < len(vec_617):
            var_619 = vec_617[vec_index617]
            vec_index617 += 1
            tuple_618_0_index: int = 0
            tuple_618_0_vec: List[int] = self.index_276[var_619]
            while tuple_618_0_index < len(tuple_618_0_vec):
                tuple_618_0 = tuple_618_0_vec[tuple_618_0_index]
                tuple_618_0_index += 1
                var_620 = tuple_618_0
                if var_619 in self.index_277:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_620_619 = (var_620, var_619)
                    prev_state = self.table_99[tuple_620_619]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_99[tuple_620_619] = 1 | 4
                        if not present_bit:
                            self.index_282[tuple_620_619[1]].append(tuple_620_619[0])
                        # Program VectorAppend Region
                        vec_621.append(var_619)
                    # Program TransitionState Region
                    tuple_620_619 = (var_620, var_619)
                    prev_state = self.table_20[tuple_620_619]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_620_619] = 1 | 4
                        if not present_bit:
                            self.index_715[tuple_620_619[0]].append(tuple_620_619[1])
        # Program VectorClear Region
        del vec_617[:]
        vec_index617 = 0
        # Program VectorUnique Region
        vec_621 = list(set(vec_621))
        vec_index621 = 0
        # Program TableJoin Region
        while vec_index621 < len(vec_621):
            var_623 = vec_621[vec_index621]
            vec_index621 += 1
            tuple_622_0_index: int = 0
            tuple_622_0_vec: List[int] = self.index_282[var_623]
            while tuple_622_0_index < len(tuple_622_0_vec):
                tuple_622_0 = tuple_622_0_vec[tuple_622_0_index]
                tuple_622_0_index += 1
                var_624 = tuple_622_0
                if var_623 in self.index_253:
                    # Program TransitionState Region
                    tuple_624 = var_624
                    prev_state = self.table_13[tuple_624]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_624] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_621[:]
        vec_index621 = 0
        # Program VectorUnique Region
        vec_625 = list(set(vec_625))
        vec_index625 = 0
        # Program TableJoin Region
        while vec_index625 < len(vec_625):
            var_627 = vec_625[vec_index625]
            vec_index625 += 1
            tuple_626_0_index: int = 0
            tuple_626_0_vec: List[int] = self.index_287[var_627]
            while tuple_626_0_index < len(tuple_626_0_vec):
                tuple_626_0 = tuple_626_0_vec[tuple_626_0_index]
                tuple_626_0_index += 1
                var_628 = tuple_626_0
                tuple_626_1_index: int = 0
                tuple_626_1_vec: List[int] = self.index_288[var_627]
                while tuple_626_1_index < len(tuple_626_1_vec):
                    tuple_626_1 = tuple_626_1_vec[tuple_626_1_index]
                    tuple_626_1_index += 1
                    var_629 = tuple_626_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_291_(var_628, var_627)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_147_(var_627, var_629)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_296_(var_628, var_629)
                            if not ret:
                                # Program TransitionState Region
                                tuple_628_629 = (var_628, var_629)
                                prev_state = self.table_6[tuple_628_629]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_628_629] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_628_629[1]].append(tuple_628_629[0])
                                        self.index_707[tuple_628_629[0]].append(tuple_628_629[1])
                                    # Program VectorAppend Region
                                    vec_580.append((var_628, var_629))
        # Program VectorClear Region
        del vec_625[:]
        vec_index625 = 0
        # Induction Fixpoint Loop Region
        while len(vec_580):
            # Program Call Region
            param_582_0 = [vec_580]
            ret = self.proc_151_(param_582_0)
            vec_580 = param_582_0[0]

        vec_index580 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_580[:]
        vec_index580 = 0
        # Program Return Region
        return False
        return False

    def relocation_2(self, vec_634: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index634: int = 0
        vec_637: List[int] = list()
        vec_index637: int = 0
        vec_642: List[int] = list()
        vec_index642: int = 0
        vec_647: List[int] = list()
        vec_index647: int = 0
        vec_654: List[Tuple[int, int]] = list()
        vec_index654: int = 0
        vec_657: List[int] = list()
        vec_index657: int = 0
        vec_661: List[int] = list()
        vec_index661: int = 0
        vec_668: List[int] = list()
        vec_index668: int = 0
        vec_672: List[int] = list()
        vec_index672: int = 0
        vec_675: List[int] = list()
        vec_index675: int = 0
        vec_679: List[int] = list()
        vec_index679: int = 0
        vec_683: List[int] = list()
        vec_index683: int = 0
        vec_687: List[int] = list()
        vec_index687: int = 0
        vec_691: List[int] = list()
        vec_index691: int = 0
        vec_695: List[int] = list()
        vec_index695: int = 0
        vec_699: List[int] = list()
        vec_index699: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index634 = 0
        while vec_index634 < len(vec_634):
            var_635, var_636 = vec_634[vec_index634]
            vec_index634 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_635_636 = (var_635, var_636)
            prev_state = self.table_76[tuple_635_636]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_76[tuple_635_636] = 1 | 4
                if not present_bit:
                    self.index_180[tuple_635_636[0]].append(tuple_635_636[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_642.append(var_635)
                # Program VectorAppend Region
                vec_637.append(var_635)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_635_636 = (var_635, var_636)
            prev_state = self.table_76[tuple_635_636]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_76[tuple_635_636] = 1 | 4
                if not present_bit:
                    self.index_180[tuple_635_636[0]].append(tuple_635_636[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_642.append(var_635)
                # Program VectorAppend Region
                vec_637.append(var_635)
        # Program VectorUnique Region
        vec_637 = list(set(vec_637))
        vec_index637 = 0
        # Program TableJoin Region
        while vec_index637 < len(vec_637):
            var_639 = vec_637[vec_index637]
            vec_index637 += 1
            tuple_638_0_index: int = 0
            tuple_638_0_vec: List[int] = self.index_180[var_639]
            while tuple_638_0_index < len(tuple_638_0_vec):
                tuple_638_0 = tuple_638_0_vec[tuple_638_0_index]
                tuple_638_0_index += 1
                var_640 = tuple_638_0
                tuple_638_1_index: int = 0
                tuple_638_1_vec: List[int] = self.index_181[var_639]
                while tuple_638_1_index < len(tuple_638_1_vec):
                    tuple_638_1 = tuple_638_1_vec[tuple_638_1_index]
                    tuple_638_1_index += 1
                    var_641 = tuple_638_1
                    # Program TransitionState Region
                    tuple_640_641 = (var_640, var_641)
                    prev_state = self.table_90[tuple_640_641]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_90[tuple_640_641] = 1 | 4
                        if not present_bit:
                            self.index_229[tuple_640_641[0]].append(tuple_640_641[1])
                        # Program VectorAppend Region
                        vec_647.append(var_640)
        # Program VectorClear Region
        del vec_637[:]
        vec_index637 = 0
        # Program VectorUnique Region
        vec_642 = list(set(vec_642))
        vec_index642 = 0
        # Program TableJoin Region
        while vec_index642 < len(vec_642):
            var_644 = vec_642[vec_index642]
            vec_index642 += 1
            tuple_643_0_index: int = 0
            tuple_643_0_vec: List[int] = self.index_180[var_644]
            while tuple_643_0_index < len(tuple_643_0_vec):
                tuple_643_0 = tuple_643_0_vec[tuple_643_0_index]
                tuple_643_0_index += 1
                var_645 = tuple_643_0
                tuple_643_1_index: int = 0
                tuple_643_1_vec: List[int] = self.index_199[var_644]
                while tuple_643_1_index < len(tuple_643_1_vec):
                    tuple_643_1 = tuple_643_1_vec[tuple_643_1_index]
                    tuple_643_1_index += 1
                    var_646 = tuple_643_1
                    # Program TransitionState Region
                    tuple_645_646 = (var_645, var_646)
                    prev_state = self.table_82[tuple_645_646]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_82[tuple_645_646] = 1 | 4
                        if not present_bit:
                            self.index_241[tuple_645_646[0]].append(tuple_645_646[1])
                        # Program VectorAppend Region
                        vec_661.append(var_645)
        # Program VectorClear Region
        del vec_642[:]
        vec_index642 = 0
        # Program VectorUnique Region
        vec_647 = list(set(vec_647))
        vec_index647 = 0
        # Program TableJoin Region
        while vec_index647 < len(vec_647):
            var_649 = vec_647[vec_index647]
            vec_index647 += 1
            if var_649 in self.index_140:
                tuple_648_1_index: int = 0
                tuple_648_1_vec: List[int] = self.index_229[var_649]
                while tuple_648_1_index < len(tuple_648_1_vec):
                    tuple_648_1 = tuple_648_1_vec[tuple_648_1_index]
                    tuple_648_1_index += 1
                    var_650 = tuple_648_1
                    # Program TransitionState Region
                    tuple_650_649_0 = (var_650, var_649, self.var_0)
                    prev_state = self.table_9[tuple_650_649_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_650_649_0] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_650_649_0[0], tuple_650_649_0[1])].append(tuple_650_649_0[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_649_650 = (var_649, var_650)
                        prev_state = self.table_30[tuple_649_650]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_649_650] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_649_650[0]].append(tuple_649_650[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_649)
                        if not ret:
                            # Program TransitionState Region
                            tuple_649_650 = (var_649, var_650)
                            prev_state = self.table_30[tuple_649_650]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_649_650] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_649_650[0]].append(tuple_649_650[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_650, var_649)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_650_649 = (var_650, var_649)
                                    prev_state = self.table_54[tuple_650_649]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_650_649] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_650_649[0]].append(tuple_650_649[1])
                                            self.index_749[tuple_650_649[1]].append(tuple_650_649[0])
                                        # Program VectorAppend Region
                                        vec_699.append(var_650)
                                # Program TransitionState Region
                                tuple_650_649 = (var_650, var_649)
                                prev_state = self.table_15[tuple_650_649]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_650_649] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_650_649[0]].append(tuple_650_649[1])
                        # Program TransitionState Region
                        tuple_650_649 = (var_650, var_649)
                        prev_state = self.table_96[tuple_650_649]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_650_649] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_650_649[1]].append(tuple_650_649[0])
                            # Program VectorAppend Region
                            vec_691.append(var_649)
                        # Program TransitionState Region
                        tuple_649 = var_649
                        prev_state = self.table_40[tuple_649]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_649] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_672.append(var_649)
                        # Program TransitionState Region
                        tuple_649 = var_649
                        prev_state = self.table_18[tuple_649]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_18[tuple_649] = 1 | 4
                            if not present_bit:
                                pass
                            # Program Parallel Region
                            # Program TransitionState Region
                            tuple_649_649 = (var_649, var_649)
                            prev_state = self.table_6[tuple_649_649]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_6[tuple_649_649] = 1 | 4
                                if not present_bit:
                                    self.index_287[tuple_649_649[1]].append(tuple_649_649[0])
                                    self.index_707[tuple_649_649[0]].append(tuple_649_649[1])
                                # Program VectorAppend Region
                                vec_654.append((var_649, var_649))
                            # Program VectorAppend Region
                            vec_691.append(var_649)
                            # Program Series Region
                            # Program TableScan Region
                            scan_tuple_657: int
                            scan_index_657: int = 0
                            scan_tuple_657_vec: List[int] = self.index_158[var_649]
                            while scan_index_657 < len(scan_tuple_657_vec):
                                scan_tuple_657 = scan_tuple_657_vec[scan_index_657]
                                scan_index_657 += 1
                                vec_657.append(scan_tuple_657)
                            # Program VectorLoop Region
                            vec_index657 = 0
                            while vec_index657 < len(vec_657):
                                var_658 = vec_657[vec_index657]
                                vec_index657 += 1
                                # Program TransitionState Region
                                # Remove from negated view
                                tuple_649_658 = (var_649, var_658)
                                prev_state = self.table_30[tuple_649_658]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 1:
                                    self.table_30[tuple_649_658] = 0 | 4
                                    # Program Parallel Region
                                    # Program Call Region
                                    ret = self.proc_161_(var_649, var_658)

                                    # Program Call Region
                                    ret = self.proc_165_(var_649, var_658)

                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_650_649 = (var_650, var_649)
                            prev_state = self.table_48[tuple_650_649]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_48[tuple_650_649] = 1 | 4
                                if not present_bit:
                                    self.index_262[tuple_650_649[0]].append(tuple_650_649[1])
                                # Program VectorAppend Region
                                vec_679.append(var_650)
        # Program VectorClear Region
        del vec_647[:]
        vec_index647 = 0
        # Program VectorUnique Region
        vec_661 = list(set(vec_661))
        vec_index661 = 0
        # Program TableJoin Region
        while vec_index661 < len(vec_661):
            var_663 = vec_661[vec_index661]
            vec_index661 += 1
            if var_663 in self.index_140:
                tuple_662_1_index: int = 0
                tuple_662_1_vec: List[int] = self.index_241[var_663]
                while tuple_662_1_index < len(tuple_662_1_vec):
                    tuple_662_1 = tuple_662_1_vec[tuple_662_1_index]
                    tuple_662_1_index += 1
                    var_664 = tuple_662_1
                    # Program TransitionState Region
                    tuple_664_663_2 = (var_664, var_663, self.var_2)
                    prev_state = self.table_9[tuple_664_663_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_9[tuple_664_663_2] = 1 | 4
                        if not present_bit:
                            self.index_729[(tuple_664_663_2[0], tuple_664_663_2[1])].append(tuple_664_663_2[2])
                        # Program Parallel Region
                        # Program Series Region
                        # Program TransitionState Region
                        # Eager insert before negation to prevent race
                        tuple_663_664 = (var_663, var_664)
                        prev_state = self.table_30[tuple_663_664]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0:
                            self.table_30[tuple_663_664] = 2 | 4
                            if not present_bit:
                                self.index_158[tuple_663_664[0]].append(tuple_663_664[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                        ret = self.proc_144_(var_663)
                        if not ret:
                            # Program TransitionState Region
                            tuple_663_664 = (var_663, var_664)
                            prev_state = self.table_30[tuple_663_664]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_30[tuple_663_664] = 1 | 4
                                if not present_bit:
                                    self.index_158[tuple_663_664[0]].append(tuple_663_664[1])
                                # Program Parallel Region
                                # Program Call Region
                                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                                ret = self.proc_147_(var_664, var_663)
                                if not ret:
                                    # Program TransitionState Region
                                    tuple_664_663 = (var_664, var_663)
                                    prev_state = self.table_54[tuple_664_663]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 0 or state == 2:
                                        self.table_54[tuple_664_663] = 1 | 4
                                        if not present_bit:
                                            self.index_288[tuple_664_663[0]].append(tuple_664_663[1])
                                            self.index_749[tuple_664_663[1]].append(tuple_664_663[0])
                                        # Program VectorAppend Region
                                        vec_699.append(var_664)
                                # Program TransitionState Region
                                tuple_664_663 = (var_664, var_663)
                                prev_state = self.table_15[tuple_664_663]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_664_663] = 1 | 4
                                    if not present_bit:
                                        self.index_711[tuple_664_663[0]].append(tuple_664_663[1])
                        # Program TransitionState Region
                        tuple_664_663 = (var_664, var_663)
                        prev_state = self.table_96[tuple_664_663]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_96[tuple_664_663] = 1 | 4
                            if not present_bit:
                                self.index_276[tuple_664_663[1]].append(tuple_664_663[0])
                            # Program VectorAppend Region
                            vec_691.append(var_663)
                        # Program TransitionState Region
                        tuple_663 = var_663
                        prev_state = self.table_40[tuple_663]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_40[tuple_663] = 1 | 4
                            if not present_bit:
                                pass
                            # Program VectorAppend Region
                            vec_672.append(var_663)
                        # Program TupleCompare Region
                        if self.var_0 == self.var_2:
                            # Program TransitionState Region
                            tuple_663 = var_663
                            prev_state = self.table_18[tuple_663]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_18[tuple_663] = 1 | 4
                                if not present_bit:
                                    pass
                                # Program Parallel Region
                                # Program TransitionState Region
                                tuple_663_663 = (var_663, var_663)
                                prev_state = self.table_6[tuple_663_663]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_663_663] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_663_663[1]].append(tuple_663_663[0])
                                        self.index_707[tuple_663_663[0]].append(tuple_663_663[1])
                                    # Program VectorAppend Region
                                    vec_654.append((var_663, var_663))
                                # Program VectorAppend Region
                                vec_691.append(var_663)
                                # Program Series Region
                                # Program TableScan Region
                                scan_tuple_668: int
                                scan_index_668: int = 0
                                scan_tuple_668_vec: List[int] = self.index_158[var_663]
                                while scan_index_668 < len(scan_tuple_668_vec):
                                    scan_tuple_668 = scan_tuple_668_vec[scan_index_668]
                                    scan_index_668 += 1
                                    vec_668.append(scan_tuple_668)
                                # Program VectorLoop Region
                                vec_index668 = 0
                                while vec_index668 < len(vec_668):
                                    var_669 = vec_668[vec_index668]
                                    vec_index668 += 1
                                    # Program TransitionState Region
                                    # Remove from negated view
                                    tuple_663_669 = (var_663, var_669)
                                    prev_state = self.table_30[tuple_663_669]
                                    state = prev_state & 3
                                    present_bit = prev_state & 4
                                    if state == 1:
                                        self.table_30[tuple_663_669] = 0 | 4
                                        # Program Parallel Region
                                        # Program Call Region
                                        ret = self.proc_161_(var_663, var_669)

                                        # Program Call Region
                                        ret = self.proc_165_(var_663, var_669)

                        # Program TransitionState Region
                        tuple_664_663 = (var_664, var_663)
                        prev_state = self.table_48[tuple_664_663]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_48[tuple_664_663] = 1 | 4
                            if not present_bit:
                                self.index_262[tuple_664_663[0]].append(tuple_664_663[1])
                            # Program VectorAppend Region
                            vec_679.append(var_664)
        # Program VectorClear Region
        del vec_661[:]
        vec_index661 = 0
        # Program VectorUnique Region
        vec_672 = list(set(vec_672))
        vec_index672 = 0
        # Program TableJoin Region
        while vec_index672 < len(vec_672):
            var_674 = vec_672[vec_index672]
            vec_index672 += 1
            if var_674 in self.index_253:
                if var_674 in self.index_254:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_674 = var_674
                    prev_state = self.table_18[tuple_674]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_674] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_674_674 = (var_674, var_674)
                        prev_state = self.table_6[tuple_674_674]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_674_674] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_674_674[1]].append(tuple_674_674[0])
                                self.index_707[tuple_674_674[0]].append(tuple_674_674[1])
                            # Program VectorAppend Region
                            vec_654.append((var_674, var_674))
                        # Program VectorAppend Region
                        vec_691.append(var_674)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_675: int
                        scan_index_675: int = 0
                        scan_tuple_675_vec: List[int] = self.index_158[var_674]
                        while scan_index_675 < len(scan_tuple_675_vec):
                            scan_tuple_675 = scan_tuple_675_vec[scan_index_675]
                            scan_index_675 += 1
                            vec_675.append(scan_tuple_675)
                        # Program VectorLoop Region
                        vec_index675 = 0
                        while vec_index675 < len(vec_675):
                            var_676 = vec_675[vec_index675]
                            vec_index675 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_674_676 = (var_674, var_676)
                            prev_state = self.table_30[tuple_674_676]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_674_676] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_674, var_676)

                                # Program Call Region
                                ret = self.proc_165_(var_674, var_676)

        # Program VectorClear Region
        del vec_672[:]
        vec_index672 = 0
        # Program VectorUnique Region
        vec_679 = list(set(vec_679))
        vec_index679 = 0
        # Program TableJoin Region
        while vec_index679 < len(vec_679):
            var_681 = vec_679[vec_index679]
            vec_index679 += 1
            if var_681 in self.index_134:
                tuple_680_1_index: int = 0
                tuple_680_1_vec: List[int] = self.index_262[var_681]
                while tuple_680_1_index < len(tuple_680_1_vec):
                    tuple_680_1 = tuple_680_1_vec[tuple_680_1_index]
                    tuple_680_1_index += 1
                    var_682 = tuple_680_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_681_682 = (var_681, var_682)
                    prev_state = self.table_51[tuple_681_682]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_51[tuple_681_682] = 1 | 4
                        if not present_bit:
                            self.index_267[tuple_681_682[1]].append(tuple_681_682[0])
                        # Program VectorAppend Region
                        vec_683.append(var_682)
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
            if var_685 in self.index_253:
                tuple_684_1_index: int = 0
                tuple_684_1_vec: List[int] = self.index_267[var_685]
                while tuple_684_1_index < len(tuple_684_1_vec):
                    tuple_684_1 = tuple_684_1_vec[tuple_684_1_index]
                    tuple_684_1_index += 1
                    var_686 = tuple_684_1
                    # Program TransitionState Region
                    tuple_686 = var_686
                    prev_state = self.table_18[tuple_686]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_18[tuple_686] = 1 | 4
                        if not present_bit:
                            pass
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_686_686 = (var_686, var_686)
                        prev_state = self.table_6[tuple_686_686]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_6[tuple_686_686] = 1 | 4
                            if not present_bit:
                                self.index_287[tuple_686_686[1]].append(tuple_686_686[0])
                                self.index_707[tuple_686_686[0]].append(tuple_686_686[1])
                            # Program VectorAppend Region
                            vec_654.append((var_686, var_686))
                        # Program VectorAppend Region
                        vec_691.append(var_686)
                        # Program Series Region
                        # Program TableScan Region
                        scan_tuple_687: int
                        scan_index_687: int = 0
                        scan_tuple_687_vec: List[int] = self.index_158[var_686]
                        while scan_index_687 < len(scan_tuple_687_vec):
                            scan_tuple_687 = scan_tuple_687_vec[scan_index_687]
                            scan_index_687 += 1
                            vec_687.append(scan_tuple_687)
                        # Program VectorLoop Region
                        vec_index687 = 0
                        while vec_index687 < len(vec_687):
                            var_688 = vec_687[vec_index687]
                            vec_index687 += 1
                            # Program TransitionState Region
                            # Remove from negated view
                            tuple_686_688 = (var_686, var_688)
                            prev_state = self.table_30[tuple_686_688]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 1:
                                self.table_30[tuple_686_688] = 0 | 4
                                # Program Parallel Region
                                # Program Call Region
                                ret = self.proc_161_(var_686, var_688)

                                # Program Call Region
                                ret = self.proc_165_(var_686, var_688)

        # Program VectorClear Region
        del vec_683[:]
        vec_index683 = 0
        # Program VectorUnique Region
        vec_691 = list(set(vec_691))
        vec_index691 = 0
        # Program TableJoin Region
        while vec_index691 < len(vec_691):
            var_693 = vec_691[vec_index691]
            vec_index691 += 1
            tuple_692_0_index: int = 0
            tuple_692_0_vec: List[int] = self.index_276[var_693]
            while tuple_692_0_index < len(tuple_692_0_vec):
                tuple_692_0 = tuple_692_0_vec[tuple_692_0_index]
                tuple_692_0_index += 1
                var_694 = tuple_692_0
                if var_693 in self.index_277:
                    # Program Parallel Region
                    # Program TransitionState Region
                    tuple_694_693 = (var_694, var_693)
                    prev_state = self.table_99[tuple_694_693]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_99[tuple_694_693] = 1 | 4
                        if not present_bit:
                            self.index_282[tuple_694_693[1]].append(tuple_694_693[0])
                        # Program VectorAppend Region
                        vec_695.append(var_693)
                    # Program TransitionState Region
                    tuple_694_693 = (var_694, var_693)
                    prev_state = self.table_20[tuple_694_693]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_694_693] = 1 | 4
                        if not present_bit:
                            self.index_715[tuple_694_693[0]].append(tuple_694_693[1])
        # Program VectorClear Region
        del vec_691[:]
        vec_index691 = 0
        # Program VectorUnique Region
        vec_695 = list(set(vec_695))
        vec_index695 = 0
        # Program TableJoin Region
        while vec_index695 < len(vec_695):
            var_697 = vec_695[vec_index695]
            vec_index695 += 1
            tuple_696_0_index: int = 0
            tuple_696_0_vec: List[int] = self.index_282[var_697]
            while tuple_696_0_index < len(tuple_696_0_vec):
                tuple_696_0 = tuple_696_0_vec[tuple_696_0_index]
                tuple_696_0_index += 1
                var_698 = tuple_696_0
                if var_697 in self.index_253:
                    # Program TransitionState Region
                    tuple_698 = var_698
                    prev_state = self.table_13[tuple_698]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_13[tuple_698] = 1 | 4
                        if not present_bit:
                            pass
        # Program VectorClear Region
        del vec_695[:]
        vec_index695 = 0
        # Program VectorUnique Region
        vec_699 = list(set(vec_699))
        vec_index699 = 0
        # Program TableJoin Region
        while vec_index699 < len(vec_699):
            var_701 = vec_699[vec_index699]
            vec_index699 += 1
            tuple_700_0_index: int = 0
            tuple_700_0_vec: List[int] = self.index_287[var_701]
            while tuple_700_0_index < len(tuple_700_0_vec):
                tuple_700_0 = tuple_700_0_vec[tuple_700_0_index]
                tuple_700_0_index += 1
                var_702 = tuple_700_0
                tuple_700_1_index: int = 0
                tuple_700_1_vec: List[int] = self.index_288[var_701]
                while tuple_700_1_index < len(tuple_700_1_vec):
                    tuple_700_1 = tuple_700_1_vec[tuple_700_1_index]
                    tuple_700_1_index += 1
                    var_703 = tuple_700_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_291_(var_702, var_701)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_147_(var_701, var_703)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_296_(var_702, var_703)
                            if not ret:
                                # Program TransitionState Region
                                tuple_702_703 = (var_702, var_703)
                                prev_state = self.table_6[tuple_702_703]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_6[tuple_702_703] = 1 | 4
                                    if not present_bit:
                                        self.index_287[tuple_702_703[1]].append(tuple_702_703[0])
                                        self.index_707[tuple_702_703[0]].append(tuple_702_703[1])
                                    # Program VectorAppend Region
                                    vec_654.append((var_702, var_703))
        # Program VectorClear Region
        del vec_699[:]
        vec_index699 = 0
        # Induction Fixpoint Loop Region
        while len(vec_654):
            # Program Call Region
            param_656_0 = [vec_654]
            ret = self.proc_151_(param_656_0)
            vec_654 = param_656_0[0]

        vec_index654 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_654[:]
        vec_index654 = 0
        # Program Return Region
        return False
        return False

    def proc_708_(self, var_709: int, var_710: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_732_(var_709, var_710)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_712_(self, var_713: int, var_714: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[(var_713, var_714)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_713_714 = (var_713, var_714)
            prev_state = self.table_15[tuple_713_714]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_713_714] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker::call_pred
                ret = self.proc_717_(var_714, var_713)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_713_714 = (var_713, var_714)
                    prev_state = self.table_15[tuple_713_714]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_713_714] = 1 | 4
                        if not present_bit:
                            self.index_711[tuple_713_714[0]].append(tuple_713_714[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_717_(self, var_718: int, var_719: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_30[(var_718, var_719)] & 3
        if state == 1:
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_144_(var_718)
            if not ret:
                # Program Return Region
                return True
            # Program TransitionState Region
            tuple_718_719 = (var_718, var_719)
            prev_state = self.table_30[tuple_718_719]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 1:
                self.table_30[tuple_718_719] = 0 | 4
        elif state == 2:
            # Program TransitionState Region
            tuple_718_719 = (var_718, var_719)
            prev_state = self.table_30[tuple_718_719]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_30[tuple_718_719] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_144_(var_718)
                if not ret:
                    # Program Call Region
                    ret = self.proc_725_(var_719, var_718)
                    if ret:
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_725_(self, var_726: int, var_727: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_730: List[int] = list()
        vec_index730: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_730: int
        scan_index_730: int = 0
        scan_tuple_730_vec: List[int] = self.index_729[var_726, var_727]
        while scan_index_730 < len(scan_tuple_730_vec):
            scan_tuple_730 = scan_tuple_730_vec[scan_index_730]
            scan_index_730 += 1
            vec_730.append(scan_tuple_730)
        # Program VectorLoop Region
        vec_index730 = 0
        while vec_index730 < len(vec_730):
            var_731 = vec_730[vec_index730]
            vec_index730 += 1
            # Program CheckState Region
            state = self.table_9[(var_726, var_727, var_731)] & 3
            if state == 1:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_732_(self, var_733: int, var_734: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_6[(var_733, var_734)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_733_734 = (var_733, var_734)
            prev_state = self.table_6[tuple_733_734]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_6[tuple_733_734] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_740_(var_733, var_734)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_733_734 = (var_733, var_734)
                    prev_state = self.table_6[tuple_733_734]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_6[tuple_733_734] = 1 | 4
                        if not present_bit:
                            self.index_287[tuple_733_734[1]].append(tuple_733_734[0])
                            self.index_707[tuple_733_734[0]].append(tuple_733_734[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_740_(self, var_741: int, var_742: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_744_(var_741, var_742)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_744_(self, var_745: int, var_746: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_748: List[int] = list()
        vec_index748: int = 0
        vec_750: List[int] = list()
        vec_index750: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_750: int
        scan_index_750: int = 0
        scan_tuple_750_vec: List[int] = self.index_749[var_746]
        while scan_index_750 < len(scan_tuple_750_vec):
            scan_tuple_750 = scan_tuple_750_vec[scan_index_750]
            scan_index_750 += 1
            vec_750.append(scan_tuple_750)
        # Program VectorLoop Region
        vec_index750 = 0
        while vec_index750 < len(vec_750):
            var_751 = vec_750[vec_index750]
            vec_index750 += 1
            # Program VectorAppend Region
            vec_748.append(var_751)
        # Program VectorUnique Region
        vec_748 = list(set(vec_748))
        vec_index748 = 0
        # Program TableJoin Region
        while vec_index748 < len(vec_748):
            var_753 = vec_748[vec_index748]
            vec_index748 += 1
            tuple_752_0_index: int = 0
            tuple_752_0_vec: List[int] = self.index_287[var_753]
            while tuple_752_0_index < len(tuple_752_0_vec):
                tuple_752_0 = tuple_752_0_vec[tuple_752_0_index]
                tuple_752_0_index += 1
                var_754 = tuple_752_0
                tuple_752_1_index: int = 0
                tuple_752_1_vec: List[int] = self.index_288[var_753]
                while tuple_752_1_index < len(tuple_752_1_vec):
                    tuple_752_1 = tuple_752_1_vec[tuple_752_1_index]
                    tuple_752_1_index += 1
                    var_755 = tuple_752_1
                    # Program TupleCompare Region
                    if (var_745, var_746, ) == (var_754, var_755, ):
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_291_(var_754, var_753)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_147_(var_753, var_755)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_748[:]
        vec_index748 = 0
        # Program Return Region
        return False
        return False

    def proc_759_(self, var_760: int, var_761: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_760_761 = (var_760, var_761)
        prev_state = self.table_6[tuple_760_761]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_6[tuple_760_761] = 0 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_740_(var_760, var_761)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_778_(self, var_779: int, var_780: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_782: List[int] = list()
        vec_index782: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_782: int
        scan_index_782: int = 0
        scan_tuple_782_vec: List[int] = self.index_287[var_779]
        while scan_index_782 < len(scan_tuple_782_vec):
            scan_tuple_782 = scan_tuple_782_vec[scan_index_782]
            scan_index_782 += 1
            vec_782.append(scan_tuple_782)
        # Program VectorLoop Region
        vec_index782 = 0
        while vec_index782 < len(vec_782):
            var_783 = vec_782[vec_index782]
            vec_index782 += 1
            # Program Call Region
            ret = self.proc_784_(var_779, var_783, var_780)

        # Program Return Region
        return False
        return False

    def proc_784_(self, var_785: int, var_786: int, var_787: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_786_787 = (var_786, var_787)
        prev_state = self.table_6[tuple_786_787]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_6[tuple_786_787] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_802_(var_786, var_787)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_759_(var_786, var_787)

        # Program Return Region
        return False
        return False

    def proc_802_(self, var_803: int, var_804: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_806: List[int] = list()
        vec_index806: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_806: int
        scan_index_806: int = 0
        scan_tuple_806_vec: List[int] = self.index_288[var_804]
        while scan_index_806 < len(scan_tuple_806_vec):
            scan_tuple_806 = scan_tuple_806_vec[scan_index_806]
            scan_index_806 += 1
            vec_806.append(scan_tuple_806)
        # Program VectorLoop Region
        vec_index806 = 0
        while vec_index806 < len(vec_806):
            var_807 = vec_806[vec_index806]
            vec_index806 += 1
            # Program Call Region
            ret = self.proc_784_(var_804, var_803, var_807)

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

    def function_instruction_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_707[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_708_(param_0, param_1):
                continue
            yield param_1

    def intraproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_711[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_712_(param_0, param_1):
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

    def interproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_715[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_20[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

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

    def get_instructions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_25:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_25[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def get_section_instructions_bf(self, param_0: bytes) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_716[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            full_tuple = (param_0, param_1)
            state = self.table_27[full_tuple] & 3
            if state != 1:
                continue;
            yield param_1

