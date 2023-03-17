# # update and union

# s1 = {1, 1, 2, 3, 2, 66, 23, 9}
# s2 = {1, 5.23, "aman", True, False, 3.334, '34.23232', 5.23}
# # Why True not showing search about it 😄
# print("s1 union s2 : ", s1.union(s2))
# print("s2 union s1 : ", s2.union(s1))
# print("s1 with union method : ", s1)
# print(s2)
# s1.update(s2)
# print("s1 with update method : ", s1)
# '''
# OUTPUT

# s1 union s2 :  {False, 1, 2, 3, 66, 3.334, 'aman', 5.23, 9, 23, '34.23232'}
# s2 union s1 :  {False, 1, 2, 3.334, 'aman', 5.23, 3, 66, 9, 23, '34.23232'}
# s1 with union method :  {1, 2, 3, 66, 23, 9}
# {False, 1, 3.334, 'aman', 5.23, '34.23232'}
# s1 with update method :  {False, 1, 2, 3, 66, 3.334, 'aman', 5.23, 9, 23, '34.23232'}
# '''


# # intersection and intersection_update

# s1 = {1, 1, 2, 3, 2, 66, 23, 9}
# s2 = {1, 5.23, "aman", True, False, 3.334, '34.23232', 5.23}
# s1 = s1.intersection(s2)
# print(s1)
# s1.intersection_update(s2)
# print(s1)
# '''
# OUTPUT

# {1}
# {1}
# '''


# # symmetric_difference [ a union b - a intersection b]

# s1 = {'aman', "aman", 1, 2, 4, 4, 6.34, 232.23232}
# s2 = {'aman', 1.323, 2, 4, 4.456, 6.34, "lucifer"}
# print(s1.symmetric_difference(s2))
# print(s1.symmetric_difference(s1))
# '''
# OUTPUT

# {1.323, 1, 4.456, 232.23232, 'lucifer'}
# set()
# '''


# # difference [ a - b ] AND difference_update
# s1 = {'aman', "aman", 1, 2, 4, 4, 6.34, 232.23232}
# s2 = {'aman', 1.323, 2, 4, 4.456, 6.34, "lucifer"}
# print(s1.difference(s2))
# print("s1 : ", s1)
# s1.difference_update(s2)
# print("s1 : ", s1)
# '''
# OUTPUT

# {232.23232, 1}
# s1 :  {'aman', 1, 2, 4, 6.34, 232.23232}
# s1 :  {1, 232.23232}
# '''


# # isdisjoint - returns True if intersection is zero otherwise returns False
# # issuperset , issubset

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = {"Tokyo", "Madrid", "Berlin", "Delhi", "Tokyo",
#            "Seoul", "Kabul", "Madrid", "Kanpur", "Reema"}
# print(cities.isdisjoint(cities2))
# print("cities superset of cities2 : ", cities.issuperset(cities2))
# print("cities3 superset of cities2 : ", cities3.issuperset(cities2))
# print(cities.issubset(cities3))
# '''
# OUTPUT

# False
# cities superset of cities2 :  False
# cities3 superset of cities2 :  True
# True
# '''


# # add, remove/discard - if item not present then remove raises error while discard does not raises error

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = {"Tokyo", "Madrid", "Berlin", "Delhi", "Tokyo",
#            "Seoul", "Kabul", "Madrid", "Kanpur", "Reema"}
# cities.add("Hellskitchen")
# print(cities)
# cities.remove("Tokyo")
# print(cities)
# cities.discard("Berlin")
# print(cities)
# # cities.remove('aman') # error raised
# # cities.discard('aman') # no error
# '''
# OUTPUT
# ', 'Madrid', 'Berlin', 'Tokyo'}
# {'Hellskitchen', 'Delhi', 'Madrid', 'Berlin'}
# {'Hellskitchen', 'Delhi', 'Madrid'}
# '''


# # pop - random element which comes at last is popped out

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# item = cities2.pop()
# print("Item popped from cities2 is : ", item, "and cities2 : ", cities2)


# # del - to delete an entire set

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# # print(cities)
# '''
# OUTPUT

# NameError: name 'cities' is not defined. Did you mean: 'cities2'?
# '''


# clear - to delete elements only

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
'''
OUTPUT

set()
'''


# checking if item exits in set

s = {'amna', 1, 3, 3, 232, 2322.23}
if 2322.23 in s:
    print("2322.23 is present in set s")
else:
    print("2322.23 is not present in set s")
'''
OUTPUT

2322.23 is present in set s
'''
