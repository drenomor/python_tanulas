#!/usr/bin/env python3

# 'r' = read (olvasás)
# 'w' = write (írás)
# 'a' = append (hozzáfűzés)

with open('peldak/out.txt', 'a', encoding='utf-8') as file:
    ujsor = '\nNem akarásnak nyögés a vége.'
    file.write(ujsor)
