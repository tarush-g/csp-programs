def remove_duplicates(items):
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list

def wordLen(strings):
    strings2 = remove_duplicates(strings)
    words = {}
    for word in strings2:
        words[word[0]] = word[-1]
    return words

print(wordLen(["a", "bb", "a", "bb"]))
