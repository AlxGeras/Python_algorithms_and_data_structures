
# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

def sum_series(n):
    if n == 1:
        return 1
    if n > 1:
        return n + sum_series(n-1)

n = int(input('n = '))
value_function = sum_series(n)
if value_function == n*(n+1)/2:
    print(f'Гипотеза верна. Сумма равна {value_function}')
else: print('Гипотеза не верна')

