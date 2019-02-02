# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count:'))
position = int(input('Enter position:'))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print('Retrieving', url)
actualPosition = 1
actualName = ''

# Retrieve all of the anchor tags
while count > 0:
    tags = soup('a')
    for tag in tags:
        if actualPosition == position:
            actualURL = tag.get('href', None)
            print('Retrieving', actualURL)
            html = urllib.request.urlopen(actualURL, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            count = count - 1
            actualPosition = 1
            actualName = tag.contents[0]
            break
        else:
            actualPosition = actualPosition +1
print(actualName)