from memory_profiler import memory_usage

def decor(func):
    def wrapper():
        m1 = memory_usage()
        func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff
    return wrapper