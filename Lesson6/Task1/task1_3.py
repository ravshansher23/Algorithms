from Lesson6.Task1 import warp
from collections import namedtuple
from recordclass import recordclass
# Код с прошлого урока, произвел оптимизацию заменой namedtuple(0.0234375 MiB) на recordclass(0.00390625 MiB)
@warp.decor
def coll():
    count_company = int(input("Введите число компаний"))
    company_coll = namedtuple('Company', 'name profit1 profit2 profit3 profit4')

    val_dict = {}
    for i in range(count_company):
        company = company_coll(name=input("Введите название компании"), profit1=int(input("Введите прибыль за 1 квартал: ")),
                               profit2=int(input("Введите прибыль за 2 квартал: ")), profit3=int(input("Введите прибыль за 3 квартал: ")),
                               profit4=int(input("Введите прибыль за 4 квартал: ")))


        val_dict[company.name] = (company.profit1 + company.profit2 + company.profit3 + company.profit4) / 4


    all_profit = 0

    for i in val_dict.values():
        all_profit += i
    all_profit = all_profit / count_company

    for key, val in val_dict.items():
        if val > all_profit:
            print(f'Средняя прибыль {key} выше среднего')
        elif val < all_profit:
            print(f'Средняя прибыль {key} ниже среднего')
        else:
            print(f'Средняя прибыль {key} равна средней общей')


print(coll())

@warp.decor
def coll2():
    count_company = int(input("Введите число компаний"))
    company_coll = recordclass('Company', 'name profit1 profit2 profit3 profit4')

    val_dict = {}
    for i in range(count_company):
        company = company_coll(name=input("Введите название компании"), profit1=int(input("Введите прибыль за 1 квартал: ")),
                               profit2=int(input("Введите прибыль за 2 квартал: ")), profit3=int(input("Введите прибыль за 3 квартал: ")),
                               profit4=int(input("Введите прибыль за 4 квартал: ")))


        val_dict[company.name] = (company.profit1 + company.profit2 + company.profit3 + company.profit4) / 4


    all_profit = 0

    for i in val_dict.values():
        all_profit += i
    all_profit = all_profit / count_company

    for key, val in val_dict.items():
        if val > all_profit:
            print(f'Средняя прибыль {key} выше среднего')
        elif val < all_profit:
            print(f'Средняя прибыль {key} ниже среднего')
        else:
            print(f'Средняя прибыль {key} равна средней общей')


print(coll2())