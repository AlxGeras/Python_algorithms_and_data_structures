### Сортировка расческой

"""1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный
случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее)."""

from random import randint


def combsort(lst):
    length = len(lst)
    gap = (length * 10 // 13) if length > 1 else 0

    while gap:
        if 8 < gap < 11:
            gap = 11
        swapped = False
        for i in range(length - gap):
            if lst[i + gap] < lst[i]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
        gap = (gap * 10 // 13) or swapped
    return lst

if __name__ == '__main__':

    n = int(input('Введите размер массива из случайных чисел от -100 до 99\n'))

    ary = [randint(-100, 99) for _ in range(n)]
    print('Неотсорированный список')
    print(ary)
    print('Отсортированный список')
    print(combsort(ary))
