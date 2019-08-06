"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def addition(one, two):
    return int(one + two)


def subtraction(one, two):
    return  int(one - two)


def division(one, two):
    try:
        return one / two
    except ZeroDivisionError:
        print("На нуль делить нельзя!")


def multiplication(one, two):
    return int(one * two)


def valid_input(userInput):
    if userInput == "+" or userInput == "-" or userInput == ":" or userInput == "*" or userInput == "0":
        return "valid"


def calculator():
    operation = input("Посчитаем? Выбири операцию для вычисления (+, -, :, *) для выхода - 0!:")

    if valid_input(operation) != "valid":
        print("Вы ввели недопустимое значение! По пробуйте ещё раз!")
        calculator()

    if operation == "0":
        print("Всего наилучшего!")
        return

    try:
        one = int(input("Введите первое число:"))
        two = int(input("Введите второе число:"))

        if operation == "+":
            print(f"{one} + {two} = ", addition(one, two))
        elif operation == "-":
            print(f"{one} - {two} = ", subtraction(one, two))
        elif operation == ":":
            print(f"{one} : {two} = ", division(one, two))
        elif operation == "*":
            print(f"{one} * {two} = ", multiplication(one, two))

        calculator()
    except ValueError:
        print("Вы ввели недопустимое значение! Попробуйте снова!")
        calculator()

print("Программа КАЛЬКУЛЯТОР!")
calculator()