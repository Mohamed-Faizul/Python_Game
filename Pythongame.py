import random

name = input("What your name :")
print('Good luck ',name)

words = ["Computer","laptop","Server","Internet"]
word = random.choice(words)

print("Guess the Character :")

guesses = ''
turns = 3

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1

    if failed == 0:
        print('You are Win...')
        print("The Word is :",word)
        break

    guess = input("Guess the Character :")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have ",turns,"more guesses")

    if turns == 0:
        print('Sorry',name,"You are lose & the Secret word is ",word)