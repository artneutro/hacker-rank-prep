#!/bin/python3
# https://www.hackerrank.com/challenges/counter-game/problem

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def ispowtwo(n):
    return bin(n).count('1')==1

def counterGame(n):
    # Write your code here
    louise_and_richard = -1
    if n == 1 :
        return 'Richard'
    else :
        # This loop can be removed by checking if the else n is pair or odd
        while n != 1 : 
            # If is power of 2, divide by 2
            if ispowtwo(n) :
                n = int(n/2)
                louise_and_richard *= -1
            # If is not power of 2, look for the next below and reduce this value from it
            else :
                bin_str = str(bin(n))
                next_pow = 2**(len(bin_str) - 3)
                n = n-next_pow
                louise_and_richard *= -1
    if louise_and_richard == -1 :
        return 'Richard'
    else :
        return 'Louise'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()



