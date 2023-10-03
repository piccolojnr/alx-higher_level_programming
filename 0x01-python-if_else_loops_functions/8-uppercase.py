def uppercase(str):
    res = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            res += chr(ord(c) - 32)
        else:
            res += c
    return res
