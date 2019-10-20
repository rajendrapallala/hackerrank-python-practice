# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
if __name__ == "__main__":
    s, n = input().split()
    c=list()
    print(*["".join(a) for a in list(combinations_with_replacement(sorted(s),int(n)))], sep='\n')


