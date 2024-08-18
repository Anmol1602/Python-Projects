import random

print("ROCK, PAPER, SCISSORS")

while True:
    user_score = 0
    computer_score = 0
    
    # Play 3 rounds
    for _ in range(3):
        user_action = input("Enter a choice (rock, paper, scissors): ").lower()
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
        
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win this round!")
                user_score += 1
            else:
                print("Paper covers rock! You lose this round.")
                computer_score += 1
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win this round!")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose this round.")
                computer_score += 1
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win this round!")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose this round.")
                computer_score += 1
        else:
            print("Invalid input. Please choose rock, paper, or scissors.")
        
        print(f"Score -> You: {user_score}, Computer: {computer_score}")
    
    # Determine the overall winner after 3 rounds
    if user_score > computer_score:
        print("Congratulations! You won the best of 3 games!")
    elif computer_score > user_score:
        print("Computer won the best of 3 games!")
    else:
        print("It's a tie after 3 rounds! Proceeding to a tiebreaker round...")
        # Tiebreaker round
        while True:
            user_action = input("Tiebreaker - Enter a choice (rock, paper, scissors): ").lower()
            computer_action = random.choice(possible_actions)
            
            print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
            
            if user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie! Try again.")
            elif user_action == "rock":
                if computer_action == "scissors":
                    print("Rock smashes scissors! You win the tiebreaker!")
                    user_score += 1
                else:
                    print("Paper covers rock! You lose the tiebreaker.")
                    computer_score += 1
            elif user_action == "paper":
                if computer_action == "rock":
                    print("Paper covers rock! You win the tiebreaker!")
                    user_score += 1
                else:
                    print("Scissors cuts paper! You lose the tiebreaker.")
                    computer_score += 1
            elif user_action == "scissors":
                if computer_action == "paper":
                    print("Scissors cuts paper! You win the tiebreaker!")
                    user_score += 1
                else:
                    print("Rock smashes scissors! You lose the tiebreaker.")
                    computer_score += 1
            else:
                print("Invalid input. Please choose rock, paper, or scissors.")
                continue  # Invalid input doesn't count as a round
            
            if user_score > computer_score:
                print("Congratulations! You won the game in the tiebreaker!")
            else:
                print("Computer won the game in the tiebreaker!")
            break
    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Bye!")

#If the scores are tied after 3 rounds, a tiebreaker round is initiated.
#The tiebreaker continues until there's a clear winner (no ties in the tiebreaker).