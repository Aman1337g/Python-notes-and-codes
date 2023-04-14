class Student:
    name = "Aman Kumar Gutpa"
    roll_id = "B121006"
    age = 20

    def title():
        print("--------------------Student Information--------------------")

    def info(self):
        print(
            f'My name is {self.name}, age is {self.age} and my roll id is {self.roll_id}.')


Student.title()
ob1 = Student()
ob1.info()

ob2 = Student()
ob2.name = 'Mridul Tripathi'
ob2.age = 21
ob2.roll_id = 'B121030'
ob2.info()

ob3 = Student()
ob3.name = 'Jyotideep Acharjee'
ob3.roll_id = 'B121022'
ob3.info()
'''
OUTPUT

--------------------Student Information--------------------
My name is Aman Kumar Gutpa, age is 20 and my roll id is B121006.
My name is Mridul Tripathi, age is 21 and my roll id is B121030.
My name is Jyotideep Acharjee, age is 20 and my roll id is B121022.
'''
