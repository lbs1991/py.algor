#!/usr/bin/env python27

def clo(*args):
	def sum():
		s = 0
		for i in args:
			s += i
		return s	
	return sum

f1 = clo(1,2,3)
print f1()
