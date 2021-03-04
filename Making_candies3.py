import os
import sys
import math

def nr_passes(m, w, p, n):
    candy = 0
    invest = 0
    spend = sys.maxsize
    while candy < n:
        passes = (p - candy) // (m * w)
        if passes <= 0:
			# we have more candies than the cost p
			# total power is the sum of workers plus machines 
			# plus the extra ones we can purchase with the nr of candies(candy)
            mw = (candy // p) + m + w
			# we want to maximize or the nr of workers or the nr of machines
            half = math.ceil(mw / 2)
            if m > w:
				# if the nr of machines is big enough
				# we dont need to increase it
                m = max(m, half)
                w = mw - m
            else:
                w = max(w, half)
                m = mw - w
            candy %= p # update the nr of candies after the purchase
            passes = 1
		# here we are using the production to increase the nr of candies
		# and reach the cost p
        candy += passes * m * w
        invest += passes
		# we compute the nr of passes we need to add to invest
		# with the current production, to reach the goal n
        spend = min(spend, invest + math.ceil((n - candy) / (m * w)))
    return min(invest, spend)
	
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
