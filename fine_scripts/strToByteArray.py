#!/bin/python

import sys

str = sys.argv[1]
print(len(str))
strb = bytes(str, "utf-8")

bts = []
for s in strb:
	print(s, end=",")
	bts.append(s)
print("\n", len(bts))
for s in str:
	print(ord(s), end=",")
