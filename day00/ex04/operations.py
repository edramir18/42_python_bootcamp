#! /usr/bin/env python

import sys
import re


def print_usage():
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('    python operations.py 10 3')


def main():
    number = r'^-?[0-9]+$'
    argn = len(sys.argv)
    if argn < 3:
        print_usage()
    elif argn > 3:
        print("InputError: too many arguments")
        print_usage()
    elif re.search(number, sys.argv[1]) is None or re.search(number, sys.argv[2]) is None:
        print("InputError: only numbers")
        print_usage()
    else:
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])
        print(f'Sum:         {number1 + number2}')
        print(f'Difference:  {number1 - number2}')
        print(f'Product:     {number1 * number2}')
        if number2 == 0:
            print(f'Quotient:    ERROR (div by zero)')
            print(f'Remainder:   ERROR (modulo by zero)')
        else:
            print(f'Quotient:    {number1 / number2}')
            print(f'Remainder:   {number1 % number2}')


if __name__ == '__main__':
    main()
