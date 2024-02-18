#!/bin/python3
# https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zer = 0
    for i in arr :
        if i > 0 :
            pos = pos+1
        elif i < 0 :
            neg = neg+1
        else :
            zer = zer+1
    # https://stackoverflow.com/questions/15619096/add-zeros-to-a-float-after-the-decimal-point-in-python
    print(format(pos/len(arr), '.6f'))
    print(format(neg/len(arr), '.6f'))
    print(format(zer/len(arr), '.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
    
