#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def switch(case, a, b):
    if case == "+":
        print("{} {} {} = {}".format(a, case, b, add(a, b)))
        return 0
    elif case == "-":
        print("{} {} {} = {}".format(a, case, b, sub(a, b)))
        return 0
    elif case == "*":
        print("{} {} {} = {}".format(a, case, b, mul(a, b)))
        return 0
    elif case == "/":
        if b == 0:
            print("Impossible operation!!!")
            return 1
        else:
            print("{} {} {} = {}".format(a, case, b, div(a, b)))
            return 0
    else:
        return "Default case executed"


def main():
    argv = sys.argv
    argc = len(argv)
    operator = ""
    if (argc - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    else:
        operator = argv[2]
        if operator not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            return 1
        else:
            a = int(argv[1])
            b = int(argv[3])
            switch(operator, a, b)


if __name__ == "__main__":
    main()  
