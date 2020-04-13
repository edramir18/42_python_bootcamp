#! /usr/bin/env python

import sys


def main():
    if len(sys.argv) == 1:
        return
    if len(sys.argv) > 2 or not sys.argv[1].isnumeric():
        print("ERROR")
        return
    number = int(sys.argv[1])
    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == '__main__':
    main()