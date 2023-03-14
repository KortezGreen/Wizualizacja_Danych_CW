
import math
"""
1.
x= math.e ** 10
print(x)
2.

x=  math.log((5+math.sin(8)**2),10)**(1./6)
print(x)

print(math.floor(3.55))
print(math.ceil(4.80))

imie = "DAWID"
nazwisko= "ANISZKIEWICZ"
print(imie.capitalize())
print(nazwisko.capitalize())
3.

piosenka="cos tam la la la la cos tam la la la la "
print(piosenka.count("la"))
4.

imie = "Dawid"
print(imie[1])
print(imie[len(imie)-1])
5.

napis="string,float,szesnastkowe"
print(napis.split(","))
6.

liczba=24
string=str(liczba)
print(string)
print(type(string))
float=float(liczba)
print(float)
print(type(float))
hex = hex(liczba)
print(hex)
print(type(hex))
7.
sporty=["pilkan","siatkowka","golf","koszykowka"]
sporty.reverse()
sporty.extend(["golf"])
print(sporty)
8.
skrot= {"zw":"zaraz wracam" ,"jj":"juz jestem"}
print(skrot["jj"])
9.
gry={"gra1":"atr1,atr2","gra2":"atr3,atr4"}
print(gry.count())
10.
print("podaj zdanie")
x=input()
print(x.count("a"))
11.
print("podaj a")
a= int(input())
print("podaj b")
b= int(input())
print("podaj c")
c= int(input())
if(a>b&a>c):
    print("a jest najwieksze")
elif(b>a&b>c):
    print("b jest najwieksze")
elif (c > a & c>b):
    print("c jest najwieksze")
12.
lista=[1, 3.5, 2, 5.12]
for x in range(len(lista)):
    print(lista[x]**2)
13.
parzyste=[]
licznik=0
while licznik!=10:
    st = "podaj %d liczbe" % (licznik)
    print(st)
    a = int(input())
    if(a%2==0):
        parzyste.append(a)
    licznik=licznik+1
print(parzyste)
"""







