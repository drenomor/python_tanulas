#!/usr/bin/env python3

jelszo = 'setecastronomy'

bemenet = input('\nKérem a jelszót : ')
proba = 0

while bemenet != jelszo:
    proba += 1
    if proba == 3:
        print('Hibásan adtad meg! Nem probálkozhatsz többször!')
        break
    print('\nHibásan adtad meg! Próbáld újra. Még', 3 - proba,'lehetőséged van!')
    bemenet = input('\nKérem a jelszót : ')

if bemenet == jelszo:
    print('\nSikeres belépés!\nÜdvözöllek!\nHosszú eredményes életet!')
