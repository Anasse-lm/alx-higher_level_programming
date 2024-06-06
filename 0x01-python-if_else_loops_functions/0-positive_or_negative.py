#!/usr/bin/python3

import random as rm

number = rm.randint(-10, 10)

if ( number < 0 ):
    print( str(number)+ " is negative" )
elif (number > 0):
    print( str(number)+ " is positive" )
else:
    print( str(number)+ " zero" )
