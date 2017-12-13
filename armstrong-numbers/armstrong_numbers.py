def is_armstrong(number):
    number_of_digits = len(str(number))
    # add digits to list, multiply by power of number of digits and sum
    result = sum([int(i)**number_of_digits for i in str(number)])
    if result == number:
        return True
    else:
        return False
