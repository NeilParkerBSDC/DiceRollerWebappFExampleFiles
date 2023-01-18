import random

#ask the user for the dice type they require:
diceType=int(input("What type of dice do you want? 4, 6 or 12? " ))

#Create a loop to keep asking if they want to re-rerun the dice roller:
#Note this keeps the dice type the user has set - we are not re-asking the question 

reRun="Y" #setting the re -run state to "yes", so that the program will keep running until the user types something other than "Y"
while reRun=="Y": #The condition for the while loop
    #create a random number between 1 and the highest possible number on the  
    #chosen dice type
    numberRolled=random.randint(1,diceType)

    #display random number:
    print("You rolled a " + str(numberRolled)) # note I have combined the number 
    #rolled with some test, so I have had to convert the value stored in the 
    #variable to a string
    reRun=input("Do you want to roll another (Y or N)? ")

