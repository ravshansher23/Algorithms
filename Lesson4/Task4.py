from timeit import repeat


array = [1, 3, 1, 3, 4, 5, 1]
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)
    count_num = max(new_array)
    max_num = new_array.index(count_num)

    return f'Чаще всего встречается число {max_num + 1}, ' \
           f'оно появилось в массиве {count_num} раз(а)'

def func_3():
    max_num = max(array, key=array.count)
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {array.count(max_num)} раз(а)'
print(repeat("func_1()", globals=globals(), repeat=3, number=1000))
print(repeat("func_2()", globals=globals(), repeat=3, number=1000))
print(repeat("func_3()", globals=globals(), repeat=3, number=1000))

