#!/usr/bin/env python3

# if ternary operator - hármas operátor
# HAJTSD VÉGRE ...-t HA FELTÉTEL IGAZ, ELENBEN HAJTSD VÉGRE ...-t

from sajat_modulok import separator

lang = "ESP"

if lang == "HUN":
    print("Jó estét!")
elif lang == "ENG":
    print("Good evening!")

separator()
# Ha az alábbi feltétel igaz akkor hajtd végre a bal oldalt, ellenkező esetben a jobb oldalt.
print("Jó estét!") if lang == "HUN" else print("Good evening!")
# Egymásba ágyazott ternary
print("Jó estét!") if lang == "HUN" else (print("Good evening!") if lang == "ENG" else print("Buena noches!"))

separator()

if lang == "HUN":
    print("Jó estét!")
elif lang == "ENG":
    print("Good evening!")
elif lang == "ESP":
    print("Buena noches!")
