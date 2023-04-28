tup = (1, 2, 3)
lst = ('aman', 'sigma', 23, 32.2, False)

print("List of methods in tuple :")
print(dir(tup))
print()
print('List of methods in list :')
print(dir(lst))

# print(help(tup))


class Person:

    id = 'B121006'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
        self.college = 'IIIT Bhubaneswar'


print()
P = Person('Aman Kumar Gupta', 20)
print(P.name)
print(P.__dict__)  # display attributes as a dictionary
print(help(P))
'''
OUTPUT

List of methods in tuple :
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

List of methods in list :
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

Aman Kumar Gupta
{'name': 'Aman Kumar Gupta', 'age': 20, 'version': 1, 'college': 'IIIT Bhubaneswar'}
Help on Person in module __main__ object:

class Person(builtins.object)
 |  Person(name, age)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  id = 'B121006'

None
'''
