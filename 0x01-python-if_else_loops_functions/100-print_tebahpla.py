#!/usr/bin/python3
for i in range(0, 26, 2):
    print("{}{}".format(chr(ord("z") - i), chr(ord("Z") - i - 1)), end="")
