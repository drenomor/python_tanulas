#!/usr/bin/env python3

def elvalaszto(szoveg = ''):
    print('-----', szoveg, '-----')

elvalaszto('1')
# fájl olvasás

file = open('peldak/kozmondasok.txt', 'r', encoding='utf-8')
sor = file.readline()
print(sor.strip())
sor = file.readline()
print(sor.strip())
sor = file.readline()
print(sor.strip())
sor = file.readline()
print(sor.strip())

# print(file)

file.close()

elvalaszto('2')

file2 = open('peldak/kozmondasok.txt', 'r', encoding='utf-8')

for sor in file2:
    print(sor.strip())
    
file2.close()

elvalaszto('3')

file3 = open('peldak/kozmondasok.txt', 'r', encoding='utf-8')
sor = file3.readline()

while sor:
    print(sor.strip())
    sor = file3.readline()

file3.close()

elvalaszto('4')

# Autómatikusan lezárja a file-t.
with open('peldak/kozmondasok.txt', 'r', encoding='utf-8') as file4:
    for sor in file4:
        print(sor.strip())

elvalaszto('5')

with open('peldak/kozmondasok.txt', 'r', encoding='utf-8') as file5:
    #sor = file5.readline()
    sorok = file5.readlines()
    print(sorok)

    # while sor:
    #     print(sor.strip())
    #     sor = file5.readline()

elvalaszto('6')

with open('peldak/kozmondasok.txt', 'r', encoding='utf-8') as file6:
    sor = file6.read() # Az egész szöveget beolvassa a fájlból. Több soros fájl (mondjuk kb több mint 5000 sor) esetén sok memóriát eszik. Ezért érdemesebb a readline()-t használni.
    print(sor)