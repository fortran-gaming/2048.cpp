#!/usr/bin/env python3
"""
cross-platform means to test executable with stdin

expects executable path as first argument and arguments for stdin as second argument (quoted)

"""
import subprocess
import sys
import shutil

exe = shutil.which(sys.argv[1])
if not exe:
    print("executable", sys.argv[1], "not found.", file=sys.stderr)
    raise SystemExit(77)

ret = subprocess.run([exe], input=sys.argv[2], universal_newlines=True)
if ret.returncode:
    raise SystemExit(ret.stderr)
