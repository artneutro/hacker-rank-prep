#!/bin/python3
# https://www.hackerrank.com/challenges/flipping-the-matrix/problem

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    maximal = 0
    for i in range(int(len(matrix[0])/2)) :
        for j in range(int(len(matrix[0])/2)) :
            maximal += max(matrix[i][j], matrix[i][len(matrix[0])-j-1], matrix[len(matrix[0])-i-1][j], matrix[len(matrix[0])-i-1][len(matrix[0])-j-1])
    return maximal
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()


