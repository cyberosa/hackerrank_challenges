import os
# Enter your code here. Read input from STDIN. Print output to STDOUT

def match_index(ref_pos1, ref_pos2, positions1, i2):
    # find the proper value in s1 for the match
    i = 0
    i1 = positions1[i]
    if len(positions1) > 1:
        # an index higher than the last reference in ref_pos1
        while i+1 < len(positions1) and i1 <= ref_pos1[-1]:
            # the position is not valid
            i += 1
            i1 = positions1[i]
    # check if the value in s1 is already taken in ref_pos1
    if i1 in ref_pos1: 
        return -2    
    # check if the new match is breaking the index order 
    # equals means that the index is taken so we cannot ta  
    if i1 < ref_pos1[-1] or i2 < ref_pos2[-1]:
        return -1
    return i1

def build_ref_dict(s):
    ref_dict = dict()
    for i in range(len(s)):
        char = s[i]
        if char not in ref_dict.keys():
            ref_dict[char] = [i]
        else:
            ref_dict[char].append(i)
    return ref_dict

def initialize_all_lists(positions1, i, char, match_string):
    ref_pos1 = [positions1[0]] # first position found
    ref_pos2 = [i]
    match_string.clear()
    match_string.append(char)
    return ref_pos1, ref_pos2, match_string

def the_child(s1,s2):
    ref_pos1 = None
    ref_pos2 = None
    match_string = list()
    # traverse one string just to have the chars and the positions
    n = len(s1)
    ref_dict1 = build_ref_dict(s1)
    # now traverse the other string checking appearances
    for i in range(n):
        char2 = s2[i]
        if char2 in ref_dict1.keys():
            # match and get position/s of the char in s1
            positions1 = ref_dict1[char2]
            if ref_pos1 is None: # first match, no check
                ref_pos1, ref_pos2, match_string = initialize_all_lists(positions1, i, char2, match_string)
            else:
                mi = match_index(ref_pos1, ref_pos2, positions1, i)
                if mi == -1:
                    # reset all lists
                    ref_pos1, ref_pos2, match_string = initialize_all_lists(positions1, i, char2, match_string)
                elif mi != -2:
                    # all fine, update lists
                    ref_pos1.append(mi)
                    ref_pos2.append(i)
                    match_string.append(char2)
        #print(match_string)
        #print(ref_pos1)
        #print(ref_pos2)
    return len(match_string)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()
    result = the_child(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()