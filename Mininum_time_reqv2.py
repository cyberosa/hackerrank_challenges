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
    active_machines = ipd.keys()
    production = [compute_items(ipd,day,days_count) for day in active_machines]
    #print("days_count {} and production {}".format(days_count, production))
    items = sum(production)
    if next_activation == -1:
        condition1 = True
    else:
        condition1 = days_count < next_activation
    while condition1 and items < goal:
        production = [compute_items(ipd, day, days_count) for day in active_machines]
        items = sum(production)
        #print("days_count {} and production {}".format(days_count, production))
        if items == goal: # reached
            return goal, days_count
        days_count += 1
        if next_activation != -1: 
            condition1 = days_count < next_activation
        
    # it was not found yet
    return items, days_count 

# Complete the minTime function below.
def minTime(machines, goal):

    total_nr_machines = len(machines)
    # edge case
    if total_nr_machines == 1:
        return goal * machines[0]
    
    machines.sort()
    ipd = dict() # items per day
    days_count = 1
    
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
