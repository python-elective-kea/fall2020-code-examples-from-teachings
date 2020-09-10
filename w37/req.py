import requests

req = requests.get('https://kea.dk/images/resources/logo-main-black-single.png', allow_redirects=True)

print(req)


#with open('img.png', 'bw') as f:
#    f.write(req.content)

