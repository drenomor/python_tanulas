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

print('Életkor:', eletkor)

if eletkor < 18:
    print('Se cigi, se pia!')
elif eletkor >= 18 and eletkor < 30:
    print('Jó Bulizást!')
elif eletkor > 30 and eletkor < 65:
    print('Munka és család!')
else:
    print('Nyugdíjjas élet, meg unokák!')
print(elvalaszto)

# feltételek egymásba ágyazása

eletkor = 15
print('Életkor:', eletkor)
if eletkor < 18:
    if eletkor >= 16:
        print ('Egy kis sört megihatsz.')
    else:
        print('Se cigi, se pia!')
elif eletkor >= 18 and eletkor < 30:
    print('Jó Bulizást!')
elif eletkor > 30 and eletkor < 65:
    print('Munka és Család.')
else:
    print('Nyugdíjjas élet, meg unokák')
print(elvalaszto)
