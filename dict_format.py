#!/usr/bin/python27

dict1 = {'abc':111,'def':222,'rty':333}
proc = 'abc: {0[abc]}\ndef: {0[def]}\nrty: {0[rty]}'
print(proc.format(dict1))
