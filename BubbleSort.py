#!/bin/python3

import math
import os
import random
import re
import sys


def issorted(x):
    """Check if x is sorted"""
    for i in range(0,len(x)-1):
        if(x[i] > x[i+1]):
            return False
    return True

# Complete the countSwaps function below.
def countSwaps(arr, n):
    global_position = 0
    numSwaps = 0
    new_arr = arr
    while not issorted(new_arr) and global_position < n-1:
        s = list(new_arr[global_position:])
        #print(s)
        min_value = min(s)
        min_index = s.index(min_value)
        #print(min_value, min_index)
        numSwaps = numSwaps + min_index
        s.remove(min_value)
        # re-arrange the new array
        new_arr[global_position] = min_value
        new_arr[global_position+1:] = s
        global_position += 1
        #print(arr)

    print("Array is sorted in {} swaps.".format(numSwaps))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[n-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a, n)
 