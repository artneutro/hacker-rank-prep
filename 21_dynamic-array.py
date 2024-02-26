#!/bin/python3
# https://www.hackerrank.com/challenges/dynamic-array/problem

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    # Initialize the variables 
    result = []
    arr = [[] for x in range(n)]
    last_answer = 0
    # Perform the dynamic array filling based on the formulas provided
    for i in queries :
        if i[0] == 1 :
            idx = (int(i[1])^last_answer)%n
            arr[idx].append(i[2])
        else :
            idx = (int(i[1])^last_answer)%n
            last_answer = arr[idx][int(i[2])%len(arr[idx])]
            result.append(last_answer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



