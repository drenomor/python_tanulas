#!/usr/bin/env python3

def separator(text=""):
    print("-----(", text, ")-----")


def hello():
    print('Üdvözlés a sajat_modulok.py-ból!')
    print(f'Helló {__name__} modulból!')


szin = 'zold'

nevek = ['Kara Lá Béla', 'Víz Elek', 'Vincs Eszter']


class Szemely:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

    def show_fields(self):
        print(self.nev, self.kor)


szam = 10

if __name__ == "__main__":
    hello()
    print(szam)
    Denes = Szemely("Dénes", 53)
    Denes.show_fields()
