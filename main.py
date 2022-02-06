import sys
import hashlib

BUF_SIZE = 65536 

md5 = hashlib.md5()
sha1 = hashlib.sha256()

with open((sys.argv[1]), 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)

print("MD5: {0}".format(md5.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))