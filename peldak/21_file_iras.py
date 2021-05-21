#!/usr/bin/env python3

# 'r' = read (olvasás)
# 'w' = write (írás)
# 'a' = append (hozzáfűzés)

with open('peldak/kozmondasok.txt', 'r', encoding='utf-8') as infile:
    with open('peldak/out.txt', 'w', encoding='utf-8') as outfile:
        
        sor = infile.readline()

        while sor:
            outfile.write(sor)
            sor = infile.readline()
