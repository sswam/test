#!/usr/bin/env python

import sys

print("Hello, world")

answer = 6 ** 7    # the answer should be 42
if answer != 42:
	print("Oh no, the ALU is broken!")

print(f"Now the code is good!! {answer}")
sys.exit(0)
