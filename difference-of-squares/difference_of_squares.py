def square_of_sum(number):
    range_num = number + 1
    y = 0
    for x in range(1, range_num):
        y += x
    return y**2


def sum_of_squares(number):
    range_num = number + 1
    y = 0
    result= 0
    for x in range(1, range_num):
        y += x**2
    return y


def difference(number):
    x = square_of_sum(number)
    y = sum_of_squares(number)
    return x - y


