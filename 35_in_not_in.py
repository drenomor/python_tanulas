#!/usr/bin/env python3

# "in" membership operator - tagsági operátor

kozmondas = "A hazug embert hamarabb utól érik, mint a sánta kutyát."

if "kutyát" in kozmondas:
    print("A szöveg tartalmazza a keresett szót.")
else:
    print("A nem szöveg tartalmazza a keresett szót.")

nevek_lista = ['Dwalin', 'Balin', 'Kili', 'Fili', 'Dori', 'Nori', 'Ori', 'Oin', 'Gloin', 'Bifur', 'Bofur', 'Bombur', 'Thorin']

if "Ori" in nevek_lista:
    print("A lista tartalmazza a keresett nevet.")
else:
    print("A lista nem tartalmazza a keresett nevet.")

if "kili" not in nevek_lista:
    print("Nincs találat")
