#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
positive_number = number    
modulo_number = (positive_number) % 10
if (number < 0):
    positive_number = number * -1
    modulo_number = ((positive_number) % 10) * -1
print("last digit of " + str(number) + " is " + str(modulo_number) + " ", end="")
if ((positive_number) % 10 == 0):
    print("and is 0")
elif ((positive_number) % 10 < 6):
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")
