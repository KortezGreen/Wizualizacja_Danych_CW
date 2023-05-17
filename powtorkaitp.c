import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv('iris.data',header=0,sep=',',decimal='.')
# print(df)
# sns.lineplot(data=df,x=df.index,y='sepal length',hue='class', palette=['yellow','green','red'])
# plt.xlabel('Indeksy')
# plt.title('Wykres liniowy danych z iris.data')
# plt.show()

# data={'a': np.arange(10),
#      'c': np.random.randint(0,50,10),
#      'd': np.random.randn(10)}
# data['b'] = data['a'] + 10*np.random.randn(10)
# data['d'] = np.abs(data['d'])*100
# df= pd.DataFrame(data)
#
# plot = sns.relplot(data=df,x='a',y='b',hue='c', palette='bright',size='d', legend=True)
# plot.set(xticks=data['a'])
# plt.show()

data = {'Kraj': ['Belgia', 'Indie','Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delphi', 'Brazylia'],
        'Kontynent': ['Europa','Azja','Ameryka Południowa'],
        'Populacja': [11312443,34234434234,14334342,12412344]}
df=pd.DataFrame(data)
plot = sns.barplot(data=df,x='Kontynent',y='Populacja',hue='Kontynent',)
plot.legend()
plot.set()
plt.show
