#!/bin/python
import os
import sys
import pyperclip

if (len(sys.argv) < 2):
	print("ERROR: syntax: cpy file")
	exit()

file = sys.argv[1]
if (not os.path.exists(file)):
	print("ERROR: File not found")
	exit()

with open(file, "r", encoding="utf-8") as f:
	pyperclip.copy(f.read())
