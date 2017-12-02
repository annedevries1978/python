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
    pass

print(say(13))
print(say(0))
print(say(5))
print(say(42))
print(say(50))
print(say(-1))
print(say(100))



