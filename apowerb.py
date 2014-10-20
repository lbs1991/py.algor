#!/usr/bin/python27

def f1(x):
	def f2(y):
		return x**y
	return f2
print f1(2)(3)
