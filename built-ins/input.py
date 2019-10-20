# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = list(map(int, input().split()))
exp = input()
print(eval(exp.replace('x',str(x))) == k)
