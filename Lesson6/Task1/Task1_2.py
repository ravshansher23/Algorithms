
from json import dumps
from Lesson6.Task1 import warp
# Код взят с предыдущего урока, реализована оптимизация с помощью JSON
@warp.decor
def methods_dict():
    my_dict = {}
    for i in range(1000):
        my_dict[i] = 2
    return my_dict

print(methods_dict())

@warp.decor
def methods_dict2():
    my_dictw = {}
    my_dict = {}
    for i in range(1000):
        my_dict[i] = 2
        my_dictw = dumps(my_dict[i])
    return my_dictw

print(methods_dict2())