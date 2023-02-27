for i in range(4):
    print(i)

'''
OUTPUT

0
1
2
3
'''

# while loop equivalent of above code

i = 0
while (i <= 3):
    print(i)
    i = i+1

print("Done with the loop!!")

'''
OUTPUT

0
1
2
3
Done with the loop!!
'''

n = int(input("Enter a number : "))
while (n < 28):
    n = int(input("Enter a number : "))
    print(n)

'''
OUTPUT

Enter a number : 23
Enter a number : 2
2
Enter a number : 3
3
Enter a number : 4
4
Enter a number : 44
44
'''

# decrementing while loop

i = 7
while (i >= 0):
    print(i)
    i = i - 1

'''
OUTPUT

7
6
5
4
3
2
1
0
'''

# else with while loop

count = 7
while (count > 5):
    print(count)
    count = count - 1
else:
    print("Inside else statement !!")

'''
OUTPUT

7
6
Inside else statement !!
'''
