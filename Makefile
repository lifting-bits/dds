.PHONY: all examples clean

#examples:
	#$(MAKE) all -C examples 

deps = datalog/section.dr datalog/instruction.dr datalog/function.dr datalog/transfer.dr

all: 
	drlojekyll $(deps) -py-out dds.py -dot-out dds.dot
	python3 __main__.py examples/hello.elf lief

debug:
	xdot dds.dot

clean:
	rm -rf dds.py
	$(MAKE) clean -C examples
