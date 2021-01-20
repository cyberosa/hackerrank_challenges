# Enter your code here. Read input from STDIN. Print output to STDOUT
import os


def getNrPairs(n, step, values):
    seen = dict()
    found = 0
    for i, v in enumerate(values):
        # check if we have the complement already in the hash table
        pair1 = None
        # lower value
        if v > step: 
            pair1 = v - step
        # upper value
        pair2 = v + step
        if pair1 and pair1 in seen.keys():
            found += 1
        if pair2 in seen.keys():
            found += 1
        
        seen[v] = i
    return found

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, step = list(map(int, input().rstrip().split()))

    values = list(map(int, input().rstrip().split()))

    result = getNrPairs(n, step, values)
        
    fptr.write(str(result) + '\n')

    fptr.close()