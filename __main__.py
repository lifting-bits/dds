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

SECTION_DATA = 0
SECTION_EXEC = 1

INSN_NORMAL             = 0
INSN_DIRECT_JUMP        = 1
INSN_INDIRECT_JUMP      = 2
INSN_COND_DIRECT_JUMP   = 3
INSN_COND_INDIRECT_JUMP = 4
INSN_DIRECT_CALL        = 5
INSN_INDIRECT_CALL      = 6
INSN_RETURN             = 7
INSN_NOP                = 8

FLOW_INTRA_PROC = 0
FLOW_INTER_PROC = 1

EDGE_FALLTHRU   = 0
EDGE_JUMP_TARG  = 1
EDGE_COND_TRUE  = 2
EDGE_COND_FALSE = 3
EDGE_CALL_TARG  = 4
EDGE_CALL_RET   = 5

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

# Disassemble with lief
def disassemble_lief(db, targ):
	parsed = lief.parse(targ)

	# Iterate all available sections
	for s in parsed.sections:
		s_name  = bytes(s.name, "utf-8")
		s_start = s.virtual_address
		s_end   = s.virtual_address + s.size
		s_bytes = bytearray(s.content)
		s_flags = s.flags_list

		# Parse executable sections and decoded instructions
		if lief.ELF.SECTION_FLAGS.EXECINSTR in s_flags:
			db.section_4([(s_name, s_start, s_end, SECTION_EXEC)])

			for x in range(0, 15): 	
				for i in md.disasm(s_bytes[x:], s_start + x):
					i_addr   = i.address
					i_next   = i.address + i.size
					i_type = get_instruction_type(i.mnemonic, i.op_str)

					db.instruction_3([(i_addr, i_type, s_name)])
					
					if i_type == INSN_NORMAL or i_type == INSN_NOP:
						db.instruction_transfer_3([(i_addr, i_next, EDGE_FALLTHRU)])
					if i_type == INSN_COND_DIRECT_JUMP:
						i_targ = int(i.op_str,16) 
						db.instruction_transfer_3([(i_addr, i_targ, EDGE_COND_TRUE)])
						db.instruction_transfer_3([(i_addr, i_next, EDGE_COND_FALSE)]) 
					if i_type == INSN_DIRECT_CALL:
						i_targ = int(i.op_str,16)
						db.instruction_transfer_3([(i_addr, i_targ, EDGE_CALL_TARG)])
						db.instruction_transfer_3([(i_addr, i_next, EDGE_CALL_RET)]) 

		# Parse data sections
		else:
			db.section_4([(s_name, s_start, s_end, SECTION_DATA)])


	for f in db.get_functions_f():
		print (hex(f))

		for i in db.get_function_instructions_bf(f):
			print (hex(i))

		exit(0)

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