#!/usr/bin/python27

while True:
	try:
		x = int(raw_input("enter:"))
		print "here"
		break
	except ValueError as err:
		print("please try again:")
	except (RuntimeError,TypeError,NameError):
		print("main error happen")
	except :
		print("unkown errorhappen")
