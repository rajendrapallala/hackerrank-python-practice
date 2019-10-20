# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == "__main__":
    nh = int(input())
    d = Counter(input().split())
    nc = int(input())
    tm = 0
    for i in range(1 ,nc+1):
        size, price = input().split()
        if d[size] > 0:
            tm += int(price)
            d[size] -= 1
    print(tm)





