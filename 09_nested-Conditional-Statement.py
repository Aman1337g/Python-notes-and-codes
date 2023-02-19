a = int(input("Enter a number : "))
if (a > 0):
    if (a > 0 and a < 10):
        print(a, "is between 0 and 10.")
    elif (a == 10):
        print(a, "is equal to 10.")
    elif (a > 10 and a < 20):
        print(a, "is between 10 and 20")
    elif (a == 20):
        print(a, "is equal to 20.")
    else:
        print(a, "is greater than 20.")
elif (a == 0):
    print(a, "is equal to zero.")
else:
    print(a, "is negative.")
print("I am happy now !!")

'''
OUTPUT

Enter a number : 18
18 is between 10 and 20
I am happy now !!
'''
