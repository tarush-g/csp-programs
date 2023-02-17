def wordMultiple(words):
    final = {}
    for word in words:
        if word in final:
            final[word] = True
        else:
            final[word] = False
    return final

