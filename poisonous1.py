#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#
def update_queues(p):
    dying = False
    # traverse all plants in p
    # start from the end of the array
    m = len(p)
    last = p[m-1] # last element of the array
    m = m-2 # next position
    new_p = []
    while m >=0:
        if last <= p[m]:
            new_p.append(last)
        else: # last > p[m] --> die
            dying = True
        last = p[m]
        m -= 1
    # always add the first element
    new_p.append(p[0])
    # plants who survided in new_p
    return new_p[::-1], dying

def poisonousPlants(n, p):
    # we cannot sort the array because the order is key to delete or not
    if n == 1:
        return 1 # no plants dying

    dying = True # flag to update in every iteration
    days = 0
    while dying:
        #print(p)
        p, dying = update_queues(p)
        #print(f"dying {dying}")
        #print(p)
        if dying:
            days += 1
    return days
        
        
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
