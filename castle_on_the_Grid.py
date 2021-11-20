#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(n, grid, startX, startY, goalX, goalY):
    # initial point (startX, startY)
    # final point (goalX, goalY)
    rows = cols = n
    if startX == goalX and startY == goalY:
        return 0 # already arrived
    # increase row, decrease row, increase col, decrease col
    moves = ((1,0),(-1,0), (0,1), (0,-1))
    visited = {(startX, startY)} # coordinates on the grid
    # coordinates, movements
    queue = [[startX, startY, 0]]
    while len(queue)>0:
        path, queue = queue[0], queue[1:] # if there is only 1 element next queue is empty
        row, col, val = path
        for move in moves:
            # try different strategies to reach the goal
            nrow, ncol = row, col
            while True:
                nrow, ncol = nrow+move[0], ncol+move[1]
                if nrow>=0 and ncol>=0 and nrow<rows and ncol<cols and grid[nrow][ncol]== '.':
                    if (nrow, ncol) == (goalX, goalY):
                        return val+1
                    elif (nrow, ncol) not in visited:
                        visited.add((nrow, ncol))
                        queue.append([nrow, ncol, val+1])
                else:
                    break # due to end of row/col or block
    return 0

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(n, grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
