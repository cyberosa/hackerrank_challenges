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


def poisonousPlants(n, p):
    # we cannot sort the array because the order is key to delete or not
    if n == 1:
        return 1 # no plants dying

    max_days = 0
    stack=[]
    for i,plant in enumerate(p):
        days = 1

        while stack and stack[-1][0] >= plant:
            _, d = stack.pop()
            days = max(days, d + 1)
        
        if not stack:
            days = 0
        
        max_days = max(max_days, days)
        stack.append((plant, days))
    return max_days

'''
def poisonousPlants(plants):
    stack = []
    maxDays = -math.inf

    for plant in plants:
        days = 1

        while stack and stack[-1][0] >= plant:
            _, d = stack.pop()
            days = max(days, d + 1)
        
        if not stack:
            days = 0
        
        maxDays = max(maxDays, days)
        stack.append((plant, days))
    
    return maxDays'''
        
        
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
