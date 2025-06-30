import random


def randomNumGen():
    return random.randint(1, 100) # gives us a random number between 1 and 100


def winningText(correctGuess):
    print(f"Congrats! You got it, the number was: {correctGuess}.")
    print("Thanks for playing!")
    # the game ends after this :)


def isInt(guess):
    if isinstance(guess, str):
        return guess.isdigit()
    return False


def filterGuess(guess):
    while not isInt(guess):  # loop continues if guess is not a number
        print("That guess will not do! Enter only numbers.")
        guess = input("Make a guess: ")
    return int(guess)  # return guess as a number


def promptUser():
    guess = input("Make a guess: ")  # this is how we will get a response from our user
    guess = filterGuess(guess)  # special function that only allows our guess to be a number
    return guess  # return our guess, ensured to be a number


def guessingLoop(correctGuess):
    guess = promptUser()  # make an initial guess

    # loop until guess is correct
    while guess != correctGuess:  # check if the result was correct

        if guess > correctGuess:  # guess was too high
            print("TOO HIGH! Guess again.")  # inform the user

        elif guess < correctGuess:  # guess was too low
            print("TOO LOW! Guess again.")  # inform the user

        guess = promptUser()  # prompt user for another guess

    # if we made it past the loop, then the user guessed correctly
    winningText(correctGuess)  # end the game and thank player


def welcomeText():
    print("Welcome to NUMBER GUESSER!")
    print("After you guess a number, I'll tell you if it was TOO HIGH or TOO LOW")
    print("Ready? Go!")


if __name__ == "__main__":
    welcomeText()
    secretNum = randomNumGen()
    guessingLoop(secretNum)

