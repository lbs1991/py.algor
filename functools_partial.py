#!/usr/bin/env python27

import functools
int2 = functools.partial(int,base=2)

bin1 = int2('11111111')
print bin1
