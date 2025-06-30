def displayInstructions():
    # Here is where you will fill in some instructions!
    print("Hello World")


def playGame():
    noun1 = input("Please give me a noun: ")

    # Here is where you will ask for more nouns, verbs, and adverbs
    # You could even throw in some numbers or sound effects :)

    # Next, use the inputted words in your story!
    # The lines below are to remind you of the formatted string, please change them!

    print(f"Here is your noun: {noun1}!")
    print(f"Oh, and here it is again: {noun1}, just in case you missed it.")


if __name__ == "__main__":
    displayInstructions()
    playGame()