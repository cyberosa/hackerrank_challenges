#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(n, h):
	max_area = 0
	h.sort()
	for i, b in enumerate(h):
		new_area = (n - i) * b
		if new_area > max_area:
			max_area = new_area
		else:
			break

	return max_area


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	h = list(map(int, input().rstrip().split()))

	result = largestRectangle(n, h)

	fptr.write(str(result) + '\n')

	fptr.close()
