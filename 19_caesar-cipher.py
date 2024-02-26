#!/bin/python3
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    # Create a list with ASCII lowercase and ASCII uppercase characters
    lower = list(string.ascii_lowercase)  
    upper = list(string.ascii_uppercase) 
    # Idea behind: Divide k to 26 and use this value as k (Eliminate repited rotations).
    new_k = k%26
    # Create new lists with the alphabet rotated by k
    lower_rotated = lower[new_k:] + lower[:new_k]
    upper_rotated = upper[new_k:] + upper[:new_k]
    # For each character, print the Caesar cipher rotated character
    result = ''
    for i in s :
        if i in lower :
            result += lower_rotated[lower.index(i)]
        elif i in upper :
            result += upper_rotated[upper.index(i)]
        else :
            result += i
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()





