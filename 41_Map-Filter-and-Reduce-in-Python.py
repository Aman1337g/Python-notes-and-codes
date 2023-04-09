from functools import reduce  # for using reduce


def sq(x):
    return x*x


l = [1, 2, 3, 4]
print('Operand list :', l)
# Creating a new list with square of elements in 'list'

newl = [item**2 for item in l]
print('newl :', newl)

# method-2
newll = []
for item in l:
    newll.append(sq(item))
print('newll :', newll)

# Map
# return map object so convert it to list datatype implicitly
# lambda function can also be replaced with sq function above
newlist = list(map(lambda x: x*x, l))
print('newlist :', newlist)
'''
OUTPUT

Operand list : [1, 2, 3, 4]
newl : [1, 4, 9, 16]
newll : [1, 4, 9, 16]
newlist : [1, 4, 9, 16]
'''

# filter


def filter_fun(x):
    return x < 4


print(f'list : {l}')
filterList = filter(lambda x: x < 4, l)
print('filtered list using lambda function :', list(filterList))

# Method-2
print('filtered list using filter_fun() :', list(filter(filter_fun, l)))
'''
OUTPUT

list : [1, 2, 3, 4]
filtered list using lambda function : [1, 2, 3]
filtered list using filter_fun() : [1, 2, 3]
'''


# reduce

n = [1, 2, 3, 4, 5]
print('n :', n)
newn = reduce(lambda x, y: x*y, n)
print('newn :', newn)
'''
OUTPUT

n : [1, 2, 3, 4, 5]
newn : 120
'''
