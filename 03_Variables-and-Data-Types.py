a = 23842984
print(a)
b = "Aman Kumar Gupta"
print(b)
# print(a+b) ## error
c = "23842984"
print(b + c)  # no error

d = True
print(d)
e = None
print(e)
print("The type of e is : ", type(e))
print("The type of a is : ", type(a))
print("The type of b is : ", type(b))
print("The type of c is : ", type(c))
print("The type of d is : ", type(d))

f = complex(23.2, 43)
print(f)
print("The type of f is : ", type(f))

g = 23.324
print(g)
print("The type of g is : ", g)

list = [23, 32.23, "Aman", [1, 'aman'], True, False,
        "banana"]  # collection of different data items
print("List : ", list)
print("The type of list is : ", list)
a = [23, 32.23, "Aman", [1, 'aman'], True, False, "banana"]
print("Print a : ", a)

tuple1 = ("lion", 'tiger', ("parrot", "sparrow", "rhino"))  # immutable
print(tuple1)

dict1 = {"name : ": "Aman Kumar Gupta", "Age": 19,
         "College": "IIIT BBSR", "canVote": True, "CGPA": 10.0}
print(dict1)
# Everything in python everything is an OBJECT
