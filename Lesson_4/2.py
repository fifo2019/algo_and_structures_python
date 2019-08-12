"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import timeit

primes = [2, 3]
last_crossed = [2, 3]


def without_sieve(n=3000,k=50):
    while len(primes) < n:
        candidate = primes[-1] + 2
        i = 0
        while i < len(primes):
            while last_crossed[i] < candidate:
                last_crossed[i] += primes[i]
            if last_crossed[i] == candidate:
                candidate += 2
                i = 0
            i += 1

        primes.append(candidate)
        last_crossed.append(candidate)

    return primes[k-1]



def using_sieve(n=3000, k=50):
    a = [x for x  in range(n+1)]

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b[k-1]

print(using_sieve()) # приблизительно 1.4 n=3000, k=50
print(without_sieve()) # приблизительно 0.00034 n=3000, k=50

print(timeit.timeit("using_sieve()", setup = 'from __main__ import using_sieve', number = 1000))
print(timeit.timeit("without_sieve()", setup = 'from __main__ import without_sieve', number = 1000))