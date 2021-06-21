#!/usr/bin/env python3

# String formatozás, és f stringek

# régi mód

from sajat_modulok import separator
separator("régi mód")

szoveg1 = "A te neved %s, és %d éves vagy." % ("Henrik", 46)
print(szoveg1)

# nem olyan régi mód
separator("nem olyan régi mód")

szoveg2 = "A te neved {}, és {} éves vagy.".format("Erika", 29)
print(szoveg2)

# új mód (f srings)
separator("új mód 'f strings'")

nev = "Kálmán"
kor = 19

szoveg3 = f"A te neved {nev}, és {kor} éves vagy."
print(szoveg3)

separator("Példa")

nevek_szotar = {'Dwalin': 532,
                'Balin': 431,
                'Kili': 832,
                'Fili': 632,
                'Dori': 325,
                'Nori': 499,
                'Ori': 321,
                'Oin': 333,
                'Gloin': 639,
                'Bifur': 343,
                'Bofur': 521,
                'Bombur': 222,
                'Thorin': 753}
for nev, kor in nevek_szotar.items():
    print(f"A te neved {nev}, és {kor} éves vagy.")
