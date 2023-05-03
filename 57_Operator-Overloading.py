class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, c):
        return Complex(self.a+c.a, self.b+c.b)


c1 = Complex(1, 2)
print(c1)
c2 = Complex(23, 2)
print(c2)

print(c1+c2)
print(type(c1+c2))
'''
OUTPUT

1 + 2i
23 + 2i
24 + 4i
<class '__main__.Complex'>
'''


# Example 2


class Point:
    def __init__(self, a=0, b=0, c=0):
        self.i = a
        self.j = b
        self.k = c

    def __add__(self, point):
        return Point(self.i+point.i, self.j+point.j, self.k+point.k)

    def __sub__(self, point):
        return Point(self.i-point.i, self.j-point.j, self.k-point.k)

    def distance(self, p1, p2):
        temp = p1-p2
        return ((temp.i ** 2 + temp.j ** 2 + temp.k ** 2) ** 0.5)

    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'


p1 = Point(1, 2, 3)
print(p1)
p2 = Point(2, 3)
print(p2)

print('Distance between point p1 and p2 is', p1.distance(p1, p2))
'''
OUTPUT

1i + 2j + 3k
2i + 3j + 0k
Distance between point p1 and p2 is 3.3166247903554
'''
