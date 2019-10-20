# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque
if __name__ == "__main__":
    n = int(input())
    d = deque()
    for i in range(n):
        op, _ , val = input().partition(" ")
        #print(d)
        #print(op, val)
        #if op == 'append':
        #    d.append(val)
        #elif op == 'appendleft':
        #    d.appendleft(val)
        #elif op == 'pop':
        #    d.pop()
        #elif op == 'popleft':
        #    d.popleft()
        #else:
        #    eval("d."+op+'('+val+')')
        if val != '':
            getattr(d, op)(val)
        else:
            getattr(d,op)()
    print(*d)


