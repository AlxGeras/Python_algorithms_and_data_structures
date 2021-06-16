"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

# Заполняем массив случачайными числами
arr = []
# for i in range(10):
while len(arr) < 10:
    n = int(randint(1,50))
    if n in arr:        # условие для избежания дублирования элементов
        continue
    arr.append(n)
print(arr)

max_el = arr[0]
min_el = arr[0]
max_ind = 0
min_ind = 0

# Определяем индексы наибольшего и наименьшего элемент а также сами элементы
for j in range(len(arr)):
    if max_el < arr[j]:
        max_el = arr[j]
        max_ind = j
    if min_el > arr[j]:
        min_el = arr[j]
        min_ind = j
        
result = 0


for k in range(min(min_ind, max_ind)+1, max(min_ind, max_ind)):
    result += arr[k]

print(f'Сумма элементов между минимальным {min_el} и максимальным {max_el} элементами: {result}')
