TARGET = helloworld
CC     = clang
OS    := $(shell uname)

ifeq ($(OS), Linux)
	VERSIONS = elf
endif
ifeq ($(OS), Darwin)
	VERSIONS = macho
endif

all: $(VERSIONS)

# Linux ELF versions
elf: -fPIC
	$(CC) -o $(TARGET).elf.x86_64.pie     $(TARGET).c -O0 -m64 -pie -fPIC
	$(CC) -o $(TARGET).elf.x86_64.nopie   $(TARGET).c -O0 -m64 -fno-pie
	$(CC) -o $(TARGET).elf.x86_32.pie     $(TARGET).c -O0 -m32 -pie -fPIC
	$(CC) -o $(TARGET).elf.x86_32.nopie   $(TARGET).c -O0 -m32 -fno-pie

# MacOS Mach-O versions
macho:
	$(CC) -o $(TARGET).macho.x86_64.pie   $(TARGET).c -O0 -m64 -pie -fPIC
	#$(CC) -o $(TARGET).macho.x86_64.nopie $(TARGET).c -O0 -m64 -fno-pie

clean:
	for vers in $(VERSIONS) ; do \
		rm -rf $(TARGET).$${vers}.* ; \
	done