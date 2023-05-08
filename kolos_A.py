#A
#zad 1
# a = int(input())
# b = int(input())
# wynik = (a*a)+(a*b)+(b*b)
# f = open('wynik1.txt', 'w', encoding="utf-8")
# f.write(str(wynik))
# f.close()

#zad 2
# def lists(x, z):
#     if len(x)<len(z):
#         kl = x
#         ll = z
#     else:
#         kl = z
#         ll = x
#
#     sumal= []
#
#     for i in range(len(kl)):
#         suma_all_l=kl[i]+ll[i]
#         sumal.append(suma_all_l)
#
#     if len(x) != len(z):
#         for i in range (len(kl), len(ll)):
#             sumal.append(ll[i])
#
#     return sum(sumal)
#
# x = [2,4,6]
# z = [1,3,5]
# print(lists(x,z))

#zad 3
# with open('tekst.txt', 'r', encoding="utf-8") as plik:
#     tekst = plik.read()
#     znaki = tekst[100:135]
#
#     duze = [znak for znak in znaki if znak.isupper()]
#
#     if duze:
#         print("Duże litery: ")
#         for litera in duze:
#             print(litera)
#         print(f"Liczba dużych liter: {len(duze)}")
#     else:
#         print("Brak dużych liter")

#zad 4
# lista = [1,2,3,4,5]
# a = int(3)
# wynik =[element for element in lista if element > a]
# print(wynik)

#zad 5
# import math
# wynik = math.sqrt(math.exp(3) + math.cos(2)*(39))**5 + (2/7)**3 + math.pi
# wynik = round(wynik, 2)
# print(wynik)
