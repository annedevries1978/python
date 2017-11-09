import re

def word_count(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace('_', ' ')
    # word_list = phrase.split(" ",':')

    rgx = re.compile("(\w[\w'\w]*\w|\w)")
    word_list = rgx.findall(phrase)
    #word_list = re.split("\w[\w']+", phrase)
    word_dict = {}
    for word in word_list:
        if word_dict.get(word):
            word_dict[word] = word_dict[word]+1
        else:
            word_dict[word] = 1
    return word_dict





print(word_count("hey,my_spacebar_is_broken."))