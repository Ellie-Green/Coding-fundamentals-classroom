import random   # Built in function that allows for random items to be selcted/ generated

# Having individual functions for each aspect of the game, helps to make the code clearer and it is easy to reference if the code is needed in multiple places as you only need to call the function instead of re-writing the code
def get_users_choice():     # Getting the users choice is in its own function
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()      # Asks the user for their input and converts it all to lowercase
    while user_choice not in ["rock", "paper", "scissors"]:     # If the users input is not in the list then an error message will be displayed and they will be asked to re-enter their choice
        print("You have entered an invalid choice. Please enter either Rock, Paper or Scissors")
        user_choice = input("Enter your choice: ").lower()
    return user_choice

def get_computer_choice():  # Getting the computers choice is also its own function
    return random.choice(["rock", "paper", "scissors"])     # Makes use of the random function by getting the computer to select a random item from the list

def determine_winner(user_choice, computer_choice): 
    if user_choice == computer_choice:  # IF statements are used to work out who the winner is. This done by comparing the the items and returning the corresponding message
        return "Tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win"
    else:
        return "Computer wins"
    
def play_game():        # This is the main function that actual codes the game play. It will call the other functions as and when they are needed
    rounds_played = 0   # Will be used to keep track of how many rounds have been played 
    user_wins = 0       # stores the amount of wins for both the user and the computer
    computer_wins = 0

    while True:         # The game will run as long as the while statement is true or if a break is called
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

        print("\nResults:")                     # Outputs how many rounds played, and how many times the user and the computer have won based off of previous lines of code that called other functions
        print("Rounds played:", rounds_played)
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
    
        play_again = input("Do you want to play another round? (yes/no): ").lower()                 # Gives the user the option of playing again 
        if play_again == "no":
            print("\nThanks for playing! Goodbye.")
            break

#------------- MAIN CODE ----------
play_game()             # Within the main part of the code the play_game function is called

