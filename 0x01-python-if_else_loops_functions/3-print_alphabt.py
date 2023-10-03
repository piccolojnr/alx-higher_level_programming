#!/usr/bin/python3
for i in range(26):
    if chr(ord("a") + i) == "e" or chr(ord("a") + i) == "q":
        continue
    print("{}".format(chr(ord("a") + i)), end="")
