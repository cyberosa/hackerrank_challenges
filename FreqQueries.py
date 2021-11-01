import os
import re
from collections import defaultdict


def check_frequencies(n, list_commands):
    stack_v = defaultdict(int) # key = number value = freq
    stack_f = defaultdict(int) # key = frequency value = count
    for i in range(n):
        c = int(list_commands[i][0])
        v = int(list_commands[i][1])
        if c == 1: # insert
            stack_f[stack_v[v]] -= 1 # previous value updated
            stack_v[v]+=1
            stack_f[stack_v[v]] += 1

        elif c == 2: # delete occurrence
            if v in stack_v.keys():
                stack_f[stack_v[v]] -= 1 # previous value updated
                stack_v[v]-=1
                stack_f[stack_v[v]] += 1
            stack_v[v] = 0 if stack_v[v] < 0 else stack_v[v]
        else:
            print('1' if v in stack_f and stack_f[v] > 0  else '0')

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    commands = []

    for _ in range(n):
        commands.append(list(map(int, input().rstrip().split())))
    
    check_frequencies(n,commands)
