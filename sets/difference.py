# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()
fs = set (input().split())
n = input()
ss = set (input().split())
print(len(fs.difference(ss)))

