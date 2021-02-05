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
# given the items per day production we have in ipd
def compute_production(machines, limit, goal, ipd):
    production = 0
    last_day = 1
    for day in machines:
        print(day)
        if day <= limit:
            production += ipd[day] * (limit // day)
            #print("production {} at day_machine {}".format(production,day))
            # last day of production was
            last_day = max(last_day,limit - (limit % day))
        else: 
            break
    return production, last_day

# Complete the minTime function below.
def minTime(all_machines, goal):
    nr_m = len(all_machines)
    # edge case
    if nr_m == 1:
        return goal * all_machines[0]
    
    count = Counter(all_machines) # machines per day
    ipd = dict(count)
    machines = list(ipd.keys())
    machines.sort()
    #print(machines)
    
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
    mc = middle_value(l,h)
    prod_m, last_prod_day = compute_production(machines, mc, goal, ipd)
    #print("mc {}, prod_m {}, last_prod_day {}".format(mc,prod_m,last_prod_day))
    # now check the strategy to follow depending on the current production
    while prod_m != goal:        
        if prod_m < goal: # go to the higher right
            # update the new lower end
            l = mc
            mc = middle_value(l,h)
        else: # go to the lower left
            # update the new higher end
            h = mc
            mc = middle_value(l,h)
    
        prod_m, last_prod_day = compute_production(machines, mc, goal, ipd)
        #print("mc {}, prod_m {}, last_prod_day {}".format(mc,prod_m,last_prod_day))

    return int(last_prod_day)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
