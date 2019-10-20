# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    nt = int(input())
    for i in range(nt):
        restr = input()
        try:
            re.compile(restr)
        except Exception:
            print('False')
        else:
            print('True')

