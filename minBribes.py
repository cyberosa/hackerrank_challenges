#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    nr_bribes = 0
    for pos, val in enumerate(q):
        if (val-1) - pos > 2:
            return "Too chaotic"
		# check up to two previous values of the current position
        for j in range(max(0,val-2), pos):
            if q[j] > val:
                nr_bribes+=1
    return nr_bribes

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
