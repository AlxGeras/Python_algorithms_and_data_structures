# Задание-2: Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.


from timeit import timeit
import cProfile

# алгоритм «Решето Эратосфена»


def sieve(n):
    size = 0
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8
               }
    for item in pi_func:
        if n <= item:
            size = pi_func[item]
            break
    array = [_ for _ in range(size)]
    array[1] = 0
    i = 2
    p = 2
    cnt = 1
    while cnt <= n:
        if array[i] != 0:
            p = array[i]
            cnt += 1
            j = i * 2
            while j < size:
                array[j] = 0
                j += i
        i += 1
    return p


# без использования «Решета Эратосфена»


def prime(n):
    cnt = 1
    p = 2
    while cnt < n:
        p += 1
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            cnt += 1
    return p



print('*'*20+' prime '+'*'*20)
for i in range(1,802,100):
    print(f'{i = }', timeit( f'prime({i})', globals=globals(), number=10))
print('*'*20+' sieve '+'*'*20)
for i in range(1,802,100):
    print(f'{i = }', timeit(f'sieve({i})', globals=globals(), number=10))
print('*'*40)

cProfile.run('prime(900)')
cProfile.run('sieve(900)')

""" результаты работы 
******************** prime ********************
i = 1 4.450000000003063e-06
i = 101 0.027220939
i = 201 0.10410922399999999
i = 301 0.21074431000000002
i = 401 0.390405336
i = 501 0.677459731
i = 601 0.953780914
i = 701 1.3705994380000002
i = 801 1.934419986
******************** sieve ********************
i = 1 2.2771999999449122e-05
i = 101 0.005450364999999735
i = 201 0.03161227400000044
i = 301 0.03490086800000025
i = 401 0.03580782299999985
i = 501 0.03709247900000001
i = 601 0.039658387999999434
i = 701 0.0440829659999995
i = 801 0.04498599400000014
****************************************
         4 function calls in 0.251 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.251    0.251 <string>:1(<module>)
        1    0.251    0.251    0.251    0.251 task_2.py:47(prime)
        1    0.000    0.000    0.251    0.251 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         5 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.003    0.003    0.004    0.004 task_2.py:12(sieve)
        1    0.000    0.000    0.000    0.000 task_2.py:27(<listcomp>)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Общий вывод: алгоритм решета имеет линейную сложность O(n),  обычный алгоритм квадратичную(O(n:2)) 
# В разы быстрее безусловно выполняется алготим с использованием решета.

"""


