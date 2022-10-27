
from pympler import asizeof
import time
from memory_profiler import memory_usage

# Код взял из основ, хотел с помощью слот уменьшить кол во занимаемой памяти


m1 = memory_usage()
class TrafficLight:
    def __init__(self):
        self.color1 = 'Red'
        self.color2 = 'Yellow'
        self.color3 = 'Green'

    count = 0

    def frest(self):
        if self.count == 0:
            print(self.color1)
        elif self.count == 1:
            time.sleep(1)
            print(self.color2)
        elif self.count == 2:
            time.sleep(1)
            print(self.color3)
        TrafficLight.count += 1
    def running(self):
        run = TrafficLight()
        run.frest()
        run.frest()
        run.frest()

r = TrafficLight().running()
print(asizeof.asizeof((r)))

m2 = memory_usage()
mem_diff = m2[0] - m1[0]
print(mem_diff)


m3 = memory_usage()
class TrafficLight2:
    __slots__ = ['color1', 'color2', 'color3']
    def __init__(self):
        self.color1 = 'Red'
        self.color2 = 'Yellow'
        self.color3 = 'Green'
    count = 0

    def frest(self):
        if self.count == 0:
            print(self.color1)
        elif self.count == 1:
            time.sleep(1)
            print(self.color2)
        elif self.count == 2:
            time.sleep(1)
            print(self.color3)
        TrafficLight2.count += 1
    def running(self):
        run = TrafficLight2()
        run.frest()
        run.frest()
        run.frest()

d = TrafficLight2().running()
print(asizeof.asizeof((d)))
m4 = memory_usage()
mem_diff2 = m4[0] - m3[0]
print(mem_diff2)
