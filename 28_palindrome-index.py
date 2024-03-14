#!/bin/python3
# https://www.hackerrank.com/challenges/palindrome-index/problem

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def is_palindrome(s):
    # This functions receives a string s of size n, with n%2==0
    # and check if it is palindrome
    mid = int(len(s)/2)
    if s[:mid] == (s[mid:])[::-1] :
        return True
    else :
        return False

def palindromeIndex(s):
    # Write your code here
    # If size is 0, 1 or 2
    if len(s) == 0 or len(s) == 1 or len(s) == 2 :
        return -1
    # If it is already a palindrome
    if len(s)%2 == 0 :
        # The string is already pair size
        if is_palindrome(s) :
            return -1
    else :
        # The string is odd size
        mid = int((len(s)-1)/2)
        new_s = s[:mid] + s[mid+1:]
        if is_palindrome(new_s) :
            return -1
    for i in range(len(s)) :
        new_s = s[:i] + s[i+1:]
        if len(new_s)%2 == 0 :
            # The string is already pair size
            if is_palindrome(new_s) :
                return i
        else :
            # The string is odd size
            mid = int((len(s)-1)/2)
            new_s_subset = new_s[:mid] + new_s[mid+1:]
            if is_palindrome(new_s_subset) :
                return i
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

