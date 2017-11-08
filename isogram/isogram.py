'''
Examples of isograms:

- lumberjacks
- background
- downstream
- six-year-old
'''

def is_isogram(string):
    letters = []
    for letter in string.lower():
        if letter == ' ' or letter == '-':
            letters.append(letter)
        if letter not in letters:
            letters.append(letter)

    if len(letters) == len(string):
        return True
    else:
        return False

