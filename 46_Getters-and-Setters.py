class Student:
    def __init__(self, name, id):
        self.n = name
        self._roll = id

    def info(self):
        print(f'My name is {self.n} and roll_id is {self._roll}')

    @property
    def roll(self):
        return self._roll

    @roll.setter
    def roll(self, new_roll):
        self._roll = new_roll


s1 = Student('Aman Kumar Gupta', 'B121006')
s1.info()
print(s1.roll)
s1.roll = 'B121048'
s1.info()
'''
OUTPUT

My name is Aman Kumar Gupta and roll_id is B121006
B121006
My name is Aman Kumar Gupta and roll_id is B121048
'''
