import random
num=random.randint(1,100)
guessing=True
while guessing == True:
    guess = int(input('pick a random number: '))
    if guess > num:
        print('too high')
    elif guess < num:
        print('too low')
    else:
        print('correct number')
        guessing = False
