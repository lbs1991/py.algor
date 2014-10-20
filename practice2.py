#!/usr/bin/python27

import os
strfn = raw_input('enter your file:')
if os.path.isfile(strfn) != True :
	exit('not a file!')

