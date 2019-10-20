# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
rx = r'^[789]{1}[0-9]{9}$'

n = int(input())
for i in range(n):
    if re.match(rx, input()):
        print('YES')
    else:
        print('NO')
