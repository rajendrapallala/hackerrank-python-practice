# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
if __name__ == "__main__":
    n = input()
    print(*[(len(list(g)),int(k)) for k,g in groupby(n)])
