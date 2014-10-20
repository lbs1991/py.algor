#!/usr/bin/python27

theline = 'abcdefghijklmnopqrstuvwxyz'
cuts = [8,14,20,26,30]
pieces = [ theline[i:j] for i,j in zip([0]+cuts,cuts+[None])]
print pieces
