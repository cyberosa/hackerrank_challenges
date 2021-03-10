# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import math
import sys
import re
import random
from collections import defaultdict 

def update_max_mod(mods, max_sum, m, theo_max):
    prev_sum = 0
    n = len(mods)
    for i in range(n):
        prev_sum += mods[i]
        max_sum = max(max_sum, prev_sum % m)
        if max_sum == theo_max:
            return theo_max
    return max_sum

def max_subarray(a, m, n):
    # edge cases
    # n = 2
    
    # max sum that we can have for a value m 
    # (if 0 is not a value for a[i])
    # is m-1. Thus if we ever reach this sum
    # we can stop traversing the array
    theo_max = m - 1
    max_sum = 0
    # traverse the array, computing all modulo values
    mods = []
    
    for i in range(n):
        new_mod = a[i] % m
        mods.append(new_mod)
        max_sum = max(new_mod, max_sum)
        if max_sum == theo_max:
            return theo_max
        
    # try combinations in mods array
    for i in range(len(mods)):
        max_sum = update_max_mod(mods[i:], max_sum, m, theo_max)
        if max_sum == theo_max:
            return theo_max
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = max_subarray(a, m, n)

        fptr.write(str(result) + '\n')

    fptr.close()
