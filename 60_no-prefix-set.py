#!/bin/python3
# https://www.hackerrank.com/challenges/no-prefix-set/problem

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    if len(words) <= 1 :
        print('GOOD SET')
        return
    else :
        curr = 1
        prev = 0
        while curr <= len(words) :
            while prev < curr :
                if (words[curr]).startswith(words[prev]) or  (words[prev]).startswith(words[curr]):
                    print('BAD SET')
                    print(words[curr])
                    return
                prev += 1
            curr += 1
            prev = 0
    print('GOOD SET')
    return
                    
                    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)

