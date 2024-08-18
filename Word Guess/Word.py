# Python code for  guessing word

import random
import string
from collections import Counter

# list of words
word_list = ["python", "java", "kotlin", "swift"]


# function to choose random word

def choose_word():
    word = random.choice(word_list)
    return word


# main function
def main():
    # Add user input and track count of lives
    print("Available choices are :" ,word_list)
    word = choose_word()
    word_completion = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("H A N G M A N")
    print("I am thinking of a word that is", len(word), "letters long")
    print(display_hangman(tries))
    print(word_completion)

    while tries > 0 and "_" in word_completion:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    print(word_completion)
                    print("You guessed the word correctly!")
                    break

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                word_completion = word
                print(word_completion)
                print("You guessed the word correctly!")
                break

        else:
            print("Not a valid guess.")

        print(display_hangman(tries))
        print(word_completion)

    if tries == 0:
        print("You lost. The word was", word)

    else:
        print(word_completion)

    print("Thank you for playing. Goodbye!")

# function to display hangman
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        "  ----------  ",
        "  |        |  ",
        "  |        O  ",
        "  |       \\|/ ",
        "  |        |  ",
        "  |       / \\",
        "  |             ",
        " -'-------------'",
    ]
    return stages[tries]    


# call main function
if __name__ == "__main__":
    main()
    



    