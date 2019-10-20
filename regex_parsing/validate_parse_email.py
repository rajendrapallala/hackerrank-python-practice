# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
rx = r'(?P<name>[a-zA-Z]+) <(?P<email>(?P<username>[a-zA-Z]+[0-9a-zA-Z_.-]*)@(?P<domain>[a-zA-Z]+)\.(?P<extension>[a-zA-Z]{1,3}))>'

n = int(input())

for i in range(n):
    s = input()
    if re.match(rx, s):
        print(s)


