"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
count_even = 0
count_odd = 0

def even_and_odd(userInput, count_even, count_odd):
    balance_of_ten = userInput % 10
    if userInput < 10:
        if userInput % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        return print(f"Чётных: {count_even}; Нечётных: {count_odd}")
    if balance_of_ten % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    return even_and_odd(userInput // 10, count_even, count_odd)

userInput = int(input("Введите число:"))
even_and_odd(userInput, count_even, count_odd)
