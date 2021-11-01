#!/bin/python3
# https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
import math
import os
import random
import re
import sys


#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
	contests_0 = []
	contests_1 = []
	num_ones = 0
	# divide between important and not important
	for contest in contests:
		# print(contest[1])
		if contest[1] == 1:
			contests_1.append(contest[0])
			num_ones += 1
		else:
			contests_0.append(contest[0])

	zero_sum = sum(contests_0)
	# print(f"zero sum {zero_sum}")
	if k >= num_ones:
		print("all")
		ones_sum = sum(contests_1)
		# we can loose all important
		return (ones_sum + zero_sum)

	force_win = num_ones - k
	# print(f"force win {force_win}")
	contests_1.sort()
	# print(contests_1)
	win_ones = sum(contests_1[:force_win])
	ones_sum = sum(contests_1[force_win:])
	print(f"ones sum {ones_sum}")
	print(f"win ones {win_ones}")
	return (zero_sum + ones_sum - win_ones)


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	first_multiple_input = input().rstrip().split()

	n = int(first_multiple_input[0])

	k = int(first_multiple_input[1])

	contests = []

	for _ in range(n):
		contests.append(list(map(int, input().rstrip().split())))

	result = luckBalance(k, contests)

	fptr.write(str(result) + '\n')

	fptr.close()
