tupl = ("India", "Russia", "New Zealand", "Australia", 'America')
print(tupl)
l = list(tupl)
l.append("Zimbawe")
print("Tuple :", tupl)
print("List :", l)
l.pop(3)
print("List :", l)

l[4] = "Indonesia"
print("List :", l)
tupl = tuple(l)
print()
print("Tuple :", tupl)
print("List :", l)
'''
OUTPUT

('India', 'Russia', 'New Zealand', 'Australia', 'America')
Tuple : ('India', 'Russia', 'New Zealand', 'Australia', 'America')
List : ['India', 'Russia', 'New Zealand', 'Australia', 'America', 'Zimbawe']
List : ['India', 'Russia', 'New Zealand', 'America', 'Zimbawe']
List : ['India', 'Russia', 'New Zealand', 'America', 'Indonesia']

Tuple : ('India', 'Russia', 'New Zealand', 'America', 'Indonesia')
List : ['India', 'Russia', 'New Zealand', 'America', 'Indonesia']
'''

# Concatenation

Tuple = ('India', 'Russia', 'New Zealand', 'America', 'Indonesia')
tuple1 = (1, 3, 23, "'13'", True, '\'23\'')
tuple2 = Tuple + tuple1
print(tuple2)
'''
OUTPUT

('India', 'Russia', 'New Zealand', 'America', 'Indonesia', 1, 3, 23, "'13'", True, "'23'")
'''

# count() - returns the no. of occurences

tuple1 = (32, 23, " india", 'india', 'russia', 'russia', 'america', 'russia')
print(tuple1.count(32))
print(tuple1.count("india"))
print(tuple1.count("russia"))
print(tuple1.count("america"))
print(tuple1.count("am"))
'''
OUTPUT

1
1
3
1
0
'''

# index(ELEMENT, START, END) - returns the index of first occurence of element
print()
tuple1 = (32, 23, " india", 'india', 'russia', 'russia', 'america', 'russia')
print("Length of tuple1 :", len(tuple1))
print(tuple1.index(32))
print(tuple1.index(23))
print(tuple1.index(' india'))
# print(tuple1.index(' russia')) # error as ' russia' not in tuple (VALUE ERROR)
print(tuple1.index('russia'))
print(tuple1.index('russia', 5, 6))
print(tuple1.index('russia', 5, 7))
print(tuple1.index('russia', 5, 8))
print(tuple1.index('russia', 6, 9))
print(tuple1.index('russia', 3, 16))
'''
OUTPUT

Length of tuple1 : 8
0
1
2
4
5
5
5
7
4
'''
