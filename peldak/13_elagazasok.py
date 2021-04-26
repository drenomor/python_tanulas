#!/usr/bin/env python3

# elágazások, feltételek - if statement, conditions


elvalaszto = "----------"

if True:
    print('igaz')
print(elvalaszto)

if False:
    print('igaz')
print(elvalaszto)

eletkor = 66

if eletkor < 18:
    print('Se cigi, se pia!')
print(elvalaszto)


if eletkor < 18:
    print('Se cigi, se pia!')
elif eletkor >= 18 and eletkor < 30:
    print('Jó Bulizást!')
elif eletkor > 30 and eletkor < 65:
    print('Munka és család!')
else:
    print('Nyugdíjjas élet, meg unokák!')
print(elvalaszto)
