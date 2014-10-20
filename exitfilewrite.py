#!/usr/bin/python27

import os
fn = '/root/test'
if os.path.isfile(fn):
	f1 = open(fn,'a+')
	input = raw_input('please input some:')
	while input != 'q' and input != 'Q' :
		f1.write(input+'\n')
		input = raw_input('please input some:')
f1.flush()
f1.close()
