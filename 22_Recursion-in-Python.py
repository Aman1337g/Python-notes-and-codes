# factorial(7) = 7*6*5*4*3*2*1 = 5040
# factorial(6) = 6*5*4*3*2*1 = 720
# factorial(5) = 5*4*3*2*1 = 120
# factorial(4) = 4*3*2*1 = 24
# factorial(3) = 3*2*1 = 6
# factorial(0) = 1

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        factorial = n*fact(n-1)
    return factorial


n = int(input("Enter a number : "))
print(f'Factorial of {n} is : {fact(n)}')
'''
OUTPUT

Enter a number : 8
Factorial of 8 is : 40320
'''

# fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)
# 0 1 1 2 3 5 8 13 ....


def fibo(n):
    if n == 0:
        return 0
    elif (n == 1):
        return 1
    else:
        fib = fibo(n-1)+fibo(n-2)
        return fib


n = int(input("Enter a number : "))
print(f"Fibonacci sequence containing {n} values : ")
for i in range(n):
    print(fibo(i), end=" ")
'''
OUTPUT

Fibonacci sequence containing 10 values :
0 1 1 2 3 5 8 13 21 34
'''
