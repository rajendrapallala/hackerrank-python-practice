# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == "__main__":
    ab = int(input())
    bc = int(input())

    arccos = str(round(math.degrees(math.atan2(ab,bc))))+chr(176)

    print(arccos)

