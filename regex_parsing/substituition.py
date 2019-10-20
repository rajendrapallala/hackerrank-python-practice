# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def replace_and_or(m):
    x = m.group(0)
    if x == '||':
        return 'or'
    if x == '&&':
        return 'and'
n = int(input())
for l in range(n):
    rx = re.sub('(?<= )(&&|\\|\\|)(?= )', replace_and_or, input())
    print(rx)


