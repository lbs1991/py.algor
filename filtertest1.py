#!/usr/bin/python27

def f1(x):
	if x == 'b':
		return True
	else:
		return False
str1=raw_input('enter somethingi>>>')
kk = filter(f1,str1)
type(kk)
print kk
