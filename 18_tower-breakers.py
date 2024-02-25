#!/bin/python3
# https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/problem
import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    # If the height is 1, player 2 will win
    # Also if the number of towers is pair
    if m == 1 or n%2 == 0 :
        return 2
    else :
    # If the number of towers is odd and height 2+, player 1 will win
        return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()



