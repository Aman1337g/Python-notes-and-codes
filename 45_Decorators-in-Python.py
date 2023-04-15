def greet(fx):
    def m_fx(*args, **kwargs):
        print("Good Morning !!")
        fx(*args, **kwargs)
        # *args is interpreted as tuple
        # *kwargs is interpreted as dictionary
        print('Thank for using this function !!')
    return m_fx


@greet
def hello():
    print("Hello User")


@greet
def table(n):
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')


hello()
print()
greet(hello)()
print()
table(5)
print()
greet(table)(5)
'''
OUTPUT

Good Morning !!
Hello User
Thank for using this function !!

Good Morning !!
Good Morning !!
Hello User
Thank for using this function !!
Thank for using this function !!

Good Morning !!
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Thank for using this function !!

Good Morning !!
Good Morning !!
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
Thank for using this function !!
Thank for using this function !!
'''
