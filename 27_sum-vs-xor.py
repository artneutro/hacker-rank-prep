#!/bin/python3
# https://www.hackerrank.com/challenges/one-month-preparation-kit-sum-vs-xor/problem

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def ispowtwo(n):
    return bin(n).count('1')==1

def sumXor(n):
    # Write your code here
    # It will count the number zeroes in the binary rep and power 2 to this value
    if n == 0:
       return 1
    else:
        return pow(2, (str(bin(n)).count('0')-1))
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()

