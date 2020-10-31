#!/bin/python3

 

import math

import os

import random

import re

import sys

 

def count_freq(s):

    dict_s = dict()

    for c in s:

        if c in dict_s.keys():

            dict_s[c] += 1

        else:

            dict_s[c] = 1

 

    return(dict_s)

 

# Complete the makeAnagram function below.

def makeAnagram(a, b):

    dict_a = count_freq(a)

    dict_b = count_freq(b)

    extra_count = 0

    # list of unique chars in a

    keys_a = list(dict_a.keys())

    # list of unique chars in b

    keys_b = list(dict_b.keys())

    

    for c in keys_a:

        #print(c)

        if c in keys_b:

            # check frequency

            if dict_a[c] != dict_b[c]:

                # we need to remove the extra characters

                extra_count += abs(dict_a[c] - dict_b[c])

            #print("removing {}".format(c))

            keys_b.remove(c)

        else:

            #print("increasing by {}".format(dict_a[c]))

            extra_count += dict_a[c]

 

    # remaining chars are not in a, otherwise were removed

    for c in keys_b:

        #print(c)

        #print("increasing by {}".format(dict_b[c]))

        extra_count += dict_b[c]

    

    print(extra_count)

    return(extra_count)

 

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

 

    a = input()

 

    b = input()

 

    res = makeAnagram(a, b)

 

    fptr.write(str(res) + '\n')

 

    fptr.close()

 

