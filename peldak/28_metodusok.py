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
        self.kor = value # a self.kor -ral már az objektumon tudjuk beállítani a lentebb beírt értéket

    def set_nev(self, value):
        self.nev = value

    def set_neme(self, value):
        self.neme = value

sz1 = Szemely()
sz1.set_kor(21)
sz1.set_nev('Viktor')
sz1.set_neme('férfi')
print(sz1.kor)
print(sz1.nev)
print(sz1.neme)
