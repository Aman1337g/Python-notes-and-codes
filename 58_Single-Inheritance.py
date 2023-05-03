class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print("The animal is eating.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed

    def bark(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name, breed='Ashera'):
        self.breed = breed
        super().__init__(name, 'African serval + Asian leopard')

    def eat(self):
        print('Likes to drink milk.')


dog = Dog("Fido", "Labrador Retriever")
print(dog.name)
print(dog.species)
print(dog.breed)
dog.eat()
dog.bark()
print()
cat = Cat('Anku')
print(cat.name)
print(cat.breed)
print(cat.species)
cat.eat()
'''
OUTPUT

Fido
Canine
Labrador Retriever
The animal is eating.
Woof!

Anku
Ashera
African serval + Asian leopard
Likes to drink milk.
'''
