# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
fs = set(input().split())
m = int(input())
ss = set(input().split())
print (len(fs.union(ss)))
