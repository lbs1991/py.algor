#!/usr/bin/env python27
import functools
def log_1(text):
	def deco(func):
		@functools.wraps(func)
		def wrapper(*a,**b):
			print '%s' % text
			print 'call %s()' % func.__name__
			return func(*a,**b)
		return wrapper
	return deco

def log_2(text):
	def deco(func):
		@functools.wraps(func)
		def wrapper(*a,**b):
			return func(*a,**b)
			print '%s' % text
		return wrapper
l1 = ['begin call','after call']


@log_1(l1[0])
def now():
	print '2014-9-25'
@log_2(l1[1])

now()
