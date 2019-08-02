# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

numberFive = 5
numberSix = 6

print(f"Сдвиг {numberFive} на два знака вправа : {numberFive >> 2}, влево: {numberFive << 2}.")
print(f"AND: {numberFive & numberSix}; OR: {numberFive | numberSix}; NOT: {numberFive ^ numberSix}")
