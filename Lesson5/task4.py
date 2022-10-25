from collections import OrderedDict
from timeit import repeat

def methods_dict():
    my_dict = {}
    for i in range(1000):
        my_dict[i] = 2

    for i in my_dict:
        my_dict.items()
    for i in my_dict:
        my_dict.keys()

    for i in my_dict:
        my_dict.get(i)


def methods_orderdict():
    my_dict = OrderedDict()
    for i in range(1000):
        my_dict[i] = 2

    for i in my_dict:
        my_dict.items()
    for i in my_dict:
        my_dict.keys()

    for i in my_dict:
        my_dict.get(i)

print(repeat("methods_dict()", globals=globals(), repeat=3, number=1000))
print(repeat("methods_orderdict()", globals=globals(), repeat=3, number=1000))
# Скорость выполнения методов в обычном словаре быстрее.
# orderdict целесообразно использовать только в отдельных случаях,
# когда явно показываем, что нам важен именно порядок следования элементов.
# существует специальный метод  .popitem(), со значение last=True если необходимо удалить последнюю пару или last=False
# если необходимо удалить первые элемент.
