n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    op, _, oprnd = input().partition(" ")
    if oprnd:
        oprnd =  int(oprnd)
        getattr(s, op)(oprnd)
    else:
        getattr(s, op)()
print(sum(s))
