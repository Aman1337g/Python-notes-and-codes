class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self._gender = 'Male'
        self.__id = id


print(Student.__dir__)
s1 = Student('aman', 20, 'B121006')
print(s1.__dir__)
print(s1.__dir__(), end='\n\n')   # methods availabe on s1 instance
print(s1.name)
print(s1.age)
print(s1._gender)
# print(s1.__id)      # cannot be accessed directly (AttributeError)
print(s1._Student__id)  # accessed indirectly

s1._gender = 'Female'
print(s1._gender)
'''
OUTPUT

<method '__dir__' of 'object' objects>
<built-in method __dir__ of Student object at 0x000002260DF16350>
['name', 'age', '_gender', '_Student__id', '__module__', '__init__', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

aman
20
Male
B121006
Female
'''
