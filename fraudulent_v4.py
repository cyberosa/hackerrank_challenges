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
    # we need to reach the middle index,
    # no need to traverse the whole window
    # it depends if the length is even or not

    window = list()
    index = 0
    for i in range(201):
        if counts[i] > 0:
            for rep in range(counts[i]):
                window.append(i)
                #print(window)

                if index == goal_index and len(window) > goal_index:
                    # compute the double median
                    if d % 2 == 0:
                        # just sum two middle values
                        return (window[goal_index] + window[goal_index-1])
                    else:
                        # return the middle value multiplied by 2
                        return window[goal_index] * 2
                index += 1
                #print(index)

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
    if d % 2 == 0:
        goal_index = int(d/2) # we also need the value of the prev element
    else:
        goal_index = math.floor(d/2)
    print(goal_index)
    for i in range(d,n):
        d_median = compute_double_median(count, goal_index)
        #print(median)
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
