i = 0


class Student:

    def __init__(self, id, name, a):
        global i
        self.name = name
        self.age = a
        self.roll = id
        i += 1

    def info(self):
        global i
        print(f'{i} Name : {self.name}, Roll_ID : {self.roll}, Age : {self.age}')


print("--------------------Student Details--------------------")

s1 = Student('Aman Kumar Gupta', 'B121006', 20)
print('Memory location of old s1 :', id(s1))
s1.info()
s2 = Student('B121008', 'Arnab Mohanty', 21)
s2.info()
s3 = Student('B121012', 'Karthik Bankapalli', 20)
s3.info()
s1 = Student(name='Aman Kumar Gupta', id='B121006', a=20)
s1.info()
print('Memory location of new s1 :', id(s1))
'''
OUTPUT

--------------------Student Details--------------------
1 Name : B121006, Roll_ID : Aman Kumar Gupta, Age : 20
2 Name : Arnab Mohanty, Roll_ID : B121008, Age : 21
3 Name : Karthik Bankapalli, Roll_ID : B121012, Age : 20
4 Name : Aman Kumar Gupta, Roll_ID : B121006, Age : 20
Memory location of new s1 : 2488269809808
'''
