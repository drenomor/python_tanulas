#!/usr/bin/env python3

# classes and the object oriented programming
# osztályok és az objektum orientált programozás

# user defined types
# felhasználó által definiált típusok

# az __init__ metódus, más programozási nyelvekben ez a konstruktor metódus

class Szemely:
    # __init__ metódust az osztály példány kezdeti értékek megadásakor kell létrehozni.
    def __init__(self, nev, kor, neme, nemzetiseg, vallas='Taoista'):
        self.nev = nev
        self.kor = kor
        self.neme = neme
        self.nemzetiseg = nemzetiseg
        self.vallas = vallas
        self.hello() # minden egyes obejktum példánynál meghívódik a hello() metódus.

    def hello(self):
        print('Szia ' + self.nev)

class Alkalmazott(Szemely): # Az Alkalmazott örökli a Szemely összes tulajdonságát. A Szemely Super osztálya az Alkalmazottnak.
    def __init__(self, nev, kor, neme, nemzetiseg, vallas, tapasztalat, megbizhatosag, vegzettseg):
        super().__init__(nev, kor, neme, nemzetiseg, vallas)
        self.tapasztalat = tapasztalat
        self.megbizhatosag = megbizhatosag
        self.vegzettseg = vegzettseg

# object instance - objektum példány

Nandor = Alkalmazott('Nándor', 25, 'Férfi', 'Magyar', 'pogány', 4, 8, 'Könyvelő')
Erzsebet = Alkalmazott('Erzsébet', 36, 'Nő', 'Magyar', 'hindu', 12, 7.5, 'nano technológus')

print(Nandor.nev)
print(Nandor.vegzettseg)
print(Nandor.vallas)

print(Erzsebet.nev)
print(Erzsebet.vegzettseg)
print(Erzsebet.vallas)
