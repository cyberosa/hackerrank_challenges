#!/bin/python3

import math
import os
import random
import re
import sys

# check if all characters in s are equal to ref
def equal(ref, s):
    i = 0
    while i < len(s):
        if s[i] != ref:
            return False
        i +=1
    return True     

def check_palindrome(s):
    #print("check palindrome")
    #print(s)
    len_s = len(s)
    if len_s == 1: return False
    if len_s == 2:
        return(s[0] == s[1])
    if len_s == 3:
        return(s[0] == s[2])
                
    if len_s % 2 == 0: # even
        # if len_s = 4, edge = 2
        edge = int(len_s / 2)
    else: # odd
        # if len_s = 5, edge = 2
        edge = int(len_s // 2)
    
    # check left part of the string
    left_s = s[1:edge]
    
    result = equal(s[0], left_s)
    if result==False: return False
    # check right part of the string
    if len_s % 2:
        right_s = s[edge:len_s]
    else:
        right_s = s[edge+1:len_s]
    
    return(equal(s[0], right_s))

def update_counter(counter, s):
    len_s = len(s)
    # edge cases
    if len_s == 1: return counter # no update
    if len_s == 2:
        if s[0] == s[1]:
            counter+=1
        return counter
    
    # build all substrings and check if they are palindrome
    end = len_s # last position
    while end >0:
        substring = s[0:end]
        result = check_palindrome(substring)
        #print(result)
        if result:
            counter+=1
        end = end - 1
    return counter

# Complete the substrCount function below.
def substrCount(n, s):
    if n == 1: return 1
    counter = n
    i = 0
    # skip last two characters
    while i < n:
        # check all combinations starting in that position
        #print(s[i:n])
        counter = update_counter(counter, s[i:n])
        #print(list_palin)
        i += 1

    return(counter)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
