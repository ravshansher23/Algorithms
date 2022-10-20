


def calc():
    operation = input('Выберите метод + - * /')
    if operation == "0":
        return f'Завершение работы'
    else:
        try:
            first_num = int(input('Введите 1-ое число'))
            second_num = int(input('Введите 2-ое число'))
        except Exception as err:
            print(err)

        if operation == "+":
            num = first_num + second_num
            return print(num), calc()
        elif operation == "-":
            num = first_num - second_num
            return print(num), calc()
        elif operation == "*":
            num = first_num * second_num
            return print(num), calc()
        elif operation == "/":
            if second_num > 0:
                num = first_num / second_num
                return print(num), calc()
            else:
                return print(f"На ноль делить нельзя"), calc()
        else:
            return print(f"Введен неверный метод"), calc()

calc()