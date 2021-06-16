"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

row = int(input('Введите число строк матрицы: '))
col = int(input('Введите число столбцов матрицы: '))
matrix = []

for i in range(row):
    b = []
    for j in range(col):
        b.append(randint(1, 50))
        print(f"{b[j]:4d}", end='')
    matrix.append(b)
    print()

max_el = 0
min_arr = []

for j in range(col):
    min_el = matrix[0][j]
    for i in range(1, row):
        if matrix[i][j] < min_el:
            min_el = matrix[i][j]
    min_arr.append(min_el)
    if min_el > max_el:
        max_el = min_el

print("\nМаксимальный среди минимальных: ", max_el)
