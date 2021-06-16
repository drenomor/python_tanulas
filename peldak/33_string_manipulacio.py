#!/usr/bin/env python3

# string - karakter lánc
# concatenation - összefűzés
# slicing - szeletelés
# indexing - indexelés
# len() - string hossza, karakterek száma

szoveg = "Két dolog végtelen a világegyetemben, az emberi hülyeség és az univerzum, ... bár az utóbbi nem biztos."
print(szoveg)

# szövegrész cseréje

szoveg = szoveg.replace('világegyetemben', 'világon').replace('emberi', 'állati') # Láncolva is megadhatjuk ha több cserélni való van.
print(szoveg)
szoveg = szoveg + " Az élet értelme 42."  # További szöveget fűzhetünk hozzá.
print(szoveg)

print(szoveg.index("dolog")) # Keresett szöveg első előfordulásának és (első karakterének) helye 0-tól kezdve
print(len(szoveg))
print(szoveg.startswith("Két dol")) # A keresett szöveggel kezdődik-e a string. (Ture | Flase)
print(szoveg.startswith("két"))
print(szoveg.endswith("42.")) # A keresett szöveggel végződik-e a string. (Ture | Flase)

print(szoveg[4:4+5]) # Ismert indextől (karakter sorszámtól) kezdődő szövegrész, plusz egyesével 5 pozició kiiratása.
print(szoveg[-3:]) # A string végéről 3 karakter kiratása.

# fölösleges whitespace-ek levágása, balról, jobbról és mindkét irányból.
szoveg2 = "     Tüskés hátú kígyó bűvölő.      "
print(szoveg2)
print(szoveg2.lstrip())
print(szoveg2.rstrip())
print(szoveg2.strip())

# szöveg szétbontása (lista elemekké) a megadott határoló karakter alapján.
adatok1 = "0,1,2,3,4,5,6,7,8,9"
adatok1 = adatok1.split(",")
print(adatok1)
print(type(adatok1))
print(type(adatok1[0]))

# int lista elemeké alakítjuk a megadott adatok1 szétdarabolt stringet.

for i in range(len(adatok1)):
    adatok1[i] = int(adatok1[i])
print(adatok1)

adatok2 = "padlizsán;paprika;burgonya;répa;paradicsom"
adatok2 = adatok2.split(";")
print(adatok2)
