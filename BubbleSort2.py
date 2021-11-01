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

def swap(a, pos1, pos2):
	tmp = a[pos2]
	a[pos2] = a[pos1]
	a[pos1] = tmp


#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(n, a):
	total_swaps = 0
	# best case traverse the array only once O(n)
	if issorted(a):
		return total_swaps

	for i in range(n):
		for j in range(n - 1):
			if a[j] > a[j + 1]:
				total_swaps += 1
				swap(a, j, j + 1)
	return total_swaps


if __name__ == '__main__':
	n = int(input().strip())

	a = list(map(int, input().rstrip().split()))

	total = countSwaps(n, a)
	print(f"Array is sorted in {total} swaps.")
	print(f"First Element: {a[0]}")
	print(f"Last Element: {a[n - 1]}")
