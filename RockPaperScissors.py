# import random
import random

# define list
plays = ["rock", "paper", "scissors"]

# define user input
print("Let's play rock, paper, scissors!")
userChoice = input("Please choose 'rock', 'paper', or 'scissors': ")

# define computer random output
computerChoice = random.choice(plays)

# define rules
if computerChoice = "rock":
  if userChoice = "paper":
    print("Paper beats rock! You win!")
  if userChoice = "scissors":
    print("Rock beats scissors! The computer wins!")
  if userChoice = "rock":
    print("It's a tie! Try again!")
  else:
    print("Sorry, I couldn't understand what you wrote. Please try again and type 'rock', 'paper, or 'scissors'."
        
if computerChoice = "paper":
  if userChoice = "scissors":
    print("Scissors beats paper! You win!")
  if userChoice = "rock":
    print("Paper beats rock! The computer wins!")
  if userChoice = "paper":
    print("It's a tie! Try again!")
  else:
    print("Sorry, I couldn't understand what you wrote. Please try again and type 'rock', 'paper, or 'scissors'.")

if computerChoice = "scissors":
  if userChoice = "paper":
    print("Scissors beats paper! The computer wins!")
  if userChoice = "rock":
    print("Rock beats scissors! You win!")
  if userChoice = "scissors":
    print("It's a tie! Try again!")
  else:
    print("Sorry, I couldn't understand what you wrote. Please try again and type 'rock', 'paper, or 'scissors'.")
          
