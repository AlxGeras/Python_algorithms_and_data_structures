'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''


from functools import reduce

num_1 = 'A2'
num_2 = 'C4F'

num_1, num_2 = list(num_1), list(num_2)
print(num_1)
print(num_2)


class Hexadecimal:
    def __init__(self, num_lst):
        self._hex_codes = '0123456789ABCDEF'
        self.dec_num = sum(16**i*self._hex_codes.find(num_lst[::-1][i]) for i in range(len(num_lst)))

    def __add__(self, other):
        self.sum = self.dec_num + other.dec_num
        self.sum = self._convert_hex(self.sum)

    def __mul__(self, other):
        self.mult = self.dec_num * other.dec_num
        self.mult = self._convert_hex(self.mult)

    def _convert_hex(self, number_dec):
        hex_num = ''
        s = number_dec
        while True:
            chas = s // 16
            ost = s % 16
            str_ost = self._hex_codes[ost]
            hex_num = str_ost + hex_num

            if chas <= 16:
                str_chas = self._hex_codes[chas]
                return str_chas + hex_num
            s = chas


num_1 = Hexadecimal(num_1)
num_2 = Hexadecimal(num_2)

print(num_2.dec_num)

num_1 + num_2
num_1 * num_2

print(list(num_1.sum))
print(list(num_1.mult))