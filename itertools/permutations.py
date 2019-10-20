# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
if __name__ == "__main__":
    lst = input().split()
    string, num = lst[0], lst[1]
    num =  int(num)
    result=["".join(a) for a in sorted(list(permutations(string,num)))]
    for a in result:
        print(a)

