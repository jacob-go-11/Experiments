import time

#for loop function
def for_loop(num):
    total = 0
    #calculates sum using for loop
    for x in range (1, n+1):
        total += x
    return total

#while loop function
def while_loop(num):
    x = 1
    total = 0
    #calculates sum using while loop
    while x<=num:
        total += x
        x += 1
    return total

#input numbers from powers of 10
n = int(input("Please enter a number(10, 100, 1000,...): "))
fl_sum = for_loop(n)
wl_sum = while_loop(n)

#prints sum of numbers from 1 to n 
print("\n[FOR LOOP] Sum of 1 to %d = %d" %(n, fl_sum))
print("[WHILE LOOP] Sum of 1 to %d = %d\n" %(n, wl_sum))

print("\tTIME COMPARISON BETWEEN LOOPS\n")
#measures and prints executed time for for_loop function
time_start1 = time.time()
for_loop(n)
time_end1 = time.time()
time_total1 = time_end1 - time_start1
print("For loop function total time = ", time_total1)

#measures and prints executed time for while_loop function
time_start2 = time.time()
for_loop(n)
time_end2 = time.time()
time_total2 = time_end2 - time_start2
print("While loop function total time = ", time_total2)    