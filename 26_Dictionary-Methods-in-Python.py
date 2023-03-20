dic1 = {
    "aman": "spiderman",
    "shobhan": "babu rao",
    "aditya bikram jena": "sallu bhai",
    "roshan dash": "ranchor das chanchar"
}
dic2 = {
    "rohan": "king pin",
    "Aman Kumar Gupta": "Daredevil",
    "jyotideep acharjee": "Dr. Strange"
}
dic3 = {
    "Sahil Sajad Reshi": "Steve Rogers"
}
print("dictionary 1 :", dic1)
dic1.update(dic3)  # updating dic1 with dic3 data
print("Adding dic3 to dic1 :", dic1)

dic1.update({"aman": "peter parker"})  # updating "aman" with new value
print("Updated dic1 :", dic1)

print("dictionary 3 :", dic3)
dic3.clear()  # clearing dic3
print("After clearing dic3 :", dic3)

dic2.pop("rohan")  # popping out "rohan" entry in dic2
print("After removing \"rohan\" :", dic2)

print("Dictionary 1 :", dic1)
dic1.popitem()  # deleting last data from dic1
print("Dictionary 1 after removing it's last data :", dic1)

# del dic1 ## dic1 is deleted
# print("Dictionary 1 :", dic1) ## throws error  -  NameError: name 'dic1' is not defined. Did you mean: 'dic2'?

# removes key-value for key = "jyotideep acharjee"
del dic2["jyotideep acharjee"]
print("Dictionary 2 :", dic2)
'''
OUTPUT

dictionary 1 : {'aman': 'spiderman', 'shobhan': 'babu rao', 'aditya bikram jena': 'sallu bhai', 'roshan dash': 'ranchor das chanchar'}
Adding dic3 to dic1 : {'aman': 'spiderman', 'shobhan': 'babu rao', 'aditya bikram jena': 'sallu bhai', 'roshan dash': 'ranchor das chanchar', 'Sahil Sajad Reshi': 'Steve Rogers'}      
Updated dic1 : {'aman': 'peter parker', 'shobhan': 'babu rao', 'aditya bikram jena': 'sallu bhai', 'roshan dash': 'ranchor das chanchar', 'Sahil Sajad Reshi': 'Steve Rogers'}
dictionary 3 : {'Sahil Sajad Reshi': 'Steve Rogers'}
After clearing dic3 : {}
After removing "rohan" : {'Aman Kumar Gupta': 'Daredevil', 'jyotideep acharjee': 'Dr. Strange'}
Dictionary 1 : {'aman': 'peter parker', 'shobhan': 'babu rao', 'aditya bikram jena': 'sallu bhai', 'roshan dash': 'ranchor das chanchar', 'Sahil Sajad Reshi': 'Steve Rogers'}
Dictionary 1 after removing it's last data : {'aman': 'peter parker', 'shobhan': 'babu rao', 'aditya bikram jena': 'sallu bhai', 'roshan dash': 'ranchor das chanchar'}
Dictionary 2 : {'Aman Kumar Gupta': 'Daredevil'}
'''
