from timeit import repeat

nums = 4583932

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

print(repeat("revers(nums)", globals=globals(), repeat=3, number=1000))
print(repeat("revers_2(nums)", globals=globals(), repeat=3, number=1000))
print(repeat("revers_3(nums)", globals=globals(), repeat=3, number=1000))
print(f"C меморизацией")
def memoize(f):
    cache = {}
    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate

@memoize
def revers_4(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
def revers_5(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

print(repeat("revers_4(nums)", globals=globals(), repeat=3, number=1000))
print(repeat("revers_5(nums)", globals=globals(), repeat=3, number=1000))

print(f'Получилось, что с меморизацией оптимизированный рекурсивный код работает быстрее чем код с циклом ')