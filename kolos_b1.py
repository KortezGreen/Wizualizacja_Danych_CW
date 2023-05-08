#zad 3
print("zad 3")
def roznica_i_liczba_wiekszych(lista):
    roznica = max(lista) - min(lista)
    wieksze = [liczba for liczba in lista if liczba > roznica]
    return roznica, len(wieksze)
lista = [3, 6, 2, 9, 1, 8]
wynik = roznica_i_liczba_wiekszych(lista)
print(wynik)

#zad 4
print("zad 4")
with open('tekst.txt', 'r', encoding='utf-8') as plik:
    plik_tekstowy = plik.read()
fragment_tekstu = plik_tekstowy[24:55]
ilosc_malych_liter = sum(1 for znak in fragment_tekstu if znak.islower())
print("Fragment tekstu:")
print(fragment_tekstu)
print("Ilość małych liter:")
print(ilosc_malych_liter)
