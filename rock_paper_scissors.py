import random

# Print statement to welcome player
print("Welcome to the game of rock, paper, scissors. \nWhat is your name? " )
name = input()
print("Would you like to play " + name)
response = input()
if response.lower() != "yes" and response.lower() != "y":
    quit()

print("Make your selection")

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter 1 for Rock | 2 for Paper | 3 for Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input != "1" and user_input != "2" and user_input != "3":
        print("Invalid selection. Please try again.")
        continue

    if user_input == "1":
        user_choice = "rock"
    elif user_input == "2":
        user_choice = "paper"
    elif user_input == "3":
        user_choice = "scissors"
 

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_choice == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_choice == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_choice == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times \nWell done.")
print("The computer won " + str(computer_wins) + " times \nYou scored " + str(user_wins) + " points")
print("Goodbye!")