import random

# Initialize win counters
player_wins = 0
computer_wins = 0

# Game options
choices = ["rock", "paper", "scissors"]

while True:
    # Get user input
    user_choice = input("Enter Rock / Paper / Scissors or Q to quit: ").lower()
    if user_choice == "q":
        break

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice, please try again.")
        continue

    # Computer makes a choice
    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}.")

    # Determine the winner
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        player_wins += 1
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You lose!")
        computer_wins += 1

# Print the final results
print(f"You won {player_wins} times.")
print(f"The computer won {computer_wins} times.")
print("Thanks for playing!")
