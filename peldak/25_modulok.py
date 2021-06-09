#!/usr/bin/env python3

# modules, namespaces and importing - modulok, néveterek és importálás
# python standard library

from math import sin, cos # csak a cos és sin függvények importálása a math modulból.

print(sin(4))
print(cos(4))

import math # egész modul inportálása
print(math.pi)
print(math.sqrt(8))

from sajat_modulok import* # minden függvényt importálunk a "sajat_modulok.py"-ból
hello()

import sajat_modulok
sajat_modulok.hello()