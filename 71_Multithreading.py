import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(0.5)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(0.5)

if __name__ == '__main__':
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Threads have finished executing.")
'''
OUTPUT

1
a
2
b
3
c
4
d
5
e
6
f
7
g
8
h
9
i
10
j
Threads have finished executing.
'''