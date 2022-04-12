from random import randint
number = randint(1, 10)
guesses = 0

while guesses < 3:
    guess = int(input("Guess a number between 1-10! "))
    guesses = guesses + 1

    if guess == number:
        print("Correct, well done!")
        print("You guessed the number in {} tries!".format(guesses))
        break

    elif guess > number:
        print("Lower!")
    elif guess < number:
        print("Higher!")

else:
    print("You've run out of guesses!")
