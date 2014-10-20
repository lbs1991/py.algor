#!/usr/bin/env python27
import functools
def log(arg):
	if hasattr(arg,'__call__'):
		@functools.wraps(arg)
		def wrapper(*a,**b):
			print 'call %s()' % arg.__name__
			arg(*a,**b)
		return wrapper
	def decor(func):
		@functools.wraps(func)
		def wrapper(*a,**b):
			print '%s %s()' % (arg,func.__name__)
			func(*a,**b)
		return wrapper
s = raw_input()
try:
	i = int(s)
	if i:
		@log
		def now():
			print '2014-9-26'
		now()
	else:
		@log('execute')
		def now():
			print '2014-9-9'
		now()
except:
	raise TypeError,'please enter a number!'



