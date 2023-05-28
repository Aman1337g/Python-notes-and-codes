import time 

def usingWhile():
    i = 0
    while(i<500):
        print(i)
        i+=1
def usingFor():
    for i in range(500):
        print(i)

init = time.time()
usingWhile()
t1 = time.time()- init

init = time.time()
usingFor()
t2 = time.time()- init

print('Time of while loop :',t1)
print('Time of for loop :',t2)

time.sleep(10)
print('This is printed after 10 seconds.')

t = time.localtime()
date_time = time.strftime('%d-%m-%Y %I:%M:%S %p', t)
print(date_time)
print(t)
'''
OUTPUT

0
TO
499
0
TO
499
Time of while loop : 0.5053808689117432
Time of for loop : 0.36606740951538086
This is printed after 10 seconds.
28-05-2023 11:44:47 AM
'''