'''3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках'''

from random import randint
from task_1 import combsort


def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


def kthSmallest(arr, l, r, k):
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if (index - l == k - 1):
            return arr[index]

        # If position is more, recur
        # for left subarray
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)

        # Else recur for right subarray
        return kthSmallest(arr, index + 1, r,
                           k - index + l - 1)
    print("Index out of bound")


n = int(input('Введите размер массива из случайных чисел от 0 до 49\n'))
ary = [randint(0, 49) for _ in range(n)]

k = int((n + 1) / 2)

print('Исходный список')
print(ary)
print('Отсотрированный список(для наглядности)')
print(combsort(ary.copy()))
print("Mediana`s element is ", end="")
print(kthSmallest(ary, 0, n - 1, k))
