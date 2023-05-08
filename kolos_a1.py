#zad 1
print("zad 1")
import math
wynik = math.sqrt(math.log(2,32) + math.pi + math.sin(56))**5
wynik = round(wynik, 2)
print(wynik)

#zad 2
print("zad 2")
lista = [1.5,2,3.8,4,5.1]
wynik =[p for p in lista if isinstance(p, int)]
print(lista)
print(wynik)

#zad 3
print("zad 3")
def sumuj_elementy(slownik):
    suma_elementow = []
    for klucz, wartosc in slownik.items():
        if isinstance(klucz, int) and isinstance(wartosc, int):
            suma_elementow.append(klucz + wartosc)
    return suma_elementow
slownik = {'a': 1, 'b': 2, 'c': 'test', 8 : 4}
wynik = sumuj_elementy(slownik)
print(wynik)

#zad 4
print("zad 4")
with open("tekst.txt", 'r', encoding="utf-8") as plik:
    tekst = plik.read()
    znaki = tekst[35:62]
    print(znaki)

    spacja = [space for space in znaki if space ==" "]

    if spacja:
        for spc in spacja:
            print(spc)
        print(f"Ilość spacji:  {len(spacja)}")
    else:
        print("Brak spacji")

#zad 5
print("zad 5")
with open("wyrazn.txt", 'w+', encoding="utf-8") as plik:
    a1 = int(input())
    n = int(input())
    r = int(input())
    wynik5 = a1+(n-1)*r
    wynik5 = str(wynik5)
    plik.write(wynik5)
