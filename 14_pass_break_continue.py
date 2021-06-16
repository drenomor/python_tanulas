#!/usr/bin/env python3

# pass, continue és break kulcsszavak

# while True:
#     pass # Helyettesítő szöveg

for i in range(10):
    if i == 5:
        break # ciklus megszakítása
    print(i)

szam = 0
print()
while True:
    print(szam)
    szam += 1
    if szam == 5:
        break # ciklus megszakítás

print()
for i in range(10):
    if i == 5:
        continue # nem hajtja végre az aktuális ciklusmag értéket hanem folytatja a következővel (átugorja).
    print(i)

print()

szamlalo = 0

while True:
    szamlalo += 1
    if szamlalo % 2 == 0:
        continue
    print(szamlalo)
    if szamlalo > 20:
        break
