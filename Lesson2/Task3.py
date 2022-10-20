def task(num, even=""):

    if num <= 0:
        return print(even)
    else:
        a = num % 10
        even = even + str(a)
        num = num // 10
        task(num, even)



task(1234345)