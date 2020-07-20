# Enter your code here. Read input from STDIN. Print output to STDOUT
x_val, k = input().split()
k = int(k)
P = input()
P = P.replace('x',x_val)
result = eval(P)
print(result==k)