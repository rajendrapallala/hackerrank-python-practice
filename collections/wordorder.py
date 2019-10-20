# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
if __name__ == "__main__":
    n = int(input())
    l = list()
    for i in range(n):
        l.append(input())
    c = Counter(l)
    print(len(c))
    print(*c.values())


