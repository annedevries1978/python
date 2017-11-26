import re

def encode(plain_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'zyxwvutsrqponmlkjihgfedcba'

    #remove punctuation
    regex = re.compile('[!" ".,]')
    text_without_puntuation = regex.sub('', plain_text).lower()
    trantab = text_without_puntuation.maketrans(plain, cipher)
    encoded_text = text_without_puntuation.translate(trantab)
    test = [encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)]
    return " ".join(test)


def decode(ciphered_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'zyxwvutsrqponmlkjihgfedcba'
    trantab = ciphered_text.maketrans(cipher, plain)
    plain_text = ciphered_text.translate(trantab)
    return plain_text.replace(" ", "")

