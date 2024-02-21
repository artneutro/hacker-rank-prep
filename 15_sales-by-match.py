#!/bin/python3
# https://www.hackerrank.com/challenges/sock-merchant/problem

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    odd_socks = []
    pairs = 0
    for i in ar :
        if i in odd_socks :
            odd_socks.remove(i)
            pairs += 1
        else :
            odd_socks.append(i)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()






