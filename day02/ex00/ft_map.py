def ft_map(function_to_apply, list_of_inputs):
    list_new = []
    for v in list_of_inputs:
        list_new.append(function_to_apply(v))
    return iter(list_new)
