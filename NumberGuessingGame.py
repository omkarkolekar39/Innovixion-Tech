import random
import math
#Imported Libraries

low = int(input("Enter Lowest Number: "))
high = int(input("Enter Highest Number: "))
#Taking Input From Users

num = random.randint(low,high)
#Generating Random Number Between the Range

print("\n\tYou Have",round(math.log(high - low + 1, 2)),"Chances to Guess the Number!\n")
#Using Math Log Method to print the Number of Guesses Avaliable to User Based on Range

guess = 0
#Declaring Guess Variable

while guess < math.log(high - low, 2):
    guess += 1
    #Calculation of minimum number of Guesses which Depends on Range
    
    ans = int(input("Guess the Number: "))
    #Taking The Anwer as Input which the User Guesses the Random Number
    
    
    #Printing The Answers based on the User Gusses the Number
    if num == ans:
        print("\n\tCongratulations You did it in",guess, "try\n")
        break
    #The While Loop will Break if the User Guesses the Correct Answer
    
    elif num > ans:
        print("\n\tThe Number you Guessed is too Small!\n")
    #This Elif will Execute if the Number Guessed by User is Less the Answer
    
    elif num < ans:
        print("\n\tThe Number you Guessed is too High!\n")
        #This Elif will Execute if the Number Guessed by User is High the Answer
        
if guess >= math.log(high - low + 1, 2):
    print("\n\tThe Number was ",num," Which You Could Not Guess!\n\tBetter Luck Next Time!\n")
    #If the User is Unable to Guess the Number in the Given Number of Guesses
    #Then This if Statement Will be Executed