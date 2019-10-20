# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
if __name__ == "__main__":
    s, n = input().split()
    c=list()
    for i in range(1,int(n)+1):
        print(*["".join(a) for a in list(combinations(sorted(s),int(i)))], sep='\n')

