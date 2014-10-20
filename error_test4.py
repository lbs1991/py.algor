#!/usr/bin/python27

class B(Exception):
	pass
class C(B):
	pass
class D(C):
	pass

for err_ in [B,C,D]:
	try:
		raise err_()
	except D:
		print('D')
	except C:
		print('C')
	except B:
		print('B')
		
