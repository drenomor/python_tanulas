#!/usr/bin/env python3

with open("egyeb/Matild.txt", "r", encoding="utf-8") as in_file:

    szoveg = ""

    sor = in_file.readline()

    while sor:
        szoveg += sor.lstrip().replace("Matild", "Klári").replace(", marha", "")

        sor = in_file.readline()

    with open("egyeb/Klari.txt", "w", encoding="utf-8") as out_file:
        out_file.write(szoveg)
