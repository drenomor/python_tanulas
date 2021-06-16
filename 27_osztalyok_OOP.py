#!/usr/bin/env python3

# classes and the object oriented programming
# osztályok és az objektum orientált programozás

# user defined types
# felhasználó által definiált típusok

class Szemely: # az osztály neve mindig nagy betűvel kezdődjön
    # members variables/fields - tag változó/mezők
    nev = ''
    kor = None
    neme = ''

sz1 = Szemely
sz1.nev = 'Géza'
sz1.kor = 62
sz1.neme = 'férfi'
print(sz1.nev)
print(sz1.kor)
print(sz1.neme)

sz2 = Szemely
sz2.nev = 'Helga'
sz2.kor = 21
sz2.neme = 'nő'
print(sz2.nev)
print(sz2.kor)
print(sz2.neme)
