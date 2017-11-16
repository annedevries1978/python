def detect_anagrams(word, candidates):
    matches = []
    # loop over items in candidates
    for item in candidates:
        temp_word = word.lower()
        item_to_test = item.lower()
        # only compare if length are equal
        if temp_word != item_to_test and len(item) == len(word):

            # Loop over letters in item
            for x in range(0, len(item)):
                # if letter found in word strip word of letter
                if item_to_test[x] in temp_word:
                    #print("found letter:", item[x])
                    temp_word = temp_word.replace(item_to_test[x], "", 1)

                    # all letters in item are in word
                    if len(temp_word) == 0:
                        matches.append(item)


    return matches
