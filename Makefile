.PHONY: all examples clean

deps = dds/datalog/section.dr \
	   dds/datalog/instruction.dr \
	   dds/datalog/function.dr \
	   dds/datalog/transfer.dr \
	   dds/datalog/variable.dr

all: 
	drlojekyll $(deps) -py-out dds/datalog/__init__.py -dot-out dds.dot

lief: all
	python3 dds/analyze.py --binary examples/helloworld/helloworld.elf.x86_64.nopie \
		--binary_parser lief --instruction_decoder capstone

binja: all
	python3 dds/analyze.py --binary examples/helloworld/helloworld.elf.x86_64.nopie \
		--binary_parser binja --instruction_decoder capstone

bdec: all
	python3 dds/analyze.py --binary examples/helloworld/helloworld.elf.x86_64.nopie \
		--binary_parser lief --instruction_decoder binja

debug:
	xdot dds.dot

clean:
	rm -rf dds.py
	$(MAKE) clean -C examples
