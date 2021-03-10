# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import math
import sys
import re
import bisect

    
def max_subarray(a, m, n):
    max_sum,prefix=0,0
    # sorted array of prev prefix values
    a1=[]
    for value in a:
        prefix = (prefix+value) % m
        max_sum=max(max_sum,prefix)
        # Locate the insertion point for prefix+1 in a1 to maintain sorted order. 
        ind=bisect.bisect_left(a1,prefix+1)
        if(ind<len(a1)): # the closest value to prefix was found
            max_sum=max(max_sum,prefix-a1[ind]+m)
        # no closest value
        #  inserting prefix in a1 after any existing entries of prefix.
        bisect.insort(a1,prefix)
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
