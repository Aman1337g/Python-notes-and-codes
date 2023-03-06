# # break = loop chodkar nikal jao (SKIPPING THE LOOP)
# # continue = iteration chodkar nikal jao (SKIPPING THE ITERATION)

# # printing multiplication table of 5 till 5*10

# for i in range(50):
#     if (i == 10):
#         break
#     print("5 x", i+1, "=", 5*(i+1))
# print("Skipped the loop!!")

# '''
# OUTPUT

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
# Skipped the loop!!
# '''

# # while equivalent of above program

# i = 1
# while (i <= 50):
#     if (i == 11):
#         break
#     print("5 x", i, "=", 5*i)
#     i = i + 1

# '''
# OUTPUT

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
# '''

# continue statement

i = 1
while (i <= 14):
    if (i == 11):
        i = i + 1
        continue
    else:
        print("5 x", i, "=", 5*i)
        i = i + 1
print("Skipped the iteration!!")

# equivalent for loop

for i in range(14):
    if (i == 10):
        continue
    print("5 x", i+1, "=", 5*(i+1))

'''
OUTPUT

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
5 x 12 = 60
5 x 13 = 65
5 x 14 = 70
Skipped the iteration!!
'''

# EMULATING do-while loop
# PRINTING "Hello sir !!" 8 times

i = 1
while True:
    print("Hello sir !!")
    i = i + 1
    if (i == 9):
        break

'''
OUTPUT

Hello sir !!
Hello sir !!
Hello sir !!
Hello sir !!
Hello sir !!
Hello sir !!
Hello sir !!
Hello sir !!
'''
