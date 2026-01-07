import random 

while True:
    user_action = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
    actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(actions)
    print(f"you chose: {user_action} computer chose: {computer_action}")
    if user_action == computer_action:
        print("It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win!")
        else:
            print("You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
        else:
            print("You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win!")
        else:
            print("You lose.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Thanks for playing!")
        