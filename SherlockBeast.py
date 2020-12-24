#!/bin/python3

import math
import os
import random
import re
import sys

def is_divisible_by_three(n):
    return n % 3 == 0

def is_divisible_by_five(n):
    return n % 5 == 0


# this method check if it is possible to 
# find a number of lengths n-t, t
# where n-t is the number of fives
# and t is the number of threes
def check_len_three(t, n):
    # then we need to check if the other substring is divisible by 3
    if is_divisible_by_three(n-t):
        #print("printing {} fives and {} threes".format(n-t,t))
        s3 = []
        s1 = "5"*(n-t)
        s2 = "3"*t
        s3.append(s1)
        s3.append(s2)
        print("".join(s3))
        return True

    return False
      
# Return -1 if the length is not valid
# or the combination of 5's and 3's that match the requirements
def find_valid_sublengths(n):
    if n < 5:
        print('-1')
        return
    # we want to minimize the smallest substring of 3's
    # so we need to iterate til we find the first valid combination
    # we can build
    t = 5
    while t < n:
        result = check_len_three(t, n)
        if result:
            return
        t += 5
    print('-1')
    return

# Complete the decentNumber function below.
def decentNumber(n):
    # n is the length of the number and must be 
    # divisible by 3, then complete with 5 values
    if is_divisible_by_three(n):
        #print("printing only fives")
        print(n*'5')
        return
    
    # special cases where it is not possible to pass the requirements
    # for the other substring
    if n== 5 or n == 10:
        #print("printing only threes")
        print(n*'3')
        return
       
    # or a combination of two divisors of 3 and 5
    find_valid_sublengths(n)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
