#!/usr/bin/python27

def CrossProduct(seq1,seq2):
	if not seq1 or not seq2:
		raise ValueError,"sequence arguments must be non-empty"
	return [(x1,x2) for x1 in seq1 for x2 in seq2]

seq1=[]
seq2=[]
CrossProduct(seq1,seq2)
