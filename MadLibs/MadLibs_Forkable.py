def displayInstructions():
    # Here is where you will fill in some instructions!
    print("Instructions go here!")


def playMadLibs():

    # Here is where you will ask for more nouns, verbs, and adverbs
    # You could even throw in some sound effects :)

    noun1 = input("Please give me a noun: ")

    # Next, use the inputted words in your story!
    # To do so, use the formatted string, as shown below:

    print(f"Here is your noun: {noun1}!")
    print(f"Oh, and here it is again: {noun1}, just in case you missed it.")


if __name__ == "__main__": # this is a funky line that just means start the program
    displayInstructions()
    playMadLibs()

    # Here is a link to the python tutorial slideshow again:
    # https://tinyurl.com/python-slideshow
