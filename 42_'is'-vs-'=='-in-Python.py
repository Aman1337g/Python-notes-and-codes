a = 'aman kumar gupta'
b = 'aman kumar gupta'
print(a is b)  # True
print(a == b)  # True

a = [1, 2, 3]
b = (1, 2, 3)
print(a is b)  # False
print(a == b)  # False

a = None
b = None
print(a is b)  # True
print(a == b)  # True

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(a is b)  # False
print(a == b)  # True
