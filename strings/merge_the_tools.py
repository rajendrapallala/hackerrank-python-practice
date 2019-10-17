'''
Sample Input:
AABCAAADA
3   

Sample Output:
AB
CA
AD

Explanation:

Split string in groups with lenght 3 and print occurance of non-distinct char from groups

'''
def merge_the_tools(string, k):
    # your code goes here
    for idx in range(0, len(string), k):
        seg = string[idx:idx+k]
        print_seg=''
        for c in seg:
            if c not in print_seg:
                print_seg += c
        print(print_seg)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)