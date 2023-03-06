# calculating geometric mean

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)


a = 2
b = 7
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculateGmean(a, b)

'''
OUTPUT

1.5555555555555556
'''


# printing greater number

def greater(a, b):
    if (a > b):
        print(a, "is greater than", b)
    elif (a == b):
        print(a, 'is equal to', b)
    else:
        print(b, 'is greater than', a)


a = 98
b = 23
greater(a, b)
c = 45
d = 89
greater(c, d)

'''
OUTPUT

98 is greater than 23
89 is greater than 45
'''


# printing lesser number


def isLesser(a, b):
    if (a < b):
        print("First number is lesser than second number!!")
    elif (a == b):
        print("First number is equal to second number!!")
    else:
        print("Second number is lesser than first number!!")


c = 23
d = 2
isLesser(c, d)

'''
OUTPUT

Second number is lesser than first number!!
'''
