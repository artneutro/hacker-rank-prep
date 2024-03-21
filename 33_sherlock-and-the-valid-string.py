#!/bin/python3
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    if len(s) == 1 or len(s) == 2 :
        return 'YES'
    # Convert string into list for best management
    list_s = list(s)
    # Get unique values from string
    values_unique = list(set(list_s))
    counter = []
    # Get the number of times they appear on the string
    for i in values_unique :
        counter.append(s.count(i))
    # Check if the values are all the same, except 1 which must be 1 or the other value [+-]1
    key1 = 0
    key2 = 0
    delta1 = 0
    delta2 = 0
    for i in counter : 
        # Initialization
        if key1 == 0 :
            key1 = i
            delta1 = 1
        elif key2 == 0 and i != key1:
            key2 = i
            delta2 = 1
            # Can only be 1 or [+-]1
            if key2 != key1+1 and key2 != key1-1 and key1 != 1 and key2 != 1 :
                return 'NO'
        else :
            # If a third value exists, then 'NO'
            if i != key1 and i != key2 :
                return 'NO'
            elif i == key1 :
                delta1 += 1
            elif i == key2 :
                delta2 += 1
    # Equalize values for better management
    if key1 > key2 :
        key1 = key1-1
    else :
        key2 = key2-1
    # Final check
    if (delta1 == 1 and (key1 == key2 or key1 == 1))  :
        return 'YES'
    elif  (delta2 == 1 and (key2 == key1 or key2 == 1))  :
        return 'YES'
    else :
        return 'NO'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

