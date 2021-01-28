#!/usr/bin/env python3
# Copyright 2020, Trail of Bits. All rights reserved.

import argparse
import hashlib
import os
import pickle
import shutil
import subprocess
import sys
from typing import Final, List, Optional, Sequence, Union

try:
    from shlex import quote
except:
    from pipes import quote

# TODO(pag): I don't understand Python packaging, but this makes it work under
#            PyCharm's venv, and a `setup.py` install, and when executed within
#            an IDA Pro subprocess.
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from dds.datalog import \
    Database, \
    DatabaseFunctors, \
    DatabaseLog

from dds.arch import \
    ArchName, \
    arch_from_string, \
    decoder_from_string

from dds.binary import \
    binary_parser_from_string, \
    BinaryParser

from dds.analyze import BinaryMetadataImporter


def debug(message, *args):
    # print(message.format(*args), file=sys.stderr)
    pass


def _argv() -> Sequence[str]:
    try:
        import idc
        return idc.ARGV
    except:
        return sys.argv


def _exit(code: int):
    try:
        import idc
        idc.process_config_line("ABANDON_DATABASE=YES")
        idc.qexit(code)
    except:
        sys.exit(code)


def parse_binary(args, arch: ArchName) -> Optional[BinaryParser]:
    """Parse the binary at `path` with the binary parser named by
    `parser_name`."""
    parser = binary_parser_from_string(args.binary_parser)
    if not parser:
        raise Exception("Unhandled binary parser type '{}'".format(
            args.binary_parser))

    binary = parser(arch, args.os, args.binary)
    if not binary:
        raise Exception("Invalid or unrecognized file format")

    return binary


def run_under_ida(parser, args) -> int:
    """Re-run this program under the control of IDA Pro. This will give us
    access to IDA Pro's APIs."""

    ida_path = os.path.dirname(args.ida_path)

    env = {}
    env["IDALOG"] = os.devnull
    env["TVHEADLESS"] = "1"
    env["HOME"] = os.path.expanduser('~')
    env["IDA_PATH"] = ida_path

    # path: List[str] = [ida_path]
    # if "PYTHONPATH" in os.environ:
    #     path.extend(os.environ["PYTHONPATH"].split(os.pathsep))
    # path.extend(sys.path)
    # #
    # env["PYTHONPATH"] = os.pathsep.join(path)

    if "SystemRoot" in os.environ:
        env["SystemRoot"] = os.environ["SystemRoot"]

    stdout_path = os.path.join(args.workspace_dir, "stdout")
    stderr_path = os.path.join(args.workspace_dir, "stdout")

    script_cmd = []
    script_cmd.append(os.path.abspath(__file__))
    script_cmd.append("--binary")
    script_cmd.append(os.path.abspath(args.binary))
    script_cmd.append("--binary_parser")
    script_cmd.append(args.binary_parser)
    script_cmd.append("--instruction_decoder")
    script_cmd.append(args.instruction_decoder)
    script_cmd.append("--arch")
    script_cmd.append(args.arch)
    script_cmd.append("--os")
    script_cmd.append(args.os)
    script_cmd.append("--workspace_dir")
    script_cmd.append(args.workspace_dir)
    script_cmd.append("--ida_stdout_path")
    script_cmd.append(stdout_path)
    script_cmd.append("--ida_stderr_path")
    script_cmd.append(stderr_path)
    script_cmd.append("--ida_sys_path")
    script_cmd.append(pickle.dumps(sys.path).hex())

    cmd: List[str] = []
    cmd.append(quote(args.ida_path))  # Path to IDA.
    cmd.append("-B")  # Batch mode.
    cmd.append("-S\"{}\"".format(" ".join(script_cmd)))
    cmd.append(quote(os.path.abspath(args.binary)))
    ret: int
    try:
        # print(" ".join(cmd))
        # print()
        with open(os.devnull, "w") as devnull:
            ret = subprocess.check_call(
                " ".join(cmd),
                env=env,
                stdin=None,
                stdout=devnull,  # Necessary.
                stderr=devnull,  # Necessary.
                shell=True)  # Necessary.

    except Exception as e:
        parser.error("Error executing under the control of IDA Pro: {}".format(
            str(e)))
        ret = 1

    try:
        with open(stderr_path, "r") as ida_stderr:
            sys.stderr.write(ida_stderr.read())
        sys.stderr.flush()
        os.unlink(stderr_path)
    except:
        pass

    try:
        with open(stdout_path, "r") as ida_stdout:
            sys.stdout.write(ida_stdout.read())
        os.unlink(stdout_path)
    except:
        pass

    return ret


