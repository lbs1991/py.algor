#!/usr/bin/python27

def fib(n):
	a,b = 0,1
	while b < n:
		print b,'   ',
		
		a,b = b,a+b
	print('\n')

def fib2(n):
	l1 = []
	a,b = 0,1
	while b < n :
		l1.append(b)
		a,b = b,a+b
	return l1

if __name__ == '__main__':
	import sys
	fib(int(sys.argv[1]))

