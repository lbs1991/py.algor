#!/usr/bin/python27

with open('/root/file/passwd','r+') as f:
	f.seek(3)
	f.truncate(8)


