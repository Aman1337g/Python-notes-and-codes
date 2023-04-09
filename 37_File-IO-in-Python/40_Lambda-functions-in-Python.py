def cube(x):
    return x**3


print(cube(6))

# other way to write


def cube(x): return x**3


print(cube(6))
'''
OUTPUT

216
27
'''


# USING function as an argument

def farg(fx, value):
    return fx(value) + 20


print(farg(cube, 6))  # 236


def prod(x, y): return print(f'{x} * {y} = {x * y}')


prod(2, 3)
'''
OUTPUT

2 * 3 = 6
'''
