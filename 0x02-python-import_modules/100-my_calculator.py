#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        ops = {"+": add, "-": sub, "*": mul, "/": div}

        if operator not in list(ops.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            print("{} {} {} = {}".format(a, operator, b, ops[operator](a, b)))
