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

data ={'a':np.arange(50),
       'a':np.random.randint(0,50,50),
       'a':np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d'])*100

plt.scatter('a','b',t='c',i='d',data=data)
plt.xlabel('wartości a')
plt.ylabel('wartości b')
plt.show()
