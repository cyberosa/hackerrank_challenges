import os
# Enter your code here. Read input from STDIN. Print output to STDOUT

def purchase_strategy(m,w,p,acc_cand,nr_passes,goal):
    total = acc_cand//p
    if nr_passes == 1 or total == 1:
        # maximize only one purchase type
        if m < w: # only machines
            new_m = m + total
            new_w = w
        else: # only workers
            new_m = m
            new_w = w + total
    else: # hybrid purchase or saving
        if acc_cand >= (goal//2): # we already have the half of the candies
            # then just save the candies
            return m, w, acc_cand
        # split half in machines and half in workers if possible
        if total % 2 != 0:
            # we dont spend all candies
            total = total - 1
        new_m = m + total//2
        new_w = w + total//2
    acc_cand = acc_cand - p*total
    return new_m, new_w, acc_cand

def nr_passes(m,w,p,n):
    acc_cand = 0
    nr_passes = 1
    acc_cand = m*w + acc_cand
    # edge case p = n, the cost is the same as the goal nr of candies
    if (acc_cand < n) and p >= n:
        # nr of iterations with the current production
        return n // (m*w) 
    while (acc_cand < n):
        # purchase or saving strategy 
        m,w,acc_cand = purchase_strategy(m,w,p,acc_cand,nr_passes,n)
        #print("m {} w{} acc_cand{} passes{}".format(m,w,acc_cand,nr_passes))
        # increase nr passes
        nr_passes += 1
        # new production
        acc_cand = m*w + acc_cand
    #print("m {} w{} acc_cand{} passes{}".format(m,w,acc_cand,nr_passes))
    return nr_passes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])
    
    p = int(mwpn[2])

    n = int(mwpn[3])

    result = nr_passes(m,w,p,n)

    fptr.write(str(result) + '\n')

    fptr.close()
