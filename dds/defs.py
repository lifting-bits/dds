# Copyright 2020, Trail of Bits. All rights reserved.


import lief

# Sections
SECTION_DATA            = 0
SECTION_EXEC            = 1

# Instructions
INSN_NORMAL             = 0
INSN_DIRECT_JUMP        = 1
INSN_INDIRECT_JUMP      = 2
INSN_COND_DIRECT_JUMP   = 3
INSN_COND_INDIRECT_JUMP = 4
INSN_DIRECT_CALL        = 5
INSN_INDIRECT_CALL      = 6
INSN_RETURN             = 7
INSN_HALT               = 8
INSN_NOP                = 9

# Transfers
EDGE_FALLTHRU           = 0
EDGE_JUMP_TARG          = 1
EDGE_JUMP_PSEUDO        = 2
EDGE_COND_TRUE          = 3
EDGE_COND_FALSE         = 4
EDGE_CALL_TARG          = 5
EDGE_CALL_PSEUDO        = 6

# Useful Flags
FLAG_ELF_EXEC = lief.ELF.SECTION_FLAGS.EXECINSTR