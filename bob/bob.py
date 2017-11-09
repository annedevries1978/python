def hey(phrase):
    phrase = phrase.rstrip()
    if len(phrase) == 0 or phrase.isspace():
        return "Fine. Be that way!"

    elif phrase.isupper():
        return "Whoa, chill out!"
    elif phrase[-1] == "?":
        return "Sure."
    else:
        return "Whatever."


print(hey("\t\t\t\t\t\t\t\t\t\t"))

print("\thhh")