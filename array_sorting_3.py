#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def swap(l, pos1, pos2):
    #print("swapping {} and {}".format(pos1, pos2))
    tmp = l[pos2]
    l[pos2] = l[pos1]
    l[pos1] = tmp
    #print(l)

def minimumSwaps(arr):
    n = len(arr)
    nr_swaps = 0
    mod = n % 2
    for i in range(int(n/2) + mod):
        # sanity check
        if(arr[i] != (i+1)):
            new_start = max(0,i)
            #print("new_start {}".format(new_start))
            current_pos1 = arr.index(i+1, new_start)
            if current_pos1 != i:
                swap(arr, i, current_pos1)
                nr_swaps += 1
        # sanity check
        if(arr[n-1-i] != (n-i)):
            new_end = min(n-1,n-1-i)
            #print("new_end {}".format(new_end))
            current_pos2 = arr.index(n-i, 0, new_end)
            if current_pos2 != (n-1-i):
                swap(arr, n-1-i, current_pos2)
                nr_swaps += 1
    return nr_swaps       
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
