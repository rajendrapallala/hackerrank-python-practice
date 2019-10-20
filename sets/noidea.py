# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    ip =  [int(x) for x in input().split()]
    n,m = ip[0], ip[1]
    array = input().split()
    A = set( input().split() )
    B = set( input().split() )
    happiness = 0
    for x in array[:]:
        if x in A:
            happiness += 1
        if x in B:
            happiness -= 1
    print(happiness)

