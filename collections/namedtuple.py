# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
if __name__ == "__main__":
    nostds= int(input())
    fields=input().split()
    cols=namedtuple("cols",",".join(fields))
    l = list()
    s=0
    for i in range(nostds):
        try:
            line = str(input()).strip('\n').split()
        except EOFError:
            pass
        a=cols(*line)
        s += int(a.MARKS)
    print(s/nostds)


