#!/usr/bin/env python3

# Windows filekezelő címsorba beírjuk 'cmd', az aktuális mappából nyit egy parancssort.
# Parancssor argumentumok használata 'sys' könyvtár importálásával történik.

import sys

# print(sys.argv) # összes parancsor argumentum kiiratása

def osszeg(a, b):
    return a + b

if len(sys.argv) > 1:
    try:
        szam2 = int(sys.argv[2])
        szam1 = int(sys.argv[1])
    except:
        szam1 = 0
        szam2 = 0

    print(osszeg(szam1, szam2))
