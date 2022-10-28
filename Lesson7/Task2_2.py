from random import randint
from timeit import timeit



def find_mid(m):
    list_obj = list(randint(1, 100) for _ in range(2 * m + 1))
    w = sorted(list_obj[:])
    while len(list_obj) > m + 1:
        list_obj.remove(max(list_obj))

    return max(list_obj), w


print(find_mid(5))
print(timeit("find_mid(5)", globals=globals(), number=1000))
print(find_mid(50))
print(timeit("find_mid(50)", globals=globals(), number=1000))
print(find_mid(500))
print(timeit("find_mid(500)", globals=globals(), number=1000))
