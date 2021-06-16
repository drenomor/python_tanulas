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
print(sajat_modulok.szin)
print(sajat_modulok.nevek)

import Tester.sajat_modulok2
Tester.sajat_modulok2.hello()

import Tester.sajat_modulok2 as egyeni_elnevezes # egyéni aliast (álnevet) adhatunk az importált modulnak.
egyeni_elnevezes.hello() # az alias nevével hivatkozhatunk rá.

from sajat_modulok import Osztaly

o = Osztaly()

"""
Hiába importáljuk a "sajat_modulok"-ból a hello() fgv
a következő sorban a fő modulban át definiáljuk azt
így ezt hívjuk meg a hello()-val.
"""

def hello():
    print('Üdvözlés a fő modulból!"')

hello()

"""
Itt újból beimportáljuk a "sajat_modulok"-at
és hivatkozunk a benne lévő hello() fgv-re.
"""
import sajat_modulok

sajat_modulok.hello()