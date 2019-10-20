cube = lambda x: pow(x,3) # complete the lambda function 

def fibonacci(n):
    a ,b = 0 ,1
    rl = []
    for _ in range(n):
        rl.append(a)  
        a, b = b, a+b
    return rl
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))