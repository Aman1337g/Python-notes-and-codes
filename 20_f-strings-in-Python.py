letter = "I am {} and i am from {}"
country = "India"
name = 'Aman Kumar Gupta'

print(letter.format(name, country))
print(letter.format(country, name))
'''
OUTPUT

I am Aman Kumar Gupta and i am from India
I am India and i am from Aman Kumar Gupta
'''

letter = "I am {1} and i am from {0}"
print(letter.format(country, name))
'''
OUTPUT

I am Aman Kumar Gupta and i am from India
'''

sen = 'Price of this watch is : {price:.2f}'
print(sen.format(price=2000.3443))
'''
OUTPUT

Price of this watch is : 2000.34
'''

# f-string (python 3.6 onwards)


country1 = "India"
name1 = 'Aman Kumar Gupta'
letter = f"I am {name1} and i am from {country1}"
print(letter)
print(f"I am from {country1} and my name is {name1}")
'''
OUTPUT

I am Aman Kumar Gupta and i am from India
I am from India and my name is Aman Kumar Gupta
'''

price = 2000.3443
sen = F'Price of this watch is : {price:.2f}'
print(sen)
print(f'{5*4}')
print(type(f'{5*4}'))
'''
OUTPUT

Price of this watch is : 2000.34
20
<class 'str'>
'''
