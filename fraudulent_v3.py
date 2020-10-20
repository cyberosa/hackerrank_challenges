#!/bin/python3

import math
import os
import random
import re
import sys

# consider the data in the range 0 to 200
# implementing counting sort
# 1) Take a count array to store the count of each unique object.
# 2) Modify the count array such that each element at each index 
# stores the sum of previous counts. 
# The modified count array indicates the position of each object in 
# the output sequence.
# 3) Output each object from the input sequence followed by 
#  decreasing its count by 1.
def count_sort(arr, counts, d):
    output = [0 for i in range(201)]
    sorted_arr = [0 for i in range(d)]

    # cummulative counts in output
    for i in range(201):
        if i == 0:
            output[i] = counts[i]
        else:
            output[i] = output[i-1] + counts[i]
    
    # traverse the initial array and find position
    for p in range(d):
        value = arr[p]
        final_position = output[value]
        sorted_arr[final_position] = value
        # decrease position for next value
        output[value] -= 1

    return(sorted_arr)

def update_count(counts, old_value, new_value):
    # update the count by incrementing count of new element and decrementing count of old element
    counts[old_value] -= 1
    counts[new_value] += 1

    return(counts)

def compute_double_median(counts, d):
    # we can build the array just by taking the counts > 0
    window = list()
    for i in range(201):
        if counts[i] > 0:
            for rep in range(counts[i]):
                window.append(i)
    # now let's play with the middle index
    if d % 2 == 0:
        # just sum two middle values
        return (window[int(d/2)] + window[int(d/2)-1])
    
    # return the middle value multiplied by 2
    return window[math.floor(d/2)] * 2
    

# Complete the activityNotifications function below.
def activityNotifications(expenditure, n, d):
    alerts_count = 0
    window = expenditure[:d] # first window

    # in the count array we will always have the last d active elements
    count = [0 for i in range(201)]

    # compute counts
    for v in window:
        count[v] = count[v] + 1

    # we dont need to sort the window, just compute the median

    for i in range(d,n):
        d_median = compute_double_median(count, d)
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
