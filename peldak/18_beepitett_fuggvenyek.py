#!/bin/usr/env python3

def elvalaszto():
    print('------')

# kiiratás
elvalaszto()
print(abs(-93))

gyumolcsok = ['papaya', 'ananász', 'gránátalma', 'pomelo', 'mandarin', 'málna', 'ribizli']

# felsorolás
elvalaszto()
for index, gyumolcs_db in enumerate(gyumolcsok):
    print(index, gyumolcs_db)

# kasztolás lebegő pontos számmá
elvalaszto()
print(float(45))
print(float('52.344'))
print(float('5.36e-16'))
