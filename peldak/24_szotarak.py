#!/usr/bin/env python3

# Dictionaries, key-value pairs - Szótárak, kulcs-érték  párosok (java hash-maps, javascript object literals)

nev_kor = {'Vednuria':28, 'Hamernolia':37, 'Lameroni':41, 'Kela':34}

for key in nev_kor.keys():
    print(key)

for value in nev_kor.values():
    print(value)

for key, value in nev_kor.items():
    print(key, value)