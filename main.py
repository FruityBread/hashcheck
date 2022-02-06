import sys
import hashlib

BUF_SIZE = 65536 

def hashselect():
    print("(1) SHA256 \n(2) SHA512 \n(3) MD5")
    choice=input("")
    if choice =="1":
        type = ("SHA256")
        hash = hashlib.sha256()
        openfile(hash)
        output(type, hash)
    elif choice =="2":
        type = ("SHA512")
        hash = hashlib.sha512()
        openfile(hash)
        output(type, hash)
    elif choice=="3":
        type = ("MD5")
        hash = hashlib.md5()
        openfile(hash)
        output(type, hash)
    else:
        print("Please enter a valid option.")
        hashselect()


def openfile(hash):
    with open((sys.argv[1]), 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            hash.update(data)

def output(type, hash):   
    print(type+": {0}".format(hash.hexdigest()))

hashselect()