import numpy as np
import pandas as pd

#Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku imiona.xlsx
df = pd.read_excel('imiona.xlsx')

#Z danych z imiona.xlsx wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
#•tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
#•tylko rekordy gdzie nadane imię jest takie jak Twoje
#•sumę wszystkich urodzonych dzieci w całym danym okresie,
#•sumędzieci urodzonych w latach 2000-2005•sumę urodzonych chłopców i dziewczynek,
#•najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
#•najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,

# rekordy z liczbą nadanych imion większą niż 1000
df_over_1000 = df[df['Liczba'] > 1000]
print(df_over_1000)

# rekordy z nadanym imieniem równej nazwie jak Twoje
df_your_name = df[df['Imie'] == 'IMIE']
print(df_your_name)

# suma wszystkich urodzonych dzieci w całym okresie
total_births = df['Liczba'].sum()
print("Suma wszystkich urodzonych dzieci: ", total_births)

# suma dzieci urodzonych w latach 2000-2005
births_2000_2005 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]['Liczba'].sum()
print("Suma dzieci urodzonych w latach 2000-2005: ", births_2000_2005)

# suma urodzonych chłopców i dziewczynek
male_births = df[df['Plec'] == 'M']['Liczba'].sum()
female_births = df[df['Plec'] == 'K']['Liczba'].sum()
print("Suma urodzonych chłopców: ", male_births)
print("Suma urodzonych dziewczynek: ", female_births)

# najbardziej popularne imię dziewczynki i chłopca w danym roku
most_popular_names_by_year = df.groupby(['Rok', 'Plec']).apply(lambda x: x.nlargest(2, 'Liczba'))
print(most_popular_names_by_year)

# najbardziej popularne imię dziewczynki i chłopca w całym okresie
most_popular_names_all_time = df.groupby(['Imie', 'Plec']).agg({'Liczba': 'sum'}).reset_index().sort_values(by='Liczba', ascending=False).groupby('Plec').head(1)

#zad 2

df = pd.read_csv('zamowienia.csv', delimiter=';')

# lista unikalnych nazwisk sprzedawców
unique_surnames = df['Sprzedawca'].unique()
print(unique_surnames)

# 5 najwyższych wartości zamówień
top_orders = df.nlargest(5, 'Utarg')
print(top_orders)

# ilość zamówień złożonych przez każdego sprzedawcę
orders_per_seller = df['Sprzedawca'].value_counts()
print(orders_per_seller)

# suma zamówień dla każdego kraju
orders_per_country = df.groupby('Kraj').agg({'Utarg': 'sum'})
print(orders_per_country)

# suma zamówień dla roku 2005, dla sprzedawców z Polski
orders_poland_2005 = df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'].str.endswith('2005'))]['Utarg'].sum()
print(orders_poland_2005)

# średnia kwota zamówienia w 2004 roku
avg_order_amount_2004 = df[df['Data zamowienia'].str.endswith('2004')]['Utarg'].mean()
print(avg_order_amount_2004)

# zapis danych za 2004 rok do pliku zamówienia_2004.csv
df[df['Data zamowienia'].str.endswith('2004')].to_csv('zamowienia_2004.csv', index=False, sep=';')

# zapis danych za 2005 rok do pliku zamówienia_2005.csv
df[df['Data zamowienia'].str.endswith('2005')].to_csv('zamowienia_2005.csv', index=False, sep=';')
