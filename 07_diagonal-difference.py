#!/bin/python3
# https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    counter = 0
    for i in arr :
        left_diagonal_sum = left_diagonal_sum + i[counter]
        right_diagonal_sum = right_diagonal_sum + i[len(arr) - counter - 1]
        counter = counter + 1
    # https://www.w3schools.com/Python/ref_func_abs.asp
    return (abs(left_diagonal_sum - right_diagonal_sum))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

