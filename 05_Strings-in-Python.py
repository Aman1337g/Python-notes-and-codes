name = "Aman"
friend = "Aditya Bikram Jena"
anotherFriend = "Roshan Dash"

print("Hello, ", name)
print("Hello,", name)
print("Hello,"+friend)
print("Hello, " + anotherFriend)

# multi-line string
apple = '''He said,
hi aman , how was your day.
I said, it went awesome.
'''
print(apple)

# string index starts from 0
print(anotherFriend[0])
print(anotherFriend[1])
print(anotherFriend[2])
print(anotherFriend[3])
print(anotherFriend[4])
print(anotherFriend[5])
# print(anotherFriend[55]) # IndexError

print("Let's use for Loop to traverse \"friend : ")
for character in friend:
    print(character)

'''
OUTPUT

Hello,  Aman
Hello, Aman
Hello,Aditya Bikram Jena
Hello, Roshan Dash
He said,
hi aman , how was your day.
I said, it went awesome.

R
o
s
h
a
n
Let's use for Loop to traverse "friend :
A
d
i
t
y
a

B
i
k
r
a
m

J
e
n
a
'''
