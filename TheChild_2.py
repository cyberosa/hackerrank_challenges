#!/bin/python3
import os

def lcs(i, j, s1, s2, len_mat):
    #print("{},{}".format(i,j))
    if i == 0 or j == 0:
        return 0
    # always adapt the index to the string
    # s indexes are from 0 to n-1
    if s1[i-1] == s2[j-1]:
        # the common char attached to the computed length
        return (len_mat[i-1][j-1] + 1)  
    else: # no match, check previous matches
        left = len_mat[i][j-1]
        right = len_mat[i-1][j]
        return max(left,right)
    

def the_child(s1,s2):
    # we need a (n+1)x(n+1) matrix where we will store the length of the common
    # sequence found at that position
    # following the algorithm described here:
    # https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    max_length = 0
    n = len(s1)
    len_mat = [[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            len_mat[i][j] = lcs(i, j, s1, s2, len_mat)
            if len_mat[i][j] > max_length:
                max_length = len_mat[i][j]
            #print(max_length)
    return max_length



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()
    result = the_child(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

