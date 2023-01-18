import random

#ask the user for the dice type they require:
diceType=int(input("What type of dice do you want? 4, 6 or 12"))

#create a random number between 1 and the highest possible number on the chosen dice type
numberRolled=random.randint(1,diceType)

#display random number:
print(numberRolled)
