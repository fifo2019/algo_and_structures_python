"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
from random import random

bottom_line = int(input("Введите нижнюю границу чисел: "))
top_line = int(input("Введите верхнюю границу чисел: "))
calculate = random() * (top_line - bottom_line + 1) + bottom_line
print("Случайное целое число: ", int(calculate))

bottom_line = float(input("Введите нижнюю границу чисел: "))
top_line = float(input("Введите верхнюю границу чисел: "))
calculate = random() * (top_line - bottom_line + 1) + bottom_line
print("Случайное вещественное число: ", round(calculate, 3))

bottom_line = ord(input("Введите латинскую букву нижнюю границу: "))
top_line = ord(input("Введите латинскую букву верхнюю границу: "))
calculate = random() * (top_line - bottom_line + 1) + bottom_line
print("Cлучайный символ: ", chr(int(calculate)))