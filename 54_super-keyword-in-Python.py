# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def info(self):
#         print(f'Employee name is {self.name} and id is {self.id}.PARENT CLASS')


# class Programmer(Employee):
#     def __init__(self, name, id, lang):
#         super().__init__(name, id)
#         self.lang = lang

#     def info(self):
#         print(
#             f'Employee name is {self.name} and id is {self.id} and language uses is {self.lang}.CHILD CLASS')
#         super().info()


# e1 = Employee('Aman Kumar Gupta', 'B121006')
# e1.info()

# e2 = Programmer('Roshan Dash', 'B121046', 'HTML CSS JS C++ C Python SQL')
# e2.info()
# '''
# OUTPUT

# Employee name is Aman Kumar Gupta and id is B121006.PARENT CLASS
# Employee name is Roshan Dash and id is B121046 and language uses is HTML CSS JS C++ C Python SQL.CHILD CLASS
# Employee name is Roshan Dash and id is B121046.PARENT CLASS
# '''
