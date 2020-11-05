import os
# Enter your code here. Read input from STDIN. Print output to STDOUT

# return the reference frequency
def update_freq_count(freq_count, freq, ref_freq):
    if freq not in freq_count.keys():
        freq_count[freq] = 1
    else:
        # increase the count for that freq
        freq_count[freq] += 1
        if freq > 1:
            # decrease the count of the prev freq
            freq_count[freq-1] -= 1

    if ref_freq >0 and freq_count[freq] > freq_count[ref_freq]:
        return freq_count, freq
    return freq_count, ref_freq

def is_valid(s):
    ref_freq = 0
    dict_freq = dict()
    freq_count = dict()
    
    for c in s:
        if c not in dict_freq.keys():
            # new character
            dict_freq[c] = 1
            freq_count, ref_freq = update_freq_count(freq_count, 1, ref_freq)
        else:
            # update the freq for that character
            dict_freq[c] += 1
            freq_count, ref_freq = update_freq_count(freq_count, dict_freq[c], ref_freq)
    
    # studying all cases
    nr_entries = 0
    prev_freq = 0
    for freq in freq_count.keys():
        if freq_count[freq] > 0:
            nr_entries += 1
        else:
            continue
        
        # more than three types of frequencies
        if nr_entries > 2:
            return 'NO'
        
        # jump between the seen frequencies greater than 1
        if abs(ref_freq - freq) > 1:
            return 'NO'
        
        # not the reference group
        if freq != ref_freq:
            # or decreasing we reach the ref_freq
            if (freq_count[freq]*freq)-1 == ref_freq:
                return 'YES'
            # or if the extra group is only once
            if (freq_count[freq]*freq)-1 == 0:
                return 'YES'
        # if no matching of any previous
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = is_valid(s)

    fptr.write(str(result) + '\n')

    fptr.close()