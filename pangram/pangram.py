# Better solutiom then mine

import string

def is_pangram(sentence):
    sentence_lower = sentence.lower()

    for char in string.ascii_lowercase:
        if char not in sentence_lower:
            return False

    return True

'''    letter_dict = {'a': 0,
                   'b': 0,
                   'c': 0,
                   'd': 0,
                   'e': 0,
                   'f': 0,
                   'g': 0,
                   'h': 0,
                   'i': 0,
                   'j': 0,
                   'k': 0,
                   'l': 0, 'm': 0, 'n': 0,
                   'o': 0, 'p': 0, 'q': 0,
                   'r' :0, 's': 0, 't': 0,
                   'u' :0, 'v': 0, 'w': 0,
                   'x': 0, 'y': 0, 'z': 0
                }
    sentence = sentence.replace(' ', '')
    for letter in sentence.lower():
        if letter in letter_dict:
            letter_dict.get(letter)

            letter_dict[letter] = letter_dict[letter] + 1
    if 0 in letter_dict.values():
        return False
    else:
        return True 
    '''


is_pangram('the quick brown fox jumps over the lazy dog')