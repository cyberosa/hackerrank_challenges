import os

# Enter your code here. Read input from STDIN. Print output to STDOUT
def count_deletions(s):
    deletes = 0
    next_char = None
    for c in s:
        if next_char is not None and next_char != c:
            deletes += 1
        if c is 'A':
            next_char = 'B'
        else:
            next_char = 'A'
    return deletes
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = count_deletions(s)

        fptr.write(str(result) + '\n')

    fptr.close()