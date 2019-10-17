def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    l =[]
    if size == 0:
        return 
    if size == 1:
        print(alpha[0])
        return
    for i in range(size):
        strg = alpha[i:size]
        l.append('-'.join(strg[::-1]+strg[1:]).center(size+3*(size-1),'-'))
    print('\n'.join(l[:0:-1]),'\n'.join(l),sep='\n')

def print_rangoli_noteligent(size):
    # your code goes here
    alphab = 'abcdefghijklmnopqrstuvwxyz'
    cnt = 0
    line_len = size + (size-1) * 3
    for i in range(size):
        cntr=''
        if cnt == 0:
            cntr = alphab[size-1] + '-'
        else:
            for j in range(cnt,-1,-1):
                if j == cnt:
                   cntr = alphab[size-j-1] + '-'
                else:
                    cntr = alphab[size-j-1] + '-' + cntr + alphab[size-j-1] + '-'
        cnt = cnt + 1
        print(cntr.strip('-').center(line_len,'-'))
    cnt = size
    for i in range(size-2,-1,-1):
        cntr=''
        if cnt == 1:
            cntr = alphab[size-cnt] + '-'
        else:
            for j in range(cnt-1):
                if j == 0:
                   cntr = alphab[size-cnt+1] + '-'
                else:
                    cntr = alphab[size-cnt+j+1] + '-' + cntr + alphab[size-cnt+j+1] + '-'
        cnt = cnt - 1
        print(cntr.strip('-').center(line_len,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
