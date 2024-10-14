def apply_all_func(int_list, *functions):
    results = {}
    for funcs in functions:
        results[funcs.__name__] = funcs(int_list)
    return results


def min_arg(int_list):
    return min(int_list)


def max_arg(arg):
    return max(arg)


def len_arg(arg):
    return len(arg)


def sum_arg(arg):
    return sum(arg)


def sorted_arg(arg):
    return sorted(arg)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
