from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(x):
    time.sleep(5)
    return x

print(fx(1))
print(fx(12))
print(fx(69))
print(fx(100))

print(fx(1))
print(fx(12))
print(fx(69))
print(fx(100))
print(fx(61))
'''
OUTPUT

1
12
69
100
1
12
69
100
61
'''