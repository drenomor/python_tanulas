#!/usr/bin/env python3

# Dictionaries, key-value pairs - Szótárak, kulcs-érték  párosok (java hash-maps, javascript object literals)

from typing import ItemsView


nev_kor = {'Vednuria':28, 'Hamernolia':37, 'Lameroni':41, 'Klea':34}

for key in nev_kor.keys():
    print(key)

for value in nev_kor.values():
    print(value)

for key, value in nev_kor.items():
    print(key, value)

dict_01 = {'adat1':[1,2,3,4,5,6], 'adat2':23, 'adat3':(4,1,6,2)}

nev_kor['Mondaria'] = 56
print(nev_kor)

nev_kor.pop('Klea')
print(nev_kor)

print(nev_kor.get('Vednuria'))

zoldseg_gyumolcs = {'Körte':{'Méret':3, 'Szín':'sárga'},
                    'Alma':{'Méret':3, 'Szín':'piros'},
                    'Barack':{'Méret':2, 'Szín':'sárga'},
                    'Ribizli':{'Méret':1, 'Szín':'fehér'}}
                    
fokok = {0:'Kelet',
        45:'Észak-Kelet',
        90:'Észak',
        135:'Észak-nyugat',
        180:'Nyugat',
        225:'Dél-nyugat',
        270:'Dél',
        315:'Dél-kelet'}

for kulcsok, ertekek in zoldseg_gyumolcs.items():
    print(kulcsok, ertekek)
for kulcsok, ertekek in fokok.items():
    print(kulcsok, ertekek)
