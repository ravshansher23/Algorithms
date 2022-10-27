
from json import dumps
from Lesson6.Task1 import warp
#Оптимизированный код
@warp.decor
def add_item():
    items = {}
    for i in range(1000):

        name = f'com{i}'
        price = i
        quantity = i + 1
        item = {name: [price, quantity]}
        items = dumps(item)
    return items

print(add_item())
#Код до оптимизации
@warp.decor
def add_item2():
    items = {}
    for i in range(1000):
        name = f'com{i}'
        price = i
        quantity = i + 1
        item = {name: [price, quantity]}
        items.update(item)

print(add_item2())

#Оптимизировал код с помощью JSON, он занимает меньше места т.к. после преобразования записывает данные в формате str