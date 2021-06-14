# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

n = input('n = ')
quntity_original = len(n)
n = int(n)

reverted = 0

while n > 0:
    reverted = reverted * 10 + n%10
    n //= 10

print(str(reverted).zfill(quntity_original))