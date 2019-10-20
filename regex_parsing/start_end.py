# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = input()
k = re.compile(input())

r = k.search(S)
if r:
    while r:
        print((r.start(), r.end()-1))
        r = k.search(S, r.start()+1)
else:
    print('(-1, -1)')
