a = 343
b = 23

print(f"{a} is greater than {b}") if (a > b) else print(
    "a and b are equal") if (a == b) else print(f"{b} is greater than {a}")

c = "hello" if (a > b) else "douche" if (a == b) else "lucifer"
print(c)

'''
OUTPUT

343 is greater than 23
hello
'''
