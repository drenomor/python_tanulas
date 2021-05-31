#!/usr/bin/env python3

def koz(bemenetiszoveg = ''):
    print('-----', bemenetiszoveg, '-----')

# tuple - nem módosítható adathalmaz (immutable)

# módosítható adat []
telepules_0 = ['Homokbödöge', 'Piripócs', 'Kiskunmajsa', 'Závod']

# nem módosíható adat ()
telepules_1 = ('Homokbödöge', 'Piripócs', 'Kiskunmajsa', 'Závod')

koz('Lista módoítás')
telepules_0.append('Mór')
print(telepules_0)
telepules_0[-1] = 'Nagyvázsony'
print(telepules_0)

koz('Tuple módosítás nem lehetséges')
# telepules_1[-1] = 'Tata' # Hiba
koz('Tuple elem kiratása')
print(telepules_1[2])
print(telepules_1[1:2])
print(telepules_1[1:])
