def firstChar(words):
    final = {}
    for word in words:
        if word[0] not in final:
            final[word[0]] = word
        else:
            final[word[0]] += word 
    return final

print(firstChar(['salt', 'tea', 'soda', 'toast']))
