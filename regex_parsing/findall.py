# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
#reg = r"(?:[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]+)([aeiouAEIOU]{2,})(?:[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]+)"
reg = r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]+?"
s = input()
l = re.findall(reg, s)
if len(l) == 0:
    print('-1')
else:
    for grp in l[:]:
        print(grp)

