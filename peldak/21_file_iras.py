#!/usr/bin/env python3

# 'r' = read (olvasás)
# 'w' = write (írás)
# 'a' = append (hozzáfűzés)

with open('peldak/out.txt', 'w', encoding='utf-8') as file:
    szoveg = 'Számszeríjjal őrizd bűnös ékezeteidet!'

    file.write(szoveg)
