# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

if __name__ == "__main__":
    m, d, y = [int(x) for x in input().split()]
    dt = datetime.date(y,m,d)
    print(dt.strftime('%A').upper())


