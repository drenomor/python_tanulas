#!/usr/bin/env python3

def koz(bemenetiszoveg = ''):
    print('\n-----', bemenetiszoveg, '-----\n')

# tuple - nem módosítható adathalmaz (immutable)
# Műveleteket sokkal gyorsabban eltudja végezni mint [list] adat halmazon.

# list - módosítható adat []
telepules_0 = ['Homokbödöge', 'Piripócs', 'Kiskunmajsa', 'Závod']

# tuple - nem módosíható adat ()
telepules_1 = ('Homokbödöge', 'Piripócs', 'Kiskunmajsa', 'Závod', 'Nagyvázsony', 'Nagyvázsony')


koz('Lista végéhez hozzáfűzés')
telepules_0.append('Mór')
print(telepules_0)
koz('Lista utolsó elemének módoítása')
telepules_0[-1] = 'Nagyvázsony'
print(telepules_0)

koz('Tuple módosítás nem lehetséges')
# telepules_1[-1] = 'Tata' # Hiba
koz('Tuple elem kiratása')
print(telepules_1[2])
print(telepules_1[1:2])
print(telepules_1[1:])

koz('Lista tuple-é konvertálása')
tup2 = tuple(telepules_0)
print(type(tup2))
print(tup2)

koz('Tuple objektum listává konvertálása')
lista2 = list(tup2)
print(type(lista2))
print(lista2)

koz('Ismert értékű elem indexének kiratása')
print(telepules_1.index('Piripócs'))

koz('Ismert értékű elem mennyiszer fordul elő a tuple-ben')
print(telepules_1.count('Nagyvázsony'))

koz('Tuple egyetlen módon módosítható ha új értéket rendelünk hozzá a program kódban')
telepules_1 = ('Homokbödöge', 'Piripócs', 'Kiskunmajsa', 'Závod', 'Nagyvázsony')
print(telepules_1)

koz('Ha a tuple csak egyetlen elemet tartalmaz, utánna vesszőt kell tenni mert stringnek értelmezi a program.')
tup2 = ('Barack')
print(tup2)
tup2 = ('Barack',)
print(tup2)
