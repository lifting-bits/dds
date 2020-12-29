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

FLAG_ELF_EXEC = lief.ELF.SECTION_FLAGS.EXECINSTR

SECTION_DATA            = 0
SECTION_EXEC            = 1

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

EDGE_FALLTHRU           = 0
EDGE_JUMP_TARG          = 1
EDGE_JUMP_PSEUDO        = 2
EDGE_COND_TRUE          = 3
EDGE_COND_FALSE         = 4
EDGE_CALL_TARG          = 5
EDGE_CALL_PSEUDO        = 6

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
	if (re.match(r'(hlt)',           insn_str)): # 8
		return INSN_HALT
	if (re.match(r'(nop)',           insn_str)): # 9
		return INSN_NOP	
	return INSN_NORMAL # 0

def get_addrs_in_operands(operands, lbound, ubound):
	matches = re.findall(r'(0x[0-9a-fA-F]+)', operands)

	for addr in matches:
		addr = int(addr,16)
		if addr >= lbound and addr <= ubound:
			yield addr

	return

# Disassemble with lief
def disassemble_lief(db, targ):
	parsed = lief.parse(targ)

	# Get instruction entry / exit boundaries
	exec_lower = min([(x.virtual_address) \
		for x in parsed.sections if FLAG_ELF_EXEC in x.flags_list])
	exec_upper = max([(x.virtual_address+x.size) \
		for x in parsed.sections if FLAG_ELF_EXEC in x.flags_list])

	#print (hex(b_lower), hex(b_upper))

	print ([x.name for x in parsed.dynamic_symbols])

	# Iterate all available sections
	for s in parsed.sections:
		s_name  = bytes(s.name, "utf-8")
		s_start = s.virtual_address
		s_end   = s.virtual_address + s.size
		s_bytes = bytearray(s.content)
		s_flags = s.flags_list

		# Parse executable sections and decoded instructions
		if FLAG_ELF_EXEC in s_flags:
			db.section_4([(s_name, s_start, s_end, SECTION_EXEC)])

			for x in range(0, 15): 	
				for i in md.disasm(s_bytes[x:], s_start + x):
					i_addr  = i.address
					i_next  = i.address + i.size
					i_type  = get_instruction_type(i.mnemonic, i.op_str)
					i_bytes = i.bytes.hex()

					db.instruction_4([(i_addr, i_type, i_bytes, s_name)])

					# We connect all instructions with transfers (or pseudo
					# -transfers, for jumps and calls). We omit new transfers
					# when a RET or HLT instruction is encountered, as these
					# designate a procedure end.

					#print (hex(i_addr), i_type, i.mnemonic, i.op_str, get_possible_function(i.op_str))
						
					if i_type == INSN_NORMAL or i_type == INSN_NOP:
						db.transfer_3([(i_addr, i_next, EDGE_FALLTHRU)])
					
					if i_type == INSN_COND_DIRECT_JUMP:
						db.transfer_3([(i_addr, i_next, EDGE_COND_FALSE)]) 
						for i_targ in get_addrs_in_operands(i.op_str, exec_lower, exec_upper):
							db.transfer_3([(i_addr, i_targ, EDGE_COND_TRUE)])

					if i_type == INSN_DIRECT_JUMP:
						db.transfer_3([(i_addr, i_next, EDGE_JUMP_PSEUDO)]) # post-jump fallthrough
						for i_targ in get_addrs_in_operands(i.op_str, exec_lower, exec_upper):
							db.transfer_3([(i_addr, i_targ, EDGE_CALL_TARG)])
						
					if i_type == INSN_DIRECT_CALL:
						db.transfer_3([(i_addr, i_next, EDGE_CALL_PSEUDO)]) # post-call fallthrough
						for i_targ in get_addrs_in_operands(i.op_str, exec_lower, exec_upper):
							db.transfer_3([(i_addr, i_targ, EDGE_CALL_TARG)])
						
					# For PLT relocations, figure out the pointer address
					
					#if (s_name == b'.plt') and i_type == INSN_INDIRECT_JUMP:
					#	print (hex(i_addr))
						#for i_targ in get_addrs_in_operands(i.op_str, exec_lower, exec_upper):
						#	print (hex(i_targ))
						#print ()

		# Parse data sections
		else:
			db.section_4([(s_name, s_start, s_end, SECTION_DATA)])
	
	#for f in db.get_functions_f():
		#print (hex(f))
		#for i in db.get_function_instructions_bf(f):
		#	print (hex(i))

		#print ('')
		#exit(0)

	#for i in db.get_external_calls_f():
	#	print (hex(i))
	
	
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