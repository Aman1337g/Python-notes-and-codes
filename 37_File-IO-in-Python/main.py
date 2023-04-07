# READING A FILE
f = open('mytext.txt', 'r')  # r(read) mode is default
print(f)
text = f.read()
print(text)
f.close()
'''
OUTPUT

<_io.TextIOWrapper name='mytext.txt' mode='r' encoding='cp1252'>
Hey Aman awesome man !!
'''

# f = open('mytext 2.txt', 'w') # write mode automatically creates the file if it doesn't exist


# WRITING TO A FILE
f = open('mytext 2.txt', 'w')
n = input('Enter your name : ')
f.write(f"Hello {n}, Welcome to file IO in python tutorial !!")
f.write("aman kumar gupta")
f.write('jhinganlala')
f.close()

# APPENDING
f = open('mytext 2.txt', 'a')
f.write('kurhe')
f.close()
'''
OUTPUT

Enter your name : dinosaur kumar
'''

f = open('mytext 2.txt', 'r')
text = f.read()
print(text)
f.close()
'''
OUTPUT

Hello dinosaur kumar, Welcome to file IO in python tutorial !!aman kumar guptajhinganlalakurhe
'''

with open('mytext 2.txt', 'r') as f:
    text = f.read()
    print(text)
'''
OUTPUT

Hello dinosaur kumar, Welcome to file IO in python tutorial !!aman kumar guptajhinganlalakurhe
'''
