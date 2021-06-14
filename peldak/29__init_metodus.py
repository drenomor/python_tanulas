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

    def hello(self):
        print('Szia ' + self.nev)

# object instance - objektum példány
Klea = Szemely('Klea', 32, 'nő', 'Magyar', 'Görög katolikus')
Leonard = Szemely('Leonard', 33, 'férfi', 'Francia')

print(Klea.vallas)
print(Leonard.vallas)

Klea.hello()
Leonard.hello()

print(type(Klea))
print(type(Leonard))
