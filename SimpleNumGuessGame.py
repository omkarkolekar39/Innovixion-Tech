import random
n = random.randrange(1,10)
ans = int(input("Enter any number: "))
while n!= ans:
    if ans < n:
        print("Too low")
        ans = int(input("Guess the Number again: "))
    elif ans > n:
        print("Too high!")
        ans = int(input("Guess the Number again: "))
    else:
        break
print("You Guessed the Right Number!")