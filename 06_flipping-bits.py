#!/bin/python3
# https://www.hackerrank.com/challenges/flipping-bits/problem

import math
import os
import random
import re
import sys
from ctypes import c_int32

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    # https://docs.python.org/3/library/functions.html#bin
    binary_str = bin(n)[2:]
    # https://www.w3schools.com/python/ref_string_zfill.asp
    binary_32_bit = binary_str.zfill(32)
    reverse_binary_32_bit = ''
    for i in binary_32_bit :
        if i == '0' :
            reverse_binary_32_bit = reverse_binary_32_bit + '1'
        else :
            reverse_binary_32_bit = reverse_binary_32_bit + '0'
    # https://docs.python.org/3/library/functions.html#int
    return int(reverse_binary_32_bit, 2)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

