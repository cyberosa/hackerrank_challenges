#!/bin/python3

#Given an array of integers, find the minimum absolute difference between any two elements in the array.

import math

import os

import random

import re

import sys

 

# Complete the minimumAbsoluteDifference function below.

def minimumAbsoluteDifference(arr, n):

    # edge case n = 2

    if n == 2:

        return abs(arr[0]-arr[1])

    

    # order array, ignoring signs but keeping record of them

    arr.sort()

    #print(arr)

    min_dif = 1000000

 

    for i in range(1,n):

        prev = arr[i-1]

        num = arr[i]

        # Check if we have zero

        if num == 0:

            new_dif = abs(prev)

        elif prev == 0:

            # we can return the result

            return min(min_dif, abs(num))

        else:

            new_dif = abs(prev - num)

        if new_dif < min_dif:

            min_dif = new_dif

    return min_dif

 

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

 

    n = int(input())

 

    arr = list(map(int, input().rstrip().split()))

 

    result = minimumAbsoluteDifference(arr, n)

 

    fptr.write(str(result) + '\n')

 

    fptr.close()