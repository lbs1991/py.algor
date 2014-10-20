#!/usr/bin/python27
def is_str(x):
	return True if isinstance(x,basestring) else False

def is_str2(x):
	try: 	x.lower() + x
	except:	return False
	else:	return True

str1 = 'abcd'
print is_str(str1)
print is_str2(str1)