def setup_workspace(parser, args):
    """Setup the solypsis workspace directory."""
    if not os.path.isdir(args.workspace_dir):
        try:
            os.makedirs(args.workspace_dir, 0o777)
        except OSError as e:
            parser.error("Unable to create workspace directory '{}': {}".format(
                args.workspace_dir, str(e)))

    args.workspace_dir = os.path.abspath(args.workspace_dir)


def copy_binary_into_workspace(args):
    """IDA Pro has issues when opening files in directories in which the
    user does not have write access, e.g. `/bin/ls` often cannot be opened
    directly because IDA Pro will want to create a `/bin/ls.i64` file."""
    with open(args.binary, "rb") as binary_file:
        sha1_hash = hashlib.sha1(binary_file.read())

    temp_bin_path = os.path.join(args.workspace_dir, sha1_hash.hexdigest())
    if not os.path.isfile(temp_bin_path):
        try:
            os.link(args.binary, temp_bin_path)
        except:
            shutil.copyfile(args.binary, temp_bin_path)

    args.binary = temp_bin_path


def main(argv: Optional[Sequence[str]] = None):
    """Disassemble a binary."""
    if argv is None:
        argv = _argv()

    parser = argparse.ArgumentParser(
        prog=argv[0], description="Dr. Disassembler's binary analyzer")
    parser.add_argument("--binary", type=str, required=True,
                        help="Path to the binary to analyze.")

    parser.add_argument(
        "--binary_parser", type=str, default="lief",
        help="Which binary parser to use.",
        choices=("lief", "binja", "ida",))

    parser.add_argument(
        "--instruction_decoder", type=str, default="capstone",
        help="Instruction instruction used by the binary",
        choices=("capstone", "binja", "ida",))

    parser.add_argument(
        "--ida_path", type=str, default="",
        help="Path to IDA Pro 7's `idat` or `idat64` binary.")

    parser.add_argument(
        "--arch", type=str, default="amd64",
        help="Architecture of the instructions of the binary.",
        choices=("x86", "x86_avx", "x86_avx512",
                 "amd64", "amd64_avx", "amd64_avx512",
                 "aarch32", "aarch64",
                 "sparc32", "sparc64"))

    parser.add_argument(
        "--os", type=str, default="linux",
        help="Operating system on which this binary is expected to execute.",
        choices=("linux", "macos", "windows", "solaris"))

    parser.add_argument(
        "--workspace_dir", type=str, default="", required=True,
        help="Path to a workspace directory where temporary files will be "
             "stored.")

    parser.add_argument(
        "--ida_stdout_path", type=str, default="", help=argparse.SUPPRESS)

    parser.add_argument(
        "--ida_stderr_path", type=str, default="", help=argparse.SUPPRESS)

    parser.add_argument(
        "--ida_sys_path", type=str, default="", help=argparse.SUPPRESS)

    args = parser.parse_args(argv[1:])

    setup_workspace(parser, args)

    # We want to run under IDA Pro's Python interpreter.
    if args.ida_path:
        copy_binary_into_workspace(args)
        return run_under_ida(parser, args)

    # Here we assume we have already copied the binary into the workspace.
    elif args.ida_stdout_path and args.ida_stderr_path and args.ida_sys_path:
        sys.stdout = open(args.ida_stdout_path, "w+")
        sys.stderr = open(args.ida_stderr_path, "w+")

        # Super evil >:-) Try to pull out IDA's main python directories.
        paths = []
        old_paths = []
        for i, p in enumerate(sys.path):
            if "ida" in p.lower() and i < 10:
                paths.append(p)
            else:
                old_paths.append(p)

        # Now add in the `sys.path` of the parent process.
        paths.extend(pickle.loads(bytes.fromhex(args.ida_sys_path)))

        # Now add in the old paths that IDA had.
        paths.extend(old_paths)

        sys.path.clear()
        sys.path.extend(paths)
    else:
        copy_binary_into_workspace(args)

    arch = arch_from_string(args.arch)

    binary: Optional[BinaryParser]
    try:
        binary = parse_binary(args, arch)
    except Exception as e:
        parser.error("Error parsing file '{}': {}".format(args.binary, str(e)))
        return 1

    functors = DatabaseFunctors()
    log = DatabaseLog()
    db = Database(log, functors)

    decoder = decoder_from_string(args.instruction_decoder, arch)
    visitor = BinaryMetadataImporter(decoder)
    binary.visit_metadata(visitor)

    metadata = visitor.produce()
    if metadata is not None:
        metadata.apply(db)

    for f in sorted(db.function_f()):
        print("Function {:x}".format(f))
        for i in sorted(db.function_instruction_bf(f)):
            print("  {:x}".format(i))
        print()

    return 0


# Main function.
if __name__ == "__main__":
    _exit(main(_argv()))
