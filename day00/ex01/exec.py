#! /usr/bin/env python

import sys


def main():
    argv = len(sys.argv)
    if argv == 1:
        return
    last_n = len(sys.argv) - 1
    for i in range(last_n, 0, -1):
        if i < last_n:
            print(" ", end="")
        for k in reversed(list(sys.argv[i])):
            if k.isupper():
                print(k.lower(), end="")
            else:
                print(k.upper(), end="")
    print("")


if __name__ == "__main__":
    main()
