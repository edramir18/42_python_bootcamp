#! /usr/bin/env python

import sys


def print_usage():
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('    python operations.py 10 3')


def main():
    argn = len(sys.argv)
    if argn < 3:
        print_usage()
    elif argn > 3:
        print("InputError: too many arguments")
        print_usage()
    elif not (sys.argv[1].isnumeric() and sys.argv[2].isnumeric()):
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
