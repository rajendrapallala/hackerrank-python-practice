if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    l=[]
    mx=max(arr)
    for i in arr:
        if i != mx:
            l.append(i)
    l.sort(reverse=True)
    print(l[0])
