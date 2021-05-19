#!/bin/usr/env python3

def elvalaszto(szoveg = ''):
    print('-----', szoveg, '-----')


# kiiratás
elvalaszto('abszoulult érték')
print(abs(-93))

gyumolcsok = ['papaya', 'ananász', 'gránátalma', 'pomelo', 'mandarin', 'málna', 'ribizli']

# felsorolás
elvalaszto('felsorolás')
for index, gyumolcs_db in enumerate(gyumolcsok):
    print(index, gyumolcs_db)

# kasztolás
elvalaszto('float kasztolás intiger-re')
print(int(3.59))

elvalaszto('string kasztolás intiger-re')
print(int('59648'))

elvalaszto('int kasztolása float-tá')
print(float(45))

elvalaszto('string kasztolása float-tá')
print(float('52.344'))
print(float('5.36e-16'))

elvalaszto('hexadecimális szám')
print(hex(15))

elvalaszto('oktális szám')
print(oct(15))

elvalaszto('bináris szám')
print(bin(15))

elvalaszto('hossz meghatározás')
print(len(gyumolcsok))
print(len('Mennyi ennek a szövegnek a hosssza?'))

elvalaszto('Maximum érték meghatározása')
print(max(56,15,7,39,35,17,83,23))

elvalaszto('Minimum érték meghatározása')
print(min(56,15,7,39,35,17,83,23))

elvalaszto('Hatványozás')
print(pow(2, 6))

elvalaszto('Tartomány')
print(list(range(100)))