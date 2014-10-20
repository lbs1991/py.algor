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
	except B:
		print('B')
	except C:
		print('C')
	except D:
		print('D')
		
