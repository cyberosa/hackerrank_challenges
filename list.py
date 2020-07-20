def append(d, position, value):
    d.append(value)
 
def insert(d, position, value):
    d.insert(position, value)
 
def pop(d, position, value):
    d.pop()
 
def remove(d, position, value):
    d.remove(value)

def print_l(d, position, value):
    print(d)

def sort(d, position, value):
    d.sort()

def reverse(d, position, value):
    d.reverse()

def run_operation(l, str_op):
    options = {'append' : append,
                'insert' : insert,
                'pop' : pop,
                'remove' : remove,
                'print' : print_l,
                'sort':sort,
                'reverse':reverse}
    list_oa = str_op.split()
    op = list_oa[0]
    value = None
    position = None
    if len(list_oa) == 2:
        value = int(list_oa[1])
    elif len(list_oa) == 3:
        value = int(list_oa[2])
        position = int(list_oa[1])
    options[op](l, position, value)

if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        run_operation(l, str(input()))
