def pairs(strings):
    words = {}
    for word in strings:
        if word not in words:
            words[word[0]] = word[-1]
    return words

print(pairs(["code", "bug"]))

