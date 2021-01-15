#!/bin/python3

import os
import sys
from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.root = data
        
    def __repr__(self):
        if self.left and self.right:
            return "("+ str(self.root) + ", "+ str(self.left) +", "+ str(self.right)+ ")"
        if self.right:
            return "("+ str(self.root) + ", None, "+ str(self.right) + ")" 
        if self.left:
            return "("+ str(self.root) + ", "+ str(self.left) + ",None)"
        else:
            return "("+ str(self.root) + ", None, None)"
        
    def __str__(self):
        return str(self.root)

def build_tree(indexes):
    f = lambda x: None if x == -1 else Node(x)
    # children is a list of lists
    children = [list(map(f,x)) for x in indexes]
    #print(children)
    # get the list of nodes by adding all elements in children that are not None
    # Adding all elements to the empty list []
    nodes = {n.root: n for n in filter(None, sum(children, []))}
    nodes[1] = Node(1)
    for idx, child_pair in enumerate(children):
        print(idx)
        print(child_pair)
        # adding each children to the right node, inthe same order as collected
        nodes[idx+1].left = child_pair[0]
        nodes[idx+1].right = child_pair[1]
    return nodes[1]
        
def inorder(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr.root
            curr = curr.right

# Complete the swapNodes function below.
def swapNodes(n, indexes, queries):
    root = build_tree(indexes)
    for k in queries:
        h = 1
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if h % k == 0:
                    node.left, node.right = node.right, node.left
                q += filter(None, (node.left, node.right))
            h += 1
        yield inorder(root)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(n, indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
