# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
if __name__ == "__main__":
    n,m = input().split()
    n=int(n)
    m=int(m)
    d=defaultdict(list)
    ml = list()
    for i in range(n):
        d[input()].append(i+1)
    for i in range(m):
        ml.append(input())

    for char in ml:
        if char in d.keys():
            print(*d[char])
        else:
            print(-1)


    




