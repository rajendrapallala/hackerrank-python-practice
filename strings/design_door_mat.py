# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    l= input().split(" ")
    n = int(l[0])
    m = int(l[1])
    for i in range(1, n,2):
        print("-"*((m//2)-(i*3//2))+(".|."*i)+ 
              "-"*((m//2)-(i*3//2)) )
    print("WELCOME".center(m,"-"))
    for i in range(n-2, -1,-2):
        print("-"*((m//2)-(i*3//2))+(".|."*i)+ 
              "-"*((m//2)-(i*3//2)) )
    
    


