# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
'''
lu = []
ll = []
lodd = []
leven = [] 
for c in s[:]:
    if c.isupper():
        lu.append(c)
    if c.islower():
        ll.append(c)
    if c.isdigit() and int(c)%2 == 0:
        leven.append(c)
    if c.isdigit() and int(c)%2 != 0:
        lodd.append(c)

print(*sorted(ll), *sorted(lu), *sorted(lodd), *sorted(leven), sep='' )

'''
print(*sorted(s, key= lambda c: (c.isdigit(),c.isupper(), c.islower(), c.isdigit() and int(c)%2 == 0, c)), sep='')
