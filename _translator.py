#!/usr/bin/python27

import string
def translator(fm='',to='',delete='',keep=None):
	if len(to) == 1 :
		to = to * len(fm)
	trans = string.maketrans(fm,to)
	if keep != None :
		delete = trans.translate(trans,keep.translate(trans,delete))
	def translate(x):
		return x.translate(trans,delete)
	return translate
