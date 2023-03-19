dic = {
    "aman": "human being",
    23: "aditya bikram jena",
    True: "shobhan parida",
    False: "roshan dash",
    '1': "shubham kumar chaudhary"
}
print(dic)
print(dic[True])  # it throws error if key doesn't exist
print(dic.get(True))  # it prints "none" if key doesn't exist

# to print all keys
print()
print(dic.keys())
print(dic.values())
print()
for key in dic.keys():
    print(dic[key])
print()
i = 0
for value in dic.values():
    print(f"value {i+1} :", value)
    i += 1
print()
for key in dic.keys():
    print(f"dic[{key}] :", dic[key])
'''
OUTPUT

{'aman': 'human being', 23: 'aditya bikram jena', True: 'shobhan parida', False: 'roshan dash', '1': 'shubham kumar chaudhary'}
shobhan parida
shobhan parida

dict_keys(['aman', 23, True, False, '1'])
dict_values(['human being', 'aditya bikram jena', 'shobhan parida', 'roshan dash', 'shubham kumar chaudhary'])

human being
aditya bikram jena
shobhan parida
roshan dash
shubham kumar chaudhary

value 1 : human being
value 2 : aditya bikram jena
value 3 : shobhan parida
value 4 : roshan dash
value 5 : shubham kumar chaudhary

dic[aman] : human being
dic[23] : aditya bikram jena
dic[True] : shobhan parida
dic[False] : roshan dash
dic[1] : shubham kumar chaudhary
'''

print(dic.items())
for key, value in dic.items():
    print(f"The value corresponding to {key} is {value}")
'''
OUTPUT

dict_items([('aman', 'human being'), (23, 'aditya bikram jena'), (True, 'shobhan parida'), (False, 'roshan dash'), ('1', 'shubham kumar chaudhary')])
The value corresponding to aman is human being
The value corresponding to 23 is aditya bikram jena
The value corresponding to True is shobhan parida
The value corresponding to False is roshan dash
The value corresponding to 1 is shubham kumar chaudhary
'''
