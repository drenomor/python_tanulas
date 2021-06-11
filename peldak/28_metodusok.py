#!/usr/bin/env python3

# classes and the object oriented programming
# osztályok és az objektum orientált programozás

# user defined types
# felhasználó által definiált típusok

class Szemely:
    # members variables/fields - tag változó/mezők
    nev = ''
    kor = None
    neme = ''

    # methods - metódusok (osztályban deffiniált függvények)
    # osztályból létrehozot objektumon hajt végre különböző műveleteket vagy operációkat.
    def set_kor(self, value):
        kor = value

# object instance - objektum pledany
# ha metódusokat akarunk használni az osztályon
# akkor az osztály után ki kell rakni a () jeleket.
# sz1 = Szemely
sz1 = Szemely()
sz1.set_kor(21) # így csak a metódusban léterhozott kor változónak állítjuk be az értéket.
print(sz1.kor)