#!/usr/bin/env python3

a = 10 
b = 20

# paramérter nélküli függvény
def osszeadas_1(): 
    print(a + b) # nincs visszatérési érték

def osszeadas_2(a, b, c=6): # alapértelemezett értéket is megadhatunk.
    return a + b + c

def osszeadas_3(*tobb_adat): # változó számú paraméterek megadása a * és valamilyen változó név megadásával történik.
    return sum(tobb_adat)

def udvozlesek(*args):
    koszones = 'Ennyi féle köszönés létezik: '
    for k in args:
        koszones += k
        koszones += ', '
    print(koszones[0:len(koszones) - 2])

udvozlesek('Szia', 'Csá', 'Helló', 'Szervusz', 'Hi')
    
osszeadas_1()

osszeg = osszeadas_2(31, 3)

print(osszeg)

print(osszeadas_3(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))