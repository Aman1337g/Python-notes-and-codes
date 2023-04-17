class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(s):
        print(f'Student name is {s.name} and id is {s.id}')


class President(Student):
    def specialFun(s):
        print(f'Class President {s.name} gets free of cost meals !!')


s1 = Student('Aman Kumar Gupta', 'B121006')
s1.showDetails()
s2 = President('Harshit Goel', 'B123023')
s2.showDetails()
s2.specialFun()
'''
OUTPUT

Student name is Aman Kumar Gupta and id is B121006
Student name is Harshit Goel and id is B123023
Class President Harshit Goel gets free of cost meals !!
'''
