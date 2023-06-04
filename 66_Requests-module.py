# GET request

import requests

url = 'https://httpbin.org/post'
r = requests.get(url)
print(r.text)
'''
OUTPUT

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
'''

# POST request

import requests
in_values = {'username':'Jack','password':'Hello','address':'221B Baker Street'}
res = requests.post('https://httpbin.org/post',data = in_values)
print(res.text)
'''
OUTPUT

{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "address": "221B Baker Street",
    "password": "Hello",
    "username": "Jack"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "54",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.31.0",
    "X-Amzn-Trace-Id": "Root=1-647cc1c1-34d8cb8518c78a5d03fe1f5e"
  },
  "json": null,
  "origin": "122.50.227.45",
  "url": "https://httpbin.org/post"
}
'''

# bs4 module

import requests
from bs4 import BeautifulSoup

url = 'https://aman1337g.netlify.app/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
with open('beautify.txt','w',encoding='utf-8') as file:
  file.write(soup.prettify())
print('Content saved to ''beautify.txt'' file.')
for heading in soup.find_all("h2"):
  print(heading.text)

'''
OUTPUT

Content saved to beautify.txt file.
Intro
Work
Skills
Contact
Elements
Heading Level 2
'''