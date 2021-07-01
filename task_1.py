''' Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
 Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
 Результаты анализа вставьте в виде комментариев к коду.
 Также укажите в комментариях версию Python и разрядность вашей ОС'''

"""Анализируется задача 4 из урока 2:
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) равно 800
Python 3.8.1
64-bit
"""

import sys


def rec(n):
    n_stack = [1]
    if n == 1:
        return 1
    elif n % 2 == 0:
        storage = rec(n - 1) - 1 / (2 ** (n - 1))
        if n not in n_stack: stack.append(storage)
        return storage
    else:
        storage = rec(n - 1) + 1 / (2 ** (n - 1))
        if n not in n_stack: stack.append(storage)
        return storage


# вариант 2, рекурсия и мемоизация


def rec_dict(n):
    seq_dict = {1: 1, 2: 0.5, 3: 0.75}  # суммы для n = 1, 2, 3

    def _rec_dict(n):
        if n in seq_dict:
            return seq_dict[n]
        elif n % 2 == 0:
            seq_dict[n] = _rec_dict(n - 1) - 1 / (2 ** (n - 1))
        else:
            seq_dict[n] = _rec_dict(n - 1) + 1 / (2 ** (n - 1))
        return seq_dict[n]

    return _rec_dict(n), seq_dict


# вариант 3, цикл


def loop_func(n):
    sum_of_bytes = 0
    res = 0
    for i in range(n):
        if i % 2 == 0:
            res += 1 / (2 ** i)
            sum_of_bytes = sys.getsizeof(res) + sys.getsizeof(i)
        else:
            res -= 1 / (2 ** i)
            sum_of_bytes = sys.getsizeof(res) + sys.getsizeof(i)
    return res, sum_of_bytes

n = 800
stack = [1] # используем список для подсчета памяти выделяемой в стеке
rec(n)
sum_of_bytes = 0
for i in stack: sum_of_bytes += sys.getsizeof(i)
sum_of_bytes = sum_of_bytes + sys.getsizeof(stack)
print(f'При использованиии метода рекурсии выделяется {sum_of_bytes + sys.getsizeof(n)} байт.')

sum_of_bytes = 0
rec_dict_test = rec_dict(n)[1]
for i in rec_dict_test: sum_of_bytes += sys.getsizeof(rec_dict_test[i])
sum_of_bytes = sum_of_bytes + sys.getsizeof(rec_dict_test)
print(f'При использованиии метода рекурсии c использованием словаря выделяется {sum_of_bytes+ sys.getsizeof(n)} байт.')

print(f'При использованиии цикла выделяется {loop_func(n)[1] + sys.getsizeof(n)} байт.')


'''n = 800
При использованиии метода рекурсии выделяется 16408 байт.
При использованиии метода рекурсии c использованием словаря выделяется 33348 байт.
При использованиии цикла выделяется 44 байт.
Наиболее эффекивным в использовании памяти является способ решения циклом.
'''
