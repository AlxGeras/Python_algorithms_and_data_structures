"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []

for i in range(4):
    b = []
    s = 0
    print(f"{i+1}-я строка:")
    for j in range(4):
        while True:
            try:
                n = int(input())
                break
            except:
                print("Неверный формат")
        s += n
        b.append(n)
    b.append(s)
    matrix.append(b)

for i in matrix:
    print(i)
