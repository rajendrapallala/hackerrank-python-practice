# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__== "__main__":
    nt = int(input())
    for i in range(nt):
        a, b = input().split()
        try:
            print (int(a)//int(b))
        except (ValueError, ZeroDivisionError) as e:
            print("Error Code:", e)
