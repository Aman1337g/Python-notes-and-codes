with open('zebra.txt', 'w') as f:
    f.write('I am a beautiful Zebra.I eat lot of grass.')
    f.seek(3)  # NO effect on truncate unlike for reading data
    f.truncate(6)
with open('zebra.txt', 'r') as f:
    data = f.read()
    print(data)
'''
OUTPUT

I am a
'''
