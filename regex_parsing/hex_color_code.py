# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
rx = r'(?<!^)(#(?:[0-9a-fA-F]{3}){1,2})'

N=int(input())

for i in range(N):
    m = re.findall(rx, input())
    if m:
        print('\n'.join(m))
    


