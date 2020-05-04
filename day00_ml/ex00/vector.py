class Vector:
    def __init__(self, data):
        self.values = []
        if (isinstance(data, list)
                and all(isinstance(v, (int, float)) for v in data)):
            self.values = [float(v) for v in data]
        elif (isinstance(data, tuple) and len(data) == 2
                and all(isinstance(v, int) for v in data)):
            self.values = [float(v) for v in range(*data)]
        elif isinstance(data, int):
            self.values = [float(v) for v in range(4)]
        else:
            raise TypeError
        self.size = len(self.values)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            values = [x + other for x in self.values]
        elif isinstance(other, Vector) and self.size == other.size:
            values = [x + y for x, y in zip(self.values, other.values)]
        else:
            raise ValueError
        return Vector(values)

    def __radd__(self, other):
        return self.__add__(other)
