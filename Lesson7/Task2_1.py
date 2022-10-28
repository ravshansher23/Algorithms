from random import randint
from timeit import timeit


def gnome_sort(lst_obj):
    for i in range(1, len(lst_obj)):
        while i != 0 and lst_obj[i] < lst_obj[i - 1]:
            lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
            i = i - 1
    return lst_obj



def find_mid(m):
    list_obj = list(randint(1, 100) for _ in range(2 * m + 1))
    list_obj = gnome_sort(list_obj)
    w = list_obj[:]
    ind_mid = len(list_obj) // 2
    return list_obj[ind_mid], w

print(find_mid(5))
print(timeit("find_mid(5)", globals=globals(), number=1000))
print(find_mid(50))
print(timeit("find_mid(50)", globals=globals(), number=1000))
print(find_mid(500))
print(timeit("find_mid(500)", globals=globals(), number=1000))