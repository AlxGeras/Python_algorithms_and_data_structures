# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# # блоксхемы я не рисую из принципа. курс называется алгоритмы на языке питон  а не уроки рисования.


def sum_series(n):
    if n == 1:
        return 1
    if n > 1:
        return 1/(2**(n-1))*(-1)**(n-1) + sum_series(n-1)


n = int(input('n = '))

print(sum_series(n))