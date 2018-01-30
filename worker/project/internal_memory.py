import string
import random
from memory_profiler import memory_usage,profile

@profile
def my_func(a,n=100):
    '''
    a = 10*10*[1]
    del a
    b = 2**5*[2]
    del b
    c = 3**3
    del c
    d = 4**4
    del d
    '''

    import time
    time.sleep(2)
    b = [a]*n
    time.sleep(1)
    return b
if __name__ == "__main__":
    usage=memory_usage((my_func, (1,), {'n': int(1e6)}))
