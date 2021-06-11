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

    def set_nev(self, value): # a self az éppen meghívott objektum példányra mutat pl. set_nev(Viktor, value) vagy set_kor(Franciska, value)
        self.nev = value

    def set_neme(self, value):
        self.neme = value

# object instance - objektum példány

Viktor = Szemely()
Viktor.set_kor(21)
Viktor.set_nev('Viktor')
Viktor.set_neme('férfi')
print(Viktor.kor)
print(Viktor.nev)
print(Viktor.neme)

Franciska = Szemely()
Franciska.set_kor(38)
Franciska.set_nev('Franciska')
Franciska.set_neme('Nő')
print(Franciska.kor)
print(Franciska.nev)
print(Franciska.neme)
