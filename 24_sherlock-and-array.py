#!/bin/python3
# https://www.hackerrank.com/challenges/sherlock-and-array/problem
import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    # Optimization to avoid the comparison of sum(arr[:i]) and sum(arr[i+1:])
    sum_arr = []
    total_arr = sum(arr)
    if len(arr) == 1 :
        return 'YES'
    for i in range(0,len(arr)-1) :
        if i == 0 :
            sum_arr = 0
            total_arr -= arr[i]
        else :
            sum_arr += arr[i-1]
            total_arr -= arr[i]
        if sum_arr == total_arr :
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()









