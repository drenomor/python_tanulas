#!/usr/bin/env python3

# variable scope - Változók láthatósága és élettartama - lokális és globális változók

# function scope, module scope, class scope


# module scope

a = 78
b = 47

# function scope

def teszt():
    print('----- teszt fgv -----')
    a = 12
    b = 15
    print(a, b)

teszt()
print(a, b)

def teszt():
    print('----- teszt fgv globális változók használatávalval -----')
    global a, b
    a = 12
    b = 15
    print(a, b)

teszt()
print(a, b)

# for && és while ciklusban létrehozott változók globálisan látszódnak

def teszt2():
    print('----- teszt2 fgv for ciklus -----')
    for i in range(5):
        b = 54
        pass
    print(i)
    print(b)

teszt2()

print('----- if kondíció -----')
if True:
    c = 78
print(c)

def teszt3():
    print('----- if kondíció -----')
    if True:
        d = 78
print(d)