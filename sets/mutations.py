# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
fs = set(map(int, input().split()))
l = int(input())
for i in range(0,l*2,2):
    op, _ = input().split()
    s = set(map(int, input().split()))
    getattr(fs, op)(s)
print(sum(fs))


