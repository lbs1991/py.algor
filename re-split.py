#!/usr/bin/python27

import re
text = 'abc def  ghk'
m = re.split(r'(\s+)',text)
print m
n = re.split(r'\s+',text)
print n
m.reverse()
n = reversed(n)
s = ''.join(m)
print s
s = ''.join(n)
print s
