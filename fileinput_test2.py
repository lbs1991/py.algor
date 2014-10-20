#!/usr/bin/python27
#inplace=1 means replace,=0 means print not replace
import fileinput
for line in fileinput.input("/root/file/passwd",inplace=0):
	line = line.replace("!!!!!!!!!!!!!!!!","##########")
	print line

