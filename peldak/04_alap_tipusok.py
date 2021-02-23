#!/usr/bin/env python3

# Típusok

## Számok (numbers), Szöveg (String), Logikai (Boolean),
## Lista (list), Rendezett lista (tuple), Szótár (dictionary),
## Felhasználó által definiált típus (user defined)


### Számok (numbers)

szam_egesz = 10         # Egész (intiger)
szam_lebego_pontos = 48.234  # Lebegőpontos [valós] (float)
szam_mernoki = 5.67e5   # Mernöki vagy tudományos (scientific)
szam_komplex = 0.392j   # Komplex (complex)

### Szöveg (string)

Kereszt_Nev = "Enikő"
Szemszin = 'Kék'

### Logikai (Boolean)

igaz_ertek = True
hamis_ertek = False

### Lista, tömb (list)

lista = []

### Rendezett lista (tuple)

rendezett_lista = ()

### Szótár (dictionary)

szotar = {}

# Típusok meghatározása a type() függvényel

print(type(szam_egesz))
print(type(szam_lebego_pontos))
print(type(szam_mernoki))
print(type(szam_komplex))
print(type(igaz_ertek))
print(type(hamis_ertek))
print(type(Kereszt_Nev))
print(type(Szemszin))
print(type(lista))
print(type(rendezett_lista))
print(type(szotar))
