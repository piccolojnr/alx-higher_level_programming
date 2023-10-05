#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_args = len(sys.argv) - 1
    if total_args == 0:
        print("{} arguments.".format(total_args))
    elif total_args == 1:
        print("{} argument:".format(total_args))

    if total_args == 0:
        print(".")
    else:
        print()
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
