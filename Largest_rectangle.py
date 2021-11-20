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

	# traverse all elements in h

	for i, b in enumerate(h):

		current_h = b

		blocks = 1

		# move to the left

		left_i = i - 1

		while left_i >= 0:

			if h[left_i] >= current_h:

				blocks += 1

				left_i -= 1

			else:

				break

		# move to the right

		right_i = i + 1

		while right_i < n:

			if h[right_i] >= current_h:

				blocks += 1

				right_i += 1

			else:

				break

		# compute largest possible rectangle

		new_area = blocks * current_h

		# new max_area? -> update

		if new_area > max_area:
			max_area = new_area

	return max_area


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	h = list(map(int, input().rstrip().split()))

	result = largestRectangle(n, h)

	fptr.write(str(result) + '\n')

	fptr.close()