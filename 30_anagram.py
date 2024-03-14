#!/bin/python3
# https://www.hackerrank.com/challenges/anagram/problem

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    print(s)
    if len(s)%2==0 :
        # The size is pair, we can proceed
        mid = int(len(s)/2)
        # Split the string
        s1 = sorted(s[:mid])
        s2 = sorted(s[mid:])
        # For each repeated character, removes it
        for i in s1 :
            if i in s2 :
                s2.remove(i)
        # Return the size of values not in the other
        return len(s2)
    else :
        # The size is odd, not possible to proceed
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

