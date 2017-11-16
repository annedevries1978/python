def detect_anagrams(word, candidates):
    matches = []
    # loop over items in candidates
    for item in candidates:
        temp_word = word.lower()
        item_to_test = item.lower()
        # only compare if length are equal but words are not
        if temp_word != item_to_test and len(item) == len(word):
            print(sorted(temp_word), sorted(item_to_test))
            # Loop over letters in item
            # use sorted instead of for loop
            if sorted(temp_word) == sorted(item_to_test):
                matches.append(item)
    return matches

print(detect_anagrams('master', ["stream", "pigeon", "maters"]))