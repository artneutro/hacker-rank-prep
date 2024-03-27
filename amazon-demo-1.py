#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimalHeaviestSetA(arr):
    # Write your code here
    # Optimized to check up to half elements in the worst case
    sum_arr = sum(arr)
    # Sort the elements
    sorted_arr = sorted(arr)
    # Start in the last element
    pointer = len(arr)-1
    # Go through the array until the sum of maximal elements are higher than the half of the sum of all
    while (pointer >= 0) :
        if sum(sorted_arr[pointer:]) > int(sum_arr/2) :
            return sorted_arr[pointer:]
        pointer -= 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minimalHeaviestSetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

