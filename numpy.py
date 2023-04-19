#zad 1
import numpy as np
tablica = np.arange(0,80,4)
print(tablica)

#zad 2
listaf = [1.5, 2.7, 3.9, 4.2, 5.0]
tabf = np.array(listaf)
tabi = tabf.astype(np.int32)
print("Lista z wartościami zmiennoprzecinkowymi:", listaf)
print("Kopia listy przekonwertowana na typ int32:", tabi)

#zad 3
def power_matrix(n):
    matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 2**(i+j)
    
    return matrix

wynik = power_matrix(4)
print(wynik)

#zad 4
def generate_powers(base, n):
    powers = np.logspace(start=0, stop=n-1, num=n, base=base, dtype=int)
    return powers
  
result = generate_powers(2, 4)
print(result)

#zad 5
def generate_matrix(n):
    vector = np.arange(n)[::-1]
    diagonal_matrix = np.diag(vector, k=2)
    return diagonal_matrix
  
result = generate_matrix(5)
print(result)

#zad 6
words = ['KOT', 'PANDA', 'ALGORYTM']
max_len = max([len(word) for word in words])
matrix = np.empty((max_len, max_len), dtype='U1')
matrix[:] = ' '

for i, word in enumerate(words):
    matrix[:len(word), i] = list(word)
    matrix[i, len(word)-1:max_len] = list(word[::-1])
    diagonal = np.diag(matrix[::-1])
    diagonal[max_len-len(word):max_len] = list(word[::-1])
    np.fill_diagonal(matrix[::-1], diagonal)
print(matrix)

#zad 7
def generate_matrix(n):
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        diagonal = np.full(n-i, 2*(i+1), dtype=int)
        np.fill_diagonal(matrix[i:, :-i], diagonal)
        np.fill_diagonal(matrix[:-i, i:], diagonal)
    return matrix

#zad 8
def split_array(array, direction):
    rows, cols = array.shape
    if direction == "poziom":
        if cols % 2 != 0:
            print("Nie można dokonać podziału, liczba kolumn jest nieparzysta.")
            return None
        else:
            half = cols // 2
            left_half = array[:, :half]
            right_half = array[:, half:]
            return left_half, right_half
    elif direction == "pion":
        if rows % 2 != 0:
            print("Nie można dokonać podziału, liczba wierszy jest nieparzysta.")
            return None
        else:
            half = rows // 2
            top_half = array[:half, :]
            bottom_half = array[half:, :]
            return top_half, bottom_half
    else:
        print("Nieprawidłowy kierunek podziału, dostępne opcje: 'poziom' lub 'pion'.")
        return None

#zad 9
a = 2
d = 3

matrix = np.zeros((5, 5))
for i in range(5):
    for j in range(5):
        matrix[i][j] = a + (i * 5 + j) * d
        
print(matrix)
