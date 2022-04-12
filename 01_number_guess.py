from random import randint
number = randint(1, 10)
guesses = 0

while guesses <3:
    guess = int(input("Guess a number between 1-10! "))
    guesses = guesses + 1
    if guess != number:
        print("Incorrect, try again!")
    elif guess == number:
        print("Correct, well done!")
        print("You guessed the number in {} tries!".format(guesses))
        break
else:
    print("You've run out of guesses!")

