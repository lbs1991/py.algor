#!/usr/bin/python27

import fileinput
for line in fileinput.input("/root/file/passwd",inplace=1):
	line = line.replace("rpc","!!!!!!!!!!!!!!!!")
	print line

