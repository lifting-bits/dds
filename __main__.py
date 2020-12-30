from dds import DatabaseFunctors, DatabaseLog, Database
from util import *
from defs import *
from capstone import *
import capstone.x86
import lief, os, re, sys

# Add an `.extern` section (4-byte aligned) with 
# enough slots to accommodate each PLT relocations.
def lief_relocate_externs(parsed, relocs):
	s_extern                 = lief.ELF.Section()
	s_extern.name            = ".extern"
	s_extern.type            = lief.ELF.SECTION_TYPES.PROGBITS
	s_extern.virtual_address = max([(x.virtual_address+x.size) \
								     for x in parsed.sections])
	s_extern.alignment       = 4
	s_extern.content         = [0] * s_extern.alignment * len(relocs)
	s_extern                 = parsed.add(s_extern, False)

	for i in range(0, len(relocs)):
		reloc_addr  = relocs[i].address
		extern_addr = (i * s_extern.alignment) + s_extern.virtual_address
		db.relocation_2([(reloc_addr, extern_addr)])

	return


# For edges with two outgoing edges (including calls
# and jumps), add their corresponding target and 
# fallthrough (or pseudo-fallthrough) edges.
def lief_add_two_edges(instruction, TARGET, FALLTHRU):
	i_addr = instruction.address
	i_next = instruction.address + instruction.size
	i_targ = get_transfer_target(instruction)

	if (i_targ): 
		# Check if the target address is relocated.
		i_targ = next(db.get_relocated_target_bf(i_targ), i_targ)
		db.transfer_3([(i_addr, i_targ, TARGET)])
		#print (hex(i_addr), hex(i_targ))

	db.transfer_3([(i_addr, i_next, FALLTHRU)]) 

	return


# Disassemble with lief.
def lief_disassemble(db, target):
	parsed                     = lief.parse(target)
	(b_type, b_arch, b_relocs) = get_target_info(parsed)
	cs                         = get_capstone(b_type, b_arch)

	# Set up necessary relocations.
	lief_relocate_externs(parsed, b_relocs)

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

			# Decode instructions with Capstone.
			for x in range(0, 15): 	
				for i in cs.disasm(s_bytes[x:], s_start + x):
					i_addr  = i.address
					i_next  = i.address + i.size
					i_type  = get_instruction_type(i.mnemonic, i.op_str)
					i_bytes = i.bytes.hex()

					# Add the instruction to our database.
					db.instruction_4([(i_addr, i_type, i_bytes, s_name)])

					# Conditional branches: add target and fallthrough edges.
					if i_type == INSN_COND_DIRECT_JUMP:
						lief_add_two_edges(i, EDGE_COND_TRUE, EDGE_COND_FALSE)
					
					# Jumps: add target edge, and post-jump fallthrough.
					elif i_type == INSN_DIRECT_JUMP or i_type == INSN_INDIRECT_JUMP:
						lief_add_two_edges(i, EDGE_JUMP_TARG, EDGE_JUMP_PSEUDO)
					
					# Calls: add target edge, and post-call fallthrough.
					elif i_type == INSN_DIRECT_CALL or i_type == INSN_INDIRECT_CALL:
						lief_add_two_edges(i, EDGE_CALL_TARG, EDGE_CALL_PSEUDO)

					# Rest: add fallthrough edges (except if RET or HLT).
					elif i_type == INSN_NORMAL or i_type == INSN_NOP:
						db.transfer_3([(i_addr, i_next, EDGE_FALLTHRU)])

		else:	
			db.section_4([(s_name, s_start, s_end, SECTION_DATA)])
	
	#print ([hex(x.address) for x in b_relocs])

	#for f in db.get_functions_f():
		#print (hex(f))
	#	for i in db.get_function_instructions_bf(f):
	#		print (hex(i))
	#	print ('')

	#for i in db.get_relocations_f():
	#	print (hex(i))
	
	return

# Main function.
if __name__ == "__main__":
	usage = '''Usage: 
		\tpython3 %s [target_binary] [disassembler]
		\tSupported disassemblers:
		\t  lief
		''' % sys.argv[0]

	functors = DatabaseFunctors()
	log = DatabaseLog()
	db = Database(log, functors)

	if len(sys.argv) != 3:
		print("ERROR: Missing argument(s)!")
		print(usage)
		exit(0)

	target = sys.argv[1]
	if not os.path.exists(target):
		print("ERROR: Can't find target binary (%s)!" % target)
		print(usage)
		exit(0)	

	lief_disassemble(db, target)