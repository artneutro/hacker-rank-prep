#!/bin/python3
# https://www.hackerrank.com/challenges/balanced-brackets/problem

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{' :
            stack.append(i)
        elif i == ')' and len(stack) != 0 :
            if stack[-1] == '(' :
                stack = stack[:-1]
            else :
                return 'NO'
        elif i == ']' and len(stack) != 0 :
            if stack[-1] == '[' :
                stack = stack[:-1]
            else :
                return 'NO'
        elif i == '}' and len(stack) != 0 :
            if stack[-1] == '{' :
                stack = stack[:-1]
            else :
                return 'NO'
        else :
            return 'NO'
    if len(stack) == 0 :
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

