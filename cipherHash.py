import hashlib

def hash(str):
    return hashlib.sha224(str).hexdigest()

def cipher(str, key):
    charSet = "LMEry3CbeUAzt08nOxHhpc1ufsTSR ia92jVGPIvNoJKZQdm6WlXFYgqkD7B54w"
    ret = ""
    for s in str:
        ret += charSet[(charSet.index(s) + charSet.index(key))%len(charSet)]
    return ret


def unCipher(str, key):
    charSet = "LMEry3CbeUAzt08nOxHhpc1ufsTSR ia92jVGPIvNoJKZQdm6WlXFYgqkD7B54w"
    uCharSet = charSet[::-1]
    ret = ""
    for s in str:
        ret += uCharSet[(uCharSet.index(s) + charSet.index(key))%len(uCharSet)]
    return ret

def genPassPhrase(length, key):
    nkey = hash(key)
    while length > len(nkey):
        nkey += hash(nkey)
    return nkey

def cipherHash(msg, passPhrase):
    passPhrase = genPassPhrase(len(msg), passPhrase)
    ret = ""
    index = 0
    for m in msg:
        ret += cipher(m,passPhrase[index])
        index += 1
    return ret

def unCipherHash(msg, passPhrase):
    passPhrase = genPassPhrase(len(msg), passPhrase)
    ret = ""
    index = 0
    for m in msg:
        ret += unCipher(m,passPhrase[index])
        index += 1
    return ret
