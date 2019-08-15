"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections

numbers = collections.defaultdict(list)

for i in range(2):
    hexadecimal = input(f'Введите {i + 1}-е шестнадцатеричное число: ')
    numbers[i + 1] = list(hexadecimal)
print(numbers)

lst = [int(''.join(i), 16) for i in numbers.values()]
amount = list(hex(sum(lst)).upper())
composition = list(hex(lst[0] * lst[1]).upper())

print(f'Сумма введенных чисел: {amount[2:]}')
print(f'Произведение введенных чисел : {composition[2:]}')