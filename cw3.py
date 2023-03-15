import math
import random

#zad 2
# lista1 = [random.randint(1, 100) for _ in range(10)]
# parzyste = [x for x in lista1 if x % 2==0]
# print(parzyste)

#zad 3
produkty = [
            {"nazwa": "banany", "zakup": "sztuka"}
            {"nazwa": "maka", "zakup": "kilogram"}
            {"nazwa": "arbuz", "zakup": "sztuka"}
            {"nazwa": "mleko", "zakup": "litr"}
]
sztuki = [p for p in produkty if "sztuka" in p["zakup"]]
print(sztuki)


#zad 4
# def trojkat_prosty(a,b,c):
#     if a + b <=c or a+c <=b or b +c <= a:
#         return False
#     naj_bok=max(a,b,c)
#
#     suma_poz = a**2 + b**2 + c**2 - naj_bok**2
#
#     return naj_bok**2 == suma_poz

#zad 5
# a=2
# b=3
# h=5
#
# def trapez_pole(a,b,h):
#     pole=((a+b)*h)*0.5
#     return pole
#
# print(trapez_pole(a,b,h))

# zad 6
