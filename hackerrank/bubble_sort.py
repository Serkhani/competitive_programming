#!/bin/python3

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
    swapCount = 0
    for j in range(len(a)-1):
        noSwap = True
        for i in range(1,len(a)-j):
            if a[i-1]>a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                swapCount += 1
                noSwap = False
        if noSwap:
            break
    return print(f"Array is sorted in {swapCount} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}")
  

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
