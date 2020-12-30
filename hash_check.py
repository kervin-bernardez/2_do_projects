import hashlib


def hasher(texts):
    hash_algo = ["md5", "sha1", "sha256"]
    hash_list = []
    for algo in hash_algo:
        if algo == "md5":
            hash = hashlib.md5(texts)
        elif algo == "sha1":
            hash = hashlib.sha1(texts)
        else:
            hash = hashlib.sha256(texts)
        hash_list.append(hash.hexdigest())
    return hash_list


def text_hasher(texts):
    encoded = texts.encode()
    x = hasher(encoded)
    return x


def file_hasher(file_in):
    with open(file_in, "rb") as filename:
        encoded = filename.read()
        x = hasher(encoded)
        return x


def print_hash(hash_list):
    print("MD5 Hash: {}".format(hash_list[0]))
    print("SHA1 Hash: {}".format(hash_list[1]))
    print("SHA256 Hash: {}".format(hash_list[2]))
