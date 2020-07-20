# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
 
def append(d, value):
    d.append(value)
 
def appendleft(d, value):
    d.appendleft(value)
 
def pop(d,value):
    d.pop()
 
def popleft(d,value):
    d.popleft()

def run_operation(d, str_op):
    options = {'append' : append,
                'appendleft' : appendleft,
                'pop' : pop,
                'popleft' : popleft}
    list_oa = str_op.split()
    op = list_oa[0]
    value = None
    if len(list_oa) == 2:
        value = int(list_oa[1])
    options[op](d, value)

if __name__ == '__main__':
    deck = collections.deque()
    for _ in range(int(input())):
        str_op = input()
        run_operation(deck, str_op)
    # print the contents of deck
    print(*deck) # print values in the same line
    #for v in deck:
    #    print(v)