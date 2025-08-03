import random

def get_user_choice():
    print("Welcome to rock, paper, scissors game")
    game = ["rock", "paper", "scissors"]
    for i, options in enumerate(game, start = 1):
       print(f"{i}. {options}")

    choice = int(input("Enter your choice: "))
    if choice >= 1 and choice <= 3:
       return game[choice - 1]
    else:
       choice = input("\nInvalid Operation! Enter [1: rock, 2: paper, 3: scissors]: ")
       return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def find_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
       return "The game is drow"
    elif ((user_choice == "rock" and computer_choice == "scissors") or
         (user_choice == "paper" and computer_choice == "rock") or
         (user_choice == "scissors" and computer_choice == "paper")):
          return "You Won"
    else:
         return "You lost! Computer is Won"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYour choice: {user_choice}")
    print(f"Computer choice: {computer_choice}\n")

    result = find_winner(user_choice, computer_choice)
    print(result)

main()
