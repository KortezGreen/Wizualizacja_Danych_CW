import numpy as np

#zad 1
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b
print(c)

#zad 2
a = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
min_rows = np.min(a, axis=1)
min_cols = np.min(a, axis=0)
print("Macierz 3x3:")
print(a)
print("Najniższe wartości dla każdego rzędu: ", min_rows)
print("Najniższe wartości dla każdej kolumny: ", min_cols)
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
min_rows = np.min(b, axis=1)
min_cols = np.min(b, axis=0)
print("\nMacierz 4x4:")
print(b)
print("Najniższe wartości dla każdego rzędu: ", min_rows)
print("Najniższe wartości dla każdej kolumny: ", min_cols)

#zad 3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.dot(matrix1, matrix2.T)
print(result)

#zad 4
matrix1 = np.array([2, 3, 4], dtype=int)
matrix2 = np.array([1.5, 2.5, 3.5], dtype=float)
result = np.dot(matrix1, matrix2)
print(result)

#zad 5
