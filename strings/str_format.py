def print_formatted(number):
    # below W line captures the len of binary value
    # this w is used to equally space different formats
    w = len("{:b}".format(number))
    print("w is ", w)
    for i in range(1,number+1):
        print("{num:{w}d} {num:{w}o} {num:{w}X} {num:{w}b}".format(num=i,w=w))


if __name__ == '__main__':
    #n = int(input())
    n = 10
    print_formatted(n)