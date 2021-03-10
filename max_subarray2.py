# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import math
import sys
import re
import random 

def max_subarray(a, m, n):
    # edge cases
    # n = 2
    
    # max sum that we can have for a value m 
    # (if 0 is not a value for a[i])
    # is m-1. Thus if we ever reach this sum
    # we can stop traversing the array
    theo_max = m - 1
    max_sum = 0
    # traverse the array, reusing previous sum
    array_of_sums = []
    for i in range(n):
        prev_sum = a[i]
        max_sum = max(prev_sum % m, max_sum)
        if max_sum == theo_max:
            return theo_max

        if i == 0:
            # combine with the rest of the array
            for j in range(i+1,n):
                prev_sum = prev_sum + a[j]
                array_of_sums.append(prev_sum)
                max_sum = max(prev_sum % m, max_sum)
                if max_sum == theo_max:
                    return theo_max
        else:
            # use array_of_sums
            # length of array_of_sums is n - i
            # start traversing from element j = 1
            array_of_sums = array_of_sums[1:]
            array_of_sums = [asu-a[i-1] for asu in array_of_sums]
            for s in array_of_sums:
                max_sum = max(s % m, max_sum)
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
