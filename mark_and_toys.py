#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(n, prices, k):
    sort_p = sorted(prices)
    spent = 0
    items = 0
    for i in range(n):
        if (spent + sort_p[i]) <= k:
            items += 1
            spent = spent + sort_p[i]
    return items

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(n, prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
