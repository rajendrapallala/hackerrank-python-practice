# Enter your code here. Read input from STDIN. Print output to STDOUT
nt = int (input())
for t in range(0,nt*4,4):
    an = int(input())
    a = set(map(int, input().split()))
    bn = int(input())
    b = set(map(int, input().split()))
    if a.issubset(b):
        print("True")
    else:
        print("False")


