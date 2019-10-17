def minion_game(s):
    # your code goes here
    '''
    stuart_score=0
    kevin_score=0
    kevin_vw=['A','E','I','O','U']
    for idx in range(len(string)):
        char = string[idx]
        if char in kevin_vw:
            kevin_score += 1
            kevin_substring=char
            for kevin_char in string[idx+1:]:
                kevin_substring += kevin_char 
                kevin_score += 1
        else:
            stuart_score += 1
            stuart_substring= char
            for stuart_char in string[idx+1:]:
                stuart_substring += stuart_char 
                stuart_score += 1
    if kevin_score == stuart_score:
        print("Draw")
    elif kevin_score > stuart_score:
        print("Kevin {} ".format(kevin_score))
    else:
        print("Stuart {} ".format(stuart_score))
    '''
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
       if s[i] in vowels:
           kevsc += (len(s)-i)
       else:
           stusc += (len(s)-i)
    if kevsc > stusc:
       print ("Kevin", kevsc)
    elif kevsc < stusc:
       print ("Stuart", stusc)
    else:
       print ("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)