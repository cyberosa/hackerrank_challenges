#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def middle_value(min_v, max_v):
    return (min_v + (max_v - min_v)//2)

# method to compute the production at the specific limit day
def compute_production(machines, limit, goal):
    # limit is the number of days until we need to compute
    production = 0

    for machine_day in machines:
        production += (limit // machine_day)

    return production

# Complete the minTime function below.
def minTime(machines, goal):
    machines.sort()
    nr_m = len(machines)
    
    # edge case
    if goal == 1: 
        return machines[0]
    
    # the fastest machine is the first element in machines
    # best case is all machines as fast as this one
    bc = int((goal/nr_m) * machines[0])
    #print(bc)
    # the slowest machine is the last element in machines
    # worst case is all machines as slow as this one
    wc = int((goal/nr_m) * machines[-1])
    #print(wc)
    # the solution is between [bc,wc] so we need to search 
    # within this range, but instead of starting from the bc
    # we can start in the middle and check how far we are
    # from the goal 
    l = bc
    h = wc
    while (l < h):
        mc = middle_value(l,h)
        prod_m = compute_production(machines, mc, goal)
        #print("mc {}, prod_m {}".format(mc,prod_m))
        # now check the strategy to follow depending on the current production
        if prod_m < goal: # go to the higher right
            # update the new lower end
            l = mc + 1 # next position to the already checked mc
        else: # go to the lower left
            # update the new higher end
            h = mc
    # you might have reached the solution in more than one value
    # so we keep the lower value
    return int(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
