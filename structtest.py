#!/usr/bin/python27

import struct

t1=(1,2,3)
print repr(apply(struct.pack,("!ihb",)+t1))
print repr(apply(struct.pack,("ihb",)+t1))
