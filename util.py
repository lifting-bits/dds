from defs import *
from capstone import *
import capstone.x86
import lief, re

# Retrieve target operands from transfer instructions.
def get_transfer_target(instruction):	
	target = None
	op = instruction.operands[0]

	# All direct transfers, e.g., `jmp 0xaddr`
	if op.type == capstone.x86.X86_OP_IMM:
		return op.imm
			
	# Indirect transfers
	elif op.type == capstone.x86.X86_OP_MEM:
		mem = op.mem
	
		# PC-relative, e.g. `jmp [RIP + 0xdisp]`.
		if mem.base == capstone.x86.X86_REG_RIP \
		and not mem.segment \
		and not mem.index:
			return instruction.address + mem.disp					
		
		# Absolute addr, e.g. `jmp [0xaddr]`.
		elif not mem.base \
		and not mem.segment \
		and not mem.index \
		and mem.disp:
			return mem.disp	

		else:
			return None

	return None
	

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


# Returns a triple of the target's supported type 
# (ELF, ...), architecture (i386, x86_64, ...),
# and a list of PLT relocations.
def get_target_info(parsed):
	b_type = type(parsed)
	
	if (b_type == lief.ELF.Binary):
		b_arch = parsed.header.machine_type
		b_relocs = [x for x in parsed.relocations \
			if x.purpose == lief.ELF.RELOCATION_PURPOSES.PLTGOT]
	else:
		print("ERROR: Unsupported target type!")
		exit(0)

	return (b_type, b_arch, b_relocs)


# Returns a Capstone disassembler object based on
# the specified target type and architecture. 
def get_capstone(b_type, b_arch):
	if b_type == lief.ELF.Binary:

		if b_arch == lief.ELF.ARCH.i386:
			cs = Cs(CS_ARCH_X86, CS_MODE_32)
		elif b_arch == lief.ELF.ARCH.x86_64:
			cs = Cs(CS_ARCH_X86, CS_MODE_64)
		else:
			print ("ERROR: Unsupported target arch!")
			exit(0)

	cs.detail = True
	cs.syntax = CS_OPT_SYNTAX_ATT
	return cs
