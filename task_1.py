# Задание - 1. Анализируется задача 4 из урока 2:
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.




from timeit import timeit
import cProfile


# вариант 1, рекурсия


def rec(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return rec(n - 1) - 1 / (2 ** (n - 1))
    else:
        return rec(n - 1) + 1 / (2 ** (n - 1))


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
    return _rec_dict(n)


# вариант 3, цикл


def loop_func(n):
    res = 0
    for i in range(n):
        if i % 2 == 0:
            res += 1 / (2 ** i)
        else:
            res -= 1 / (2 ** i)
    return res


# анализируем скорость алгоритма с использованием timeit:

print('*'*20+' rec '+'*'*20)
for i in range(1,802,100):
     print(f'{i = }', timeit(f'rec({i})', globals=globals(), number=100))
print('*'*20+' rec_dict '+'*'*20)
for i in range(1,802,100):
    print(f'{i = }', timeit(f'rec_dict({i})', globals=globals(), number=100))
print('*'*20+' loop_func '+'*'*20)
for i in range(1,802,100):
    print(f'{i = }', timeit(f'loop_func({i})', globals=globals(), number=100))
print('*'*40)


# анализируем скорость алгоритма с использованием cProfile:

cProfile.run('rec(900)')
cProfile.run('rec_dict(900)')
cProfile.run('loop_func(900)')

''' Результаты работы:

******************** rec ********************
i = 1 1.2301999999998758e-05
i = 101 0.014931901999999997
i = 201 0.030516862
i = 301 0.04259938099999999
i = 401 0.062396119
i = 501 0.07192319900000002
i = 601 0.09635365000000001
i = 701 0.125300028
i = 801 0.14643612699999997
******************** rec_dict ********************
i = 1 5.313399999995472e-05
i = 101 0.00812620800000008
i = 201 0.021999341999999977
i = 301 0.04053733599999998
i = 401 0.057092593999999997
i = 501 0.08444492999999997
i = 601 0.12093277399999991
i = 701 0.13251221400000013
i = 801 0.15732560099999993
******************** loop_func ********************
i = 1 5.60139999998821e-05
i = 101 0.005648246999999884
i = 201 0.016767535000000056
i = 301 0.03146569599999993
i = 401 0.04699228699999991
i = 501 0.06483036999999992
i = 601 0.0876555240000001
i = 701 0.1116857630000001
i = 801 0.13874154000000005
****************************************
         903 function calls (4 primitive calls) in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
    900/1    0.002    0.000    0.002    0.002 task_1.py:14(rec)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         902 function calls (5 primitive calls) in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.002    0.002 task_1.py:26(rec_dict)
    898/1    0.002    0.000    0.002    0.002 task_1.py:29(_rec_dict)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_1.py:43(loop_func)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

# Общий вывод: все алгоритмы имеют сложность O(n^2) (зависимость квадратичная, O(0.0027*n^2 + 0.0153n) ~ O (n^2)).
# Быстрее всех выполняется алгоритм с использованием цикла.
#
# Обусловлено это тем, что рекурсивные алгоритмы складывают данные на стек и тратят время на доступ к этим данным.
# Рекурсия с ипользованием мемоизации работает немного медленнее обычной рекурсии, т.к. использует словарь для
# решения задачи и тратит время на запись и чтение данных из словаря, и в данном случае операции чтения записи
# проигрывают по времени.
