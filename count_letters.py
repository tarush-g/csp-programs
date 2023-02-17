string = 'eriguabwerunawrogn[aerijgawor npwiaengpwiagpwiagnpegn'
def count_letter(string):
    letters = {}
    for letter in string:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] = letters[letter]+1
    return letters
print(count_letter(string))
