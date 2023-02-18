a = "!!!Aman Kumar Gupta!!!!!!"
a1 = "!!! Am an Kum ar Gupta!! 1Aman!! !!"
print(a)

print("Length of string 'a' is : ", len(a))
# upper()
print(a.upper())
# lower()
print(a.lower())
# rstrip()
print("a.rstrip(\"!\") : ", a.rstrip("!"))
print('a1.rstrip("!") : ', a1.rstrip("!"))
# replace
print('a.replace("Aman", "Mridul") : ', a.replace("Aman", "Mridul"))
print('a1.replace("Aman", "Mridul") : ', a1.replace("Aman", "Mridul"))
# split()
print(a1.split(" "))

# capitalize()
blogHeading = 'introduction tO JS'
print(blogHeading.capitalize())
# center()
str1 = "Welcome to the Console !!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))
# endswith()
print("No. of exclamation marks : ", a.count("!"))
print(a.endswith("!!"))

print(a[4:10])
print(a.endswith("Ku", 4, 10))
print(a.endswith("n Ku", 4, 10))

# find - return the index of first occurence of provided string and return -1 if not found
str1 = "He's nameis is Aman. He is a honest man."
print(str1.find("is"))
print(str1.find("ishhh"))

# index - to raise exception if specified string is not present
print(str1.index("is"))
# print(str1.index("ishhh")) # raises exception and program ends

# isalnum()
str1 = "Aman01"
print(str1.isalnum())
# isalpha()
str1 = "Aman01"
print(str1.isalpha())
# islower()
str1 = "aman01"
print(str1.islower())
# isprintable
str1 = "aman\n"
print(str1.isprintable())
str1 = "aman"
print(str1.isprintable())
# isspace()
str1 = "Aman Gupta"
print(str1.isspace())
str1 = "AmanGupta"
print(str1.isspace())
str1 = "  "
print(str1.isspace())
# istitle()
str1 = "Aman kumar"
print(str1.istitle())
str1 = "Aman Kumar"
print(str1.istitle())
# startswith()
str1 = "amankumar Gupta"
print(str1.startswith("aman"))
# swapcase()
print(str1.swapcase())
# title()
str1 = "aman Is a honest man."
print(str1.title())

'''
OUTPUT

!!!Aman Kumar Gupta!!!!!!
Length of string 'a' is :  25
!!!AMAN KUMAR GUPTA!!!!!!
!!!aman kumar gupta!!!!!!
a.rstrip("!") :  !!!Aman Kumar Gupta
a1.rstrip("!") :  !!! Am an Kum ar Gupta!! 1Aman!!
a.replace("Aman", "Mridul") :  !!!Mridul Kumar Gupta!!!!!!
a1.replace("Aman", "Mridul") :  !!! Am an Kum ar Gupta!! 1Mridul!! !!
['!!!', 'Am', 'an', 'Kum', 'ar', 'Gupta!!', '1Aman!!', '!!']
Introduction to js
            Welcome to the Console !!
25
50
No. of exclamation marks :  9
True
man Ku
True
True
9
-1
9
True
False
True
False
True
False
False
True
False
True
True
AMANKUMAR gUPTA
Aman Is A Honest Man.
'''
