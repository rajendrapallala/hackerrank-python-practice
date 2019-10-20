# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
if __name__ == "__main__":
    n = int(input())
    d = OrderedDict()
    for i in range(n):
        key, val = input().rsplit(maxsplit=1)
        d[key] = d.setdefault(key,0) + int(val)
    for i1,i2 in d.items():
        print(i1, i2)


