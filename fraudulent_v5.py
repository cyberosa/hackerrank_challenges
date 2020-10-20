#!/bin/python3

import math
import os
import random
import re
import sys

def update_count(counts, old_value, new_value):
    # update the count by incrementing count of new element and decrementing count of old element
    counts[old_value] -= 1
    counts[new_value] += 1

    return(counts)

def compute_double_median(counts, goal_index, d):
    # we can build the array just by taking the counts > 0
    # we need to reach the goal index,
    # no need to build any window array
    # cummulative counts in output that gives us the current position of the value
    # warning: position starting in 1, not in 0!
    output = [0 for i in range(201)]
    for i in range(201):
        if i == 0:
            output[i] = counts[i]
        else:
            output[i] = output[i-1] + counts[i]

    if d % 2 == 0:
        # we need to find two values: goal_index and goal_index -1
        for i in range(201):
            if output[i] >= (goal_index - 1):
                first = i
                break
        # the second value is goal_index
        for i in range(201):
            if output[i] >= goal_index:
                second = i
                break

        # compute the double median
        # just sum two middle values
        return (first + second)
    else:  
        # we need to find only the middle value
        for i in range(201):            
            if output[i] >= goal_index:
                return i*2

# Complete the activityNotifications function below.
def activityNotifications(expenditure, n, d):
    alerts_count = 0

    # in the count array we will always have the last d active elements
    count = [0 for i in range(201)]

    # compute counts of the first d window
    for i in range(d):
        v = expenditure[i]
        count[v] = count[v] + 1

    # we dont need to sort the window, just compute the median
    # we need to adapt the goal_index to the range in output which starts in 1
    if d % 2 == 0:
        goal_index = int(d/2) + 1 # we also need the value of the prev element
    else:
        goal_index = math.ceil(d/2)

    #print(goal_index)
    for i in range(d,n):
        d_median = compute_double_median(count, goal_index, d)
        #print(d_median)
        #print(expenditure[i])
        if expenditure[i] >= d_median:
            alerts_count += 1
        # update count and output to get the new sorted window
        count = update_count(count, expenditure[i-d], expenditure[i])

    return(alerts_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, n, d)

    fptr.write(str(result) + '\n')

    fptr.close()
