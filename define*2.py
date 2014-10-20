#!/usr/bin/python27

def f1(*x,**y):
	print x
	print y

a=1
b=2
c=3
f1(a,b,c,i='i',j='j')

