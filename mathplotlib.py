import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x = np.array([1,2,3,4])
# y = x**2
#
# plt.plot(x,y,'ro-')
# plt.axis([0,6,0,20])
# plt.show()
#
# plt.plot(x,y,'r')
# plt.plot(x,y,'o')
# plt.axis([0,6,0,20])
# plt.show()

# plt.plot(a,a,a,'r--',a,a**2,'bs',a,a**3,'g^')
# plt.legend(labels=['liniowa', 'kwadratowa','sześcienna'])
# plt.show()

# plt.plot(a,a,a,'g--',a,a**2,'bs',a,a**3,'r^')
# plt.plot(lables=['liniowa', 'kwadratowa','sześcienna'])
# plt.show()
#
# plt.savefig('wykres1.png')

# x = np.arange(0,10.1,0.1)
# y = np.sin(x)
#
# plt.plot(x,y)
# plt.ylabel('x')
# plt.ylabel('sin(x)')
#
# plt.title('wykres sin(x)')
# plt.show()

# data ={'a':np.arange(50),
#        'a':np.random.randint(0,50,50),
#        'a':np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d'])*100
#
# plt.scatter('a','b',t='c',i='d',data=data)
# plt.xlabel('wartości a')
# plt.ylabel('wartości b')
# plt.show()
#
# x1 = np.arange(0,2,0.02)
# x2 = np.arange(0,2,0.02)

# y1 = np.sin(2*np.pi*x1)
# y2 = np.sin(2*np.pi*x2)
#
# plt.subplot(4,1,1)
# plt.plot(x1,y1, 'r')
# plt.title('Wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(4,1,4)
# plt.plot(x2, y2, 'g')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('Wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()
#
# fig, axs = plt.subplots(3,2)
# axs[0,0].plot(x1,y1, 'g-')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x)')
# axs[0,0].set_title('Wykres sin(x)')
#
# axs[1,1].plot(x2,y2, 'r-')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
# axs[1,1].set_title('Wykres cos(x)')
#
# axs[2,0].plot(x1,y1, 'g-')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('sin(x)')
# axs[2,0].set_title('Wykres sin(x)')
#
# fig.delaxes([0,1])
# fig.delaxes([1,0])
# fig.delaxes([2,1])
#
# plt.show()

data = {'Kraj': ['Belgia', 'Indie','Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delphi', 'Brazylia'],
        'Kontynent': ['Europa','Azja','Ameryka Południowa'],
        'Populacja': [11312443,34234434234,14334342,12412344]}

df = pd.DataFrame(data)
print(df)
grupa = df.groupby('Kontynent')
etykiety = list(grupa.groups.keys())
wartosc = list(grupa.agg('Populacja').sum())

plt.bar(etykiety, wartosc, color=['yellow','green','red'])
plt.xlabel('Konynent')
plt.ylabel('Populacja w mld')
plt.show()
