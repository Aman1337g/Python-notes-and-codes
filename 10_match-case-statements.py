x = int(input("Input value : "))
match x:
    case 0:
        print("x is zero.")
    case 4:
        print("x is 4.")
    case _ if (x != 30): print(x, "is not 30.")
    case _ if (x != 40): print(x, "is not 40.")
    case _ if (x != 50): print(x, "is not 50.")
    case _: print(x)

'''
OUTPUT

Input value : 40
40 is not 30.
'''
