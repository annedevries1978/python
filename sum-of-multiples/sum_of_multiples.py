def sum_of_multiples(limit, multiples):
    return sum([x for x in range(limit) if any(x % y == 0 for y in multiples)])


print(sum_of_multiples(20,[3,5]))
