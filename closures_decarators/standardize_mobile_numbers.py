
def wrapper(f):
    def fun(l):
        # complete the function
        f("+91 "+ s[-10:-5] + " " + s[-5:] for s in l[:])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


