#!/bin/python3

import math
import os
import random
import re
import sys

def mergeSort(arr, size):
    swaps_count = c_l = c_r = 0
    if size > 1:
        middle_index = size//2
        left = arr[:middle_index]
        len_left = middle_index
        right = arr[middle_index:]
        len_right = size - middle_index
        # sort the left part
        c_l = mergeSort(left, len_left)
        # sort the right part
        c_r = mergeSort(right, len_right)
    
        # merge
        # left and right should be in order
        l = r = m = 0
        # l + r should always be m
        # we can override arr because we have the elements in left and right
        
        while l < len_left and r < len_right:
            if left[l] <= right[r]:
                arr[m] = left[l]
                l += 1
            else:
                arr[m] = right[r]
                # len(left) - m is the jump size
                # but we need to adjust it with the current index in r
                # in the right array 
                swaps_count += r + (len_left - m)
                r += 1

            m += 1
        # extra elements in left to collect?
        # any left positions increases the swap counter
        while l < len_left:
            arr[m] = left[l]
            l += 1
            m += 1

        # extra elements in right to collect?
        while r < len_right:
            arr[m] = right[r]
            r += 1
            m += 1
    #print(arr)
    #print("swaps count.{}".format(swaps_count))
    #print("c_l.{}".format(c_l))
    #print("c_r.{}".format(c_r))
    return(swaps_count + c_l + c_r)

# Complete the countInversions function below.
def countInversions(arr, n):
    return mergeSort(arr, n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr, n)

        fptr.write(str(result) + '\n')

    fptr.close()



