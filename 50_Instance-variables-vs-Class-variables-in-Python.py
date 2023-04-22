class Student:
    serial = 0  # class variable
    school = 'KV No.1 A.F.S Chakeri Kanpur'  # class variable

    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age      # instance variable
        Student.serial += 1  # instance variable

    def showDetails(self):
        print(
            f'{Student.serial}. {self.name} has age {self.age} and studies in {self.school}.')


s1 = Student('Aman Kumar Gupta', 20)
s1.showDetails()  # same as Student.showDetails(s1)

s2 = Student('Roshan Dash', 21)
s2.school = 'Mothers Public School, Odisha'
s2.showDetails()

Student.school = 'KV Andhara'
s3 = Student('Tepela Shubham', 21)
Student.showDetails(s3)

s4 = Student('Shobhan Parida', 20)
s4.showDetails()
'''
OUTPUT

1. Aman Kumar Gupta has age 20 and studies in KV No.1 A.F.S Chakeri Kanpur.
2. Roshan Dash has age 21 and studies in Mothers Public School, Odisha.
3. Tepela Shubham has age 21 and studies in KV Andhara.
4. Shobhan Parida has age 20 and studies in KV Andhara.
'''
