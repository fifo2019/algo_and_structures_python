# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))
thirdNumber = int(input("Введите третье число: "))

if firstNumber == secondNumber or secondNumber == thirdNumber or firstNumber == thirdNumber:
    print("Вы ввели одинаковые числа для сравнения!")
elif firstNumber < secondNumber < thirdNumber or thirdNumber < secondNumber < firstNumber:
    print("Среднее число - ", secondNumber)
elif secondNumber < firstNumber < thirdNumber or thirdNumber < firstNumber < secondNumber:
    print("Среднее число - ", firstNumber)
else:
    print("Среднее число - ", thirdNumber)