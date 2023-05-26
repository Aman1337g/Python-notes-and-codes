class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Mammal(Animal):
    def speak(self):
        print("Mammal sound")

class Bird(Animal):
    def speak(self):
        print("Bird sound")

class Dog(Mammal, Bird):
    def speak(self):
        print("Dog sound")

dog = Dog("Buddy")
dog.speak()
print(dog.name)
'''
OUTPUT

Dog sound
Buddy
'''