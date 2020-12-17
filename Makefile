.PHONY: all examples clean

#examples:
	#$(MAKE) all -C examples 

all: 
	drlojekyll dds.dr -py-out dds.py -dot-out dds.dot
	python3 __main__.py examples/hello.elf lief

debug:
	xdot dds.dot

clean:
	rm -rf dds.py
	$(MAKE) clean -C examples
