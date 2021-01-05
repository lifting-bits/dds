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
        self.index_1479: DefaultDict[Tuple[int, ControlFlowEdgeKind], List[int]] = defaultdict(list)

        self.table_15: DefaultDict[int, int] = defaultdict(int)
        self.index_289 = self.table_15

        self.table_17: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_557: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_882: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_20: DefaultDict[Tuple[int, int, ControlFlowEdgeKind], int] = defaultdict(int)
        self.index_969: DefaultDict[Tuple[int, ControlFlowEdgeKind], List[int]] = defaultdict(list)
        self.index_1062: DefaultDict[Tuple[int, int], List[ControlFlowEdgeKind]] = defaultdict(list)
        self.index_1488: DefaultDict[int, List[Tuple[int, ControlFlowEdgeKind]]] = defaultdict(list)

        self.table_24: DefaultDict[int, int] = defaultdict(int)
        self.index_469 = self.table_24

        self.table_26: DefaultDict[int, int] = defaultdict(int)

        self.table_28: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_876: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_31: DefaultDict[int, int] = defaultdict(int)

        self.table_33: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_886: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_36: DefaultDict[bytes, int] = defaultdict(int)

        self.table_38: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_459: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_41: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_374: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_44: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_363: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_47: DefaultDict[int, int] = defaultdict(int)
        self.index_210 = self.table_47

        self.table_49: DefaultDict[int, int] = defaultdict(int)
        self.index_172 = self.table_49

        self.table_51: DefaultDict[int, int] = defaultdict(int)
        self.index_206 = self.table_51

        self.table_53: DefaultDict[int, int] = defaultdict(int)
        self.index_202 = self.table_53

        self.table_55: DefaultDict[int, int] = defaultdict(int)
        self.index_198 = self.table_55

        self.table_57: DefaultDict[int, int] = defaultdict(int)
        self.index_194 = self.table_57

        self.table_59: DefaultDict[int, int] = defaultdict(int)
        self.index_190 = self.table_59

        self.table_61: DefaultDict[int, int] = defaultdict(int)
        self.index_186 = self.table_61

        self.table_63: DefaultDict[int, int] = defaultdict(int)
        self.index_171 = self.table_63

        self.table_65: DefaultDict[int, int] = defaultdict(int)
        self.index_451 = self.table_65

        self.table_67: DefaultDict[int, int] = defaultdict(int)
        self.index_596 = self.table_67

        self.table_69: DefaultDict[int, int] = defaultdict(int)
        self.index_261 = self.table_69

        self.table_71: DefaultDict[int, int] = defaultdict(int)
        self.index_248 = self.table_71

        self.table_73: DefaultDict[int, int] = defaultdict(int)
        self.index_230 = self.table_73

        self.table_75: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_235: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_78: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_290: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_957: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_81: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_558: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_917: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_84: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_215: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_87: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_265: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_90: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_305: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_93: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_336: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_96: DefaultDict[int, int] = defaultdict(int)
        self.index_225 = self.table_96

        self.table_98: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_266: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_101: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_331: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_104: DefaultDict[int, int] = defaultdict(int)
        self.index_220 = self.table_104

        self.table_106: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_272: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_109: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_326: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_112: DefaultDict[int, int] = defaultdict(int)
        self.index_214 = self.table_112

        self.table_114: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_278: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_117: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_321: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_120: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_758 = self.table_120

        self.table_123: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_759 = self.table_123

        self.table_126: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_284: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_129: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_316: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_132: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_345: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_135: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_346: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_138: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_311: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_141: DefaultDict[Tuple[ControlFlowEdgeKind, int, int], int] = defaultdict(int)
        self.index_247: DefaultDict[int, List[Tuple[ControlFlowEdgeKind, int]]] = defaultdict(list)

        self.table_145: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_401: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_1103: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_148: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_421: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_151: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_436: DefaultDict[int, List[int]] = defaultdict(list)

        self.table_154: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        self.index_450: DefaultDict[int, List[int]] = defaultdict(list)
        self.index_1073: DefaultDict[int, List[int]] = defaultdict(list)

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
        self.init_157_()

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

    def init_157_(self) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Return Region
        return False
        return False

    def section_3(self, vec_159: List[Tuple[bytes, int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index159: int = 0
        # Program Series Region
        # Program VectorLoop Region
        vec_index159 = 0
        while vec_index159 < len(vec_159):
            var_160, var_161, var_162 = vec_159[vec_index159]
            vec_index159 += 1
            # Program TransitionState Region
            tuple_160 = var_160
            prev_state = self.table_36[tuple_160]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_36[tuple_160] = 1 | 4
                if not present_bit:
                    pass
        # Program Return Region
        return False
        return False

    def instruction_3(self, vec_164: List[Tuple[int, InstructionType, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index164: int = 0
        vec_168: List[int] = list()
        vec_index168: int = 0
        vec_179: List[int] = list()
        vec_index179: int = 0
        vec_180: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index180: int = 0
        vec_183: List[int] = list()
        vec_index183: int = 0
        vec_187: List[int] = list()
        vec_index187: int = 0
        vec_191: List[int] = list()
        vec_index191: int = 0
        vec_195: List[int] = list()
        vec_index195: int = 0
        vec_199: List[int] = list()
        vec_index199: int = 0
        vec_203: List[int] = list()
        vec_index203: int = 0
        vec_207: List[int] = list()
        vec_index207: int = 0
        vec_211: List[int] = list()
        vec_index211: int = 0
        vec_217: List[int] = list()
        vec_index217: int = 0
        vec_222: List[int] = list()
        vec_index222: int = 0
        vec_227: List[int] = list()
        vec_index227: int = 0
        vec_232: List[int] = list()
        vec_index232: int = 0
        vec_244: List[int] = list()
        vec_index244: int = 0
        vec_255: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index255: int = 0
        vec_258: List[int] = list()
        vec_index258: int = 0
        vec_262: List[int] = list()
        vec_index262: int = 0
        vec_269: List[int] = list()
        vec_index269: int = 0
        vec_275: List[int] = list()
        vec_index275: int = 0
        vec_281: List[int] = list()
        vec_index281: int = 0
        vec_286: List[int] = list()
        vec_index286: int = 0
        vec_302: List[int] = list()
        vec_index302: int = 0
        vec_308: List[int] = list()
        vec_index308: int = 0
        vec_313: List[int] = list()
        vec_index313: int = 0
        vec_318: List[int] = list()
        vec_index318: int = 0
        vec_323: List[int] = list()
        vec_index323: int = 0
        vec_328: List[int] = list()
        vec_index328: int = 0
        vec_333: List[int] = list()
        vec_index333: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index164 = 0
        while vec_index164 < len(vec_164):
            var_165, var_166, var_167 = vec_164[vec_index164]
            vec_index164 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TupleCompare Region
            if self.var_3 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_96[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_96[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_222.append(var_165)
            # Program TupleCompare Region
            if self.var_4 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_104[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_104[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_217.append(var_165)
            # Program TupleCompare Region
            if self.var_5 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_112[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_112[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_211.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_31[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_31[tuple_165] = 1 | 4
                if not present_bit:
                    pass
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
            # Program TransitionState Region
            tuple_165 = var_165
            prev_state = self.table_49[tuple_165]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_49[tuple_165] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_71[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_258.append(var_165)
                    # Program VectorAppend Region
                    vec_333.append(var_165)
                    # Program VectorAppend Region
                    vec_328.append(var_165)
                    # Program VectorAppend Region
                    vec_323.append(var_165)
                    # Program VectorAppend Region
                    vec_318.append(var_165)
                    # Program VectorAppend Region
                    vec_281.append(var_165)
                    # Program VectorAppend Region
                    vec_313.append(var_165)
                    # Program VectorAppend Region
                    vec_308.append(var_165)
                    # Program VectorAppend Region
                    vec_244.append(var_165)
                # Program VectorAppend Region
                vec_207.append(var_165)
                # Program VectorAppend Region
                vec_203.append(var_165)
                # Program VectorAppend Region
                vec_199.append(var_165)
                # Program VectorAppend Region
                vec_195.append(var_165)
                # Program VectorAppend Region
                vec_191.append(var_165)
                # Program VectorAppend Region
                vec_187.append(var_165)
                # Program VectorAppend Region
                vec_183.append(var_165)
                # Program VectorAppend Region
                vec_168.append(var_165)
            # Program TupleCompare Region
            if self.var_1 == var_166:
                # Program TransitionState Region
                tuple_165 = var_165
                prev_state = self.table_73[tuple_165]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_73[tuple_165] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_232.append(var_165)
                    # Program VectorAppend Region
                    vec_227.append(var_165)
        # Program VectorUnique Region
        vec_168 = list(set(vec_168))
        vec_index168 = 0
        # Program TableJoin Region
        while vec_index168 < len(vec_168):
            var_170 = vec_168[vec_index168]
            vec_index168 += 1
            if var_170 in self.index_171:
                if var_170 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_170 = var_170
                    prev_state = self.table_15[tuple_170]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_170] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_179.append(var_170)
        # Program VectorClear Region
        del vec_168[:]
        vec_index168 = 0
        # Program VectorUnique Region
        vec_183 = list(set(vec_183))
        vec_index183 = 0
        # Program TableJoin Region
        while vec_index183 < len(vec_183):
            var_185 = vec_183[vec_index183]
            vec_index183 += 1
            if var_185 in self.index_186:
                if var_185 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_185 = var_185
                    prev_state = self.table_15[tuple_185]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_185] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_179.append(var_185)
        # Program VectorClear Region
        del vec_183[:]
        vec_index183 = 0
        # Program VectorUnique Region
        vec_187 = list(set(vec_187))
        vec_index187 = 0
        # Program TableJoin Region
        while vec_index187 < len(vec_187):
            var_189 = vec_187[vec_index187]
            vec_index187 += 1
            if var_189 in self.index_190:
                if var_189 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_189 = var_189
                    prev_state = self.table_15[tuple_189]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_189] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_179.append(var_189)
        # Program VectorClear Region
        del vec_187[:]
        vec_index187 = 0
        # Program VectorUnique Region
        vec_191 = list(set(vec_191))
        vec_index191 = 0
        # Program TableJoin Region
        while vec_index191 < len(vec_191):
            var_193 = vec_191[vec_index191]
            vec_index191 += 1
            if var_193 in self.index_194:
                if var_193 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_193 = var_193
                    prev_state = self.table_15[tuple_193]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_193] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_179.append(var_193)
        # Program VectorClear Region
        del vec_191[:]
        vec_index191 = 0
        # Program VectorUnique Region
        vec_195 = list(set(vec_195))
        vec_index195 = 0
        # Program TableJoin Region
        while vec_index195 < len(vec_195):
            var_197 = vec_195[vec_index195]
            vec_index195 += 1
            if var_197 in self.index_198:
                if var_197 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_197 = var_197
                    prev_state = self.table_15[tuple_197]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_197] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_179.append(var_197)
        # Program VectorClear Region
        del vec_195[:]
        vec_index195 = 0
        # Program VectorUnique Region
        vec_199 = list(set(vec_199))
        vec_index199 = 0
        # Program TableJoin Region
        while vec_index199 < len(vec_199):
            var_201 = vec_199[vec_index199]
            vec_index199 += 1
            if var_201 in self.index_202:
                if var_201 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_201 = var_201
                    prev_state = self.table_15[tuple_201]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_201] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_179.append(var_201)
        # Program VectorClear Region
        del vec_199[:]
        vec_index199 = 0
        # Program VectorUnique Region
        vec_203 = list(set(vec_203))
        vec_index203 = 0
        # Program TableJoin Region
        while vec_index203 < len(vec_203):
            var_205 = vec_203[vec_index203]
            vec_index203 += 1
            if var_205 in self.index_206:
                if var_205 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_205 = var_205
                    prev_state = self.table_15[tuple_205]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_205] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_179.append(var_205)
        # Program VectorClear Region
        del vec_203[:]
        vec_index203 = 0
        # Program VectorUnique Region
        vec_207 = list(set(vec_207))
        vec_index207 = 0
        # Program TableJoin Region
        while vec_index207 < len(vec_207):
            var_209 = vec_207[vec_index207]
            vec_index207 += 1
            if var_209 in self.index_210:
                if var_209 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_209 = var_209
                    prev_state = self.table_15[tuple_209]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_209] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_179.append(var_209)
        # Program VectorClear Region
        del vec_207[:]
        vec_index207 = 0
        # Program VectorUnique Region
        vec_211 = list(set(vec_211))
        vec_index211 = 0
        # Program TableJoin Region
        while vec_index211 < len(vec_211):
            var_213 = vec_211[vec_index211]
            vec_index211 += 1
            if var_213 in self.index_214:
                tuple_212_1_index: int = 0
                tuple_212_1_vec: List[int] = self.index_215[var_213]
                while tuple_212_1_index < len(tuple_212_1_vec):
                    tuple_212_1 = tuple_212_1_vec[tuple_212_1_index]
                    tuple_212_1_index += 1
                    var_216 = tuple_212_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_213_216 = (var_213, var_216)
                    prev_state = self.table_114[tuple_213_216]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_114[tuple_213_216] = 1 | 4
                        if not present_bit:
                            self.index_278[tuple_213_216[1]].append(tuple_213_216[0])
                        # Program VectorAppend Region
                        vec_275.append(var_216)
        # Program VectorClear Region
        del vec_211[:]
        vec_index211 = 0
        # Program VectorUnique Region
        vec_217 = list(set(vec_217))
        vec_index217 = 0
        # Program TableJoin Region
        while vec_index217 < len(vec_217):
            var_219 = vec_217[vec_index217]
            vec_index217 += 1
            if var_219 in self.index_220:
                tuple_218_1_index: int = 0
                tuple_218_1_vec: List[int] = self.index_215[var_219]
                while tuple_218_1_index < len(tuple_218_1_vec):
                    tuple_218_1 = tuple_218_1_vec[tuple_218_1_index]
                    tuple_218_1_index += 1
                    var_221 = tuple_218_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_219_221 = (var_219, var_221)
                    prev_state = self.table_106[tuple_219_221]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_106[tuple_219_221] = 1 | 4
                        if not present_bit:
                            self.index_272[tuple_219_221[1]].append(tuple_219_221[0])
                        # Program VectorAppend Region
                        vec_269.append(var_221)
        # Program VectorClear Region
        del vec_217[:]
        vec_index217 = 0
        # Program VectorUnique Region
        vec_222 = list(set(vec_222))
        vec_index222 = 0
        # Program TableJoin Region
        while vec_index222 < len(vec_222):
            var_224 = vec_222[vec_index222]
            vec_index222 += 1
            if var_224 in self.index_225:
                tuple_223_1_index: int = 0
                tuple_223_1_vec: List[int] = self.index_215[var_224]
                while tuple_223_1_index < len(tuple_223_1_vec):
                    tuple_223_1 = tuple_223_1_vec[tuple_223_1_index]
                    tuple_223_1_index += 1
                    var_226 = tuple_223_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_224_226 = (var_224, var_226)
                    prev_state = self.table_98[tuple_224_226]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_98[tuple_224_226] = 1 | 4
                        if not present_bit:
                            self.index_266[tuple_224_226[1]].append(tuple_224_226[0])
                        # Program VectorAppend Region
                        vec_262.append(var_226)
        # Program VectorClear Region
        del vec_222[:]
        vec_index222 = 0
        # Program VectorUnique Region
        vec_227 = list(set(vec_227))
        vec_index227 = 0
        # Program TableJoin Region
        while vec_index227 < len(vec_227):
            var_229 = vec_227[vec_index227]
            vec_index227 += 1
            if var_229 in self.index_230:
                tuple_228_1_index: int = 0
                tuple_228_1_vec: List[int] = self.index_215[var_229]
                while tuple_228_1_index < len(tuple_228_1_vec):
                    tuple_228_1 = tuple_228_1_vec[tuple_228_1_index]
                    tuple_228_1_index += 1
                    var_231 = tuple_228_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_229_231 = (var_229, var_231)
                    prev_state = self.table_90[tuple_229_231]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_90[tuple_229_231] = 1 | 4
                        if not present_bit:
                            self.index_305[tuple_229_231[1]].append(tuple_229_231[0])
                        # Program VectorAppend Region
                        vec_302.append(var_231)
        # Program VectorClear Region
        del vec_227[:]
        vec_index227 = 0
        # Program VectorUnique Region
        vec_232 = list(set(vec_232))
        vec_index232 = 0
        # Program TableJoin Region
        while vec_index232 < len(vec_232):
            var_234 = vec_232[vec_index232]
            vec_index232 += 1
            if var_234 in self.index_230:
                tuple_233_1_index: int = 0
                tuple_233_1_vec: List[int] = self.index_235[var_234]
                while tuple_233_1_index < len(tuple_233_1_vec):
                    tuple_233_1 = tuple_233_1_vec[tuple_233_1_index]
                    tuple_233_1_index += 1
                    var_236 = tuple_233_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_237_(var_234)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_240_(var_234, var_236)
                        if ret:
                            # Program TransitionState Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                            tuple_234_236 = (var_234, var_236)
                            prev_state = self.table_78[tuple_234_236]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_78[tuple_234_236] = 1 | 4
                                if not present_bit:
                                    self.index_290[tuple_234_236[1]].append(tuple_234_236[0])
                                    self.index_957[tuple_234_236[0]].append(tuple_234_236[1])
                                # Program VectorAppend Region
                                vec_286.append(var_236)
        # Program VectorClear Region
        del vec_232[:]
        vec_index232 = 0
        # Program VectorUnique Region
        vec_244 = list(set(vec_244))
        vec_index244 = 0
        # Program TableJoin Region
        while vec_index244 < len(vec_244):
            var_246 = vec_244[vec_index244]
            vec_index244 += 1
            tuple_245_0_index: int = 0
            tuple_245_0_vec: List[Tuple[ControlFlowEdgeKind, int]] = self.index_247[var_246]
            while tuple_245_0_index < len(tuple_245_0_vec):
                tuple_245_0 = tuple_245_0_vec[tuple_245_0_index]
                tuple_245_0_index += 1
                var_249 = tuple_245_0[0]
                var_250 = tuple_245_0[1]
                if var_246 in self.index_248:
                    # Program TransitionState Region
                    var_249 = self._resolve_edgetype(var_249)
                    tuple_250_246_249 = (var_250, var_246, var_249)
                    prev_state = self.table_11[tuple_250_246_249]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_250_246_249] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_250_246_249[1], tuple_250_246_249[2])].append(tuple_250_246_249[0])
                        # Program VectorAppend Region
                        var_249 = self._resolve_edgetype(var_249)
                        vec_255.append((var_250, var_246, var_249))
        # Program VectorClear Region
        del vec_244[:]
        vec_index244 = 0
        # Program VectorUnique Region
        vec_258 = list(set(vec_258))
        vec_index258 = 0
        # Program TableJoin Region
        while vec_index258 < len(vec_258):
            var_260 = vec_258[vec_index258]
            vec_index258 += 1
            if var_260 in self.index_261:
                if var_260 in self.index_248:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_260 = var_260
                    prev_state = self.table_15[tuple_260]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_260] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_179.append(var_260)
        # Program VectorClear Region
        del vec_258[:]
        vec_index258 = 0
        # Program VectorUnique Region
        vec_262 = list(set(vec_262))
        vec_index262 = 0
        # Program TableJoin Region
        while vec_index262 < len(vec_262):
            var_264 = vec_262[vec_index262]
            vec_index262 += 1
            tuple_263_0_index: int = 0
            tuple_263_0_vec: List[int] = self.index_265[var_264]
            while tuple_263_0_index < len(tuple_263_0_vec):
                tuple_263_0 = tuple_263_0_vec[tuple_263_0_index]
                tuple_263_0_index += 1
                var_267 = tuple_263_0
                tuple_263_1_index: int = 0
                tuple_263_1_vec: List[int] = self.index_266[var_264]
                while tuple_263_1_index < len(tuple_263_1_vec):
                    tuple_263_1 = tuple_263_1_vec[tuple_263_1_index]
                    tuple_263_1_index += 1
                    var_268 = tuple_263_1
                    # Program TransitionState Region
                    tuple_267_268 = (var_267, var_268)
                    prev_state = self.table_101[tuple_267_268]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_101[tuple_267_268] = 1 | 4
                        if not present_bit:
                            self.index_331[tuple_267_268[0]].append(tuple_267_268[1])
                        # Program VectorAppend Region
                        vec_328.append(var_267)
        # Program VectorClear Region
        del vec_262[:]
        vec_index262 = 0
        # Program VectorUnique Region
        vec_269 = list(set(vec_269))
        vec_index269 = 0
        # Program TableJoin Region
        while vec_index269 < len(vec_269):
            var_271 = vec_269[vec_index269]
            vec_index269 += 1
            tuple_270_0_index: int = 0
            tuple_270_0_vec: List[int] = self.index_265[var_271]
            while tuple_270_0_index < len(tuple_270_0_vec):
                tuple_270_0 = tuple_270_0_vec[tuple_270_0_index]
                tuple_270_0_index += 1
                var_273 = tuple_270_0
                tuple_270_1_index: int = 0
                tuple_270_1_vec: List[int] = self.index_272[var_271]
                while tuple_270_1_index < len(tuple_270_1_vec):
                    tuple_270_1 = tuple_270_1_vec[tuple_270_1_index]
                    tuple_270_1_index += 1
                    var_274 = tuple_270_1
                    # Program TransitionState Region
                    tuple_273_274 = (var_273, var_274)
                    prev_state = self.table_109[tuple_273_274]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_273_274] = 1 | 4
                        if not present_bit:
                            self.index_326[tuple_273_274[0]].append(tuple_273_274[1])
                        # Program VectorAppend Region
                        vec_323.append(var_273)
        # Program VectorClear Region
        del vec_269[:]
        vec_index269 = 0
        # Program VectorUnique Region
        vec_275 = list(set(vec_275))
        vec_index275 = 0
        # Program TableJoin Region
        while vec_index275 < len(vec_275):
            var_277 = vec_275[vec_index275]
            vec_index275 += 1
            tuple_276_0_index: int = 0
            tuple_276_0_vec: List[int] = self.index_265[var_277]
            while tuple_276_0_index < len(tuple_276_0_vec):
                tuple_276_0 = tuple_276_0_vec[tuple_276_0_index]
                tuple_276_0_index += 1
                var_279 = tuple_276_0
                tuple_276_1_index: int = 0
                tuple_276_1_vec: List[int] = self.index_278[var_277]
                while tuple_276_1_index < len(tuple_276_1_vec):
                    tuple_276_1 = tuple_276_1_vec[tuple_276_1_index]
                    tuple_276_1_index += 1
                    var_280 = tuple_276_1
                    # Program TransitionState Region
                    tuple_279_280 = (var_279, var_280)
                    prev_state = self.table_117[tuple_279_280]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_117[tuple_279_280] = 1 | 4
                        if not present_bit:
                            self.index_321[tuple_279_280[0]].append(tuple_279_280[1])
                        # Program VectorAppend Region
                        vec_318.append(var_279)
        # Program VectorClear Region
        del vec_275[:]
        vec_index275 = 0
        # Program VectorUnique Region
        vec_281 = list(set(vec_281))
        vec_index281 = 0
        # Program TableJoin Region
        while vec_index281 < len(vec_281):
            var_283 = vec_281[vec_index281]
            vec_index281 += 1
            if var_283 in self.index_248:
                tuple_282_1_index: int = 0
                tuple_282_1_vec: List[int] = self.index_284[var_283]
                while tuple_282_1_index < len(tuple_282_1_vec):
                    tuple_282_1 = tuple_282_1_vec[tuple_282_1_index]
                    tuple_282_1_index += 1
                    var_285 = tuple_282_1
                    # Program TransitionState Region
                    tuple_285_283_6 = (var_285, var_283, self.var_6)
                    prev_state = self.table_11[tuple_285_283_6]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_285_283_6] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_285_283_6[1], tuple_285_283_6[2])].append(tuple_285_283_6[0])
                        # Program VectorAppend Region
                        vec_255.append((var_285, var_283, self.var_6))
        # Program VectorClear Region
        del vec_281[:]
        vec_index281 = 0
        # Program VectorUnique Region
        vec_286 = list(set(vec_286))
        vec_index286 = 0
        # Program TableJoin Region
        while vec_index286 < len(vec_286):
            var_288 = vec_286[vec_index286]
            vec_index286 += 1
            if var_288 in self.index_289:
                tuple_287_1_index: int = 0
                tuple_287_1_vec: List[int] = self.index_290[var_288]
                while tuple_287_1_index < len(tuple_287_1_vec):
                    tuple_287_1 = tuple_287_1_vec[tuple_287_1_index]
                    tuple_287_1_index += 1
                    var_291 = tuple_287_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_292_(var_288)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_295_(var_291, var_288)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_299_(var_291)
                            if not ret:
                                # Program TransitionState Region
                                tuple_291 = var_291
                                prev_state = self.table_15[tuple_291]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_291] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_179.append(var_291)
        # Program VectorClear Region
        del vec_286[:]
        vec_index286 = 0
        # Program VectorUnique Region
        vec_302 = list(set(vec_302))
        vec_index302 = 0
        # Program TableJoin Region
        while vec_index302 < len(vec_302):
            var_304 = vec_302[vec_index302]
            vec_index302 += 1
            tuple_303_0_index: int = 0
            tuple_303_0_vec: List[int] = self.index_265[var_304]
            while tuple_303_0_index < len(tuple_303_0_vec):
                tuple_303_0 = tuple_303_0_vec[tuple_303_0_index]
                tuple_303_0_index += 1
                var_306 = tuple_303_0
                tuple_303_1_index: int = 0
                tuple_303_1_vec: List[int] = self.index_305[var_304]
                while tuple_303_1_index < len(tuple_303_1_vec):
                    tuple_303_1 = tuple_303_1_vec[tuple_303_1_index]
                    tuple_303_1_index += 1
                    var_307 = tuple_303_1
                    # Program TransitionState Region
                    tuple_306_307 = (var_306, var_307)
                    prev_state = self.table_93[tuple_306_307]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_93[tuple_306_307] = 1 | 4
                        if not present_bit:
                            self.index_336[tuple_306_307[0]].append(tuple_306_307[1])
                        # Program VectorAppend Region
                        vec_333.append(var_306)
        # Program VectorClear Region
        del vec_302[:]
        vec_index302 = 0
        # Program VectorUnique Region
        vec_308 = list(set(vec_308))
        vec_index308 = 0
        # Program TableJoin Region
        while vec_index308 < len(vec_308):
            var_310 = vec_308[vec_index308]
            vec_index308 += 1
            if var_310 in self.index_248:
                tuple_309_1_index: int = 0
                tuple_309_1_vec: List[int] = self.index_311[var_310]
                while tuple_309_1_index < len(tuple_309_1_vec):
                    tuple_309_1 = tuple_309_1_vec[tuple_309_1_index]
                    tuple_309_1_index += 1
                    var_312 = tuple_309_1
                    # Program TransitionState Region
                    tuple_312_310_7 = (var_312, var_310, self.var_7)
                    prev_state = self.table_11[tuple_312_310_7]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_312_310_7] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_312_310_7[1], tuple_312_310_7[2])].append(tuple_312_310_7[0])
                        # Program VectorAppend Region
                        vec_255.append((var_312, var_310, self.var_7))
        # Program VectorClear Region
        del vec_308[:]
        vec_index308 = 0
        # Program VectorUnique Region
        vec_313 = list(set(vec_313))
        vec_index313 = 0
        # Program TableJoin Region
        while vec_index313 < len(vec_313):
            var_315 = vec_313[vec_index313]
            vec_index313 += 1
            if var_315 in self.index_248:
                tuple_314_1_index: int = 0
                tuple_314_1_vec: List[int] = self.index_316[var_315]
                while tuple_314_1_index < len(tuple_314_1_vec):
                    tuple_314_1 = tuple_314_1_vec[tuple_314_1_index]
                    tuple_314_1_index += 1
                    var_317 = tuple_314_1
                    # Program TransitionState Region
                    tuple_317_315_0 = (var_317, var_315, self.var_0)
                    prev_state = self.table_11[tuple_317_315_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_317_315_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_317_315_0[1], tuple_317_315_0[2])].append(tuple_317_315_0[0])
                        # Program VectorAppend Region
                        vec_255.append((var_317, var_315, self.var_0))
        # Program VectorClear Region
        del vec_313[:]
        vec_index313 = 0
        # Program VectorUnique Region
        vec_318 = list(set(vec_318))
        vec_index318 = 0
        # Program TableJoin Region
        while vec_index318 < len(vec_318):
            var_320 = vec_318[vec_index318]
            vec_index318 += 1
            if var_320 in self.index_248:
                tuple_319_1_index: int = 0
                tuple_319_1_vec: List[int] = self.index_321[var_320]
                while tuple_319_1_index < len(tuple_319_1_vec):
                    tuple_319_1 = tuple_319_1_vec[tuple_319_1_index]
                    tuple_319_1_index += 1
                    var_322 = tuple_319_1
                    # Program TransitionState Region
                    tuple_322_320_0 = (var_322, var_320, self.var_0)
                    prev_state = self.table_11[tuple_322_320_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_322_320_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_322_320_0[1], tuple_322_320_0[2])].append(tuple_322_320_0[0])
                        # Program VectorAppend Region
                        vec_255.append((var_322, var_320, self.var_0))
        # Program VectorClear Region
        del vec_318[:]
        vec_index318 = 0
        # Program VectorUnique Region
        vec_323 = list(set(vec_323))
        vec_index323 = 0
        # Program TableJoin Region
        while vec_index323 < len(vec_323):
            var_325 = vec_323[vec_index323]
            vec_index323 += 1
            if var_325 in self.index_248:
                tuple_324_1_index: int = 0
                tuple_324_1_vec: List[int] = self.index_326[var_325]
                while tuple_324_1_index < len(tuple_324_1_vec):
                    tuple_324_1 = tuple_324_1_vec[tuple_324_1_index]
                    tuple_324_1_index += 1
                    var_327 = tuple_324_1
                    # Program TransitionState Region
                    tuple_327_325_0 = (var_327, var_325, self.var_0)
                    prev_state = self.table_11[tuple_327_325_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_327_325_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_327_325_0[1], tuple_327_325_0[2])].append(tuple_327_325_0[0])
                        # Program VectorAppend Region
                        vec_255.append((var_327, var_325, self.var_0))
        # Program VectorClear Region
        del vec_323[:]
        vec_index323 = 0
        # Program VectorUnique Region
        vec_328 = list(set(vec_328))
        vec_index328 = 0
        # Program TableJoin Region
        while vec_index328 < len(vec_328):
            var_330 = vec_328[vec_index328]
            vec_index328 += 1
            if var_330 in self.index_248:
                tuple_329_1_index: int = 0
                tuple_329_1_vec: List[int] = self.index_331[var_330]
                while tuple_329_1_index < len(tuple_329_1_vec):
                    tuple_329_1 = tuple_329_1_vec[tuple_329_1_index]
                    tuple_329_1_index += 1
                    var_332 = tuple_329_1
                    # Program TransitionState Region
                    tuple_332_330_2 = (var_332, var_330, self.var_2)
                    prev_state = self.table_11[tuple_332_330_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_332_330_2] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_332_330_2[1], tuple_332_330_2[2])].append(tuple_332_330_2[0])
                        # Program VectorAppend Region
                        vec_255.append((var_332, var_330, self.var_2))
        # Program VectorClear Region
        del vec_328[:]
        vec_index328 = 0
        # Program VectorUnique Region
        vec_333 = list(set(vec_333))
        vec_index333 = 0
        # Program TableJoin Region
        while vec_index333 < len(vec_333):
            var_335 = vec_333[vec_index333]
            vec_index333 += 1
            if var_335 in self.index_248:
                tuple_334_1_index: int = 0
                tuple_334_1_vec: List[int] = self.index_336[var_335]
                while tuple_334_1_index < len(tuple_334_1_vec):
                    tuple_334_1 = tuple_334_1_vec[tuple_334_1_index]
                    tuple_334_1_index += 1
                    var_337 = tuple_334_1
                    # Program TransitionState Region
                    tuple_337_335_2 = (var_337, var_335, self.var_2)
                    prev_state = self.table_11[tuple_337_335_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_337_335_2] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_337_335_2[1], tuple_337_335_2[2])].append(tuple_337_335_2[0])
                        # Program VectorAppend Region
                        vec_255.append((var_337, var_335, self.var_2))
        # Program VectorClear Region
        del vec_333[:]
        vec_index333 = 0
        # Induction Fixpoint Loop Region
        while len(vec_255) or len(vec_179) or len(vec_180):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_179, vec_180)

            # Program Call Region
            param_182_0 = [vec_179]
            param_182_1 = [vec_180]
            ret = self.proc_173_(param_182_0, param_182_1)
            vec_179 = param_182_0[0]
            vec_180 = param_182_1[0]

            # Program Call Region
            ret = self.proc_253_(vec_255)

            # Program Call Region
            param_257_0 = [vec_255]
            ret = self.proc_251_(param_257_0)
            vec_255 = param_257_0[0]

        vec_index255 = 0
        vec_index179 = 0
        vec_index180 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_179[:]
        vec_index179 = 0
        # Program VectorClear Region
        del vec_180[:]
        vec_index180 = 0
        # Program VectorClear Region
        del vec_255[:]
        vec_index255 = 0
        # Program Return Region
        return False
        return False

    def proc_173_(self, param_0: List[List[int]], param_1: List[List[Tuple[int, int, ControlFlowEdgeKind]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_174 = param_0[0]
        vec_175 = param_1[0]
        vec_index174: int = 0
        vec_index175: int = 0
        vec_357: List[int] = list()
        vec_index357: int = 0
        vec_358: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index358: int = 0
        vec_364: List[int] = list()
        vec_index364: int = 0
        vec_375: List[int] = list()
        vec_index375: int = 0
        vec_385: List[int] = list()
        vec_index385: int = 0
        vec_391: List[int] = list()
        vec_index391: int = 0
        vec_398: List[int] = list()
        vec_index398: int = 0
        vec_415: List[int] = list()
        vec_index415: int = 0
        vec_418: List[int] = list()
        vec_index418: int = 0
        vec_433: List[int] = list()
        vec_index433: int = 0
        vec_447: List[int] = list()
        vec_index447: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorSwap Region
        vec_174, vec_357 = vec_357, vec_174
        # Program VectorSwap Region
        vec_175, vec_358 = vec_358, vec_175
        # Program Parallel Region
        # Program VectorLoop Region
        while vec_index357 < len(vec_357):
            var_359 = vec_357[vec_index357]
            vec_index357 += 1
            # Program Series Region
            # Program Parallel Region
            # Program Series Region
            # Program TableScan Region
            scan_tuple_364: int
            scan_index_364: int = 0
            scan_tuple_364_vec: List[int] = self.index_363[var_359]
            while scan_index_364 < len(scan_tuple_364_vec):
                scan_tuple_364 = scan_tuple_364_vec[scan_index_364]
                scan_index_364 += 1
                vec_364.append(scan_tuple_364)
            # Program VectorLoop Region
            vec_index364 = 0
            while vec_index364 < len(vec_364):
                var_365 = vec_364[vec_index364]
                vec_index364 += 1
                # Program TransitionState Region
                # Remove from negated view
                tuple_359_365 = (var_359, var_365)
                prev_state = self.table_44[tuple_359_365]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 1:
                    self.table_44[tuple_359_365] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    ret = self.proc_366_(var_359, var_365)

                    # Program Call Region
                    ret = self.proc_370_(var_359, var_365)

            # Program Series Region
            # Program TableScan Region
            scan_tuple_375: int
            scan_index_375: int = 0
            scan_tuple_375_vec: List[int] = self.index_374[var_359]
            while scan_index_375 < len(scan_tuple_375_vec):
                scan_tuple_375 = scan_tuple_375_vec[scan_index_375]
                scan_index_375 += 1
                vec_375.append(scan_tuple_375)
            # Program VectorLoop Region
            vec_index375 = 0
            while vec_index375 < len(vec_375):
                var_376 = vec_375[vec_index375]
                vec_index375 += 1
                # Program TransitionState Region
                # Remove from negated view
                tuple_359_376 = (var_359, var_376)
                prev_state = self.table_41[tuple_359_376]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 1:
                    self.table_41[tuple_359_376] = 0 | 4
                    # Program Call Region
                    ret = self.proc_377_(var_359, var_376)

            # Program Parallel Region
            # Program VectorAppend Region
            vec_391.append(var_359)
            # Program VectorAppend Region
            vec_398.append(var_359)
            # Program VectorAppend Region
            vec_418.append(var_359)
            # Program VectorAppend Region
            vec_433.append(var_359)
        # Program VectorLoop Region
        while vec_index358 < len(vec_358):
            var_360, var_361, var_362 = vec_358[vec_index358]
            vec_index358 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_2 == var_362:
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                ret = self.proc_240_(var_360, var_361)
                if not ret:
                    # Program TransitionState Region
                    tuple_360_361 = (var_360, var_361)
                    prev_state = self.table_75[tuple_360_361]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_75[tuple_360_361] = 1 | 4
                        if not present_bit:
                            self.index_235[tuple_360_361[0]].append(tuple_360_361[1])
                        # Program VectorAppend Region
                        vec_385.append(var_360)
            # Program TupleCompare Region
            if self.var_0 == var_362:
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                ret = self.proc_382_(var_361)
                if not ret:
                    # Program TransitionState Region
                    tuple_361 = var_361
                    prev_state = self.table_15[tuple_361]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_361] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_174.append(var_361)
        # Program VectorUnique Region
        vec_385 = list(set(vec_385))
        vec_index385 = 0
        # Program TableJoin Region
        while vec_index385 < len(vec_385):
            var_387 = vec_385[vec_index385]
            vec_index385 += 1
            if var_387 in self.index_230:
                tuple_386_1_index: int = 0
                tuple_386_1_vec: List[int] = self.index_235[var_387]
                while tuple_386_1_index < len(tuple_386_1_vec):
                    tuple_386_1 = tuple_386_1_vec[tuple_386_1_index]
                    tuple_386_1_index += 1
                    var_388 = tuple_386_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_237_(var_387)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_240_(var_387, var_388)
                        if ret:
                            # Program TransitionState Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                            tuple_387_388 = (var_387, var_388)
                            prev_state = self.table_78[tuple_387_388]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_78[tuple_387_388] = 1 | 4
                                if not present_bit:
                                    self.index_290[tuple_387_388[1]].append(tuple_387_388[0])
                                    self.index_957[tuple_387_388[0]].append(tuple_387_388[1])
                                # Program VectorAppend Region
                                vec_391.append(var_388)
        # Program VectorClear Region
        del vec_385[:]
        vec_index385 = 0
        # Program VectorUnique Region
        vec_391 = list(set(vec_391))
        vec_index391 = 0
        # Program TableJoin Region
        while vec_index391 < len(vec_391):
            var_393 = vec_391[vec_index391]
            vec_index391 += 1
            if var_393 in self.index_289:
                tuple_392_1_index: int = 0
                tuple_392_1_vec: List[int] = self.index_290[var_393]
                while tuple_392_1_index < len(tuple_392_1_vec):
                    tuple_392_1 = tuple_392_1_vec[tuple_392_1_index]
                    tuple_392_1_index += 1
                    var_394 = tuple_392_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_292_(var_393)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_295_(var_394, var_393)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_299_(var_394)
                            if not ret:
                                # Program TransitionState Region
                                tuple_394 = var_394
                                prev_state = self.table_15[tuple_394]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_15[tuple_394] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_174.append(var_394)
        # Program VectorClear Region
        del vec_391[:]
        vec_index391 = 0
        # Program VectorUnique Region
        vec_398 = list(set(vec_398))
        vec_index398 = 0
        # Program TableJoin Region
        while vec_index398 < len(vec_398):
            var_400 = vec_398[vec_index398]
            vec_index398 += 1
            tuple_399_0_index: int = 0
            tuple_399_0_vec: List[int] = self.index_401[var_400]
            while tuple_399_0_index < len(tuple_399_0_vec):
                tuple_399_0 = tuple_399_0_vec[tuple_399_0_index]
                tuple_399_0_index += 1
                var_402 = tuple_399_0
                if var_400 in self.index_289:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_403_(var_402, var_400)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_292_(var_400)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_408_(var_402)
                            if not ret:
                                # Program TransitionState Region
                                tuple_402 = var_402
                                prev_state = self.table_24[tuple_402]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_24[tuple_402] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_415.append(var_402)
        # Program VectorClear Region
        del vec_398[:]
        vec_index398 = 0
        # Program VectorUnique Region
        vec_418 = list(set(vec_418))
        vec_index418 = 0
        # Program TableJoin Region
        while vec_index418 < len(vec_418):
            var_420 = vec_418[vec_index418]
            vec_index418 += 1
            tuple_419_0_index: int = 0
            tuple_419_0_vec: List[int] = self.index_421[var_420]
            while tuple_419_0_index < len(tuple_419_0_vec):
                tuple_419_0 = tuple_419_0_vec[tuple_419_0_index]
                tuple_419_0_index += 1
                var_422 = tuple_419_0
                if var_420 in self.index_289:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_423_(var_422, var_420)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_292_(var_420)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_428_(var_422, var_420, self.var_10)
                            if not ret:
                                # Program TransitionState Region
                                tuple_422_420_10 = (var_422, var_420, self.var_10)
                                prev_state = self.table_20[tuple_422_420_10]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_20[tuple_422_420_10] = 1 | 4
                                    if not present_bit:
                                        self.index_969[(tuple_422_420_10[1], tuple_422_420_10[2])].append(tuple_422_420_10[0])
                                        self.index_1062[(tuple_422_420_10[0], tuple_422_420_10[1])].append(tuple_422_420_10[2])
                                        self.index_1488[tuple_422_420_10[1]].append((tuple_422_420_10[0], tuple_422_420_10[2]))
                                    # Program VectorAppend Region
                                    vec_175.append((var_422, var_420, self.var_10))
        # Program VectorClear Region
        del vec_418[:]
        vec_index418 = 0
        # Program VectorUnique Region
        vec_433 = list(set(vec_433))
        vec_index433 = 0
        # Program TableJoin Region
        while vec_index433 < len(vec_433):
            var_435 = vec_433[vec_index433]
            vec_index433 += 1
            tuple_434_0_index: int = 0
            tuple_434_0_vec: List[int] = self.index_436[var_435]
            while tuple_434_0_index < len(tuple_434_0_vec):
                tuple_434_0 = tuple_434_0_vec[tuple_434_0_index]
                tuple_434_0_index += 1
                var_437 = tuple_434_0
                if var_435 in self.index_289:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_438_(var_437, var_435)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_292_(var_435)
                        if ret:
                            # Program Parallel Region
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_443_(var_437, var_435)
                            if not ret:
                                # Program TransitionState Region
                                tuple_437_435 = (var_437, var_435)
                                prev_state = self.table_154[tuple_437_435]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_154[tuple_437_435] = 1 | 4
                                    if not present_bit:
                                        self.index_450[tuple_437_435[1]].append(tuple_437_435[0])
                                        self.index_1073[tuple_437_435[0]].append(tuple_437_435[1])
                                    # Program VectorAppend Region
                                    vec_447.append(var_435)
                            # Program TransitionState Region
                            tuple_437_435 = (var_437, var_435)
                            prev_state = self.table_33[tuple_437_435]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_33[tuple_437_435] = 1 | 4
                                if not present_bit:
                                    self.index_886[tuple_437_435[0]].append(tuple_437_435[1])
        # Program VectorClear Region
        del vec_433[:]
        vec_index433 = 0
        # Program VectorUnique Region
        vec_447 = list(set(vec_447))
        vec_index447 = 0
        # Program TableJoin Region
        while vec_index447 < len(vec_447):
            var_449 = vec_447[vec_index447]
            vec_index447 += 1
            tuple_448_0_index: int = 0
            tuple_448_0_vec: List[int] = self.index_450[var_449]
            while tuple_448_0_index < len(tuple_448_0_vec):
                tuple_448_0 = tuple_448_0_vec[tuple_448_0_index]
                tuple_448_0_index += 1
                var_452 = tuple_448_0
                if var_449 in self.index_451:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_443_(var_452, var_449)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_454_(var_449)
                        if ret:
                            # Program TransitionState Region
                            tuple_452 = var_452
                            prev_state = self.table_26[tuple_452]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_26[tuple_452] = 1 | 4
                                if not present_bit:
                                    pass
        # Program VectorClear Region
        del vec_447[:]
        vec_index447 = 0
        # Induction Fixpoint Loop Region
        while len(vec_415):
            # Program Call Region
            param_417_0 = [vec_415]
            ret = self.proc_411_(param_417_0)
            vec_415 = param_417_0[0]

        vec_index415 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_415[:]
        vec_index415 = 0
        # Program Return Region
        param_0[0] = vec_174
        param_1[0] = vec_175
        return False
        return False

    def proc_176_(self, vec_177: List[int], vec_178: List[Tuple[int, int, ControlFlowEdgeKind]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index177: int = 0
        vec_index178: int = 0
        vec_519: List[Tuple[int, int]] = list()
        vec_index519: int = 0
        vec_530: List[int] = list()
        vec_index530: int = 0
        vec_537: List[int] = list()
        vec_index537: int = 0
        vec_540: List[int] = list()
        vec_index540: int = 0
        vec_547: List[int] = list()
        vec_index547: int = 0
        vec_554: List[int] = list()
        vec_index554: int = 0
        vec_570: List[int] = list()
        vec_index570: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program Parallel Region
        # Program VectorLoop Region
        while vec_index177 < len(vec_177):
            var_507 = vec_177[vec_index177]
            vec_index177 += 1
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
            ret = self.proc_511_(var_507, var_507)
            if not ret:
                # Program TransitionState Region
                tuple_507_507 = (var_507, var_507)
                prev_state = self.table_17[tuple_507_507]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_17[tuple_507_507] = 1 | 4
                    if not present_bit:
                        self.index_557[tuple_507_507[1]].append(tuple_507_507[0])
                        self.index_882[tuple_507_507[0]].append(tuple_507_507[1])
                    # Program VectorAppend Region
                    vec_519.append((var_507, var_507))
        # Program VectorLoop Region
        while vec_index178 < len(vec_178):
            var_508, var_509, var_510 = vec_178[vec_index178]
            vec_index178 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_8 == var_510:
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                ret = self.proc_403_(var_508, var_509)
                if not ret:
                    # Program TransitionState Region
                    tuple_508_509 = (var_508, var_509)
                    prev_state = self.table_145[tuple_508_509]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_145[tuple_508_509] = 1 | 4
                        if not present_bit:
                            self.index_401[tuple_508_509[1]].append(tuple_508_509[0])
                            self.index_1103[tuple_508_509[0]].append(tuple_508_509[1])
                        # Program Parallel Region
                        # Program VectorAppend Region
                        vec_540.append(var_509)
                        # Program VectorAppend Region
                        vec_530.append(var_509)
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
            ret = self.proc_438_(var_508, var_509)
            if not ret:
                # Program TransitionState Region
                tuple_508_509 = (var_508, var_509)
                prev_state = self.table_151[tuple_508_509]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_151[tuple_508_509] = 1 | 4
                    if not present_bit:
                        self.index_436[tuple_508_509[1]].append(tuple_508_509[0])
                    # Program VectorAppend Region
                    vec_547.append(var_509)
            # Program Series Region
            # Program TransitionState Region
            # Eager insert before negation to prevent race
            tuple_509_508 = (var_509, var_508)
            prev_state = self.table_44[tuple_509_508]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0:
                self.table_44[tuple_509_508] = 2 | 4
                if not present_bit:
                    self.index_363[tuple_509_508[0]].append(tuple_509_508[1])
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_292_(var_509)
            if not ret:
                # Program TransitionState Region
                tuple_509_508 = (var_509, var_508)
                prev_state = self.table_44[tuple_509_508]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_44[tuple_509_508] = 1 | 4
                    if not present_bit:
                        self.index_363[tuple_509_508[0]].append(tuple_509_508[1])
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                    ret = self.proc_526_(var_508, var_509)
                    if not ret:
                        # Program TransitionState Region
                        tuple_508_509 = (var_508, var_509)
                        prev_state = self.table_81[tuple_508_509]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_81[tuple_508_509] = 1 | 4
                            if not present_bit:
                                self.index_558[tuple_508_509[0]].append(tuple_508_509[1])
                                self.index_917[tuple_508_509[1]].append(tuple_508_509[0])
                            # Program VectorAppend Region
                            vec_554.append(var_508)
                    # Program TransitionState Region
                    tuple_508_509 = (var_508, var_509)
                    prev_state = self.table_28[tuple_508_509]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_28[tuple_508_509] = 1 | 4
                        if not present_bit:
                            self.index_876[tuple_508_509[0]].append(tuple_508_509[1])
        # Program VectorUnique Region
        vec_530 = list(set(vec_530))
        vec_index530 = 0
        # Program TableJoin Region
        while vec_index530 < len(vec_530):
            var_532 = vec_530[vec_index530]
            vec_index530 += 1
            tuple_531_0_index: int = 0
            tuple_531_0_vec: List[int] = self.index_401[var_532]
            while tuple_531_0_index < len(tuple_531_0_vec):
                tuple_531_0 = tuple_531_0_vec[tuple_531_0_index]
                tuple_531_0_index += 1
                var_533 = tuple_531_0
                if var_532 in self.index_469:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_403_(var_533, var_532)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_472_(var_532)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_475_(var_533)
                            if not ret:
                                # Program TransitionState Region
                                tuple_533 = var_533
                                prev_state = self.table_24[tuple_533]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_24[tuple_533] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_537.append(var_533)
        # Program VectorClear Region
        del vec_530[:]
        vec_index530 = 0
        # Program VectorUnique Region
        vec_540 = list(set(vec_540))
        vec_index540 = 0
        # Program TableJoin Region
        while vec_index540 < len(vec_540):
            var_542 = vec_540[vec_index540]
            vec_index540 += 1
            tuple_541_0_index: int = 0
            tuple_541_0_vec: List[int] = self.index_401[var_542]
            while tuple_541_0_index < len(tuple_541_0_vec):
                tuple_541_0 = tuple_541_0_vec[tuple_541_0_index]
                tuple_541_0_index += 1
                var_543 = tuple_541_0
                if var_542 in self.index_289:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_403_(var_543, var_542)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_292_(var_542)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_408_(var_543)
                            if not ret:
                                # Program TransitionState Region
                                tuple_543 = var_543
                                prev_state = self.table_24[tuple_543]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_24[tuple_543] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_537.append(var_543)
        # Program VectorClear Region
        del vec_540[:]
        vec_index540 = 0
        # Program VectorUnique Region
        vec_547 = list(set(vec_547))
        vec_index547 = 0
        # Program TableJoin Region
        while vec_index547 < len(vec_547):
            var_549 = vec_547[vec_index547]
            vec_index547 += 1
            tuple_548_0_index: int = 0
            tuple_548_0_vec: List[int] = self.index_436[var_549]
            while tuple_548_0_index < len(tuple_548_0_vec):
                tuple_548_0 = tuple_548_0_vec[tuple_548_0_index]
                tuple_548_0_index += 1
                var_550 = tuple_548_0
                if var_549 in self.index_289:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_438_(var_550, var_549)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_292_(var_549)
                        if ret:
                            # Program Parallel Region
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_443_(var_550, var_549)
                            if not ret:
                                # Program TransitionState Region
                                tuple_550_549 = (var_550, var_549)
                                prev_state = self.table_154[tuple_550_549]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_154[tuple_550_549] = 1 | 4
                                    if not present_bit:
                                        self.index_450[tuple_550_549[1]].append(tuple_550_549[0])
                                        self.index_1073[tuple_550_549[0]].append(tuple_550_549[1])
                                    # Program VectorAppend Region
                                    vec_570.append(var_549)
                            # Program TransitionState Region
                            tuple_550_549 = (var_550, var_549)
                            prev_state = self.table_33[tuple_550_549]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_33[tuple_550_549] = 1 | 4
                                if not present_bit:
                                    self.index_886[tuple_550_549[0]].append(tuple_550_549[1])
        # Program VectorClear Region
        del vec_547[:]
        vec_index547 = 0
        # Program VectorUnique Region
        vec_554 = list(set(vec_554))
        vec_index554 = 0
        # Program TableJoin Region
        while vec_index554 < len(vec_554):
            var_556 = vec_554[vec_index554]
            vec_index554 += 1
            tuple_555_0_index: int = 0
            tuple_555_0_vec: List[int] = self.index_557[var_556]
            while tuple_555_0_index < len(tuple_555_0_vec):
                tuple_555_0 = tuple_555_0_vec[tuple_555_0_index]
                tuple_555_0_index += 1
                var_559 = tuple_555_0
                tuple_555_1_index: int = 0
                tuple_555_1_vec: List[int] = self.index_558[var_556]
                while tuple_555_1_index < len(tuple_555_1_vec):
                    tuple_555_1 = tuple_555_1_vec[tuple_555_1_index]
                    tuple_555_1_index += 1
                    var_560 = tuple_555_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_561_(var_559, var_556)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_526_(var_556, var_560)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_566_(var_559, var_560)
                            if not ret:
                                # Program TransitionState Region
                                tuple_559_560 = (var_559, var_560)
                                prev_state = self.table_17[tuple_559_560]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_559_560] = 1 | 4
                                    if not present_bit:
                                        self.index_557[tuple_559_560[1]].append(tuple_559_560[0])
                                        self.index_882[tuple_559_560[0]].append(tuple_559_560[1])
                                    # Program VectorAppend Region
                                    vec_519.append((var_559, var_560))
        # Program VectorClear Region
        del vec_554[:]
        vec_index554 = 0
        # Program VectorUnique Region
        vec_570 = list(set(vec_570))
        vec_index570 = 0
        # Program TableJoin Region
        while vec_index570 < len(vec_570):
            var_572 = vec_570[vec_index570]
            vec_index570 += 1
            tuple_571_0_index: int = 0
            tuple_571_0_vec: List[int] = self.index_450[var_572]
            while tuple_571_0_index < len(tuple_571_0_vec):
                tuple_571_0 = tuple_571_0_vec[tuple_571_0_index]
                tuple_571_0_index += 1
                var_573 = tuple_571_0
                if var_572 in self.index_451:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_443_(var_573, var_572)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_454_(var_572)
                        if ret:
                            # Program TransitionState Region
                            tuple_573 = var_573
                            prev_state = self.table_26[tuple_573]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_26[tuple_573] = 1 | 4
                                if not present_bit:
                                    pass
        # Program VectorClear Region
        del vec_570[:]
        vec_index570 = 0
        # Induction Fixpoint Loop Region
        while len(vec_537) or len(vec_519):
            # Program Series Region
            # Program Call Region
            param_521_0 = [vec_519]
            ret = self.proc_515_(param_521_0)
            vec_519 = param_521_0[0]

            # Program Call Region
            param_539_0 = [vec_537]
            ret = self.proc_411_(param_539_0)
            vec_537 = param_539_0[0]

        vec_index537 = 0
        vec_index519 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_519[:]
        vec_index519 = 0
        # Program VectorClear Region
        del vec_537[:]
        vec_index537 = 0
        # Program Return Region
        return False
        return False

    def proc_237_(self, var_238: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_73[var_238] & 3
        if state == 1:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_240_(self, var_241: int, var_242: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_75[(var_241, var_242)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_241_242 = (var_241, var_242)
            prev_state = self.table_75[tuple_241_242]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_75[tuple_241_242] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1182_(self.var_2, var_241, var_242)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_241_242 = (var_241, var_242)
                    prev_state = self.table_75[tuple_241_242]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_75[tuple_241_242] = 1 | 4
                        if not present_bit:
                            self.index_235[tuple_241_242[0]].append(tuple_241_242[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_251_(self, param_0: List[List[Tuple[int, int, ControlFlowEdgeKind]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_252 = param_0[0]
        vec_index252: int = 0
        vec_338: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index338: int = 0
        vec_342: List[int] = list()
        vec_index342: int = 0
        vec_349: List[int] = list()
        vec_index349: int = 0
        vec_353: List[int] = list()
        vec_index353: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_252, vec_338 = vec_338, vec_252
        # Program VectorLoop Region
        while vec_index338 < len(vec_338):
            var_339, var_340, var_341 = vec_338[vec_index338]
            vec_index338 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_7 == var_341:
                # Program TransitionState Region
                tuple_339_340 = (var_339, var_340)
                prev_state = self.table_135[tuple_339_340]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_135[tuple_339_340] = 1 | 4
                    if not present_bit:
                        self.index_346[tuple_339_340[0]].append(tuple_339_340[1])
                    # Program VectorAppend Region
                    vec_342.append(var_339)
            # Program TupleCompare Region
            if self.var_0 == var_341:
                # Program TransitionState Region
                tuple_339_340 = (var_339, var_340)
                prev_state = self.table_132[tuple_339_340]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_132[tuple_339_340] = 1 | 4
                    if not present_bit:
                        self.index_345[tuple_339_340[0]].append(tuple_339_340[1])
                    # Program VectorAppend Region
                    vec_342.append(var_339)
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
                var_347 = tuple_343_0
                tuple_343_1_index: int = 0
                tuple_343_1_vec: List[int] = self.index_346[var_344]
                while tuple_343_1_index < len(tuple_343_1_vec):
                    tuple_343_1 = tuple_343_1_vec[tuple_343_1_index]
                    tuple_343_1_index += 1
                    var_348 = tuple_343_1
                    # Program TupleCompare Region
                    if var_347 != var_348:
                        # Program Parallel Region
                        # Program TransitionState Region
                        tuple_348_344 = (var_348, var_344)
                        prev_state = self.table_138[tuple_348_344]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_138[tuple_348_344] = 1 | 4
                            if not present_bit:
                                self.index_311[tuple_348_344[0]].append(tuple_348_344[1])
                            # Program VectorAppend Region
                            vec_353.append(var_348)
                        # Program TransitionState Region
                        tuple_347_344 = (var_347, var_344)
                        prev_state = self.table_129[tuple_347_344]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_129[tuple_347_344] = 1 | 4
                            if not present_bit:
                                self.index_316[tuple_347_344[0]].append(tuple_347_344[1])
                            # Program VectorAppend Region
                            vec_349.append(var_347)
        # Program VectorClear Region
        del vec_342[:]
        vec_index342 = 0
        # Program VectorUnique Region
        vec_349 = list(set(vec_349))
        vec_index349 = 0
        # Program TableJoin Region
        while vec_index349 < len(vec_349):
            var_351 = vec_349[vec_index349]
            vec_index349 += 1
            if var_351 in self.index_248:
                tuple_350_1_index: int = 0
                tuple_350_1_vec: List[int] = self.index_316[var_351]
                while tuple_350_1_index < len(tuple_350_1_vec):
                    tuple_350_1 = tuple_350_1_vec[tuple_350_1_index]
                    tuple_350_1_index += 1
                    var_352 = tuple_350_1
                    # Program TransitionState Region
                    tuple_352_351_0 = (var_352, var_351, self.var_0)
                    prev_state = self.table_11[tuple_352_351_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_352_351_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_352_351_0[1], tuple_352_351_0[2])].append(tuple_352_351_0[0])
                        # Program VectorAppend Region
                        vec_252.append((var_352, var_351, self.var_0))
        # Program VectorClear Region
        del vec_349[:]
        vec_index349 = 0
        # Program VectorUnique Region
        vec_353 = list(set(vec_353))
        vec_index353 = 0
        # Program TableJoin Region
        while vec_index353 < len(vec_353):
            var_355 = vec_353[vec_index353]
            vec_index353 += 1
            if var_355 in self.index_248:
                tuple_354_1_index: int = 0
                tuple_354_1_vec: List[int] = self.index_311[var_355]
                while tuple_354_1_index < len(tuple_354_1_vec):
                    tuple_354_1 = tuple_354_1_vec[tuple_354_1_index]
                    tuple_354_1_index += 1
                    var_356 = tuple_354_1
                    # Program TransitionState Region
                    tuple_356_355_7 = (var_356, var_355, self.var_7)
                    prev_state = self.table_11[tuple_356_355_7]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_356_355_7] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_356_355_7[1], tuple_356_355_7[2])].append(tuple_356_355_7[0])
                        # Program VectorAppend Region
                        vec_252.append((var_356, var_355, self.var_7))
        # Program VectorClear Region
        del vec_353[:]
        vec_index353 = 0
        # Program VectorClear Region
        del vec_338[:]
        vec_index338 = 0
        # Program Return Region
        param_0[0] = vec_252
        return False
        return False

    def proc_253_(self, vec_254: List[Tuple[int, int, ControlFlowEdgeKind]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index254: int = 0
        vec_488: List[int] = list()
        vec_index488: int = 0
        vec_489: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index489: int = 0
        vec_499: List[int] = list()
        vec_index499: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        while vec_index254 < len(vec_254):
            var_478, var_479, var_480 = vec_254[vec_index254]
            vec_index254 += 1
            # Program Parallel Region
            # Program TupleCompare Region
            if self.var_2 == var_480:
                # Program Parallel Region
                # Program Series Region
                # Program TransitionState Region
                # Eager insert before negation to prevent race
                tuple_479_478 = (var_479, var_478)
                prev_state = self.table_41[tuple_479_478]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0:
                    self.table_41[tuple_479_478] = 2 | 4
                    if not present_bit:
                        self.index_374[tuple_479_478[0]].append(tuple_479_478[1])
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_292_(var_479)
                if not ret:
                    # Program TransitionState Region
                    tuple_479_478 = (var_479, var_478)
                    prev_state = self.table_41[tuple_479_478]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_41[tuple_479_478] = 1 | 4
                        if not present_bit:
                            self.index_374[tuple_479_478[0]].append(tuple_479_478[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_483_(var_478, var_479, self.var_2)
                        if not ret:
                            # Program TransitionState Region
                            tuple_478_479_2 = (var_478, var_479, self.var_2)
                            prev_state = self.table_20[tuple_478_479_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_20[tuple_478_479_2] = 1 | 4
                                if not present_bit:
                                    self.index_969[(tuple_478_479_2[1], tuple_478_479_2[2])].append(tuple_478_479_2[0])
                                    self.index_1062[(tuple_478_479_2[0], tuple_478_479_2[1])].append(tuple_478_479_2[2])
                                    self.index_1488[tuple_478_479_2[1]].append((tuple_478_479_2[0], tuple_478_479_2[2]))
                                # Program VectorAppend Region
                                vec_489.append((var_478, var_479, self.var_2))
                # Program TransitionState Region
                tuple_478_479 = (var_478, var_479)
                prev_state = self.table_148[tuple_478_479]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_148[tuple_478_479] = 1 | 4
                    if not present_bit:
                        self.index_421[tuple_478_479[1]].append(tuple_478_479[0])
                    # Program VectorAppend Region
                    vec_499.append(var_479)
            # Program TupleCompare Region
            if var_480 != self.var_2:
                # Program TupleCompare Region
                if var_480 != self.var_9:
                    # Program TransitionState Region
                    var_480 = self._resolve_edgetype(var_480)
                    tuple_478_479_480 = (var_478, var_479, var_480)
                    prev_state = self.table_20[tuple_478_479_480]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_478_479_480] = 1 | 4
                        if not present_bit:
                            self.index_969[(tuple_478_479_480[1], tuple_478_479_480[2])].append(tuple_478_479_480[0])
                            self.index_1062[(tuple_478_479_480[0], tuple_478_479_480[1])].append(tuple_478_479_480[2])
                            self.index_1488[tuple_478_479_480[1]].append((tuple_478_479_480[0], tuple_478_479_480[2]))
                        # Program VectorAppend Region
                        var_480 = self._resolve_edgetype(var_480)
                        vec_489.append((var_478, var_479, var_480))
            # Program TupleCompare Region
            if self.var_9 == var_480:
                # Program Series Region
                # Program TransitionState Region
                # Eager insert before negation to prevent race
                tuple_479_478 = (var_479, var_478)
                prev_state = self.table_38[tuple_479_478]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0:
                    self.table_38[tuple_479_478] = 2 | 4
                    if not present_bit:
                        self.index_459[tuple_479_478[0]].append(tuple_479_478[1])
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_472_(var_479)
                if not ret:
                    # Program TransitionState Region
                    tuple_479_478 = (var_479, var_478)
                    prev_state = self.table_38[tuple_479_478]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_38[tuple_479_478] = 1 | 4
                        if not present_bit:
                            self.index_459[tuple_479_478[0]].append(tuple_479_478[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_494_(var_478, var_479, self.var_9)
                        if not ret:
                            # Program TransitionState Region
                            tuple_478_479_9 = (var_478, var_479, self.var_9)
                            prev_state = self.table_20[tuple_478_479_9]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_20[tuple_478_479_9] = 1 | 4
                                if not present_bit:
                                    self.index_969[(tuple_478_479_9[1], tuple_478_479_9[2])].append(tuple_478_479_9[0])
                                    self.index_1062[(tuple_478_479_9[0], tuple_478_479_9[1])].append(tuple_478_479_9[2])
                                    self.index_1488[tuple_478_479_9[1]].append((tuple_478_479_9[0], tuple_478_479_9[2]))
                                # Program VectorAppend Region
                                vec_489.append((var_478, var_479, self.var_9))
        # Program VectorUnique Region
        vec_499 = list(set(vec_499))
        vec_index499 = 0
        # Program TableJoin Region
        while vec_index499 < len(vec_499):
            var_501 = vec_499[vec_index499]
            vec_index499 += 1
            tuple_500_0_index: int = 0
            tuple_500_0_vec: List[int] = self.index_421[var_501]
            while tuple_500_0_index < len(tuple_500_0_vec):
                tuple_500_0 = tuple_500_0_vec[tuple_500_0_index]
                tuple_500_0_index += 1
                var_502 = tuple_500_0
                if var_501 in self.index_289:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_423_(var_502, var_501)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_292_(var_501)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_428_(var_502, var_501, self.var_10)
                            if not ret:
                                # Program TransitionState Region
                                tuple_502_501_10 = (var_502, var_501, self.var_10)
                                prev_state = self.table_20[tuple_502_501_10]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_20[tuple_502_501_10] = 1 | 4
                                    if not present_bit:
                                        self.index_969[(tuple_502_501_10[1], tuple_502_501_10[2])].append(tuple_502_501_10[0])
                                        self.index_1062[(tuple_502_501_10[0], tuple_502_501_10[1])].append(tuple_502_501_10[2])
                                        self.index_1488[tuple_502_501_10[1]].append((tuple_502_501_10[0], tuple_502_501_10[2]))
                                    # Program VectorAppend Region
                                    vec_489.append((var_502, var_501, self.var_10))
        # Program VectorClear Region
        del vec_499[:]
        vec_index499 = 0
        # Induction Fixpoint Loop Region
        while len(vec_488) or len(vec_489):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_488, vec_489)

            # Program Call Region
            param_491_0 = [vec_488]
            param_491_1 = [vec_489]
            ret = self.proc_173_(param_491_0, param_491_1)
            vec_488 = param_491_0[0]
            vec_489 = param_491_1[0]

        vec_index488 = 0
        vec_index489 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_488[:]
        vec_index488 = 0
        # Program VectorClear Region
        del vec_489[:]
        vec_index489 = 0
        # Program Return Region
        return False
        return False

    def proc_292_(self, var_293: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_293] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_293 = var_293
            prev_state = self.table_15[tuple_293]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_293] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1188_(var_293)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_293 = var_293
                    prev_state = self.table_15[tuple_293]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_293] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_295_(self, var_296: int, var_297: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_78[(var_296, var_297)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_296_297 = (var_296, var_297)
            prev_state = self.table_78[tuple_296_297]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_78[tuple_296_297] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1170_(var_296, var_297)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_296_297 = (var_296, var_297)
                    prev_state = self.table_78[tuple_296_297]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_78[tuple_296_297] = 1 | 4
                        if not present_bit:
                            self.index_290[tuple_296_297[1]].append(tuple_296_297[0])
                            self.index_957[tuple_296_297[0]].append(tuple_296_297[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_299_(self, var_300: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_300] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_300 = var_300
            prev_state = self.table_15[tuple_300]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_300] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_953_(var_300)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_300 = var_300
                    prev_state = self.table_15[tuple_300]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_300] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_366_(self, var_367: int, var_368: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_368_367 = (var_368, var_367)
        prev_state = self.table_81[tuple_368_367]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_81[tuple_368_367] = 2 | 4
            # Program Call Region
            ret = self.proc_1466_(var_368, var_367)

        # Program Return Region
        return False
        return False

    def proc_370_(self, var_371: int, var_372: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_372_371 = (var_372, var_371)
        prev_state = self.table_28[tuple_372_371]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_28[tuple_372_371] = 2 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1050_(var_371, var_372)

        # Program Return Region
        return False
        return False

    def proc_377_(self, var_378: int, var_379: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_379_378_2 = (var_379, var_378, self.var_2)
        prev_state = self.table_20[tuple_379_378_2]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_20[tuple_379_378_2] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1202_(var_379, var_378, self.var_2)

            # Program Call Region
            ret = self.proc_1207_(var_379, var_378, self.var_2)

            # Program Call Region
            ret = self.proc_1212_(var_379, var_378, self.var_2)

            # Program Call Region
            ret = self.proc_1217_(var_379, var_378, self.var_2)

            # Program Call Region
            ret = self.proc_1222_(var_379, var_378, self.var_2)

        # Program Return Region
        return False
        return False

    def proc_382_(self, var_383: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_383] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_383 = var_383
            prev_state = self.table_15[tuple_383]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_383] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_965_(self.var_0, var_383)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_383 = var_383
                    prev_state = self.table_15[tuple_383]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_383] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_403_(self, var_404: int, var_405: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_145[(var_404, var_405)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_404_405 = (var_404, var_405)
            prev_state = self.table_145[tuple_404_405]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_145[tuple_404_405] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1154_(self.var_8, var_404, var_405)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_404_405 = (var_404, var_405)
                    prev_state = self.table_145[tuple_404_405]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_145[tuple_404_405] = 1 | 4
                        if not present_bit:
                            self.index_401[tuple_404_405[1]].append(tuple_404_405[0])
                            self.index_1103[tuple_404_405[0]].append(tuple_404_405[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_408_(self, var_409: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_24[var_409] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_409 = var_409
            prev_state = self.table_24[tuple_409]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_24[tuple_409] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1121_(var_409)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_409 = var_409
                    prev_state = self.table_24[tuple_409]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_24[tuple_409] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_411_(self, param_0: List[List[int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_412 = param_0[0]
        vec_index412: int = 0
        vec_457: List[int] = list()
        vec_index457: int = 0
        vec_460: List[int] = list()
        vec_index460: int = 0
        vec_466: List[int] = list()
        vec_index466: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_412, vec_457 = vec_457, vec_412
        # Program VectorLoop Region
        while vec_index457 < len(vec_457):
            var_458 = vec_457[vec_index457]
            vec_index457 += 1
            # Program Series Region
            # Program TableScan Region
            scan_tuple_460: int
            scan_index_460: int = 0
            scan_tuple_460_vec: List[int] = self.index_459[var_458]
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
                tuple_458_461 = (var_458, var_461)
                prev_state = self.table_38[tuple_458_461]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 1:
                    self.table_38[tuple_458_461] = 0 | 4
                    # Program Call Region
                    ret = self.proc_462_(var_458, var_461)

            # Program VectorAppend Region
            vec_466.append(var_458)
        # Program VectorUnique Region
        vec_466 = list(set(vec_466))
        vec_index466 = 0
        # Program TableJoin Region
        while vec_index466 < len(vec_466):
            var_468 = vec_466[vec_index466]
            vec_index466 += 1
            tuple_467_0_index: int = 0
            tuple_467_0_vec: List[int] = self.index_401[var_468]
            while tuple_467_0_index < len(tuple_467_0_vec):
                tuple_467_0 = tuple_467_0_vec[tuple_467_0_index]
                tuple_467_0_index += 1
                var_470 = tuple_467_0
                if var_468 in self.index_469:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_403_(var_470, var_468)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_472_(var_468)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_475_(var_470)
                            if not ret:
                                # Program TransitionState Region
                                tuple_470 = var_470
                                prev_state = self.table_24[tuple_470]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_24[tuple_470] = 1 | 4
                                    if not present_bit:
                                        pass
                                    # Program VectorAppend Region
                                    vec_412.append(var_470)
        # Program VectorClear Region
        del vec_466[:]
        vec_index466 = 0
        # Program VectorClear Region
        del vec_457[:]
        vec_index457 = 0
        # Program Return Region
        param_0[0] = vec_412
        return False
        return False

    def proc_423_(self, var_424: int, var_425: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_148[(var_424, var_425)] & 3
        if state == 1:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_428_(self, var_429: int, var_430: int, var_431: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_20[(var_429, var_430, self.var_10)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_429_430_10 = (var_429, var_430, self.var_10)
            prev_state = self.table_20[tuple_429_430_10]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_20[tuple_429_430_10] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1016_(var_430, var_429)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_429_430_10 = (var_429, var_430, self.var_10)
                    prev_state = self.table_20[tuple_429_430_10]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_429_430_10] = 1 | 4
                        if not present_bit:
                            self.index_969[(tuple_429_430_10[1], tuple_429_430_10[2])].append(tuple_429_430_10[0])
                            self.index_1062[(tuple_429_430_10[0], tuple_429_430_10[1])].append(tuple_429_430_10[2])
                            self.index_1488[tuple_429_430_10[1]].append((tuple_429_430_10[0], tuple_429_430_10[2]))
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_438_(self, var_439: int, var_440: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_151[(var_439, var_440)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_439_440 = (var_439, var_440)
            prev_state = self.table_151[tuple_439_440]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_151[tuple_439_440] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1142_(var_439, var_440)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_439_440 = (var_439, var_440)
                    prev_state = self.table_151[tuple_439_440]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_151[tuple_439_440] = 1 | 4
                        if not present_bit:
                            self.index_436[tuple_439_440[1]].append(tuple_439_440[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_443_(self, var_444: int, var_445: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_154[(var_444, var_445)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_444_445 = (var_444, var_445)
            prev_state = self.table_154[tuple_444_445]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_154[tuple_444_445] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1132_(var_445, var_444)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_444_445 = (var_444, var_445)
                    prev_state = self.table_154[tuple_444_445]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_154[tuple_444_445] = 1 | 4
                        if not present_bit:
                            self.index_450[tuple_444_445[1]].append(tuple_444_445[0])
                            self.index_1073[tuple_444_445[0]].append(tuple_444_445[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_454_(self, var_455: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_65[var_455] & 3
        if state == 1:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_462_(self, var_463: int, var_464: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_464_463_9 = (var_464, var_463, self.var_9)
        prev_state = self.table_20[tuple_464_463_9]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_20[tuple_464_463_9] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1202_(var_464, var_463, self.var_9)

            # Program Call Region
            ret = self.proc_1207_(var_464, var_463, self.var_9)

            # Program Call Region
            ret = self.proc_1212_(var_464, var_463, self.var_9)

            # Program Call Region
            ret = self.proc_1217_(var_464, var_463, self.var_9)

            # Program Call Region
            ret = self.proc_1222_(var_464, var_463, self.var_9)

        # Program Return Region
        return False
        return False

    def proc_472_(self, var_473: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_24[var_473] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_473 = var_473
            prev_state = self.table_24[tuple_473]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_24[tuple_473] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1111_(var_473)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_473 = var_473
                    prev_state = self.table_24[tuple_473]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_24[tuple_473] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_475_(self, var_476: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_24[var_476] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_476 = var_476
            prev_state = self.table_24[tuple_476]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_24[tuple_476] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1099_(var_476)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_476 = var_476
                    prev_state = self.table_24[tuple_476]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_24[tuple_476] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_483_(self, var_484: int, var_485: int, var_486: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_20[(var_484, var_485, self.var_2)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_484_485_2 = (var_484, var_485, self.var_2)
            prev_state = self.table_20[tuple_484_485_2]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_20[tuple_484_485_2] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_998_(var_485, var_484)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_484_485_2 = (var_484, var_485, self.var_2)
                    prev_state = self.table_20[tuple_484_485_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_484_485_2] = 1 | 4
                        if not present_bit:
                            self.index_969[(tuple_484_485_2[1], tuple_484_485_2[2])].append(tuple_484_485_2[0])
                            self.index_1062[(tuple_484_485_2[0], tuple_484_485_2[1])].append(tuple_484_485_2[2])
                            self.index_1488[tuple_484_485_2[1]].append((tuple_484_485_2[0], tuple_484_485_2[2]))
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_494_(self, var_495: int, var_496: int, var_497: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_20[(var_495, var_496, self.var_9)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_495_496_9 = (var_495, var_496, self.var_9)
            prev_state = self.table_20[tuple_495_496_9]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_20[tuple_495_496_9] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1025_(var_496, var_495)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_495_496_9 = (var_495, var_496, self.var_9)
                    prev_state = self.table_20[tuple_495_496_9]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_495_496_9] = 1 | 4
                        if not present_bit:
                            self.index_969[(tuple_495_496_9[1], tuple_495_496_9[2])].append(tuple_495_496_9[0])
                            self.index_1062[(tuple_495_496_9[0], tuple_495_496_9[1])].append(tuple_495_496_9[2])
                            self.index_1488[tuple_495_496_9[1]].append((tuple_495_496_9[0], tuple_495_496_9[2]))
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_511_(self, var_512: int, var_513: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_17[(var_512, var_513)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_512_513 = (var_512, var_513)
            prev_state = self.table_17[tuple_512_513]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_17[tuple_512_513] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_926_(var_513)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_512_513 = (var_512, var_513)
                    prev_state = self.table_17[tuple_512_513]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_512_513] = 1 | 4
                        if not present_bit:
                            self.index_557[tuple_512_513[1]].append(tuple_512_513[0])
                            self.index_882[tuple_512_513[0]].append(tuple_512_513[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_515_(self, param_0: List[List[Tuple[int, int]]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_516 = param_0[0]
        vec_index516: int = 0
        vec_576: List[Tuple[int, int]] = list()
        vec_index576: int = 0
        vec_579: List[int] = list()
        vec_index579: int = 0
        # Program Series Region
        # Program VectorSwap Region
        vec_516, vec_576 = vec_576, vec_516
        # Program VectorLoop Region
        while vec_index576 < len(vec_576):
            var_577, var_578 = vec_576[vec_index576]
            vec_index576 += 1
            # Program VectorAppend Region
            vec_579.append(var_578)
        # Program VectorUnique Region
        vec_579 = list(set(vec_579))
        vec_index579 = 0
        # Program TableJoin Region
        while vec_index579 < len(vec_579):
            var_581 = vec_579[vec_index579]
            vec_index579 += 1
            tuple_580_0_index: int = 0
            tuple_580_0_vec: List[int] = self.index_557[var_581]
            while tuple_580_0_index < len(tuple_580_0_vec):
                tuple_580_0 = tuple_580_0_vec[tuple_580_0_index]
                tuple_580_0_index += 1
                var_582 = tuple_580_0
                tuple_580_1_index: int = 0
                tuple_580_1_vec: List[int] = self.index_558[var_581]
                while tuple_580_1_index < len(tuple_580_1_vec):
                    tuple_580_1 = tuple_580_1_vec[tuple_580_1_index]
                    tuple_580_1_index += 1
                    var_583 = tuple_580_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_561_(var_582, var_581)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_526_(var_581, var_583)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_566_(var_582, var_583)
                            if not ret:
                                # Program TransitionState Region
                                tuple_582_583 = (var_582, var_583)
                                prev_state = self.table_17[tuple_582_583]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_582_583] = 1 | 4
                                    if not present_bit:
                                        self.index_557[tuple_582_583[1]].append(tuple_582_583[0])
                                        self.index_882[tuple_582_583[0]].append(tuple_582_583[1])
                                    # Program VectorAppend Region
                                    vec_516.append((var_582, var_583))
        # Program VectorClear Region
        del vec_579[:]
        vec_index579 = 0
        # Program VectorClear Region
        del vec_576[:]
        vec_index576 = 0
        # Program Return Region
        param_0[0] = vec_516
        return False
        return False

    def proc_526_(self, var_527: int, var_528: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_81[(var_527, var_528)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_527_528 = (var_527, var_528)
            prev_state = self.table_81[tuple_527_528]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_81[tuple_527_528] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1050_(var_528, var_527)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_527_528 = (var_527, var_528)
                    prev_state = self.table_81[tuple_527_528]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_81[tuple_527_528] = 1 | 4
                        if not present_bit:
                            self.index_558[tuple_527_528[0]].append(tuple_527_528[1])
                            self.index_917[tuple_527_528[1]].append(tuple_527_528[0])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_561_(self, var_562: int, var_563: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_17[(var_562, var_563)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_562_563 = (var_562, var_563)
            prev_state = self.table_17[tuple_562_563]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_17[tuple_562_563] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_1081_(var_562, var_563)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_562_563 = (var_562, var_563)
                    prev_state = self.table_17[tuple_562_563]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_562_563] = 1 | 4
                        if not present_bit:
                            self.index_557[tuple_562_563[1]].append(tuple_562_563[0])
                            self.index_882[tuple_562_563[0]].append(tuple_562_563[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_566_(self, var_567: int, var_568: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_17[(var_567, var_568)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_567_568 = (var_567, var_568)
            prev_state = self.table_17[tuple_567_568]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_17[tuple_567_568] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
                ret = self.proc_912_(var_567, var_568)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_567_568 = (var_567, var_568)
                    prev_state = self.table_17[tuple_567_568]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_567_568] = 1 | 4
                        if not present_bit:
                            self.index_557[tuple_567_568[1]].append(tuple_567_568[0])
                            self.index_882[tuple_567_568[0]].append(tuple_567_568[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def external_symbol_2(self, vec_590: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index590: int = 0
        vec_593: List[int] = list()
        vec_index593: int = 0
        vec_597: List[int] = list()
        vec_index597: int = 0
        vec_598: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index598: int = 0
        vec_601: List[int] = list()
        vec_index601: int = 0
        vec_606: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index606: int = 0
        vec_609: List[int] = list()
        vec_index609: int = 0
        vec_612: List[int] = list()
        vec_index612: int = 0
        vec_616: List[int] = list()
        vec_index616: int = 0
        vec_620: List[int] = list()
        vec_index620: int = 0
        vec_624: List[int] = list()
        vec_index624: int = 0
        vec_628: List[int] = list()
        vec_index628: int = 0
        vec_632: List[int] = list()
        vec_index632: int = 0
        vec_636: List[int] = list()
        vec_index636: int = 0
        vec_640: List[int] = list()
        vec_index640: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index590 = 0
        while vec_index590 < len(vec_590):
            var_591, var_592 = vec_590[vec_index590]
            vec_index590 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_591 = var_591
            prev_state = self.table_65[tuple_591]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_591] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_591 = var_591
                prev_state = self.table_71[tuple_591]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_591] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_609.append(var_591)
                    # Program VectorAppend Region
                    vec_636.append(var_591)
                    # Program VectorAppend Region
                    vec_632.append(var_591)
                    # Program VectorAppend Region
                    vec_628.append(var_591)
                    # Program VectorAppend Region
                    vec_624.append(var_591)
                    # Program VectorAppend Region
                    vec_612.append(var_591)
                    # Program VectorAppend Region
                    vec_620.append(var_591)
                    # Program VectorAppend Region
                    vec_616.append(var_591)
                    # Program VectorAppend Region
                    vec_601.append(var_591)
                # Program VectorAppend Region
                vec_593.append(var_591)
                # Program VectorAppend Region
                vec_640.append(var_591)
            # Program TransitionState Region
            tuple_591 = var_591
            prev_state = self.table_65[tuple_591]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_591] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_591 = var_591
                prev_state = self.table_71[tuple_591]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_591] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_609.append(var_591)
                    # Program VectorAppend Region
                    vec_636.append(var_591)
                    # Program VectorAppend Region
                    vec_632.append(var_591)
                    # Program VectorAppend Region
                    vec_628.append(var_591)
                    # Program VectorAppend Region
                    vec_624.append(var_591)
                    # Program VectorAppend Region
                    vec_612.append(var_591)
                    # Program VectorAppend Region
                    vec_620.append(var_591)
                    # Program VectorAppend Region
                    vec_616.append(var_591)
                    # Program VectorAppend Region
                    vec_601.append(var_591)
                # Program VectorAppend Region
                vec_593.append(var_591)
                # Program VectorAppend Region
                vec_640.append(var_591)
            # Program TransitionState Region
            tuple_591 = var_591
            prev_state = self.table_65[tuple_591]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_65[tuple_591] = 1 | 4
                if not present_bit:
                    pass
                # Program Parallel Region
                # Program TransitionState Region
                tuple_591 = var_591
                prev_state = self.table_71[tuple_591]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_71[tuple_591] = 1 | 4
                    if not present_bit:
                        pass
                    # Program Parallel Region
                    # Program VectorAppend Region
                    vec_609.append(var_591)
                    # Program VectorAppend Region
                    vec_636.append(var_591)
                    # Program VectorAppend Region
                    vec_632.append(var_591)
                    # Program VectorAppend Region
                    vec_628.append(var_591)
                    # Program VectorAppend Region
                    vec_624.append(var_591)
                    # Program VectorAppend Region
                    vec_612.append(var_591)
                    # Program VectorAppend Region
                    vec_620.append(var_591)
                    # Program VectorAppend Region
                    vec_616.append(var_591)
                    # Program VectorAppend Region
                    vec_601.append(var_591)
                # Program VectorAppend Region
                vec_593.append(var_591)
                # Program VectorAppend Region
                vec_640.append(var_591)
        # Program VectorUnique Region
        vec_593 = list(set(vec_593))
        vec_index593 = 0
        # Program TableJoin Region
        while vec_index593 < len(vec_593):
            var_595 = vec_593[vec_index593]
            vec_index593 += 1
            if var_595 in self.index_451:
                if var_595 in self.index_596:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_595 = var_595
                    prev_state = self.table_15[tuple_595]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_595] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_597.append(var_595)
        # Program VectorClear Region
        del vec_593[:]
        vec_index593 = 0
        # Program VectorUnique Region
        vec_601 = list(set(vec_601))
        vec_index601 = 0
        # Program TableJoin Region
        while vec_index601 < len(vec_601):
            var_603 = vec_601[vec_index601]
            vec_index601 += 1
            tuple_602_0_index: int = 0
            tuple_602_0_vec: List[Tuple[ControlFlowEdgeKind, int]] = self.index_247[var_603]
            while tuple_602_0_index < len(tuple_602_0_vec):
                tuple_602_0 = tuple_602_0_vec[tuple_602_0_index]
                tuple_602_0_index += 1
                var_604 = tuple_602_0[0]
                var_605 = tuple_602_0[1]
                if var_603 in self.index_248:
                    # Program TransitionState Region
                    var_604 = self._resolve_edgetype(var_604)
                    tuple_605_603_604 = (var_605, var_603, var_604)
                    prev_state = self.table_11[tuple_605_603_604]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_605_603_604] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_605_603_604[1], tuple_605_603_604[2])].append(tuple_605_603_604[0])
                        # Program VectorAppend Region
                        var_604 = self._resolve_edgetype(var_604)
                        vec_606.append((var_605, var_603, var_604))
        # Program VectorClear Region
        del vec_601[:]
        vec_index601 = 0
        # Program VectorUnique Region
        vec_609 = list(set(vec_609))
        vec_index609 = 0
        # Program TableJoin Region
        while vec_index609 < len(vec_609):
            var_611 = vec_609[vec_index609]
            vec_index609 += 1
            if var_611 in self.index_261:
                if var_611 in self.index_248:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_611 = var_611
                    prev_state = self.table_15[tuple_611]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_611] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_597.append(var_611)
        # Program VectorClear Region
        del vec_609[:]
        vec_index609 = 0
        # Program VectorUnique Region
        vec_612 = list(set(vec_612))
        vec_index612 = 0
        # Program TableJoin Region
        while vec_index612 < len(vec_612):
            var_614 = vec_612[vec_index612]
            vec_index612 += 1
            if var_614 in self.index_248:
                tuple_613_1_index: int = 0
                tuple_613_1_vec: List[int] = self.index_284[var_614]
                while tuple_613_1_index < len(tuple_613_1_vec):
                    tuple_613_1 = tuple_613_1_vec[tuple_613_1_index]
                    tuple_613_1_index += 1
                    var_615 = tuple_613_1
                    # Program TransitionState Region
                    tuple_615_614_6 = (var_615, var_614, self.var_6)
                    prev_state = self.table_11[tuple_615_614_6]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_615_614_6] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_615_614_6[1], tuple_615_614_6[2])].append(tuple_615_614_6[0])
                        # Program VectorAppend Region
                        vec_606.append((var_615, var_614, self.var_6))
        # Program VectorClear Region
        del vec_612[:]
        vec_index612 = 0
        # Program VectorUnique Region
        vec_616 = list(set(vec_616))
        vec_index616 = 0
        # Program TableJoin Region
        while vec_index616 < len(vec_616):
            var_618 = vec_616[vec_index616]
            vec_index616 += 1
            if var_618 in self.index_248:
                tuple_617_1_index: int = 0
                tuple_617_1_vec: List[int] = self.index_311[var_618]
                while tuple_617_1_index < len(tuple_617_1_vec):
                    tuple_617_1 = tuple_617_1_vec[tuple_617_1_index]
                    tuple_617_1_index += 1
                    var_619 = tuple_617_1
                    # Program TransitionState Region
                    tuple_619_618_7 = (var_619, var_618, self.var_7)
                    prev_state = self.table_11[tuple_619_618_7]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_619_618_7] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_619_618_7[1], tuple_619_618_7[2])].append(tuple_619_618_7[0])
                        # Program VectorAppend Region
                        vec_606.append((var_619, var_618, self.var_7))
        # Program VectorClear Region
        del vec_616[:]
        vec_index616 = 0
        # Program VectorUnique Region
        vec_620 = list(set(vec_620))
        vec_index620 = 0
        # Program TableJoin Region
        while vec_index620 < len(vec_620):
            var_622 = vec_620[vec_index620]
            vec_index620 += 1
            if var_622 in self.index_248:
                tuple_621_1_index: int = 0
                tuple_621_1_vec: List[int] = self.index_316[var_622]
                while tuple_621_1_index < len(tuple_621_1_vec):
                    tuple_621_1 = tuple_621_1_vec[tuple_621_1_index]
                    tuple_621_1_index += 1
                    var_623 = tuple_621_1
                    # Program TransitionState Region
                    tuple_623_622_0 = (var_623, var_622, self.var_0)
                    prev_state = self.table_11[tuple_623_622_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_623_622_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_623_622_0[1], tuple_623_622_0[2])].append(tuple_623_622_0[0])
                        # Program VectorAppend Region
                        vec_606.append((var_623, var_622, self.var_0))
        # Program VectorClear Region
        del vec_620[:]
        vec_index620 = 0
        # Program VectorUnique Region
        vec_624 = list(set(vec_624))
        vec_index624 = 0
        # Program TableJoin Region
        while vec_index624 < len(vec_624):
            var_626 = vec_624[vec_index624]
            vec_index624 += 1
            if var_626 in self.index_248:
                tuple_625_1_index: int = 0
                tuple_625_1_vec: List[int] = self.index_321[var_626]
                while tuple_625_1_index < len(tuple_625_1_vec):
                    tuple_625_1 = tuple_625_1_vec[tuple_625_1_index]
                    tuple_625_1_index += 1
                    var_627 = tuple_625_1
                    # Program TransitionState Region
                    tuple_627_626_0 = (var_627, var_626, self.var_0)
                    prev_state = self.table_11[tuple_627_626_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_627_626_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_627_626_0[1], tuple_627_626_0[2])].append(tuple_627_626_0[0])
                        # Program VectorAppend Region
                        vec_606.append((var_627, var_626, self.var_0))
        # Program VectorClear Region
        del vec_624[:]
        vec_index624 = 0
        # Program VectorUnique Region
        vec_628 = list(set(vec_628))
        vec_index628 = 0
        # Program TableJoin Region
        while vec_index628 < len(vec_628):
            var_630 = vec_628[vec_index628]
            vec_index628 += 1
            if var_630 in self.index_248:
                tuple_629_1_index: int = 0
                tuple_629_1_vec: List[int] = self.index_326[var_630]
                while tuple_629_1_index < len(tuple_629_1_vec):
                    tuple_629_1 = tuple_629_1_vec[tuple_629_1_index]
                    tuple_629_1_index += 1
                    var_631 = tuple_629_1
                    # Program TransitionState Region
                    tuple_631_630_0 = (var_631, var_630, self.var_0)
                    prev_state = self.table_11[tuple_631_630_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_631_630_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_631_630_0[1], tuple_631_630_0[2])].append(tuple_631_630_0[0])
                        # Program VectorAppend Region
                        vec_606.append((var_631, var_630, self.var_0))
        # Program VectorClear Region
        del vec_628[:]
        vec_index628 = 0
        # Program VectorUnique Region
        vec_632 = list(set(vec_632))
        vec_index632 = 0
        # Program TableJoin Region
        while vec_index632 < len(vec_632):
            var_634 = vec_632[vec_index632]
            vec_index632 += 1
            if var_634 in self.index_248:
                tuple_633_1_index: int = 0
                tuple_633_1_vec: List[int] = self.index_331[var_634]
                while tuple_633_1_index < len(tuple_633_1_vec):
                    tuple_633_1 = tuple_633_1_vec[tuple_633_1_index]
                    tuple_633_1_index += 1
                    var_635 = tuple_633_1
                    # Program TransitionState Region
                    tuple_635_634_2 = (var_635, var_634, self.var_2)
                    prev_state = self.table_11[tuple_635_634_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_635_634_2] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_635_634_2[1], tuple_635_634_2[2])].append(tuple_635_634_2[0])
                        # Program VectorAppend Region
                        vec_606.append((var_635, var_634, self.var_2))
        # Program VectorClear Region
        del vec_632[:]
        vec_index632 = 0
        # Program VectorUnique Region
        vec_636 = list(set(vec_636))
        vec_index636 = 0
        # Program TableJoin Region
        while vec_index636 < len(vec_636):
            var_638 = vec_636[vec_index636]
            vec_index636 += 1
            if var_638 in self.index_248:
                tuple_637_1_index: int = 0
                tuple_637_1_vec: List[int] = self.index_336[var_638]
                while tuple_637_1_index < len(tuple_637_1_vec):
                    tuple_637_1 = tuple_637_1_vec[tuple_637_1_index]
                    tuple_637_1_index += 1
                    var_639 = tuple_637_1
                    # Program TransitionState Region
                    tuple_639_638_2 = (var_639, var_638, self.var_2)
                    prev_state = self.table_11[tuple_639_638_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_639_638_2] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_639_638_2[1], tuple_639_638_2[2])].append(tuple_639_638_2[0])
                        # Program VectorAppend Region
                        vec_606.append((var_639, var_638, self.var_2))
        # Program VectorClear Region
        del vec_636[:]
        vec_index636 = 0
        # Program VectorUnique Region
        vec_640 = list(set(vec_640))
        vec_index640 = 0
        # Program TableJoin Region
        while vec_index640 < len(vec_640):
            var_642 = vec_640[vec_index640]
            vec_index640 += 1
            tuple_641_0_index: int = 0
            tuple_641_0_vec: List[int] = self.index_450[var_642]
            while tuple_641_0_index < len(tuple_641_0_vec):
                tuple_641_0 = tuple_641_0_vec[tuple_641_0_index]
                tuple_641_0_index += 1
                var_643 = tuple_641_0
                if var_642 in self.index_451:
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_443_(var_643, var_642)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_454_(var_642)
                        if ret:
                            # Program TransitionState Region
                            tuple_643 = var_643
                            prev_state = self.table_26[tuple_643]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_26[tuple_643] = 1 | 4
                                if not present_bit:
                                    pass
        # Program VectorClear Region
        del vec_640[:]
        vec_index640 = 0
        # Induction Fixpoint Loop Region
        while len(vec_606) or len(vec_597) or len(vec_598):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_597, vec_598)

            # Program Call Region
            param_600_0 = [vec_597]
            param_600_1 = [vec_598]
            ret = self.proc_173_(param_600_0, param_600_1)
            vec_597 = param_600_0[0]
            vec_598 = param_600_1[0]

            # Program Call Region
            ret = self.proc_253_(vec_606)

            # Program Call Region
            param_608_0 = [vec_606]
            ret = self.proc_251_(param_608_0)
            vec_606 = param_608_0[0]

        vec_index606 = 0
        vec_index597 = 0
        vec_index598 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_597[:]
        vec_index597 = 0
        # Program VectorClear Region
        del vec_598[:]
        vec_index598 = 0
        # Program VectorClear Region
        del vec_606[:]
        vec_index606 = 0
        # Program Return Region
        return False
        return False

    def entrypoint_1(self, vec_647: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index647: int = 0
        vec_649: List[int] = list()
        vec_index649: int = 0
        vec_652: List[int] = list()
        vec_index652: int = 0
        vec_653: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index653: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index647 = 0
        while vec_index647 < len(vec_647):
            var_648 = vec_647[vec_index647]
            vec_index647 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
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
            if var_651 in self.index_261:
                if var_651 in self.index_248:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_651 = var_651
                    prev_state = self.table_15[tuple_651]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_651] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_652.append(var_651)
        # Program VectorClear Region
        del vec_649[:]
        vec_index649 = 0
        # Induction Fixpoint Loop Region
        while len(vec_652) or len(vec_653):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_652, vec_653)

            # Program Call Region
            param_655_0 = [vec_652]
            param_655_1 = [vec_653]
            ret = self.proc_173_(param_655_0, param_655_1)
            vec_652 = param_655_0[0]
            vec_653 = param_655_1[0]

        vec_index652 = 0
        vec_index653 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_652[:]
        vec_index652 = 0
        # Program VectorClear Region
        del vec_653[:]
        vec_index653 = 0
        # Program Return Region
        return False
        return False

    def constructor_function_1(self, vec_657: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index657: int = 0
        vec_659: List[int] = list()
        vec_index659: int = 0
        vec_662: List[int] = list()
        vec_index662: int = 0
        vec_663: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index663: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index657 = 0
        while vec_index657 < len(vec_657):
            var_658 = vec_657[vec_index657]
            vec_index657 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_658 = var_658
            prev_state = self.table_47[tuple_658]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_47[tuple_658] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_659.append(var_658)
        # Program VectorUnique Region
        vec_659 = list(set(vec_659))
        vec_index659 = 0
        # Program TableJoin Region
        while vec_index659 < len(vec_659):
            var_661 = vec_659[vec_index659]
            vec_index659 += 1
            if var_661 in self.index_210:
                if var_661 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_661 = var_661
                    prev_state = self.table_15[tuple_661]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_661] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_662.append(var_661)
        # Program VectorClear Region
        del vec_659[:]
        vec_index659 = 0
        # Induction Fixpoint Loop Region
        while len(vec_662) or len(vec_663):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_662, vec_663)

            # Program Call Region
            param_665_0 = [vec_662]
            param_665_1 = [vec_663]
            ret = self.proc_173_(param_665_0, param_665_1)
            vec_662 = param_665_0[0]
            vec_663 = param_665_1[0]

        vec_index662 = 0
        vec_index663 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_662[:]
        vec_index662 = 0
        # Program VectorClear Region
        del vec_663[:]
        vec_index663 = 0
        # Program Return Region
        return False
        return False

    def destructor_function_1(self, vec_667: List[int]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index667: int = 0
        vec_669: List[int] = list()
        vec_index669: int = 0
        vec_672: List[int] = list()
        vec_index672: int = 0
        vec_673: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index673: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index667 = 0
        while vec_index667 < len(vec_667):
            var_668 = vec_667[vec_index667]
            vec_index667 += 1
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_668 = var_668
            prev_state = self.table_51[tuple_668]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_51[tuple_668] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_669.append(var_668)
        # Program VectorUnique Region
        vec_669 = list(set(vec_669))
        vec_index669 = 0
        # Program TableJoin Region
        while vec_index669 < len(vec_669):
            var_671 = vec_669[vec_index669]
            vec_index669 += 1
            if var_671 in self.index_206:
                if var_671 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_671 = var_671
                    prev_state = self.table_15[tuple_671]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_671] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_672.append(var_671)
        # Program VectorClear Region
        del vec_669[:]
        vec_index669 = 0
        # Induction Fixpoint Loop Region
        while len(vec_672) or len(vec_673):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_672, vec_673)

            # Program Call Region
            param_675_0 = [vec_672]
            param_675_1 = [vec_673]
            ret = self.proc_173_(param_675_0, param_675_1)
            vec_672 = param_675_0[0]
            vec_673 = param_675_1[0]

        vec_index672 = 0
        vec_index673 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_672[:]
        vec_index672 = 0
        # Program VectorClear Region
        del vec_673[:]
        vec_index673 = 0
        # Program Return Region
        return False
        return False

    def imported_function_2(self, vec_677: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index677: int = 0
        vec_680: List[int] = list()
        vec_index680: int = 0
        vec_683: List[int] = list()
        vec_index683: int = 0
        vec_684: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index684: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index677 = 0
        while vec_index677 < len(vec_677):
            var_678, var_679 = vec_677[vec_index677]
            vec_index677 += 1
            # Program TransitionState Region
            tuple_678 = var_678
            prev_state = self.table_53[tuple_678]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_53[tuple_678] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_680.append(var_678)
        # Program VectorUnique Region
        vec_680 = list(set(vec_680))
        vec_index680 = 0
        # Program TableJoin Region
        while vec_index680 < len(vec_680):
            var_682 = vec_680[vec_index680]
            vec_index680 += 1
            if var_682 in self.index_202:
                if var_682 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_682 = var_682
                    prev_state = self.table_15[tuple_682]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_682] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_683.append(var_682)
        # Program VectorClear Region
        del vec_680[:]
        vec_index680 = 0
        # Induction Fixpoint Loop Region
        while len(vec_683) or len(vec_684):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_683, vec_684)

            # Program Call Region
            param_686_0 = [vec_683]
            param_686_1 = [vec_684]
            ret = self.proc_173_(param_686_0, param_686_1)
            vec_683 = param_686_0[0]
            vec_684 = param_686_1[0]

        vec_index683 = 0
        vec_index684 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_683[:]
        vec_index683 = 0
        # Program VectorClear Region
        del vec_684[:]
        vec_index684 = 0
        # Program Return Region
        return False
        return False

    def exported_function_2(self, vec_688: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index688: int = 0
        vec_691: List[int] = list()
        vec_index691: int = 0
        vec_694: List[int] = list()
        vec_index694: int = 0
        vec_695: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index695: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index688 = 0
        while vec_index688 < len(vec_688):
            var_689, var_690 = vec_688[vec_index688]
            vec_index688 += 1
            # Program TransitionState Region
            tuple_689 = var_689
            prev_state = self.table_55[tuple_689]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_55[tuple_689] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_691.append(var_689)
        # Program VectorUnique Region
        vec_691 = list(set(vec_691))
        vec_index691 = 0
        # Program TableJoin Region
        while vec_index691 < len(vec_691):
            var_693 = vec_691[vec_index691]
            vec_index691 += 1
            if var_693 in self.index_198:
                if var_693 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_693 = var_693
                    prev_state = self.table_15[tuple_693]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_693] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_694.append(var_693)
        # Program VectorClear Region
        del vec_691[:]
        vec_index691 = 0
        # Induction Fixpoint Loop Region
        while len(vec_694) or len(vec_695):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_694, vec_695)

            # Program Call Region
            param_697_0 = [vec_694]
            param_697_1 = [vec_695]
            ret = self.proc_173_(param_697_0, param_697_1)
            vec_694 = param_697_0[0]
            vec_695 = param_697_1[0]

        vec_index694 = 0
        vec_index695 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_694[:]
        vec_index694 = 0
        # Program VectorClear Region
        del vec_695[:]
        vec_index695 = 0
        # Program Return Region
        return False
        return False

    def local_function_2(self, vec_699: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index699: int = 0
        vec_702: List[int] = list()
        vec_index702: int = 0
        vec_705: List[int] = list()
        vec_index705: int = 0
        vec_706: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index706: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index699 = 0
        while vec_index699 < len(vec_699):
            var_700, var_701 = vec_699[vec_index699]
            vec_index699 += 1
            # Program TransitionState Region
            tuple_700 = var_700
            prev_state = self.table_57[tuple_700]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_57[tuple_700] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_702.append(var_700)
        # Program VectorUnique Region
        vec_702 = list(set(vec_702))
        vec_index702 = 0
        # Program TableJoin Region
        while vec_index702 < len(vec_702):
            var_704 = vec_702[vec_index702]
            vec_index702 += 1
            if var_704 in self.index_194:
                if var_704 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_704 = var_704
                    prev_state = self.table_15[tuple_704]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_704] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_705.append(var_704)
        # Program VectorClear Region
        del vec_702[:]
        vec_index702 = 0
        # Induction Fixpoint Loop Region
        while len(vec_705) or len(vec_706):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_705, vec_706)

            # Program Call Region
            param_708_0 = [vec_705]
            param_708_1 = [vec_706]
            ret = self.proc_173_(param_708_0, param_708_1)
            vec_705 = param_708_0[0]
            vec_706 = param_708_1[0]

        vec_index705 = 0
        vec_index706 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_705[:]
        vec_index705 = 0
        # Program VectorClear Region
        del vec_706[:]
        vec_index706 = 0
        # Program Return Region
        return False
        return False

    def imported_symbol_2(self, vec_710: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index710: int = 0
        vec_713: List[int] = list()
        vec_index713: int = 0
        vec_716: List[int] = list()
        vec_index716: int = 0
        vec_717: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index717: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index710 = 0
        while vec_index710 < len(vec_710):
            var_711, var_712 = vec_710[vec_index710]
            vec_index710 += 1
            # Program TransitionState Region
            tuple_711 = var_711
            prev_state = self.table_59[tuple_711]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_59[tuple_711] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_713.append(var_711)
        # Program VectorUnique Region
        vec_713 = list(set(vec_713))
        vec_index713 = 0
        # Program TableJoin Region
        while vec_index713 < len(vec_713):
            var_715 = vec_713[vec_index713]
            vec_index713 += 1
            if var_715 in self.index_190:
                if var_715 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_715 = var_715
                    prev_state = self.table_15[tuple_715]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_715] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_716.append(var_715)
        # Program VectorClear Region
        del vec_713[:]
        vec_index713 = 0
        # Induction Fixpoint Loop Region
        while len(vec_716) or len(vec_717):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_716, vec_717)

            # Program Call Region
            param_719_0 = [vec_716]
            param_719_1 = [vec_717]
            ret = self.proc_173_(param_719_0, param_719_1)
            vec_716 = param_719_0[0]
            vec_717 = param_719_1[0]

        vec_index716 = 0
        vec_index717 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_716[:]
        vec_index716 = 0
        # Program VectorClear Region
        del vec_717[:]
        vec_index717 = 0
        # Program Return Region
        return False
        return False

    def exported_symbol_2(self, vec_721: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index721: int = 0
        vec_724: List[int] = list()
        vec_index724: int = 0
        vec_727: List[int] = list()
        vec_index727: int = 0
        vec_728: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index728: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index721 = 0
        while vec_index721 < len(vec_721):
            var_722, var_723 = vec_721[vec_index721]
            vec_index721 += 1
            # Program TransitionState Region
            tuple_722 = var_722
            prev_state = self.table_61[tuple_722]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_61[tuple_722] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_724.append(var_722)
        # Program VectorUnique Region
        vec_724 = list(set(vec_724))
        vec_index724 = 0
        # Program TableJoin Region
        while vec_index724 < len(vec_724):
            var_726 = vec_724[vec_index724]
            vec_index724 += 1
            if var_726 in self.index_186:
                if var_726 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_726 = var_726
                    prev_state = self.table_15[tuple_726]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_726] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_727.append(var_726)
        # Program VectorClear Region
        del vec_724[:]
        vec_index724 = 0
        # Induction Fixpoint Loop Region
        while len(vec_727) or len(vec_728):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_727, vec_728)

            # Program Call Region
            param_730_0 = [vec_727]
            param_730_1 = [vec_728]
            ret = self.proc_173_(param_730_0, param_730_1)
            vec_727 = param_730_0[0]
            vec_728 = param_730_1[0]

        vec_index727 = 0
        vec_index728 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_727[:]
        vec_index727 = 0
        # Program VectorClear Region
        del vec_728[:]
        vec_index728 = 0
        # Program Return Region
        return False
        return False

    def local_symbol_2(self, vec_732: List[Tuple[int, bytes]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index732: int = 0
        vec_735: List[int] = list()
        vec_index735: int = 0
        vec_738: List[int] = list()
        vec_index738: int = 0
        vec_739: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index739: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index732 = 0
        while vec_index732 < len(vec_732):
            var_733, var_734 = vec_732[vec_index732]
            vec_index732 += 1
            # Program TransitionState Region
            tuple_733 = var_733
            prev_state = self.table_63[tuple_733]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_63[tuple_733] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_735.append(var_733)
        # Program VectorUnique Region
        vec_735 = list(set(vec_735))
        vec_index735 = 0
        # Program TableJoin Region
        while vec_index735 < len(vec_735):
            var_737 = vec_735[vec_index735]
            vec_index735 += 1
            if var_737 in self.index_171:
                if var_737 in self.index_172:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_737 = var_737
                    prev_state = self.table_15[tuple_737]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_737] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_738.append(var_737)
        # Program VectorClear Region
        del vec_735[:]
        vec_index735 = 0
        # Induction Fixpoint Loop Region
        while len(vec_738) or len(vec_739):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_738, vec_739)

            # Program Call Region
            param_741_0 = [vec_738]
            param_741_1 = [vec_739]
            ret = self.proc_173_(param_741_0, param_741_1)
            vec_738 = param_741_0[0]
            vec_739 = param_741_1[0]

        vec_index738 = 0
        vec_index739 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_738[:]
        vec_index738 = 0
        # Program VectorClear Region
        del vec_739[:]
        vec_index739 = 0
        # Program Return Region
        return False
        return False

    def raw_transfer_3(self, vec_743: List[Tuple[int, int, ControlFlowEdgeKind]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index743: int = 0
        vec_747: List[int] = list()
        vec_index747: int = 0
        vec_750: List[int] = list()
        vec_index750: int = 0
        vec_751: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index751: int = 0
        vec_754: List[Tuple[int, int]] = list()
        vec_index754: int = 0
        vec_760: List[int] = list()
        vec_index760: int = 0
        vec_765: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index765: int = 0
        vec_768: List[int] = list()
        vec_index768: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index743 = 0
        while vec_index743 < len(vec_743):
            var_744, var_745, var_746 = vec_743[vec_index743]
            vec_index743 += 1
            # Program Parallel Region
            # Program TransitionState Region
            tuple_745 = var_745
            prev_state = self.table_67[tuple_745]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_67[tuple_745] = 1 | 4
                if not present_bit:
                    pass
                # Program VectorAppend Region
                vec_747.append(var_745)
            # Program TupleCompare Region
            if self.var_0 == var_746:
                # Program TransitionState Region
                tuple_744_745 = (var_744, var_745)
                prev_state = self.table_120[tuple_744_745]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_120[tuple_744_745] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_754.append((var_744, var_745))
            # Program TupleCompare Region
            if self.var_7 == var_746:
                # Program TransitionState Region
                tuple_744_745 = (var_744, var_745)
                prev_state = self.table_123[tuple_744_745]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_123[tuple_744_745] = 1 | 4
                    if not present_bit:
                        pass
                    # Program VectorAppend Region
                    vec_754.append((var_744, var_745))
            # Program TupleCompare Region
            if var_746 != self.var_0:
                # Program TupleCompare Region
                if var_746 != self.var_7:
                    # Program TransitionState Region
                    var_746 = self._resolve_edgetype(var_746)
                    tuple_746_744_745 = (var_746, var_744, var_745)
                    prev_state = self.table_141[tuple_746_744_745]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_141[tuple_746_744_745] = 1 | 4
                        if not present_bit:
                            self.index_247[tuple_746_744_745[2]].append((tuple_746_744_745[0], tuple_746_744_745[1]))
                        # Program VectorAppend Region
                        vec_760.append(var_745)
        # Program VectorUnique Region
        vec_747 = list(set(vec_747))
        vec_index747 = 0
        # Program TableJoin Region
        while vec_index747 < len(vec_747):
            var_749 = vec_747[vec_index747]
            vec_index747 += 1
            if var_749 in self.index_451:
                if var_749 in self.index_596:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_749 = var_749
                    prev_state = self.table_15[tuple_749]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_749] = 1 | 4
                        if not present_bit:
                            pass
                        # Program VectorAppend Region
                        vec_750.append(var_749)
        # Program VectorClear Region
        del vec_747[:]
        vec_index747 = 0
        # Program VectorUnique Region
        vec_754 = list(set(vec_754))
        vec_index754 = 0
        # Program TableJoin Region
        while vec_index754 < len(vec_754):
            var_756, var_757 = vec_754[vec_index754]
            vec_index754 += 1
            if (var_756, var_757) in self.index_758:
                if (var_756, var_757) in self.index_759:
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_756_757 = (var_756, var_757)
                    prev_state = self.table_126[tuple_756_757]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_126[tuple_756_757] = 1 | 4
                        if not present_bit:
                            self.index_284[tuple_756_757[1]].append(tuple_756_757[0])
                        # Program VectorAppend Region
                        vec_768.append(var_757)
        # Program VectorClear Region
        del vec_754[:]
        vec_index754 = 0
        # Program VectorUnique Region
        vec_760 = list(set(vec_760))
        vec_index760 = 0
        # Program TableJoin Region
        while vec_index760 < len(vec_760):
            var_762 = vec_760[vec_index760]
            vec_index760 += 1
            tuple_761_0_index: int = 0
            tuple_761_0_vec: List[Tuple[ControlFlowEdgeKind, int]] = self.index_247[var_762]
            while tuple_761_0_index < len(tuple_761_0_vec):
                tuple_761_0 = tuple_761_0_vec[tuple_761_0_index]
                tuple_761_0_index += 1
                var_763 = tuple_761_0[0]
                var_764 = tuple_761_0[1]
                if var_762 in self.index_248:
                    # Program TransitionState Region
                    var_763 = self._resolve_edgetype(var_763)
                    tuple_764_762_763 = (var_764, var_762, var_763)
                    prev_state = self.table_11[tuple_764_762_763]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_764_762_763] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_764_762_763[1], tuple_764_762_763[2])].append(tuple_764_762_763[0])
                        # Program VectorAppend Region
                        var_763 = self._resolve_edgetype(var_763)
                        vec_765.append((var_764, var_762, var_763))
        # Program VectorClear Region
        del vec_760[:]
        vec_index760 = 0
        # Program VectorUnique Region
        vec_768 = list(set(vec_768))
        vec_index768 = 0
        # Program TableJoin Region
        while vec_index768 < len(vec_768):
            var_770 = vec_768[vec_index768]
            vec_index768 += 1
            if var_770 in self.index_248:
                tuple_769_1_index: int = 0
                tuple_769_1_vec: List[int] = self.index_284[var_770]
                while tuple_769_1_index < len(tuple_769_1_vec):
                    tuple_769_1 = tuple_769_1_vec[tuple_769_1_index]
                    tuple_769_1_index += 1
                    var_771 = tuple_769_1
                    # Program TransitionState Region
                    tuple_771_770_6 = (var_771, var_770, self.var_6)
                    prev_state = self.table_11[tuple_771_770_6]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_771_770_6] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_771_770_6[1], tuple_771_770_6[2])].append(tuple_771_770_6[0])
                        # Program VectorAppend Region
                        vec_765.append((var_771, var_770, self.var_6))
        # Program VectorClear Region
        del vec_768[:]
        vec_index768 = 0
        # Induction Fixpoint Loop Region
        while len(vec_750) or len(vec_751) or len(vec_765):
            # Program Series Region
            # Program Call Region
            ret = self.proc_253_(vec_765)

            # Program Call Region
            param_767_0 = [vec_765]
            ret = self.proc_251_(param_767_0)
            vec_765 = param_767_0[0]

            # Program Call Region
            ret = self.proc_176_(vec_750, vec_751)

            # Program Call Region
            param_753_0 = [vec_750]
            param_753_1 = [vec_751]
            ret = self.proc_173_(param_753_0, param_753_1)
            vec_750 = param_753_0[0]
            vec_751 = param_753_1[0]

        vec_index750 = 0
        vec_index751 = 0
        vec_index765 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_765[:]
        vec_index765 = 0
        # Program VectorClear Region
        del vec_750[:]
        vec_index750 = 0
        # Program VectorClear Region
        del vec_751[:]
        vec_index751 = 0
        # Program Return Region
        return False
        return False

    def address_operand_2(self, vec_773: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index773: int = 0
        vec_776: List[int] = list()
        vec_index776: int = 0
        vec_780: List[int] = list()
        vec_index780: int = 0
        vec_784: List[int] = list()
        vec_index784: int = 0
        vec_788: List[int] = list()
        vec_index788: int = 0
        vec_792: List[int] = list()
        vec_index792: int = 0
        vec_797: List[int] = list()
        vec_index797: int = 0
        vec_802: List[int] = list()
        vec_index802: int = 0
        vec_807: List[int] = list()
        vec_index807: int = 0
        vec_812: List[int] = list()
        vec_index812: int = 0
        vec_816: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index816: int = 0
        vec_819: List[int] = list()
        vec_index819: int = 0
        vec_823: List[int] = list()
        vec_index823: int = 0
        vec_827: List[int] = list()
        vec_index827: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index773 = 0
        while vec_index773 < len(vec_773):
            var_774, var_775 = vec_773[vec_index773]
            vec_index773 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_774_775 = (var_774, var_775)
            prev_state = self.table_84[tuple_774_775]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_84[tuple_774_775] = 1 | 4
                if not present_bit:
                    self.index_215[tuple_774_775[0]].append(tuple_774_775[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_788.append(var_774)
                # Program VectorAppend Region
                vec_784.append(var_774)
                # Program VectorAppend Region
                vec_780.append(var_774)
                # Program VectorAppend Region
                vec_776.append(var_774)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_774_775 = (var_774, var_775)
            prev_state = self.table_84[tuple_774_775]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_84[tuple_774_775] = 1 | 4
                if not present_bit:
                    self.index_215[tuple_774_775[0]].append(tuple_774_775[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_788.append(var_774)
                # Program VectorAppend Region
                vec_784.append(var_774)
                # Program VectorAppend Region
                vec_780.append(var_774)
                # Program VectorAppend Region
                vec_776.append(var_774)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_774_775 = (var_774, var_775)
            prev_state = self.table_84[tuple_774_775]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_84[tuple_774_775] = 1 | 4
                if not present_bit:
                    self.index_215[tuple_774_775[0]].append(tuple_774_775[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_788.append(var_774)
                # Program VectorAppend Region
                vec_784.append(var_774)
                # Program VectorAppend Region
                vec_780.append(var_774)
                # Program VectorAppend Region
                vec_776.append(var_774)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_774_775 = (var_774, var_775)
            prev_state = self.table_84[tuple_774_775]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_84[tuple_774_775] = 1 | 4
                if not present_bit:
                    self.index_215[tuple_774_775[0]].append(tuple_774_775[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_788.append(var_774)
                # Program VectorAppend Region
                vec_784.append(var_774)
                # Program VectorAppend Region
                vec_780.append(var_774)
                # Program VectorAppend Region
                vec_776.append(var_774)
        # Program VectorUnique Region
        vec_776 = list(set(vec_776))
        vec_index776 = 0
        # Program TableJoin Region
        while vec_index776 < len(vec_776):
            var_778 = vec_776[vec_index776]
            vec_index776 += 1
            if var_778 in self.index_214:
                tuple_777_1_index: int = 0
                tuple_777_1_vec: List[int] = self.index_215[var_778]
                while tuple_777_1_index < len(tuple_777_1_vec):
                    tuple_777_1 = tuple_777_1_vec[tuple_777_1_index]
                    tuple_777_1_index += 1
                    var_779 = tuple_777_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_778_779 = (var_778, var_779)
                    prev_state = self.table_114[tuple_778_779]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_114[tuple_778_779] = 1 | 4
                        if not present_bit:
                            self.index_278[tuple_778_779[1]].append(tuple_778_779[0])
                        # Program VectorAppend Region
                        vec_802.append(var_779)
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
            if var_782 in self.index_220:
                tuple_781_1_index: int = 0
                tuple_781_1_vec: List[int] = self.index_215[var_782]
                while tuple_781_1_index < len(tuple_781_1_vec):
                    tuple_781_1 = tuple_781_1_vec[tuple_781_1_index]
                    tuple_781_1_index += 1
                    var_783 = tuple_781_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_782_783 = (var_782, var_783)
                    prev_state = self.table_106[tuple_782_783]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_106[tuple_782_783] = 1 | 4
                        if not present_bit:
                            self.index_272[tuple_782_783[1]].append(tuple_782_783[0])
                        # Program VectorAppend Region
                        vec_797.append(var_783)
        # Program VectorClear Region
        del vec_780[:]
        vec_index780 = 0
        # Program VectorUnique Region
        vec_784 = list(set(vec_784))
        vec_index784 = 0
        # Program TableJoin Region
        while vec_index784 < len(vec_784):
            var_786 = vec_784[vec_index784]
            vec_index784 += 1
            if var_786 in self.index_225:
                tuple_785_1_index: int = 0
                tuple_785_1_vec: List[int] = self.index_215[var_786]
                while tuple_785_1_index < len(tuple_785_1_vec):
                    tuple_785_1 = tuple_785_1_vec[tuple_785_1_index]
                    tuple_785_1_index += 1
                    var_787 = tuple_785_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_786_787 = (var_786, var_787)
                    prev_state = self.table_98[tuple_786_787]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_98[tuple_786_787] = 1 | 4
                        if not present_bit:
                            self.index_266[tuple_786_787[1]].append(tuple_786_787[0])
                        # Program VectorAppend Region
                        vec_792.append(var_787)
        # Program VectorClear Region
        del vec_784[:]
        vec_index784 = 0
        # Program VectorUnique Region
        vec_788 = list(set(vec_788))
        vec_index788 = 0
        # Program TableJoin Region
        while vec_index788 < len(vec_788):
            var_790 = vec_788[vec_index788]
            vec_index788 += 1
            if var_790 in self.index_230:
                tuple_789_1_index: int = 0
                tuple_789_1_vec: List[int] = self.index_215[var_790]
                while tuple_789_1_index < len(tuple_789_1_vec):
                    tuple_789_1 = tuple_789_1_vec[tuple_789_1_index]
                    tuple_789_1_index += 1
                    var_791 = tuple_789_1
                    # Program TransitionState Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
                    tuple_790_791 = (var_790, var_791)
                    prev_state = self.table_90[tuple_790_791]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_90[tuple_790_791] = 1 | 4
                        if not present_bit:
                            self.index_305[tuple_790_791[1]].append(tuple_790_791[0])
                        # Program VectorAppend Region
                        vec_807.append(var_791)
        # Program VectorClear Region
        del vec_788[:]
        vec_index788 = 0
        # Program VectorUnique Region
        vec_792 = list(set(vec_792))
        vec_index792 = 0
        # Program TableJoin Region
        while vec_index792 < len(vec_792):
            var_794 = vec_792[vec_index792]
            vec_index792 += 1
            tuple_793_0_index: int = 0
            tuple_793_0_vec: List[int] = self.index_265[var_794]
            while tuple_793_0_index < len(tuple_793_0_vec):
                tuple_793_0 = tuple_793_0_vec[tuple_793_0_index]
                tuple_793_0_index += 1
                var_795 = tuple_793_0
                tuple_793_1_index: int = 0
                tuple_793_1_vec: List[int] = self.index_266[var_794]
                while tuple_793_1_index < len(tuple_793_1_vec):
                    tuple_793_1 = tuple_793_1_vec[tuple_793_1_index]
                    tuple_793_1_index += 1
                    var_796 = tuple_793_1
                    # Program TransitionState Region
                    tuple_795_796 = (var_795, var_796)
                    prev_state = self.table_101[tuple_795_796]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_101[tuple_795_796] = 1 | 4
                        if not present_bit:
                            self.index_331[tuple_795_796[0]].append(tuple_795_796[1])
                        # Program VectorAppend Region
                        vec_823.append(var_795)
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
            tuple_798_0_vec: List[int] = self.index_265[var_799]
            while tuple_798_0_index < len(tuple_798_0_vec):
                tuple_798_0 = tuple_798_0_vec[tuple_798_0_index]
                tuple_798_0_index += 1
                var_800 = tuple_798_0
                tuple_798_1_index: int = 0
                tuple_798_1_vec: List[int] = self.index_272[var_799]
                while tuple_798_1_index < len(tuple_798_1_vec):
                    tuple_798_1 = tuple_798_1_vec[tuple_798_1_index]
                    tuple_798_1_index += 1
                    var_801 = tuple_798_1
                    # Program TransitionState Region
                    tuple_800_801 = (var_800, var_801)
                    prev_state = self.table_109[tuple_800_801]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_800_801] = 1 | 4
                        if not present_bit:
                            self.index_326[tuple_800_801[0]].append(tuple_800_801[1])
                        # Program VectorAppend Region
                        vec_819.append(var_800)
        # Program VectorClear Region
        del vec_797[:]
        vec_index797 = 0
        # Program VectorUnique Region
        vec_802 = list(set(vec_802))
        vec_index802 = 0
        # Program TableJoin Region
        while vec_index802 < len(vec_802):
            var_804 = vec_802[vec_index802]
            vec_index802 += 1
            tuple_803_0_index: int = 0
            tuple_803_0_vec: List[int] = self.index_265[var_804]
            while tuple_803_0_index < len(tuple_803_0_vec):
                tuple_803_0 = tuple_803_0_vec[tuple_803_0_index]
                tuple_803_0_index += 1
                var_805 = tuple_803_0
                tuple_803_1_index: int = 0
                tuple_803_1_vec: List[int] = self.index_278[var_804]
                while tuple_803_1_index < len(tuple_803_1_vec):
                    tuple_803_1 = tuple_803_1_vec[tuple_803_1_index]
                    tuple_803_1_index += 1
                    var_806 = tuple_803_1
                    # Program TransitionState Region
                    tuple_805_806 = (var_805, var_806)
                    prev_state = self.table_117[tuple_805_806]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_117[tuple_805_806] = 1 | 4
                        if not present_bit:
                            self.index_321[tuple_805_806[0]].append(tuple_805_806[1])
                        # Program VectorAppend Region
                        vec_812.append(var_805)
        # Program VectorClear Region
        del vec_802[:]
        vec_index802 = 0
        # Program VectorUnique Region
        vec_807 = list(set(vec_807))
        vec_index807 = 0
        # Program TableJoin Region
        while vec_index807 < len(vec_807):
            var_809 = vec_807[vec_index807]
            vec_index807 += 1
            tuple_808_0_index: int = 0
            tuple_808_0_vec: List[int] = self.index_265[var_809]
            while tuple_808_0_index < len(tuple_808_0_vec):
                tuple_808_0 = tuple_808_0_vec[tuple_808_0_index]
                tuple_808_0_index += 1
                var_810 = tuple_808_0
                tuple_808_1_index: int = 0
                tuple_808_1_vec: List[int] = self.index_305[var_809]
                while tuple_808_1_index < len(tuple_808_1_vec):
                    tuple_808_1 = tuple_808_1_vec[tuple_808_1_index]
                    tuple_808_1_index += 1
                    var_811 = tuple_808_1
                    # Program TransitionState Region
                    tuple_810_811 = (var_810, var_811)
                    prev_state = self.table_93[tuple_810_811]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_93[tuple_810_811] = 1 | 4
                        if not present_bit:
                            self.index_336[tuple_810_811[0]].append(tuple_810_811[1])
                        # Program VectorAppend Region
                        vec_827.append(var_810)
        # Program VectorClear Region
        del vec_807[:]
        vec_index807 = 0
        # Program VectorUnique Region
        vec_812 = list(set(vec_812))
        vec_index812 = 0
        # Program TableJoin Region
        while vec_index812 < len(vec_812):
            var_814 = vec_812[vec_index812]
            vec_index812 += 1
            if var_814 in self.index_248:
                tuple_813_1_index: int = 0
                tuple_813_1_vec: List[int] = self.index_321[var_814]
                while tuple_813_1_index < len(tuple_813_1_vec):
                    tuple_813_1 = tuple_813_1_vec[tuple_813_1_index]
                    tuple_813_1_index += 1
                    var_815 = tuple_813_1
                    # Program TransitionState Region
                    tuple_815_814_0 = (var_815, var_814, self.var_0)
                    prev_state = self.table_11[tuple_815_814_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_815_814_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_815_814_0[1], tuple_815_814_0[2])].append(tuple_815_814_0[0])
                        # Program VectorAppend Region
                        vec_816.append((var_815, var_814, self.var_0))
        # Program VectorClear Region
        del vec_812[:]
        vec_index812 = 0
        # Program VectorUnique Region
        vec_819 = list(set(vec_819))
        vec_index819 = 0
        # Program TableJoin Region
        while vec_index819 < len(vec_819):
            var_821 = vec_819[vec_index819]
            vec_index819 += 1
            if var_821 in self.index_248:
                tuple_820_1_index: int = 0
                tuple_820_1_vec: List[int] = self.index_326[var_821]
                while tuple_820_1_index < len(tuple_820_1_vec):
                    tuple_820_1 = tuple_820_1_vec[tuple_820_1_index]
                    tuple_820_1_index += 1
                    var_822 = tuple_820_1
                    # Program TransitionState Region
                    tuple_822_821_0 = (var_822, var_821, self.var_0)
                    prev_state = self.table_11[tuple_822_821_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_822_821_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_822_821_0[1], tuple_822_821_0[2])].append(tuple_822_821_0[0])
                        # Program VectorAppend Region
                        vec_816.append((var_822, var_821, self.var_0))
        # Program VectorClear Region
        del vec_819[:]
        vec_index819 = 0
        # Program VectorUnique Region
        vec_823 = list(set(vec_823))
        vec_index823 = 0
        # Program TableJoin Region
        while vec_index823 < len(vec_823):
            var_825 = vec_823[vec_index823]
            vec_index823 += 1
            if var_825 in self.index_248:
                tuple_824_1_index: int = 0
                tuple_824_1_vec: List[int] = self.index_331[var_825]
                while tuple_824_1_index < len(tuple_824_1_vec):
                    tuple_824_1 = tuple_824_1_vec[tuple_824_1_index]
                    tuple_824_1_index += 1
                    var_826 = tuple_824_1
                    # Program TransitionState Region
                    tuple_826_825_2 = (var_826, var_825, self.var_2)
                    prev_state = self.table_11[tuple_826_825_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_826_825_2] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_826_825_2[1], tuple_826_825_2[2])].append(tuple_826_825_2[0])
                        # Program VectorAppend Region
                        vec_816.append((var_826, var_825, self.var_2))
        # Program VectorClear Region
        del vec_823[:]
        vec_index823 = 0
        # Program VectorUnique Region
        vec_827 = list(set(vec_827))
        vec_index827 = 0
        # Program TableJoin Region
        while vec_index827 < len(vec_827):
            var_829 = vec_827[vec_index827]
            vec_index827 += 1
            if var_829 in self.index_248:
                tuple_828_1_index: int = 0
                tuple_828_1_vec: List[int] = self.index_336[var_829]
                while tuple_828_1_index < len(tuple_828_1_vec):
                    tuple_828_1 = tuple_828_1_vec[tuple_828_1_index]
                    tuple_828_1_index += 1
                    var_830 = tuple_828_1
                    # Program TransitionState Region
                    tuple_830_829_2 = (var_830, var_829, self.var_2)
                    prev_state = self.table_11[tuple_830_829_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_830_829_2] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_830_829_2[1], tuple_830_829_2[2])].append(tuple_830_829_2[0])
                        # Program VectorAppend Region
                        vec_816.append((var_830, var_829, self.var_2))
        # Program VectorClear Region
        del vec_827[:]
        vec_index827 = 0
        # Induction Fixpoint Loop Region
        while len(vec_816):
            # Program Series Region
            # Program Call Region
            ret = self.proc_253_(vec_816)

            # Program Call Region
            param_818_0 = [vec_816]
            ret = self.proc_251_(param_818_0)
            vec_816 = param_818_0[0]

        vec_index816 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_816[:]
        vec_index816 = 0
        # Program Return Region
        return False
        return False

    def relocation_2(self, vec_832: List[Tuple[int, int]]) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_index832: int = 0
        vec_835: List[int] = list()
        vec_index835: int = 0
        vec_840: List[int] = list()
        vec_index840: int = 0
        vec_845: List[int] = list()
        vec_index845: int = 0
        vec_850: List[int] = list()
        vec_index850: int = 0
        vec_855: List[int] = list()
        vec_index855: int = 0
        vec_859: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index859: int = 0
        vec_862: List[int] = list()
        vec_index862: int = 0
        vec_866: List[int] = list()
        vec_index866: int = 0
        vec_870: List[int] = list()
        vec_index870: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program VectorLoop Region
        vec_index832 = 0
        while vec_index832 < len(vec_832):
            var_833, var_834 = vec_832[vec_index832]
            vec_index832 += 1
            # Program Parallel Region
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_833_834 = (var_833, var_834)
            prev_state = self.table_87[tuple_833_834]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_87[tuple_833_834] = 1 | 4
                if not present_bit:
                    self.index_265[tuple_833_834[0]].append(tuple_833_834[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_850.append(var_833)
                # Program VectorAppend Region
                vec_845.append(var_833)
                # Program VectorAppend Region
                vec_840.append(var_833)
                # Program VectorAppend Region
                vec_835.append(var_833)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_833_834 = (var_833, var_834)
            prev_state = self.table_87[tuple_833_834]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_87[tuple_833_834] = 1 | 4
                if not present_bit:
                    self.index_265[tuple_833_834[0]].append(tuple_833_834[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_850.append(var_833)
                # Program VectorAppend Region
                vec_845.append(var_833)
                # Program VectorAppend Region
                vec_840.append(var_833)
                # Program VectorAppend Region
                vec_835.append(var_833)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_833_834 = (var_833, var_834)
            prev_state = self.table_87[tuple_833_834]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_87[tuple_833_834] = 1 | 4
                if not present_bit:
                    self.index_265[tuple_833_834[0]].append(tuple_833_834[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_850.append(var_833)
                # Program VectorAppend Region
                vec_845.append(var_833)
                # Program VectorAppend Region
                vec_840.append(var_833)
                # Program VectorAppend Region
                vec_835.append(var_833)
            # Program TransitionState Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildEagerSuccessorRegions
            tuple_833_834 = (var_833, var_834)
            prev_state = self.table_87[tuple_833_834]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_87[tuple_833_834] = 1 | 4
                if not present_bit:
                    self.index_265[tuple_833_834[0]].append(tuple_833_834[1])
                # Program Parallel Region
                # Program VectorAppend Region
                vec_850.append(var_833)
                # Program VectorAppend Region
                vec_845.append(var_833)
                # Program VectorAppend Region
                vec_840.append(var_833)
                # Program VectorAppend Region
                vec_835.append(var_833)
        # Program VectorUnique Region
        vec_835 = list(set(vec_835))
        vec_index835 = 0
        # Program TableJoin Region
        while vec_index835 < len(vec_835):
            var_837 = vec_835[vec_index835]
            vec_index835 += 1
            tuple_836_0_index: int = 0
            tuple_836_0_vec: List[int] = self.index_265[var_837]
            while tuple_836_0_index < len(tuple_836_0_vec):
                tuple_836_0 = tuple_836_0_vec[tuple_836_0_index]
                tuple_836_0_index += 1
                var_838 = tuple_836_0
                tuple_836_1_index: int = 0
                tuple_836_1_vec: List[int] = self.index_278[var_837]
                while tuple_836_1_index < len(tuple_836_1_vec):
                    tuple_836_1 = tuple_836_1_vec[tuple_836_1_index]
                    tuple_836_1_index += 1
                    var_839 = tuple_836_1
                    # Program TransitionState Region
                    tuple_838_839 = (var_838, var_839)
                    prev_state = self.table_117[tuple_838_839]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_117[tuple_838_839] = 1 | 4
                        if not present_bit:
                            self.index_321[tuple_838_839[0]].append(tuple_838_839[1])
                        # Program VectorAppend Region
                        vec_866.append(var_838)
        # Program VectorClear Region
        del vec_835[:]
        vec_index835 = 0
        # Program VectorUnique Region
        vec_840 = list(set(vec_840))
        vec_index840 = 0
        # Program TableJoin Region
        while vec_index840 < len(vec_840):
            var_842 = vec_840[vec_index840]
            vec_index840 += 1
            tuple_841_0_index: int = 0
            tuple_841_0_vec: List[int] = self.index_265[var_842]
            while tuple_841_0_index < len(tuple_841_0_vec):
                tuple_841_0 = tuple_841_0_vec[tuple_841_0_index]
                tuple_841_0_index += 1
                var_843 = tuple_841_0
                tuple_841_1_index: int = 0
                tuple_841_1_vec: List[int] = self.index_272[var_842]
                while tuple_841_1_index < len(tuple_841_1_vec):
                    tuple_841_1 = tuple_841_1_vec[tuple_841_1_index]
                    tuple_841_1_index += 1
                    var_844 = tuple_841_1
                    # Program TransitionState Region
                    tuple_843_844 = (var_843, var_844)
                    prev_state = self.table_109[tuple_843_844]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_109[tuple_843_844] = 1 | 4
                        if not present_bit:
                            self.index_326[tuple_843_844[0]].append(tuple_843_844[1])
                        # Program VectorAppend Region
                        vec_862.append(var_843)
        # Program VectorClear Region
        del vec_840[:]
        vec_index840 = 0
        # Program VectorUnique Region
        vec_845 = list(set(vec_845))
        vec_index845 = 0
        # Program TableJoin Region
        while vec_index845 < len(vec_845):
            var_847 = vec_845[vec_index845]
            vec_index845 += 1
            tuple_846_0_index: int = 0
            tuple_846_0_vec: List[int] = self.index_265[var_847]
            while tuple_846_0_index < len(tuple_846_0_vec):
                tuple_846_0 = tuple_846_0_vec[tuple_846_0_index]
                tuple_846_0_index += 1
                var_848 = tuple_846_0
                tuple_846_1_index: int = 0
                tuple_846_1_vec: List[int] = self.index_266[var_847]
                while tuple_846_1_index < len(tuple_846_1_vec):
                    tuple_846_1 = tuple_846_1_vec[tuple_846_1_index]
                    tuple_846_1_index += 1
                    var_849 = tuple_846_1
                    # Program TransitionState Region
                    tuple_848_849 = (var_848, var_849)
                    prev_state = self.table_101[tuple_848_849]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_101[tuple_848_849] = 1 | 4
                        if not present_bit:
                            self.index_331[tuple_848_849[0]].append(tuple_848_849[1])
                        # Program VectorAppend Region
                        vec_855.append(var_848)
        # Program VectorClear Region
        del vec_845[:]
        vec_index845 = 0
        # Program VectorUnique Region
        vec_850 = list(set(vec_850))
        vec_index850 = 0
        # Program TableJoin Region
        while vec_index850 < len(vec_850):
            var_852 = vec_850[vec_index850]
            vec_index850 += 1
            tuple_851_0_index: int = 0
            tuple_851_0_vec: List[int] = self.index_265[var_852]
            while tuple_851_0_index < len(tuple_851_0_vec):
                tuple_851_0 = tuple_851_0_vec[tuple_851_0_index]
                tuple_851_0_index += 1
                var_853 = tuple_851_0
                tuple_851_1_index: int = 0
                tuple_851_1_vec: List[int] = self.index_305[var_852]
                while tuple_851_1_index < len(tuple_851_1_vec):
                    tuple_851_1 = tuple_851_1_vec[tuple_851_1_index]
                    tuple_851_1_index += 1
                    var_854 = tuple_851_1
                    # Program TransitionState Region
                    tuple_853_854 = (var_853, var_854)
                    prev_state = self.table_93[tuple_853_854]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_93[tuple_853_854] = 1 | 4
                        if not present_bit:
                            self.index_336[tuple_853_854[0]].append(tuple_853_854[1])
                        # Program VectorAppend Region
                        vec_870.append(var_853)
        # Program VectorClear Region
        del vec_850[:]
        vec_index850 = 0
        # Program VectorUnique Region
        vec_855 = list(set(vec_855))
        vec_index855 = 0
        # Program TableJoin Region
        while vec_index855 < len(vec_855):
            var_857 = vec_855[vec_index855]
            vec_index855 += 1
            if var_857 in self.index_248:
                tuple_856_1_index: int = 0
                tuple_856_1_vec: List[int] = self.index_331[var_857]
                while tuple_856_1_index < len(tuple_856_1_vec):
                    tuple_856_1 = tuple_856_1_vec[tuple_856_1_index]
                    tuple_856_1_index += 1
                    var_858 = tuple_856_1
                    # Program TransitionState Region
                    tuple_858_857_2 = (var_858, var_857, self.var_2)
                    prev_state = self.table_11[tuple_858_857_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_858_857_2] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_858_857_2[1], tuple_858_857_2[2])].append(tuple_858_857_2[0])
                        # Program VectorAppend Region
                        vec_859.append((var_858, var_857, self.var_2))
        # Program VectorClear Region
        del vec_855[:]
        vec_index855 = 0
        # Program VectorUnique Region
        vec_862 = list(set(vec_862))
        vec_index862 = 0
        # Program TableJoin Region
        while vec_index862 < len(vec_862):
            var_864 = vec_862[vec_index862]
            vec_index862 += 1
            if var_864 in self.index_248:
                tuple_863_1_index: int = 0
                tuple_863_1_vec: List[int] = self.index_326[var_864]
                while tuple_863_1_index < len(tuple_863_1_vec):
                    tuple_863_1 = tuple_863_1_vec[tuple_863_1_index]
                    tuple_863_1_index += 1
                    var_865 = tuple_863_1
                    # Program TransitionState Region
                    tuple_865_864_0 = (var_865, var_864, self.var_0)
                    prev_state = self.table_11[tuple_865_864_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_865_864_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_865_864_0[1], tuple_865_864_0[2])].append(tuple_865_864_0[0])
                        # Program VectorAppend Region
                        vec_859.append((var_865, var_864, self.var_0))
        # Program VectorClear Region
        del vec_862[:]
        vec_index862 = 0
        # Program VectorUnique Region
        vec_866 = list(set(vec_866))
        vec_index866 = 0
        # Program TableJoin Region
        while vec_index866 < len(vec_866):
            var_868 = vec_866[vec_index866]
            vec_index866 += 1
            if var_868 in self.index_248:
                tuple_867_1_index: int = 0
                tuple_867_1_vec: List[int] = self.index_321[var_868]
                while tuple_867_1_index < len(tuple_867_1_vec):
                    tuple_867_1 = tuple_867_1_vec[tuple_867_1_index]
                    tuple_867_1_index += 1
                    var_869 = tuple_867_1
                    # Program TransitionState Region
                    tuple_869_868_0 = (var_869, var_868, self.var_0)
                    prev_state = self.table_11[tuple_869_868_0]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_869_868_0] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_869_868_0[1], tuple_869_868_0[2])].append(tuple_869_868_0[0])
                        # Program VectorAppend Region
                        vec_859.append((var_869, var_868, self.var_0))
        # Program VectorClear Region
        del vec_866[:]
        vec_index866 = 0
        # Program VectorUnique Region
        vec_870 = list(set(vec_870))
        vec_index870 = 0
        # Program TableJoin Region
        while vec_index870 < len(vec_870):
            var_872 = vec_870[vec_index870]
            vec_index870 += 1
            if var_872 in self.index_248:
                tuple_871_1_index: int = 0
                tuple_871_1_vec: List[int] = self.index_336[var_872]
                while tuple_871_1_index < len(tuple_871_1_vec):
                    tuple_871_1 = tuple_871_1_vec[tuple_871_1_index]
                    tuple_871_1_index += 1
                    var_873 = tuple_871_1
                    # Program TransitionState Region
                    tuple_873_872_2 = (var_873, var_872, self.var_2)
                    prev_state = self.table_11[tuple_873_872_2]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_11[tuple_873_872_2] = 1 | 4
                        if not present_bit:
                            self.index_1479[(tuple_873_872_2[1], tuple_873_872_2[2])].append(tuple_873_872_2[0])
                        # Program VectorAppend Region
                        vec_859.append((var_873, var_872, self.var_2))
        # Program VectorClear Region
        del vec_870[:]
        vec_index870 = 0
        # Induction Fixpoint Loop Region
        while len(vec_859):
            # Program Series Region
            # Program Call Region
            ret = self.proc_253_(vec_859)

            # Program Call Region
            param_861_0 = [vec_859]
            ret = self.proc_251_(param_861_0)
            vec_859 = param_861_0[0]

        vec_index859 = 0
        # Induction Output Region
        # Program VectorClear Region
        del vec_859[:]
        vec_index859 = 0
        # Program Return Region
        return False
        return False

    def proc_874_(self, var_875: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_26[var_875] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_875 = var_875
            prev_state = self.table_26[tuple_875]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_26[tuple_875] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker::call_pred
                ret = self.proc_1069_(var_875)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_875 = var_875
                    prev_state = self.table_26[tuple_875]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_26[tuple_875] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_877_(self, var_878: int, var_879: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_28[(var_878, var_879)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_878_879 = (var_878, var_879)
            prev_state = self.table_28[tuple_878_879]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_28[tuple_878_879] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker::call_pred
                ret = self.proc_1050_(var_879, var_878)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_878_879 = (var_878, var_879)
                    prev_state = self.table_28[tuple_878_879]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_28[tuple_878_879] = 1 | 4
                        if not present_bit:
                            self.index_876[tuple_878_879[0]].append(tuple_878_879[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_880_(self, var_881: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_1042_(var_881)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_883_(self, var_884: int, var_885: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker
        ret = self.proc_900_(var_884, var_885)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_887_(self, var_888: int, var_889: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_33[(var_888, var_889)] & 3
        if state == 0:
            # Program Return Region
            return False
        elif state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_888_889 = (var_888, var_889)
            prev_state = self.table_33[tuple_888_889]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_33[tuple_888_889] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: BuildTopDownInsertChecker::call_pred
                ret = self.proc_890_(var_889, var_888)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_888_889 = (var_888, var_889)
                    prev_state = self.table_33[tuple_888_889]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_33[tuple_888_889] = 1 | 4
                        if not present_bit:
                            self.index_886[tuple_888_889[0]].append(tuple_888_889[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_890_(self, var_891: int, var_892: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_894: List[int] = list()
        vec_index894: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_894.append(var_891)
        # Program VectorUnique Region
        vec_894 = list(set(vec_894))
        vec_index894 = 0
        # Program TableJoin Region
        while vec_index894 < len(vec_894):
            var_896 = vec_894[vec_index894]
            vec_index894 += 1
            tuple_895_0_index: int = 0
            tuple_895_0_vec: List[int] = self.index_436[var_896]
            while tuple_895_0_index < len(tuple_895_0_vec):
                tuple_895_0 = tuple_895_0_vec[tuple_895_0_index]
                tuple_895_0_index += 1
                var_897 = tuple_895_0
                if var_896 in self.index_289:
                    # Program TupleCompare Region
                    if var_892 == var_897:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_438_(var_897, var_896)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_292_(var_896)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_894[:]
        vec_index894 = 0
        # Program Return Region
        return False
        return False

    def proc_900_(self, var_901: int, var_902: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_17[(var_901, var_902)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_901_902 = (var_901, var_902)
            prev_state = self.table_17[tuple_901_902]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_17[tuple_901_902] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_904_(var_901, var_902)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_901_902 = (var_901, var_902)
                    prev_state = self.table_17[tuple_901_902]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_901_902] = 1 | 4
                        if not present_bit:
                            self.index_557[tuple_901_902[1]].append(tuple_901_902[0])
                            self.index_882[tuple_901_902[0]].append(tuple_901_902[1])
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_908_(var_901, var_902)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_901_902 = (var_901, var_902)
                    prev_state = self.table_17[tuple_901_902]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_17[tuple_901_902] = 1 | 4
                        if not present_bit:
                            self.index_557[tuple_901_902[1]].append(tuple_901_902[0])
                            self.index_882[tuple_901_902[0]].append(tuple_901_902[1])
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_904_(self, var_905: int, var_906: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_926_(var_906)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_908_(self, var_909: int, var_910: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_912_(var_909, var_910)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_912_(self, var_913: int, var_914: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_916: List[int] = list()
        vec_index916: int = 0
        vec_918: List[int] = list()
        vec_index918: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_918: int
        scan_index_918: int = 0
        scan_tuple_918_vec: List[int] = self.index_917[var_914]
        while scan_index_918 < len(scan_tuple_918_vec):
            scan_tuple_918 = scan_tuple_918_vec[scan_index_918]
            scan_index_918 += 1
            vec_918.append(scan_tuple_918)
        # Program VectorLoop Region
        vec_index918 = 0
        while vec_index918 < len(vec_918):
            var_919 = vec_918[vec_index918]
            vec_index918 += 1
            # Program VectorAppend Region
            vec_916.append(var_919)
        # Program VectorUnique Region
        vec_916 = list(set(vec_916))
        vec_index916 = 0
        # Program TableJoin Region
        while vec_index916 < len(vec_916):
            var_921 = vec_916[vec_index916]
            vec_index916 += 1
            tuple_920_0_index: int = 0
            tuple_920_0_vec: List[int] = self.index_557[var_921]
            while tuple_920_0_index < len(tuple_920_0_vec):
                tuple_920_0 = tuple_920_0_vec[tuple_920_0_index]
                tuple_920_0_index += 1
                var_922 = tuple_920_0
                tuple_920_1_index: int = 0
                tuple_920_1_vec: List[int] = self.index_558[var_921]
                while tuple_920_1_index < len(tuple_920_1_vec):
                    tuple_920_1 = tuple_920_1_vec[tuple_920_1_index]
                    tuple_920_1_index += 1
                    var_923 = tuple_920_1
                    # Program TupleCompare Region
                    if (var_913, var_914, ) == (var_922, var_923, ):
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_561_(var_922, var_921)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_526_(var_921, var_923)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_916[:]
        vec_index916 = 0
        # Program Return Region
        return False
        return False

    def proc_926_(self, var_927: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_927] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_927 = var_927
            prev_state = self.table_15[tuple_927]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_927] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_929_(var_927)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_927 = var_927
                    prev_state = self.table_15[tuple_927]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_927] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_932_(var_927)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_927 = var_927
                    prev_state = self.table_15[tuple_927]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_927] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_929_(self, var_930: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1039: List[int] = list()
        vec_index1039: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_1039.append(var_930)
        # Program VectorUnique Region
        vec_1039 = list(set(vec_1039))
        vec_index1039 = 0
        # Program TableJoin Region
        while vec_index1039 < len(vec_1039):
            var_1041 = vec_1039[vec_index1039]
            vec_index1039 += 1
            if var_1041 in self.index_261:
                if var_1041 in self.index_248:
                    # Program Return Region
                    return True
        # Program VectorClear Region
        del vec_1039[:]
        vec_index1039 = 0
        # Program Return Region
        return False
        return False

    def proc_932_(self, var_933: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_944_(var_933)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_944_(self, var_945: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Parallel Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Union.cpp: BuildTopDownUnionChecker::call_preds
        ret = self.proc_947_(var_945)
        if ret:
            # Program Return Region
            return True
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Union.cpp: BuildTopDownUnionChecker::call_preds
        ret = self.proc_950_(var_945)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_947_(self, var_948: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_965_(self.var_0, var_948)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_950_(self, var_951: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_953_(var_951)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_953_(self, var_954: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_956: List[int] = list()
        vec_index956: int = 0
        vec_958: List[int] = list()
        vec_index958: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_958: int
        scan_index_958: int = 0
        scan_tuple_958_vec: List[int] = self.index_957[var_954]
        while scan_index_958 < len(scan_tuple_958_vec):
            scan_tuple_958 = scan_tuple_958_vec[scan_index_958]
            scan_index_958 += 1
            vec_958.append(scan_tuple_958)
        # Program VectorLoop Region
        vec_index958 = 0
        while vec_index958 < len(vec_958):
            var_959 = vec_958[vec_index958]
            vec_index958 += 1
            # Program VectorAppend Region
            vec_956.append(var_959)
        # Program VectorUnique Region
        vec_956 = list(set(vec_956))
        vec_index956 = 0
        # Program TableJoin Region
        while vec_index956 < len(vec_956):
            var_961 = vec_956[vec_index956]
            vec_index956 += 1
            if var_961 in self.index_289:
                tuple_960_1_index: int = 0
                tuple_960_1_vec: List[int] = self.index_290[var_961]
                while tuple_960_1_index < len(tuple_960_1_vec):
                    tuple_960_1 = tuple_960_1_vec[tuple_960_1_index]
                    tuple_960_1_index += 1
                    var_962 = tuple_960_1
                    # Program TupleCompare Region
                    if var_954 == var_962:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_292_(var_961)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_295_(var_962, var_961)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_956[:]
        vec_index956 = 0
        # Program Return Region
        return False
        return False

    def proc_965_(self, var_966: ControlFlowEdgeKind, var_967: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_970: List[int] = list()
        vec_index970: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_970: int
        scan_index_970: int = 0
        scan_tuple_970_vec: List[int] = self.index_969[var_967, self.var_0]
        while scan_index_970 < len(scan_tuple_970_vec):
            scan_tuple_970 = scan_tuple_970_vec[scan_index_970]
            scan_index_970 += 1
            vec_970.append(scan_tuple_970)
        # Program VectorLoop Region
        vec_index970 = 0
        while vec_index970 < len(vec_970):
            var_971 = vec_970[vec_index970]
            vec_index970 += 1
            # Program Call Region
            ret = self.proc_972_(var_967, self.var_0)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_972_(self, var_973: int, var_974: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_976: List[int] = list()
        vec_index976: int = 0
        # Program Series Region
        # Program TableScan Region
        var_974 = self._resolve_edgetype(var_974)
        scan_tuple_976: int
        scan_index_976: int = 0
        scan_tuple_976_vec: List[int] = self.index_969[var_973, var_974]
        while scan_index_976 < len(scan_tuple_976_vec):
            scan_tuple_976 = scan_tuple_976_vec[scan_index_976]
            scan_index_976 += 1
            vec_976.append(scan_tuple_976)
        # Program VectorLoop Region
        vec_index976 = 0
        while vec_index976 < len(vec_976):
            var_977 = vec_976[vec_index976]
            vec_index976 += 1
            # Program CheckState Region
            state = self.table_20[(var_977, var_973, var_974)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_974 = self._resolve_edgetype(var_974)
                tuple_977_973_974 = (var_977, var_973, var_974)
                prev_state = self.table_20[tuple_977_973_974]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_977_973_974] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_978_(var_977, var_973, var_974)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_974 = self._resolve_edgetype(var_974)
                        tuple_977_973_974 = (var_977, var_973, var_974)
                        prev_state = self.table_20[tuple_977_973_974]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_977_973_974] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_977_973_974[1], tuple_977_973_974[2])].append(tuple_977_973_974[0])
                                self.index_1062[(tuple_977_973_974[0], tuple_977_973_974[1])].append(tuple_977_973_974[2])
                                self.index_1488[tuple_977_973_974[1]].append((tuple_977_973_974[0], tuple_977_973_974[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_988_(var_977, var_973, var_974)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_974 = self._resolve_edgetype(var_974)
                        tuple_977_973_974 = (var_977, var_973, var_974)
                        prev_state = self.table_20[tuple_977_973_974]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_977_973_974] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_977_973_974[1], tuple_977_973_974[2])].append(tuple_977_973_974[0])
                                self.index_1062[(tuple_977_973_974[0], tuple_977_973_974[1])].append(tuple_977_973_974[2])
                                self.index_1488[tuple_977_973_974[1]].append((tuple_977_973_974[0], tuple_977_973_974[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_993_(var_977, var_973, var_974)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_974 = self._resolve_edgetype(var_974)
                        tuple_977_973_974 = (var_977, var_973, var_974)
                        prev_state = self.table_20[tuple_977_973_974]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_977_973_974] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_977_973_974[1], tuple_977_973_974[2])].append(tuple_977_973_974[0])
                                self.index_1062[(tuple_977_973_974[0], tuple_977_973_974[1])].append(tuple_977_973_974[2])
                                self.index_1488[tuple_977_973_974[1]].append((tuple_977_973_974[0], tuple_977_973_974[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_978_(self, var_979: int, var_980: int, var_981: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1025_(var_980, var_979)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_988_(self, var_989: int, var_990: int, var_991: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1016_(var_990, var_989)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_993_(self, var_994: int, var_995: int, var_996: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_998_(var_995, var_994)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_998_(self, var_999: int, var_1000: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_41[(var_999, var_1000)] & 3
        if state == 1:
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_292_(var_999)
            if not ret:
                # Program Return Region
                return True
            # Program TransitionState Region
            tuple_999_1000 = (var_999, var_1000)
            prev_state = self.table_41[tuple_999_1000]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 1:
                self.table_41[tuple_999_1000] = 0 | 4
        elif state == 2:
            # Program TransitionState Region
            tuple_999_1000 = (var_999, var_1000)
            prev_state = self.table_41[tuple_999_1000]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_41[tuple_999_1000] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_292_(var_999)
                if not ret:
                    # Program Call Region
                    ret = self.proc_1006_(self.var_2, var_1000, var_999)
                    if ret:
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1006_(self, var_1007: ControlFlowEdgeKind, var_1008: int, var_1009: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        ret = self.proc_1011_(var_1008, var_1009, self.var_2)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1011_(self, var_1012: int, var_1013: int, var_1014: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_11[(var_1012, var_1013, var_1014)] & 3
        if state == 1:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1016_(self, var_1017: int, var_1018: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1020: List[int] = list()
        vec_index1020: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_1020.append(var_1017)
        # Program VectorUnique Region
        vec_1020 = list(set(vec_1020))
        vec_index1020 = 0
        # Program TableJoin Region
        while vec_index1020 < len(vec_1020):
            var_1022 = vec_1020[vec_index1020]
            vec_index1020 += 1
            tuple_1021_0_index: int = 0
            tuple_1021_0_vec: List[int] = self.index_421[var_1022]
            while tuple_1021_0_index < len(tuple_1021_0_vec):
                tuple_1021_0 = tuple_1021_0_vec[tuple_1021_0_index]
                tuple_1021_0_index += 1
                var_1023 = tuple_1021_0
                if var_1022 in self.index_289:
                    # Program TupleCompare Region
                    if var_1018 == var_1023:
                        # Program Series Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_292_(var_1022)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1020[:]
        vec_index1020 = 0
        # Program Return Region
        return False
        return False

    def proc_1025_(self, var_1026: int, var_1027: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_38[(var_1026, var_1027)] & 3
        if state == 1:
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_472_(var_1026)
            if not ret:
                # Program Return Region
                return True
            # Program TransitionState Region
            tuple_1026_1027 = (var_1026, var_1027)
            prev_state = self.table_38[tuple_1026_1027]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 1:
                self.table_38[tuple_1026_1027] = 0 | 4
        elif state == 2:
            # Program TransitionState Region
            tuple_1026_1027 = (var_1026, var_1027)
            prev_state = self.table_38[tuple_1026_1027]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_38[tuple_1026_1027] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_472_(var_1026)
                if not ret:
                    # Program Call Region
                    ret = self.proc_1033_(self.var_9, var_1027, var_1026)
                    if ret:
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1033_(self, var_1034: ControlFlowEdgeKind, var_1035: int, var_1036: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        ret = self.proc_1011_(var_1035, var_1036, self.var_9)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1042_(self, var_1043: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_15[var_1043] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            tuple_1043 = var_1043
            prev_state = self.table_15[tuple_1043]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_15[tuple_1043] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_929_(var_1043)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_1043 = var_1043
                    prev_state = self.table_15[tuple_1043]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_1043] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_932_(var_1043)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    tuple_1043 = var_1043
                    prev_state = self.table_15[tuple_1043]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_15[tuple_1043] = 1 | 4
                        if not present_bit:
                            pass
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_1050_(self, var_1051: int, var_1052: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_44[(var_1051, var_1052)] & 3
        if state == 1:
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_292_(var_1051)
            if not ret:
                # Program Return Region
                return True
            # Program TransitionState Region
            tuple_1051_1052 = (var_1051, var_1052)
            prev_state = self.table_44[tuple_1051_1052]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 1:
                self.table_44[tuple_1051_1052] = 0 | 4
        elif state == 2:
            # Program TransitionState Region
            tuple_1051_1052 = (var_1051, var_1052)
            prev_state = self.table_44[tuple_1051_1052]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_44[tuple_1051_1052] = 0 | 4
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
                ret = self.proc_292_(var_1051)
                if not ret:
                    # Program Call Region
                    ret = self.proc_1058_(var_1052, var_1051)
                    if ret:
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1058_(self, var_1059: int, var_1060: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1063: List[ControlFlowEdgeKind] = list()
        vec_index1063: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1063: ControlFlowEdgeKind
        scan_index_1063: int = 0
        scan_tuple_1063_vec: List[ControlFlowEdgeKind] = self.index_1062[var_1059, var_1060]
        while scan_index_1063 < len(scan_tuple_1063_vec):
            scan_tuple_1063 = scan_tuple_1063_vec[scan_index_1063]
            scan_index_1063 += 1
            vec_1063.append(scan_tuple_1063)
        # Program VectorLoop Region
        vec_index1063 = 0
        while vec_index1063 < len(vec_1063):
            var_1064 = vec_1063[vec_index1063]
            vec_index1063 += 1
            # Program CheckState Region
            state = self.table_20[(var_1059, var_1060, var_1064)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_1064 = self._resolve_edgetype(var_1064)
                tuple_1059_1060_1064 = (var_1059, var_1060, var_1064)
                prev_state = self.table_20[tuple_1059_1060_1064]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_1059_1060_1064] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_978_(var_1059, var_1060, var_1064)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1064 = self._resolve_edgetype(var_1064)
                        tuple_1059_1060_1064 = (var_1059, var_1060, var_1064)
                        prev_state = self.table_20[tuple_1059_1060_1064]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1059_1060_1064] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1059_1060_1064[1], tuple_1059_1060_1064[2])].append(tuple_1059_1060_1064[0])
                                self.index_1062[(tuple_1059_1060_1064[0], tuple_1059_1060_1064[1])].append(tuple_1059_1060_1064[2])
                                self.index_1488[tuple_1059_1060_1064[1]].append((tuple_1059_1060_1064[0], tuple_1059_1060_1064[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_988_(var_1059, var_1060, var_1064)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1064 = self._resolve_edgetype(var_1064)
                        tuple_1059_1060_1064 = (var_1059, var_1060, var_1064)
                        prev_state = self.table_20[tuple_1059_1060_1064]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1059_1060_1064] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1059_1060_1064[1], tuple_1059_1060_1064[2])].append(tuple_1059_1060_1064[0])
                                self.index_1062[(tuple_1059_1060_1064[0], tuple_1059_1060_1064[1])].append(tuple_1059_1060_1064[2])
                                self.index_1488[tuple_1059_1060_1064[1]].append((tuple_1059_1060_1064[0], tuple_1059_1060_1064[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_993_(var_1059, var_1060, var_1064)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1064 = self._resolve_edgetype(var_1064)
                        tuple_1059_1060_1064 = (var_1059, var_1060, var_1064)
                        prev_state = self.table_20[tuple_1059_1060_1064]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1059_1060_1064] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1059_1060_1064[1], tuple_1059_1060_1064[2])].append(tuple_1059_1060_1064[0])
                                self.index_1062[(tuple_1059_1060_1064[0], tuple_1059_1060_1064[1])].append(tuple_1059_1060_1064[2])
                                self.index_1488[tuple_1059_1060_1064[1]].append((tuple_1059_1060_1064[0], tuple_1059_1060_1064[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1069_(self, var_1070: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1072: List[int] = list()
        vec_index1072: int = 0
        vec_1074: List[int] = list()
        vec_index1074: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1074: int
        scan_index_1074: int = 0
        scan_tuple_1074_vec: List[int] = self.index_1073[var_1070]
        while scan_index_1074 < len(scan_tuple_1074_vec):
            scan_tuple_1074 = scan_tuple_1074_vec[scan_index_1074]
            scan_index_1074 += 1
            vec_1074.append(scan_tuple_1074)
        # Program VectorLoop Region
        vec_index1074 = 0
        while vec_index1074 < len(vec_1074):
            var_1075 = vec_1074[vec_index1074]
            vec_index1074 += 1
            # Program VectorAppend Region
            vec_1072.append(var_1075)
        # Program VectorUnique Region
        vec_1072 = list(set(vec_1072))
        vec_index1072 = 0
        # Program TableJoin Region
        while vec_index1072 < len(vec_1072):
            var_1077 = vec_1072[vec_index1072]
            vec_index1072 += 1
            tuple_1076_0_index: int = 0
            tuple_1076_0_vec: List[int] = self.index_450[var_1077]
            while tuple_1076_0_index < len(tuple_1076_0_vec):
                tuple_1076_0 = tuple_1076_0_vec[tuple_1076_0_index]
                tuple_1076_0_index += 1
                var_1078 = tuple_1076_0
                if var_1077 in self.index_451:
                    # Program TupleCompare Region
                    if var_1070 == var_1078:
                        # Program Series Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_443_(var_1078, var_1077)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1072[:]
        vec_index1072 = 0
        # Program Return Region
        return False
        return False

    def proc_1081_(self, var_1082: int, var_1083: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1082_1083 = (var_1082, var_1083)
        prev_state = self.table_17[tuple_1082_1083]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_17[tuple_1082_1083] = 0 | 4
            # Program Parallel Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_904_(var_1082, var_1083)
            if ret:
                # Program Return Region
                return True
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_908_(var_1082, var_1083)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1099_(self, var_1100: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1102: List[int] = list()
        vec_index1102: int = 0
        vec_1104: List[int] = list()
        vec_index1104: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1104: int
        scan_index_1104: int = 0
        scan_tuple_1104_vec: List[int] = self.index_1103[var_1100]
        while scan_index_1104 < len(scan_tuple_1104_vec):
            scan_tuple_1104 = scan_tuple_1104_vec[scan_index_1104]
            scan_index_1104 += 1
            vec_1104.append(scan_tuple_1104)
        # Program VectorLoop Region
        vec_index1104 = 0
        while vec_index1104 < len(vec_1104):
            var_1105 = vec_1104[vec_index1104]
            vec_index1104 += 1
            # Program VectorAppend Region
            vec_1102.append(var_1105)
        # Program VectorUnique Region
        vec_1102 = list(set(vec_1102))
        vec_index1102 = 0
        # Program TableJoin Region
        while vec_index1102 < len(vec_1102):
            var_1107 = vec_1102[vec_index1102]
            vec_index1102 += 1
            tuple_1106_0_index: int = 0
            tuple_1106_0_vec: List[int] = self.index_401[var_1107]
            while tuple_1106_0_index < len(tuple_1106_0_vec):
                tuple_1106_0 = tuple_1106_0_vec[tuple_1106_0_index]
                tuple_1106_0_index += 1
                var_1108 = tuple_1106_0
                if var_1107 in self.index_469:
                    # Program TupleCompare Region
                    if var_1100 == var_1108:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_403_(var_1108, var_1107)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_472_(var_1107)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1102[:]
        vec_index1102 = 0
        # Program Return Region
        return False
        return False

    def proc_1111_(self, var_1112: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1112 = var_1112
        prev_state = self.table_24[tuple_1112]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 2:
            self.table_24[tuple_1112] = 0 | 4
            # Program Parallel Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_1114_(var_1112)
            if ret:
                # Program Return Region
                return True
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_1117_(var_1112)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1114_(self, var_1115: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1121_(var_1115)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1117_(self, var_1118: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1099_(var_1118)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1121_(self, var_1122: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1124: List[int] = list()
        vec_index1124: int = 0
        vec_1125: List[int] = list()
        vec_index1125: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1125: int
        scan_index_1125: int = 0
        scan_tuple_1125_vec: List[int] = self.index_1103[var_1122]
        while scan_index_1125 < len(scan_tuple_1125_vec):
            scan_tuple_1125 = scan_tuple_1125_vec[scan_index_1125]
            scan_index_1125 += 1
            vec_1125.append(scan_tuple_1125)
        # Program VectorLoop Region
        vec_index1125 = 0
        while vec_index1125 < len(vec_1125):
            var_1126 = vec_1125[vec_index1125]
            vec_index1125 += 1
            # Program VectorAppend Region
            vec_1124.append(var_1126)
        # Program VectorUnique Region
        vec_1124 = list(set(vec_1124))
        vec_index1124 = 0
        # Program TableJoin Region
        while vec_index1124 < len(vec_1124):
            var_1128 = vec_1124[vec_index1124]
            vec_index1124 += 1
            tuple_1127_0_index: int = 0
            tuple_1127_0_vec: List[int] = self.index_401[var_1128]
            while tuple_1127_0_index < len(tuple_1127_0_vec):
                tuple_1127_0 = tuple_1127_0_vec[tuple_1127_0_index]
                tuple_1127_0_index += 1
                var_1129 = tuple_1127_0
                if var_1128 in self.index_289:
                    # Program TupleCompare Region
                    if var_1122 == var_1129:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_403_(var_1129, var_1128)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_292_(var_1128)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1124[:]
        vec_index1124 = 0
        # Program Return Region
        return False
        return False

    def proc_1132_(self, var_1133: int, var_1134: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1136: List[int] = list()
        vec_index1136: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_1136.append(var_1133)
        # Program VectorUnique Region
        vec_1136 = list(set(vec_1136))
        vec_index1136 = 0
        # Program TableJoin Region
        while vec_index1136 < len(vec_1136):
            var_1138 = vec_1136[vec_index1136]
            vec_index1136 += 1
            tuple_1137_0_index: int = 0
            tuple_1137_0_vec: List[int] = self.index_436[var_1138]
            while tuple_1137_0_index < len(tuple_1137_0_vec):
                tuple_1137_0 = tuple_1137_0_vec[tuple_1137_0_index]
                tuple_1137_0_index += 1
                var_1139 = tuple_1137_0
                if var_1138 in self.index_289:
                    # Program TupleCompare Region
                    if var_1134 == var_1139:
                        # Program Series Region
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_438_(var_1139, var_1138)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_292_(var_1138)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1136[:]
        vec_index1136 = 0
        # Program Return Region
        return False
        return False

    def proc_1142_(self, var_1143: int, var_1144: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1146: List[ControlFlowEdgeKind] = list()
        vec_index1146: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1146: ControlFlowEdgeKind
        scan_index_1146: int = 0
        scan_tuple_1146_vec: List[ControlFlowEdgeKind] = self.index_1062[var_1143, var_1144]
        while scan_index_1146 < len(scan_tuple_1146_vec):
            scan_tuple_1146 = scan_tuple_1146_vec[scan_index_1146]
            scan_index_1146 += 1
            vec_1146.append(scan_tuple_1146)
        # Program VectorLoop Region
        vec_index1146 = 0
        while vec_index1146 < len(vec_1146):
            var_1147 = vec_1146[vec_index1146]
            vec_index1146 += 1
            # Program CheckState Region
            state = self.table_20[(var_1143, var_1144, var_1147)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_1147 = self._resolve_edgetype(var_1147)
                tuple_1143_1144_1147 = (var_1143, var_1144, var_1147)
                prev_state = self.table_20[tuple_1143_1144_1147]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_1143_1144_1147] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_978_(var_1143, var_1144, var_1147)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1147 = self._resolve_edgetype(var_1147)
                        tuple_1143_1144_1147 = (var_1143, var_1144, var_1147)
                        prev_state = self.table_20[tuple_1143_1144_1147]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1143_1144_1147] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1143_1144_1147[1], tuple_1143_1144_1147[2])].append(tuple_1143_1144_1147[0])
                                self.index_1062[(tuple_1143_1144_1147[0], tuple_1143_1144_1147[1])].append(tuple_1143_1144_1147[2])
                                self.index_1488[tuple_1143_1144_1147[1]].append((tuple_1143_1144_1147[0], tuple_1143_1144_1147[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_988_(var_1143, var_1144, var_1147)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1147 = self._resolve_edgetype(var_1147)
                        tuple_1143_1144_1147 = (var_1143, var_1144, var_1147)
                        prev_state = self.table_20[tuple_1143_1144_1147]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1143_1144_1147] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1143_1144_1147[1], tuple_1143_1144_1147[2])].append(tuple_1143_1144_1147[0])
                                self.index_1062[(tuple_1143_1144_1147[0], tuple_1143_1144_1147[1])].append(tuple_1143_1144_1147[2])
                                self.index_1488[tuple_1143_1144_1147[1]].append((tuple_1143_1144_1147[0], tuple_1143_1144_1147[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_993_(var_1143, var_1144, var_1147)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1147 = self._resolve_edgetype(var_1147)
                        tuple_1143_1144_1147 = (var_1143, var_1144, var_1147)
                        prev_state = self.table_20[tuple_1143_1144_1147]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1143_1144_1147] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1143_1144_1147[1], tuple_1143_1144_1147[2])].append(tuple_1143_1144_1147[0])
                                self.index_1062[(tuple_1143_1144_1147[0], tuple_1143_1144_1147[1])].append(tuple_1143_1144_1147[2])
                                self.index_1488[tuple_1143_1144_1147[1]].append((tuple_1143_1144_1147[0], tuple_1143_1144_1147[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1154_(self, var_1155: ControlFlowEdgeKind, var_1156: int, var_1157: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        ret = self.proc_1159_(var_1156, var_1157, self.var_8)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1159_(self, var_1160: int, var_1161: int, var_1162: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program CheckState Region
        state = self.table_20[(var_1160, var_1161, var_1162)] & 3
        if state == 1:
            # Program Return Region
            return True
        elif state == 2:
            # Program TransitionState Region
            var_1162 = self._resolve_edgetype(var_1162)
            tuple_1160_1161_1162 = (var_1160, var_1161, var_1162)
            prev_state = self.table_20[tuple_1160_1161_1162]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 2:
                self.table_20[tuple_1160_1161_1162] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_978_(var_1160, var_1161, var_1162)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    var_1162 = self._resolve_edgetype(var_1162)
                    tuple_1160_1161_1162 = (var_1160, var_1161, var_1162)
                    prev_state = self.table_20[tuple_1160_1161_1162]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_1160_1161_1162] = 1 | 4
                        if not present_bit:
                            self.index_969[(tuple_1160_1161_1162[1], tuple_1160_1161_1162[2])].append(tuple_1160_1161_1162[0])
                            self.index_1062[(tuple_1160_1161_1162[0], tuple_1160_1161_1162[1])].append(tuple_1160_1161_1162[2])
                            self.index_1488[tuple_1160_1161_1162[1]].append((tuple_1160_1161_1162[0], tuple_1160_1161_1162[2]))
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_988_(var_1160, var_1161, var_1162)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    var_1162 = self._resolve_edgetype(var_1162)
                    tuple_1160_1161_1162 = (var_1160, var_1161, var_1162)
                    prev_state = self.table_20[tuple_1160_1161_1162]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_1160_1161_1162] = 1 | 4
                        if not present_bit:
                            self.index_969[(tuple_1160_1161_1162[1], tuple_1160_1161_1162[2])].append(tuple_1160_1161_1162[0])
                            self.index_1062[(tuple_1160_1161_1162[0], tuple_1160_1161_1162[1])].append(tuple_1160_1161_1162[2])
                            self.index_1488[tuple_1160_1161_1162[1]].append((tuple_1160_1161_1162[0], tuple_1160_1161_1162[2]))
                    # Program Return Region
                    return True
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                ret = self.proc_993_(var_1160, var_1161, var_1162)
                if ret:
                    # Program Series Region
                    # Program TransitionState Region
                    var_1162 = self._resolve_edgetype(var_1162)
                    tuple_1160_1161_1162 = (var_1160, var_1161, var_1162)
                    prev_state = self.table_20[tuple_1160_1161_1162]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_20[tuple_1160_1161_1162] = 1 | 4
                        if not present_bit:
                            self.index_969[(tuple_1160_1161_1162[1], tuple_1160_1161_1162[2])].append(tuple_1160_1161_1162[0])
                            self.index_1062[(tuple_1160_1161_1162[0], tuple_1160_1161_1162[1])].append(tuple_1160_1161_1162[2])
                            self.index_1488[tuple_1160_1161_1162[1]].append((tuple_1160_1161_1162[0], tuple_1160_1161_1162[2]))
                    # Program Return Region
                    return True
        # Program Return Region
        return False
        return False

    def proc_1170_(self, var_1171: int, var_1172: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1174: List[int] = list()
        vec_index1174: int = 0
        # Program Series Region
        # Program VectorAppend Region
        vec_1174.append(var_1171)
        # Program VectorUnique Region
        vec_1174 = list(set(vec_1174))
        vec_index1174 = 0
        # Program TableJoin Region
        while vec_index1174 < len(vec_1174):
            var_1176 = vec_1174[vec_index1174]
            vec_index1174 += 1
            if var_1176 in self.index_230:
                tuple_1175_1_index: int = 0
                tuple_1175_1_vec: List[int] = self.index_235[var_1176]
                while tuple_1175_1_index < len(tuple_1175_1_vec):
                    tuple_1175_1 = tuple_1175_1_vec[tuple_1175_1_index]
                    tuple_1175_1_index += 1
                    var_1177 = tuple_1175_1
                    # Program TupleCompare Region
                    if var_1172 == var_1177:
                        # Program Series Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: BuildTopDownJoinChecker
                        ret = self.proc_240_(var_1176, var_1177)
                        if not ret:
                            # Program Return Region
                            return False
                        # Program Return Region
                        return True
        # Program VectorClear Region
        del vec_1174[:]
        vec_index1174 = 0
        # Program Return Region
        return False
        return False

    def proc_1182_(self, var_1183: ControlFlowEdgeKind, var_1184: int, var_1185: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        ret = self.proc_1159_(var_1184, var_1185, self.var_2)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1188_(self, var_1189: int) -> bool:
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
        if state == 2:
            self.table_15[tuple_1189] = 0 | 4
            # Program Parallel Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_929_(var_1189)
            if ret:
                # Program Return Region
                return True
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
            ret = self.proc_932_(var_1189)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1202_(self, var_1203: int, var_1204: int, var_1205: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1204_1203 = (var_1204, var_1203)
        prev_state = self.table_44[tuple_1204_1203]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_44[tuple_1204_1203] = 2 | 4
            # Program Series Region
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CheckInNegatedView
            ret = self.proc_292_(var_1204)
            if ret:
                # Program Series Region
                # Program TransitionState Region
                tuple_1204_1203 = (var_1204, var_1203)
                prev_state = self.table_44[tuple_1204_1203]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_44[tuple_1204_1203] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    ret = self.proc_366_(var_1204, var_1203)

                    # Program Call Region
                    ret = self.proc_370_(var_1204, var_1203)

                # Program Return Region
                return False
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Negate.cpp: CreateBottomUpNegationRemover
            ret = self.proc_1449_(var_1204, var_1203)
            if ret:
                # Program Series Region
                # Program TransitionState Region
                tuple_1204_1203 = (var_1204, var_1203)
                prev_state = self.table_44[tuple_1204_1203]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 0 or state == 2:
                    self.table_44[tuple_1204_1203] = 1 | 4
                    if not present_bit:
                        self.index_363[tuple_1204_1203[0]].append(tuple_1204_1203[1])
                # Program Return Region
                return False
            # Program TransitionState Region
            tuple_1204_1203 = (var_1204, var_1203)
            prev_state = self.table_44[tuple_1204_1203]
            state = prev_state & 3
            present_bit = prev_state & 4
            if state == 0 or state == 2:
                self.table_44[tuple_1204_1203] = 0 | 4
                # Program Parallel Region
                # Program Call Region
                ret = self.proc_366_(var_1204, var_1203)

                # Program Call Region
                ret = self.proc_370_(var_1204, var_1203)

        # Program Return Region
        return False
        return False

    def proc_1207_(self, var_1208: int, var_1209: int, var_1210: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1208_1209 = (var_1208, var_1209)
        prev_state = self.table_151[tuple_1208_1209]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_151[tuple_1208_1209] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1391_(var_1209, var_1208)

            # Program Call Region
            ret = self.proc_1395_(var_1209, var_1208)

        # Program Return Region
        return False
        return False

    def proc_1212_(self, var_1213: int, var_1214: int, var_1215: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TupleCompare Region
        if self.var_0 == var_1215:
            # Program Call Region
            ret = self.proc_1432_(self.var_0, var_1214)

        # Program Return Region
        return False
        return False

    def proc_1217_(self, var_1218: int, var_1219: int, var_1220: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TupleCompare Region
        if self.var_2 == var_1220:
            # Program Call Region
            ret = self.proc_1278_(self.var_2, var_1218, var_1219)

        # Program Return Region
        return False
        return False

    def proc_1222_(self, var_1223: int, var_1224: int, var_1225: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TupleCompare Region
        if self.var_8 == var_1225:
            # Program Call Region
            ret = self.proc_1228_(self.var_8, var_1223, var_1224)

        # Program Return Region
        return False
        return False

    def proc_1228_(self, var_1229: ControlFlowEdgeKind, var_1230: int, var_1231: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1230_1231 = (var_1230, var_1231)
        prev_state = self.table_145[tuple_1230_1231]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_145[tuple_1230_1231] = 2 | 4
            # Program Call Region
            ret = self.proc_1240_(var_1231, var_1230)

        # Program Return Region
        return False
        return False

    def proc_1240_(self, var_1241: int, var_1242: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1242 = var_1242
        prev_state = self.table_24[tuple_1242]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_24[tuple_1242] = 2 | 4
            # Program Call Region
            ret = self.proc_1247_(var_1242)

        # Program Return Region
        return False
        return False

    def proc_1247_(self, var_1248: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1253: List[int] = list()
        vec_index1253: int = 0
        vec_1259: List[int] = list()
        vec_index1259: int = 0
        vec_1260: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index1260: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: CreateBottomUpTupleRemover
        ret = self.proc_1250_(var_1248)
        if not ret:
            # Program Parallel Region
            # Program Series Region
            # Program TableScan Region
            scan_tuple_1253: int
            scan_index_1253: int = 0
            scan_tuple_1253_vec: List[int] = self.index_459[var_1248]
            while scan_index_1253 < len(scan_tuple_1253_vec):
                scan_tuple_1253 = scan_tuple_1253_vec[scan_index_1253]
                scan_index_1253 += 1
                vec_1253.append(scan_tuple_1253)
            # Program VectorLoop Region
            vec_index1253 = 0
            while vec_index1253 < len(vec_1253):
                var_1254 = vec_1253[vec_index1253]
                vec_index1253 += 1
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: ReAddToNegatedView
                ret = self.proc_1255_(var_1248)
                if ret:
                    # Program TransitionState Region
                    # Re-adding to negated view
                    tuple_1248_1254 = (var_1248, var_1254)
                    prev_state = self.table_38[tuple_1248_1254]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_38[tuple_1248_1254] = 1 | 4
                        if not present_bit:
                            self.index_459[tuple_1248_1254[0]].append(tuple_1248_1254[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_494_(var_1254, var_1248, self.var_9)
                        if not ret:
                            # Program TransitionState Region
                            tuple_1254_1248_9 = (var_1254, var_1248, self.var_9)
                            prev_state = self.table_20[tuple_1254_1248_9]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_20[tuple_1254_1248_9] = 1 | 4
                                if not present_bit:
                                    self.index_969[(tuple_1254_1248_9[1], tuple_1254_1248_9[2])].append(tuple_1254_1248_9[0])
                                    self.index_1062[(tuple_1254_1248_9[0], tuple_1254_1248_9[1])].append(tuple_1254_1248_9[2])
                                    self.index_1488[tuple_1254_1248_9[1]].append((tuple_1254_1248_9[0], tuple_1254_1248_9[2]))
                                # Program VectorAppend Region
                                vec_1260.append((var_1254, var_1248, self.var_9))
            # Program Call Region
            ret = self.proc_1263_(var_1248)

        # Induction Fixpoint Loop Region
        while len(vec_1259) or len(vec_1260):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_1259, vec_1260)

            # Program Call Region
            param_1262_0 = [vec_1259]
            param_1262_1 = [vec_1260]
            ret = self.proc_173_(param_1262_0, param_1262_1)
            vec_1259 = param_1262_0[0]
            vec_1260 = param_1262_1[0]

        vec_index1259 = 0
        vec_index1260 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_1259[:]
        vec_index1259 = 0
        # Program VectorClear Region
        del vec_1260[:]
        vec_index1260 = 0
        # Program Return Region
        return False
        return False

    def proc_1250_(self, var_1251: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1111_(var_1251)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1255_(self, var_1256: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1497: List[int] = list()
        vec_index1497: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1497: int
        scan_index_1497: int = 0
        scan_tuple_1497_vec: List[int] = self.index_1479[var_1256, self.var_9]
        while scan_index_1497 < len(scan_tuple_1497_vec):
            scan_tuple_1497 = scan_tuple_1497_vec[scan_index_1497]
            scan_index_1497 += 1
            vec_1497.append(scan_tuple_1497)
        # Program VectorLoop Region
        vec_index1497 = 0
        while vec_index1497 < len(vec_1497):
            var_1498 = vec_1497[vec_index1497]
            vec_index1497 += 1
            # Program Call Region
            ret = self.proc_1482_(var_1256, self.var_9)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1263_(self, var_1264: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1266: List[int] = list()
        vec_index1266: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1266: int
        scan_index_1266: int = 0
        scan_tuple_1266_vec: List[int] = self.index_401[var_1264]
        while scan_index_1266 < len(scan_tuple_1266_vec):
            scan_tuple_1266 = scan_tuple_1266_vec[scan_index_1266]
            scan_index_1266 += 1
            vec_1266.append(scan_tuple_1266)
        # Program VectorLoop Region
        vec_index1266 = 0
        while vec_index1266 < len(vec_1266):
            var_1267 = vec_1266[vec_index1266]
            vec_index1266 += 1
            # Program Call Region
            ret = self.proc_1240_(var_1264, var_1267)

        # Program Return Region
        return False
        return False

    def proc_1278_(self, var_1279: ControlFlowEdgeKind, var_1280: int, var_1281: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1280_1281 = (var_1280, var_1281)
        prev_state = self.table_75[tuple_1280_1281]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_75[tuple_1280_1281] = 2 | 4
            # Program Call Region
            ret = self.proc_1286_(var_1280, var_1281)

        # Program Return Region
        return False
        return False

    def proc_1286_(self, var_1287: int, var_1288: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1287_1288 = (var_1287, var_1288)
        prev_state = self.table_78[tuple_1287_1288]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_78[tuple_1287_1288] = 2 | 4
            # Program Call Region
            ret = self.proc_1294_(var_1288, var_1287)

        # Program Return Region
        return False
        return False

    def proc_1294_(self, var_1295: int, var_1296: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1296 = var_1296
        prev_state = self.table_15[tuple_1296]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_15[tuple_1296] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1307_(var_1296)

            # Program Call Region
            ret = self.proc_1310_(var_1296)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1188_(var_1296)

        # Program Return Region
        return False
        return False

    def proc_1307_(self, var_1308: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1350: List[int] = list()
        vec_index1350: int = 0
        vec_1356: List[int] = list()
        vec_index1356: int = 0
        vec_1362: List[int] = list()
        vec_index1362: int = 0
        vec_1363: List[Tuple[int, int, ControlFlowEdgeKind]] = list()
        vec_index1363: int = 0
        vec_1378: List[int] = list()
        vec_index1378: int = 0
        vec_1386: List[Tuple[int, int]] = list()
        vec_index1386: int = 0
        # Program Series Region
        # Program Induction Init Region
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: CreateBottomUpTupleRemover
        ret = self.proc_1347_(var_1308)
        if not ret:
            # Program Parallel Region
            # Program Series Region
            # Program TableScan Region
            scan_tuple_1350: int
            scan_index_1350: int = 0
            scan_tuple_1350_vec: List[int] = self.index_363[var_1308]
            while scan_index_1350 < len(scan_tuple_1350_vec):
                scan_tuple_1350 = scan_tuple_1350_vec[scan_index_1350]
                scan_index_1350 += 1
                vec_1350.append(scan_tuple_1350)
            # Program VectorLoop Region
            vec_index1350 = 0
            while vec_index1350 < len(vec_1350):
                var_1351 = vec_1350[vec_index1350]
                vec_index1350 += 1
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: ReAddToNegatedView
                ret = self.proc_1352_(var_1308)
                if ret:
                    # Program TransitionState Region
                    # Re-adding to negated view
                    tuple_1308_1351 = (var_1308, var_1351)
                    prev_state = self.table_44[tuple_1308_1351]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_44[tuple_1308_1351] = 1 | 4
                        if not present_bit:
                            self.index_363[tuple_1308_1351[0]].append(tuple_1308_1351[1])
                        # Program Parallel Region
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_526_(var_1351, var_1308)
                        if not ret:
                            # Program TransitionState Region
                            tuple_1351_1308 = (var_1351, var_1308)
                            prev_state = self.table_81[tuple_1351_1308]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_81[tuple_1351_1308] = 1 | 4
                                if not present_bit:
                                    self.index_558[tuple_1351_1308[0]].append(tuple_1351_1308[1])
                                    self.index_917[tuple_1351_1308[1]].append(tuple_1351_1308[0])
                                # Program VectorAppend Region
                                vec_1378.append(var_1351)
                        # Program TransitionState Region
                        tuple_1351_1308 = (var_1351, var_1308)
                        prev_state = self.table_28[tuple_1351_1308]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_28[tuple_1351_1308] = 1 | 4
                            if not present_bit:
                                self.index_876[tuple_1351_1308[0]].append(tuple_1351_1308[1])
            # Program Series Region
            # Program TableScan Region
            scan_tuple_1356: int
            scan_index_1356: int = 0
            scan_tuple_1356_vec: List[int] = self.index_374[var_1308]
            while scan_index_1356 < len(scan_tuple_1356_vec):
                scan_tuple_1356 = scan_tuple_1356_vec[scan_index_1356]
                scan_index_1356 += 1
                vec_1356.append(scan_tuple_1356)
            # Program VectorLoop Region
            vec_index1356 = 0
            while vec_index1356 < len(vec_1356):
                var_1357 = vec_1356[vec_index1356]
                vec_index1356 += 1
                # Program Call Region
                # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: ReAddToNegatedView
                ret = self.proc_1358_(var_1308)
                if ret:
                    # Program TransitionState Region
                    # Re-adding to negated view
                    tuple_1308_1357 = (var_1308, var_1357)
                    prev_state = self.table_41[tuple_1308_1357]
                    state = prev_state & 3
                    present_bit = prev_state & 4
                    if state == 0 or state == 2:
                        self.table_41[tuple_1308_1357] = 1 | 4
                        if not present_bit:
                            self.index_374[tuple_1308_1357[0]].append(tuple_1308_1357[1])
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                        ret = self.proc_483_(var_1357, var_1308, self.var_2)
                        if not ret:
                            # Program TransitionState Region
                            tuple_1357_1308_2 = (var_1357, var_1308, self.var_2)
                            prev_state = self.table_20[tuple_1357_1308_2]
                            state = prev_state & 3
                            present_bit = prev_state & 4
                            if state == 0 or state == 2:
                                self.table_20[tuple_1357_1308_2] = 1 | 4
                                if not present_bit:
                                    self.index_969[(tuple_1357_1308_2[1], tuple_1357_1308_2[2])].append(tuple_1357_1308_2[0])
                                    self.index_1062[(tuple_1357_1308_2[0], tuple_1357_1308_2[1])].append(tuple_1357_1308_2[2])
                                    self.index_1488[tuple_1357_1308_2[1]].append((tuple_1357_1308_2[0], tuple_1357_1308_2[2]))
                                # Program VectorAppend Region
                                vec_1363.append((var_1357, var_1308, self.var_2))
            # Program Call Region
            ret = self.proc_1366_(var_1308)

            # Program Call Region
            ret = self.proc_1263_(var_1308)

            # Program Call Region
            ret = self.proc_1372_(var_1308)

            # Program Call Region
            ret = self.proc_1375_(var_1308)

        # Program VectorUnique Region
        vec_1378 = list(set(vec_1378))
        vec_index1378 = 0
        # Program TableJoin Region
        while vec_index1378 < len(vec_1378):
            var_1380 = vec_1378[vec_index1378]
            vec_index1378 += 1
            tuple_1379_0_index: int = 0
            tuple_1379_0_vec: List[int] = self.index_557[var_1380]
            while tuple_1379_0_index < len(tuple_1379_0_vec):
                tuple_1379_0 = tuple_1379_0_vec[tuple_1379_0_index]
                tuple_1379_0_index += 1
                var_1381 = tuple_1379_0
                tuple_1379_1_index: int = 0
                tuple_1379_1_vec: List[int] = self.index_558[var_1380]
                while tuple_1379_1_index < len(tuple_1379_1_vec):
                    tuple_1379_1 = tuple_1379_1_vec[tuple_1379_1_index]
                    tuple_1379_1_index += 1
                    var_1382 = tuple_1379_1
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                    ret = self.proc_561_(var_1381, var_1380)
                    if ret:
                        # Program Call Region
                        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Join.cpp: ContinueJoinWorkItem::Run
                        ret = self.proc_526_(var_1380, var_1382)
                        if ret:
                            # Program Call Region
                            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Build.h: BuildInsertCheck
                            ret = self.proc_566_(var_1381, var_1382)
                            if not ret:
                                # Program TransitionState Region
                                tuple_1381_1382 = (var_1381, var_1382)
                                prev_state = self.table_17[tuple_1381_1382]
                                state = prev_state & 3
                                present_bit = prev_state & 4
                                if state == 0 or state == 2:
                                    self.table_17[tuple_1381_1382] = 1 | 4
                                    if not present_bit:
                                        self.index_557[tuple_1381_1382[1]].append(tuple_1381_1382[0])
                                        self.index_882[tuple_1381_1382[0]].append(tuple_1381_1382[1])
                                    # Program VectorAppend Region
                                    vec_1386.append((var_1381, var_1382))
        # Program VectorClear Region
        del vec_1378[:]
        vec_index1378 = 0
        # Induction Fixpoint Loop Region
        while len(vec_1386) or len(vec_1362) or len(vec_1363):
            # Program Series Region
            # Program Call Region
            ret = self.proc_176_(vec_1362, vec_1363)

            # Program Call Region
            param_1365_0 = [vec_1362]
            param_1365_1 = [vec_1363]
            ret = self.proc_173_(param_1365_0, param_1365_1)
            vec_1362 = param_1365_0[0]
            vec_1363 = param_1365_1[0]

            # Program Call Region
            param_1388_0 = [vec_1386]
            ret = self.proc_515_(param_1388_0)
            vec_1386 = param_1388_0[0]

        vec_index1386 = 0
        vec_index1362 = 0
        vec_index1363 = 0
        # Induction Output Region
        # Program Series Region
        # Program VectorClear Region
        del vec_1362[:]
        vec_index1362 = 0
        # Program VectorClear Region
        del vec_1363[:]
        vec_index1363 = 0
        # Program VectorClear Region
        del vec_1386[:]
        vec_index1386 = 0
        # Program Return Region
        return False
        return False

    def proc_1310_(self, var_1311: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1311_1311 = (var_1311, var_1311)
        prev_state = self.table_17[tuple_1311_1311]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_17[tuple_1311_1311] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1330_(var_1311, var_1311)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1081_(var_1311, var_1311)

        # Program Return Region
        return False
        return False

    def proc_1330_(self, var_1331: int, var_1332: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1334: List[int] = list()
        vec_index1334: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1334: int
        scan_index_1334: int = 0
        scan_tuple_1334_vec: List[int] = self.index_558[var_1332]
        while scan_index_1334 < len(scan_tuple_1334_vec):
            scan_tuple_1334 = scan_tuple_1334_vec[scan_index_1334]
            scan_index_1334 += 1
            vec_1334.append(scan_tuple_1334)
        # Program VectorLoop Region
        vec_index1334 = 0
        while vec_index1334 < len(vec_1334):
            var_1335 = vec_1334[vec_index1334]
            vec_index1334 += 1
            # Program Call Region
            ret = self.proc_1336_(var_1332, var_1331, var_1335)

        # Program Return Region
        return False
        return False

    def proc_1336_(self, var_1337: int, var_1338: int, var_1339: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1338_1339 = (var_1338, var_1339)
        prev_state = self.table_17[tuple_1338_1339]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_17[tuple_1338_1339] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1330_(var_1338, var_1339)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1081_(var_1338, var_1339)

        # Program Return Region
        return False
        return False

    def proc_1347_(self, var_1348: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program Call Region
        # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Tuple.cpp: BuildTopDownTupleChecker::call_pred
        ret = self.proc_1188_(var_1348)
        if ret:
            # Program Return Region
            return True
        # Program Return Region
        return False
        return False

    def proc_1352_(self, var_1353: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1489: List[Tuple[int, ControlFlowEdgeKind]] = list()
        vec_index1489: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1489: Tuple[int, ControlFlowEdgeKind]
        scan_index_1489: int = 0
        scan_tuple_1489_vec: List[Tuple[int, ControlFlowEdgeKind]] = self.index_1488[var_1353]
        while scan_index_1489 < len(scan_tuple_1489_vec):
            scan_tuple_1489 = scan_tuple_1489_vec[scan_index_1489]
            scan_index_1489 += 1
            vec_1489.append(scan_tuple_1489)
        # Program VectorLoop Region
        vec_index1489 = 0
        while vec_index1489 < len(vec_1489):
            var_1490, var_1491 = vec_1489[vec_index1489]
            vec_index1489 += 1
            # Program CheckState Region
            state = self.table_20[(var_1490, var_1353, var_1491)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_1491 = self._resolve_edgetype(var_1491)
                tuple_1490_1353_1491 = (var_1490, var_1353, var_1491)
                prev_state = self.table_20[tuple_1490_1353_1491]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_1490_1353_1491] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_978_(var_1490, var_1353, var_1491)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1491 = self._resolve_edgetype(var_1491)
                        tuple_1490_1353_1491 = (var_1490, var_1353, var_1491)
                        prev_state = self.table_20[tuple_1490_1353_1491]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1490_1353_1491] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1490_1353_1491[1], tuple_1490_1353_1491[2])].append(tuple_1490_1353_1491[0])
                                self.index_1062[(tuple_1490_1353_1491[0], tuple_1490_1353_1491[1])].append(tuple_1490_1353_1491[2])
                                self.index_1488[tuple_1490_1353_1491[1]].append((tuple_1490_1353_1491[0], tuple_1490_1353_1491[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_988_(var_1490, var_1353, var_1491)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1491 = self._resolve_edgetype(var_1491)
                        tuple_1490_1353_1491 = (var_1490, var_1353, var_1491)
                        prev_state = self.table_20[tuple_1490_1353_1491]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1490_1353_1491] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1490_1353_1491[1], tuple_1490_1353_1491[2])].append(tuple_1490_1353_1491[0])
                                self.index_1062[(tuple_1490_1353_1491[0], tuple_1490_1353_1491[1])].append(tuple_1490_1353_1491[2])
                                self.index_1488[tuple_1490_1353_1491[1]].append((tuple_1490_1353_1491[0], tuple_1490_1353_1491[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_993_(var_1490, var_1353, var_1491)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1491 = self._resolve_edgetype(var_1491)
                        tuple_1490_1353_1491 = (var_1490, var_1353, var_1491)
                        prev_state = self.table_20[tuple_1490_1353_1491]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1490_1353_1491] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1490_1353_1491[1], tuple_1490_1353_1491[2])].append(tuple_1490_1353_1491[0])
                                self.index_1062[(tuple_1490_1353_1491[0], tuple_1490_1353_1491[1])].append(tuple_1490_1353_1491[2])
                                self.index_1488[tuple_1490_1353_1491[1]].append((tuple_1490_1353_1491[0], tuple_1490_1353_1491[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1358_(self, var_1359: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1480: List[int] = list()
        vec_index1480: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1480: int
        scan_index_1480: int = 0
        scan_tuple_1480_vec: List[int] = self.index_1479[var_1359, self.var_2]
        while scan_index_1480 < len(scan_tuple_1480_vec):
            scan_tuple_1480 = scan_tuple_1480_vec[scan_index_1480]
            scan_index_1480 += 1
            vec_1480.append(scan_tuple_1480)
        # Program VectorLoop Region
        vec_index1480 = 0
        while vec_index1480 < len(vec_1480):
            var_1481 = vec_1480[vec_index1480]
            vec_index1480 += 1
            # Program Call Region
            ret = self.proc_1482_(var_1359, self.var_2)
            if ret:
                # Program Return Region
                return True
        # Program Return Region
        return False
        return False

    def proc_1366_(self, var_1367: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1428: List[int] = list()
        vec_index1428: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1428: int
        scan_index_1428: int = 0
        scan_tuple_1428_vec: List[int] = self.index_290[var_1367]
        while scan_index_1428 < len(scan_tuple_1428_vec):
            scan_tuple_1428 = scan_tuple_1428_vec[scan_index_1428]
            scan_index_1428 += 1
            vec_1428.append(scan_tuple_1428)
        # Program VectorLoop Region
        vec_index1428 = 0
        while vec_index1428 < len(vec_1428):
            var_1429 = vec_1428[vec_index1428]
            vec_index1428 += 1
            # Program Call Region
            ret = self.proc_1294_(var_1367, var_1429)

        # Program Return Region
        return False
        return False

    def proc_1372_(self, var_1373: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1409: List[int] = list()
        vec_index1409: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1409: int
        scan_index_1409: int = 0
        scan_tuple_1409_vec: List[int] = self.index_421[var_1373]
        while scan_index_1409 < len(scan_tuple_1409_vec):
            scan_tuple_1409 = scan_tuple_1409_vec[scan_index_1409]
            scan_index_1409 += 1
            vec_1409.append(scan_tuple_1409)
        # Program VectorLoop Region
        vec_index1409 = 0
        while vec_index1409 < len(vec_1409):
            var_1410 = vec_1409[vec_index1409]
            vec_index1409 += 1
            # Program Call Region
            ret = self.proc_1411_(var_1373, var_1410)

        # Program Return Region
        return False
        return False

    def proc_1375_(self, var_1376: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1389: List[int] = list()
        vec_index1389: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1389: int
        scan_index_1389: int = 0
        scan_tuple_1389_vec: List[int] = self.index_436[var_1376]
        while scan_index_1389 < len(scan_tuple_1389_vec):
            scan_tuple_1389 = scan_tuple_1389_vec[scan_index_1389]
            scan_index_1389 += 1
            vec_1389.append(scan_tuple_1389)
        # Program VectorLoop Region
        vec_index1389 = 0
        while vec_index1389 < len(vec_1389):
            var_1390 = vec_1389[vec_index1389]
            vec_index1389 += 1
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1391_(var_1376, var_1390)

            # Program Call Region
            ret = self.proc_1395_(var_1376, var_1390)

        # Program Return Region
        return False
        return False

    def proc_1391_(self, var_1392: int, var_1393: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1393_1392 = (var_1393, var_1392)
        prev_state = self.table_154[tuple_1393_1392]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_154[tuple_1393_1392] = 2 | 4
            # Program Call Region
            ret = self.proc_1404_(var_1392, var_1393)

        # Program Return Region
        return False
        return False

    def proc_1395_(self, var_1396: int, var_1397: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1397_1396 = (var_1397, var_1396)
        prev_state = self.table_33[tuple_1397_1396]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_33[tuple_1397_1396] = 2 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_890_(var_1396, var_1397)

        # Program Return Region
        return False
        return False

    def proc_1404_(self, var_1405: int, var_1406: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1406 = var_1406
        prev_state = self.table_26[tuple_1406]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_26[tuple_1406] = 2 | 4
            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1069_(var_1406)

        # Program Return Region
        return False
        return False

    def proc_1411_(self, var_1412: int, var_1413: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1413_1412_10 = (var_1413, var_1412, self.var_10)
        prev_state = self.table_20[tuple_1413_1412_10]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_20[tuple_1413_1412_10] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1202_(var_1413, var_1412, self.var_10)

            # Program Call Region
            ret = self.proc_1207_(var_1413, var_1412, self.var_10)

            # Program Call Region
            ret = self.proc_1212_(var_1413, var_1412, self.var_10)

            # Program Call Region
            ret = self.proc_1217_(var_1413, var_1412, self.var_10)

            # Program Call Region
            ret = self.proc_1222_(var_1413, var_1412, self.var_10)

        # Program Return Region
        return False
        return False

    def proc_1432_(self, var_1433: ControlFlowEdgeKind, var_1434: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        # Program Series Region
        # Program TransitionState Region
        tuple_1434 = var_1434
        prev_state = self.table_15[tuple_1434]
        state = prev_state & 3
        present_bit = prev_state & 4
        if state == 1:
            self.table_15[tuple_1434] = 2 | 4
            # Program Parallel Region
            # Program Call Region
            ret = self.proc_1307_(var_1434)

            # Program Call Region
            ret = self.proc_1310_(var_1434)

            # Program Call Region
            # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Optimize.cpp: InlineCalls: /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Insert.cpp: CreateBottomUpInsertRemover
            ret = self.proc_1188_(var_1434)

        # Program Return Region
        return False
        return False

    def proc_1449_(self, var_1450: int, var_1451: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1473: List[ControlFlowEdgeKind] = list()
        vec_index1473: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1473: ControlFlowEdgeKind
        scan_index_1473: int = 0
        scan_tuple_1473_vec: List[ControlFlowEdgeKind] = self.index_1062[var_1451, var_1450]
        while scan_index_1473 < len(scan_tuple_1473_vec):
            scan_tuple_1473 = scan_tuple_1473_vec[scan_index_1473]
            scan_index_1473 += 1
            vec_1473.append(scan_tuple_1473)
        # Program VectorLoop Region
        vec_index1473 = 0
        while vec_index1473 < len(vec_1473):
            var_1474 = vec_1473[vec_index1473]
            vec_index1473 += 1
            # Program CheckState Region
            state = self.table_20[(var_1451, var_1450, var_1474)] & 3
            if state == 1:
                # Program Return Region
                return True
            elif state == 2:
                # Program TransitionState Region
                var_1474 = self._resolve_edgetype(var_1474)
                tuple_1451_1450_1474 = (var_1451, var_1450, var_1474)
                prev_state = self.table_20[tuple_1451_1450_1474]
                state = prev_state & 3
                present_bit = prev_state & 4
                if state == 2:
                    self.table_20[tuple_1451_1450_1474] = 0 | 4
                    # Program Parallel Region
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_978_(var_1451, var_1450, var_1474)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1474 = self._resolve_edgetype(var_1474)
                        tuple_1451_1450_1474 = (var_1451, var_1450, var_1474)
                        prev_state = self.table_20[tuple_1451_1450_1474]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1451_1450_1474] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1451_1450_1474[1], tuple_1451_1450_1474[2])].append(tuple_1451_1450_1474[0])
                                self.index_1062[(tuple_1451_1450_1474[0], tuple_1451_1450_1474[1])].append(tuple_1451_1450_1474[2])
                                self.index_1488[tuple_1451_1450_1474[1]].append((tuple_1451_1450_1474[0], tuple_1451_1450_1474[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_988_(var_1451, var_1450, var_1474)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1474 = self._resolve_edgetype(var_1474)
                        tuple_1451_1450_1474 = (var_1451, var_1450, var_1474)
                        prev_state = self.table_20[tuple_1451_1450_1474]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1451_1450_1474] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1451_1450_1474[1], tuple_1451_1450_1474[2])].append(tuple_1451_1450_1474[0])
                                self.index_1062[(tuple_1451_1450_1474[0], tuple_1451_1450_1474[1])].append(tuple_1451_1450_1474[2])
                                self.index_1488[tuple_1451_1450_1474[1]].append((tuple_1451_1450_1474[0], tuple_1451_1450_1474[2]))
                        # Program Return Region
                        return True
                    # Program Call Region
                    # /Users/pag/Code/DrLojekyll/lib/ControlFlow/Build/Induction.cpp: BuildTopDownInductionChecker::build_rule_checks
                    ret = self.proc_993_(var_1451, var_1450, var_1474)
                    if ret:
                        # Program Series Region
                        # Program TransitionState Region
                        var_1474 = self._resolve_edgetype(var_1474)
                        tuple_1451_1450_1474 = (var_1451, var_1450, var_1474)
                        prev_state = self.table_20[tuple_1451_1450_1474]
                        state = prev_state & 3
                        present_bit = prev_state & 4
                        if state == 0 or state == 2:
                            self.table_20[tuple_1451_1450_1474] = 1 | 4
                            if not present_bit:
                                self.index_969[(tuple_1451_1450_1474[1], tuple_1451_1450_1474[2])].append(tuple_1451_1450_1474[0])
                                self.index_1062[(tuple_1451_1450_1474[0], tuple_1451_1450_1474[1])].append(tuple_1451_1450_1474[2])
                                self.index_1488[tuple_1451_1450_1474[1]].append((tuple_1451_1450_1474[0], tuple_1451_1450_1474[2]))
                        # Program Return Region
                        return True
        # Program Return Region
        return False
        return False

    def proc_1466_(self, var_1467: int, var_1468: int) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1470: List[int] = list()
        vec_index1470: int = 0
        # Program Series Region
        # Program TableScan Region
        scan_tuple_1470: int
        scan_index_1470: int = 0
        scan_tuple_1470_vec: List[int] = self.index_557[var_1467]
        while scan_index_1470 < len(scan_tuple_1470_vec):
            scan_tuple_1470 = scan_tuple_1470_vec[scan_index_1470]
            scan_index_1470 += 1
            vec_1470.append(scan_tuple_1470)
        # Program VectorLoop Region
        vec_index1470 = 0
        while vec_index1470 < len(vec_1470):
            var_1471 = vec_1470[vec_index1470]
            vec_index1470 += 1
            # Program Call Region
            ret = self.proc_1336_(var_1467, var_1471, var_1468)

        # Program Return Region
        return False
        return False

    def proc_1482_(self, var_1483: int, var_1484: ControlFlowEdgeKind) -> bool:
        state: int = 2
        prev_state: int = 2
        present_bit: int = 0
        ret: bool = False
        found: bool = False
        vec_1486: List[int] = list()
        vec_index1486: int = 0
        # Program Series Region
        # Program TableScan Region
        var_1484 = self._resolve_edgetype(var_1484)
        scan_tuple_1486: int
        scan_index_1486: int = 0
        scan_tuple_1486_vec: List[int] = self.index_1479[var_1483, var_1484]
        while scan_index_1486 < len(scan_tuple_1486_vec):
            scan_tuple_1486 = scan_tuple_1486_vec[scan_index_1486]
            scan_index_1486 += 1
            vec_1486.append(scan_tuple_1486)
        # Program VectorLoop Region
        vec_index1486 = 0
        while vec_index1486 < len(vec_1486):
            var_1487 = vec_1486[vec_index1486]
            vec_index1486 += 1
            # Program CheckState Region
            state = self.table_11[(var_1487, var_1483, var_1484)] & 3
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
            if not self.proc_874_(param_0):
                continue
            yield param_0

    def intraproc_transfer_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_876[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_877_(param_0, param_1):
                continue
            yield param_1

    def function_b(self, param_0: int) -> bool:
        state: int = 0
        tuple_index: int = 0
        if True:
            if not self.proc_880_(param_0):
                return False
            return True

    def function_f(self) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        for tuple in self.table_15:
            tuple_index += 1
            param_0: int = tuple
            if not self.proc_880_(param_0):
                continue
            yield param_0

    def function_instruction_bf(self, param_0: int) -> Iterator[int]:
        state: int = 0
        tuple_index: int = 0
        tuple_vec: List[int] = self.index_882[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_883_(param_0, param_1):
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
        tuple_vec: List[int] = self.index_886[param_0]
        while tuple_index < len(tuple_vec):
            tuple = tuple_vec[tuple_index]
            tuple_index += 1
            param_1: int = tuple
            if not self.proc_887_(param_0, param_1):
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

