from vector import Vector


class BC:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKMSG = f'{OKGREEN}[ OK]{ENDC}'
    NOKMSG = f'{FAIL}[NOK]{ENDC}'
    WARNINGMSG = f'{WARNING}[WNG]{ENDC}'

    @staticmethod
    def bold(msg: str):
        return f'{BC.BOLD}{msg}{BC.ENDC}'


def function_name(func):
    def wrapper(*args, **kwargs):
        print(f'{BC.OKBLUE}[{func.__name__:30}]{BC.ENDC}', end='')
        func(*args, **kwargs)
    return wrapper


@function_name
def test_wrong_type_on_create():
    values = "Hello World"
    try:
        Vector(values)
    except TypeError:
        print(f'{BC.OKMSG} Detect wrong type on create')
    else:
        print(f'{BC.NOKMSG} Not raise error on type')


@function_name
def test_create_from_list():
    try:
        list_values = [1, 2, 3]
        expected = [float(v) for v in list_values]
        a = Vector([1, 2, 3])
        size = getattr(a, 'size', None)
        values = getattr(a, 'values', None)
        if size is None or size != len(list_values):
            raise AttributeError(f'{BC.NOKMSG} Vector size is incorrect')
        if values is None or any(type(k) != float for k in values):
            raise AttributeError(f'{BC.NOKMSG} Values are not float type')
        if (values is None or
                any(k1 != float(k2) for k1, k2 in zip(values, expected))):
            raise AttributeError(f'{BC.NOKMSG} Values are different to source')
    except AttributeError as err:
        print(err)
    except TypeError:
        print(f'{BC.NOKMSG} Unable to create {BC.bold("Vector")} from list')
    else:
        print(f'{BC.OKMSG} Vector from list created correctly')


@function_name
def test_create_from_tuple():
    try:
        tuple_values = (1, 4)
        expected = [float(v) for v in range(*tuple_values)]
        a = Vector(tuple_values)
        size = getattr(a, 'size', None)
        values = getattr(a, 'values', None)
        if size is None or size != len(expected):
            raise AttributeError(f'{BC.NOKMSG} Vector size is incorrect')
        if values is None or any(type(k) != float for k in values):
            raise AttributeError(f'{BC.NOKMSG} Values are not float type')
        if (values is None or
                any(k1 != float(k2) for k1, k2 in zip(values, expected))):
            raise AttributeError(f'{BC.NOKMSG} Values are different to source')
    except AttributeError as err:
        print(err)
    except TypeError:
        print(f'{BC.NOKMSG} Unable to create {BC.bold("Vector")} from tuple')
    else:
        print(f'{BC.OKMSG} Vector from tuple created correctly')


@function_name
def test_create_tuple_wrong_size():
    try:
        tuple_value = (1, 2, 3)
        Vector(tuple_value)
    except TypeError:
        print(f'{BC.OKMSG} Vector raise error on wrong tuple size')
    else:
        print(f'{BC.NOKMSG} Vector not raise error on wrong tuple')


@function_name
def test_create_from_range():
    try:
        range_int = 4
        expected = [float(v) for v in range(range_int)]
        a = Vector(range_int)
        size = getattr(a, 'size', None)
        values = getattr(a, 'values')
        if size is None or size != len(expected):
            raise AttributeError(f'{BC.NOKMSG} Vector size is incorrect')
        if values is None or any(type(k) != float for k in values):
            raise AttributeError(f'{BC.NOKMSG} Values are not float type')
        if (values is None or
                any(k1 != float(k2) for k1, k2 in zip(values, expected))):
            raise AttributeError(f'{BC.NOKMSG} Values are different to source')
    except AttributeError as err:
        print(err)
    except TypeError:
        print(f'{BC.NOKMSG} Unable to create {BC.bold("Vector")} from range')
    else:
        print(f'{BC.OKMSG} Vector from range created correctly')


