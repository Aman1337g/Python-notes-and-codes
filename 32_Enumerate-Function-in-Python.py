index = 0
l = ['aman', 'harshit', 'aditya bikram jena',
     'pratyush kurhe', 'vikas ranjan', 't. shubham']
for i in l:
    print(i)
    if (index == 4):
        print(f"At index {index} and value is {i}")
    index += 1
'''
OUTPUT

aman
harshit
aditya bikram jena
pratyush kurhe
vikas ranjan
At index 4 and value is vikas ranjan
t. shubham
'''


for index, names in enumerate(l):
    print(f"{index} : {names}")
'''
OUTPUT

0 : aman
1 : harshit
2 : aditya bikram jena
3 : pratyush kurhe
4 : vikas ranjan
5 : t. shubham
'''


S = "aman kumar gupta !!"
print(S)
print(S.upper())
for i, str in enumerate(S, start=1):
    print(i, ":", str)
    if (i == 4):
        print("At index 4 value :", str)
'''
OUTPUT

aman kumar gupta !!
AMAN KUMAR GUPTA !!
1 : a
2 : m
3 : a
4 : n
At index 4 value : n
5 :
6 : k
7 : u
8 : m
9 : a
10 : r
11 :
12 : g
13 : u
14 : p
15 : t
16 : a
17 :
18 : !
19 : !
'''


l = ['banana', 'guava', 'strawberry', 'papaya']
for t in enumerate(l):
    print(t)
'''
OUTPUT

(0, 'banana')
(1, 'guava')
(2, 'strawberry')
(3, 'papaya')
'''
