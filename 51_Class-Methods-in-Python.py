class Employee:
    company = 'Apple'

    def info(self):
        print(f'Employee name is {self.name} and company is {self.company}')

    def changeCom(self):
        self.company = 'Google'

    @classmethod    # class method decorator
    def changeCom(cls, newComp):
        cls.company = newComp


e1 = Employee()
e1.name = 'Aman Kumar Gupta'
e1.info()

e2 = Employee()
e2.name = 'Prabhanjan Mishra'
e2.company = 'Microsoft'
e2.info()

e3 = Employee()
e3.name = 'Pratyush Kurhe'
e3.info()
print()
print(Employee.company, '\n')

e4 = Employee()
e4.changeCom('Tesla')
e4.name = 'Mridul Tripathi'
e4.info()
print('\n'+Employee.company)
'''
OUTPUT

Employee name is Aman Kumar Gupta and company is Apple
Employee name is Prabhanjan Mishra and company is Microsoft
Employee name is Pratyush Kurhe and company is Apple

Apple

Employee name is Mridul Tripathi and company is Tesla

Tesla
'''
