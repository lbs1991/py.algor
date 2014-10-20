#!/usr/bin/python27

def f1(*x,**y):
	print x
	print y

t1 = (1,2,3)
d1 = {'a':1,'b':2}
f1(t1,d1)
