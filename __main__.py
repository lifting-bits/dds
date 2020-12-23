from dds import DatabaseFunctors, DatabaseLog, Database
import lief
import os
import re
import subprocess
import sys
from capstone import *
from binascii import unhexlify

'''
class Instruction:
	self.addr = 
	self.mnem = 
	self.ops  = 
	self.pred = 
	self.succ = 
	def __init__(self):
'''

# Instruction personality types
PERSONALITY_NORMAL = 0
PERSONALITY_DIRECT_JUMP = 1
PERSONALITY_INDIRECT_JUMP = 2
PERSONALITY_CONDITIONAL_DIRECT_JUMP = 3
PERSONALITY_CONDITIONAL_INDIRECT_JUMP = 4
PERSONALITY_DIRECT_CALL = 5
PERSONALITY_INDIRECT_CALL = 6
PERSONALITY_RETURN = 7

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

# Return instruction type 
def get_instruction_type(mnemonic, operands):
	insn_str = "%s %s" % (mnemonic, operands)
	if (re.match(r'(jmp[a-z]*) 0x',  insn_str)): # 1
		return PERSONALITY_DIRECT_JUMP	
	if (re.match(r'(jmp[a-z]*) \*',  insn_str)): # 2
		return PERSONALITY_INDIRECT_JUMP
	if (re.match(r'(j[a-z]*) 0x',    insn_str)): # 3
		return PERSONALITY_CONDITIONAL_DIRECT_JUMP
	if (re.match(r'(j[a-z]*) \*',    insn_str)): # 4
		return PERSONALITY_CONDITIONAL_INDIRECT_JUMP
	if (re.match(r'(call[a-z]*) 0x', insn_str)): # 5
		return PERSONALITY_DIRECT_CALL
	if (re.match(r'(call[a-z]*) \*', insn_str)): # 6
		return PERSONALITY_INDIRECT_CALL
	if (re.match(r'(ret)',           insn_str)): # 7
		return PERSONALITY_RETURN	
	return PERSONALITY_NORMAL # 0

# Disassemble with lief
def disassemble_lief(targ, db):
	parsed = lief.parse(targ)

	for s in parsed.sections:
		s_name  = bytes(s.name, "utf-8")
		s_start = hex(s.virtual_address)
		s_end   = hex(s.virtual_address + s.size)
		s_bytes = bytearray(s.content)
		s_flags = s.flags_list

		# Declare section
		db.section_3([(s_name, s_start, s_end)])
		#if lief.ELF.SECTION_FLAGS.EXECINSTR in s_flags:
			#db.executable_section_3([(s_name, s_start, s_end)])

		if s_name == b'.text':

			# Decode with Capstone
			for x in range(0, 15): 
				s_insns = md.disasm(s_bytes[x:], int(s_start,16)+x)

			# Go through all instructions
			for i in s_insns:
				i_addr = hex(i.address)
				i_mnem = i.mnemonic
				i_ops  = i.op_str
				i_type = get_instruction_type(i_mnem, i_ops)

				print (i_addr, i_mnem, i_ops, i_type)	

				
				
				# Decode and declare
				#db.decoded_instruction_4([(s_name, s_start, i_addr, i_type)])
				
				
				

	#for x in db.instructions_from_section_name_bf(b'.text'):
		#print (x)

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