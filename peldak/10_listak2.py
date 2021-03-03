#!/usr/bin/env python3

lista1 = ['Dwalin','Balin','Kili','Fili','Dori','Nori','Ori','Oin','Gloin','Bifur','Bofur','Bombur','Thorin']

print(lista1)

# indexelés
## lista1 0-dik eleme (kezdő eleme)
print(lista1[0])

# Szeletelés
## lista[0:2] (kezdő indextől, két elem kiírása)
##               0       1       2      3      4     5      6    7       8       9       10      11      12
## lista1 = ['Dwalin','Balin','Kili','Fili','Dori','Nori','Ori','Oin','Gloin','Bifur','Bofur','Bombur','Thorin']
print(lista1[0:2])

## Adott indextől a végéig
print(lista1[4:])

## utolsó elem
print(lista1[-1])

# Több dimenziós listák
##          0         1         2         3
lista2 = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
## 4 * 3 -as lista (tömb)
## 4 sor * 3 elem lista (tömb)

## 3. sor összes eleme (0-tól kezdődik a sor)
print(lista2[2])

## 4. sor 1. eleme (0-tól kezdődik a sor / elem számozás)
print(lista2[3][0])

# tartomány
tartomany = range(100)
print(list(tartomany))
