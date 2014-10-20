#!/usr/bin/env python27

def _private1(name):
	print 'hi, %s'%name

def _private2(name):
	print 'hello,%s'%name

def greeting(name):
	if len(name) > 3:
		_private1(name)
	else:
		_private2(name)

name = 'lbs'
greeting(name)
