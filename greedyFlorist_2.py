#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c, n):
    # first purchase
    first = min(k,n)
    c.sort()
    cost = 0
    if k >= n : # more buyers than flowers, no need to increase purchase counter
        for i in range(n):
            cost += c[i]
    else:
        purchased = 0
        customer = 0
        # in reverse order
        for i in range(n-1, -1, -1):
            if customer == k: # reset index
                customer = 0
                purchased += 1
            
            cost += (purchased + 1) * c[i];
            customer += 1
    
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c, n)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
