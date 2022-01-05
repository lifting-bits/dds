# Diagnosing Disassembly with Dr. Disassembler

This repository contains a prototype of using Datalog for disassembly, described
in [this blog post](Toward%20a%20Best-of-Both-Worlds%20Binary%20Disassembler.pdf).
This disassembler takes a portfolio approach to disassembly: it supports
multiple binary parser frontends, and multiple instruction decoder frontends.

The core of the disassembly algorithm is implemented in Datalog, which is
compiled to Python. We have included the auto-generated code in here. This
prototype does not scale well to large binaries as Python is very slow.

## Installation

```shell
pip3 install --index-url https://lief.quarkslab.com/packages lief==0.11.0.dev0
python3 setup.py install
```

## Usage guide

### Changing the binary parser

Dr. Disassembler (DDS) allows one to switch out the binary parser that is used.
DDS supports three binary parsers: LIEF, Binary Ninja, and IDA Pro.

#### LIEF

```shell
python3 -m dds.__main__ --binary examples/helloworld/helloworld.elf.x86_64.nopie \
    --binary_parser lief --instruction_decoder capstone --workspace_dir dds_tmp
```

#### Binary Ninja

```shell
python3 -m dds.__main__ --binary examples/helloworld/helloworld.elf.x86_64.nopie \
    --binary_parser binja --instruction_decoder capstone --workspace_dir dds_tmp
```

#### IDA Pro

```shell
python3 -m dds.__main__ --binary examples/helloworld/helloworld.elf.x86_64.nopie \
    --binary_parser ida --ida_path /Users/$USER/Applications/IDA\ Pro\ 7.5/idabin/idat64 \
    --instruction_decoder capstone --workspace_dir dds_tmp

```

Note that `--ida_stdout_path` and `--ida_stderr_path` are also supported.

### Changing the instruction decoder

The instruction decoder can also be changed, by changing `--instruction_decoder`.
For example, if you are using `--binary_parser binja`, then you should probably
also use `--instruction_decoder binja`.
