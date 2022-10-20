


def task(num, even=0, odd=0):
    even = even
    odd = odd
    if num <= 0:
        return print(f"Четных: {even}, Нечетных: {odd}")
    else:
        a = num % 10
        if a % 2 == 0:
            even += 1
            num = num // 10
            task(num, even, odd)
        else:
            odd += 1
            num = num // 10
            task(num, even, odd)


task(1234345)