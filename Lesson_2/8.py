"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

userInput = int(input("Какое количество чисел в последовательности? "))
number = int(input("Какую цифру ищем? "))
count = 0
print("Введите числа подрят")
for i in range(1, userInput + 1):
    sequence = int(input(f"Число № {str(i)}: "))
    while sequence > 0:
        if sequence % 10 == number:
            count += 1
        sequence //= 10

print(f"Введено количество чисел {userInput} из них число {number} встречается {count} раз")
