import random

def get_user_choice():
    while True:
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            return "rock"
        elif choice == "2":
            return "paper"
        elif choice == "3":
            return "scissors"
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_num = 1

    while True:
        print(f"\n--- ROUND {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"\nCurrent Scores -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != "y":
            print("\nThank you for playing!")
            if user_score > computer_score:
                print("🎉 Congratulations! You won the game!")
            elif computer_score > user_score:
                print("💻 Computer wins the game! Better luck next time.")
            else:
                print("🤝 The game ended in a tie.")
            break

        round_num += 1

if __name__ == "__main__":
    print("==== Welcome to Rock-Paper-Scissors Game ====")
    play_game()
    
