from dds import DatabaseFunctors, DatabaseLog, Database
import lief
import os
import re
import subprocess
import sys
from capstone import *
from binascii import unhexlify

# Capstone setup.
md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = True
md.syntax = CS_OPT_SYNTAX_ATT

# Usage help.
usage = '''Usage: 
		\tpython3 %s [target_binary] [disassembler]
		\tSupported disassemblers:
		\t  objdump
		\t  llvm-objdump
		\t  lief
		''' % sys.argv[0]

# Important definitions.
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

# Return instruction type given its mnemonic and operand.
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


# Retrieve potential addresses from instruction operands.
def get_address_in_operands(operands):
	matches = re.search(r'(0x[0-9a-fA-F]+)', operands)
	return int(matches.group(),16)


# Add an `.extern` section (4-byte aligned) with 
# enough slots to accommodate each PLT relocations.
def lief_reloc_externs(parsed, plt_relocs):
	s_extern                 = lief.ELF.Section()
	s_extern.name            = ".extern"
	s_extern.type            = lief.ELF.SECTION_TYPES.PROGBITS
	s_extern.virtual_address = max([(x.virtual_address+x.size) for x in parsed.sections])
	s_extern.alignment       = 4
	s_extern.content         = [0] * s_extern.alignment * len(plt_relocs)
	s_extern                 = parsed.add(s_extern, False)

	for i in range(0, len(plt_relocs)):
		reloc_addr = plt_relocs[i].address
		extrn_addr = (i * s_extern.alignment) + s_extern.virtual_address
		#db.relocation_2(reloc_addr, extrn_addr)

	return

# Disassemble with lief.
def lief_disassemble(db, targ):
	parsed = lief.parse(targ)

	# Set up .extern section.
	
	plt_relocs = [x for x in parsed.relocations \
		if x.purpose == lief.ELF.RELOCATION_PURPOSES.PLTGOT]
	lief_reloc_externs(parsed, plt_relocs)

	# Iterate all sections.

	for s in parsed.sections:
		s_name  = bytes(s.name, "utf-8")
		s_start = s.virtual_address
		s_end   = s.virtual_address + s.size
		s_bytes = bytearray(s.content)
		s_flags = s.flags_list

		# Parse executable sections.

		if FLAG_ELF_EXEC in s_flags:	
			db.section_4([(s_name, s_start, s_end, SECTION_EXEC)])

			for x in range(0, 15): 	
				for i in md.disasm(s_bytes[x:], s_start + x):
					i_addr  = i.address
					i_next  = i.address + i.size
					i_type  = get_instruction_type(i.mnemonic, i.op_str)
					i_bytes = i.bytes.hex()

					db.instruction_4([(i_addr, i_type, i_bytes, s_name)])

					# Connect instructions with transfers (or pseudo-transfers, 
					# for jumps / calls). Omit new transfers for RETs / HLTs.

					if i_type == INSN_NORMAL or i_type == INSN_NOP:
						db.transfer_3([(i_addr, i_next, EDGE_FALLTHRU)])
					if i_type == INSN_COND_DIRECT_JUMP:
						i_targ = get_address_in_operands(i.op_str)
						db.transfer_3([(i_addr, i_targ, EDGE_COND_TRUE)])
						db.transfer_3([(i_addr, i_next, EDGE_COND_FALSE)]) 
					if i_type == INSN_DIRECT_JUMP:
						i_targ = get_address_in_operands(i.op_str)
						db.transfer_3([(i_addr, i_targ, EDGE_JUMP_TARG)])
						db.transfer_3([(i_addr, i_next, EDGE_JUMP_PSEUDO)]) # post-jump fallthrough	
					if i_type == INSN_DIRECT_CALL:
						i_targ = get_address_in_operands(i.op_str)
						db.transfer_3([(i_addr, i_targ, EDGE_CALL_TARG)])
						db.transfer_3([(i_addr, i_next, EDGE_CALL_PSEUDO)]) # post-call fallthrough
					
					#if (s_name == b'.plt') and i_type == INSN_INDIRECT_JUMP:
					#	i_targ = get_address_in_operands(i.op_str)
					#	print (hex(i_addr), hex(i_targ))
						#for i_targ in get_addrs_in_operands(i.op_str, exec_lower, exec_upper):
						#	print (hex(i_targ))
						#print ()

		else:	
			db.section_4([(s_name, s_start, s_end, SECTION_DATA)])
	
	#print ([hex(x.address) for x in plt_relocs])

	#for f in db.get_functions_f():
		#print (hex(f))
	#	for i in db.get_function_instructions_bf(f):
	#		print (hex(i))
	#	print ('')

	#for i in db.get_external_calls_f():
	#	print (hex(i))
	
	
	return

# Main function.
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

	lief_disassemble(db, targ)