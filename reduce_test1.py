#!/usr/bin/env python27

def f(x,y):
	return x*10+y

l1 = [1,2,3]
print reduce(f,l1)
print type(reduce(f,l1))
