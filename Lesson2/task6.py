from random import randint

def luck(num=None, attempt=10):
    if num == None:
        num = randint(0, 100)
        luck(num)
    else:
        if attempt == 0:
            return f' Попытки закончились, загаданное число: {num}'
        else:
            att = int(input('Введите число'))
            if att == num:
                print(f'вы угадали {num}')
            else:
                attempt -= 1
                if att > num:
                    print(f'Не угадали, загаданное число меньше, осталось {attempt} попыток')
                    luck(num, attempt)
                else:
                    print(f'Не угадали, загаданное число больше, осталось {attempt} попыток')
                    luck(num, attempt)

luck()