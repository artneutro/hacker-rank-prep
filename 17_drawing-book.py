#!/bin/python3
# https://www.hackerrank.com/challenges/drawing-book/problem

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    # Pair number of pages in the book
    if n%2 == 0 : 
        # Page to look is pair
        if p%2 == 0 :
            return min(int(p/2),int((n-p)/2))
        # Page to look is odd
        else :
            return min(int(p/2),int((n-p)/2)+1)
    # Odd number of pages in the book
    else :
        return min(int(p/2),int((n-p)/2))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()




