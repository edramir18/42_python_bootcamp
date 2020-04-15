def ft_reduce(function_to_apply, list_of_inputs):
    itr = iter(list_of_inputs)
    a = next(itr, None)
    for b in itr:
        a = function_to_apply(a, b)
    return a
