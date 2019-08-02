# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

userInput = int(input("Введите трёхзначное число: "))
firstNumber = userInput % 1000 // 100
secondNumber = userInput % 100 // 10
thirdNumber = userInput % 10
print("Сумма трёх чисел = ", firstNumber + secondNumber + thirdNumber)
print("Произведение трёх чисел = ", firstNumber * secondNumber * thirdNumber)