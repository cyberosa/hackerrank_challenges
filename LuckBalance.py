#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests, n):
    important_c = []
    non_important_c = []
    # split the contests between important and not important
    # into two separate arrays
    for i in range(n):
        contest = contests[i]
        if contest[1] == 1:
            # important
            important_c.append(contest[0])
        else:
            non_important_c.append(contest[0])
    
    # check the length of important_c array len_ic
    len_ic = len(important_c)
    pos_sum = sum(non_important_c)
    if len_ic > k: # I cannot lose all important contests
        # sort the important_c array staring with the smallest value
        important_c.sort()
        # take the first (len_ic - k) elements and sum the value neg_sum
        neg_sum = sum(important_c[:len_ic-k])
        # take the rest elements and sum the value pos_sum
        pos_sum = pos_sum + sum(important_c[len_ic-k:])
        return pos_sum - neg_sum

    # we can loose all
    return(pos_sum + sum(important_c))     


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests, n)

    fptr.write(str(result) + '\n')

    fptr.close()
