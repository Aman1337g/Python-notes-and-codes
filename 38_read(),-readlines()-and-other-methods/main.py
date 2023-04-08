with open('myfile.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
'''
OUTPUT

My name is aman 

Hello bro awesome !!

Hello Duniya
'''
