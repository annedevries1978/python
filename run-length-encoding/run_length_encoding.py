def decode(string):
    decoded = ""
    for i in range(len(string)):
        if string[i].isnumeric():
            if string[i + 1].isnumeric():
                decoded += string[i + 2] * (int(string[i] + string[i + 1]) - 1)
            elif not string[i - 1].isnumeric():
                decoded += string[i + 1] * (int(string[i]) - 1)
        else:
            decoded += string[i]
    return decoded


def encode(string):
    if string is "":
        return string

    compression = ""
    letter = string[0]
    count = 1

    for char in string[1:]:
        if char == letter:
            count += 1
        else:
            compression += (str(count) if count != 1 else "") + letter
            letter = char
            count = 1

    compression += (str(count) if count != 1 else "") + letter

    return compression


print(decode('2A2B2C'))