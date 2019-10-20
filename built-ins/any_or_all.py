# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nl = list(map(int,input().split()))
print( all(map(lambda x:x>0, nl)) and any( map(lambda x: str(x) == str(x)[::-1] ,nl) ) )
