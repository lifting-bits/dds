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

# Control-flow personalities
FLOW_FALLTHRU   = 0
FLOW_JUMP_TARG  = 1
FLOW_COND_TRUE  = 2
FLOW_COND_FALSE = 3
FLOW_CALL_TARG  = 4
FLOW_PSEUDO     = 5

# Return instruction type 
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
def disassemble_lief(targ, db):
	parsed = lief.parse(targ)

	for s in parsed.sections:
		s_name  = bytes(s.name, "utf-8")
		s_start = s.virtual_address
		s_end   = s.virtual_address + s.size
		s_bytes = bytearray(s.content)
		s_flags = s.flags_list

		# Declare section
		db.section_3([(s_name, s_start, s_end)])
		
		# Declare executable section
		if lief.ELF.SECTION_FLAGS.EXECINSTR in s_flags:
		#	db.executable_section_3([(s_name, s_start, s_end)])

			for x in range(0, 15): 
				s_insns = md.disasm(s_bytes[x:], s_start+x)

			for i in s_insns:
				i_type = get_instruction_type(i.mnemonic, i.op_str)

				db.instruction_3([(i.address, i_type, s_name)])
				
				if i_type == INSN_NORMAL or i_type == INSN_NOP:
					db.instruction_transfer_3([(i.address, i.address+i.size, FLOW_FALLTHRU)])
				if i_type == INSN_COND_DIRECT_JUMP:
					db.instruction_transfer_3([(i.address, int(i.op_str,16), FLOW_COND_TRUE)])
					db.instruction_transfer_3([(i.address, i.address+i.size, FLOW_COND_FALSE)]) 
				if i_type == INSN_DIRECT_CALL:
					db.instruction_transfer_3([(i.address, int(i.op_str,16), FLOW_CALL_TARG)])
					db.instruction_transfer_3([(i.address, i.address+i.size, FLOW_PSEUDO)]) # fallthrough (pseudo-edge)
				

	#for x in db.get_section_instructions(b'.text'):
	#	print (hex(x))
	for x in db.get_called_functions_f():
		print (hex(x))

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

	disassemble_lief(targ, db)