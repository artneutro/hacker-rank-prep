#!/bin/python3
# https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    print(str(sum(arr)-max(arr)) + " " + str(sum(arr)-min(arr)))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
