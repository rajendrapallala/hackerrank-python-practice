# Enter your code here. Read input from STDIN. Print output to STDOUT

ns, nosub =  tuple(map(int, input().split()))
sublst=[]
for i in range(nosub):
    sublst.append(list(map(float, input().split())))

stdlst = zip(*sublst)
for std in stdlst:
    print(sum(std)/len(std))


