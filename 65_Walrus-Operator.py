# walrus operator :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression


happy = True
print(happy)
print(happy := True)
'''
OUTPUT

True
True
'''

# without using walrus operator
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
print(foods)
'''
OUTPUT

What food do you like?: ginger
What food do you like?: mango
What food do you like?: aam
What food do you like?: santra
What food do you like?: orange
What food do you like?: kela
What food do you like?: quit
['ginger', 'mango', 'aam', 'santra', 'orange', 'kela']
'''

# using walrus operator
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
print(foods)
'''
OUTPUT

What food do you like?: kela
What food do you like?: banana
What food do you like?: aloo
What food do you like?: gobi
What food do you like?: pineapple
What food do you like?: quit
['kela', 'banana', 'aloo', 'gobi', 'pineapple']
'''