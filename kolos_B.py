#B
#zad 1
print("zad 1")
with open('tekst.txt', 'r', encoding="utf-8") as plik:
    tekst = plik.read()
    znaki = tekst[71:111]

    liczba_A = znaki.count('A') + znaki.count('a')

    if liczba_A == 0:
        print('Nie ma żadnej litery "A".')
    else:
        print(f'Liczba liter "A" we fragmencie: {liczba_A}')

#zad 2
print("zad 2")
lista = [1.5,2,3.8,4,5.1]
wynik =[p for p in lista if isinstance(p, float)]
#int tez działa
print(lista)
print(wynik)

#zad 3
print("zad 3")
def dodaj_pierwszy(lista):
    suma = lista[0] + sum(lista[1:])
    lista.append(suma)
    return lista

lista = [1,3,5]
print(dodaj_pierwszy(lista))

#zad 4
print("zad 4")
import math
wynik = math.sin(2)*(56) + math.sqrt((((4)**2)/25) + math.log(85, 3))**4
wynik = round(wynik, 2)
print(wynik)

#zad 5
print("zad 5")
n1 = int(input("Podaj pierwszą liczbę całkowitą: "))
n2 = int(input("Podaj drugą liczbę całkowitą: "))
suma = sum(range(1, n2+1))
f = open('zadanie5.txt', 'w', encoding="utf-8")
f.write(str(suma))
f.close()
