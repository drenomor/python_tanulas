#!/usr/bin/env python3

# exception handling (error handling) - kivétel kezelés (hibakezelés)
lista = [4,6,8,9]

try:
    #print(duma)
    #print(lista[9])
    print(1/0)
except NameError as e:
    print(e)
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

print('A program vége!')
