# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import math
import sys
import re
import bisect
from collections import defaultdict 

def get_sum(pi, pj, m):
    return (pi - pj + m) % m

def insert_and_closest(values, v):
    #print("before {}".format(values))
    l = len(values)
    if l == 0:
        values.append(v)
        return values, 0
    i = 0 
    while i < l:
        if values[i] > v:
            break
        i += 1
    new_values = values[:i]
    new_values.append(v)
    if i < l:
        new_values.extend(values[i:])
        return new_values, values[i]
    #print("after {}".format(new_values))    
    return new_values, values[i-1]

def max_subarray(a, m, n):
    # max sum that we can have for a value m 
    # (if 0 is not a value for a[i])
    # is m-1. Thus if we ever reach this sum
    # we can stop traversing the array
    theo_max = m - 1
    max_sum = 0
    # keep the previous seen values in ordered
    prev_values = []
    # compute the prefix as a balanced tree
    prefix = defaultdict()
    curr = 0; 
    # this operation takes O(n)
    for i in range(n): 
        curr = int((a[i] % m + curr)%m) 
        # update the value
        prefix[i] = curr
        # find the smallest and closest to curr
        # previously seen
        prev_values, pj = insert_and_closest(prev_values, curr)
        #print("closest to {} is {}".format(prefix[i],pj))
        new_sum = get_sum(prefix[i], pj, m)
        #print("new sum = {}".format(new_sum))
        max_sum = max(max_sum, prefix[i], new_sum)
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
