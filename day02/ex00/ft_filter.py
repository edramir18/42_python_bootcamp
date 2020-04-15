def ft_filter(function_to_apply, list_of_inputs):
    list_new = []
    for v in list_of_inputs:
        if function_to_apply(v):
            list_new.append(v)
    return iter(list_new)
