import random
import tkinter as tk
from tkinter import messagebox

# Initialize win counters
player_wins = 0
computer_wins = 0

# Game options
choices = ["rock", "paper", "scissors"]


# Function to handle the game logic
def play(user_choice):
    global player_wins, computer_wins

    computer_choice = random.choice(choices)
    result = ""

    if (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
        player_wins += 1
    elif user_choice == computer_choice:
        result = "It's a tie!"
    else:
        result = "You lose!"
        computer_wins += 1

    result_label.config(text=f"Computer chose {computer_choice}. {result}")
    player_score_label.config(text=f"Player Wins: {player_wins}")
    computer_score_label.config(text=f"Computer Wins: {computer_wins}")


# Function to quit the game
def quit_game():
    root.quit()


# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Create and place widgets
tk.Label(root, text="Choose your option:").pack()

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Rock", command=lambda: play("rock")).grid(row=0, column=0)
tk.Button(button_frame, text="Paper", command=lambda: play("paper")).grid(row=0, column=1)
tk.Button(button_frame, text="Scissors", command=lambda: play("scissors")).grid(row=0, column=2)
tk.Button(button_frame, text="Quit", command=quit_game).grid(row=0, column=3)

result_label = tk.Label(root, text="")
result_label.pack()

player_score_label = tk.Label(root, text=f"Player Wins: {player_wins}")
player_score_label.pack()

computer_score_label = tk.Label(root, text=f"Computer Wins: {computer_wins}")
computer_score_label.pack()

# Run the application
root.mainloop()
