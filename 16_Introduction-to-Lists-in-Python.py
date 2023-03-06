l = [2, 4, True, "Aman Kumar Gupta", -1, 'a']
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])
# print(l[6]) # error (index out of range)
print()
print(l[-1])  # negative index
print("Number of elements in list l :", len(l))
print(l[len(l)-1])  # equivalent positive index
print(l[6-1])
print(l[5])

'''
OUTPUT

[2, 4, True, 'Aman Kumar Gupta', -1, 'a']
<class 'list'>
2
4
True
Aman Kumar Gupta
-1
a

a
Number of elements in list l : 6
a
a
a
'''

if "Aman" in l:
    print("Yes")
else:
    print("No")

'''
OUTPUT

No
'''


if "Aman Kumar Gupta" in l:
    print("Yes")
else:
    print("No")

'''
OUTPUT

Yes
'''
# Same thing applies for string as well

# Printing all the elements in list, l

for i in l:
    print(i, end=" ")
print()
print(l)
print(l[:])

'''
OUTPUT

2 4 True Aman Kumar Gupta -1 a
[2, 4, True, 'Aman Kumar Gupta', -1, 'a']
[2, 4, True, 'Aman Kumar Gupta', -1, 'a']
'''

print(l[1:])
print(l[1:-1])
# =>
print(l[1:len(l)-1])
print(l[::2])
print(l[0:len(l)])
'''
OUTPUT

[4, True, 'Aman Kumar Gupta', -1, 'a']
[4, True, 'Aman Kumar Gupta', -1]
[4, True, 'Aman Kumar Gupta', -1]
[2, True, -1]
'''

# list comprehension

lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(8, 13) if i % 2 == 0]
print(lst)

'''
OUTPUT

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[64, 100, 144]
'''

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4 and "o" in item)]
print(namesWith_O)

'''
OUTPUT

['Bruno']
'''
