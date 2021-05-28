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
