#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the riddle function below.
def riddle(n, arr):
	if n == 1:
		return max(arr)

	# take the largest window size for a sample
	# to be the minimum
	max_window = dict()
	for i, v in enumerate(arr):
		window_size = 1
		# check left boundary
		left_i = i - 1
		while left_i >= 0:
			if arr[left_i] >= v:
				window_size += 1
				left_i -= 1
			else:
				break
		# check right boundary
		right_i = i + 1
		while right_i < n:
			if arr[right_i] >= v:
				window_size += 1
				right_i += 1
			else:
				break
		max_window[v] = window_size

	# print(max_window)
	# Iterating over values
	size_values = dict()
	for v, size in max_window.items():
		sizes = size_values.keys()
		if size in sizes:  # we have a prev value
			prev = size_values[size]
			size_values[size] = max(v, prev)
		else:
			size_values[size] = v
	# print(size_values)
	prev_value = size_values[n]
	# print(f"prev_value{prev_value}")
	sizes = size_values.keys()
	final_list = []
	final_list.append(prev_value)
	for i in range(n - 1, 0, -1):
		if i not in sizes:
			# repeat prev value
			final_list.append(prev_value)
		else:
			final_list.append(size_values[i])
		prev_value = final_list[-1]  # last value
	return reversed(final_list)


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	res = riddle(n, arr)

	fptr.write(' '.join(map(str, res)))
	fptr.write('\n')

	fptr.close()
