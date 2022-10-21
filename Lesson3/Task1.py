import time

def dec_func(func):
    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        print(finish - start)
    return wrapper()
#Для запуска пункта А нужно раскомментировать декораторы
# O(n) линейная сложность
# @dec_func
def fill_list(n=50000):
    filled_list = []
    while n > 0:
        filled_list.append(n)
        n = n - 1
    return filled_list


# O(n) линейная сложность
# @dec_func
def fill_dict(n=50000):
    filled_dict = {}
    while n > 0:
        filled_dict[n] = n
        n = n - 1
    return filled_dict


# Сложность одинаковая, но длительность выполнения при заполнении словаря больше т.к. объем данных больше

#b)

test_list = fill_list(n=500000)
test_dict = fill_dict(n=500000)

@dec_func
# O(n) линейная сложность
def select_obj(n=470000):
    return test_list.index(n)
@dec_func
# O(1) константная сложность
def select_k(n=470000):
    return test_dict[n]

# скорость получения объекта из списка меньше т.к. надо пройти по списку чтоб получить данные, в словаре можно по ключу получить данные


#c)

@dec_func
# O(n) линейная сложность
def pop_obj(n=470000):
    test_list.remove(n)
@dec_func
# O(1) константная сложность
def pop_k(n=470000):
    return test_dict.pop(n)

# скорость получения объекта из списка меньше т.к. надо пройти по списку чтоб получить данные, в словаре можно по ключу получить данные