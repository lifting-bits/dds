.PHONY: all examples clean

deps = dds/datalog/section.dr \
	   dds/datalog/instruction.dr \
	   dds/datalog/function.dr \
	   dds/datalog/transfer.dr 

all: 
	drlojekyll $(deps) \
	    -py-out dds/datalog/database.py \
	    -py-interface-out dds/datalog/interface.py \
	    -dot-out dds.dot

lief: all
	python3 -m dds.__main__ --binary examples/helloworld/helloworld.elf.x86_64.nopie \
		--binary_parser lief --instruction_decoder capstone --workspace_dir dds_tmp

binja: all
	python3 -m dds.__main__ --binary examples/helloworld/helloworld.elf.x86_64.nopie \
		--binary_parser binja --instruction_decoder capstone --workspace_dir dds_tmp

bdec: all
	python3 -m dds.__main__ --binary examples/helloworld/helloworld.elf.x86_64.nopie \
		--binary_parser lief --instruction_decoder binja --workspace_dir dds_tmp

debug:
	xdot dds.dot

clean:
	rm -rf dds.py
	$(MAKE) clean -C examples
