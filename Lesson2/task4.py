

def sum_el(n=None, sum=0.0, el=1, s=0):

    if n == None:
        n = int(input('введите'))
        sum_el(n)

    else:
        if n > 0:
            n -= 1
            s += 1
            a = el * -0.5
            sum += a
            sum_el(n, sum, el, s)
        else:
            return print(f'Количество элементов - {s}, их сумма: {sum}')

sum_el()        