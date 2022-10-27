from numpy import array
from collections import deque
from Lesson6.Task1 import warp

# Код взял из предыдущего урока сравнение LC, deque и numpy.array, deque и numpy.array используют меньше памяти, чем LC, при
# этом deque и numpy.array используют примерно одинаковое кол во памяти




# Сравнение append в списке и в Deque
@warp.decor
def cl_append():
    my_list = [i for i in range(1000)]

    return my_list


@warp.decor
def deq_append():
    my_deq = deque([i for i in range(1000)])

    return my_deq
@warp.decor
def numpy_append():
    my_deq = array([i for i in range(1000)])

    return my_deq
print(cl_append())
print(deq_append())
print(numpy_append())