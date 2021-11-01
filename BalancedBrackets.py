#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def give_closing_bracket(b1):
	if b1 == "{":
		return "}"
	if b1 == "(":
		return ")"
	if b1 == "[":
		return "]"


def isBalanced(s):
	brackets = []  # list as a stack

	for char in s:
		if len(brackets) == 0:
			brackets.append(char)
		elif char == give_closing_bracket(brackets[-1]):
			# last character was an open bracket
			# and the current one is a close bracket
			brackets.pop()
		else:
			brackets.append(char)

	return "YES" if not brackets else "NO"


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input().strip())

	for t_itr in range(t):
		s = input()

		result = isBalanced(s)

		fptr.write(result + '\n')

	fptr.close()
