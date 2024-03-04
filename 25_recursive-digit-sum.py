#!/bin/python3
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    # Phase 1: Sum all the digits
    p = 0
    for i in n :
        p += int(i)
    # Phase 2: Multiply k times (concatenate)
    concatenated = p*k
    # Phase 3: Iteratively sum the digits until number of digits is 1
    while (len(str(concatenated)) > 1) :
        p = 0
        for i in range(len(str(concatenated))) :
            p += int(str(concatenated)[i])
        concatenated = p
    return concatenated


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()









