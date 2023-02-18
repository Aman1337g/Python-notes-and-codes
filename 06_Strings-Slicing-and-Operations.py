# string[start:stop:step]

fruit = "Jack Fruit"
print("Length of fruit string is : ", len(fruit))


print(fruit[0:5])  # including 0 but not 5
print(fruit[1:5])  # including 1 but not 5
print(fruit[1:])  # same as fruit[1:len(fruit)]
print(fruit[1:len(fruit)])

# -1 = len(fruit)-1 = 10-1 = 9 and -10 = 10-10 = 0 so => fruit[9:0] but output is blank until we provide a negative step
print(fruit[-1:-10:])
print(fruit[-1:-10:-1])
print(fruit[-1:-10:-2])

'''
OUTPUT

Length of fruit string is :  10
Jack
ack
ack Fruit
ack Fruit

tiurF kca
tuFka
'''
