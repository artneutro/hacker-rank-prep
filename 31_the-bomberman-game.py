#!/bin/python3
# https://www.hackerrank.com/challenges/bomber-man/problem

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def next_grid (new_grid):
    # Function to generate the next grid after 2 seconds (after explosions)
    for i in range(len(new_grid)) :
        for j in range(len(new_grid[0])) :
            # Convert all 'O' and neighbours (not O) to a temporal value
            if new_grid[i][j] == 'O' :
                new_grid[i][j] = 't'
                if i != 0 and new_grid [i-1][j] != 'O' :
                    new_grid [i-1][j] = 't'
                if i != len(new_grid)-1 and new_grid [i+1][j] != 'O' :
                    new_grid [i+1][j] = 't'
                if j != 0 and new_grid [i][j-1] != 'O' :
                    new_grid [i][j-1] = 't'
                if j != len(new_grid[0])-1  and new_grid [i][j+1] != 'O' :
                    new_grid [i][j+1] = 't'
    for i in range(len(new_grid)) :
        for j in range(len(new_grid[0])) :
            # Convert all temporal values to '.' and all '.' to 'O'
            if new_grid[i][j] == '.' :
                new_grid[i][j] = 'O'
            elif new_grid[i][j] == 't' :
                new_grid[i][j] = '.'
    return new_grid
        

def bomberMan(n, grid):
    # Write your code here
    print(grid)
    new_grid = []
    # Convert the strings into list for better manipulation
    for i in grid :
        new_grid.append(list(i))
        
    final_grid = []
    
    if n == 1 : 
        # If n==1, it returns the same state
        return grid
    elif n%2 == 0 :
        # If n%2==0, it means all are O
        for i in range(len(new_grid)) :
            for j in range(len(new_grid[0])) :
                new_grid[i][j] = 'O'
        final_grid = new_grid
    elif n%4 == 3 :
        # If n%4==3, it returns the possible state 1
        final_grid = next_grid(new_grid)
    elif n%4 == 1 :
        # If n%4==1, it returns the possible state 2
        grid_3 = next_grid(new_grid)
        final_grid = next_grid(grid_3)
        
    # Convert the internal lists to strings again
    for i in range(len(final_grid)) :
        grid[i] = ''.join(final_grid[i])
        
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

