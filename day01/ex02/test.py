#! /usr/bin/env python3

from vector import Vector


def test_init(value):
    print(f'\nTesting: {value}:{type(value)}')
    try:
        a = Vector(value)
        print(str(a))
    except ValueError as v:
        print(v)
    except TypeError as t:
        print(t)


def test_add(vect, value):
    print(f'\nTesting: {repr(vect)} + {value}:{type(value)}')
    try:
        b = vect + value
        print(f'{type(b)} {repr(b)}')
    except ArithmeticError as a:
        print(a)


def test_radd(vect, value):
    print(f'\nTesting: {value}:{type(value)} + {repr(vect)}')
    try:
        b = value + vect
        print(f'{type(b)} {repr(b)}')
    except ArithmeticError as a:
        print(a)


def test_sub(vect, value):
    print(f'\nTesting: {repr(vect)} - {value}:{type(value)}')
    try:
        b = vect - value
        print(f'{type(b)} {repr(b)}')
    except ArithmeticError as a:
        print(a)


def test_rsub(vect, value):
    print(f'\nTesting: {value}:{type(value)} - {repr(vect)}')
    try:
        b = value - vect
        print(f'{type(b)} {repr(b)}')
    except ArithmeticError as a:
        print(a)


def test_truediv(vect, value):
    print(f'\nTesting: {repr(vect)} - {value}:{type(value)}')
    try:
        b = vect / value
        print(f'{type(b)} {repr(b)}')
    except ArithmeticError as a:
        print(a)


def test_rtruediv(vect, value):
    print(f'\nTesting: {value}:{type(value)} - {repr(vect)}')
    try:
        b = value / vect
        print(f'{type(b)} {repr(b)}')
    except ArithmeticError as a:
        print(a)


def main():
    test_init(2.3)
    test_init('2')
    test_init((2, 3, 4))
    test_init((2, 4))
    test_init(-1)
    test_init(2)
    test_init(1)
    a = Vector(3)
    b = Vector(4)
    test_add(a, 3)
    test_add(a, 4.0)
    test_add(a, '3')
    test_add(a, b)
    test_radd(3, a)
    test_radd(4.0, a)
    test_radd('3', a)
    test_radd(b, a)
    test_sub(a, 3)
    test_sub(a, 4.0)
    test_sub(a, '3')
    test_sub(a, b)
    test_rsub(3, a)
    test_rsub(4.0, a)
    test_rsub('3', a)
    test_rsub(b, a)
    print(a * 2)
    print(a * a)
    print(a / 2)
    c = Vector(1)
    print(repr(c))

if __name__ == '__main__':
    main()
