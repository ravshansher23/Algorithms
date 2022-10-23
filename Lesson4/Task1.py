from timeit import timeit
def test_list():
    my_list = list(range(1000))
    return my_list

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
my_list = test_list()
print(timeit("func_1(my_list)", globals=globals(), number=1000))

def func_2(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr

print(timeit("func_2(my_list)", globals=globals(), number=1000))


#В func_2 расчет проходит быстрее т.к. цикл for и так проходится по каждому числу и необходимости индексировать список нет.