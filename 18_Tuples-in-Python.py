tup = (1)
# here type(tup) is int we have to put a comma(,) for type(tup) to show tuple
print(type(tup), tup)

tup = (1, )
print(type(tup), tup)
'''
OUTPUT

<class 'int'> 1
<class 'tuple'> (1,)
'''

tup = (1, 3234, 23, 56, 657, 64, -1, True, "aman")
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-3])
print(tup[4])
print()
for i in tup:
    print(i, end=" ")

# print(tup(108)) # error, index out of range
print()
if 3234 in tup:
    print("3234 in tuple tup!!")

# tup[0] = 4324 # error, tuple is immutable
print(tup)
'''
OUTPUT

1
3234
23
56
-1
657

1 3234 23 56 657 64 -1 True aman
3234 in tuple tup!!
(1, 3234, 23, 56, 657, 64, -1, True, 'aman')
'''

print(tup[1:4])
tup2 = tup[::2]
print(tup2)
'''
OUTPUT

(3234, 23, 56)
(1, 23, 657, -1, 'aman')
'''
