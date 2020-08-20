#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import functools 

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    nr_anagrams = 0
    # list of characters, including repetitions
    list_chars = list(s)
    n = len(list_chars)
    # extreme case: all are different characters
    if n == len(set(list_chars)):
        return 0
    # length counter for anagrammatics
    min_length = 1
    max_length = n - 1
    length = min_length
    while (length <= max_length):
        groups = [list_chars[i:i+length] for i in range(0, n) if (n-i >= length)]
        #groups = [list_chars[i:i+length] for i in range(0, n)]
        #print(groups)
        for i, g in enumerate(groups): 
            if i < (len(groups)-1):
                for other_g in groups[i+1:]:
                    s1 = set(g)
                    s2 = set(other_g)
                    if len(s1) != len(s2):
                        continue
                    g.sort()
                    other_g.sort()
                    if g ==other_g:
                        nr_anagrams +=1
                        #print(nr_anagrams)
        length +=1
    return nr_anagrams

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
