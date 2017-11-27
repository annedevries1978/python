import re

def abbreviate(words):
    abbreviation = ""
    x = re.compile(r'\W+')
    word_list = x.split(words)  # create a list of the words
    for a, b in enumerate(word_list):
        abbreviation += word_list[a][0].upper()  # get first letter of each word and capitalize
    return abbreviation


# print(abbreviate('Portable Network-Graphics'))