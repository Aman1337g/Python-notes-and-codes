str = str(input("Enter the string \"aman\" : "))
if (str != "aman"):
    raise ValueError("Entered string is not 'aman'")
else:
    print("Input excepted !!")
'''
OUTPUT

Enter the string "aman" : 1
Traceback (most recent call last):
  File "c:\Users\ankit\OneDrive\Desktop\GitHub\Python-notes-and-codes\30_Raising-custom-errors-in-Python.py", line 3, in <module>
    raise ValueError("Entered string is not 'aman'")
ValueError: Entered string is not 'aman'
'''
