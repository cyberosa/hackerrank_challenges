#!/bin/python3

import math
import os
import random
import re
import sys

# check if we the machines we have so far
# we are able to reach the goal.
# if not found return -1
# otherwise return the number of days
def achieved_goal(total_ipd, goal):
    # if the goal is divisible by the total_ipd, we found the perfect solution
    # otherwise we go for an extra day, i.e. if the division is 7.3, then
    # we need 8 days
    print(goal % total_ipd)
    if goal % total_ipd == 0 or goal % total_ipd < 0.000001:
        return int(goal // total_ipd)
    
    return math.ceil(goal/total_ipd)

# Complete the minTime function below.
def minTime(machines, goal):
    machines.sort()
    ipd = dict() # items per day
    # in parallel we traverse the dictionary 
    # computing the total nr of items per day
    # that we can achieve
    total_ipd = 0.0
    # traverse machines and compute items per each register day
    for day in machines:
        if day in ipd.keys():
            ipd[day] += 1
        else:
            ipd[day] = 1
        print(ipd)
        
        total_ipd += float(ipd[day] / day)
        print("total_ipd {}".format(total_ipd))
        needed = achieved_goal(total_ipd, goal)
        print("needed_days {}".format(needed))
    
    return needed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
