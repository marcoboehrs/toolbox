import pickle

payload = b'''(lp1
Vmarco2
p2
aS'40115a7e43e79edfe65cc3f2233a88c4'
p3
a.'''

print(payload);

c = pickle.loads(payload)
print(c)
