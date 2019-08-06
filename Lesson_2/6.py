"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

from random import randint


print("Попробуй угодай число от 0 до 100! У Вас 10 попыток!")

number = randint(1, 100)
attempt = 1


def guess_number(number, attempt):
    guess = int(input(f"Попытка № {attempt} - Назовите число: "))
    while guess != number:
        if attempt > 10:
            return print("Вы проиграли!")
        if guess > number:
            print("Меньше..")
        else:
            print("Больше..")
        attempt += 1
        guess = int(input(f"Попытка № {attempt} - Назовите число: "))
    print("Количество попыток было ", attempt)
    print("Вам удалось отгадать число!", number)


guess_number(number, attempt)

