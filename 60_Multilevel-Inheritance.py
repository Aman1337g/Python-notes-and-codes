class Grandfather:
    def __init__(self,name1,occupation):
        self.name1 = name1
        self.occ = occupation
    def show(self):
        print('show method of Grandfather class called !!')
        print(f'Grandfather : {self.name1}, Occupation : {self.occ}\n')

class Father(Grandfather):
    def __init__(self,name1, name2):
        super().__init__( name1,'Archaeologist')
        self.name2 = name2
    def show(self):
        super().show()
        print('show method of Father class called !!')
        print(f'Father : {self.name2}, Occupation : {self.occ}\n')

class Child(Father):
    def __init__(self,name1, name2, name3):
        Father.__init__(self, name1, name2)
        self.name3 = name3
    def show(self):
        super().show()
        print('show method of Child class called !!')
        print(f'Child : {self.name3}, Occupation : {self.occ}\n')

ob = Child('Ankit Kumar Gupta', 'Hajmola Gupta', 'Child Gupta')
ob.show()
print(Child.mro())
'''
OUTPUT

show method of Grandfather class called !!
Grandfather : Ankit Kumar Gupta, Occupation : Archaeologist

show method of Father class called !!
Father : Hajmola Gupta, Occupation : Archaeologist

show method of Child class called !!
Child : Child Gupta, Occupation : Archaeologist

[<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Grandfather'>, <class 'object'>]
'''