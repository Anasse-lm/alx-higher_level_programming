#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    argc = len(argv)
    if argc == 0:
        print(0)
    else:
        result = 0
        for i in range(1, argc):
            result = result + int(argv[i])
        print(result)


if __name__ == "__main__":
    main()
