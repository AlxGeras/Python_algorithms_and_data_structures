#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
from random import randint

count = 0
max=(0,0)
n = int(input('Введите максимальное значение натуального числа для функции случайных чисел '))
for _ in range(0, 10):
    m = mm = randint(0,n)
    print(f'{_+1}-е число {m}')
    sum = 0
    while m > 0:
        sum += m % 10
        m //= 10
    if sum > max[0]:
        max = (sum, mm)

print (f'\nЧисло {max[1]} имеет максимальную сумму цифр равную {max[0]}.')
