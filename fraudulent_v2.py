#!/bin/python3

import math
import os
import random
import re
import sys
import statistics 
# Python3 program to insert  
# an element into sorted list 
import bisect  
  
def insert(l, n): 
    bisect.insort(l, n)  
    return l

def compute_median(values):
   
    #print(values)
    total_length = len(values)
    if total_length % 2 == 0:
        # take the two middle values and compute the mean
        value1 = values[int(total_length/2) - 1]
        value2 = values[int(total_length/2)]
        return (value1+value2)/2
    else:
        # return the middle value
        return values[math.floor(total_length/2)]

# Complete the activityNotifications function below.
def activityNotifications(expenditure, n, d):
    alerts_count = 0
    window = expenditure[:d] # first window
    window = sorted(window)
    for i in range(d,n):
        if len(window) == d:
            #median = compute_median(window)
            median = statistics.median(sorted(window))
            #print(median)
            #print(expenditure[i])
            if expenditure[i] >= median*2:
                alerts_count += 1
            # remove first element of the window
            window.pop(0)
            # add new last element in the window but in the right place
            window = insert(window, expenditure[i])
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
