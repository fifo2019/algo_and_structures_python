"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
import sys
from pympler import asizeof


class Name:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = 18
        self.address = 'Moskau'
        self.phone = +79999999990


class Name_slots:
    __slots__ = ['name', 'age', 'address', 'phone']
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = 18
        self.address = 'Moskau'
        self.phone = +79999999990


name_one = Name('Имя', 21, 'Saratov', 555555)
name_two = Name_slots('Имя', 21, 'Saratov', 555555)

print(name_one.__dict__)
print(name_two.__slots__)

print(asizeof.asizeof(name_one))
print(sys.getsizeof(name_one))
print(asizeof.asizeof(name_two))
print(sys.getsizeof(name_two))