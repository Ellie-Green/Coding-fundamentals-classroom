import random 

def get_users_choice():
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("You have entered an invalid choice. Please enter either Rock, Paper or Scissors")
        user_choice = input("Enter your choice: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win"
    else:
        return "Computer wins"
    
def play_game():
    rounds_played = 0
    user_wins = 0
    computer_wins = 0

    while True:
        print(f"\n----- Round {rounds_played + 1} -----")

        user_choice = get_users_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "you" in result.lower():
            user_wins = user_wins + 1
        elif "computer" in result.lower():
            computer_wins = computer_wins + 1

        rounds_played = rounds_played + 1

        print("\nResults:")
        print("Rounds played:", rounds_played)
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
    
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again == "no":
            print("\nThanks for playing! Goodbye.")
            break

#------------- MAIN CODE ----------
play_game()

