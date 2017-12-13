def largest_product(series, size):
    start = 0
    end = size
    result_list = []
    if size > len(series):
        raise ValueError
    elif size == 0:
        return 1
    else:
        for x, y in enumerate(series):
            if size == len(series[start:end]):  # series length equals size
                result = series[start:end]
                end += 1
                start += 1
                num_list = [int(a) for a in list(result)]
                result_list.append(num_list)
        return multiply_nested_list(result_list)


def multiply_nested_list(nested_list):
    return max([product(i) for i in nested_list])


def product(num_list):
    product = 1
    for number in num_list:
        product *= number
    return product
