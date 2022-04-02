import hashlib
from tkinter.filedialog import askopenfilename


def hash_choice(choice):
    try:
        my_hash = {"1": hashlib.sha256, "2": hashlib.sha512, "3": hashlib.md5}[choice]()
    except KeyError:
        return hash_choice(input("Please enter a valid option."))
    return my_hash


def file_choice(my_hash):
    file = askopenfilename()
    if file:
        with open(file, 'rb') as f:
            while True:
                data = f.read(65536)
                if not data:
                    my_obj = HashObject(my_hash, None)
                    print(my_obj.my_hash.hexdigest())
                    return my_obj

                my_hash.update(data)

    else:
        exit()


class HashObject:
    def __init__(self, my_hash, user_hash):
        self.my_hash = my_hash
        self.user_hash = user_hash


def compare(my_obj, user_hash):
    return my_obj.my_hash.hexdigest() == user_hash

