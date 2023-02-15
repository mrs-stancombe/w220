print("Let's roll!!")

#this will important the rando functions
import random

#this randomizes our 'die'
die1 = random.randrange(1,6)
die2 = random.randrange(1,6)

#this provides the total of the 'roll'
total = die1 + die2

# this turns each number into a string type so that it can be printed
die3 = str(die1)
die4 = str(die2)
message = str(total)

print("You rolled a " + die3 + " and a " + die4)
print("Your total is " + message)
