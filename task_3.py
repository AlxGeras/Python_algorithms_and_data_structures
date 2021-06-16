"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.
"""

from random import randint

list_len = 10
arr = [randint(-99, 99) for i in range(list_len)]
print(arr)

max_el = arr[0]
min_el = arr[0]
max_ind = 0
min_ind = 0

for i in range(len(arr)):
    if max_el < arr[i]:
        max_el = arr[i]
        max_ind = i
    if min_el > arr[i]:
        min_el = arr[i]
        min_ind = i

arr[min_ind], arr[max_ind] = max_el, min_el

print('Новая последовательность: ')
print(arr)
