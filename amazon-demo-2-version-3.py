#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#

def numberOfItems(s, startIndices, endIndices):
    # Write your code here
    # Initialize variables
    cur_start = 0
    cur_end = 0
    count_asterisk = 0
    result_arr = []
    # For each start and end
    for i in range(len(startIndices)) :
        cur_start = startIndices[i]-1
        cur_end = endIndices[i]
        # If there is at least 2 pipes to get a compartment and number of asterisk is > 0
        if s[cur_start:cur_end].count('|') > 1 and s[cur_start:cur_end].count('*') > 0:
            # Get the substring from start to end, search for the first and last pipes and count the asterisks in between
            sub_str = s[cur_start:cur_end]
            first_pipe = sub_str.index('|')
            last_pipe = sub_str.rindex('|')
            count_asterisk = sub_str[first_pipe:last_pipe].count('*')
        # Append the new result and reset the counts
        result_arr.append(count_asterisk)
        count_asterisk = 0
    return result_arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    startIndices_count = int(input().strip())

    startIndices = []

    for _ in range(startIndices_count):
        startIndices_item = int(input().strip())
        startIndices.append(startIndices_item)

    endIndices_count = int(input().strip())

    endIndices = []

    for _ in range(endIndices_count):
        endIndices_item = int(input().strip())
        endIndices.append(endIndices_item)

    result = numberOfItems(s, startIndices, endIndices)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

