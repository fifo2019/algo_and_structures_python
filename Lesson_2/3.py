"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
stringNumbers = ''


def reverse_numbers(userInput, stringNumbers):
    balance_of_ten = userInput % 10
    if userInput < 10:
        stringNumbers += str(userInput)
        return print(stringNumbers)
    else:
        stringNumbers += str(balance_of_ten)
        return reverse_numbers(userInput // 10, stringNumbers)


userInput = int(input("Введите число:"))
reverse_numbers(userInput, stringNumbers)