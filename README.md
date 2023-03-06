# Experiments



# Experiment 5: Python Loop Performance

Hi! This program compares the execution time of "for loops" and "while loops" . The program will calculate the sum of 1 to n using both loops and compare the execution times.

## How the program works
This is a simple rundown of how this program works:
1. Enter a number (ideally in powers of 10; 10, 100, 1000, ...)
2. The program will calculate the sum of 1 to the number (n) using a for loop and while loop.
3. The program will output the sum of each loop.
4. The program will also output the execution times of each loop.

## for_loop Function 
This function simply uses the for loop function in python. The program will continue looping the code within the for loop for as long as the condition variable is within the range(1, n+1). It will end once the variable is out of the range. 

## while_loop Function
This function used the while loop function in python. A variable is first initialized to a value. This is then compared to a condition or "limit". The lines of code within the while loop will repeatedly run until the condition is false.

## time module
The time module is used in time-related programs/issues. In the context of this experiement, it was used to measure the starting and final time of the functions. 

### Sample
Please enter a number(10, 100, 1000,...): 100000

[FOR LOOP] Sum of 1 to 100000 = 5000050000
[WHILE LOOP] Sum of 1 to 100000 = 5000050000
		
				TIME COMPARISION 
For loop function total time =  -0.005671977996826172
While loop function total time =  -0.005203962326049805

