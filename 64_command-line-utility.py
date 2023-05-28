import argparse
import requests

import requests

def DownloadFile(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 

parser = argparse.ArgumentParser()

# Adding command line arguments
parser.add_argument('url', help='url of the the file to download')
# parser.add_argument('output', help='by which name you want to save your file')
parser.add_argument('-o','--output', help='name of the file', default=None)

# Parse the arguments 
args = parser.parse_args()

# Using arguments
print(args.url)
print(args.output, type(args.output))
DownloadFile(args.url, args.output)

'''
INPUT without fileName

python .\64_command-line-utility.py https://imagej.net/images/clown.jpg      
https://imagej.net/images/clown.jpg
None <class 'NoneType'>
'''

'''
INPUT with fileName

python .\64_command-line-utility.py https://imagej.net/images/clown.jpg -o c.jpg
https://imagej.net/images/clown.jpg
c.jpg <class 'str'>
'''