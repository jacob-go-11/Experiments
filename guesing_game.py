import random

#generates random number from given range
def randomNumber(lo, hi):
    ranNum = random.randrange(lo, hi)
    print("\nYou have 10 chances to guess the number between %d and %d." %(lo, hi))
    return ranNum 

#initial welcoming          
print("*** Welcome to the Number Guessing Game! ***")
print("\nYou may choose the range of numbers to guess from.")

#user can choose range of numbers to guess from
high = int(input("\nEnter maximum number: "))
low = int(input("Enter minumum number: "))

#calls randonNumber function
num = randomNumber(low, high)

numOfGuesses = 0
#loops for ten times or until number is guessed
while numOfGuesses < 10:
    guess = int(input("\nEnter a number: "))
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    else: 
        break
    numOfGuesses += 1

#checks if number is guessed
if guess == num:
    print("Congratulations! You guessed the number %d in %d tries!" % (num, numOfGuesses+1))
else:
    print("The number is %d. Try again next time!" % num)
