from emp import Employee

e1 = Employee('Shobhan Parida')
print(e1.name)
print(len(e1))
# in case str method is commented out repr method will be executed in place of it
print(str(e1))
print(repr(e1))
e1()
'''
OUTPUT

Shobhan Parida
14
Employee name is Shobhan Parida. str
Employee name is Shobhan Parida. repr
'''