@function_name
def test_add_two_vector():
    try:
        a = Vector([1, 2, 3])
        b = Vector([1, 2, 3])
        expected = [2, 4, 6]
        a_op_b = a + b
        values = getattr(a_op_b, 'values', None)
        if any(v1 != v2 for v1, v2 in zip(expected, values)):
            raise ArithmeticError(f'{BC.NOKMSG} Returned values are incorrect')
    except ArithmeticError as err:
        print(err)
    except (TypeError, ValueError):
        print(f'{BC.NOKMSG} Operation {BC.bold("__add__")} not supported')
    else:
        print(f'{BC.OKMSG} Operation {BC.bold("__add__")} work correctly')


@function_name
def test_add_different_vector_size():
    try:
        a = Vector([1, 2, 3])
        b = Vector([1, 2])
        a + b
    except TypeError as err:
        print(f'{BC.NOKMSG} Operation {BC.bold("__add__")} not supported')
    except ValueError:
        print(f'{BC.OKMSG} Operation raise error on diferent vector size')
    else:
        print(f'{BC.NOKMSG} Operation not raise error on diferent vector size')


@function_name
def test_check_attributes():
    try:
        list_values = [1, 2, 3]
        a = Vector(list_values)
        size = getattr(a, 'size', None)
        values = getattr(a, 'values', None)
        if size is None:
            raise ValueError(
                f'{BC.NOKMSG} Vector has not {BC.bold("size")} attribute')
        if type(size) != int:
            raise ValueError(
                f'{BC.NOKMSG} {BC.bold("size")} attribute has to be an int')
        if values is None:
            raise ValueError(
                f'{BC.NOKMSG} Vector has not {BC.bold("values")} attribute')
        if type(values) != list:
            raise ValueError(
                f'{BC.NOKMSG} {BC.bold("values")} attribute has to be a list')
    except ValueError as err:
        print(err)
    except TypeError:
        print(f'{BC.NOKMSG} Vector class not accept arguments')
    else:
        print(f'{BC.OKMSG} Vector has size and values attributes')


@function_name
def test_create_from_float_list():
    try:
        list_values = [float(x) for x in range(3)]
        a = Vector(list_values)
        values = getattr(a, 'values', None)
        if (values is None or any(type(k) != float for k in values)
                or any((k1 != k2 for k1, k2 in zip(values, list_values)))):
            raise TypeError(f'{BC.NOKMSG} Unable to create from float list')
    except TypeError as err:
        print(err)
    else:
        print(f'{BC.OKMSG} Vector from float list created correctly')


@function_name
def test_add_scalar_to_vector():
    try:
        values_list = [float(k) for k in range(4)]
        a = 3
        b = Vector(values_list)
        a_op_b = a + b
        values = getattr(a_op_b, 'values', None)
        expected = [k + 3 for k in values_list]
        if not isinstance(a_op_b, Vector):
            raise ValueError(f'{BC.NOKMSG} Returned value type incorrect')
        if (values is None
                or any(k1 != k2 for k1, k2 in zip(expected, values))):
            raise ValueError(f'{BC.NOKMSG} Returned vector is incorrect')
    except TypeError:
        print(f'{BC.NOKMSG} Operation {BC.bold("__radd__")} not supported')
    except ValueError as err:
        print(err)
    else:
        print(f'{BC.OKMSG} Operation {BC.bold("__radd__")} work correctly')


@function_name
def test_add_wrong_type_to_vector():
    print(f'{BC.NOKMSG} Operation {BC.bold("__radd__")} not supported')


@function_name
def test_add_vector_to_wrong_type():
    print(f'{BC.NOKMSG} Operation {BC.bold("__add__")} not supported')


@function_name
def test_add_vector_to_scalar():
    print(f'{BC.NOKMSG} Operation {BC.bold("__add__")} not supported')


if __name__ == '__main__':
    test_check_attributes()
    test_wrong_type_on_create()
    test_create_from_list()
    test_create_from_float_list()
    test_create_from_tuple()
    test_create_tuple_wrong_size()
    test_create_from_range()
    test_add_two_vector()
    test_add_wrong_type_to_vector()
    test_add_vector_to_wrong_type()
    test_add_different_vector_size()
    test_add_scalar_to_vector()
    test_add_vector_to_scalar()
