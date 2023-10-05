#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_args = len(sys.argv) - 1
    print(
        "{} {}:".format(total_args,
                        "argument" if total_args == 1 else "arguments"),
        end="",
    )

    if total_args == 0:
        print(".")
    else:
        print()
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
