#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
positive_number = number
modulo_number = (positive_number) % 10
if (number < 0):
    positive_number = number * -1
    modulo_number = ((positive_number) % 10) * -1
print("Last digit of " + str(number) + " is " + str(modulo_number), end="")
if (modulo_number == 0):
    print(" and is 0")
elif (modulo_number < 6):
    print(" and is less than 6 and not 0")
else:
    print(" and is greater than 5")
