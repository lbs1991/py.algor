#!/usr/bin/python2

import re
text1 ="djhfmn10/15/994678df3fgfder"
text = "10/15/991iuhk"
m = re.search("(\d{2})/(\d{2})/(\d{2,4})",text1)
if m:
	print m.group(2)
	print m.group(0)
