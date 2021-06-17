#!/usr/bin/env python3

with open("egyeb/Matild.txt", "r", encoding="utf-8") as in_file:

    szoveg = ""

    sor = in_file.readline()

    while sor:
        szoveg += sor

        sor = in_file.readline()

    print(szoveg)
