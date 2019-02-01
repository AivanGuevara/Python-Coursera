import json
import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
totalSum = 0

while True:
    address = input('Enter location: ')
    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    info = json.loads(data)
    print('User count:', len(info))

    commentsList = info['comments']
    for item in commentsList:
        totalSum = totalSum + int(item['count'])
    print(totalSum)