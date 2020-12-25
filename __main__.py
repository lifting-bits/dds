from dds import DatabaseFunctors, DatabaseLog, Database
import lief
import os
import re
import subprocess
import sys
from capstone import *
from binascii import unhexlify

# Capstone setup
md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = True
md.syntax = CS_OPT_SYNTAX_ATT

# Usage help
usage = '''Usage: 
		\tpython3 %s [target_binary] [disassembler]
		\tSupported disassemblers:
		\t  objdump
		\t  llvm-objdump
		\t  lief
		''' % sys.argv[0]

# Section personalities
SECTION_DATA = 0
SECTION_EXEC = 1

# Instruction personalities
INSN_NORMAL             = 0
INSN_DIRECT_JUMP        = 1
INSN_INDIRECT_JUMP      = 2
INSN_COND_DIRECT_JUMP   = 3
INSN_COND_INDIRECT_JUMP = 4
INSN_DIRECT_CALL        = 5
INSN_INDIRECT_CALL      = 6
INSN_RETURN             = 7
INSN_NOP                = 8

# Flow personalities
FLOW_INTRA_PROC = 0
FLOW_INTER_PROC = 1

# Edge personalities
EDGE_FALLTHRU   = 0
EDGE_JUMP_TARG  = 1
EDGE_COND_TRUE  = 2
EDGE_COND_FALSE = 3
EDGE_CALL_TARG  = 4
EDGE_PSEUDO     = 5


# Return instruction type given its mnemonic and operand
def get_instruction_type(mnemonic, operands):
	insn_str = "%s %s" % (mnemonic, operands)
	if (re.match(r'(jmp[a-z]*) 0x',  insn_str)): # 1
		return INSN_DIRECT_JUMP	
	if (re.match(r'(jmp[a-z]*) \*',  insn_str)): # 2
		return INSN_INDIRECT_JUMP
	if (re.match(r'(j[a-z]*) 0x',    insn_str)): # 3
		return INSN_COND_DIRECT_JUMP
	if (re.match(r'(j[a-z]*) \*',    insn_str)): # 4
		return INSN_COND_INDIRECT_JUMP
	if (re.match(r'(call[a-z]*) 0x', insn_str)): # 5
		return INSN_DIRECT_CALL
	if (re.match(r'(call[a-z]*) \*', insn_str)): # 6
		return INSN_INDIRECT_CALL
	if (re.match(r'(ret)',           insn_str)): # 7
		return INSN_RETURN	
	if (re.match(r'(nop)',           insn_str)): # 8
		return INSN_NOP	
	return INSN_NORMAL # 0


# Parses a Capstone CsInsn object into DrLoj
def lief_parse_instruction(CsInsn, SecName):
	InsnEA   = CsInsn.address
	NextEA   = CsInsn.address + CsInsn.size
	InsnType = get_instruction_type(CsInsn.mnemonic, CsInsn.op_str)

	db.instruction_4([(InsnEA, InsnType, '', SecName)])
	
	if InsnType == INSN_NORMAL or InsnType == INSN_NOP:
		db.instruction_transfer_4([(InsnEA, NextEA, EDGE_FALLTHRU, FLOW_INTRA_PROC)])
	if InsnType == INSN_COND_DIRECT_JUMP:
		TargEA = int(CsInsn.op_str,16) 
		db.instruction_transfer_4([(InsnEA, TargEA, EDGE_COND_TRUE, FLOW_INTRA_PROC)])
		db.instruction_transfer_4([(InsnEA, NextEA, EDGE_COND_FALSE, FLOW_INTRA_PROC)]) 
	if InsnType == INSN_DIRECT_CALL:
		TargEA = int(CsInsn.op_str,16)
		db.instruction_transfer_4([(InsnEA, TargEA, EDGE_CALL_TARG, FLOW_INTER_PROC)])
		db.instruction_transfer_4([(InsnEA, NextEA, EDGE_PSEUDO, FLOW_INTRA_PROC)]) # fallthrough (pseudo-edge)

	return


# Parses a function as a group of intraprocedural successors
def lief_parse_function(InsnEA):
	FuncStart = InsnEA
	
	while (InsnEA != None):
		try: 
			InsnEA = next(db.get_intraproc_successor_bf(InsnEA))
			#db.instruction(InsnEA) -> want to now update FuncEA
			#db.function_instruction(InsnEA, FuncEA)
		except: 
			break

	FuncEnd = InsnEA

	print (hex(FuncStart), hex(FuncEnd))
	return


# Disassemble with lief
def disassemble_lief(db, targ):
	parsed = lief.parse(targ)

	# Iterate all available sections
	for s in parsed.sections:
		SecName  = bytes(s.name, "utf-8")
		SecStart = s.virtual_address
		SecEnd   = s.virtual_address + s.size
		SecBytes = bytearray(s.content)
		SecFlags = s.flags_list

		# Parse executable sections
		if lief.ELF.SECTION_FLAGS.EXECINSTR in SecFlags:
			db.section_4([(SecName, SecStart, SecEnd, SECTION_EXEC)])

			# Parse all decoded instructions
			for x in range(0, 15): 	
				for i in md.disasm(SecBytes[x:], SecStart + x):
					lief_parse_instruction(i, SecName) 

		# Parse data sections
		else:
			db.section_4([(SecName, SecStart, SecEnd, SECTION_DATA)])

	# Parse functions 			
	for i in db.get_direct_call_targets_f():
		lief_parse_function(i)

	return


# Main function
if __name__ == "__main__":
	functors = DatabaseFunctors()
	log = DatabaseLog()
	db = Database(log, functors)

	if len(sys.argv) != 3:
		print("ERROR: Missing argument(s)!")
		print(usage)
		exit(0)

	targ = sys.argv[1]
	if not os.path.exists(targ):
		print("ERROR: Can't find target binary (%s)!" % targ)
		print(usage)
		exit(0)	

	disassemble_lief(db, targ)