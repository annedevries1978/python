def say(number):

    basic = {1: 'one', 2: 'two',
             3: 'three', 4: 'four',
             5: 'five', 6: 'six',
             7: 'seven', 8: 'eight',
             9: 'nine',
             10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
             14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
             18: 'eighteen', 19: 'nineteen'
             }

    ten_numbers = {20: 'twenty',
                   30: 'thirty', 40: 'forty',
                   50: 'fifty', 60: 'sixty',
                   70: 'seventy', 80: 'eighty',
                   90: 'ninety'
                   }

    words = ['trillion', 'billion', 'million', 'thousand']

    if number == 0:
        return 'zero'
    elif number in ten_numbers.keys():
        return ten_numbers[number]
    elif 1 <= number < 20:
        return basic[number]
    elif 20 <= number < 100:
        tens, below_ten = divmod(number, 10)
        return ten_numbers[tens*10] + "-" + basic[below_ten]
    else:
        return "Number not in Range!!!"


def number_split(number):
    number_split_list = []
    n = True
    while n is True:
        x, y = divmod(number, 1000)
        number_split_list.append(y)
        number = x
        if len(str(x)) <= 3:
            number_split_list.append(x)
            n = False
        else:
            number_split(number)
    number_split_list.reverse()
    return number_split_list


print(number_split(45))





