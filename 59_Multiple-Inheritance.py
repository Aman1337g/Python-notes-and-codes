class Programmer:
    def __init__(self,name,language):
        self.name = name
        self.lang = language
    def show(self):
        print(f'The name of programmer is {self.name} and language uses is {self.lang}.')

class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.sub = subject
    def show(self):
        print(f'The name of teacher is {self.name} and subject teaches is {self.sub}.')

class PartTimer(Programmer, Teacher):
    def __init__(self, name, language, subject):
        print('Person is doing part timing as a Teacher and Programmer !!')
        super().__init__(name, language)
        self.sub = subject
    def show(self):
        print(f'Printing details in PartTimer Class :\nName : {self.name}\nProgramming Language : {self.lang}\nSubject : {self.sub}.')

ob = PartTimer('Aman Kumar Gupta', 'C++, Python', 'Mathematics')
ob.show()
print()
Teacher.show(ob)
Programmer.show(ob)
print(f'\nmro(method resolution order) : {PartTimer.mro()}')
'''
OUTPUT

Person is doing part timing as a Teacher and Programmer !!
Printing details in PartTimer Class :
Name : Aman Kumar Gupta
Programming Language : C++, Python
Subject : Mathematics.

The name of teacher is Aman Kumar Gupta and subject teaches is Mathematics.
The name of programmer is Aman Kumar Gupta and language uses is C++, Python.

mro(method resolution order) : [<class '__main__.PartTimer'>, <class '__main__.Programmer'>, <class '__main__.Teacher'>, <class 'object'>]
'''