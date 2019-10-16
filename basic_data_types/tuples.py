if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    print(hash(tuple(integer_list)))
'''
Hash is built in function
Return the hash value of the object (if it has one). 
Hash values are integers. 
They are used to quickly compare dictionary keys during a dictionary lookup. 
Numeric values that compare equal have the same hash value 
(even if they are of different types, as is the case for 1 and 1.0).
'''