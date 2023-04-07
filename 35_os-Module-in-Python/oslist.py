import os

# for displaying all the folders(directories) created in Data folder
folder = os.listdir("Data")

for f in folder:
    print(f)
'''
OUTPUT

Day 1
Day 2
Day 3
Day 4
Day 5
'''

# printing folders in Data/ and their constituent folders side by side

for f in folder:
    print(f, ":", os.listdir(f"Data/{f}"))
'''
OUTPUT

Day 1 : []
Day 2 : ['aman', 'main.py', 'tutorial2.md']
Day 3 : []
Day 4 : ['hello']
Day 5 : []
'''

# DISPLAYING current directory

print(os.getcwd())
'''
OUTPUT

C:\Users\ankit\OneDrive\Desktop\GitHub\Python-notes-and-codes\35_os-Module-in-Python
'''
