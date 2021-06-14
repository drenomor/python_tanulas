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

# object instance - objektum példány