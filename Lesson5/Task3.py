from timeit import repeat
from collections import deque
my_list = [i for i in range(1000)]
my_deq = deque([i for i in range(1000)])
# Сравнение append в списке и в Deque
def cl_append():
    for i in range(1000):
        my_list.append(i)
    return my_list
def deq_append():
    for i in range(1000):
        my_deq.append(i)
    return my_deq
print(f"Append list")
print(repeat("cl_append()", globals=globals(), repeat=3, number=1000))
print(f"Append deque")
print(repeat("deq_append()", globals=globals(), repeat=3, number=1000))
# Примерно одинаковые значения

# Сравнение pop в списке и в Deque
def cl_pop():
    for i in range(100):
        my_list.pop()
    return my_list
def deq_pop():
    for i in range(100):
        my_deq.pop()
    return my_deq
print(f"pop list")
print(repeat("cl_pop()", globals=globals(), repeat=1, number=100))
print(f"pop deque")
print(repeat("deq_pop()", globals=globals(), repeat=1, number=100))
# Примерно одинаковые значения
# Сравнение extend в списке и в Deque
n = [1, 2]
def cl_ex():
    for i in range(100):
        my_list.extend(n)
    return my_list
def deq_ex():
    for i in range(100):
        my_deq.extend(n)
    return my_deq
print(f"ex list")
print(repeat("cl_ex()", globals=globals(), repeat=3, number=1000))
print(f"ex deque")
print(repeat("deq_ex()", globals=globals(), repeat=3, number=1000))
# Примерно одинаковые значения, но deq чаще бывает быстрее
# Сравнение append_left и аналога в списке и в Deque
def cl_append_left():
    for i in range(100):
        my_list.insert(0, i)
    return my_list
def deq_append_left():
    for i in range(100):
        my_deq.appendleft(i)
    return my_deq
print(f"append_left list")
print(repeat("cl_append_left", globals=globals(), repeat=3, number=1000))
print(f"append_left deque")
print(repeat("deq_append_left()", globals=globals(), repeat=3, number=1000))
# В deque намного быстрее
# Сравнение pop_left и аналога в списке и в Deque
def cl_pop_left():
    for i in range(100):
        my_list.pop(0)
    return my_list
def deq_pop_left():
    for i in range(100):
        my_deq.popleft()
    return my_deq
print(f"popleft list")
print(repeat("cl_pop_left", globals=globals(), repeat=3, number=1000))
print(f"popleft deque")
print(repeat("deq_pop_left()", globals=globals(), repeat=3, number=1000))
# В deque намного быстрее
# Сравнение extendleft и аналога в списке и в Deque
d = (1, 2)
def cl_exleft():
    for i in range(100):
        my_list.insert(0, d)
    return my_list
def deq_exleft():
    for i in range(100):
        my_deq.extendleft(d)
    return my_deq
print(f"extendleft list")
print(repeat("cl_exleft()", globals=globals(), repeat=1, number=10))
print(f"extendleft deque")
print(repeat("deq_exleft()", globals=globals(), repeat=1, number=10))
# В deque намного быстрее
# Сравнение получения елемента в списке и в Deque
def cl_elem():
    for i in range(1000):
        my_list[i] = i
    return my_list
def deq_elem():
    for i in range(1000):
        my_deq[i] = i
    return my_deq
print(f"elem list")
print(repeat("cl_elem()", globals=globals(), repeat=3, number=1000))
print(f"elem deque")
print(repeat("deq_elem()", globals=globals(), repeat=3, number=1000))
# Получение случайного числа из списка быстрее чем из deque
