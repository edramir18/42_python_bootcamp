from functools import reduce


class Vector:
    def __init__(self, value):
        self.validate(value)
        if type(value) == list:
            self.values = [float(x) for x in value]
        elif type(value) == tuple:
            self.values = [float(x) for x in range(value[0], value[1])]
        else:
            self.values = [float(x) for x in range(0, value)]
        self.size = len(self.values)

    def __str__(self):
        return reduce(lambda x, y: f'{x} {y}', [str(k) for k in self.values])

    def __repr__(self):
        value = reduce(lambda x, y: f'{x}, {y}', [str(k) for k in self.values])
        return f'({value})'

    def __add__(self, other):
        if type(other) in [int, float]:
            return Vector([x + other for x in self.values])
        elif type(other) == Vector and self.size == other.size:
            return Vector([x + y for x, y in zip(self.values, other.values)])
        elif type(other) == Vector and self.size != other.size:
            raise ArithmeticError('The size of both vectors has to be equal')
        else:
            raise ArithmeticError(f'The operation is not supported with '
                                  f'{type(other)}')

    def __radd__(self, other):
        self.__add__(other)

    def __sub__(self, other):
        if type(other) in [int, float]:
            return Vector([x - other for x in self.values])
        elif type(other) == Vector and self.size == other.size:
            return Vector([x - y for x, y in zip(self.values, other.values)])
        elif type(other) == Vector and self.size != other.size:
            raise ArithmeticError('The size of both vectors has to be equal')
        else:
            raise ArithmeticError(f'The operation is not supported with '
                                  f'{type(other)}')

    def __rsub__(self, other):
        self.__sub__(other)

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Vector([x * other for x in self.values])
        elif type(other) == Vector and self.size == other.size:
            return reduce(lambda r, v: r + v[0] * v[1],
                          zip(self.values, other.values), 0)
        elif type(other) == Vector and self.size != other.size:
            raise ArithmeticError('The size of both vectors has to be equal')
        else:
            raise ArithmeticError(f'The operation is not supported with '
                                  f'{type(other)}')

    def __rmul__(self, other):
        self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in [int, float] and other == 0:
            raise ZeroDivisionError
        elif type(other) in [int, float]:
            return Vector([x / other for x in self.values])
        else:
            raise ArithmeticError(f'The operation is not supported with '
                                  f'{type(other)}')

    def __rtruediv__(self, other):
        self.__truediv__(other)

    @staticmethod
    def validate(value):
        if type(value) == list and len(value) == 0:
            raise ValueError("List can't be empty")
        elif type(value) == tuple and (len(value) != 2 or value[0] > value[1]):
            raise ValueError('The tuple has to have 2 elements')
        elif type(value) == int and value <= 0:
            raise ValueError('The number has to be positive')
        elif type(value) not in [list, tuple, int]:
            raise TypeError('The argument supplied is not valid')
