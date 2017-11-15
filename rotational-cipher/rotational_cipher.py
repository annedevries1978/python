
def rotate(text, key):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    # set key to 26 otherwise 0 does not work
    if key == 0:
        key = 26
    part1 = plain[-key:]
    part2 = plain[:26-key]
    # take letters from end of string and place them at string start
    result = part1 + part2

    # take into account capital letters
    plain_caps = plain + plain.swapcase()
    caps = result + result.swapcase()

    # use maketrans and translate to convert/map letters
    trantab = text.maketrans(caps, plain_caps)
    str = text
    return str.translate(trantab)


