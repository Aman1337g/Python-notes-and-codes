def fun(fx):        # decorator
    def m_fx(*args, **kwargs):
        print("😁 ", end='')
        fx(*args, **kwargs)
        print("😁")
    return m_fx


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @fun
    def work(self):
        print(f"{self.name} is working.", end='')


class Programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        print(f"{self.name} is coding in {self.language}.")


class ProgrammingLanguage(Employee):
    def __init__(self, name):
        self.name = name

    def run_code(self):
        super().work()
        print(f"Running code written in {self.name}.")


python = ProgrammingLanguage("Python")
john = Programmer("John", 50000, 'python')

john.work()  # John is coding in Python.
python.run_code()  # Running code written in Python.
'''
OUTPUT

John is coding in python.
😁 Python is working.😁
Running code written in Python.
'''


# Example 2

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        print("Drawing a shape.")


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def draw(self):
        print(
            f"Drawing a {self.color} rectangle with width {self.width} and height {self.height}.")


my_shape = Shape("blue")
my_shape.draw()  # Drawing a shape.

my_rectangle = Rectangle("red", 5, 3)
my_rectangle.draw()  # Drawing a red rectangle with width 5 and height 3.
'''
OUTPUT

Drawing a shape.
Drawing a red rectangle with width 5 and height 3.
'''
