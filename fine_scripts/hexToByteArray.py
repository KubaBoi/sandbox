#!/bin/python

import sys

hx = sys.argv[1]
ba = bytearray.fromhex(hx)

print(ba)
print("Unsigned: ", end="")
for b in ba:
	print(b, end=",")
print("\nSigned: ", end="")
for b in ba:
	print(b - 128, end=",")

print("\nNVM: ", end="")
for b in ba:
	if (b >= 128):
		b -= 256
	print(b, end=",")