from dds import DatabaseFunctors, DatabaseLog, Database

import lief
import os
import re
import subprocess
import sys
from capstone import *
from binascii import unhexlify

md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = True
md.syntax = CS_OPT_SYNTAX_ATT

usage = '''Usage: 
		\tpython3 %s [target_binary] [disassembler]
		\tSupported disassemblers:
		\t  objdump
		\t  llvm-objdump
		\t  lief
		''' % sys.argv[0]


def parse_insn(i):
	addr   = i.address
	mnem   = i.mnemonic
	op_str = i.op_str
	instructions.add()
	#print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
	return

# Disassemble with lief

def disas_lief(targ, db):
	parsed = lief.parse(targ)

	for s in parsed.sections:
		s_name  = bytes(s.name)
		s_start = s.virtual_address
		s_end   = s.virtual_address + s.size
		s_bytes = bytearray(s.content)
		s_flags = s.flags_list

		db.section_3([(s_name, s_start, s_end)])

		print (s_name)

		# TODO: make format-agnostic

		if lief.ELF.SECTION_FLAGS.EXECINSTR in s_flags:
			#db.executable_section_3([(s_name, s_start, s_end)]) 
			
			for i in range(0, 15):
				s_insns = md.disasm(s_bytes[i:], s_start+i)

				for insn in s_insns:
					print(insn.address, insn)
					db.decoded_instruction_2([(insn.address, insn)])

	for addr in db.instruction_section_fb(b'.text'):
		print (addr)

	return

# Main function

if __name__ == "__main__":
	functors = DatabaseFunctors()
	log = DatabaseLog()
	db = Database(log, functors)

	# Get and check args

	if len(sys.argv) != 3:
		print("ERROR: Missing argument(s)!")
		print(usage)
		exit(0)

	targ = sys.argv[1]
	if not os.path.exists(targ):
		print("ERROR: Can't find target binary (%s)!" % targ)
		print(usage)
		exit(0)	

	disas_lief(targ, db)