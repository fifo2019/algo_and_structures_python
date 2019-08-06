"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

result = 0
startNumber = 1

def sum_series_numbers(userInput, result, startNumber):
    if userInput < 1:
        return print("Вы не указали количество элементов!")
    elif userInput == 1:
        return print(startNumber)
    else:
        result += startNumber
        startNumber *= (-0.5)
        return sum_series_numbers(userInput - 1, result, startNumber)

userInput = int(input("Введите количество элементов: "))
sum_series_numbers(userInput, result, startNumber)