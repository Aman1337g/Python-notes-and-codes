l = [23, 33, 2, 1, 32, 1]
print(l)
l.append(344)
print(l)
l.sort()
print(l)
l.append(-32)
print("List after adding -32 :", l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
# l.index() - returns the index of first occurence of the list item.
print(l.index(1))

'''
OUTPUT

[23, 33, 2, 1, 32, 1]
[23, 33, 2, 1, 32, 1, 344]
[1, 1, 2, 23, 32, 33, 344]
List after adding -32 : [1, 1, 2, 23, 32, 33, 344, -32]
[344, 33, 32, 23, 2, 1, 1, -32]
[-32, 1, 1, 2, 23, 32, 33, 344]
1
'''

l = [1, 1, 2, 23, 32, 33, 344, -32, 1, 1]

# l.count(i) - returns the count of the number of items with the given value.
print(l.count(1))

'''
OUTPUT

4
'''


# m = l  # m acts as a reference to l
m = l.copy()
m[0] = 0
print(m)
print(l)
'''
OUTPUT

[0, 1, 2, 23, 32, 33, 344, -32, 1, 1]
[1, 1, 2, 23, 32, 33, 344, -32, 1, 1]
'''
# l.index() - inserting an item in a given index

l = [2, 22, 3, 1, 0, 233]
print(l)
l.insert(4, 2322)
print(l)
'''
OUTPUT

[2, 22, 3, 1, 0, 233]
[2, 22, 3, 1, 2322, 0, 233]
'''

# l.extend(l1) - exteding l1 and adding l's elements to l1
print(l)
l1 = [0, 1, -22]
l.extend(l1)
print(l)
print(l1)
'''
OUTPUT

[2, 22, 3, 1, 2322, 0, 233]
[2, 22, 3, 1, 2322, 0, 233, 0, 1, -22]
[0, 1, -22]
'''

# CONCATENATION

l1 = [1, 2, 3]
l2 = [-1, -2, "aman"]
l3 = l1 + l2
print(l3)
'''
OUTPUT

[1, 2, 3, -1, -2, 'aman']
'''
