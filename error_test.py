#!/usr/bin/python27

def divideby():
	return 1/0

try:
	divideby()
except ZeroDivisionError as err:
	print('bad happening ' , err)
