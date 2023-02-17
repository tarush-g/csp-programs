import random

fhand = open('words.txt')
for line in fhand:
    words = line.split()

word = random.choice(words)

incorrect = []
correct = []
max_incorrect = 6

man =[\
'   O ',\
'  /|\ ',\
' / | \ ',\
'   |   ',\
'   |     ',\
' _/ \_ '
]

def print_guy():
    print('-----\n    |')
    for i in range(len(incorrect)):
        print(man[i])
    
    


def count_unique(w):
    a=""
    for i in w:
        if i not in a:
            a+=i
    return len(a)

unique = count_unique(word)

    
def guess():
    valid_guess = False
    while not valid_guess:
        guess = input("guess letter: ")
        if (not guess.isalpha()) or (len(guess)!=1) or (guess in incorrect) or (guess in correct):
            print("error: enter valid letter")
        else:
            break
    return guess

def print_letters():
    for letter in range(len(word)):
        if word[letter] in correct:
            print(word[letter], end='')
        else:
            print("_", end='')
    print("\nIncorrect: "+str(incorrect))
    
def check_guess(guess):
    if guess in word:
        print(guess+" was in the word")
        correct.append(guess)
    else:
        print(guess+" was not in the word")
        incorrect.append(guess)
            
def check_game():
    if len(incorrect) == max_incorrect:
        return 1
    if len(correct) == unique:
        return 2
    else:
        return False
    
def game():
    game = False
    while not game:
        usrguess = guess()
        check_guess(usrguess)
        print_letters()
        print_guy()
        game = check_game()
    if game == 1:
        print('you lost')
    if game == 2:
        print('you won')
        
game()
