#!/bin/python3
# https://www.hackerrank.com/challenges/new-year-chaos/problem

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    for i in range(len(q)) :
        if q[i] > i+3 :
            print('Too chaotic')
            return 0
            # Optimized solution in progress
        #elif i >= q[i] :
            #bribes += i+1-q[i]
        else :
            j = i
            while j >= 0 :
                if q[j] > q[i] :
                    bribes += 1
                j = j-1
    print(bribes)
    return 0

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

