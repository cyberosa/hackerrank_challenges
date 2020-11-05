import os
# Enter your code here. Read input from STDIN. Print output to STDOUT

# return the reference frequency
def update_freq_count(freq_count, freq):
    print("freq_count update {}".format(freq))
    if freq not in freq_count.keys():
        freq_count[freq] = 1
    else:
        # increase the count for that freq
        freq_count[freq] += 1
    if freq > 1:
        # decrease the count of the prev freq
        if freq-1 in freq_count.keys(): 
            freq_count[freq-1] -= 1
            if freq_count[freq - 1] == 0: 
                del freq_count[freq-1]
    return freq_count

def is_valid(s):
    ref_freq = 0
    dict_freq = dict()
    freq_count = dict()
    
    for c in s:
        print(c)
        if c not in dict_freq.keys():
            # new character
            dict_freq[c] = 1
            print("dict_freq {}".format(dict_freq[c]))
            freq_count = update_freq_count(freq_count, 1)
        else:
            # update the freq for that character
            dict_freq[c] += 1
            freq_count = update_freq_count(freq_count, dict_freq[c])
        print(freq_count)
        if dict_freq[c] in freq_count.keys() and freq_count[dict_freq[c]] > ref_freq:
            ref_freq = dict_freq[c]
    
    # studying all cases
    nr_entries = 0
    print("ref freq {}".format(ref_freq))
    if len(freq_count.keys()) == 1: return 'YES'   
    if len(freq_count.keys()) > 2: return 'NO'
    for freq in freq_count.keys():
        if freq == ref_freq:
            continue
        # jump between the seen frequencies greater than 1
        if abs(ref_freq - freq) > 1:
            return 'NO'
        
        # not the reference group
        if freq != ref_freq:
            print("freq {}".format(freq))
            print("count freq {}".format(freq_count[freq]))
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