#solution adapted from solution by denis631

import os
import sys
from collections import defaultdict 

def frequency(s):
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    return freq

# Complete the reverseShuffleMerge function below.
def getMinimumA(s):
    char_freq = frequency(s)
    used_chars = defaultdict(int)
    # copy of the freq dictionary to update the frequencies as we iterate
    # this dictionary is synchronized with the used_chars one
    remain_chars = dict(char_freq)
    stack = []
    
    def can_use(char):
        # half the freq of the original s string
        # check if you used already all chars
        needed_chars = char_freq[char] // 2
        return (needed_chars - used_chars[char]) > 0
    
    # method to check if we can remove a char from the stack
    # if it has been used enough times
    # Note: the freq in remain_chars is from the whole S string
    # but it is decremented after every visit
    def can_pop(char):
        needed_chars = char_freq[char] // 2
        return used_chars[char] + remain_chars[char] - 1 >= needed_chars
    
    for char in reversed(s):
        if can_use(char):
            # smaller char found that the one on the top of the stack
            # check if we can remove the top char of the stack
            while stack and stack[-1] > char and can_pop(stack[-1]):
                removed_char = stack.pop()
                used_chars[removed_char] -= 1
            
            used_chars[char] += 1
            stack.append(char)
        # it does not matter if we use the char or not in the stack
        # always update the frequency
        remain_chars[char] -= 1
    
    return "".join(stack)


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    minimumA = getMinimumA(s)

    fptr.write(str(minimumA) + '\n')

    fptr.close()
