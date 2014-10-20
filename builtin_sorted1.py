#!/usr/bin/python27

def cmp_ign_case(a,b):
	ch1 = a.lower()
	ch2 = b.lower()
	if ch1 < ch2:
		return -1
	elif ch1 == ch2:
		return 0 
	else:
		return 1
l1 = []
while True:
	st1 = raw_input("enter:")
	if st1 == 'q' or st1 == 'Q':
		break
	l1.append(st1)	
print sorted(l1,cmp_ign_case)
print type(sorted(l1,cmp_ign_case))
