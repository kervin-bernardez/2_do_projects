import hashlib


def hasher(texts, *args):
    if len(args) != 0:
        hash_algo = [args[0]]
    else:
        hash_algo = ["md5", "sha1", "sha256", "sha512"]
    hash_list = []
    for algo in hash_algo:
        if algo == "md5":
            hash = hashlib.md5(texts)
        elif algo == "sha1":
            hash = hashlib.sha1(texts)
        elif algo == "sha256":
            hash = hashlib.sha256(texts)
        elif algo == "sha512":
            hash = hashlib.sha512(texts)
        else:
            return False
        hash_list.append(hash.hexdigest())
    return hash_list


def text_hasher(texts, *args):
    encoded = texts.encode()
    hash_list = hasher(encoded, *args)
    return hash_list


def file_hasher(file_in, *args):
    with open(file_in, "rb") as filename:
        encoded = filename.read()
        hash_list = hasher(encoded, *args)
        return hash_list
