#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def is_sorted(l):
    if (all(l[i] <= l[i + 1] for i in range(len(l)-1))):
        return True
    return False

def swap(l, pos1, pos2):
    #print("swapping {} and {}".format(pos1, pos2))
    tmp = l[pos2]
    l[pos2] = l[pos1]
    l[pos1] = tmp
    #print(l)
    return l

def minimumSwaps(arr):
    nr_swaps = 0
    done = is_sorted(arr)
    while(not done):
        for pos, val in enumerate(arr):
            if val != (pos + 1):
                #print(pos)
                # swap to the right place
                arr = swap(arr, pos, val-1)
                nr_swaps += 1
            done = is_sorted(arr)
            if done:
                break
    return nr_swaps       
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
