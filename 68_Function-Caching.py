from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(x):
    time.sleep(5)
    print(x)

fx(1)
fx(12)
fx(69)
fx(100)

fx(1)
fx(12)
fx(69)
fx(100)
fx(61)