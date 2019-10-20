# Enter your code here. Read input from STDIN. Print output to STDOUT
ss = set(map(int, input().split()))
prt = 'True'
for i in range(int(input())):
    sbs = set(map(int, input().split()))
    if ss.issuperset(sbs) and len(ss) > len(sbs):
        continue
    else:
        prt = 'False'
print(prt)  

