f = open('marks.txt', 'r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = line.split(',')[0]  # these marks are strings now
    m2 = line.split(',')[1]
    m3 = line.split(',')[2]
    print(f"Marks of student {i} in maths {m1}")
    print(f"Marks of student {i} in chemistry {m2}")
    print(f"Marks of student {i} in physics {m3}")
    print(line)
f.close()
'''
OUTPUT

Marks of student 1 in maths 56
Marks of student 1 in chemistry 32
Marks of student 1 in physics 23

56,32,23

Marks of student 2 in maths 77
Marks of student 2 in chemistry 88
Marks of student 2 in physics 91

77,88,91

Marks of student 3 in maths 10
Marks of student 3 in chemistry 34
Marks of student 3 in physics 43
10,34,43
'''
