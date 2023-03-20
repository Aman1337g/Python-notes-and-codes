# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")
# '''
# OUTPUT

# Enter the number: 4
# Multiplication table of 4 is:
# 4 X 1 = 4
# 4 X 2 = 8
# 4 X 3 = 12
# 4 X 4 = 16
# 4 X 5 = 20
# 4 X 6 = 24
# 4 X 7 = 28
# 4 X 8 = 32
# 4 X 9 = 36
# 4 X 10 = 40
# Some imp lines of code
# End of program
# '''


# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")

# except IndexError:
#     print("Index Error")
# '''
# OUTPUT

# Enter an integer: aman
# Number entered is not an integer.
# '''


try:
    a = input("Enter number1 : ")
    b = int(input("Enter number2 : "))
    print(a+b)
except Exception as e:
    print(e)

print("Program ends !!")
'''
OUTPUT

Enter number1 : 4
Enter number2 : 2
can only concatenate str (not "int") to str
Program ends !!
'''
