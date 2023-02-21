colors = ["Red", "Green", "Yellow", "Blue", "White"]
for color in colors:
    print(color)
    for i in color:
        print(i)

'''
OUTPUT

Red
R
e
d
Green
G
r
e
e
n
Yellow
Y
e
l
l
o
w
Blue
B
l
u
e
White
W
h
i
t
e
'''


# using range()

for i in range(5):
    print(i, end=",")

'''
OUTPUT

0,1,2,3,4,
'''


for i in range(5, 20):
    print(i, end=", ")

'''
OUTPUT

5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
'''


for i in range(1, 12, 2):
    print(i, end=" ")

'''
OUTPUT

1 3 5 7 9 11
'''
