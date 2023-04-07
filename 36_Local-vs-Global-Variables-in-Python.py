x = 10


def func():
    print("Hello user !!")
    # x = 56
    # print("Local x :", x)
    global x  # globally changing value of x
    x = 38
    print("Local x :", x)


print("Global x :", x)
func()
print("Global x :", x)
'''
OUTPUT

Global x : 10
Hello user !!
Local x : 38
Global x : 38
'''
