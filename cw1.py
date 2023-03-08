a = 'napis \ndrugi napis'
print(a)
b = 5
c = 5.5
print(b, c)
d = 5+3j
print(d)

e=c+d
print(e)
f=c//b
print(f)
g= c%b
print(g)
h =b**2
print(h)
i=b**1/2
j = pow(b,1/2)
print(i)
print(j)

listy = [6]
print(listy)

owoce = [3]
owoce.insert(1, 'Figa')
print(owoce)

slownik = {'a':2, 1:2, 4: 'ab'}
print(slownik)
print(slownik[4])
slownik['klucz'] = 'wartosc'
print(slownik)

print('a=%(zm)d' % {'zm':12})
napis = 'a={}, b={}'
print(napis.format(12,12))

a=67
b=55
if a<b:
    print(a)
elif b<a:
    print(b)
else:
    print(a, b)

a=67
b=55
if a<b:
    print(a)
elif b<a:
    print(b)
else:
    print(a, b)