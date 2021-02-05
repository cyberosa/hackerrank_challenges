#!/bin/python3

import math
import os
import random
import re
import sys

def compute_items(ipd, day, days_count):
    return ipd[day] * (days_count // day)

# with the current dictionary of days
# we need to check if we achieve the goal production
# by counting how many items have been produced
# before reaching the next machine activation
def achieved_goal(ipd, days_count, goal, next_activation):
    active_machines = list(ipd.keys())
    # production per day capacity of the active machines
    ppd = 0.0
    for day in active_machines:
        ppd += float(ipd[day] / day)
        
    # edge case: we reached the last element of the array
    # which this production capacity we can compute the needed days
    if next_activation == -1:
        if goal % ppd == 0 or goal % ppd < 0.000001:
            return goal, int(goal // ppd)
        return goal, math.ceil(goal/ppd)
    
    # with this production per day capacity, 
    # how many days do we need to reach the goal
    # before the next activation if possible?
    needed_days = int(goal // ppd)
    print("needed days {} and next_activation {}".format(needed_days,next_activation))
    if needed_days < next_activation: # we dont need to wait for another machine
        # goal reached before finishing the array
        return goal, needed_days
    
    # take the lastest active machine, the highest day we need to wait
    highest_day = active_machines[-1]
    # production reached that day
    items = int(ppd*highest_day)
    return items, highest_day 

# Complete the minTime function below.
def minTime(machines, goal):

    total_nr_machines = len(machines)
    # edge case
    if total_nr_machines == 1:
        return goal * machines[0]
    
    machines.sort()
    ipd = dict() # items per day
    # initial count
    days_count = machines[0]
    items = 1
    # edge case
    if items == goal: 
        return days_count
    
    # traverse machines and compute items per each register day
    for i in range(total_nr_machines):
        day = machines[i]
        if i == total_nr_machines-1:
            # we reached the last element of the array 
            # and the goal was not achieved
            next_act_day = -1
        else:
            next_act_day = machines[i+1]
        
        if day in ipd.keys():
            ipd[day] += 1
        else:
            ipd[day] = 1
        print(ipd)
        if next_act_day == day:
            continue
        
        items, days_count = achieved_goal(ipd, days_count, goal, next_act_day)
        #print("items {}, days_count {}".format(items, days_count))
        if items == goal:
            return days_count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
