# Experiments


# Experiment 3: Guessing Game

Hi! This program is a number guessing game. The program will choose a random number from a range of numbers for the user to guess. There are only 10 chances for the users to guess the number.

## How the program works
This is a simple rundown of how this program works:
1. Enter the minimum and maximum numbers for the range of numbers you will be guessing from.
2. You will be promped to enter your guess. 
3. If your guess is lower than the number, the program will display "Too Low".
4. If you guess if higher than the number, the program will display "Too High".
5. You may continue guessing until you have consumed your 10 chances or you guess the right number. 
6. The program will then output the right number and your number of guesses. 

## randomNumber Function 
The program imports the random module in python. In this program, a function was created to accept the maximum and minimum range from the user. The maximum and minimum are then inserted into the "randrange()" function where it will generate a random number between the inputted range. 

### Sample: 
*** Welcome to the Number Guessing Game! ***


You may choose the range of numbers to guess from.


Enter maximum number: 20
Enter minumum number: 1

You have 10 chances to guess the number between 1 and 20.

Enter a number: 10

Too low!

Enter a number: 15

Too low!

Enter a number: 17

Congratulations! You guessed the number 17 in 3 tries!
