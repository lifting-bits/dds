.PHONY: all examples clean

deps = dds/datalog/section.dr dds/datalog/instruction.dr dds/datalog/function.dr dds/datalog/transfer.dr

all: 
	drlojekyll $(deps) -py-out dds/datalog/__init__.py -dot-out dds.dot
	python3 dds/analyze.py --binary examples/helloworld/helloworld.elf.x86_64.nopie --binary_parser binja

debug:
	xdot dds.dot

clean:
	rm -rf dds.py
	$(MAKE) clean -C examples
