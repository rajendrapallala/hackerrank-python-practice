# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
n,m = input().split()   
nl = []
n = int(n)
m = int(m)
for i in range(n):
    l = list(map(int, input().split()))[1:]
    nl.append(l)
MAX = -1
for comb in product(*nl):
    MAX = max(sum(map(lambda i: i**2, comb))%m, MAX)
print(MAX)
