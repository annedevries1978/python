def say(number):

    basic = {1: 'one', 2: 'two',
                  3: 'three', 4: 'four',
                  5: 'five', 6: 'six',
                  7: 'seven', 8: 'eight',
                  9: 'nine'}

    tens = {10: 'ten', 20: 'twenty',
            30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty',
            70: 'seventy', 80: 'eighty',
            90: 'ninety'}

    exotic = {11: 'eleven', 12: 'twelve',
              13: 'thirteen'}

    teen = {}

    # split to tenth
    tenth = int(number/10)

    if tenth < 1:
        return basic[number]

    elif number % 10 == 0:
        return tens[number]

    if number in exotic.keys():
        return exotic[number]


print(say(70))
print(say(13))
