#!/usr/bin/env python3

# "is" "is not" Identity Operator - Azonossági operátor

from sajat_modulok import separator

szam1 = 4
szam2 = 5

print(szam1 == szam2)
separator()
szam = 8

if type(szam) is int: # int típusú-e a "szam" változó.
    print("Int típus!")

if type(szam) is not str:
    print("Nem string típus!")

separator()
igaz = True
print(type(igaz) is bool)

separator()
class Szemely:
    pass


sz1 = Szemely()
sz2 = Szemely()

if type(sz1) is Szemely:
    print("Szemely típus!")
else:
    print(type(sz1))

separator()

print("'sz1' ugyanaz az objektum mint 'sz2' :", sz1 is sz2) # sz1 ugyanaz az objektum-e mint az sz2? Ha így írnánk akkor lenne igaz "sz1 = sz2"
print("'sz1' nem ugyanaz az objektum mint 'sz2' :", sz1 is not sz2)

separator()
if isinstance(sz1, Szemely):
    print("Szemely típus!")
