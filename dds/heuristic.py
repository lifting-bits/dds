# Copyright 2021, Trail of Bits. All rights reserved.

from enum import IntEnum


class ControlFlowRecoveryHeuristic(IntEnum):
    # Should we assume that a control-flow transfer that is a function call
    # that leads to an instruction that is plausible (i.e. doesn't always lead
    # to non-decodable instructions) is a function head?
    FUNCTION_CALL_TARGETS_ARE_FUNCTION_HEADS = 0

    # Should we trust the function heads identified by the binary parser?
    # The binary parser may pass through function heads that are present
    # in the binary itself, as well as ones that it has figured out through
    # analysis alone (e.g. byte-pased pattern matching to discover likely
    # function prologues).
    TRUST_BINARY_PARSER_FUNCTION_HEADS = 1
