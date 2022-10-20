
def asd(num=0, f=0):
    if num == 0:
        return f
    else:
        f = num + f
        num = num - 1
        return asd(num, f)


def sum_of_num(n):
    first = asd(n)
    second = int(n * (n + 1) / 2)
    if first == second:
        print(f'Утверждение верно, сумма ={second}')
    else:
        print(f'Утверждение не верно, сумма ={second}, {first}')

sum_of_num(55)