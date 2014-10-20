#!/usr/bin/env python27

def func(*a,**b):
	for i in b.iterkeys():
		print i

d1 = {'a':97,'b':98,'c':99}
func(**d1)
