#!/usr/bin/env python3

# Listák (módosítható) - list (mutable)

lista1 = []
print(lista1)

# Hozzáfűzés - append()

lista1.append(100)
lista1.append(101)
lista1.append(102)
lista1.append(103)
lista1.append(104)
lista1.append(105)

print(lista1)

# Különböző típusú értékek is összefűzhetőek.

lista1.append("Ez")
lista1.append("is")
lista1.append("hozzáfűzhető.")
print(lista1)

# Lista elem eltávolítása - remove()

lista1.remove("is")
print(lista1)

# Minden elem eltávolítása - clear()

lista1.clear()
print(lista1)

# Elem beszúrása adott pozicióba - insert()

lista2 = ['egész', 18, 'tört', 8.232, 'valós', True]
print(lista2)

lista2.insert(0, 6e32)
print(lista2)

# Lista megfordítása - reverse()

lista2.reverse()
print(lista2)

# Lista rendezés - sort()
# (csak számokat vagy betűket tud rendezni, különböző típusú értékeket már nem!)

lista3 = [15, 8, 78, 23, 1, 65, 184]
lista3.sort()
print(lista3)

lista4 = ['Erika', 'Hedvig', 'Clara', 'Emese', 'Xen']
lista4.sort()
print(lista4)

# lista4 = [15, 8, 78, 23, 1, 65, 'gewge', 184]
# lista4.sort()
# print(lista4)


# Lista hossza, hány darab elem van benne - len()

print(len(lista1))
print(len(lista2))
print(len(lista3))
print(len(lista4))
