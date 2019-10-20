# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
x = r'([0-9a-zA-Z])\1+'
a = input() 
m = re.search(x, a)
print(m.group(1) if m else -1)


