def average(a, b=2, c=5, d=3):  # a = required argument , b,c,d = default arguments
    average = (a+b+c+d)/4
    print("Average is", average)


average(1)
average(2)
average(2, 3, 4, 5)
average(2, 3, 4)
average(d=2, a=3, b=4)

'''
OUTPUT

Average is 2.75
Average is 3.0
Average is 3.5
Average is 3.0
Average is 3.5
'''

# variable length argument

# ARBITRARY ARGUMENTS


def sum(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Average of elements :", sum/len(numbers))


sum(4, 5, 2)
sum(1, 2, 3, 4)

'''
OUTPUT

<class 'tuple'>
Average of elements : 3.6666666666666665
<class 'tuple'>
Average of elements : 2.5
'''

# KEYWORD ARBITRARY ARGUMENTS


def name(**n):
    print(type(n))
    print("Hello,", n["fname"], n["mname"], n["lname"])


name(fname="Aman", lname="Gupta", mname="Kumar")

'''
OUTPUT

<class 'dict'>
Hello, Aman Kumar Gupta
'''


# return


def hel():
    return "Hello World!!"


c = hel()
print(type(c))
print(c)
print(hel())

'''
OUTPUT

Hello World!!
Hello World!!
'''
