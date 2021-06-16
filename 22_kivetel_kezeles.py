#!/usr/bin/env python3

# exception handling (error handling) - kivétel kezelés (hibakezelés)
def koz(bemenetiszoveg = ''):
    print('-----', bemenetiszoveg, '-----')

lista = [4,6,8,9]

try:
    print(duma)
except NameError as e:
    print(e, '- Nem létező válzotó!')
try:
    print(lista[9])
except IndexError as e:
    print(e, '- Tartományon kívüli index!')
try:
    print(1/0)
except ZeroDivisionError as e:
    print(e, '- Nullával való osztás!')

print('A program vége!')
koz()

lista_2 = ['1', '2', '3', None, '4', '', '5', True, 'Bözsi', '12.64']

for i in lista_2:
    try:
        print(int(i)*2)
    except:
        #print('Nem végrehajtható a művelet!')
        continue

koz('Except fut le!')
try:
    print(Bla)
except:     # Ha a try ág nem tud lefutni akkor az except ág fut le.
    print('Nem létező változó!')
else:       # Az else ág akkor fut le ha a try ág sikeresen lefutott.
    print('Az else ág!')
finally:    # A finally ág mindenképpen lefut ha a try vagy az except ág lefutott.
    print('Try vége!')

koz('Try fut le!')
try:
    print('Bla')
except:     # Ha a try ág nem tud lefutni akkor az except ág fut le.
    print('Nem létező változó!')
else:       # Az else ág akkor fut le ha a try ág sikeresen lefutott.
    print('Az else ág!')
finally:    # A finally ág mindenképpen lefut ha a try vagy az except ág lefutott.
    print('Try vége!')