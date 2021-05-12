#!/usr/bin/env python3

gyumolcsok = ['papaya', 'ananász', 'gránátalma', 'pomelo', 'mandarin', 'málna', 'ribizli', 639]
zoldsegek = ['krumpli', 'hagyma', 'karalábé', 'káposzta', 'uborka', 'répa', 'csicsóka']

# for gyumolcs_szamlalo in gyumolcsok:
#     print(gyumolcs_szamlalo)

# for zoldseg_szamlalo in zoldsegek:
#     print(zoldseg_szamlalo)

def lista_printer(bemeneti_lista):
    for szamlalo in bemeneti_lista:
        if isinstance(szamlalo, str): # megvizsgáljuk, hogy string-e a lista eleme
            print(szamlalo.upper())

lista_printer(gyumolcsok)
print()
lista_printer(zoldsegek)