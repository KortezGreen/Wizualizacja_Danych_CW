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
matrix = np.array([[1, 2, 3], [4, 5, 6]])
a = np.sin(matrix)
print(a)

#zad 6
matrix = np.array([[1, 2, 3], [4, 5, 6]])
a = np.sin(matrix)
print(a)
new_matrix = np.array([[0.5, 1.5, 2.5], [3.5, 4.5, 5.5]])
b = np.cos(new_matrix)
print(b)

#zad 7
matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
a = np.sin(matrix1)
matrix2 = np.array([[0.5, 1.5, 2.5], [3.5, 4.5, 5.5]])
b = np.cos(matrix2)
result = a + b
print(result)

#zad 8
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for row in matrix:
    print(row)

#zad 9
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for element in matrix.flat:
    print(element)

#zad 10
matrix = np.arange(81).reshape((9,9))
print("Macierz początkowa:")
print(matrix)
new_matrix = matrix.reshape((3,27))
print("Macierz po zmianie kształtu:")
print(new_matrix)

#zad 11
vector = np.arange(12)
matrix_3x4 = vector.reshape((3, 4))
matrix_4x3 = np.arange(12).reshape((4, 3))
matrix_2x6 = np.arange(12).reshape((2, 6))
print(matrix_3x4.flatten())
print(matrix_4x3.flatten())
print(matrix_2x6.flatten())
print(np.array_equal(matrix_3x4.flatten(), matrix_4x3.flatten()))
print(np.array_equal(matrix_3x4.flatten(), matrix_2x6.flatten()))
