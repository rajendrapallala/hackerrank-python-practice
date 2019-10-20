# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
if __name__ == "__main__":
    l1 = [ int(i) for i in input().split()]
    l2 = [ int(i) for i in input().split()]
    print(*list(product(l1,l2)))
