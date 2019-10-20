# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    i = int(input())
    M = set(list(map(int, input().split())))
    j = int(input())
    N = set(list(map(int, input().split())))
    u = M.union(N)
    diff = u.difference(M.intersection(N))
    print(*sorted(diff), sep='\n')
