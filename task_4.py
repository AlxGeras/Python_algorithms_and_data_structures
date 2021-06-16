"""
Задание_4. Определить, какое число в массиве встречается чаще всего
"""
from random import randint


list_len = 25
arr = [randint(0, 20) for i in range(list_len)]
print(arr)

max_count = max([(i, arr.count(i)) for i in set(arr)], key=lambda t: t[1])
print(f'Наиболее встречающееся число {max_count[0]}, количество вхождений равно {max_count[1]}')


