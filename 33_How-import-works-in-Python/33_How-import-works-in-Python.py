import math
print(math.pi)
'''
OUTPUT

3.141592653589793
'''

from math import pi, sqrt, pow
print(pi)
print(sqrt(196))
print(pow(2, 10))
'''
OUTPUT

3.141592653589793
14.0
1024.0
'''


from math import pi as p, sqrt, pow as power
print(p)
print(sqrt(81))
print(power(6, 2))
'''
OUTPUT

3.141592653589793
9.0
36.0
'''

import math as m
print(m.pi)
'''
OUTPUT

3.141592653589793
'''


from math import * # IMPORTING all function in math module
print(sin(45*pi/180))
print(tan(90*pi/180))
print(pi)
print(pi*sqrt(9))
'''
OUTPUT

0.7071067811865476
1.633123935319537e+16
3.141592653589793
9.42477796076938
'''


import math
print(dir(math))  # printing all functions in math module
print(math.sin(math.radians(90)))
print(math.nan, type(math.nan))
'''
OUTPUT

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2',
'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite',
'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm',
'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
1.0
nan <class 'float'>
'''


# from aman import welcome, aman
from aman import *
import aman as a
welcome()
print(a.aman)
'''
OUTPUT

Enter your name : Abhas Agarwal
Welcome, Abhas Agarwal to this 100 days of code !!🥳
Aman is a good boy !!😇
'''
