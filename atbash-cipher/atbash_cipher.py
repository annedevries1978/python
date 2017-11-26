def encode(plain_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'zyxwvutsrqponmlkjihgfedcba'

    trantab = plain_text.maketrans(plain, cipher)

    return plain_text.translate(trantab)

def decode(ciphered_text):
    pass

print(encode('abcdeabcde'))

