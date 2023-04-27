class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Student name is {self.name} and age is {self.age}.')

    @classmethod
    def fromStr(cls, string):   # class method as constructor
        return cls(string.split(',')[0], int(string.split(',')[1]))


s1 = Student('Aman Kumar Gupta', 89)
s1.info()

s2 = Student.fromStr('Harshit Goel,90')
print(s2.name)
print(s2.age)
s2.info()
'''
OUTPUT

Student name is Aman Kumar Gupta and age is 89.
Harshit Goel
90
Student name is Harshit Goel and age is 90.
'''
