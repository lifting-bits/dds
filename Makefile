.PHONY: all examples clean

deps = datalog/section.dr datalog/instruction.dr datalog/function.dr datalog/transfer.dr

all: 
	drlojekyll $(deps) -py-out dds.py -dot-out dds.dot
	python3 __main__.py examples/helloworld/helloworld.elf.x86_64.pie lief

debug:
	xdot dds.dot

clean:
	rm -rf dds.py
	$(MAKE) clean -C examples
