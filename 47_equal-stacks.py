#!/bin/python3
# https://www.hackerrank.com/challenges/equal-stacks/problem

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    # Performance improvement: get the sum only once to avoid TLE
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    # Pointers to get the current top in stack
    h1_p = 0
    h2_p = 0
    h3_p = 0
    # While the 3 stacks are different, check the higher and pop the top
    while (sum_h1 != sum_h2 or sum_h1 != sum_h3 or sum_h2 != sum_h3) :
        max_height = max(sum_h1, sum_h2, sum_h3)
        if max_height == sum_h1 :
            sum_h1 = sum_h1 - h1[h1_p]
            h1_p += 1
        if max_height == sum_h2 :
            sum_h2 = sum_h2 - h2[h2_p]
            h2_p += 1
        if max_height == sum_h3 :
            sum_h3 = sum_h3 - h3[h3_p]
            h3_p += 1
    return sum_h1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

