#!/bin/python3
# https://www.hackerrank.com/challenges/lonely-integer/problem

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    elements = []
    for i in a :
        if i in elements :
            # https://www.w3schools.com/python/python_lists_remove.asp
            elements.remove(i)
        else :
            # https://www.w3schools.com/python/python_lists_add.asp
            elements.append(i)
    return elements[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()









