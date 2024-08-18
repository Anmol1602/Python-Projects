#Python code for number guesing 

import random

number = random.randint(1,100)

# take user input  

guess = int(input("Guess a number between 1 and 100: "))

# keep track of number of guesses

count = 1

while guess != number:
    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Guess again: "))
    count += 1

print("Congratulations! You guessed the number.")

print("It took you", count, "guesses.")
