"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random


def merge_sort(n):
    if len(n) > 1:
        c = len(n) // 2
        left = n[:c]
        right = n[c:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                n[k] = left[i]
                i += 1
            else:
                n[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            n[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            n[k] = right[j]
            j += 1
            k += 1
        return n


test = [random.randint(0, 50) for i in range(10)]
print(test)
print(merge_sort(test))