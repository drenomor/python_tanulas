#!/usr/bin/env python3

# "is" "is not" Identity Operator - Azonossági operátor

from sajat_modulok import separator

szam1 = 4
szam2 = 5

print(szam1 == szam2)
separator()
szam = 8

if type(szam) is int:
    print("Int típusú")

