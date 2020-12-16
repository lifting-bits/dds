.PHONY: all examples clean

#examples:
	#$(MAKE) all -C examples 

all: 
	drlojekyll objdump.dr -py-out objdump.py
	python3 objdump.py examples/hello.elf lief

clean:
	rm -rf objdump.py
	$(MAKE) clean -C examples
