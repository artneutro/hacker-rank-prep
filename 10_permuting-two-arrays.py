#!/bin/python3
# https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    # https://www.w3schools.com/python/ref_func_sorted.asp
    A_sorted = sorted(A)
    B_sorted_reverse = sorted(B, reverse=True)
    for i in range(len(A)) :
        if A_sorted[i] + B_sorted_reverse[i] < k :
            return 'NO'
    return 'YES'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()







