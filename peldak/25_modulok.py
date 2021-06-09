#!/usr/bin/env python3

# modules, namespaces and importing - modulok, néveterek és importálás
# python standard library

import math # egész modul inportálása
print(math.pi)
print(math.sqrt(8))

from math import sin, cos # csak a cos és sin függvények importálása a math modulból.

print(sin(4))
print(cos(4))