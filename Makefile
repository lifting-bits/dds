.PHONY: all examples clean

all: examples
	drlojekyll objdump.dr -py-out objdump.py
	python3 objdump.py examples/helloworld

examples:
	$(MAKE) all -C examples 

clean:
	rm -rf objdump.py
	$(MAKE) clean -C examples
