# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
if __name__ == "__main__":
    z = complex(input())
    r=abs(cmath.sqrt(pow(z.real,2) + pow(z.imag,2)))
    pi = abs(cmath.sqrt(pow(z.real,2) - pow(r,2)))
    print(r)
    print(cmath.phase(z))
