# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
#rx = r'(?!([0-9a-zA-Z]{1})\1+)(?=[A-Z]{2}[0-9]{3})([0-9a-zA-Z]{10})'
rx = r'([0-9a-zA-Z]{10})'
sr1 = r'(.).*\1'
sr2 = '.*(?=.*\d.*\d.*\d.*)'
sr3 = '.*(?=.*[A-Z].*[A-Z].*)'
ip = [input().strip() for _ in range(int(input())) ]

for string in ip[:]:
    if len(string) == 10 and re.match(rx, string):
        if not re.search(sr1, string) and re.search(sr2, string) and re.search(sr3,string):
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
