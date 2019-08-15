"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

quentityEnterprises = int(input("Введите количество предприятий: "))

enterpris = collections.defaultdict(list)

for i in range(quentityEnterprises):
    nameEnterpris = input(f'Наименование {i + 1}-ого предприятия: ')
    profitQuarterly = [(int(input(f'Введите прибыль за {j + 1}-й квартал: '))) for j in range(4)]
    enterpris[nameEnterpris] = sum(profitQuarterly)

profitAverage = sum(enterpris.values()) / quentityEnterprises
print(f'Средняя прибыль {profitAverage}')

for i in enterpris:
    if enterpris[i] < profitAverage:
        print(f'Предприятие "{i}" имеет прибыль ниже средней: ({enterpris[i]})')
    elif enterpris[i] > profitAverage:
        print(f'Предприятие "{i}" имеет прибыль выше средней: ({enterpris[i]})')