#!/usr/bin/python27

strfn = '/etc/passwd'
strsc = '/bin/bash'
f1 = open(strfn,'r')
l1 = [ i.split(':')[0] for i in f1.readlines() ]
print l1
