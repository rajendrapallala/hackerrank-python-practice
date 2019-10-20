# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
xx='^[-+]?[0-9]*\.[0-9]+$'
T = int(input())
for i in range(T):
    a = input()
    if re.match(xx, a) and float(a):
        print('True')
    else:
        print('False')
