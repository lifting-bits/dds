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

from dds.arch import ControlFlowEdgeKind, InstructionType

class Database:

    def __init__(self, log: DatabaseLog, functors: DatabaseFunctors):
        self._log: DatabaseLog = log
        self._functors: DatabaseFunctors = functors
        self._refs: DefaultDict[int, List[object]] = defaultdict(list)

        self.table_11: DefaultDict[Tuple[int, int, ControlFlowEdgeKind], int] = defaultdict(int)
        self.index_1372: DefaultDict[Tuple[int, ControlFlowEdgeKind], List[int]] = defaultdict(list)

        self.table_15: DefaultDict[int, int] = defaultdict(int)
        self.index_253 = self.table_15

        self.table_17: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_521: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_780: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_20: DefaultDict[Tuple[int, int, ControlFlowEdgeKind], int] = defaultdict(int)
        self.index_864: DefaultDict[Tuple[int, ControlFlowEdgeKind], List[int]] = defaultdict(list)
        self.index_956: DefaultDict[Tuple[int, int], List[ControlFlowEdgeKind]] = defaultdict(list)
        self.index_1381: DefaultDict[int, List[Tuple[int, ControlFlowEdgeKind]]] = defaultdict(list)

        self.table_24: DefaultDict[int, int] = defaultdict(int)
        self.index_433 = self.table_24

        self.table_26: DefaultDict[int, int] = defaultdict(int)

        self.table_28: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_774: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_31: DefaultDict[int, int] = defaultdict(int)

        self.table_33: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_784: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_36: DefaultDict[bytes, int] = defaultdict(int)

        self.table_38: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_423: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_41: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_338: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_44: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_327: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_47: DefaultDict[int, int] = defaultdict(int)
        self.index_415 = self.table_47

        self.table_49: DefaultDict[int, int] = defaultdict(int)
        self.index_560 = self.table_49

        self.table_51: DefaultDict[int, int] = defaultdict(int)
        self.index_225 = self.table_51

        self.table_53: DefaultDict[int, int] = defaultdict(int)
        self.index_212 = self.table_53

        self.table_55: DefaultDict[int, int] = defaultdict(int)
        self.index_194 = self.table_55

        self.table_57: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_199: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_60: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_254: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_852: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_63: DefaultDict[int, int] = defaultdict(int)
        self.index_174 = self.table_63

        self.table_65: DefaultDict[int, int] = defaultdict(int)
        self.index_160 = self.table_65

        self.table_67: DefaultDict[int, int] = defaultdict(int)
        self.index_159 = self.table_67

        self.table_69: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_522: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_815: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_72: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_179: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_75: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_229: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_78: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_269: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_81: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_300: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_84: DefaultDict[int, int] = defaultdict(int)
        self.index_189 = self.table_84

        self.table_86: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_230: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_89: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_295: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_92: DefaultDict[int, int] = defaultdict(int)
        self.index_184 = self.table_92

        self.table_94: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_236: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_97: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_290: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_100: DefaultDict[int, int] = defaultdict(int)
        self.index_178 = self.table_100

        self.table_102: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_242: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_105: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_285: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_108: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_626 = self.table_108

        self.table_111: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_627 = self.table_111

        self.table_114: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_248: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_117: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_280: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_120: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_309: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_123: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_310: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_126: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_275: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_129: DefaultDict[Tuple[ControlFlowEdgeKind, int, int], int] = defaultdict(int)
        self.index_211: DefaultDict[int, List[Tuple[ControlFlowEdgeKind, int]]] = defaultdict(list)

        self.table_133: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_365: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_997: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_136: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_385: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_139: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_400: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_142: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_414: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_967: DefaultDict[int, List[int]] = defaultdict(list)

        self.var_0: ControlFlowEdgeKind = ControlFlowEdgeKind.FUNCTION_CALL
        self.var_1: InstructionType = InstructionType.INDIRECT_JUMP
        self.var_2: ControlFlowEdgeKind = ControlFlowEdgeKind.JUMP_TAKEN
        self.var_3: InstructionType = InstructionType.CONDITIONAL_INDIRECT_JUMP
        self.var_4: InstructionType = InstructionType.INDIRECT_FUNCTION_CALL
        self.var_5: InstructionType = InstructionType.CONDITIONAL_INDIRECT_FUNCTION_CALL
        self.var_6: ControlFlowEdgeKind = ControlFlowEdgeKind.PC_THUNK_FUNCTION_CALL
        self.var_7: ControlFlowEdgeKind = ControlFlowEdgeKind.FUNCTION_CALL_RETURN
        self.var_8: ControlFlowEdgeKind = ControlFlowEdgeKind.FALL_THROUGH
        self.var_9: ControlFlowEdgeKind = ControlFlowEdgeKind.PSEUDO_FALL_THROUGH
        self.var_10: ControlFlowEdgeKind = ControlFlowEdgeKind.TAIL_FUNCTION_CALL
        self.init_145_()

    _HAS_MERGE_METHOD_insntype: Final[bool] = hasattr(InstructionType, 'merge_into')
    _MERGE_METHOD_insntype: Final[Callable[[InstructionType, InstructionType], None]] = getattr(InstructionType, 'merge_into', lambda a, b: None)

    def _resolve_insntype(self, obj: InstructionType) -> InstructionType:
        if Database._HAS_MERGE_METHOD_insntype:
            ref_list = self._refs[hash(obj)]
            for maybe_obj in ref_list:
                if obj is maybe_obj:
                    return obj
                elif obj == maybe_obj:
                    prior_obj: InstructionType = cast(InstructionType, maybe_obj)
                    Database._MERGE_METHOD_insntype(obj, prior_obj)
                    return prior_obj
            ref_list.append(obj)
        return obj

    _HAS_MERGE_METHOD_edgetype: Final[bool] = hasattr(ControlFlowEdgeKind, 'merge_into')
    _MERGE_METHOD_edgetype: Final[Callable[[ControlFlowEdgeKind, ControlFlowEdgeKind], None]] = getattr(ControlFlowEdgeKind, 'merge_into', lambda a, b: None)

    def _resolve_edgetype(self, obj: ControlFlowEdgeKind) -> ControlFlowEdgeKind:
        if Database._HAS_MERGE_METHOD_edgetype:
            ref_list = self._refs[hash(obj)]
            for maybe_obj in ref_list:
                if obj is maybe_obj:
                    return obj
                elif obj == maybe_obj:
                    prior_obj: ControlFlowEdgeKind = cast(ControlFlowEdgeKind, maybe_obj)
                    Database._MERGE_METHOD_edgetype(obj, prior_obj)
                    return prior_obj
            ref_list.append(obj)
        return obj

    def init_145_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False
        return False

    def section_3(self, vec_147: List[Tuple[bytes, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index147: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index147 = 0
        while vec_index147 < len(vec_147):
            var_148, var_149, var_150 = vec_147[vec_index147]
            vec_index147 += 1
            # Program TransitionState Region
            tuple_148 = var_148
            prev_state = self.table_36[tuple_148]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_148] = 1 | 4
                if not present_bit:
                    pass
        # Program Return Region
        return False
        return False

    def instruction_3(self, vec_152: List[Tuple[int, InstructionType, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index152: int = 0
        vec_156: List[int] = list()
        vec_index156: int = 0
        vec_167: List[int] = list()
        vec_index167: int = 0
        vec_168: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index168: int = 0
        vec_171: List[int] = list()
        vec_index171: int = 0
        vec_175: List[int] = list()
        vec_index175: int = 0
        vec_181: List[int] = list()
        vec_index181: int = 0
        vec_186: List[int] = list()
        vec_index186: int = 0
        vec_191: List[int] = list()
        vec_index191: int = 0
        vec_196: List[int] = list()
        vec_index196: int = 0
        vec_208: List[int] = list()
        vec_index208: int = 0
        vec_219: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index219: int = 0
        vec_222: List[int] = list()
        vec_index222: int = 0
        vec_226: List[int] = list()
        vec_index226: int = 0
        vec_233: List[int] = list()
        vec_index233: int = 0
        vec_239: List[int] = list()
        vec_index239: int = 0
        vec_245: List[int] = list()
        vec_index245: int = 0
        vec_250: List[int] = list()
        vec_index250: int = 0
        vec_266: List[int] = list()
        vec_index266: int = 0
        vec_272: List[int] = list()
        vec_index272: int = 0
        vec_277: List[int] = list()
        vec_index277: int = 0
        vec_282: List[int] = list()
        vec_index282: int = 0
        vec_287: List[int] = list()
        vec_index287: int = 0
        vec_292: List[int] = list()
        vec_index292: int = 0
        vec_297: List[int] = list()
        vec_index297: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index152 = 0
        while vec_index152 < len(vec_152):
            var_153, var_154, var_155 = vec_152[vec_index152]
            vec_index152 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_65[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_153] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_53[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_222.append(var_153)
                    # Program VectorAppend Region
                    vec_297.append(var_153)
                    # Program VectorAppend Region
                    vec_292.append(var_153)
                    # Program VectorAppend Region
                    vec_287.append(var_153)
                    # Program VectorAppend Region
                    vec_282.append(var_153)
                    # Program VectorAppend Region
                    vec_245.append(var_153)
                    # Program VectorAppend Region
                    vec_277.append(var_153)
                    # Program VectorAppend Region
                    vec_272.append(var_153)
                    # Program VectorAppend Region
                    vec_208.append(var_153)
                # Program VectorAppend Region
                vec_171.append(var_153)
                # Program VectorAppend Region
                vec_156.append(var_153)
            # Program TupleCompare Region
            if self.var_1 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_55[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_55[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_196.append(var_153)
                    # Program VectorAppend Region
                    vec_191.append(var_153)
            # Program TupleCompare Region
            if self.var_3 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_84[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_84[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_186.append(var_153)
            # Program TupleCompare Region
            if self.var_4 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_92[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_92[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_181.append(var_153)
            # Program TupleCompare Region
            if self.var_5 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_100[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_100[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_175.append(var_153)
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_31[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_31[tuple_153] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_65[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_153] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_53[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_222.append(var_153)
                    # Program VectorAppend Region
                    vec_297.append(var_153)
                    # Program VectorAppend Region
                    vec_292.append(var_153)
                    # Program VectorAppend Region
                    vec_287.append(var_153)
                    # Program VectorAppend Region
                    vec_282.append(var_153)
                    # Program VectorAppend Region
                    vec_245.append(var_153)
                    # Program VectorAppend Region
                    vec_277.append(var_153)
                    # Program VectorAppend Region
                    vec_272.append(var_153)
                    # Program VectorAppend Region
                    vec_208.append(var_153)
                # Program VectorAppend Region
                vec_171.append(var_153)
                # Program VectorAppend Region
                vec_156.append(var_153)
            # Program TupleCompare Region
            if self.var_1 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_55[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_55[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_196.append(var_153)
                    # Program VectorAppend Region
                    vec_191.append(var_153)
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_65[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_153] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_53[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_222.append(var_153)
                    # Program VectorAppend Region
                    vec_297.append(var_153)
                    # Program VectorAppend Region
                    vec_292.append(var_153)
                    # Program VectorAppend Region
                    vec_287.append(var_153)
                    # Program VectorAppend Region
                    vec_282.append(var_153)
                    # Program VectorAppend Region
                    vec_245.append(var_153)
                    # Program VectorAppend Region
                    vec_277.append(var_153)
                    # Program VectorAppend Region
                    vec_272.append(var_153)
                    # Program VectorAppend Region
                    vec_208.append(var_153)
                # Program VectorAppend Region
                vec_171.append(var_153)
                # Program VectorAppend Region
                vec_156.append(var_153)
            # Program TupleCompare Region
            if self.var_1 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_55[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_55[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_196.append(var_153)
                    # Program VectorAppend Region
                    vec_191.append(var_153)
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_65[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_153] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_53[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_222.append(var_153)
                    # Program VectorAppend Region
                    vec_297.append(var_153)
                    # Program VectorAppend Region
                    vec_292.append(var_153)
                    # Program VectorAppend Region
                    vec_287.append(var_153)
                    # Program VectorAppend Region
                    vec_282.append(var_153)
                    # Program VectorAppend Region
                    vec_245.append(var_153)
                    # Program VectorAppend Region
                    vec_277.append(var_153)
                    # Program VectorAppend Region
                    vec_272.append(var_153)
                    # Program VectorAppend Region
                    vec_208.append(var_153)
                # Program VectorAppend Region
                vec_171.append(var_153)
                # Program VectorAppend Region
                vec_156.append(var_153)
            # Program TupleCompare Region
            if self.var_1 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_55[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_55[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_196.append(var_153)
                    # Program VectorAppend Region
                    vec_191.append(var_153)
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_65[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_153] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_53[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_222.append(var_153)
                    # Program VectorAppend Region
                    vec_297.append(var_153)
                    # Program VectorAppend Region
                    vec_292.append(var_153)
                    # Program VectorAppend Region
                    vec_287.append(var_153)
                    # Program VectorAppend Region
                    vec_282.append(var_153)
                    # Program VectorAppend Region
                    vec_245.append(var_153)
                    # Program VectorAppend Region
                    vec_277.append(var_153)
                    # Program VectorAppend Region
                    vec_272.append(var_153)
                    # Program VectorAppend Region
                    vec_208.append(var_153)
                # Program VectorAppend Region
                vec_171.append(var_153)
                # Program VectorAppend Region
                vec_156.append(var_153)
            # Program TupleCompare Region
            if self.var_1 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_55[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_55[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_196.append(var_153)
                    # Program VectorAppend Region
                    vec_191.append(var_153)
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_65[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_153] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_53[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_222.append(var_153)
                    # Program VectorAppend Region
                    vec_297.append(var_153)
                    # Program VectorAppend Region
                    vec_292.append(var_153)
                    # Program VectorAppend Region
                    vec_287.append(var_153)
                    # Program VectorAppend Region
                    vec_282.append(var_153)
                    # Program VectorAppend Region
                    vec_245.append(var_153)
                    # Program VectorAppend Region
                    vec_277.append(var_153)
                    # Program VectorAppend Region
                    vec_272.append(var_153)
                    # Program VectorAppend Region
                    vec_208.append(var_153)
                # Program VectorAppend Region
                vec_171.append(var_153)
                # Program VectorAppend Region
                vec_156.append(var_153)
            # Program TupleCompare Region
            if self.var_1 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_55[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_55[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_196.append(var_153)
                    # Program VectorAppend Region
                    vec_191.append(var_153)
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_65[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_153] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_53[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_222.append(var_153)
                    # Program VectorAppend Region
                    vec_297.append(var_153)
                    # Program VectorAppend Region
                    vec_292.append(var_153)
                    # Program VectorAppend Region
                    vec_287.append(var_153)
                    # Program VectorAppend Region
                    vec_282.append(var_153)
                    # Program VectorAppend Region
                    vec_245.append(var_153)
                    # Program VectorAppend Region
                    vec_277.append(var_153)
                    # Program VectorAppend Region
                    vec_272.append(var_153)
                    # Program VectorAppend Region
                    vec_208.append(var_153)
                # Program VectorAppend Region
                vec_171.append(var_153)
                # Program VectorAppend Region
                vec_156.append(var_153)
            # Program TupleCompare Region
            if self.var_1 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_55[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_55[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_196.append(var_153)
                    # Program VectorAppend Region
                    vec_191.append(var_153)
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_65[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_153] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_53[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_222.append(var_153)
                    # Program VectorAppend Region
                    vec_297.append(var_153)
                    # Program VectorAppend Region
                    vec_292.append(var_153)
                    # Program VectorAppend Region
                    vec_287.append(var_153)
                    # Program VectorAppend Region
                    vec_282.append(var_153)
                    # Program VectorAppend Region
                    vec_245.append(var_153)
                    # Program VectorAppend Region
                    vec_277.append(var_153)
                    # Program VectorAppend Region
                    vec_272.append(var_153)
                    # Program VectorAppend Region
                    vec_208.append(var_153)
                # Program VectorAppend Region
                vec_171.append(var_153)
                # Program VectorAppend Region
                vec_156.append(var_153)
            # Program TupleCompare Region
            if self.var_1 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_55[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_55[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_196.append(var_153)
                    # Program VectorAppend Region
                    vec_191.append(var_153)
            # Program TransitionState Region
            tuple_153 = var_153
            prev_state = self.table_65[tuple_153]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_153] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_53[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_222.append(var_153)
                    # Program VectorAppend Region
                    vec_297.append(var_153)
                    # Program VectorAppend Region
                    vec_292.append(var_153)
                    # Program VectorAppend Region
                    vec_287.append(var_153)
                    # Program VectorAppend Region
                    vec_282.append(var_153)
                    # Program VectorAppend Region
                    vec_245.append(var_153)
                    # Program VectorAppend Region
                    vec_277.append(var_153)
                    # Program VectorAppend Region
                    vec_272.append(var_153)
                    # Program VectorAppend Region
                    vec_208.append(var_153)
                # Program VectorAppend Region
                vec_171.append(var_153)
                # Program VectorAppend Region
                vec_156.append(var_153)
            # Program TupleCompare Region
            if self.var_1 == var_154:
                # Program TransitionState Region
                tuple_153 = var_153
                prev_state = self.table_55[tuple_153]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_55[tuple_153] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_196.append(var_153)
                    # Program VectorAppend Region
                    vec_191.append(var_153)
        # Program VectorUnique Region
        vec_156 = list(set(vec_156))
        vec_index156 = 0
        # Program TableJoin Region
        while vec_index156 < len(vec_156):
            var_158 = vec_156[vec_index156]
            vec_index156 += 1
            if var_158 in self.index_159:
                if var_158 in self.index_160:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_158 = var_158
                    prev_state = self.table_15[tuple_158]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_158] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_167.append(var_158)
        # Program VectorClear Region
        del vec_156[:]
        vec_index156 = 0
        # Program VectorUnique Region
        vec_171 = list(set(vec_171))
        vec_index171 = 0
        # Program TableJoin Region
        while vec_index171 < len(vec_171):
            var_173 = vec_171[vec_index171]
            vec_index171 += 1
            if var_173 in self.index_174:
                if var_173 in self.index_160:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_173 = var_173
                    prev_state = self.table_15[tuple_173]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_173] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_167.append(var_173)
        # Program VectorClear Region
        del vec_171[:]
        vec_index171 = 0
        # Program VectorUnique Region
        vec_175 = list(set(vec_175))
        vec_index175 = 0
        # Program TableJoin Region
        while vec_index175 < len(vec_175):
            var_177 = vec_175[vec_index175]
            vec_index175 += 1
            if var_177 in self.index_178:
                tuple_176_1_index: int = 0
                tuple_176_1_vec: List[int] = self.index_179[var_177]
                while tuple_176_1_index < len(tuple_176_1_vec):
                    tuple_176_1 = tuple_176_1_vec[tuple_176_1_index]
                    tuple_176_1_index += 1
                    var_180 = tuple_176_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_177_180 = (var_177, var_180)
                    prev_state = self.table_102[tuple_177_180]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_102[tuple_177_180] = 1 | 4
                        if not present_bit:
                            self.index_242[tuple_177_180[1]].append(tuple_177_180[0])
                        # Program VectorAppend Region
                        vec_239.append(var_180)
        # Program VectorClear Region
        del vec_175[:]
        vec_index175 = 0
        # Program VectorUnique Region
        vec_181 = list(set(vec_181))
        vec_index181 = 0
        # Program TableJoin Region
        while vec_index181 < len(vec_181):
            var_183 = vec_181[vec_index181]
            vec_index181 += 1
            if var_183 in self.index_184:
                tuple_182_1_index: int = 0
                tuple_182_1_vec: List[int] = self.index_179[var_183]
                while tuple_182_1_index < len(tuple_182_1_vec):
                    tuple_182_1 = tuple_182_1_vec[tuple_182_1_index]
                    tuple_182_1_index += 1
                    var_185 = tuple_182_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_183_185 = (var_183, var_185)
                    prev_state = self.table_94[tuple_183_185]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_94[tuple_183_185] = 1 | 4
                        if not present_bit:
                            self.index_236[tuple_183_185[1]].append(tuple_183_185[0])
                        # Program VectorAppend Region
                        vec_233.append(var_185)
        # Program VectorClear Region
        del vec_181[:]
        vec_index181 = 0
        # Program VectorUnique Region
        vec_186 = list(set(vec_186))
        vec_index186 = 0
        # Program TableJoin Region
        while vec_index186 < len(vec_186):
            var_188 = vec_186[vec_index186]
            vec_index186 += 1
            if var_188 in self.index_189:
                tuple_187_1_index: int = 0
                tuple_187_1_vec: List[int] = self.index_179[var_188]
                while tuple_187_1_index < len(tuple_187_1_vec):
                    tuple_187_1 = tuple_187_1_vec[tuple_187_1_index]
                    tuple_187_1_index += 1
                    var_190 = tuple_187_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_188_190 = (var_188, var_190)
                    prev_state = self.table_86[tuple_188_190]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_86[tuple_188_190] = 1 | 4
                        if not present_bit:
                            self.index_230[tuple_188_190[1]].append(tuple_188_190[0])
                        # Program VectorAppend Region
                        vec_226.append(var_190)
        # Program VectorClear Region
        del vec_186[:]
        vec_index186 = 0
        # Program VectorUnique Region
        vec_191 = list(set(vec_191))
        vec_index191 = 0
        # Program TableJoin Region
        while vec_index191 < len(vec_191):
            var_193 = vec_191[vec_index191]
            vec_index191 += 1
            if var_193 in self.index_194:
                tuple_192_1_index: int = 0
                tuple_192_1_vec: List[int] = self.index_179[var_193]
                while tuple_192_1_index < len(tuple_192_1_vec):
                    tuple_192_1 = tuple_192_1_vec[tuple_192_1_index]
                    tuple_192_1_index += 1
                    var_195 = tuple_192_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_193_195 = (var_193, var_195)
                    prev_state = self.table_78[tuple_193_195]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_78[tuple_193_195] = 1 | 4
                        if not present_bit:
                            self.index_269[tuple_193_195[1]].append(tuple_193_195[0])
                        # Program VectorAppend Region
                        vec_266.append(var_195)
        # Program VectorClear Region
        del vec_191[:]
        vec_index191 = 0
        # Program VectorUnique Region
        vec_196 = list(set(vec_196))
        vec_index196 = 0
        # Program TableJoin Region
        while vec_index196 < len(vec_196):
            var_198 = vec_196[vec_index196]
            vec_index196 += 1
            if var_198 in self.index_194:
                tuple_197_1_index: int = 0
                tuple_197_1_vec: List[int] = self.index_199[var_198]
                while tuple_197_1_index < len(tuple_197_1_vec):
                    tuple_197_1 = tuple_197_1_vec[tuple_197_1_index]
                    tuple_197_1_index += 1
                    var_200 = tuple_197_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_201_(var_198)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_204_(var_198, var_200)
                        if ret:
                            # Program TransitionState Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                            tuple_198_200 = (var_198, var_200)
                            prev_state = self.table_60[tuple_198_200]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_60[tuple_198_200] = 1 | 4
                                if not present_bit:
                                    self.index_254[tuple_198_200[1]].append(tuple_198_200[0])
                                    self.index_852[tuple_198_200[0]].append(tuple_198_200[1])
                                # Program VectorAppend Region
                                vec_250.append(var_200)
        # Program VectorClear Region
        del vec_196[:]
        vec_index196 = 0
        # Program VectorUnique Region
        vec_208 = list(set(vec_208))
        vec_index208 = 0
        # Program TableJoin Region
        while vec_index208 < len(vec_208):
            var_210 = vec_208[vec_index208]
            vec_index208 += 1
            tuple_209_0_index: int = 0
            tuple_209_0_vec: List[Tuple[ControlFlowEdgeKind, int]] = self.index_211[var_210]
            while tuple_209_0_index < len(tuple_209_0_vec):
                tuple_209_0 = tuple_209_0_vec[tuple_209_0_index]
                tuple_209_0_index += 1
                var_213 = tuple_209_0[0]
                var_214 = tuple_209_0[1]
                if var_210 in self.index_212:
                    # Program TransitionState Region
                    var_213 = self._resolve_edgetype(var_213)
                    tuple_214_210_213 = (var_214, var_210, var_213)
                    prev_state = self.table_11[tuple_214_210_213]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_214_210_213] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_214_210_213[1], tuple_214_210_213[2])].append(tuple_214_210_213[0])
                        # Program VectorAppend Region
                        var_213 = self._resolve_edgetype(var_213)
                        vec_219.append((var_214, var_210, var_213))
        # Program VectorClear Region
        del vec_208[:]
        vec_index208 = 0
        # Program VectorUnique Region
        vec_222 = list(set(vec_222))
        vec_index222 = 0
        # Program TableJoin Region
        while vec_index222 < len(vec_222):
            var_224 = vec_222[vec_index222]
            vec_index222 += 1
            if var_224 in self.index_225:
                if var_224 in self.index_212:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_224 = var_224
                    prev_state = self.table_15[tuple_224]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_224] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_167.append(var_224)
        # Program VectorClear Region
        del vec_222[:]
        vec_index222 = 0
        # Program VectorUnique Region
        vec_226 = list(set(vec_226))
        vec_index226 = 0
        # Program TableJoin Region
        while vec_index226 < len(vec_226):
            var_228 = vec_226[vec_index226]
            vec_index226 += 1
            tuple_227_0_index: int = 0
            tuple_227_0_vec: List[int] = self.index_229[var_228]
            while tuple_227_0_index < len(tuple_227_0_vec):
                tuple_227_0 = tuple_227_0_vec[tuple_227_0_index]
                tuple_227_0_index += 1
                var_231 = tuple_227_0
                tuple_227_1_index: int = 0
                tuple_227_1_vec: List[int] = self.index_230[var_228]
                while tuple_227_1_index < len(tuple_227_1_vec):
                    tuple_227_1 = tuple_227_1_vec[tuple_227_1_index]
                    tuple_227_1_index += 1
                    var_232 = tuple_227_1
                    # Program TransitionState Region
                    tuple_231_232 = (var_231, var_232)
                    prev_state = self.table_89[tuple_231_232]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_89[tuple_231_232] = 1 | 4
                        if not present_bit:
                            self.index_295[tuple_231_232[0]].append(tuple_231_232[1])
                        # Program VectorAppend Region
                        vec_292.append(var_231)
        # Program VectorClear Region
        del vec_226[:]
        vec_index226 = 0
        # Program VectorUnique Region
        vec_233 = list(set(vec_233))
        vec_index233 = 0
        # Program TableJoin Region
        while vec_index233 < len(vec_233):
            var_235 = vec_233[vec_index233]
            vec_index233 += 1
            tuple_234_0_index: int = 0
            tuple_234_0_vec: List[int] = self.index_229[var_235]
            while tuple_234_0_index < len(tuple_234_0_vec):
                tuple_234_0 = tuple_234_0_vec[tuple_234_0_index]
                tuple_234_0_index += 1
                var_237 = tuple_234_0
                tuple_234_1_index: int = 0
                tuple_234_1_vec: List[int] = self.index_236[var_235]
                while tuple_234_1_index < len(tuple_234_1_vec):
                    tuple_234_1 = tuple_234_1_vec[tuple_234_1_index]
                    tuple_234_1_index += 1
                    var_238 = tuple_234_1
                    # Program TransitionState Region
                    tuple_237_238 = (var_237, var_238)
                    prev_state = self.table_97[tuple_237_238]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_237_238] = 1 | 4
                        if not present_bit:
                            self.index_290[tuple_237_238[0]].append(tuple_237_238[1])
                        # Program VectorAppend Region
                        vec_287.append(var_237)
        # Program VectorClear Region
        del vec_233[:]
        vec_index233 = 0
        # Program VectorUnique Region
        vec_239 = list(set(vec_239))
        vec_index239 = 0
        # Program TableJoin Region
        while vec_index239 < len(vec_239):
            var_241 = vec_239[vec_index239]
            vec_index239 += 1
            tuple_240_0_index: int = 0
            tuple_240_0_vec: List[int] = self.index_229[var_241]
            while tuple_240_0_index < len(tuple_240_0_vec):
                tuple_240_0 = tuple_240_0_vec[tuple_240_0_index]
                tuple_240_0_index += 1
                var_243 = tuple_240_0
                tuple_240_1_index: int = 0
                tuple_240_1_vec: List[int] = self.index_242[var_241]
                while tuple_240_1_index < len(tuple_240_1_vec):
                    tuple_240_1 = tuple_240_1_vec[tuple_240_1_index]
                    tuple_240_1_index += 1
                    var_244 = tuple_240_1
                    # Program TransitionState Region
                    tuple_243_244 = (var_243, var_244)
                    prev_state = self.table_105[tuple_243_244]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_243_244] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_243_244[0]].append(tuple_243_244[1])
                        # Program VectorAppend Region
                        vec_282.append(var_243)
        # Program VectorClear Region
        del vec_239[:]
        vec_index239 = 0
        # Program VectorUnique Region
        vec_245 = list(set(vec_245))
        vec_index245 = 0
        # Program TableJoin Region
        while vec_index245 < len(vec_245):
            var_247 = vec_245[vec_index245]
            vec_index245 += 1
            if var_247 in self.index_212:
                tuple_246_1_index: int = 0
                tuple_246_1_vec: List[int] = self.index_248[var_247]
                while tuple_246_1_index < len(tuple_246_1_vec):
                    tuple_246_1 = tuple_246_1_vec[tuple_246_1_index]
                    tuple_246_1_index += 1
                    var_249 = tuple_246_1
                    # Program TransitionState Region
                    tuple_249_247_6 = (var_249, var_247, self.var_6)
                    prev_state = self.table_11[tuple_249_247_6]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_249_247_6] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_249_247_6[1], tuple_249_247_6[2])].append(tuple_249_247_6[0])
                        # Program VectorAppend Region
                        vec_219.append((var_249, var_247, self.var_6))
        # Program VectorClear Region
        del vec_245[:]
        vec_index245 = 0
        # Program VectorUnique Region
        vec_250 = list(set(vec_250))
        vec_index250 = 0
        # Program TableJoin Region
        while vec_index250 < len(vec_250):
            var_252 = vec_250[vec_index250]
            vec_index250 += 1
            if var_252 in self.index_253:
                tuple_251_1_index: int = 0
                tuple_251_1_vec: List[int] = self.index_254[var_252]
                while tuple_251_1_index < len(tuple_251_1_vec):
                    tuple_251_1 = tuple_251_1_vec[tuple_251_1_index]
                    tuple_251_1_index += 1
                    var_255 = tuple_251_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_256_(var_252)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_259_(var_255, var_252)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_263_(var_255)
                            if not ret:
                                # Program TransitionState Region
                                tuple_255 = var_255
                                prev_state = self.table_15[tuple_255]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_255] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_167.append(var_255)
        # Program VectorClear Region
        del vec_250[:]
        vec_index250 = 0
        # Program VectorUnique Region
        vec_266 = list(set(vec_266))
        vec_index266 = 0
        # Program TableJoin Region
        while vec_index266 < len(vec_266):
            var_268 = vec_266[vec_index266]
            vec_index266 += 1
            tuple_267_0_index: int = 0
            tuple_267_0_vec: List[int] = self.index_229[var_268]
            while tuple_267_0_index < len(tuple_267_0_vec):
                tuple_267_0 = tuple_267_0_vec[tuple_267_0_index]
                tuple_267_0_index += 1
                var_270 = tuple_267_0
                tuple_267_1_index: int = 0
                tuple_267_1_vec: List[int] = self.index_269[var_268]
                while tuple_267_1_index < len(tuple_267_1_vec):
                    tuple_267_1 = tuple_267_1_vec[tuple_267_1_index]
                    tuple_267_1_index += 1
                    var_271 = tuple_267_1
                    # Program TransitionState Region
                    tuple_270_271 = (var_270, var_271)
                    prev_state = self.table_81[tuple_270_271]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_81[tuple_270_271] = 1 | 4
                        if not present_bit:
                            self.index_300[tuple_270_271[0]].append(tuple_270_271[1])
                        # Program VectorAppend Region
                        vec_297.append(var_270)
        # Program VectorClear Region
        del vec_266[:]
        vec_index266 = 0
        # Program VectorUnique Region
        vec_272 = list(set(vec_272))
        vec_index272 = 0
        # Program TableJoin Region
        while vec_index272 < len(vec_272):
            var_274 = vec_272[vec_index272]
            vec_index272 += 1
            if var_274 in self.index_212:
                tuple_273_1_index: int = 0
                tuple_273_1_vec: List[int] = self.index_275[var_274]
                while tuple_273_1_index < len(tuple_273_1_vec):
                    tuple_273_1 = tuple_273_1_vec[tuple_273_1_index]
                    tuple_273_1_index += 1
                    var_276 = tuple_273_1
                    # Program TransitionState Region
                    tuple_276_274_7 = (var_276, var_274, self.var_7)
                    prev_state = self.table_11[tuple_276_274_7]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_276_274_7] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_276_274_7[1], tuple_276_274_7[2])].append(tuple_276_274_7[0])
                        # Program VectorAppend Region
                        vec_219.append((var_276, var_274, self.var_7))
        # Program VectorClear Region
        del vec_272[:]
        vec_index272 = 0
        # Program VectorUnique Region
        vec_277 = list(set(vec_277))
        vec_index277 = 0
        # Program TableJoin Region
        while vec_index277 < len(vec_277):
            var_279 = vec_277[vec_index277]
            vec_index277 += 1
            if var_279 in self.index_212:
                tuple_278_1_index: int = 0
                tuple_278_1_vec: List[int] = self.index_280[var_279]
                while tuple_278_1_index < len(tuple_278_1_vec):
                    tuple_278_1 = tuple_278_1_vec[tuple_278_1_index]
                    tuple_278_1_index += 1
                    var_281 = tuple_278_1
                    # Program TransitionState Region
                    tuple_281_279_0 = (var_281, var_279, self.var_0)
                    prev_state = self.table_11[tuple_281_279_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_281_279_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_281_279_0[1], tuple_281_279_0[2])].append(tuple_281_279_0[0])
                        # Program VectorAppend Region
                        vec_219.append((var_281, var_279, self.var_0))
        # Program VectorClear Region
        del vec_277[:]
        vec_index277 = 0
        # Program VectorUnique Region
        vec_282 = list(set(vec_282))
        vec_index282 = 0
        # Program TableJoin Region
        while vec_index282 < len(vec_282):
            var_284 = vec_282[vec_index282]
            vec_index282 += 1
            if var_284 in self.index_212:
                tuple_283_1_index: int = 0
                tuple_283_1_vec: List[int] = self.index_285[var_284]
                while tuple_283_1_index < len(tuple_283_1_vec):
                    tuple_283_1 = tuple_283_1_vec[tuple_283_1_index]
                    tuple_283_1_index += 1
                    var_286 = tuple_283_1
                    # Program TransitionState Region
                    tuple_286_284_0 = (var_286, var_284, self.var_0)
                    prev_state = self.table_11[tuple_286_284_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_286_284_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_286_284_0[1], tuple_286_284_0[2])].append(tuple_286_284_0[0])
                        # Program VectorAppend Region
                        vec_219.append((var_286, var_284, self.var_0))
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
            if var_289 in self.index_212:
                tuple_288_1_index: int = 0
                tuple_288_1_vec: List[int] = self.index_290[var_289]
                while tuple_288_1_index < len(tuple_288_1_vec):
                    tuple_288_1 = tuple_288_1_vec[tuple_288_1_index]
                    tuple_288_1_index += 1
                    var_291 = tuple_288_1
                    # Program TransitionState Region
                    tuple_291_289_0 = (var_291, var_289, self.var_0)
                    prev_state = self.table_11[tuple_291_289_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_291_289_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_291_289_0[1], tuple_291_289_0[2])].append(tuple_291_289_0[0])
                        # Program VectorAppend Region
                        vec_219.append((var_291, var_289, self.var_0))
        # Program VectorClear Region
        del vec_287[:]
        vec_index287 = 0
        # Program VectorUnique Region
        vec_292 = list(set(vec_292))
        vec_index292 = 0
        # Program TableJoin Region
        while vec_index292 < len(vec_292):
            var_294 = vec_292[vec_index292]
            vec_index292 += 1
            if var_294 in self.index_212:
                tuple_293_1_index: int = 0
                tuple_293_1_vec: List[int] = self.index_295[var_294]
                while tuple_293_1_index < len(tuple_293_1_vec):
                    tuple_293_1 = tuple_293_1_vec[tuple_293_1_index]
                    tuple_293_1_index += 1
                    var_296 = tuple_293_1
                    # Program TransitionState Region
                    tuple_296_294_2 = (var_296, var_294, self.var_2)
                    prev_state = self.table_11[tuple_296_294_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_296_294_2] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_296_294_2[1], tuple_296_294_2[2])].append(tuple_296_294_2[0])
                        # Program VectorAppend Region
                        vec_219.append((var_296, var_294, self.var_2))
        # Program VectorClear Region
        del vec_292[:]
        vec_index292 = 0
        # Program VectorUnique Region
        vec_297 = list(set(vec_297))
        vec_index297 = 0
        # Program TableJoin Region
        while vec_index297 < len(vec_297):
            var_299 = vec_297[vec_index297]
            vec_index297 += 1
            if var_299 in self.index_212:
                tuple_298_1_index: int = 0
                tuple_298_1_vec: List[int] = self.index_300[var_299]
                while tuple_298_1_index < len(tuple_298_1_vec):
                    tuple_298_1 = tuple_298_1_vec[tuple_298_1_index]
                    tuple_298_1_index += 1
                    var_301 = tuple_298_1
                    # Program TransitionState Region
                    tuple_301_299_2 = (var_301, var_299, self.var_2)
                    prev_state = self.table_11[tuple_301_299_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_301_299_2] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_301_299_2[1], tuple_301_299_2[2])].append(tuple_301_299_2[0])
                        # Program VectorAppend Region
                        vec_219.append((var_301, var_299, self.var_2))
        # Program VectorClear Region
        del vec_297[:]
        vec_index297 = 0
        # Induction Fixpoint Loop Region
        while len(vec_219) or len(vec_167) or len(vec_168):
            # Program Series Region
            # Program Call Region
            ret = self.proc_164_(vec_167, vec_168)

            # Program Call Region
            param_170_0 = [vec_167]
            param_170_1 = [vec_168]
            ret = self.proc_161_(param_170_0, param_170_1)
            vec_167 = param_170_0[0]
            vec_168 = param_170_1[0]

            # Program Call Region
            ret = self.proc_217_(vec_219)

            # Program Call Region
            param_221_0 = [vec_219]
            ret = self.proc_215_(param_221_0)
            vec_219 = param_221_0[0]

        vec_index219 = 0
        vec_index167 = 0
        vec_index168 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_167[:]
        vec_index167 = 0
        # Program VectorClear Region
        del vec_168[:]
        vec_index168 = 0
        # Program VectorClear Region
        del vec_219[:]
        vec_index219 = 0
        # Program Return Region
        return False
        return False

    def proc_161_(self, param_0: List[List[int]], param_1: List[List[Tuple[int, int, ControlFlowEdgeKind]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_162 = param_0[0]
        vec_163 = param_1[0]
        vec_index162: int = 0
        vec_index163: int = 0
        vec_321: List[int] = list()
        vec_index321: int = 0
        vec_322: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index322: int = 0
        vec_328: List[int] = list()
        vec_index328: int = 0
        vec_339: List[int] = list()
        vec_index339: int = 0
        vec_349: List[int] = list()
        vec_index349: int = 0
        vec_355: List[int] = list()
        vec_index355: int = 0
        vec_362: List[int] = list()
        vec_index362: int = 0
        vec_379: List[int] = list()
        vec_index379: int = 0
        vec_382: List[int] = list()
        vec_index382: int = 0
        vec_397: List[int] = list()
        vec_index397: int = 0
        vec_411: List[int] = list()
        vec_index411: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorSwap Region
        vec_162, vec_321 = vec_321, vec_162
        # Program VectorSwap Region
        vec_163, vec_322 = vec_322, vec_163
        # Program Parallel Region
        # Program VectorLoop Region
        while vec_index321 < len(vec_321):
            var_323 = vec_321[vec_index321]
            vec_index321 += 1
            # Program Series Region
            # Program Parallel Region
            # Program Series Region
            # Program TableScan Region
            scan_tuple_328: int
            scan_index_328: int = 0
            scan_tuple_328_vec: List[int] = self.index_327[var_323]
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
                tuple_323_329 = (var_323, var_329)
                prev_state = self.table_44[tuple_323_329]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 1:
                    self.table_44[tuple_323_329] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    ret = self.proc_330_(var_323, var_329)

                    # Program Call Region
                    ret = self.proc_334_(var_323, var_329)

            # Program Series Region
            # Program TableScan Region
            scan_tuple_339: int
            scan_index_339: int = 0
            scan_tuple_339_vec: List[int] = self.index_338[var_323]
            while scan_index_339 < len(scan_tuple_339_vec):
                scan_tuple_339 = scan_tuple_339_vec[scan_index_339]
                scan_index_339 += 1
                vec_339.append(scan_tuple_339)
            # Program VectorLoop Region
            vec_index339 = 0
            while vec_index339 < len(vec_339):
                var_340 = vec_339[vec_index339]
                vec_index339 += 1
                # Program TransitionState Region
                # Remove from negated view
                tuple_323_340 = (var_323, var_340)
                prev_state = self.table_41[tuple_323_340]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 1:
                    self.table_41[tuple_323_340] = 0 | 4
                    # Program Call Region
                    ret = self.proc_341_(var_323, var_340)

            # Program Parallel Region
            # Program VectorAppend Region
            vec_355.append(var_323)
            # Program VectorAppend Region
            vec_362.append(var_323)
            # Program VectorAppend Region
            vec_382.append(var_323)
            # Program VectorAppend Region
            vec_397.append(var_323)
        # Program VectorLoop Region
        while vec_index322 < len(vec_322):
            var_324, var_325, var_326 = vec_322[vec_index322]
            vec_index322 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_2 == var_326:
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                ret = self.proc_204_(var_324, var_325)
                if not ret:
                    # Program TransitionState Region
                    tuple_324_325 = (var_324, var_325)
                    prev_state = self.table_57[tuple_324_325]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_57[tuple_324_325] = 1 | 4
                        if not present_bit:
                            self.index_199[tuple_324_325[0]].append(tuple_324_325[1])
                        # Program VectorAppend Region
                        vec_349.append(var_324)
            # Program TupleCompare Region
            if self.var_0 == var_326:
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                ret = self.proc_346_(var_325)
                if not ret:
                    # Program TransitionState Region
                    tuple_325 = var_325
                    prev_state = self.table_15[tuple_325]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_325] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_162.append(var_325)
        # Program VectorUnique Region
        vec_349 = list(set(vec_349))
        vec_index349 = 0
        # Program TableJoin Region
        while vec_index349 < len(vec_349):
            var_351 = vec_349[vec_index349]
            vec_index349 += 1
            if var_351 in self.index_194:
                tuple_350_1_index: int = 0
                tuple_350_1_vec: List[int] = self.index_199[var_351]
                while tuple_350_1_index < len(tuple_350_1_vec):
                    tuple_350_1 = tuple_350_1_vec[tuple_350_1_index]
                    tuple_350_1_index += 1
                    var_352 = tuple_350_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_201_(var_351)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_204_(var_351, var_352)
                        if ret:
                            # Program TransitionState Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                            tuple_351_352 = (var_351, var_352)
                            prev_state = self.table_60[tuple_351_352]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_60[tuple_351_352] = 1 | 4
                                if not present_bit:
                                    self.index_254[tuple_351_352[1]].append(tuple_351_352[0])
                                    self.index_852[tuple_351_352[0]].append(tuple_351_352[1])
                                # Program VectorAppend Region
                                vec_355.append(var_352)
        # Program VectorClear Region
        del vec_349[:]
        vec_index349 = 0
        # Program VectorUnique Region
        vec_355 = list(set(vec_355))
        vec_index355 = 0
        # Program TableJoin Region
        while vec_index355 < len(vec_355):
            var_357 = vec_355[vec_index355]
            vec_index355 += 1
            if var_357 in self.index_253:
                tuple_356_1_index: int = 0
                tuple_356_1_vec: List[int] = self.index_254[var_357]
                while tuple_356_1_index < len(tuple_356_1_vec):
                    tuple_356_1 = tuple_356_1_vec[tuple_356_1_index]
                    tuple_356_1_index += 1
                    var_358 = tuple_356_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_256_(var_357)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_259_(var_358, var_357)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_263_(var_358)
                            if not ret:
                                # Program TransitionState Region
                                tuple_358 = var_358
                                prev_state = self.table_15[tuple_358]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_358] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_162.append(var_358)
        # Program VectorClear Region
        del vec_355[:]
        vec_index355 = 0
        # Program VectorUnique Region
        vec_362 = list(set(vec_362))
        vec_index362 = 0
        # Program TableJoin Region
        while vec_index362 < len(vec_362):
            var_364 = vec_362[vec_index362]
            vec_index362 += 1
            tuple_363_0_index: int = 0
            tuple_363_0_vec: List[int] = self.index_365[var_364]
            while tuple_363_0_index < len(tuple_363_0_vec):
                tuple_363_0 = tuple_363_0_vec[tuple_363_0_index]
                tuple_363_0_index += 1
                var_366 = tuple_363_0
                if var_364 in self.index_253:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_367_(var_366, var_364)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_256_(var_364)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_372_(var_366)
                            if not ret:
                                # Program TransitionState Region
                                tuple_366 = var_366
                                prev_state = self.table_24[tuple_366]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_24[tuple_366] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_379.append(var_366)
        # Program VectorClear Region
        del vec_362[:]
        vec_index362 = 0
        # Program VectorUnique Region
        vec_382 = list(set(vec_382))
        vec_index382 = 0
        # Program TableJoin Region
        while vec_index382 < len(vec_382):
            var_384 = vec_382[vec_index382]
            vec_index382 += 1
            tuple_383_0_index: int = 0
            tuple_383_0_vec: List[int] = self.index_385[var_384]
            while tuple_383_0_index < len(tuple_383_0_vec):
                tuple_383_0 = tuple_383_0_vec[tuple_383_0_index]
                tuple_383_0_index += 1
                var_386 = tuple_383_0
                if var_384 in self.index_253:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_387_(var_386, var_384)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_256_(var_384)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_392_(var_386, var_384, self.var_10)
                            if not ret:
                                # Program TransitionState Region
                                tuple_386_384_10 = (var_386, var_384, self.var_10)
                                prev_state = self.table_20[tuple_386_384_10]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_20[tuple_386_384_10] = 1 | 4
                                    if not present_bit:
                                        self.index_864[(tuple_386_384_10[1], tuple_386_384_10[2])].append(tuple_386_384_10[0])
                                        self.index_956[(tuple_386_384_10[0], tuple_386_384_10[1])].append(tuple_386_384_10[2])
                                        self.index_1381[tuple_386_384_10[1]].append((tuple_386_384_10[0], tuple_386_384_10[2]))
                                    # Program VectorAppend Region
                                    vec_163.append((var_386, var_384, self.var_10))
        # Program VectorClear Region
        del vec_382[:]
        vec_index382 = 0
        # Program VectorUnique Region
        vec_397 = list(set(vec_397))
        vec_index397 = 0
        # Program TableJoin Region
        while vec_index397 < len(vec_397):
            var_399 = vec_397[vec_index397]
            vec_index397 += 1
            tuple_398_0_index: int = 0
            tuple_398_0_vec: List[int] = self.index_400[var_399]
            while tuple_398_0_index < len(tuple_398_0_vec):
                tuple_398_0 = tuple_398_0_vec[tuple_398_0_index]
                tuple_398_0_index += 1
                var_401 = tuple_398_0
                if var_399 in self.index_253:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_402_(var_401, var_399)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_256_(var_399)
                        if ret:
                            # Program Parallel Region
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_407_(var_401, var_399)
                            if not ret:
                                # Program TransitionState Region
                                tuple_401_399 = (var_401, var_399)
                                prev_state = self.table_142[tuple_401_399]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_142[tuple_401_399] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_401_399[1]].append(tuple_401_399[0])
                                        self.index_967[tuple_401_399[0]].append(tuple_401_399[1])
                                    # Program VectorAppend Region
                                    vec_411.append(var_399)
                            # Program TransitionState Region
                            tuple_401_399 = (var_401, var_399)
                            prev_state = self.table_33[tuple_401_399]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_33[tuple_401_399] = 1 | 4
                                if not present_bit:
                                    self.index_784[tuple_401_399[0]].append(tuple_401_399[1])
        # Program VectorClear Region
        del vec_397[:]
        vec_index397 = 0
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
                if var_413 in self.index_415:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_407_(var_416, var_413)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_418_(var_413)
                        if ret:
                            # Program TransitionState Region
                            tuple_416 = var_416
                            prev_state = self.table_26[tuple_416]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_26[tuple_416] = 1 | 4
                                if not present_bit:
                                    pass
        # Program VectorClear Region
        del vec_411[:]
        vec_index411 = 0
        # Induction Fixpoint Loop Region
        while len(vec_379):
            # Program Call Region
            param_381_0 = [vec_379]
            ret = self.proc_375_(param_381_0)
            vec_379 = param_381_0[0]

        vec_index379 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_379[:]
        vec_index379 = 0
        # Program Return Region
        param_0[0] = vec_162
        param_1[0] = vec_163
        return False
        return False

    def proc_164_(self, vec_165: List[int], vec_166: List[Tuple[int, int, ControlFlowEdgeKind]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index165: int = 0
        vec_index166: int = 0
        vec_483: List[Tuple[int, int]] = list()
        vec_index483: int = 0
        vec_494: List[int] = list()
        vec_index494: int = 0
        vec_501: List[int] = list()
        vec_index501: int = 0
        vec_504: List[int] = list()
        vec_index504: int = 0
        vec_511: List[int] = list()
        vec_index511: int = 0
        vec_518: List[int] = list()
        vec_index518: int = 0
        vec_534: List[int] = list()
        vec_index534: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program Parallel Region
        # Program VectorLoop Region
        while vec_index165 < len(vec_165):
            var_471 = vec_165[vec_index165]
            vec_index165 += 1
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
            ret = self.proc_475_(var_471, var_471)
            if not ret:
                # Program TransitionState Region
                tuple_471_471 = (var_471, var_471)
                prev_state = self.table_17[tuple_471_471]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_17[tuple_471_471] = 1 | 4
                    if not present_bit:
                        self.index_521[tuple_471_471[1]].append(tuple_471_471[0])
                        self.index_780[tuple_471_471[0]].append(tuple_471_471[1])
                    # Program VectorAppend Region
                    vec_483.append((var_471, var_471))
        # Program VectorLoop Region
        while vec_index166 < len(vec_166):
            var_472, var_473, var_474 = vec_166[vec_index166]
            vec_index166 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_8 == var_474:
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                ret = self.proc_367_(var_472, var_473)
                if not ret:
                    # Program TransitionState Region
                    tuple_472_473 = (var_472, var_473)
                    prev_state = self.table_133[tuple_472_473]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_133[tuple_472_473] = 1 | 4
                        if not present_bit:
                            self.index_365[tuple_472_473[1]].append(tuple_472_473[0])
                            self.index_997[tuple_472_473[0]].append(tuple_472_473[1])
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_504.append(var_473)
                        # Program VectorAppend Region
                        vec_494.append(var_473)
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
            ret = self.proc_402_(var_472, var_473)
            if not ret:
                # Program TransitionState Region
                tuple_472_473 = (var_472, var_473)
                prev_state = self.table_139[tuple_472_473]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_139[tuple_472_473] = 1 | 4
                    if not present_bit:
                        self.index_400[tuple_472_473[1]].append(tuple_472_473[0])
                    # Program VectorAppend Region
                    vec_511.append(var_473)
            # Program Series Region
            # Program TransitionState Region
            # Eager insert before negation to prevent race
            tuple_473_472 = (var_473, var_472)
            prev_state = self.table_44[tuple_473_472]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0:
                self.table_44[tuple_473_472] = 2 | 4
                if not present_bit:
                    self.index_327[tuple_473_472[0]].append(tuple_473_472[1])
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_256_(var_473)
            if not ret:
                # Program TransitionState Region
                tuple_473_472 = (var_473, var_472)
                prev_state = self.table_44[tuple_473_472]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_44[tuple_473_472] = 1 | 4
                    if not present_bit:
                        self.index_327[tuple_473_472[0]].append(tuple_473_472[1])
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                    ret = self.proc_490_(var_472, var_473)
                    if not ret:
                        # Program TransitionState Region
                        tuple_472_473 = (var_472, var_473)
                        prev_state = self.table_69[tuple_472_473]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_69[tuple_472_473] = 1 | 4
                            if not present_bit:
                                self.index_522[tuple_472_473[0]].append(tuple_472_473[1])
                                self.index_815[tuple_472_473[1]].append(tuple_472_473[0])
                            # Program VectorAppend Region
                            vec_518.append(var_472)
                    # Program TransitionState Region
                    tuple_472_473 = (var_472, var_473)
                    prev_state = self.table_28[tuple_472_473]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_28[tuple_472_473] = 1 | 4
                        if not present_bit:
                            self.index_774[tuple_472_473[0]].append(tuple_472_473[1])
        # Program VectorUnique Region
        vec_494 = list(set(vec_494))
        vec_index494 = 0
        # Program TableJoin Region
        while vec_index494 < len(vec_494):
            var_496 = vec_494[vec_index494]
            vec_index494 += 1
            tuple_495_0_index: int = 0
            tuple_495_0_vec: List[int] = self.index_365[var_496]
            while tuple_495_0_index < len(tuple_495_0_vec):
                tuple_495_0 = tuple_495_0_vec[tuple_495_0_index]
                tuple_495_0_index += 1
                var_497 = tuple_495_0
                if var_496 in self.index_433:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_367_(var_497, var_496)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_436_(var_496)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_439_(var_497)
                            if not ret:
                                # Program TransitionState Region
                                tuple_497 = var_497
                                prev_state = self.table_24[tuple_497]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_24[tuple_497] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_501.append(var_497)
        # Program VectorClear Region
        del vec_494[:]
        vec_index494 = 0
        # Program VectorUnique Region
        vec_504 = list(set(vec_504))
        vec_index504 = 0
        # Program TableJoin Region
        while vec_index504 < len(vec_504):
            var_506 = vec_504[vec_index504]
            vec_index504 += 1
            tuple_505_0_index: int = 0
            tuple_505_0_vec: List[int] = self.index_365[var_506]
            while tuple_505_0_index < len(tuple_505_0_vec):
                tuple_505_0 = tuple_505_0_vec[tuple_505_0_index]
                tuple_505_0_index += 1
                var_507 = tuple_505_0
                if var_506 in self.index_253:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_367_(var_507, var_506)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_256_(var_506)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_372_(var_507)
                            if not ret:
                                # Program TransitionState Region
                                tuple_507 = var_507
                                prev_state = self.table_24[tuple_507]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_24[tuple_507] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_501.append(var_507)
        # Program VectorClear Region
        del vec_504[:]
        vec_index504 = 0
        # Program VectorUnique Region
        vec_511 = list(set(vec_511))
        vec_index511 = 0
        # Program TableJoin Region
        while vec_index511 < len(vec_511):
            var_513 = vec_511[vec_index511]
            vec_index511 += 1
            tuple_512_0_index: int = 0
            tuple_512_0_vec: List[int] = self.index_400[var_513]
            while tuple_512_0_index < len(tuple_512_0_vec):
                tuple_512_0 = tuple_512_0_vec[tuple_512_0_index]
                tuple_512_0_index += 1
                var_514 = tuple_512_0
                if var_513 in self.index_253:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_402_(var_514, var_513)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_256_(var_513)
                        if ret:
                            # Program Parallel Region
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_407_(var_514, var_513)
                            if not ret:
                                # Program TransitionState Region
                                tuple_514_513 = (var_514, var_513)
                                prev_state = self.table_142[tuple_514_513]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_142[tuple_514_513] = 1 | 4
                                    if not present_bit:
                                        self.index_414[tuple_514_513[1]].append(tuple_514_513[0])
                                        self.index_967[tuple_514_513[0]].append(tuple_514_513[1])
                                    # Program VectorAppend Region
                                    vec_534.append(var_513)
                            # Program TransitionState Region
                            tuple_514_513 = (var_514, var_513)
                            prev_state = self.table_33[tuple_514_513]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_33[tuple_514_513] = 1 | 4
                                if not present_bit:
                                    self.index_784[tuple_514_513[0]].append(tuple_514_513[1])
        # Program VectorClear Region
        del vec_511[:]
        vec_index511 = 0
        # Program VectorUnique Region
        vec_518 = list(set(vec_518))
        vec_index518 = 0
        # Program TableJoin Region
        while vec_index518 < len(vec_518):
            var_520 = vec_518[vec_index518]
            vec_index518 += 1
            tuple_519_0_index: int = 0
            tuple_519_0_vec: List[int] = self.index_521[var_520]
            while tuple_519_0_index < len(tuple_519_0_vec):
                tuple_519_0 = tuple_519_0_vec[tuple_519_0_index]
                tuple_519_0_index += 1
                var_523 = tuple_519_0
                tuple_519_1_index: int = 0
                tuple_519_1_vec: List[int] = self.index_522[var_520]
                while tuple_519_1_index < len(tuple_519_1_vec):
                    tuple_519_1 = tuple_519_1_vec[tuple_519_1_index]
                    tuple_519_1_index += 1
                    var_524 = tuple_519_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_525_(var_523, var_520)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_490_(var_520, var_524)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_530_(var_523, var_524)
                            if not ret:
                                # Program TransitionState Region
                                tuple_523_524 = (var_523, var_524)
                                prev_state = self.table_17[tuple_523_524]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_523_524] = 1 | 4
                                    if not present_bit:
                                        self.index_521[tuple_523_524[1]].append(tuple_523_524[0])
                                        self.index_780[tuple_523_524[0]].append(tuple_523_524[1])
                                    # Program VectorAppend Region
                                    vec_483.append((var_523, var_524))
        # Program VectorClear Region
        del vec_518[:]
        vec_index518 = 0
        # Program VectorUnique Region
        vec_534 = list(set(vec_534))
        vec_index534 = 0
        # Program TableJoin Region
        while vec_index534 < len(vec_534):
            var_536 = vec_534[vec_index534]
            vec_index534 += 1
            tuple_535_0_index: int = 0
            tuple_535_0_vec: List[int] = self.index_414[var_536]
            while tuple_535_0_index < len(tuple_535_0_vec):
                tuple_535_0 = tuple_535_0_vec[tuple_535_0_index]
                tuple_535_0_index += 1
                var_537 = tuple_535_0
                if var_536 in self.index_415:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_407_(var_537, var_536)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_418_(var_536)
                        if ret:
                            # Program TransitionState Region
                            tuple_537 = var_537
                            prev_state = self.table_26[tuple_537]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_26[tuple_537] = 1 | 4
                                if not present_bit:
                                    pass
        # Program VectorClear Region
        del vec_534[:]
        vec_index534 = 0
        # Induction Fixpoint Loop Region
        while len(vec_501) or len(vec_483):
            # Program Series Region
            # Program Call Region
            param_485_0 = [vec_483]
            ret = self.proc_479_(param_485_0)
            vec_483 = param_485_0[0]

            # Program Call Region
            param_503_0 = [vec_501]
            ret = self.proc_375_(param_503_0)
            vec_501 = param_503_0[0]

        vec_index501 = 0
        vec_index483 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_483[:]
        vec_index483 = 0
        # Program VectorClear Region
        del vec_501[:]
        vec_index501 = 0
        # Program Return Region
        return False
        return False

    def proc_201_(self, var_202: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_55[var_202] & 3
        if state == 1:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_204_(self, var_205: int, var_206: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_57[(var_205, var_206)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_205_206 = (var_205, var_206)
            prev_state = self.table_57[tuple_205_206]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_57[tuple_205_206] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1076_(self.var_2, var_205, var_206)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_205_206 = (var_205, var_206)
                    prev_state = self.table_57[tuple_205_206]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_57[tuple_205_206] = 1 | 4
                        if not present_bit:
                            self.index_199[tuple_205_206[0]].append(tuple_205_206[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_215_(self, param_0: List[List[Tuple[int, int, ControlFlowEdgeKind]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_216 = param_0[0]
        vec_index216: int = 0
        vec_302: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index302: int = 0
        vec_306: List[int] = list()
        vec_index306: int = 0
        vec_313: List[int] = list()
        vec_index313: int = 0
        vec_317: List[int] = list()
        vec_index317: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_216, vec_302 = vec_302, vec_216
        # Program VectorLoop Region
        while vec_index302 < len(vec_302):
            var_303, var_304, var_305 = vec_302[vec_index302]
            vec_index302 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_7 == var_305:
                # Program TransitionState Region
                tuple_303_304 = (var_303, var_304)
                prev_state = self.table_123[tuple_303_304]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_123[tuple_303_304] = 1 | 4
                    if not present_bit:
                        self.index_310[tuple_303_304[0]].append(tuple_303_304[1])
                    # Program VectorAppend Region
                    vec_306.append(var_303)
            # Program TupleCompare Region
            if self.var_0 == var_305:
                # Program TransitionState Region
                tuple_303_304 = (var_303, var_304)
                prev_state = self.table_120[tuple_303_304]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_120[tuple_303_304] = 1 | 4
                    if not present_bit:
                        self.index_309[tuple_303_304[0]].append(tuple_303_304[1])
                    # Program VectorAppend Region
                    vec_306.append(var_303)
        # Program VectorUnique Region
        vec_306 = list(set(vec_306))
        vec_index306 = 0
        # Program TableJoin Region
        while vec_index306 < len(vec_306):
            var_308 = vec_306[vec_index306]
            vec_index306 += 1
            tuple_307_0_index: int = 0
            tuple_307_0_vec: List[int] = self.index_309[var_308]
            while tuple_307_0_index < len(tuple_307_0_vec):
                tuple_307_0 = tuple_307_0_vec[tuple_307_0_index]
                tuple_307_0_index += 1
                var_311 = tuple_307_0
                tuple_307_1_index: int = 0
                tuple_307_1_vec: List[int] = self.index_310[var_308]
                while tuple_307_1_index < len(tuple_307_1_vec):
                    tuple_307_1 = tuple_307_1_vec[tuple_307_1_index]
                    tuple_307_1_index += 1
                    var_312 = tuple_307_1
                    # Program TupleCompare Region
                    if var_311 != var_312:
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_311_308 = (var_311, var_308)
                        prev_state = self.table_117[tuple_311_308]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_117[tuple_311_308] = 1 | 4
                            if not present_bit:
                                self.index_280[tuple_311_308[0]].append(tuple_311_308[1])
                            # Program VectorAppend Region
                            vec_317.append(var_311)
                        # Program TransitionState Region
                        tuple_312_308 = (var_312, var_308)
                        prev_state = self.table_126[tuple_312_308]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_126[tuple_312_308] = 1 | 4
                            if not present_bit:
                                self.index_275[tuple_312_308[0]].append(tuple_312_308[1])
                            # Program VectorAppend Region
                            vec_313.append(var_312)
        # Program VectorClear Region
        del vec_306[:]
        vec_index306 = 0
        # Program VectorUnique Region
        vec_313 = list(set(vec_313))
        vec_index313 = 0
        # Program TableJoin Region
        while vec_index313 < len(vec_313):
            var_315 = vec_313[vec_index313]
            vec_index313 += 1
            if var_315 in self.index_212:
                tuple_314_1_index: int = 0
                tuple_314_1_vec: List[int] = self.index_275[var_315]
                while tuple_314_1_index < len(tuple_314_1_vec):
                    tuple_314_1 = tuple_314_1_vec[tuple_314_1_index]
                    tuple_314_1_index += 1
                    var_316 = tuple_314_1
                    # Program TransitionState Region
                    tuple_316_315_7 = (var_316, var_315, self.var_7)
                    prev_state = self.table_11[tuple_316_315_7]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_316_315_7] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_316_315_7[1], tuple_316_315_7[2])].append(tuple_316_315_7[0])
                        # Program VectorAppend Region
                        vec_216.append((var_316, var_315, self.var_7))
        # Program VectorClear Region
        del vec_313[:]
        vec_index313 = 0
        # Program VectorUnique Region
        vec_317 = list(set(vec_317))
        vec_index317 = 0
        # Program TableJoin Region
        while vec_index317 < len(vec_317):
            var_319 = vec_317[vec_index317]
            vec_index317 += 1
            if var_319 in self.index_212:
                tuple_318_1_index: int = 0
                tuple_318_1_vec: List[int] = self.index_280[var_319]
                while tuple_318_1_index < len(tuple_318_1_vec):
                    tuple_318_1 = tuple_318_1_vec[tuple_318_1_index]
                    tuple_318_1_index += 1
                    var_320 = tuple_318_1
                    # Program TransitionState Region
                    tuple_320_319_0 = (var_320, var_319, self.var_0)
                    prev_state = self.table_11[tuple_320_319_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_320_319_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_320_319_0[1], tuple_320_319_0[2])].append(tuple_320_319_0[0])
                        # Program VectorAppend Region
                        vec_216.append((var_320, var_319, self.var_0))
        # Program VectorClear Region
        del vec_317[:]
        vec_index317 = 0
        # Program VectorClear Region
        del vec_302[:]
        vec_index302 = 0
        # Program Return Region
        param_0[0] = vec_216
        return False
        return False

    def proc_217_(self, vec_218: List[Tuple[int, int, ControlFlowEdgeKind]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index218: int = 0
        vec_452: List[int] = list()
        vec_index452: int = 0
        vec_453: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index453: int = 0
        vec_463: List[int] = list()
        vec_index463: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        while vec_index218 < len(vec_218):
            var_442, var_443, var_444 = vec_218[vec_index218]
            vec_index218 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_2 == var_444:
                # Program Parallel Region
                # Program Series Region
                # Program TransitionState Region
                # Eager insert before negation to prevent race
                tuple_443_442 = (var_443, var_442)
                prev_state = self.table_41[tuple_443_442]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0:
                    self.table_41[tuple_443_442] = 2 | 4
                    if not present_bit:
                        self.index_338[tuple_443_442[0]].append(tuple_443_442[1])
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_256_(var_443)
                if not ret:
                    # Program TransitionState Region
                    tuple_443_442 = (var_443, var_442)
                    prev_state = self.table_41[tuple_443_442]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_41[tuple_443_442] = 1 | 4
                        if not present_bit:
                            self.index_338[tuple_443_442[0]].append(tuple_443_442[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_447_(var_442, var_443, self.var_2)
                        if not ret:
                            # Program TransitionState Region
                            tuple_442_443_2 = (var_442, var_443, self.var_2)
                            prev_state = self.table_20[tuple_442_443_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_20[tuple_442_443_2] = 1 | 4
                                if not present_bit:
                                    self.index_864[(tuple_442_443_2[1], tuple_442_443_2[2])].append(tuple_442_443_2[0])
                                    self.index_956[(tuple_442_443_2[0], tuple_442_443_2[1])].append(tuple_442_443_2[2])
                                    self.index_1381[tuple_442_443_2[1]].append((tuple_442_443_2[0], tuple_442_443_2[2]))
                                # Program VectorAppend Region
                                vec_453.append((var_442, var_443, self.var_2))
                # Program TransitionState Region
                tuple_442_443 = (var_442, var_443)
                prev_state = self.table_136[tuple_442_443]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_136[tuple_442_443] = 1 | 4
                    if not present_bit:
                        self.index_385[tuple_442_443[1]].append(tuple_442_443[0])
                    # Program VectorAppend Region
                    vec_463.append(var_443)
            # Program TupleCompare Region
            if var_444 != self.var_2:
                # Program TupleCompare Region
                if var_444 != self.var_9:
                    # Program TransitionState Region
                    var_444 = self._resolve_edgetype(var_444)
                    tuple_442_443_444 = (var_442, var_443, var_444)
                    prev_state = self.table_20[tuple_442_443_444]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_442_443_444] = 1 | 4
                        if not present_bit:
                            self.index_864[(tuple_442_443_444[1], tuple_442_443_444[2])].append(tuple_442_443_444[0])
                            self.index_956[(tuple_442_443_444[0], tuple_442_443_444[1])].append(tuple_442_443_444[2])
                            self.index_1381[tuple_442_443_444[1]].append((tuple_442_443_444[0], tuple_442_443_444[2]))
                        # Program VectorAppend Region
                        var_444 = self._resolve_edgetype(var_444)
                        vec_453.append((var_442, var_443, var_444))
            # Program TupleCompare Region
            if self.var_9 == var_444:
                # Program Series Region
                # Program TransitionState Region
                # Eager insert before negation to prevent race
                tuple_443_442 = (var_443, var_442)
                prev_state = self.table_38[tuple_443_442]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0:
                    self.table_38[tuple_443_442] = 2 | 4
                    if not present_bit:
                        self.index_423[tuple_443_442[0]].append(tuple_443_442[1])
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_436_(var_443)
                if not ret:
                    # Program TransitionState Region
                    tuple_443_442 = (var_443, var_442)
                    prev_state = self.table_38[tuple_443_442]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_38[tuple_443_442] = 1 | 4
                        if not present_bit:
                            self.index_423[tuple_443_442[0]].append(tuple_443_442[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_458_(var_442, var_443, self.var_9)
                        if not ret:
                            # Program TransitionState Region
                            tuple_442_443_9 = (var_442, var_443, self.var_9)
                            prev_state = self.table_20[tuple_442_443_9]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_20[tuple_442_443_9] = 1 | 4
                                if not present_bit:
                                    self.index_864[(tuple_442_443_9[1], tuple_442_443_9[2])].append(tuple_442_443_9[0])
                                    self.index_956[(tuple_442_443_9[0], tuple_442_443_9[1])].append(tuple_442_443_9[2])
                                    self.index_1381[tuple_442_443_9[1]].append((tuple_442_443_9[0], tuple_442_443_9[2]))
                                # Program VectorAppend Region
                                vec_453.append((var_442, var_443, self.var_9))
        # Program VectorUnique Region
        vec_463 = list(set(vec_463))
        vec_index463 = 0
        # Program TableJoin Region
        while vec_index463 < len(vec_463):
            var_465 = vec_463[vec_index463]
            vec_index463 += 1
            tuple_464_0_index: int = 0
            tuple_464_0_vec: List[int] = self.index_385[var_465]
            while tuple_464_0_index < len(tuple_464_0_vec):
                tuple_464_0 = tuple_464_0_vec[tuple_464_0_index]
                tuple_464_0_index += 1
                var_466 = tuple_464_0
                if var_465 in self.index_253:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_387_(var_466, var_465)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_256_(var_465)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_392_(var_466, var_465, self.var_10)
                            if not ret:
                                # Program TransitionState Region
                                tuple_466_465_10 = (var_466, var_465, self.var_10)
                                prev_state = self.table_20[tuple_466_465_10]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_20[tuple_466_465_10] = 1 | 4
                                    if not present_bit:
                                        self.index_864[(tuple_466_465_10[1], tuple_466_465_10[2])].append(tuple_466_465_10[0])
                                        self.index_956[(tuple_466_465_10[0], tuple_466_465_10[1])].append(tuple_466_465_10[2])
                                        self.index_1381[tuple_466_465_10[1]].append((tuple_466_465_10[0], tuple_466_465_10[2]))
                                    # Program VectorAppend Region
                                    vec_453.append((var_466, var_465, self.var_10))
        # Program VectorClear Region
        del vec_463[:]
        vec_index463 = 0
        # Induction Fixpoint Loop Region
        while len(vec_452) or len(vec_453):
            # Program Series Region
            # Program Call Region
            ret = self.proc_164_(vec_452, vec_453)

            # Program Call Region
            param_455_0 = [vec_452]
            param_455_1 = [vec_453]
            ret = self.proc_161_(param_455_0, param_455_1)
            vec_452 = param_455_0[0]
            vec_453 = param_455_1[0]

        vec_index452 = 0
        vec_index453 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_452[:]
        vec_index452 = 0
        # Program VectorClear Region
        del vec_453[:]
        vec_index453 = 0
        # Program Return Region
        return False
        return False

    def proc_256_(self, var_257: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_257] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_257 = var_257
            prev_state = self.table_15[tuple_257]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_257] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1082_(var_257)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_257 = var_257
                    prev_state = self.table_15[tuple_257]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_257] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_259_(self, var_260: int, var_261: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_60[(var_260, var_261)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_260_261 = (var_260, var_261)
            prev_state = self.table_60[tuple_260_261]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_60[tuple_260_261] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1064_(var_260, var_261)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_260_261 = (var_260, var_261)
                    prev_state = self.table_60[tuple_260_261]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_60[tuple_260_261] = 1 | 4
                        if not present_bit:
                            self.index_254[tuple_260_261[1]].append(tuple_260_261[0])
                            self.index_852[tuple_260_261[0]].append(tuple_260_261[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_263_(self, var_264: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_264] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_264 = var_264
            prev_state = self.table_15[tuple_264]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_264] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_848_(var_264)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_264 = var_264
                    prev_state = self.table_15[tuple_264]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_264] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_330_(self, var_331: int, var_332: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_332_331 = (var_332, var_331)
        prev_state = self.table_69[tuple_332_331]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_69[tuple_332_331] = 2 | 4
            # Program Call Region
            ret = self.proc_1359_(var_332, var_331)

        # Program Return Region
        return False
        return False

    def proc_334_(self, var_335: int, var_336: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_336_335 = (var_336, var_335)
        prev_state = self.table_28[tuple_336_335]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_28[tuple_336_335] = 2 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_944_(var_335, var_336)

        # Program Return Region
        return False
        return False

    def proc_341_(self, var_342: int, var_343: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_343_342_2 = (var_343, var_342, self.var_2)
        prev_state = self.table_20[tuple_343_342_2]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_20[tuple_343_342_2] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1095_(var_343, var_342, self.var_2)

            # Program Call Region
            ret = self.proc_1100_(var_343, var_342, self.var_2)

            # Program Call Region
            ret = self.proc_1105_(var_343, var_342, self.var_2)

            # Program Call Region
            ret = self.proc_1110_(var_343, var_342, self.var_2)

            # Program Call Region
            ret = self.proc_1115_(var_343, var_342, self.var_2)

        # Program Return Region
        return False
        return False

    def proc_346_(self, var_347: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_347] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_347 = var_347
            prev_state = self.table_15[tuple_347]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_347] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_860_(self.var_0, var_347)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_347 = var_347
                    prev_state = self.table_15[tuple_347]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_347] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_367_(self, var_368: int, var_369: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_133[(var_368, var_369)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_368_369 = (var_368, var_369)
            prev_state = self.table_133[tuple_368_369]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_133[tuple_368_369] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1048_(self.var_8, var_368, var_369)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_368_369 = (var_368, var_369)
                    prev_state = self.table_133[tuple_368_369]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_133[tuple_368_369] = 1 | 4
                        if not present_bit:
                            self.index_365[tuple_368_369[1]].append(tuple_368_369[0])
                            self.index_997[tuple_368_369[0]].append(tuple_368_369[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_372_(self, var_373: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_24[var_373] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_373 = var_373
            prev_state = self.table_24[tuple_373]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_24[tuple_373] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1015_(var_373)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_373 = var_373
                    prev_state = self.table_24[tuple_373]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_24[tuple_373] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_375_(self, param_0: List[List[int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_376 = param_0[0]
        vec_index376: int = 0
        vec_421: List[int] = list()
        vec_index421: int = 0
        vec_424: List[int] = list()
        vec_index424: int = 0
        vec_430: List[int] = list()
        vec_index430: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_376, vec_421 = vec_421, vec_376
        # Program VectorLoop Region
        while vec_index421 < len(vec_421):
            var_422 = vec_421[vec_index421]
            vec_index421 += 1
            # Program Series Region
            # Program TableScan Region
            scan_tuple_424: int
            scan_index_424: int = 0
            scan_tuple_424_vec: List[int] = self.index_423[var_422]
            while scan_index_424 < len(scan_tuple_424_vec):
                scan_tuple_424 = scan_tuple_424_vec[scan_index_424]
                scan_index_424 += 1
                vec_424.append(scan_tuple_424)
            # Program VectorLoop Region
            vec_index424 = 0
            while vec_index424 < len(vec_424):
                var_425 = vec_424[vec_index424]
                vec_index424 += 1
                # Program TransitionState Region
                # Remove from negated view
                tuple_422_425 = (var_422, var_425)
                prev_state = self.table_38[tuple_422_425]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 1:
                    self.table_38[tuple_422_425] = 0 | 4
                    # Program Call Region
                    ret = self.proc_426_(var_422, var_425)

            # Program VectorAppend Region
            vec_430.append(var_422)
        # Program VectorUnique Region
        vec_430 = list(set(vec_430))
        vec_index430 = 0
        # Program TableJoin Region
        while vec_index430 < len(vec_430):
            var_432 = vec_430[vec_index430]
            vec_index430 += 1
            tuple_431_0_index: int = 0
            tuple_431_0_vec: List[int] = self.index_365[var_432]
            while tuple_431_0_index < len(tuple_431_0_vec):
                tuple_431_0 = tuple_431_0_vec[tuple_431_0_index]
                tuple_431_0_index += 1
                var_434 = tuple_431_0
                if var_432 in self.index_433:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_367_(var_434, var_432)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_436_(var_432)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_439_(var_434)
                            if not ret:
                                # Program TransitionState Region
                                tuple_434 = var_434
                                prev_state = self.table_24[tuple_434]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_24[tuple_434] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_376.append(var_434)
        # Program VectorClear Region
        del vec_430[:]
        vec_index430 = 0
        # Program VectorClear Region
        del vec_421[:]
        vec_index421 = 0
        # Program Return Region
        param_0[0] = vec_376
        return False
        return False

    def proc_387_(self, var_388: int, var_389: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_136[(var_388, var_389)] & 3
        if state == 1:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_392_(self, var_393: int, var_394: int, var_395: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_20[(var_393, var_394, self.var_10)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_393_394_10 = (var_393, var_394, self.var_10)
            prev_state = self.table_20[tuple_393_394_10]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_20[tuple_393_394_10] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_911_(var_394, var_393)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_393_394_10 = (var_393, var_394, self.var_10)
                    prev_state = self.table_20[tuple_393_394_10]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_393_394_10] = 1 | 4
                        if not present_bit:
                            self.index_864[(tuple_393_394_10[1], tuple_393_394_10[2])].append(tuple_393_394_10[0])
                            self.index_956[(tuple_393_394_10[0], tuple_393_394_10[1])].append(tuple_393_394_10[2])
                            self.index_1381[tuple_393_394_10[1]].append((tuple_393_394_10[0], tuple_393_394_10[2]))
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_402_(self, var_403: int, var_404: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_139[(var_403, var_404)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_403_404 = (var_403, var_404)
            prev_state = self.table_139[tuple_403_404]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_139[tuple_403_404] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1036_(var_403, var_404)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_403_404 = (var_403, var_404)
                    prev_state = self.table_139[tuple_403_404]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_139[tuple_403_404] = 1 | 4
                        if not present_bit:
                            self.index_400[tuple_403_404[1]].append(tuple_403_404[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_407_(self, var_408: int, var_409: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_142[(var_408, var_409)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_408_409 = (var_408, var_409)
            prev_state = self.table_142[tuple_408_409]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_142[tuple_408_409] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1026_(var_409, var_408)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_408_409 = (var_408, var_409)
                    prev_state = self.table_142[tuple_408_409]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_142[tuple_408_409] = 1 | 4
                        if not present_bit:
                            self.index_414[tuple_408_409[1]].append(tuple_408_409[0])
                            self.index_967[tuple_408_409[0]].append(tuple_408_409[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_418_(self, var_419: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_47[var_419] & 3
        if state == 1:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_426_(self, var_427: int, var_428: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_428_427_9 = (var_428, var_427, self.var_9)
        prev_state = self.table_20[tuple_428_427_9]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_20[tuple_428_427_9] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1095_(var_428, var_427, self.var_9)

            # Program Call Region
            ret = self.proc_1100_(var_428, var_427, self.var_9)

            # Program Call Region
            ret = self.proc_1105_(var_428, var_427, self.var_9)

            # Program Call Region
            ret = self.proc_1110_(var_428, var_427, self.var_9)

            # Program Call Region
            ret = self.proc_1115_(var_428, var_427, self.var_9)

        # Program Return Region
        return False
        return False

    def proc_436_(self, var_437: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_24[var_437] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_437 = var_437
            prev_state = self.table_24[tuple_437]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_24[tuple_437] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1005_(var_437)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_437 = var_437
                    prev_state = self.table_24[tuple_437]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_24[tuple_437] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_439_(self, var_440: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_24[var_440] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_440 = var_440
            prev_state = self.table_24[tuple_440]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_24[tuple_440] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_993_(var_440)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_440 = var_440
                    prev_state = self.table_24[tuple_440]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_24[tuple_440] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_447_(self, var_448: int, var_449: int, var_450: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_20[(var_448, var_449, self.var_2)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_448_449_2 = (var_448, var_449, self.var_2)
            prev_state = self.table_20[tuple_448_449_2]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_20[tuple_448_449_2] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_893_(var_449, var_448)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_448_449_2 = (var_448, var_449, self.var_2)
                    prev_state = self.table_20[tuple_448_449_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_448_449_2] = 1 | 4
                        if not present_bit:
                            self.index_864[(tuple_448_449_2[1], tuple_448_449_2[2])].append(tuple_448_449_2[0])
                            self.index_956[(tuple_448_449_2[0], tuple_448_449_2[1])].append(tuple_448_449_2[2])
                            self.index_1381[tuple_448_449_2[1]].append((tuple_448_449_2[0], tuple_448_449_2[2]))
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_458_(self, var_459: int, var_460: int, var_461: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_20[(var_459, var_460, self.var_9)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_459_460_9 = (var_459, var_460, self.var_9)
            prev_state = self.table_20[tuple_459_460_9]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_20[tuple_459_460_9] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_920_(var_460, var_459)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_459_460_9 = (var_459, var_460, self.var_9)
                    prev_state = self.table_20[tuple_459_460_9]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_459_460_9] = 1 | 4
                        if not present_bit:
                            self.index_864[(tuple_459_460_9[1], tuple_459_460_9[2])].append(tuple_459_460_9[0])
                            self.index_956[(tuple_459_460_9[0], tuple_459_460_9[1])].append(tuple_459_460_9[2])
                            self.index_1381[tuple_459_460_9[1]].append((tuple_459_460_9[0], tuple_459_460_9[2]))
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_475_(self, var_476: int, var_477: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_17[(var_476, var_477)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_476_477 = (var_476, var_477)
            prev_state = self.table_17[tuple_476_477]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_17[tuple_476_477] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_824_(var_477)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_476_477 = (var_476, var_477)
                    prev_state = self.table_17[tuple_476_477]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_476_477] = 1 | 4
                        if not present_bit:
                            self.index_521[tuple_476_477[1]].append(tuple_476_477[0])
                            self.index_780[tuple_476_477[0]].append(tuple_476_477[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_479_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_480 = param_0[0]
        vec_index480: int = 0
        vec_540: List[Tuple[int, int]] = list()
        vec_index540: int = 0
        vec_543: List[int] = list()
        vec_index543: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_480, vec_540 = vec_540, vec_480
        # Program VectorLoop Region
        while vec_index540 < len(vec_540):
            var_541, var_542 = vec_540[vec_index540]
            vec_index540 += 1
            # Program VectorAppend Region
            vec_543.append(var_542)
        # Program VectorUnique Region
        vec_543 = list(set(vec_543))
        vec_index543 = 0
        # Program TableJoin Region
        while vec_index543 < len(vec_543):
            var_545 = vec_543[vec_index543]
            vec_index543 += 1
            tuple_544_0_index: int = 0
            tuple_544_0_vec: List[int] = self.index_521[var_545]
            while tuple_544_0_index < len(tuple_544_0_vec):
                tuple_544_0 = tuple_544_0_vec[tuple_544_0_index]
                tuple_544_0_index += 1
                var_546 = tuple_544_0
                tuple_544_1_index: int = 0
                tuple_544_1_vec: List[int] = self.index_522[var_545]
                while tuple_544_1_index < len(tuple_544_1_vec):
                    tuple_544_1 = tuple_544_1_vec[tuple_544_1_index]
                    tuple_544_1_index += 1
                    var_547 = tuple_544_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_525_(var_546, var_545)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_490_(var_545, var_547)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_530_(var_546, var_547)
                            if not ret:
                                # Program TransitionState Region
                                tuple_546_547 = (var_546, var_547)
                                prev_state = self.table_17[tuple_546_547]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_546_547] = 1 | 4
                                    if not present_bit:
                                        self.index_521[tuple_546_547[1]].append(tuple_546_547[0])
                                        self.index_780[tuple_546_547[0]].append(tuple_546_547[1])
                                    # Program VectorAppend Region
                                    vec_480.append((var_546, var_547))
        # Program VectorClear Region
        del vec_543[:]
        vec_index543 = 0
        # Program VectorClear Region
        del vec_540[:]
        vec_index540 = 0
        # Program Return Region
        param_0[0] = vec_480
        return False
        return False

    def proc_490_(self, var_491: int, var_492: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_69[(var_491, var_492)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_491_492 = (var_491, var_492)
            prev_state = self.table_69[tuple_491_492]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_69[tuple_491_492] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_944_(var_492, var_491)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_491_492 = (var_491, var_492)
                    prev_state = self.table_69[tuple_491_492]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_69[tuple_491_492] = 1 | 4
                        if not present_bit:
                            self.index_522[tuple_491_492[0]].append(tuple_491_492[1])
                            self.index_815[tuple_491_492[1]].append(tuple_491_492[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_525_(self, var_526: int, var_527: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_17[(var_526, var_527)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_526_527 = (var_526, var_527)
            prev_state = self.table_17[tuple_526_527]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_17[tuple_526_527] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_975_(var_526, var_527)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_526_527 = (var_526, var_527)
                    prev_state = self.table_17[tuple_526_527]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_526_527] = 1 | 4
                        if not present_bit:
                            self.index_521[tuple_526_527[1]].append(tuple_526_527[0])
                            self.index_780[tuple_526_527[0]].append(tuple_526_527[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_530_(self, var_531: int, var_532: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_17[(var_531, var_532)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_531_532 = (var_531, var_532)
            prev_state = self.table_17[tuple_531_532]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_17[tuple_531_532] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_810_(var_531, var_532)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_531_532 = (var_531, var_532)
                    prev_state = self.table_17[tuple_531_532]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_531_532] = 1 | 4
                        if not present_bit:
                            self.index_521[tuple_531_532[1]].append(tuple_531_532[0])
                            self.index_780[tuple_531_532[0]].append(tuple_531_532[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def external_symbol_2(self, vec_554: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index554: int = 0
        vec_557: List[int] = list()
        vec_index557: int = 0
        vec_561: List[int] = list()
        vec_index561: int = 0
        vec_562: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index562: int = 0
        vec_565: List[int] = list()
        vec_index565: int = 0
        vec_570: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index570: int = 0
        vec_573: List[int] = list()
        vec_index573: int = 0
        vec_576: List[int] = list()
        vec_index576: int = 0
        vec_580: List[int] = list()
        vec_index580: int = 0
        vec_584: List[int] = list()
        vec_index584: int = 0
        vec_588: List[int] = list()
        vec_index588: int = 0
        vec_592: List[int] = list()
        vec_index592: int = 0
        vec_596: List[int] = list()
        vec_index596: int = 0
        vec_600: List[int] = list()
        vec_index600: int = 0
        vec_604: List[int] = list()
        vec_index604: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index554 = 0
        while vec_index554 < len(vec_554):
            var_555, var_556 = vec_554[vec_index554]
            vec_index554 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_555 = var_555
            prev_state = self.table_47[tuple_555]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_47[tuple_555] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_555 = var_555
                prev_state = self.table_53[tuple_555]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_555] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_573.append(var_555)
                    # Program VectorAppend Region
                    vec_600.append(var_555)
                    # Program VectorAppend Region
                    vec_596.append(var_555)
                    # Program VectorAppend Region
                    vec_592.append(var_555)
                    # Program VectorAppend Region
                    vec_588.append(var_555)
                    # Program VectorAppend Region
                    vec_576.append(var_555)
                    # Program VectorAppend Region
                    vec_584.append(var_555)
                    # Program VectorAppend Region
                    vec_580.append(var_555)
                    # Program VectorAppend Region
                    vec_565.append(var_555)
                # Program VectorAppend Region
                vec_557.append(var_555)
                # Program VectorAppend Region
                vec_604.append(var_555)
            # Program TransitionState Region
            tuple_555 = var_555
            prev_state = self.table_47[tuple_555]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_47[tuple_555] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_555 = var_555
                prev_state = self.table_53[tuple_555]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_555] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_573.append(var_555)
                    # Program VectorAppend Region
                    vec_600.append(var_555)
                    # Program VectorAppend Region
                    vec_596.append(var_555)
                    # Program VectorAppend Region
                    vec_592.append(var_555)
                    # Program VectorAppend Region
                    vec_588.append(var_555)
                    # Program VectorAppend Region
                    vec_576.append(var_555)
                    # Program VectorAppend Region
                    vec_584.append(var_555)
                    # Program VectorAppend Region
                    vec_580.append(var_555)
                    # Program VectorAppend Region
                    vec_565.append(var_555)
                # Program VectorAppend Region
                vec_557.append(var_555)
                # Program VectorAppend Region
                vec_604.append(var_555)
            # Program TransitionState Region
            tuple_555 = var_555
            prev_state = self.table_47[tuple_555]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_47[tuple_555] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_555 = var_555
                prev_state = self.table_53[tuple_555]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_53[tuple_555] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_573.append(var_555)
                    # Program VectorAppend Region
                    vec_600.append(var_555)
                    # Program VectorAppend Region
                    vec_596.append(var_555)
                    # Program VectorAppend Region
                    vec_592.append(var_555)
                    # Program VectorAppend Region
                    vec_588.append(var_555)
                    # Program VectorAppend Region
                    vec_576.append(var_555)
                    # Program VectorAppend Region
                    vec_584.append(var_555)
                    # Program VectorAppend Region
                    vec_580.append(var_555)
                    # Program VectorAppend Region
                    vec_565.append(var_555)
                # Program VectorAppend Region
                vec_557.append(var_555)
                # Program VectorAppend Region
                vec_604.append(var_555)
        # Program VectorUnique Region
        vec_557 = list(set(vec_557))
        vec_index557 = 0
        # Program TableJoin Region
        while vec_index557 < len(vec_557):
            var_559 = vec_557[vec_index557]
            vec_index557 += 1
            if var_559 in self.index_415:
                if var_559 in self.index_560:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_559 = var_559
                    prev_state = self.table_15[tuple_559]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_559] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_561.append(var_559)
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
            tuple_566_0_vec: List[Tuple[ControlFlowEdgeKind, int]] = self.index_211[var_567]
            while tuple_566_0_index < len(tuple_566_0_vec):
                tuple_566_0 = tuple_566_0_vec[tuple_566_0_index]
                tuple_566_0_index += 1
                var_568 = tuple_566_0[0]
                var_569 = tuple_566_0[1]
                if var_567 in self.index_212:
                    # Program TransitionState Region
                    var_568 = self._resolve_edgetype(var_568)
                    tuple_569_567_568 = (var_569, var_567, var_568)
                    prev_state = self.table_11[tuple_569_567_568]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_569_567_568] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_569_567_568[1], tuple_569_567_568[2])].append(tuple_569_567_568[0])
                        # Program VectorAppend Region
                        var_568 = self._resolve_edgetype(var_568)
                        vec_570.append((var_569, var_567, var_568))
        # Program VectorClear Region
        del vec_565[:]
        vec_index565 = 0
        # Program VectorUnique Region
        vec_573 = list(set(vec_573))
        vec_index573 = 0
        # Program TableJoin Region
        while vec_index573 < len(vec_573):
            var_575 = vec_573[vec_index573]
            vec_index573 += 1
            if var_575 in self.index_225:
                if var_575 in self.index_212:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_575 = var_575
                    prev_state = self.table_15[tuple_575]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_575] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_561.append(var_575)
        # Program VectorClear Region
        del vec_573[:]
        vec_index573 = 0
        # Program VectorUnique Region
        vec_576 = list(set(vec_576))
        vec_index576 = 0
        # Program TableJoin Region
        while vec_index576 < len(vec_576):
            var_578 = vec_576[vec_index576]
            vec_index576 += 1
            if var_578 in self.index_212:
                tuple_577_1_index: int = 0
                tuple_577_1_vec: List[int] = self.index_248[var_578]
                while tuple_577_1_index < len(tuple_577_1_vec):
                    tuple_577_1 = tuple_577_1_vec[tuple_577_1_index]
                    tuple_577_1_index += 1
                    var_579 = tuple_577_1
                    # Program TransitionState Region
                    tuple_579_578_6 = (var_579, var_578, self.var_6)
                    prev_state = self.table_11[tuple_579_578_6]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_579_578_6] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_579_578_6[1], tuple_579_578_6[2])].append(tuple_579_578_6[0])
                        # Program VectorAppend Region
                        vec_570.append((var_579, var_578, self.var_6))
        # Program VectorClear Region
        del vec_576[:]
        vec_index576 = 0
        # Program VectorUnique Region
        vec_580 = list(set(vec_580))
        vec_index580 = 0
        # Program TableJoin Region
        while vec_index580 < len(vec_580):
            var_582 = vec_580[vec_index580]
            vec_index580 += 1
            if var_582 in self.index_212:
                tuple_581_1_index: int = 0
                tuple_581_1_vec: List[int] = self.index_275[var_582]
                while tuple_581_1_index < len(tuple_581_1_vec):
                    tuple_581_1 = tuple_581_1_vec[tuple_581_1_index]
                    tuple_581_1_index += 1
                    var_583 = tuple_581_1
                    # Program TransitionState Region
                    tuple_583_582_7 = (var_583, var_582, self.var_7)
                    prev_state = self.table_11[tuple_583_582_7]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_583_582_7] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_583_582_7[1], tuple_583_582_7[2])].append(tuple_583_582_7[0])
                        # Program VectorAppend Region
                        vec_570.append((var_583, var_582, self.var_7))
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
            if var_586 in self.index_212:
                tuple_585_1_index: int = 0
                tuple_585_1_vec: List[int] = self.index_280[var_586]
                while tuple_585_1_index < len(tuple_585_1_vec):
                    tuple_585_1 = tuple_585_1_vec[tuple_585_1_index]
                    tuple_585_1_index += 1
                    var_587 = tuple_585_1
                    # Program TransitionState Region
                    tuple_587_586_0 = (var_587, var_586, self.var_0)
                    prev_state = self.table_11[tuple_587_586_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_587_586_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_587_586_0[1], tuple_587_586_0[2])].append(tuple_587_586_0[0])
                        # Program VectorAppend Region
                        vec_570.append((var_587, var_586, self.var_0))
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
            if var_590 in self.index_212:
                tuple_589_1_index: int = 0
                tuple_589_1_vec: List[int] = self.index_285[var_590]
                while tuple_589_1_index < len(tuple_589_1_vec):
                    tuple_589_1 = tuple_589_1_vec[tuple_589_1_index]
                    tuple_589_1_index += 1
                    var_591 = tuple_589_1
                    # Program TransitionState Region
                    tuple_591_590_0 = (var_591, var_590, self.var_0)
                    prev_state = self.table_11[tuple_591_590_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_591_590_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_591_590_0[1], tuple_591_590_0[2])].append(tuple_591_590_0[0])
                        # Program VectorAppend Region
                        vec_570.append((var_591, var_590, self.var_0))
        # Program VectorClear Region
        del vec_588[:]
        vec_index588 = 0
        # Program VectorUnique Region
        vec_592 = list(set(vec_592))
        vec_index592 = 0
        # Program TableJoin Region
        while vec_index592 < len(vec_592):
            var_594 = vec_592[vec_index592]
            vec_index592 += 1
            if var_594 in self.index_212:
                tuple_593_1_index: int = 0
                tuple_593_1_vec: List[int] = self.index_290[var_594]
                while tuple_593_1_index < len(tuple_593_1_vec):
                    tuple_593_1 = tuple_593_1_vec[tuple_593_1_index]
                    tuple_593_1_index += 1
                    var_595 = tuple_593_1
                    # Program TransitionState Region
                    tuple_595_594_0 = (var_595, var_594, self.var_0)
                    prev_state = self.table_11[tuple_595_594_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_595_594_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_595_594_0[1], tuple_595_594_0[2])].append(tuple_595_594_0[0])
                        # Program VectorAppend Region
                        vec_570.append((var_595, var_594, self.var_0))
        # Program VectorClear Region
        del vec_592[:]
        vec_index592 = 0
        # Program VectorUnique Region
        vec_596 = list(set(vec_596))
        vec_index596 = 0
        # Program TableJoin Region
        while vec_index596 < len(vec_596):
            var_598 = vec_596[vec_index596]
            vec_index596 += 1
            if var_598 in self.index_212:
                tuple_597_1_index: int = 0
                tuple_597_1_vec: List[int] = self.index_295[var_598]
                while tuple_597_1_index < len(tuple_597_1_vec):
                    tuple_597_1 = tuple_597_1_vec[tuple_597_1_index]
                    tuple_597_1_index += 1
                    var_599 = tuple_597_1
                    # Program TransitionState Region
                    tuple_599_598_2 = (var_599, var_598, self.var_2)
                    prev_state = self.table_11[tuple_599_598_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_599_598_2] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_599_598_2[1], tuple_599_598_2[2])].append(tuple_599_598_2[0])
                        # Program VectorAppend Region
                        vec_570.append((var_599, var_598, self.var_2))
        # Program VectorClear Region
        del vec_596[:]
        vec_index596 = 0
        # Program VectorUnique Region
        vec_600 = list(set(vec_600))
        vec_index600 = 0
        # Program TableJoin Region
        while vec_index600 < len(vec_600):
            var_602 = vec_600[vec_index600]
            vec_index600 += 1
            if var_602 in self.index_212:
                tuple_601_1_index: int = 0
                tuple_601_1_vec: List[int] = self.index_300[var_602]
                while tuple_601_1_index < len(tuple_601_1_vec):
                    tuple_601_1 = tuple_601_1_vec[tuple_601_1_index]
                    tuple_601_1_index += 1
                    var_603 = tuple_601_1
                    # Program TransitionState Region
                    tuple_603_602_2 = (var_603, var_602, self.var_2)
                    prev_state = self.table_11[tuple_603_602_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_603_602_2] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_603_602_2[1], tuple_603_602_2[2])].append(tuple_603_602_2[0])
                        # Program VectorAppend Region
                        vec_570.append((var_603, var_602, self.var_2))
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
            tuple_605_0_index: int = 0
            tuple_605_0_vec: List[int] = self.index_414[var_606]
            while tuple_605_0_index < len(tuple_605_0_vec):
                tuple_605_0 = tuple_605_0_vec[tuple_605_0_index]
                tuple_605_0_index += 1
                var_607 = tuple_605_0
                if var_606 in self.index_415:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_407_(var_607, var_606)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_418_(var_606)
                        if ret:
                            # Program TransitionState Region
                            tuple_607 = var_607
                            prev_state = self.table_26[tuple_607]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_26[tuple_607] = 1 | 4
                                if not present_bit:
                                    pass
        # Program VectorClear Region
        del vec_604[:]
        vec_index604 = 0
        # Induction Fixpoint Loop Region
        while len(vec_570) or len(vec_561) or len(vec_562):
            # Program Series Region
            # Program Call Region
            ret = self.proc_164_(vec_561, vec_562)

            # Program Call Region
            param_564_0 = [vec_561]
            param_564_1 = [vec_562]
            ret = self.proc_161_(param_564_0, param_564_1)
            vec_561 = param_564_0[0]
            vec_562 = param_564_1[0]

            # Program Call Region
            ret = self.proc_217_(vec_570)

            # Program Call Region
            param_572_0 = [vec_570]
            ret = self.proc_215_(param_572_0)
            vec_570 = param_572_0[0]

        vec_index570 = 0
        vec_index561 = 0
        vec_index562 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_561[:]
        vec_index561 = 0
        # Program VectorClear Region
        del vec_562[:]
        vec_index562 = 0
        # Program VectorClear Region
        del vec_570[:]
        vec_index570 = 0
        # Program Return Region
        return False
        return False

    def raw_transfer_3(self, vec_611: List[Tuple[int, int, ControlFlowEdgeKind]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index611: int = 0
        vec_615: List[int] = list()
        vec_index615: int = 0
        vec_618: List[int] = list()
        vec_index618: int = 0
        vec_619: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index619: int = 0
        vec_622: List[Tuple[int, int]] = list()
        vec_index622: int = 0
        vec_628: List[int] = list()
        vec_index628: int = 0
        vec_633: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index633: int = 0
        vec_636: List[int] = list()
        vec_index636: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index611 = 0
        while vec_index611 < len(vec_611):
            var_612, var_613, var_614 = vec_611[vec_index611]
            vec_index611 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_613 = var_613
            prev_state = self.table_49[tuple_613]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_613] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_615.append(var_613)
            # Program TupleCompare Region
            if self.var_0 == var_614:
                # Program TransitionState Region
                tuple_612_613 = (var_612, var_613)
                prev_state = self.table_108[tuple_612_613]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_108[tuple_612_613] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_622.append((var_612, var_613))
            # Program TupleCompare Region
            if self.var_7 == var_614:
                # Program TransitionState Region
                tuple_612_613 = (var_612, var_613)
                prev_state = self.table_111[tuple_612_613]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_111[tuple_612_613] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_622.append((var_612, var_613))
            # Program TupleCompare Region
            if var_614 != self.var_0:
                # Program TupleCompare Region
                if var_614 != self.var_7:
                    # Program TransitionState Region
                    var_614 = self._resolve_edgetype(var_614)
                    tuple_614_612_613 = (var_614, var_612, var_613)
                    prev_state = self.table_129[tuple_614_612_613]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_129[tuple_614_612_613] = 1 | 4
                        if not present_bit:
                            self.index_211[tuple_614_612_613[2]].append((tuple_614_612_613[0], tuple_614_612_613[1]))
                        # Program VectorAppend Region
                        vec_628.append(var_613)
        # Program VectorUnique Region
        vec_615 = list(set(vec_615))
        vec_index615 = 0
        # Program TableJoin Region
        while vec_index615 < len(vec_615):
            var_617 = vec_615[vec_index615]
            vec_index615 += 1
            if var_617 in self.index_415:
                if var_617 in self.index_560:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_617 = var_617
                    prev_state = self.table_15[tuple_617]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_617] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_618.append(var_617)
        # Program VectorClear Region
        del vec_615[:]
        vec_index615 = 0
        # Program VectorUnique Region
        vec_622 = list(set(vec_622))
        vec_index622 = 0
        # Program TableJoin Region
        while vec_index622 < len(vec_622):
            var_624, var_625 = vec_622[vec_index622]
            vec_index622 += 1
            if (var_624, var_625) in self.index_626:
                if (var_624, var_625) in self.index_627:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_624_625 = (var_624, var_625)
                    prev_state = self.table_114[tuple_624_625]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_114[tuple_624_625] = 1 | 4
                        if not present_bit:
                            self.index_248[tuple_624_625[1]].append(tuple_624_625[0])
                        # Program VectorAppend Region
                        vec_636.append(var_625)
        # Program VectorClear Region
        del vec_622[:]
        vec_index622 = 0
        # Program VectorUnique Region
        vec_628 = list(set(vec_628))
        vec_index628 = 0
        # Program TableJoin Region
        while vec_index628 < len(vec_628):
            var_630 = vec_628[vec_index628]
            vec_index628 += 1
            tuple_629_0_index: int = 0
            tuple_629_0_vec: List[Tuple[ControlFlowEdgeKind, int]] = self.index_211[var_630]
            while tuple_629_0_index < len(tuple_629_0_vec):
                tuple_629_0 = tuple_629_0_vec[tuple_629_0_index]
                tuple_629_0_index += 1
                var_631 = tuple_629_0[0]
                var_632 = tuple_629_0[1]
                if var_630 in self.index_212:
                    # Program TransitionState Region
                    var_631 = self._resolve_edgetype(var_631)
                    tuple_632_630_631 = (var_632, var_630, var_631)
                    prev_state = self.table_11[tuple_632_630_631]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_632_630_631] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_632_630_631[1], tuple_632_630_631[2])].append(tuple_632_630_631[0])
                        # Program VectorAppend Region
                        var_631 = self._resolve_edgetype(var_631)
                        vec_633.append((var_632, var_630, var_631))
        # Program VectorClear Region
        del vec_628[:]
        vec_index628 = 0
        # Program VectorUnique Region
        vec_636 = list(set(vec_636))
        vec_index636 = 0
        # Program TableJoin Region
        while vec_index636 < len(vec_636):
            var_638 = vec_636[vec_index636]
            vec_index636 += 1
            if var_638 in self.index_212:
                tuple_637_1_index: int = 0
                tuple_637_1_vec: List[int] = self.index_248[var_638]
                while tuple_637_1_index < len(tuple_637_1_vec):
                    tuple_637_1 = tuple_637_1_vec[tuple_637_1_index]
                    tuple_637_1_index += 1
                    var_639 = tuple_637_1
                    # Program TransitionState Region
                    tuple_639_638_6 = (var_639, var_638, self.var_6)
                    prev_state = self.table_11[tuple_639_638_6]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_639_638_6] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_639_638_6[1], tuple_639_638_6[2])].append(tuple_639_638_6[0])
                        # Program VectorAppend Region
                        vec_633.append((var_639, var_638, self.var_6))
        # Program VectorClear Region
        del vec_636[:]
        vec_index636 = 0
        # Induction Fixpoint Loop Region
        while len(vec_618) or len(vec_619) or len(vec_633):
            # Program Series Region
            # Program Call Region
            ret = self.proc_217_(vec_633)

            # Program Call Region
            param_635_0 = [vec_633]
            ret = self.proc_215_(param_635_0)
            vec_633 = param_635_0[0]

            # Program Call Region
            ret = self.proc_164_(vec_618, vec_619)

            # Program Call Region
            param_621_0 = [vec_618]
            param_621_1 = [vec_619]
            ret = self.proc_161_(param_621_0, param_621_1)
            vec_618 = param_621_0[0]
            vec_619 = param_621_1[0]

        vec_index618 = 0
        vec_index619 = 0
        vec_index633 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_633[:]
        vec_index633 = 0
        # Program VectorClear Region
        del vec_618[:]
        vec_index618 = 0
        # Program VectorClear Region
        del vec_619[:]
        vec_index619 = 0
        # Program Return Region
        return False
        return False

    def entrypoint_1(self, vec_641: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index641: int = 0
        vec_643: List[int] = list()
        vec_index643: int = 0
        vec_646: List[int] = list()
        vec_index646: int = 0
        vec_647: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index647: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index641 = 0
        while vec_index641 < len(vec_641):
            var_642 = vec_641[vec_index641]
            vec_index641 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_642 = var_642
            prev_state = self.table_51[tuple_642]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_51[tuple_642] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_643.append(var_642)
        # Program VectorUnique Region
        vec_643 = list(set(vec_643))
        vec_index643 = 0
        # Program TableJoin Region
        while vec_index643 < len(vec_643):
            var_645 = vec_643[vec_index643]
            vec_index643 += 1
            if var_645 in self.index_225:
                if var_645 in self.index_212:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_645 = var_645
                    prev_state = self.table_15[tuple_645]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_645] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_646.append(var_645)
        # Program VectorClear Region
        del vec_643[:]
        vec_index643 = 0
        # Induction Fixpoint Loop Region
        while len(vec_646) or len(vec_647):
            # Program Series Region
            # Program Call Region
            ret = self.proc_164_(vec_646, vec_647)

            # Program Call Region
            param_649_0 = [vec_646]
            param_649_1 = [vec_647]
            ret = self.proc_161_(param_649_0, param_649_1)
            vec_646 = param_649_0[0]
            vec_647 = param_649_1[0]

        vec_index646 = 0
        vec_index647 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_646[:]
        vec_index646 = 0
        # Program VectorClear Region
        del vec_647[:]
        vec_index647 = 0
        # Program Return Region
        return False
        return False

    def constructor_function_1(self, vec_651: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index651: int = 0
        vec_653: List[int] = list()
        vec_index653: int = 0
        vec_656: List[int] = list()
        vec_index656: int = 0
        vec_657: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index657: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index651 = 0
        while vec_index651 < len(vec_651):
            var_652 = vec_651[vec_index651]
            vec_index651 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_652 = var_652
            prev_state = self.table_63[tuple_652]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_63[tuple_652] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_653.append(var_652)
        # Program VectorUnique Region
        vec_653 = list(set(vec_653))
        vec_index653 = 0
        # Program TableJoin Region
        while vec_index653 < len(vec_653):
            var_655 = vec_653[vec_index653]
            vec_index653 += 1
            if var_655 in self.index_174:
                if var_655 in self.index_160:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_655 = var_655
                    prev_state = self.table_15[tuple_655]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_655] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_656.append(var_655)
        # Program VectorClear Region
        del vec_653[:]
        vec_index653 = 0
        # Induction Fixpoint Loop Region
        while len(vec_656) or len(vec_657):
            # Program Series Region
            # Program Call Region
            ret = self.proc_164_(vec_656, vec_657)

            # Program Call Region
            param_659_0 = [vec_656]
            param_659_1 = [vec_657]
            ret = self.proc_161_(param_659_0, param_659_1)
            vec_656 = param_659_0[0]
            vec_657 = param_659_1[0]

        vec_index656 = 0
        vec_index657 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_656[:]
        vec_index656 = 0
        # Program VectorClear Region
        del vec_657[:]
        vec_index657 = 0
        # Program Return Region
        return False
        return False

    def destructor_function_1(self, vec_661: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index661: int = 0
        vec_663: List[int] = list()
        vec_index663: int = 0
        vec_666: List[int] = list()
        vec_index666: int = 0
        vec_667: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index667: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index661 = 0
        while vec_index661 < len(vec_661):
            var_662 = vec_661[vec_index661]
            vec_index661 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_662 = var_662
            prev_state = self.table_67[tuple_662]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_67[tuple_662] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_663.append(var_662)
        # Program VectorUnique Region
        vec_663 = list(set(vec_663))
        vec_index663 = 0
        # Program TableJoin Region
        while vec_index663 < len(vec_663):
            var_665 = vec_663[vec_index663]
            vec_index663 += 1
            if var_665 in self.index_159:
                if var_665 in self.index_160:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_665 = var_665
                    prev_state = self.table_15[tuple_665]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_665] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_666.append(var_665)
        # Program VectorClear Region
        del vec_663[:]
        vec_index663 = 0
        # Induction Fixpoint Loop Region
        while len(vec_666) or len(vec_667):
            # Program Series Region
            # Program Call Region
            ret = self.proc_164_(vec_666, vec_667)

            # Program Call Region
            param_669_0 = [vec_666]
            param_669_1 = [vec_667]
            ret = self.proc_161_(param_669_0, param_669_1)
            vec_666 = param_669_0[0]
            vec_667 = param_669_1[0]

        vec_index666 = 0
        vec_index667 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_666[:]
        vec_index666 = 0
        # Program VectorClear Region
        del vec_667[:]
        vec_index667 = 0
        # Program Return Region
        return False
        return False

    def address_operand_2(self, vec_671: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index671: int = 0
        vec_674: List[int] = list()
        vec_index674: int = 0
        vec_678: List[int] = list()
        vec_index678: int = 0
        vec_682: List[int] = list()
        vec_index682: int = 0
        vec_686: List[int] = list()
        vec_index686: int = 0
        vec_690: List[int] = list()
        vec_index690: int = 0
        vec_695: List[int] = list()
        vec_index695: int = 0
        vec_700: List[int] = list()
        vec_index700: int = 0
        vec_705: List[int] = list()
        vec_index705: int = 0
        vec_710: List[int] = list()
        vec_index710: int = 0
        vec_714: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index714: int = 0
        vec_717: List[int] = list()
        vec_index717: int = 0
        vec_721: List[int] = list()
        vec_index721: int = 0
        vec_725: List[int] = list()
        vec_index725: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index671 = 0
        while vec_index671 < len(vec_671):
            var_672, var_673 = vec_671[vec_index671]
            vec_index671 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_672_673 = (var_672, var_673)
            prev_state = self.table_72[tuple_672_673]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_72[tuple_672_673] = 1 | 4
                if not present_bit:
                    self.index_179[tuple_672_673[0]].append(tuple_672_673[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_686.append(var_672)
                # Program VectorAppend Region
                vec_682.append(var_672)
                # Program VectorAppend Region
                vec_678.append(var_672)
                # Program VectorAppend Region
                vec_674.append(var_672)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_672_673 = (var_672, var_673)
            prev_state = self.table_72[tuple_672_673]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_72[tuple_672_673] = 1 | 4
                if not present_bit:
                    self.index_179[tuple_672_673[0]].append(tuple_672_673[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_686.append(var_672)
                # Program VectorAppend Region
                vec_682.append(var_672)
                # Program VectorAppend Region
                vec_678.append(var_672)
                # Program VectorAppend Region
                vec_674.append(var_672)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_672_673 = (var_672, var_673)
            prev_state = self.table_72[tuple_672_673]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_72[tuple_672_673] = 1 | 4
                if not present_bit:
                    self.index_179[tuple_672_673[0]].append(tuple_672_673[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_686.append(var_672)
                # Program VectorAppend Region
                vec_682.append(var_672)
                # Program VectorAppend Region
                vec_678.append(var_672)
                # Program VectorAppend Region
                vec_674.append(var_672)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_672_673 = (var_672, var_673)
            prev_state = self.table_72[tuple_672_673]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_72[tuple_672_673] = 1 | 4
                if not present_bit:
                    self.index_179[tuple_672_673[0]].append(tuple_672_673[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_686.append(var_672)
                # Program VectorAppend Region
                vec_682.append(var_672)
                # Program VectorAppend Region
                vec_678.append(var_672)
                # Program VectorAppend Region
                vec_674.append(var_672)
        # Program VectorUnique Region
        vec_674 = list(set(vec_674))
        vec_index674 = 0
        # Program TableJoin Region
        while vec_index674 < len(vec_674):
            var_676 = vec_674[vec_index674]
            vec_index674 += 1
            if var_676 in self.index_178:
                tuple_675_1_index: int = 0
                tuple_675_1_vec: List[int] = self.index_179[var_676]
                while tuple_675_1_index < len(tuple_675_1_vec):
                    tuple_675_1 = tuple_675_1_vec[tuple_675_1_index]
                    tuple_675_1_index += 1
                    var_677 = tuple_675_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_676_677 = (var_676, var_677)
                    prev_state = self.table_102[tuple_676_677]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_102[tuple_676_677] = 1 | 4
                        if not present_bit:
                            self.index_242[tuple_676_677[1]].append(tuple_676_677[0])
                        # Program VectorAppend Region
                        vec_700.append(var_677)
        # Program VectorClear Region
        del vec_674[:]
        vec_index674 = 0
        # Program VectorUnique Region
        vec_678 = list(set(vec_678))
        vec_index678 = 0
        # Program TableJoin Region
        while vec_index678 < len(vec_678):
            var_680 = vec_678[vec_index678]
            vec_index678 += 1
            if var_680 in self.index_184:
                tuple_679_1_index: int = 0
                tuple_679_1_vec: List[int] = self.index_179[var_680]
                while tuple_679_1_index < len(tuple_679_1_vec):
                    tuple_679_1 = tuple_679_1_vec[tuple_679_1_index]
                    tuple_679_1_index += 1
                    var_681 = tuple_679_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_680_681 = (var_680, var_681)
                    prev_state = self.table_94[tuple_680_681]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_94[tuple_680_681] = 1 | 4
                        if not present_bit:
                            self.index_236[tuple_680_681[1]].append(tuple_680_681[0])
                        # Program VectorAppend Region
                        vec_695.append(var_681)
        # Program VectorClear Region
        del vec_678[:]
        vec_index678 = 0
        # Program VectorUnique Region
        vec_682 = list(set(vec_682))
        vec_index682 = 0
        # Program TableJoin Region
        while vec_index682 < len(vec_682):
            var_684 = vec_682[vec_index682]
            vec_index682 += 1
            if var_684 in self.index_189:
                tuple_683_1_index: int = 0
                tuple_683_1_vec: List[int] = self.index_179[var_684]
                while tuple_683_1_index < len(tuple_683_1_vec):
                    tuple_683_1 = tuple_683_1_vec[tuple_683_1_index]
                    tuple_683_1_index += 1
                    var_685 = tuple_683_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_684_685 = (var_684, var_685)
                    prev_state = self.table_86[tuple_684_685]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_86[tuple_684_685] = 1 | 4
                        if not present_bit:
                            self.index_230[tuple_684_685[1]].append(tuple_684_685[0])
                        # Program VectorAppend Region
                        vec_690.append(var_685)
        # Program VectorClear Region
        del vec_682[:]
        vec_index682 = 0
        # Program VectorUnique Region
        vec_686 = list(set(vec_686))
        vec_index686 = 0
        # Program TableJoin Region
        while vec_index686 < len(vec_686):
            var_688 = vec_686[vec_index686]
            vec_index686 += 1
            if var_688 in self.index_194:
                tuple_687_1_index: int = 0
                tuple_687_1_vec: List[int] = self.index_179[var_688]
                while tuple_687_1_index < len(tuple_687_1_vec):
                    tuple_687_1 = tuple_687_1_vec[tuple_687_1_index]
                    tuple_687_1_index += 1
                    var_689 = tuple_687_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_688_689 = (var_688, var_689)
                    prev_state = self.table_78[tuple_688_689]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_78[tuple_688_689] = 1 | 4
                        if not present_bit:
                            self.index_269[tuple_688_689[1]].append(tuple_688_689[0])
                        # Program VectorAppend Region
                        vec_705.append(var_689)
        # Program VectorClear Region
        del vec_686[:]
        vec_index686 = 0
        # Program VectorUnique Region
        vec_690 = list(set(vec_690))
        vec_index690 = 0
        # Program TableJoin Region
        while vec_index690 < len(vec_690):
            var_692 = vec_690[vec_index690]
            vec_index690 += 1
            tuple_691_0_index: int = 0
            tuple_691_0_vec: List[int] = self.index_229[var_692]
            while tuple_691_0_index < len(tuple_691_0_vec):
                tuple_691_0 = tuple_691_0_vec[tuple_691_0_index]
                tuple_691_0_index += 1
                var_693 = tuple_691_0
                tuple_691_1_index: int = 0
                tuple_691_1_vec: List[int] = self.index_230[var_692]
                while tuple_691_1_index < len(tuple_691_1_vec):
                    tuple_691_1 = tuple_691_1_vec[tuple_691_1_index]
                    tuple_691_1_index += 1
                    var_694 = tuple_691_1
                    # Program TransitionState Region
                    tuple_693_694 = (var_693, var_694)
                    prev_state = self.table_89[tuple_693_694]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_89[tuple_693_694] = 1 | 4
                        if not present_bit:
                            self.index_295[tuple_693_694[0]].append(tuple_693_694[1])
                        # Program VectorAppend Region
                        vec_721.append(var_693)
        # Program VectorClear Region
        del vec_690[:]
        vec_index690 = 0
        # Program VectorUnique Region
        vec_695 = list(set(vec_695))
        vec_index695 = 0
        # Program TableJoin Region
        while vec_index695 < len(vec_695):
            var_697 = vec_695[vec_index695]
            vec_index695 += 1
            tuple_696_0_index: int = 0
            tuple_696_0_vec: List[int] = self.index_229[var_697]
            while tuple_696_0_index < len(tuple_696_0_vec):
                tuple_696_0 = tuple_696_0_vec[tuple_696_0_index]
                tuple_696_0_index += 1
                var_698 = tuple_696_0
                tuple_696_1_index: int = 0
                tuple_696_1_vec: List[int] = self.index_236[var_697]
                while tuple_696_1_index < len(tuple_696_1_vec):
                    tuple_696_1 = tuple_696_1_vec[tuple_696_1_index]
                    tuple_696_1_index += 1
                    var_699 = tuple_696_1
                    # Program TransitionState Region
                    tuple_698_699 = (var_698, var_699)
                    prev_state = self.table_97[tuple_698_699]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_698_699] = 1 | 4
                        if not present_bit:
                            self.index_290[tuple_698_699[0]].append(tuple_698_699[1])
                        # Program VectorAppend Region
                        vec_717.append(var_698)
        # Program VectorClear Region
        del vec_695[:]
        vec_index695 = 0
        # Program VectorUnique Region
        vec_700 = list(set(vec_700))
        vec_index700 = 0
        # Program TableJoin Region
        while vec_index700 < len(vec_700):
            var_702 = vec_700[vec_index700]
            vec_index700 += 1
            tuple_701_0_index: int = 0
            tuple_701_0_vec: List[int] = self.index_229[var_702]
            while tuple_701_0_index < len(tuple_701_0_vec):
                tuple_701_0 = tuple_701_0_vec[tuple_701_0_index]
                tuple_701_0_index += 1
                var_703 = tuple_701_0
                tuple_701_1_index: int = 0
                tuple_701_1_vec: List[int] = self.index_242[var_702]
                while tuple_701_1_index < len(tuple_701_1_vec):
                    tuple_701_1 = tuple_701_1_vec[tuple_701_1_index]
                    tuple_701_1_index += 1
                    var_704 = tuple_701_1
                    # Program TransitionState Region
                    tuple_703_704 = (var_703, var_704)
                    prev_state = self.table_105[tuple_703_704]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_703_704] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_703_704[0]].append(tuple_703_704[1])
                        # Program VectorAppend Region
                        vec_710.append(var_703)
        # Program VectorClear Region
        del vec_700[:]
        vec_index700 = 0
        # Program VectorUnique Region
        vec_705 = list(set(vec_705))
        vec_index705 = 0
        # Program TableJoin Region
        while vec_index705 < len(vec_705):
            var_707 = vec_705[vec_index705]
            vec_index705 += 1
            tuple_706_0_index: int = 0
            tuple_706_0_vec: List[int] = self.index_229[var_707]
            while tuple_706_0_index < len(tuple_706_0_vec):
                tuple_706_0 = tuple_706_0_vec[tuple_706_0_index]
                tuple_706_0_index += 1
                var_708 = tuple_706_0
                tuple_706_1_index: int = 0
                tuple_706_1_vec: List[int] = self.index_269[var_707]
                while tuple_706_1_index < len(tuple_706_1_vec):
                    tuple_706_1 = tuple_706_1_vec[tuple_706_1_index]
                    tuple_706_1_index += 1
                    var_709 = tuple_706_1
                    # Program TransitionState Region
                    tuple_708_709 = (var_708, var_709)
                    prev_state = self.table_81[tuple_708_709]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_81[tuple_708_709] = 1 | 4
                        if not present_bit:
                            self.index_300[tuple_708_709[0]].append(tuple_708_709[1])
                        # Program VectorAppend Region
                        vec_725.append(var_708)
        # Program VectorClear Region
        del vec_705[:]
        vec_index705 = 0
        # Program VectorUnique Region
        vec_710 = list(set(vec_710))
        vec_index710 = 0
        # Program TableJoin Region
        while vec_index710 < len(vec_710):
            var_712 = vec_710[vec_index710]
            vec_index710 += 1
            if var_712 in self.index_212:
                tuple_711_1_index: int = 0
                tuple_711_1_vec: List[int] = self.index_285[var_712]
                while tuple_711_1_index < len(tuple_711_1_vec):
                    tuple_711_1 = tuple_711_1_vec[tuple_711_1_index]
                    tuple_711_1_index += 1
                    var_713 = tuple_711_1
                    # Program TransitionState Region
                    tuple_713_712_0 = (var_713, var_712, self.var_0)
                    prev_state = self.table_11[tuple_713_712_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_713_712_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_713_712_0[1], tuple_713_712_0[2])].append(tuple_713_712_0[0])
                        # Program VectorAppend Region
                        vec_714.append((var_713, var_712, self.var_0))
        # Program VectorClear Region
        del vec_710[:]
        vec_index710 = 0
        # Program VectorUnique Region
        vec_717 = list(set(vec_717))
        vec_index717 = 0
        # Program TableJoin Region
        while vec_index717 < len(vec_717):
            var_719 = vec_717[vec_index717]
            vec_index717 += 1
            if var_719 in self.index_212:
                tuple_718_1_index: int = 0
                tuple_718_1_vec: List[int] = self.index_290[var_719]
                while tuple_718_1_index < len(tuple_718_1_vec):
                    tuple_718_1 = tuple_718_1_vec[tuple_718_1_index]
                    tuple_718_1_index += 1
                    var_720 = tuple_718_1
                    # Program TransitionState Region
                    tuple_720_719_0 = (var_720, var_719, self.var_0)
                    prev_state = self.table_11[tuple_720_719_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_720_719_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_720_719_0[1], tuple_720_719_0[2])].append(tuple_720_719_0[0])
                        # Program VectorAppend Region
                        vec_714.append((var_720, var_719, self.var_0))
        # Program VectorClear Region
        del vec_717[:]
        vec_index717 = 0
        # Program VectorUnique Region
        vec_721 = list(set(vec_721))
        vec_index721 = 0
        # Program TableJoin Region
        while vec_index721 < len(vec_721):
            var_723 = vec_721[vec_index721]
            vec_index721 += 1
            if var_723 in self.index_212:
                tuple_722_1_index: int = 0
                tuple_722_1_vec: List[int] = self.index_295[var_723]
                while tuple_722_1_index < len(tuple_722_1_vec):
                    tuple_722_1 = tuple_722_1_vec[tuple_722_1_index]
                    tuple_722_1_index += 1
                    var_724 = tuple_722_1
                    # Program TransitionState Region
                    tuple_724_723_2 = (var_724, var_723, self.var_2)
                    prev_state = self.table_11[tuple_724_723_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_724_723_2] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_724_723_2[1], tuple_724_723_2[2])].append(tuple_724_723_2[0])
                        # Program VectorAppend Region
                        vec_714.append((var_724, var_723, self.var_2))
        # Program VectorClear Region
        del vec_721[:]
        vec_index721 = 0
        # Program VectorUnique Region
        vec_725 = list(set(vec_725))
        vec_index725 = 0
        # Program TableJoin Region
        while vec_index725 < len(vec_725):
            var_727 = vec_725[vec_index725]
            vec_index725 += 1
            if var_727 in self.index_212:
                tuple_726_1_index: int = 0
                tuple_726_1_vec: List[int] = self.index_300[var_727]
                while tuple_726_1_index < len(tuple_726_1_vec):
                    tuple_726_1 = tuple_726_1_vec[tuple_726_1_index]
                    tuple_726_1_index += 1
                    var_728 = tuple_726_1
                    # Program TransitionState Region
                    tuple_728_727_2 = (var_728, var_727, self.var_2)
                    prev_state = self.table_11[tuple_728_727_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_728_727_2] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_728_727_2[1], tuple_728_727_2[2])].append(tuple_728_727_2[0])
                        # Program VectorAppend Region
                        vec_714.append((var_728, var_727, self.var_2))
        # Program VectorClear Region
        del vec_725[:]
        vec_index725 = 0
        # Induction Fixpoint Loop Region
        while len(vec_714):
            # Program Series Region
            # Program Call Region
            ret = self.proc_217_(vec_714)

            # Program Call Region
            param_716_0 = [vec_714]
            ret = self.proc_215_(param_716_0)
            vec_714 = param_716_0[0]

        vec_index714 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_714[:]
        vec_index714 = 0
        # Program Return Region
        return False
        return False

    def relocation_2(self, vec_730: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index730: int = 0
        vec_733: List[int] = list()
        vec_index733: int = 0
        vec_738: List[int] = list()
        vec_index738: int = 0
        vec_743: List[int] = list()
        vec_index743: int = 0
        vec_748: List[int] = list()
        vec_index748: int = 0
        vec_753: List[int] = list()
        vec_index753: int = 0
        vec_757: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index757: int = 0
        vec_760: List[int] = list()
        vec_index760: int = 0
        vec_764: List[int] = list()
        vec_index764: int = 0
        vec_768: List[int] = list()
        vec_index768: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index730 = 0
        while vec_index730 < len(vec_730):
            var_731, var_732 = vec_730[vec_index730]
            vec_index730 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_731_732 = (var_731, var_732)
            prev_state = self.table_75[tuple_731_732]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_75[tuple_731_732] = 1 | 4
                if not present_bit:
                    self.index_229[tuple_731_732[0]].append(tuple_731_732[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_748.append(var_731)
                # Program VectorAppend Region
                vec_743.append(var_731)
                # Program VectorAppend Region
                vec_738.append(var_731)
                # Program VectorAppend Region
                vec_733.append(var_731)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_731_732 = (var_731, var_732)
            prev_state = self.table_75[tuple_731_732]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_75[tuple_731_732] = 1 | 4
                if not present_bit:
                    self.index_229[tuple_731_732[0]].append(tuple_731_732[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_748.append(var_731)
                # Program VectorAppend Region
                vec_743.append(var_731)
                # Program VectorAppend Region
                vec_738.append(var_731)
                # Program VectorAppend Region
                vec_733.append(var_731)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_731_732 = (var_731, var_732)
            prev_state = self.table_75[tuple_731_732]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_75[tuple_731_732] = 1 | 4
                if not present_bit:
                    self.index_229[tuple_731_732[0]].append(tuple_731_732[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_748.append(var_731)
                # Program VectorAppend Region
                vec_743.append(var_731)
                # Program VectorAppend Region
                vec_738.append(var_731)
                # Program VectorAppend Region
                vec_733.append(var_731)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_731_732 = (var_731, var_732)
            prev_state = self.table_75[tuple_731_732]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_75[tuple_731_732] = 1 | 4
                if not present_bit:
                    self.index_229[tuple_731_732[0]].append(tuple_731_732[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_748.append(var_731)
                # Program VectorAppend Region
                vec_743.append(var_731)
                # Program VectorAppend Region
                vec_738.append(var_731)
                # Program VectorAppend Region
                vec_733.append(var_731)
        # Program VectorUnique Region
        vec_733 = list(set(vec_733))
        vec_index733 = 0
        # Program TableJoin Region
        while vec_index733 < len(vec_733):
            var_735 = vec_733[vec_index733]
            vec_index733 += 1
            tuple_734_0_index: int = 0
            tuple_734_0_vec: List[int] = self.index_229[var_735]
            while tuple_734_0_index < len(tuple_734_0_vec):
                tuple_734_0 = tuple_734_0_vec[tuple_734_0_index]
                tuple_734_0_index += 1
                var_736 = tuple_734_0
                tuple_734_1_index: int = 0
                tuple_734_1_vec: List[int] = self.index_242[var_735]
                while tuple_734_1_index < len(tuple_734_1_vec):
                    tuple_734_1 = tuple_734_1_vec[tuple_734_1_index]
                    tuple_734_1_index += 1
                    var_737 = tuple_734_1
                    # Program TransitionState Region
                    tuple_736_737 = (var_736, var_737)
                    prev_state = self.table_105[tuple_736_737]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_105[tuple_736_737] = 1 | 4
                        if not present_bit:
                            self.index_285[tuple_736_737[0]].append(tuple_736_737[1])
                        # Program VectorAppend Region
                        vec_764.append(var_736)
        # Program VectorClear Region
        del vec_733[:]
        vec_index733 = 0
        # Program VectorUnique Region
        vec_738 = list(set(vec_738))
        vec_index738 = 0
        # Program TableJoin Region
        while vec_index738 < len(vec_738):
            var_740 = vec_738[vec_index738]
            vec_index738 += 1
            tuple_739_0_index: int = 0
            tuple_739_0_vec: List[int] = self.index_229[var_740]
            while tuple_739_0_index < len(tuple_739_0_vec):
                tuple_739_0 = tuple_739_0_vec[tuple_739_0_index]
                tuple_739_0_index += 1
                var_741 = tuple_739_0
                tuple_739_1_index: int = 0
                tuple_739_1_vec: List[int] = self.index_236[var_740]
                while tuple_739_1_index < len(tuple_739_1_vec):
                    tuple_739_1 = tuple_739_1_vec[tuple_739_1_index]
                    tuple_739_1_index += 1
                    var_742 = tuple_739_1
                    # Program TransitionState Region
                    tuple_741_742 = (var_741, var_742)
                    prev_state = self.table_97[tuple_741_742]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_97[tuple_741_742] = 1 | 4
                        if not present_bit:
                            self.index_290[tuple_741_742[0]].append(tuple_741_742[1])
                        # Program VectorAppend Region
                        vec_760.append(var_741)
        # Program VectorClear Region
        del vec_738[:]
        vec_index738 = 0
        # Program VectorUnique Region
        vec_743 = list(set(vec_743))
        vec_index743 = 0
        # Program TableJoin Region
        while vec_index743 < len(vec_743):
            var_745 = vec_743[vec_index743]
            vec_index743 += 1
            tuple_744_0_index: int = 0
            tuple_744_0_vec: List[int] = self.index_229[var_745]
            while tuple_744_0_index < len(tuple_744_0_vec):
                tuple_744_0 = tuple_744_0_vec[tuple_744_0_index]
                tuple_744_0_index += 1
                var_746 = tuple_744_0
                tuple_744_1_index: int = 0
                tuple_744_1_vec: List[int] = self.index_230[var_745]
                while tuple_744_1_index < len(tuple_744_1_vec):
                    tuple_744_1 = tuple_744_1_vec[tuple_744_1_index]
                    tuple_744_1_index += 1
                    var_747 = tuple_744_1
                    # Program TransitionState Region
                    tuple_746_747 = (var_746, var_747)
                    prev_state = self.table_89[tuple_746_747]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_89[tuple_746_747] = 1 | 4
                        if not present_bit:
                            self.index_295[tuple_746_747[0]].append(tuple_746_747[1])
                        # Program VectorAppend Region
                        vec_753.append(var_746)
        # Program VectorClear Region
        del vec_743[:]
        vec_index743 = 0
        # Program VectorUnique Region
        vec_748 = list(set(vec_748))
        vec_index748 = 0
        # Program TableJoin Region
        while vec_index748 < len(vec_748):
            var_750 = vec_748[vec_index748]
            vec_index748 += 1
            tuple_749_0_index: int = 0
            tuple_749_0_vec: List[int] = self.index_229[var_750]
            while tuple_749_0_index < len(tuple_749_0_vec):
                tuple_749_0 = tuple_749_0_vec[tuple_749_0_index]
                tuple_749_0_index += 1
                var_751 = tuple_749_0
                tuple_749_1_index: int = 0
                tuple_749_1_vec: List[int] = self.index_269[var_750]
                while tuple_749_1_index < len(tuple_749_1_vec):
                    tuple_749_1 = tuple_749_1_vec[tuple_749_1_index]
                    tuple_749_1_index += 1
                    var_752 = tuple_749_1
                    # Program TransitionState Region
                    tuple_751_752 = (var_751, var_752)
                    prev_state = self.table_81[tuple_751_752]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_81[tuple_751_752] = 1 | 4
                        if not present_bit:
                            self.index_300[tuple_751_752[0]].append(tuple_751_752[1])
                        # Program VectorAppend Region
                        vec_768.append(var_751)
        # Program VectorClear Region
        del vec_748[:]
        vec_index748 = 0
        # Program VectorUnique Region
        vec_753 = list(set(vec_753))
        vec_index753 = 0
        # Program TableJoin Region
        while vec_index753 < len(vec_753):
            var_755 = vec_753[vec_index753]
            vec_index753 += 1
            if var_755 in self.index_212:
                tuple_754_1_index: int = 0
                tuple_754_1_vec: List[int] = self.index_295[var_755]
                while tuple_754_1_index < len(tuple_754_1_vec):
                    tuple_754_1 = tuple_754_1_vec[tuple_754_1_index]
                    tuple_754_1_index += 1
                    var_756 = tuple_754_1
                    # Program TransitionState Region
                    tuple_756_755_2 = (var_756, var_755, self.var_2)
                    prev_state = self.table_11[tuple_756_755_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_756_755_2] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_756_755_2[1], tuple_756_755_2[2])].append(tuple_756_755_2[0])
                        # Program VectorAppend Region
                        vec_757.append((var_756, var_755, self.var_2))
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
            if var_762 in self.index_212:
                tuple_761_1_index: int = 0
                tuple_761_1_vec: List[int] = self.index_290[var_762]
                while tuple_761_1_index < len(tuple_761_1_vec):
                    tuple_761_1 = tuple_761_1_vec[tuple_761_1_index]
                    tuple_761_1_index += 1
                    var_763 = tuple_761_1
                    # Program TransitionState Region
                    tuple_763_762_0 = (var_763, var_762, self.var_0)
                    prev_state = self.table_11[tuple_763_762_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_763_762_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_763_762_0[1], tuple_763_762_0[2])].append(tuple_763_762_0[0])
                        # Program VectorAppend Region
                        vec_757.append((var_763, var_762, self.var_0))
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
            if var_766 in self.index_212:
                tuple_765_1_index: int = 0
                tuple_765_1_vec: List[int] = self.index_285[var_766]
                while tuple_765_1_index < len(tuple_765_1_vec):
                    tuple_765_1 = tuple_765_1_vec[tuple_765_1_index]
                    tuple_765_1_index += 1
                    var_767 = tuple_765_1
                    # Program TransitionState Region
                    tuple_767_766_0 = (var_767, var_766, self.var_0)
                    prev_state = self.table_11[tuple_767_766_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_767_766_0] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_767_766_0[1], tuple_767_766_0[2])].append(tuple_767_766_0[0])
                        # Program VectorAppend Region
                        vec_757.append((var_767, var_766, self.var_0))
        # Program VectorClear Region
        del vec_764[:]
        vec_index764 = 0
        # Program VectorUnique Region
        vec_768 = list(set(vec_768))
        vec_index768 = 0
        # Program TableJoin Region
        while vec_index768 < len(vec_768):
            var_770 = vec_768[vec_index768]
            vec_index768 += 1
            if var_770 in self.index_212:
                tuple_769_1_index: int = 0
                tuple_769_1_vec: List[int] = self.index_300[var_770]
                while tuple_769_1_index < len(tuple_769_1_vec):
                    tuple_769_1 = tuple_769_1_vec[tuple_769_1_index]
                    tuple_769_1_index += 1
                    var_771 = tuple_769_1
                    # Program TransitionState Region
                    tuple_771_770_2 = (var_771, var_770, self.var_2)
                    prev_state = self.table_11[tuple_771_770_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_771_770_2] = 1 | 4
                        if not present_bit:
                            self.index_1372[(tuple_771_770_2[1], tuple_771_770_2[2])].append(tuple_771_770_2[0])
                        # Program VectorAppend Region
                        vec_757.append((var_771, var_770, self.var_2))
        # Program VectorClear Region
        del vec_768[:]
        vec_index768 = 0
        # Induction Fixpoint Loop Region
        while len(vec_757):
            # Program Series Region
            # Program Call Region
            ret = self.proc_217_(vec_757)

            # Program Call Region
            param_759_0 = [vec_757]
            ret = self.proc_215_(param_759_0)
            vec_757 = param_759_0[0]

        vec_index757 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_757[:]
        vec_index757 = 0
        # Program Return Region
        return False
        return False

    def proc_772_(self, var_773: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_26[var_773] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_773 = var_773
            prev_state = self.table_26[tuple_773]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_26[tuple_773] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker::call_pred
                ret = self.proc_963_(var_773)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_773 = var_773
                    prev_state = self.table_26[tuple_773]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_26[tuple_773] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_775_(self, var_776: int, var_777: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_28[(var_776, var_777)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_776_777 = (var_776, var_777)
            prev_state = self.table_28[tuple_776_777]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_28[tuple_776_777] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker::call_pred
                ret = self.proc_944_(var_777, var_776)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_776_777 = (var_776, var_777)
                    prev_state = self.table_28[tuple_776_777]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_28[tuple_776_777] = 1 | 4
                        if not present_bit:
                            self.index_774[tuple_776_777[0]].append(tuple_776_777[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_778_(self, var_779: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_937_(var_779)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_781_(self, var_782: int, var_783: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_798_(var_782, var_783)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_785_(self, var_786: int, var_787: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_33[(var_786, var_787)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_786_787 = (var_786, var_787)
            prev_state = self.table_33[tuple_786_787]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_33[tuple_786_787] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker::call_pred
                ret = self.proc_788_(var_787, var_786)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_786_787 = (var_786, var_787)
                    prev_state = self.table_33[tuple_786_787]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_33[tuple_786_787] = 1 | 4
                        if not present_bit:
                            self.index_784[tuple_786_787[0]].append(tuple_786_787[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_788_(self, var_789: int, var_790: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_792: List[int] = list()
        vec_index792: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_792.append(var_789)
        # Program VectorUnique Region
        vec_792 = list(set(vec_792))
        vec_index792 = 0
        # Program TableJoin Region
        while vec_index792 < len(vec_792):
            var_794 = vec_792[vec_index792]
            vec_index792 += 1
            tuple_793_0_index: int = 0
            tuple_793_0_vec: List[int] = self.index_400[var_794]
            while tuple_793_0_index < len(tuple_793_0_vec):
                tuple_793_0 = tuple_793_0_vec[tuple_793_0_index]
                tuple_793_0_index += 1
                var_795 = tuple_793_0
                if var_794 in self.index_253:
                    # Program TupleCompare Region
                    if var_790 == var_795:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_402_(var_795, var_794)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_256_(var_794)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_792[:]
        vec_index792 = 0
        # Program Return Region
        return False
        return False

    def proc_798_(self, var_799: int, var_800: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_17[(var_799, var_800)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_799_800 = (var_799, var_800)
            prev_state = self.table_17[tuple_799_800]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_17[tuple_799_800] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_802_(var_799, var_800)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_799_800 = (var_799, var_800)
                    prev_state = self.table_17[tuple_799_800]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_799_800] = 1 | 4
                        if not present_bit:
                            self.index_521[tuple_799_800[1]].append(tuple_799_800[0])
                            self.index_780[tuple_799_800[0]].append(tuple_799_800[1])
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_806_(var_799, var_800)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_799_800 = (var_799, var_800)
                    prev_state = self.table_17[tuple_799_800]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_799_800] = 1 | 4
                        if not present_bit:
                            self.index_521[tuple_799_800[1]].append(tuple_799_800[0])
                            self.index_780[tuple_799_800[0]].append(tuple_799_800[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_802_(self, var_803: int, var_804: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_824_(var_804)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_806_(self, var_807: int, var_808: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_810_(var_807, var_808)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_810_(self, var_811: int, var_812: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_814: List[int] = list()
        vec_index814: int = 0
        vec_816: List[int] = list()
        vec_index816: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_816: int
        scan_index_816: int = 0
        scan_tuple_816_vec: List[int] = self.index_815[var_812]
        while scan_index_816 < len(scan_tuple_816_vec):
            scan_tuple_816 = scan_tuple_816_vec[scan_index_816]
            scan_index_816 += 1
            vec_816.append(scan_tuple_816)
        # Program VectorLoop Region
        vec_index816 = 0
        while vec_index816 < len(vec_816):
            var_817 = vec_816[vec_index816]
            vec_index816 += 1
            # Program VectorAppend Region
            vec_814.append(var_817)
        # Program VectorUnique Region
        vec_814 = list(set(vec_814))
        vec_index814 = 0
        # Program TableJoin Region
        while vec_index814 < len(vec_814):
            var_819 = vec_814[vec_index814]
            vec_index814 += 1
            tuple_818_0_index: int = 0
            tuple_818_0_vec: List[int] = self.index_521[var_819]
            while tuple_818_0_index < len(tuple_818_0_vec):
                tuple_818_0 = tuple_818_0_vec[tuple_818_0_index]
                tuple_818_0_index += 1
                var_820 = tuple_818_0
                tuple_818_1_index: int = 0
                tuple_818_1_vec: List[int] = self.index_522[var_819]
                while tuple_818_1_index < len(tuple_818_1_vec):
                    tuple_818_1 = tuple_818_1_vec[tuple_818_1_index]
                    tuple_818_1_index += 1
                    var_821 = tuple_818_1
                    # Program TupleCompare Region
                    if (var_811, var_812, ) == (var_820, var_821, ):
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_525_(var_820, var_819)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_490_(var_819, var_821)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_814[:]
        vec_index814 = 0
        # Program Return Region
        return False
        return False

    def proc_824_(self, var_825: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_825] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_825 = var_825
            prev_state = self.table_15[tuple_825]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_825] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_827_(var_825)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_825 = var_825
                    prev_state = self.table_15[tuple_825]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_825] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_830_(var_825)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_825 = var_825
                    prev_state = self.table_15[tuple_825]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_825] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_827_(self, var_828: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_934: List[int] = list()
        vec_index934: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_934.append(var_828)
        # Program VectorUnique Region
        vec_934 = list(set(vec_934))
        vec_index934 = 0
        # Program TableJoin Region
        while vec_index934 < len(vec_934):
            var_936 = vec_934[vec_index934]
            vec_index934 += 1
            if var_936 in self.index_225:
                if var_936 in self.index_212:
                    # Program Return Region
                    return True
        # Program VectorClear Region
        del vec_934[:]
        vec_index934 = 0
        # Program Return Region
        return False
        return False

    def proc_830_(self, var_831: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_839_(var_831)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_839_(self, var_840: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Parallel Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Union.cpp: BuildTopDownUnionChecker::call_preds
        ret = self.proc_842_(var_840)
        if ret:
            # Program Return Region
            return True
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Union.cpp: BuildTopDownUnionChecker::call_preds
        ret = self.proc_845_(var_840)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_842_(self, var_843: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_860_(self.var_0, var_843)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_845_(self, var_846: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_848_(var_846)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_848_(self, var_849: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_851: List[int] = list()
        vec_index851: int = 0
        vec_853: List[int] = list()
        vec_index853: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_853: int
        scan_index_853: int = 0
        scan_tuple_853_vec: List[int] = self.index_852[var_849]
        while scan_index_853 < len(scan_tuple_853_vec):
            scan_tuple_853 = scan_tuple_853_vec[scan_index_853]
            scan_index_853 += 1
            vec_853.append(scan_tuple_853)
        # Program VectorLoop Region
        vec_index853 = 0
        while vec_index853 < len(vec_853):
            var_854 = vec_853[vec_index853]
            vec_index853 += 1
            # Program VectorAppend Region
            vec_851.append(var_854)
        # Program VectorUnique Region
        vec_851 = list(set(vec_851))
        vec_index851 = 0
        # Program TableJoin Region
        while vec_index851 < len(vec_851):
            var_856 = vec_851[vec_index851]
            vec_index851 += 1
            if var_856 in self.index_253:
                tuple_855_1_index: int = 0
                tuple_855_1_vec: List[int] = self.index_254[var_856]
                while tuple_855_1_index < len(tuple_855_1_vec):
                    tuple_855_1 = tuple_855_1_vec[tuple_855_1_index]
                    tuple_855_1_index += 1
                    var_857 = tuple_855_1
                    # Program TupleCompare Region
                    if var_849 == var_857:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_256_(var_856)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_259_(var_857, var_856)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_851[:]
        vec_index851 = 0
        # Program Return Region
        return False
        return False

    def proc_860_(self, var_861: ControlFlowEdgeKind, var_862: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_865: List[int] = list()
        vec_index865: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_865: int
        scan_index_865: int = 0
        scan_tuple_865_vec: List[int] = self.index_864[var_862, self.var_0]
        while scan_index_865 < len(scan_tuple_865_vec):
            scan_tuple_865 = scan_tuple_865_vec[scan_index_865]
            scan_index_865 += 1
            vec_865.append(scan_tuple_865)
        # Program VectorLoop Region
        vec_index865 = 0
        while vec_index865 < len(vec_865):
            var_866 = vec_865[vec_index865]
            vec_index865 += 1
            # Program Call Region
            ret = self.proc_867_(var_862, self.var_0)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_867_(self, var_868: int, var_869: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_871: List[int] = list()
        vec_index871: int = 0
        # Program Series Region
        # Program TableScan Region
        var_869 = self._resolve_edgetype(var_869)
        scan_tuple_871: int
        scan_index_871: int = 0
        scan_tuple_871_vec: List[int] = self.index_864[var_868, var_869]
        while scan_index_871 < len(scan_tuple_871_vec):
            scan_tuple_871 = scan_tuple_871_vec[scan_index_871]
            scan_index_871 += 1
            vec_871.append(scan_tuple_871)
        # Program VectorLoop Region
        vec_index871 = 0
        while vec_index871 < len(vec_871):
            var_872 = vec_871[vec_index871]
            vec_index871 += 1
            # Program CheckState Region
            state = self.table_20[(var_872, var_868, var_869)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_869 = self._resolve_edgetype(var_869)
                tuple_872_868_869 = (var_872, var_868, var_869)
                prev_state = self.table_20[tuple_872_868_869]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_872_868_869] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_873_(var_872, var_868, var_869)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_869 = self._resolve_edgetype(var_869)
                        tuple_872_868_869 = (var_872, var_868, var_869)
                        prev_state = self.table_20[tuple_872_868_869]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_872_868_869] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_872_868_869[1], tuple_872_868_869[2])].append(tuple_872_868_869[0])
                                self.index_956[(tuple_872_868_869[0], tuple_872_868_869[1])].append(tuple_872_868_869[2])
                                self.index_1381[tuple_872_868_869[1]].append((tuple_872_868_869[0], tuple_872_868_869[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_883_(var_872, var_868, var_869)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_869 = self._resolve_edgetype(var_869)
                        tuple_872_868_869 = (var_872, var_868, var_869)
                        prev_state = self.table_20[tuple_872_868_869]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_872_868_869] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_872_868_869[1], tuple_872_868_869[2])].append(tuple_872_868_869[0])
                                self.index_956[(tuple_872_868_869[0], tuple_872_868_869[1])].append(tuple_872_868_869[2])
                                self.index_1381[tuple_872_868_869[1]].append((tuple_872_868_869[0], tuple_872_868_869[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_888_(var_872, var_868, var_869)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_869 = self._resolve_edgetype(var_869)
                        tuple_872_868_869 = (var_872, var_868, var_869)
                        prev_state = self.table_20[tuple_872_868_869]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_872_868_869] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_872_868_869[1], tuple_872_868_869[2])].append(tuple_872_868_869[0])
                                self.index_956[(tuple_872_868_869[0], tuple_872_868_869[1])].append(tuple_872_868_869[2])
                                self.index_1381[tuple_872_868_869[1]].append((tuple_872_868_869[0], tuple_872_868_869[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_873_(self, var_874: int, var_875: int, var_876: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_920_(var_875, var_874)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_883_(self, var_884: int, var_885: int, var_886: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_911_(var_885, var_884)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_888_(self, var_889: int, var_890: int, var_891: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_893_(var_890, var_889)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_893_(self, var_894: int, var_895: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_41[(var_894, var_895)] & 3
        if state == 1:
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_256_(var_894)
            if not ret:
                # Program Return Region
                return True
            # Program TransitionState Region
            tuple_894_895 = (var_894, var_895)
            prev_state = self.table_41[tuple_894_895]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 1:
                self.table_41[tuple_894_895] = 0 | 4
        elif state == 2:
            # Program TransitionState Region
            tuple_894_895 = (var_894, var_895)
            prev_state = self.table_41[tuple_894_895]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_41[tuple_894_895] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_256_(var_894)
                if not ret:
                    # Program Call Region
                    ret = self.proc_901_(self.var_2, var_895, var_894)
                    if ret:
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_901_(self, var_902: ControlFlowEdgeKind, var_903: int, var_904: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        ret = self.proc_906_(var_903, var_904, self.var_2)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_906_(self, var_907: int, var_908: int, var_909: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_11[(var_907, var_908, var_909)] & 3
        if state == 1:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_911_(self, var_912: int, var_913: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_915: List[int] = list()
        vec_index915: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_915.append(var_912)
        # Program VectorUnique Region
        vec_915 = list(set(vec_915))
        vec_index915 = 0
        # Program TableJoin Region
        while vec_index915 < len(vec_915):
            var_917 = vec_915[vec_index915]
            vec_index915 += 1
            tuple_916_0_index: int = 0
            tuple_916_0_vec: List[int] = self.index_385[var_917]
            while tuple_916_0_index < len(tuple_916_0_vec):
                tuple_916_0 = tuple_916_0_vec[tuple_916_0_index]
                tuple_916_0_index += 1
                var_918 = tuple_916_0
                if var_917 in self.index_253:
                    # Program TupleCompare Region
                    if var_913 == var_918:
                        # Program Series Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_256_(var_917)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_915[:]
        vec_index915 = 0
        # Program Return Region
        return False
        return False

    def proc_920_(self, var_921: int, var_922: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_38[(var_921, var_922)] & 3
        if state == 1:
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_436_(var_921)
            if not ret:
                # Program Return Region
                return True
            # Program TransitionState Region
            tuple_921_922 = (var_921, var_922)
            prev_state = self.table_38[tuple_921_922]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 1:
                self.table_38[tuple_921_922] = 0 | 4
        elif state == 2:
            # Program TransitionState Region
            tuple_921_922 = (var_921, var_922)
            prev_state = self.table_38[tuple_921_922]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_38[tuple_921_922] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_436_(var_921)
                if not ret:
                    # Program Call Region
                    ret = self.proc_928_(self.var_9, var_922, var_921)
                    if ret:
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_928_(self, var_929: ControlFlowEdgeKind, var_930: int, var_931: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        ret = self.proc_906_(var_930, var_931, self.var_9)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_937_(self, var_938: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_938] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_938 = var_938
            prev_state = self.table_15[tuple_938]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_938] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_827_(var_938)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_938 = var_938
                    prev_state = self.table_15[tuple_938]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_938] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_830_(var_938)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_938 = var_938
                    prev_state = self.table_15[tuple_938]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_938] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_944_(self, var_945: int, var_946: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_44[(var_945, var_946)] & 3
        if state == 1:
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_256_(var_945)
            if not ret:
                # Program Return Region
                return True
            # Program TransitionState Region
            tuple_945_946 = (var_945, var_946)
            prev_state = self.table_44[tuple_945_946]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 1:
                self.table_44[tuple_945_946] = 0 | 4
        elif state == 2:
            # Program TransitionState Region
            tuple_945_946 = (var_945, var_946)
            prev_state = self.table_44[tuple_945_946]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_44[tuple_945_946] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_256_(var_945)
                if not ret:
                    # Program Call Region
                    ret = self.proc_952_(var_946, var_945)
                    if ret:
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_952_(self, var_953: int, var_954: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_957: List[ControlFlowEdgeKind] = list()
        vec_index957: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_957: ControlFlowEdgeKind
        scan_index_957: int = 0
        scan_tuple_957_vec: List[ControlFlowEdgeKind] = self.index_956[var_953, var_954]
        while scan_index_957 < len(scan_tuple_957_vec):
            scan_tuple_957 = scan_tuple_957_vec[scan_index_957]
            scan_index_957 += 1
            vec_957.append(scan_tuple_957)
        # Program VectorLoop Region
        vec_index957 = 0
        while vec_index957 < len(vec_957):
            var_958 = vec_957[vec_index957]
            vec_index957 += 1
            # Program CheckState Region
            state = self.table_20[(var_953, var_954, var_958)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_958 = self._resolve_edgetype(var_958)
                tuple_953_954_958 = (var_953, var_954, var_958)
                prev_state = self.table_20[tuple_953_954_958]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_953_954_958] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_873_(var_953, var_954, var_958)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_958 = self._resolve_edgetype(var_958)
                        tuple_953_954_958 = (var_953, var_954, var_958)
                        prev_state = self.table_20[tuple_953_954_958]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_953_954_958] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_953_954_958[1], tuple_953_954_958[2])].append(tuple_953_954_958[0])
                                self.index_956[(tuple_953_954_958[0], tuple_953_954_958[1])].append(tuple_953_954_958[2])
                                self.index_1381[tuple_953_954_958[1]].append((tuple_953_954_958[0], tuple_953_954_958[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_883_(var_953, var_954, var_958)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_958 = self._resolve_edgetype(var_958)
                        tuple_953_954_958 = (var_953, var_954, var_958)
                        prev_state = self.table_20[tuple_953_954_958]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_953_954_958] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_953_954_958[1], tuple_953_954_958[2])].append(tuple_953_954_958[0])
                                self.index_956[(tuple_953_954_958[0], tuple_953_954_958[1])].append(tuple_953_954_958[2])
                                self.index_1381[tuple_953_954_958[1]].append((tuple_953_954_958[0], tuple_953_954_958[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_888_(var_953, var_954, var_958)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_958 = self._resolve_edgetype(var_958)
                        tuple_953_954_958 = (var_953, var_954, var_958)
                        prev_state = self.table_20[tuple_953_954_958]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_953_954_958] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_953_954_958[1], tuple_953_954_958[2])].append(tuple_953_954_958[0])
                                self.index_956[(tuple_953_954_958[0], tuple_953_954_958[1])].append(tuple_953_954_958[2])
                                self.index_1381[tuple_953_954_958[1]].append((tuple_953_954_958[0], tuple_953_954_958[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_963_(self, var_964: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_966: List[int] = list()
        vec_index966: int = 0
        vec_968: List[int] = list()
        vec_index968: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_968: int
        scan_index_968: int = 0
        scan_tuple_968_vec: List[int] = self.index_967[var_964]
        while scan_index_968 < len(scan_tuple_968_vec):
            scan_tuple_968 = scan_tuple_968_vec[scan_index_968]
            scan_index_968 += 1
            vec_968.append(scan_tuple_968)
        # Program VectorLoop Region
        vec_index968 = 0
        while vec_index968 < len(vec_968):
            var_969 = vec_968[vec_index968]
            vec_index968 += 1
            # Program VectorAppend Region
            vec_966.append(var_969)
        # Program VectorUnique Region
        vec_966 = list(set(vec_966))
        vec_index966 = 0
        # Program TableJoin Region
        while vec_index966 < len(vec_966):
            var_971 = vec_966[vec_index966]
            vec_index966 += 1
            tuple_970_0_index: int = 0
            tuple_970_0_vec: List[int] = self.index_414[var_971]
            while tuple_970_0_index < len(tuple_970_0_vec):
                tuple_970_0 = tuple_970_0_vec[tuple_970_0_index]
                tuple_970_0_index += 1
                var_972 = tuple_970_0
                if var_971 in self.index_415:
                    # Program TupleCompare Region
                    if var_964 == var_972:
                        # Program Series Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_407_(var_972, var_971)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_966[:]
        vec_index966 = 0
        # Program Return Region
        return False
        return False

    def proc_975_(self, var_976: int, var_977: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_976_977 = (var_976, var_977)
        prev_state = self.table_17[tuple_976_977]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_17[tuple_976_977] = 0 | 4
            # Program Parallel Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_802_(var_976, var_977)
            if ret:
                # Program Return Region
                return True
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_806_(var_976, var_977)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_993_(self, var_994: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_996: List[int] = list()
        vec_index996: int = 0
        vec_998: List[int] = list()
        vec_index998: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_998: int
        scan_index_998: int = 0
        scan_tuple_998_vec: List[int] = self.index_997[var_994]
        while scan_index_998 < len(scan_tuple_998_vec):
            scan_tuple_998 = scan_tuple_998_vec[scan_index_998]
            scan_index_998 += 1
            vec_998.append(scan_tuple_998)
        # Program VectorLoop Region
        vec_index998 = 0
        while vec_index998 < len(vec_998):
            var_999 = vec_998[vec_index998]
            vec_index998 += 1
            # Program VectorAppend Region
            vec_996.append(var_999)
        # Program VectorUnique Region
        vec_996 = list(set(vec_996))
        vec_index996 = 0
        # Program TableJoin Region
        while vec_index996 < len(vec_996):
            var_1001 = vec_996[vec_index996]
            vec_index996 += 1
            tuple_1000_0_index: int = 0
            tuple_1000_0_vec: List[int] = self.index_365[var_1001]
            while tuple_1000_0_index < len(tuple_1000_0_vec):
                tuple_1000_0 = tuple_1000_0_vec[tuple_1000_0_index]
                tuple_1000_0_index += 1
                var_1002 = tuple_1000_0
                if var_1001 in self.index_433:
                    # Program TupleCompare Region
                    if var_994 == var_1002:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_367_(var_1002, var_1001)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_436_(var_1001)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_996[:]
        vec_index996 = 0
        # Program Return Region
        return False
        return False

    def proc_1005_(self, var_1006: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1006 = var_1006
        prev_state = self.table_24[tuple_1006]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_24[tuple_1006] = 0 | 4
            # Program Parallel Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_1008_(var_1006)
            if ret:
                # Program Return Region
                return True
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_1011_(var_1006)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1008_(self, var_1009: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1015_(var_1009)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1011_(self, var_1012: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_993_(var_1012)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1015_(self, var_1016: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1018: List[int] = list()
        vec_index1018: int = 0
        vec_1019: List[int] = list()
        vec_index1019: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1019: int
        scan_index_1019: int = 0
        scan_tuple_1019_vec: List[int] = self.index_997[var_1016]
        while scan_index_1019 < len(scan_tuple_1019_vec):
            scan_tuple_1019 = scan_tuple_1019_vec[scan_index_1019]
            scan_index_1019 += 1
            vec_1019.append(scan_tuple_1019)
        # Program VectorLoop Region
        vec_index1019 = 0
        while vec_index1019 < len(vec_1019):
            var_1020 = vec_1019[vec_index1019]
            vec_index1019 += 1
            # Program VectorAppend Region
            vec_1018.append(var_1020)
        # Program VectorUnique Region
        vec_1018 = list(set(vec_1018))
        vec_index1018 = 0
        # Program TableJoin Region
        while vec_index1018 < len(vec_1018):
            var_1022 = vec_1018[vec_index1018]
            vec_index1018 += 1
            tuple_1021_0_index: int = 0
            tuple_1021_0_vec: List[int] = self.index_365[var_1022]
            while tuple_1021_0_index < len(tuple_1021_0_vec):
                tuple_1021_0 = tuple_1021_0_vec[tuple_1021_0_index]
                tuple_1021_0_index += 1
                var_1023 = tuple_1021_0
                if var_1022 in self.index_253:
                    # Program TupleCompare Region
                    if var_1016 == var_1023:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_367_(var_1023, var_1022)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_256_(var_1022)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1018[:]
        vec_index1018 = 0
        # Program Return Region
        return False
        return False

    def proc_1026_(self, var_1027: int, var_1028: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1030: List[int] = list()
        vec_index1030: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_1030.append(var_1027)
        # Program VectorUnique Region
        vec_1030 = list(set(vec_1030))
        vec_index1030 = 0
        # Program TableJoin Region
        while vec_index1030 < len(vec_1030):
            var_1032 = vec_1030[vec_index1030]
            vec_index1030 += 1
            tuple_1031_0_index: int = 0
            tuple_1031_0_vec: List[int] = self.index_400[var_1032]
            while tuple_1031_0_index < len(tuple_1031_0_vec):
                tuple_1031_0 = tuple_1031_0_vec[tuple_1031_0_index]
                tuple_1031_0_index += 1
                var_1033 = tuple_1031_0
                if var_1032 in self.index_253:
                    # Program TupleCompare Region
                    if var_1028 == var_1033:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_402_(var_1033, var_1032)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_256_(var_1032)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1030[:]
        vec_index1030 = 0
        # Program Return Region
        return False
        return False

    def proc_1036_(self, var_1037: int, var_1038: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1040: List[ControlFlowEdgeKind] = list()
        vec_index1040: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1040: ControlFlowEdgeKind
        scan_index_1040: int = 0
        scan_tuple_1040_vec: List[ControlFlowEdgeKind] = self.index_956[var_1037, var_1038]
        while scan_index_1040 < len(scan_tuple_1040_vec):
            scan_tuple_1040 = scan_tuple_1040_vec[scan_index_1040]
            scan_index_1040 += 1
            vec_1040.append(scan_tuple_1040)
        # Program VectorLoop Region
        vec_index1040 = 0
        while vec_index1040 < len(vec_1040):
            var_1041 = vec_1040[vec_index1040]
            vec_index1040 += 1
            # Program CheckState Region
            state = self.table_20[(var_1037, var_1038, var_1041)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_1041 = self._resolve_edgetype(var_1041)
                tuple_1037_1038_1041 = (var_1037, var_1038, var_1041)
                prev_state = self.table_20[tuple_1037_1038_1041]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_1037_1038_1041] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_873_(var_1037, var_1038, var_1041)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1041 = self._resolve_edgetype(var_1041)
                        tuple_1037_1038_1041 = (var_1037, var_1038, var_1041)
                        prev_state = self.table_20[tuple_1037_1038_1041]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1037_1038_1041] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_1037_1038_1041[1], tuple_1037_1038_1041[2])].append(tuple_1037_1038_1041[0])
                                self.index_956[(tuple_1037_1038_1041[0], tuple_1037_1038_1041[1])].append(tuple_1037_1038_1041[2])
                                self.index_1381[tuple_1037_1038_1041[1]].append((tuple_1037_1038_1041[0], tuple_1037_1038_1041[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_883_(var_1037, var_1038, var_1041)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1041 = self._resolve_edgetype(var_1041)
                        tuple_1037_1038_1041 = (var_1037, var_1038, var_1041)
                        prev_state = self.table_20[tuple_1037_1038_1041]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1037_1038_1041] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_1037_1038_1041[1], tuple_1037_1038_1041[2])].append(tuple_1037_1038_1041[0])
                                self.index_956[(tuple_1037_1038_1041[0], tuple_1037_1038_1041[1])].append(tuple_1037_1038_1041[2])
                                self.index_1381[tuple_1037_1038_1041[1]].append((tuple_1037_1038_1041[0], tuple_1037_1038_1041[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_888_(var_1037, var_1038, var_1041)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1041 = self._resolve_edgetype(var_1041)
                        tuple_1037_1038_1041 = (var_1037, var_1038, var_1041)
                        prev_state = self.table_20[tuple_1037_1038_1041]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1037_1038_1041] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_1037_1038_1041[1], tuple_1037_1038_1041[2])].append(tuple_1037_1038_1041[0])
                                self.index_956[(tuple_1037_1038_1041[0], tuple_1037_1038_1041[1])].append(tuple_1037_1038_1041[2])
                                self.index_1381[tuple_1037_1038_1041[1]].append((tuple_1037_1038_1041[0], tuple_1037_1038_1041[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1048_(self, var_1049: ControlFlowEdgeKind, var_1050: int, var_1051: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        ret = self.proc_1053_(var_1050, var_1051, self.var_8)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1053_(self, var_1054: int, var_1055: int, var_1056: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_20[(var_1054, var_1055, var_1056)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            var_1056 = self._resolve_edgetype(var_1056)
            tuple_1054_1055_1056 = (var_1054, var_1055, var_1056)
            prev_state = self.table_20[tuple_1054_1055_1056]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_20[tuple_1054_1055_1056] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_873_(var_1054, var_1055, var_1056)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    var_1056 = self._resolve_edgetype(var_1056)
                    tuple_1054_1055_1056 = (var_1054, var_1055, var_1056)
                    prev_state = self.table_20[tuple_1054_1055_1056]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_1054_1055_1056] = 1 | 4
                        if not present_bit:
                            self.index_864[(tuple_1054_1055_1056[1], tuple_1054_1055_1056[2])].append(tuple_1054_1055_1056[0])
                            self.index_956[(tuple_1054_1055_1056[0], tuple_1054_1055_1056[1])].append(tuple_1054_1055_1056[2])
                            self.index_1381[tuple_1054_1055_1056[1]].append((tuple_1054_1055_1056[0], tuple_1054_1055_1056[2]))
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_883_(var_1054, var_1055, var_1056)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    var_1056 = self._resolve_edgetype(var_1056)
                    tuple_1054_1055_1056 = (var_1054, var_1055, var_1056)
                    prev_state = self.table_20[tuple_1054_1055_1056]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_1054_1055_1056] = 1 | 4
                        if not present_bit:
                            self.index_864[(tuple_1054_1055_1056[1], tuple_1054_1055_1056[2])].append(tuple_1054_1055_1056[0])
                            self.index_956[(tuple_1054_1055_1056[0], tuple_1054_1055_1056[1])].append(tuple_1054_1055_1056[2])
                            self.index_1381[tuple_1054_1055_1056[1]].append((tuple_1054_1055_1056[0], tuple_1054_1055_1056[2]))
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_888_(var_1054, var_1055, var_1056)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    var_1056 = self._resolve_edgetype(var_1056)
                    tuple_1054_1055_1056 = (var_1054, var_1055, var_1056)
                    prev_state = self.table_20[tuple_1054_1055_1056]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_1054_1055_1056] = 1 | 4
                        if not present_bit:
                            self.index_864[(tuple_1054_1055_1056[1], tuple_1054_1055_1056[2])].append(tuple_1054_1055_1056[0])
                            self.index_956[(tuple_1054_1055_1056[0], tuple_1054_1055_1056[1])].append(tuple_1054_1055_1056[2])
                            self.index_1381[tuple_1054_1055_1056[1]].append((tuple_1054_1055_1056[0], tuple_1054_1055_1056[2]))
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_1064_(self, var_1065: int, var_1066: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1068: List[int] = list()
        vec_index1068: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_1068.append(var_1065)
        # Program VectorUnique Region
        vec_1068 = list(set(vec_1068))
        vec_index1068 = 0
        # Program TableJoin Region
        while vec_index1068 < len(vec_1068):
            var_1070 = vec_1068[vec_index1068]
            vec_index1068 += 1
            if var_1070 in self.index_194:
                tuple_1069_1_index: int = 0
                tuple_1069_1_vec: List[int] = self.index_199[var_1070]
                while tuple_1069_1_index < len(tuple_1069_1_vec):
                    tuple_1069_1 = tuple_1069_1_vec[tuple_1069_1_index]
                    tuple_1069_1_index += 1
                    var_1071 = tuple_1069_1
                    # Program TupleCompare Region
                    if var_1066 == var_1071:
                        # Program Series Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_204_(var_1070, var_1071)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1068[:]
        vec_index1068 = 0
        # Program Return Region
        return False
        return False

    def proc_1076_(self, var_1077: ControlFlowEdgeKind, var_1078: int, var_1079: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        ret = self.proc_1053_(var_1078, var_1079, self.var_2)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1082_(self, var_1083: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1083 = var_1083
        prev_state = self.table_15[tuple_1083]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_15[tuple_1083] = 0 | 4
            # Program Parallel Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_827_(var_1083)
            if ret:
                # Program Return Region
                return True
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_830_(var_1083)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1095_(self, var_1096: int, var_1097: int, var_1098: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1097_1096 = (var_1097, var_1096)
        prev_state = self.table_44[tuple_1097_1096]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_44[tuple_1097_1096] = 2 | 4
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_256_(var_1097)
            if ret:
                # Program Series Region
                # Program TransitionState Region
                tuple_1097_1096 = (var_1097, var_1096)
                prev_state = self.table_44[tuple_1097_1096]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_44[tuple_1097_1096] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    ret = self.proc_330_(var_1097, var_1096)

                    # Program Call Region
                    ret = self.proc_334_(var_1097, var_1096)

                # Program Return Region
                return False
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CreateBottomUpNegationRemover
            ret = self.proc_1342_(var_1097, var_1096)
            if ret:
                # Program Series Region
                # Program TransitionState Region
                tuple_1097_1096 = (var_1097, var_1096)
                prev_state = self.table_44[tuple_1097_1096]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_44[tuple_1097_1096] = 1 | 4
                    if not present_bit:
                        self.index_327[tuple_1097_1096[0]].append(tuple_1097_1096[1])
                # Program Return Region
                return False
            # Program TransitionState Region
            tuple_1097_1096 = (var_1097, var_1096)
            prev_state = self.table_44[tuple_1097_1096]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_44[tuple_1097_1096] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                ret = self.proc_330_(var_1097, var_1096)

                # Program Call Region
                ret = self.proc_334_(var_1097, var_1096)

        # Program Return Region
        return False
        return False

    def proc_1100_(self, var_1101: int, var_1102: int, var_1103: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1101_1102 = (var_1101, var_1102)
        prev_state = self.table_139[tuple_1101_1102]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_139[tuple_1101_1102] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1284_(var_1102, var_1101)

            # Program Call Region
            ret = self.proc_1288_(var_1102, var_1101)

        # Program Return Region
        return False
        return False

    def proc_1105_(self, var_1106: int, var_1107: int, var_1108: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TupleCompare Region
        if self.var_0 == var_1108:
            # Program Call Region
            ret = self.proc_1325_(self.var_0, var_1107)

        # Program Return Region
        return False
        return False

    def proc_1110_(self, var_1111: int, var_1112: int, var_1113: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TupleCompare Region
        if self.var_2 == var_1113:
            # Program Call Region
            ret = self.proc_1171_(self.var_2, var_1111, var_1112)

        # Program Return Region
        return False
        return False

    def proc_1115_(self, var_1116: int, var_1117: int, var_1118: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TupleCompare Region
        if self.var_8 == var_1118:
            # Program Call Region
            ret = self.proc_1121_(self.var_8, var_1116, var_1117)

        # Program Return Region
        return False
        return False

    def proc_1121_(self, var_1122: ControlFlowEdgeKind, var_1123: int, var_1124: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1123_1124 = (var_1123, var_1124)
        prev_state = self.table_133[tuple_1123_1124]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_133[tuple_1123_1124] = 2 | 4
            # Program Call Region
            ret = self.proc_1133_(var_1124, var_1123)

        # Program Return Region
        return False
        return False

    def proc_1133_(self, var_1134: int, var_1135: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1135 = var_1135
        prev_state = self.table_24[tuple_1135]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_24[tuple_1135] = 2 | 4
            # Program Call Region
            ret = self.proc_1140_(var_1135)

        # Program Return Region
        return False
        return False

    def proc_1140_(self, var_1141: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1146: List[int] = list()
        vec_index1146: int = 0
        vec_1152: List[int] = list()
        vec_index1152: int = 0
        vec_1153: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index1153: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: CreateBottomUpTupleRemover
        ret = self.proc_1143_(var_1141)
        if not ret:
            # Program Parallel Region
            # Program Series Region
            # Program TableScan Region
            scan_tuple_1146: int
            scan_index_1146: int = 0
            scan_tuple_1146_vec: List[int] = self.index_423[var_1141]
            while scan_index_1146 < len(scan_tuple_1146_vec):
                scan_tuple_1146 = scan_tuple_1146_vec[scan_index_1146]
                scan_index_1146 += 1
                vec_1146.append(scan_tuple_1146)
            # Program VectorLoop Region
            vec_index1146 = 0
            while vec_index1146 < len(vec_1146):
                var_1147 = vec_1146[vec_index1146]
                vec_index1146 += 1
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: ReAddToNegatedView
                ret = self.proc_1148_(var_1141)
                if ret:
                    # Program TransitionState Region
                    # Re-adding to negated view
                    tuple_1141_1147 = (var_1141, var_1147)
                    prev_state = self.table_38[tuple_1141_1147]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_38[tuple_1141_1147] = 1 | 4
                        if not present_bit:
                            self.index_423[tuple_1141_1147[0]].append(tuple_1141_1147[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_458_(var_1147, var_1141, self.var_9)
                        if not ret:
                            # Program TransitionState Region
                            tuple_1147_1141_9 = (var_1147, var_1141, self.var_9)
                            prev_state = self.table_20[tuple_1147_1141_9]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_20[tuple_1147_1141_9] = 1 | 4
                                if not present_bit:
                                    self.index_864[(tuple_1147_1141_9[1], tuple_1147_1141_9[2])].append(tuple_1147_1141_9[0])
                                    self.index_956[(tuple_1147_1141_9[0], tuple_1147_1141_9[1])].append(tuple_1147_1141_9[2])
                                    self.index_1381[tuple_1147_1141_9[1]].append((tuple_1147_1141_9[0], tuple_1147_1141_9[2]))
                                # Program VectorAppend Region
                                vec_1153.append((var_1147, var_1141, self.var_9))
            # Program Call Region
            ret = self.proc_1156_(var_1141)

        # Induction Fixpoint Loop Region
        while len(vec_1152) or len(vec_1153):
            # Program Series Region
            # Program Call Region
            ret = self.proc_164_(vec_1152, vec_1153)

            # Program Call Region
            param_1155_0 = [vec_1152]
            param_1155_1 = [vec_1153]
            ret = self.proc_161_(param_1155_0, param_1155_1)
            vec_1152 = param_1155_0[0]
            vec_1153 = param_1155_1[0]

        vec_index1152 = 0
        vec_index1153 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_1152[:]
        vec_index1152 = 0
        # Program VectorClear Region
        del vec_1153[:]
        vec_index1153 = 0
        # Program Return Region
        return False
        return False

    def proc_1143_(self, var_1144: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1005_(var_1144)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1148_(self, var_1149: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1390: List[int] = list()
        vec_index1390: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1390: int
        scan_index_1390: int = 0
        scan_tuple_1390_vec: List[int] = self.index_1372[var_1149, self.var_9]
        while scan_index_1390 < len(scan_tuple_1390_vec):
            scan_tuple_1390 = scan_tuple_1390_vec[scan_index_1390]
            scan_index_1390 += 1
            vec_1390.append(scan_tuple_1390)
        # Program VectorLoop Region
        vec_index1390 = 0
        while vec_index1390 < len(vec_1390):
            var_1391 = vec_1390[vec_index1390]
            vec_index1390 += 1
            # Program Call Region
            ret = self.proc_1375_(var_1149, self.var_9)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1156_(self, var_1157: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1159: List[int] = list()
        vec_index1159: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1159: int
        scan_index_1159: int = 0
        scan_tuple_1159_vec: List[int] = self.index_365[var_1157]
        while scan_index_1159 < len(scan_tuple_1159_vec):
            scan_tuple_1159 = scan_tuple_1159_vec[scan_index_1159]
            scan_index_1159 += 1
            vec_1159.append(scan_tuple_1159)
        # Program VectorLoop Region
        vec_index1159 = 0
        while vec_index1159 < len(vec_1159):
            var_1160 = vec_1159[vec_index1159]
            vec_index1159 += 1
            # Program Call Region
            ret = self.proc_1133_(var_1157, var_1160)

        # Program Return Region
        return False
        return False

    def proc_1171_(self, var_1172: ControlFlowEdgeKind, var_1173: int, var_1174: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1173_1174 = (var_1173, var_1174)
        prev_state = self.table_57[tuple_1173_1174]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_57[tuple_1173_1174] = 2 | 4
            # Program Call Region
            ret = self.proc_1179_(var_1173, var_1174)

        # Program Return Region
        return False
        return False

    def proc_1179_(self, var_1180: int, var_1181: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1180_1181 = (var_1180, var_1181)
        prev_state = self.table_60[tuple_1180_1181]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_60[tuple_1180_1181] = 2 | 4
            # Program Call Region
            ret = self.proc_1187_(var_1181, var_1180)

        # Program Return Region
        return False
        return False

    def proc_1187_(self, var_1188: int, var_1189: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1189 = var_1189
        prev_state = self.table_15[tuple_1189]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_15[tuple_1189] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1200_(var_1189)

            # Program Call Region
            ret = self.proc_1203_(var_1189)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1082_(var_1189)

        # Program Return Region
        return False
        return False

    def proc_1200_(self, var_1201: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1243: List[int] = list()
        vec_index1243: int = 0
        vec_1249: List[int] = list()
        vec_index1249: int = 0
        vec_1255: List[int] = list()
        vec_index1255: int = 0
        vec_1256: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index1256: int = 0
        vec_1271: List[int] = list()
        vec_index1271: int = 0
        vec_1279: List[Tuple[int, int]] = list()
        vec_index1279: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: CreateBottomUpTupleRemover
        ret = self.proc_1240_(var_1201)
        if not ret:
            # Program Parallel Region
            # Program Series Region
            # Program TableScan Region
            scan_tuple_1243: int
            scan_index_1243: int = 0
            scan_tuple_1243_vec: List[int] = self.index_327[var_1201]
            while scan_index_1243 < len(scan_tuple_1243_vec):
                scan_tuple_1243 = scan_tuple_1243_vec[scan_index_1243]
                scan_index_1243 += 1
                vec_1243.append(scan_tuple_1243)
            # Program VectorLoop Region
            vec_index1243 = 0
            while vec_index1243 < len(vec_1243):
                var_1244 = vec_1243[vec_index1243]
                vec_index1243 += 1
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: ReAddToNegatedView
                ret = self.proc_1245_(var_1201)
                if ret:
                    # Program TransitionState Region
                    # Re-adding to negated view
                    tuple_1201_1244 = (var_1201, var_1244)
                    prev_state = self.table_44[tuple_1201_1244]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_44[tuple_1201_1244] = 1 | 4
                        if not present_bit:
                            self.index_327[tuple_1201_1244[0]].append(tuple_1201_1244[1])
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_490_(var_1244, var_1201)
                        if not ret:
                            # Program TransitionState Region
                            tuple_1244_1201 = (var_1244, var_1201)
                            prev_state = self.table_69[tuple_1244_1201]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_69[tuple_1244_1201] = 1 | 4
                                if not present_bit:
                                    self.index_522[tuple_1244_1201[0]].append(tuple_1244_1201[1])
                                    self.index_815[tuple_1244_1201[1]].append(tuple_1244_1201[0])
                                # Program VectorAppend Region
                                vec_1271.append(var_1244)
                        # Program TransitionState Region
                        tuple_1244_1201 = (var_1244, var_1201)
                        prev_state = self.table_28[tuple_1244_1201]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_28[tuple_1244_1201] = 1 | 4
                            if not present_bit:
                                self.index_774[tuple_1244_1201[0]].append(tuple_1244_1201[1])
            # Program Series Region
            # Program TableScan Region
            scan_tuple_1249: int
            scan_index_1249: int = 0
            scan_tuple_1249_vec: List[int] = self.index_338[var_1201]
            while scan_index_1249 < len(scan_tuple_1249_vec):
                scan_tuple_1249 = scan_tuple_1249_vec[scan_index_1249]
                scan_index_1249 += 1
                vec_1249.append(scan_tuple_1249)
            # Program VectorLoop Region
            vec_index1249 = 0
            while vec_index1249 < len(vec_1249):
                var_1250 = vec_1249[vec_index1249]
                vec_index1249 += 1
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: ReAddToNegatedView
                ret = self.proc_1251_(var_1201)
                if ret:
                    # Program TransitionState Region
                    # Re-adding to negated view
                    tuple_1201_1250 = (var_1201, var_1250)
                    prev_state = self.table_41[tuple_1201_1250]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_41[tuple_1201_1250] = 1 | 4
                        if not present_bit:
                            self.index_338[tuple_1201_1250[0]].append(tuple_1201_1250[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_447_(var_1250, var_1201, self.var_2)
                        if not ret:
                            # Program TransitionState Region
                            tuple_1250_1201_2 = (var_1250, var_1201, self.var_2)
                            prev_state = self.table_20[tuple_1250_1201_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_20[tuple_1250_1201_2] = 1 | 4
                                if not present_bit:
                                    self.index_864[(tuple_1250_1201_2[1], tuple_1250_1201_2[2])].append(tuple_1250_1201_2[0])
                                    self.index_956[(tuple_1250_1201_2[0], tuple_1250_1201_2[1])].append(tuple_1250_1201_2[2])
                                    self.index_1381[tuple_1250_1201_2[1]].append((tuple_1250_1201_2[0], tuple_1250_1201_2[2]))
                                # Program VectorAppend Region
                                vec_1256.append((var_1250, var_1201, self.var_2))
            # Program Call Region
            ret = self.proc_1259_(var_1201)

            # Program Call Region
            ret = self.proc_1156_(var_1201)

            # Program Call Region
            ret = self.proc_1265_(var_1201)

            # Program Call Region
            ret = self.proc_1268_(var_1201)

        # Program VectorUnique Region
        vec_1271 = list(set(vec_1271))
        vec_index1271 = 0
        # Program TableJoin Region
        while vec_index1271 < len(vec_1271):
            var_1273 = vec_1271[vec_index1271]
            vec_index1271 += 1
            tuple_1272_0_index: int = 0
            tuple_1272_0_vec: List[int] = self.index_521[var_1273]
            while tuple_1272_0_index < len(tuple_1272_0_vec):
                tuple_1272_0 = tuple_1272_0_vec[tuple_1272_0_index]
                tuple_1272_0_index += 1
                var_1274 = tuple_1272_0
                tuple_1272_1_index: int = 0
                tuple_1272_1_vec: List[int] = self.index_522[var_1273]
                while tuple_1272_1_index < len(tuple_1272_1_vec):
                    tuple_1272_1 = tuple_1272_1_vec[tuple_1272_1_index]
                    tuple_1272_1_index += 1
                    var_1275 = tuple_1272_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_525_(var_1274, var_1273)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_490_(var_1273, var_1275)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_530_(var_1274, var_1275)
                            if not ret:
                                # Program TransitionState Region
                                tuple_1274_1275 = (var_1274, var_1275)
                                prev_state = self.table_17[tuple_1274_1275]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_1274_1275] = 1 | 4
                                    if not present_bit:
                                        self.index_521[tuple_1274_1275[1]].append(tuple_1274_1275[0])
                                        self.index_780[tuple_1274_1275[0]].append(tuple_1274_1275[1])
                                    # Program VectorAppend Region
                                    vec_1279.append((var_1274, var_1275))
        # Program VectorClear Region
        del vec_1271[:]
        vec_index1271 = 0
        # Induction Fixpoint Loop Region
        while len(vec_1279) or len(vec_1255) or len(vec_1256):
            # Program Series Region
            # Program Call Region
            ret = self.proc_164_(vec_1255, vec_1256)

            # Program Call Region
            param_1258_0 = [vec_1255]
            param_1258_1 = [vec_1256]
            ret = self.proc_161_(param_1258_0, param_1258_1)
            vec_1255 = param_1258_0[0]
            vec_1256 = param_1258_1[0]

            # Program Call Region
            param_1281_0 = [vec_1279]
            ret = self.proc_479_(param_1281_0)
            vec_1279 = param_1281_0[0]

        vec_index1279 = 0
        vec_index1255 = 0
        vec_index1256 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_1255[:]
        vec_index1255 = 0
        # Program VectorClear Region
        del vec_1256[:]
        vec_index1256 = 0
        # Program VectorClear Region
        del vec_1279[:]
        vec_index1279 = 0
        # Program Return Region
        return False
        return False

    def proc_1203_(self, var_1204: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1204_1204 = (var_1204, var_1204)
        prev_state = self.table_17[tuple_1204_1204]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_17[tuple_1204_1204] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1223_(var_1204, var_1204)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_975_(var_1204, var_1204)

        # Program Return Region
        return False
        return False

    def proc_1223_(self, var_1224: int, var_1225: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1227: List[int] = list()
        vec_index1227: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1227: int
        scan_index_1227: int = 0
        scan_tuple_1227_vec: List[int] = self.index_522[var_1225]
        while scan_index_1227 < len(scan_tuple_1227_vec):
            scan_tuple_1227 = scan_tuple_1227_vec[scan_index_1227]
            scan_index_1227 += 1
            vec_1227.append(scan_tuple_1227)
        # Program VectorLoop Region
        vec_index1227 = 0
        while vec_index1227 < len(vec_1227):
            var_1228 = vec_1227[vec_index1227]
            vec_index1227 += 1
            # Program Call Region
            ret = self.proc_1229_(var_1225, var_1224, var_1228)

        # Program Return Region
        return False
        return False

    def proc_1229_(self, var_1230: int, var_1231: int, var_1232: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1231_1232 = (var_1231, var_1232)
        prev_state = self.table_17[tuple_1231_1232]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_17[tuple_1231_1232] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1223_(var_1231, var_1232)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_975_(var_1231, var_1232)

        # Program Return Region
        return False
        return False

    def proc_1240_(self, var_1241: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1082_(var_1241)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1245_(self, var_1246: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1382: List[Tuple[int, ControlFlowEdgeKind]] = list()
        vec_index1382: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1382: Tuple[int, ControlFlowEdgeKind]
        scan_index_1382: int = 0
        scan_tuple_1382_vec: List[Tuple[int, ControlFlowEdgeKind]] = self.index_1381[var_1246]
        while scan_index_1382 < len(scan_tuple_1382_vec):
            scan_tuple_1382 = scan_tuple_1382_vec[scan_index_1382]
            scan_index_1382 += 1
            vec_1382.append(scan_tuple_1382)
        # Program VectorLoop Region
        vec_index1382 = 0
        while vec_index1382 < len(vec_1382):
            var_1383, var_1384 = vec_1382[vec_index1382]
            vec_index1382 += 1
            # Program CheckState Region
            state = self.table_20[(var_1383, var_1246, var_1384)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_1384 = self._resolve_edgetype(var_1384)
                tuple_1383_1246_1384 = (var_1383, var_1246, var_1384)
                prev_state = self.table_20[tuple_1383_1246_1384]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_1383_1246_1384] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_873_(var_1383, var_1246, var_1384)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1384 = self._resolve_edgetype(var_1384)
                        tuple_1383_1246_1384 = (var_1383, var_1246, var_1384)
                        prev_state = self.table_20[tuple_1383_1246_1384]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1383_1246_1384] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_1383_1246_1384[1], tuple_1383_1246_1384[2])].append(tuple_1383_1246_1384[0])
                                self.index_956[(tuple_1383_1246_1384[0], tuple_1383_1246_1384[1])].append(tuple_1383_1246_1384[2])
                                self.index_1381[tuple_1383_1246_1384[1]].append((tuple_1383_1246_1384[0], tuple_1383_1246_1384[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_883_(var_1383, var_1246, var_1384)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1384 = self._resolve_edgetype(var_1384)
                        tuple_1383_1246_1384 = (var_1383, var_1246, var_1384)
                        prev_state = self.table_20[tuple_1383_1246_1384]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1383_1246_1384] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_1383_1246_1384[1], tuple_1383_1246_1384[2])].append(tuple_1383_1246_1384[0])
                                self.index_956[(tuple_1383_1246_1384[0], tuple_1383_1246_1384[1])].append(tuple_1383_1246_1384[2])
                                self.index_1381[tuple_1383_1246_1384[1]].append((tuple_1383_1246_1384[0], tuple_1383_1246_1384[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_888_(var_1383, var_1246, var_1384)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1384 = self._resolve_edgetype(var_1384)
                        tuple_1383_1246_1384 = (var_1383, var_1246, var_1384)
                        prev_state = self.table_20[tuple_1383_1246_1384]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1383_1246_1384] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_1383_1246_1384[1], tuple_1383_1246_1384[2])].append(tuple_1383_1246_1384[0])
                                self.index_956[(tuple_1383_1246_1384[0], tuple_1383_1246_1384[1])].append(tuple_1383_1246_1384[2])
                                self.index_1381[tuple_1383_1246_1384[1]].append((tuple_1383_1246_1384[0], tuple_1383_1246_1384[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1251_(self, var_1252: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1373: List[int] = list()
        vec_index1373: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1373: int
        scan_index_1373: int = 0
        scan_tuple_1373_vec: List[int] = self.index_1372[var_1252, self.var_2]
        while scan_index_1373 < len(scan_tuple_1373_vec):
            scan_tuple_1373 = scan_tuple_1373_vec[scan_index_1373]
            scan_index_1373 += 1
            vec_1373.append(scan_tuple_1373)
        # Program VectorLoop Region
        vec_index1373 = 0
        while vec_index1373 < len(vec_1373):
            var_1374 = vec_1373[vec_index1373]
            vec_index1373 += 1
            # Program Call Region
            ret = self.proc_1375_(var_1252, self.var_2)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1259_(self, var_1260: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1321: List[int] = list()
        vec_index1321: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1321: int
        scan_index_1321: int = 0
        scan_tuple_1321_vec: List[int] = self.index_254[var_1260]
        while scan_index_1321 < len(scan_tuple_1321_vec):
            scan_tuple_1321 = scan_tuple_1321_vec[scan_index_1321]
            scan_index_1321 += 1
            vec_1321.append(scan_tuple_1321)
        # Program VectorLoop Region
        vec_index1321 = 0
        while vec_index1321 < len(vec_1321):
            var_1322 = vec_1321[vec_index1321]
            vec_index1321 += 1
            # Program Call Region
            ret = self.proc_1187_(var_1260, var_1322)

        # Program Return Region
        return False
        return False

    def proc_1265_(self, var_1266: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1302: List[int] = list()
        vec_index1302: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1302: int
        scan_index_1302: int = 0
        scan_tuple_1302_vec: List[int] = self.index_385[var_1266]
        while scan_index_1302 < len(scan_tuple_1302_vec):
            scan_tuple_1302 = scan_tuple_1302_vec[scan_index_1302]
            scan_index_1302 += 1
            vec_1302.append(scan_tuple_1302)
        # Program VectorLoop Region
        vec_index1302 = 0
        while vec_index1302 < len(vec_1302):
            var_1303 = vec_1302[vec_index1302]
            vec_index1302 += 1
            # Program Call Region
            ret = self.proc_1304_(var_1266, var_1303)

        # Program Return Region
        return False
        return False

    def proc_1268_(self, var_1269: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1282: List[int] = list()
        vec_index1282: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1282: int
        scan_index_1282: int = 0
        scan_tuple_1282_vec: List[int] = self.index_400[var_1269]
        while scan_index_1282 < len(scan_tuple_1282_vec):
            scan_tuple_1282 = scan_tuple_1282_vec[scan_index_1282]
            scan_index_1282 += 1
            vec_1282.append(scan_tuple_1282)
        # Program VectorLoop Region
        vec_index1282 = 0
        while vec_index1282 < len(vec_1282):
            var_1283 = vec_1282[vec_index1282]
            vec_index1282 += 1
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1284_(var_1269, var_1283)

            # Program Call Region
            ret = self.proc_1288_(var_1269, var_1283)

        # Program Return Region
        return False
        return False

    def proc_1284_(self, var_1285: int, var_1286: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1286_1285 = (var_1286, var_1285)
        prev_state = self.table_142[tuple_1286_1285]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_142[tuple_1286_1285] = 2 | 4
            # Program Call Region
            ret = self.proc_1297_(var_1285, var_1286)

        # Program Return Region
        return False
        return False

    def proc_1288_(self, var_1289: int, var_1290: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1290_1289 = (var_1290, var_1289)
        prev_state = self.table_33[tuple_1290_1289]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_33[tuple_1290_1289] = 2 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_788_(var_1289, var_1290)

        # Program Return Region
        return False
        return False

    def proc_1297_(self, var_1298: int, var_1299: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1299 = var_1299
        prev_state = self.table_26[tuple_1299]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_26[tuple_1299] = 2 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_963_(var_1299)

        # Program Return Region
        return False
        return False

    def proc_1304_(self, var_1305: int, var_1306: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1306_1305_10 = (var_1306, var_1305, self.var_10)
        prev_state = self.table_20[tuple_1306_1305_10]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_20[tuple_1306_1305_10] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1095_(var_1306, var_1305, self.var_10)

            # Program Call Region
            ret = self.proc_1100_(var_1306, var_1305, self.var_10)

            # Program Call Region
            ret = self.proc_1105_(var_1306, var_1305, self.var_10)

            # Program Call Region
            ret = self.proc_1110_(var_1306, var_1305, self.var_10)

            # Program Call Region
            ret = self.proc_1115_(var_1306, var_1305, self.var_10)

        # Program Return Region
        return False
        return False

    def proc_1325_(self, var_1326: ControlFlowEdgeKind, var_1327: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1327 = var_1327
        prev_state = self.table_15[tuple_1327]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_15[tuple_1327] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1200_(var_1327)

            # Program Call Region
            ret = self.proc_1203_(var_1327)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1082_(var_1327)

        # Program Return Region
        return False
        return False

    def proc_1342_(self, var_1343: int, var_1344: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1366: List[ControlFlowEdgeKind] = list()
        vec_index1366: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1366: ControlFlowEdgeKind
        scan_index_1366: int = 0
        scan_tuple_1366_vec: List[ControlFlowEdgeKind] = self.index_956[var_1344, var_1343]
        while scan_index_1366 < len(scan_tuple_1366_vec):
            scan_tuple_1366 = scan_tuple_1366_vec[scan_index_1366]
            scan_index_1366 += 1
            vec_1366.append(scan_tuple_1366)
        # Program VectorLoop Region
        vec_index1366 = 0
        while vec_index1366 < len(vec_1366):
            var_1367 = vec_1366[vec_index1366]
            vec_index1366 += 1
            # Program CheckState Region
            state = self.table_20[(var_1344, var_1343, var_1367)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_1367 = self._resolve_edgetype(var_1367)
                tuple_1344_1343_1367 = (var_1344, var_1343, var_1367)
                prev_state = self.table_20[tuple_1344_1343_1367]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_1344_1343_1367] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_873_(var_1344, var_1343, var_1367)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1367 = self._resolve_edgetype(var_1367)
                        tuple_1344_1343_1367 = (var_1344, var_1343, var_1367)
                        prev_state = self.table_20[tuple_1344_1343_1367]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1344_1343_1367] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_1344_1343_1367[1], tuple_1344_1343_1367[2])].append(tuple_1344_1343_1367[0])
                                self.index_956[(tuple_1344_1343_1367[0], tuple_1344_1343_1367[1])].append(tuple_1344_1343_1367[2])
                                self.index_1381[tuple_1344_1343_1367[1]].append((tuple_1344_1343_1367[0], tuple_1344_1343_1367[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_883_(var_1344, var_1343, var_1367)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1367 = self._resolve_edgetype(var_1367)
                        tuple_1344_1343_1367 = (var_1344, var_1343, var_1367)
                        prev_state = self.table_20[tuple_1344_1343_1367]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1344_1343_1367] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_1344_1343_1367[1], tuple_1344_1343_1367[2])].append(tuple_1344_1343_1367[0])
                                self.index_956[(tuple_1344_1343_1367[0], tuple_1344_1343_1367[1])].append(tuple_1344_1343_1367[2])
                                self.index_1381[tuple_1344_1343_1367[1]].append((tuple_1344_1343_1367[0], tuple_1344_1343_1367[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_888_(var_1344, var_1343, var_1367)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1367 = self._resolve_edgetype(var_1367)
                        tuple_1344_1343_1367 = (var_1344, var_1343, var_1367)
                        prev_state = self.table_20[tuple_1344_1343_1367]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1344_1343_1367] = 1 | 4
                            if not present_bit:
                                self.index_864[(tuple_1344_1343_1367[1], tuple_1344_1343_1367[2])].append(tuple_1344_1343_1367[0])
                                self.index_956[(tuple_1344_1343_1367[0], tuple_1344_1343_1367[1])].append(tuple_1344_1343_1367[2])
                                self.index_1381[tuple_1344_1343_1367[1]].append((tuple_1344_1343_1367[0], tuple_1344_1343_1367[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1359_(self, var_1360: int, var_1361: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1363: List[int] = list()
        vec_index1363: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1363: int
        scan_index_1363: int = 0
        scan_tuple_1363_vec: List[int] = self.index_521[var_1360]
        while scan_index_1363 < len(scan_tuple_1363_vec):
            scan_tuple_1363 = scan_tuple_1363_vec[scan_index_1363]
            scan_index_1363 += 1
            vec_1363.append(scan_tuple_1363)
        # Program VectorLoop Region
        vec_index1363 = 0
        while vec_index1363 < len(vec_1363):
            var_1364 = vec_1363[vec_index1363]
            vec_index1363 += 1
            # Program Call Region
            ret = self.proc_1229_(var_1360, var_1364, var_1361)

        # Program Return Region
        return False
        return False

    def proc_1375_(self, var_1376: int, var_1377: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1379: List[int] = list()
        vec_index1379: int = 0
        # Program Series Region
        # Program TableScan Region
        var_1377 = self._resolve_edgetype(var_1377)
        scan_tuple_1379: int
        scan_index_1379: int = 0
        scan_tuple_1379_vec: List[int] = self.index_1372[var_1376, var_1377]
        while scan_index_1379 < len(scan_tuple_1379_vec):
            scan_tuple_1379 = scan_tuple_1379_vec[scan_index_1379]
            scan_index_1379 += 1
            vec_1379.append(scan_tuple_1379)
        # Program VectorLoop Region
        vec_index1379 = 0
        while vec_index1379 < len(vec_1379):
            var_1380 = vec_1379[vec_index1379]
            vec_index1379 += 1
            # Program CheckState Region
            state = self.table_11[(var_1380, var_1376, var_1377)] & 3
            if state == 1:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def get_external_calls_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_26:
            tuple_index += 1
            param_0: int = tuple
            if not self.proc_772_(param_0):
                continue
            yield param_0

    def intraproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_774[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_775_(param_0, param_1):
                continue
            yield param_1

    def function_b(self, param_0: int) -> bool:
        state: int = 0
        tuple_index: int = 0
        if True:
            if not self.proc_778_(param_0):
                return False
            return True

    def function_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_15:
            tuple_index += 1
            param_0: int = tuple
            if not self.proc_778_(param_0):
                continue
            yield param_0

    def function_instruction_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_780[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_781_(param_0, param_1):
                continue
            yield param_1

    def get_instructions_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_31:
            tuple_index += 1
            param_0: int = tuple
            full_tuple = param_0
            state = self.table_31[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

    def interproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_784[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_785_(param_0, param_1):
                continue
            yield param_1

    def get_sections_f(self) -> Iterator[bytes]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_36:
            tuple_index += 1
            param_0: bytes = tuple
            full_tuple = param_0
            state = self.table_36[full_tuple] & 3
            if state != 1:
                continue;
            yield param_0

