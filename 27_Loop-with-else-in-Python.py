for i in range(5):
    print(i)

else:  # else is a part of the loop
    print("Sorry bro !!")
'''
OUTPUT

0
1
2
3
4
Sorry bro !!
'''

for i in range(5):
    print(i)
    if (i == 3):
        break

else:
    print("Sorry bro !!")
'''
OUTPUT

0
1
2
3
'''

i = 7
while (i < 14):
    print(i)
    i += 1
else:
    print("Chill kar Bro ❄️")
'''
OUTPUT

7
8
9
10
11
12
13
Chill kar Bro ❄️
'''
