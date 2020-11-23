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
    print(c[:first])
    # take the needed last elements of c and compute initial cost
    cost = sum(c[-first:])
    purchased = dict()
    for i in range(first):
        purchased[i] = 1
    print(purchased)
    # more purchases?
    if n > k:
        # at least 1 extra iteration for n-k customers
        # compute new purchases
        customer = 0
        for i in range(n-k):
            if customer == k: # reset index
                customer = 0
            print("i {}".format(i))
            print("customer {}".format(customer))
            cost = cost + (purchased[customer] + 1)*c[i]
            purchased[customer] += 1
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
