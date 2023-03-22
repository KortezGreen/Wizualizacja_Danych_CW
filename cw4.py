#zad 1
import random
liczby=[random.uniform(0,30) for _ in range(10)]
liczby=[num * 2 for num in liczby]
with open('liczby.txt', 'w', encoding="utf-8") as f:
    for num in liczby:
        f.write(str(num) + '\n')

#zad 2
liczb = open('liczby.txt', 'r', encoding="utf-8")
liczby_all = liczb.readlines()
print(liczby_all)

#zad 3
