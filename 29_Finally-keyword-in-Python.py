try:
    t = (1, 2, 23, 3.22, "aman", 8.2323, False)
    i = int(input('Enter an index : '))
    print(t[i])
except Exception as error:
    print(error)
finally:
    print("I am always executed !!")
'''
OUTPUT

Enter an index : 8
tuple index out of range
I am always executed !!
'''


try:
    t = (1, 2, 23, 3.22, "aman", 8.2323, False)
    i = int(input('Enter an index : '))
    print(t[i])
except Exception as error:
    print(error)
# finally:
#     print("I am always executed !!")

print("I am always executed !!")
'''
OUTPUT

Enter an index : 8
tuple index out of range
I am always executed !!
'''


def func():
    try:
        t = (1, 2, 23, 3.22, "aman", 8.2323, False)
        i = int(input('Enter an index : '))
        print(t[i])
        return 1
    except Exception as error:
        print(error)
        return 0

    # finally:
    #     print("I am always executed !!")
    print("I am always executed !!")


x = func()
print(x)
'''
OUTPUT

Enter an index : 3
3.22
1
'''


def func():
    try:
        t = (1, 2, 23, 3.22, "aman", 8.2323, False)
        i = int(input('Enter an index : '))
        print(t[i])
        return 1
    except Exception as error:
        print(error)
        return 0

    finally:
        print("I am always executed !!")
    # print("I am always executed !!")


x = func()
print(x)
'''
OUTPUT

Enter an index : 8
tuple index out of range
I am always executed !!
0
'''
