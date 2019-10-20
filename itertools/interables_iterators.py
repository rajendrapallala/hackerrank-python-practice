# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = int(input())
l = input().split()
cbn = int(input())
cmbn = list(combinations(l,cbn))
tot = len(cmbn)
aprsn = len(list(filter(lambda x: 'a' in x, cmbn)))
print('{:.3}'.format(aprsn/tot))
