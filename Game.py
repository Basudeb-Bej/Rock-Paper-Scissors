import random

def get_user_choice():
    game = ["rock", "paper", "scissors"]
    print("\nRock, Paper, Scissors Game")
    for i, option in enumerate(game, start=1):
        print(f"{i}. {option.capitalize()}")

    while True:
        try:
            choice = int(input("Enter your choice : "))
            if 1 <= choice <= 3:
                return game[choice - 1]
            else:
                print("Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def find_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        print(f"\nRound {round_num}")
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        winner = find_winner(user, computer)

        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nScore: You – {user_score} | Computer – {computer_score}")

        again = input("\nDo you want to play another round? (y/n): ").lower()
        if again != 'y':
            print("\nFinal Score:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            if user_score > computer_score:
                print("You win overall!")
            elif user_score < computer_score:
                print("Computer wins overall")
            else:
                print("It's a tie overall!")
            print("\nThanks for playing!")
            break

        round_num += 1

if __name__ == "__main__":
    main()
