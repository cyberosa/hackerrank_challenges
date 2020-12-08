#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr, n):
    arr.sort()
    min_unfair = 100000000000
    # take groups of k elements while updating min_unfair
    i = 0
    while i+k-1 < n:
        min_value = arr[i]
        max_value = arr[i+k-1]
        new_unfair = max_value - min_value
        if new_unfair == 0:
            return 0
        if new_unfair < min_unfair:
            min_unfair = new_unfair
        
        i += 1
    return min_unfair
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
