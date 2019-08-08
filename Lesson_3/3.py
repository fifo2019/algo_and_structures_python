#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 35, 12, 39]

min = 0
max = 0

for i in lis:
    for j in lis:
        if i < j:
            min = i
        if i < j:
            max = j
    break

for index, value in enumerate(lis):
    if value == min:
        lis[index] = max
    if value == max:
        lis[index] = min

print(lis)
