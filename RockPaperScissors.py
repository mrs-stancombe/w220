# import random
import random

# define list and conditions for program to run
while True:
    userPlay = input("Enter a choice (rock, paper, scissors): ")
    playChoices = ["rock", "paper", "scissors"]
    computerPlay = random.choice(playChoices) # allows the computer to choose randomly between rock, paper, and scissors
    print("You chose " + userPlay + ", computer chose " + computerPlay + ".") # prints what the user and computer chose first
    if userPlay == computerPlay:
        print("Both players selected {userPlay}. It's a tie!")
    elif userPlay == "rock":
        if computerPlay == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif userPlay == "paper":
        if computerPlay == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif userPlay == "scissors":
        if computerPlay == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
