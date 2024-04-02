#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    number_of_swaps = 0
    sorted_a = sorted(a)
    for i in range(len(a)) :
        for j in range(len(a)-1) :
            if (a[j] > a[j + 1]) :
                tmp = a[j]
                a[j] = a[j+1]
                a[j + 1] = tmp
                number_of_swaps += 1
            if a == sorted_a :
                print("Array is sorted in " + str(number_of_swaps) + " swaps.") 
                print("First Element:", a[0]) 
                print("Last Element:", a[-1]) 
                return

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

