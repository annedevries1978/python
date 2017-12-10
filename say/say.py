def say(number):
    number = int(number)
    if 0 <= number < 1000000000000:
        string = []
        number = insert_scale(number)
        for pos, num in enumerate(number):
            if isinstance(num, int):
                if len(str(num)) < 3 and pos == len(number)-1 and len(number) > 1:
                    string.append('and ' + basic_num(num))
                elif len(str(num)) < 3:
                    string.append(basic_num(num))
                else:
                    x, y = divmod(num, 100)
                    if y == 0:
                        string.append(str(basic_num(x)) + ' hundred')
                    else:
                        string.append(str(basic_num(x)) + ' hundred and ' + basic_num(y))

            else:
                string.append(num)
        s = " "
        text = s.join(string)

        return text
    else:
        raise ValueError


def basic_num(number):
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
        return ten_numbers[tens * 10] + "-" + basic[below_ten]
    else:
        return "Number not in Range!!!"


def number_split(number):
    number_split_list = []
    n = True
    while n is True:
        x, y = divmod(number, 1000)
        number_split_list.append(y)
        if len(str(x)) <= 3:
            number_split_list.append(x)
            n = False
        else:
            number = x
            number_split(number)

    number_split_list.reverse()
    return number_split_list


def insert_scale(number):
    num_list = number_split(number)
    out = []
    words = ['trillion', 'billion', 'million', 'thousand']
    start_point = 4 - len(num_list)
    for x, y in enumerate(num_list):
        if x < len(num_list)-1:
            start_point += 1
            if y != 0:
                out.append(y)
                out.append(words[start_point])
        else:
            out.append(y)
    if len(out) > 1 and out[-1] == 0:
        return out[:-1]
    else:
        return out
