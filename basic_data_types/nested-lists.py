
def return_score(item):
    return item[1], item[0]
if __name__ == '__main__':
    nl=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nl.append([name,score])
    nl.sort(key=return_score, reverse=False)
    least, second_least = nl[0][1], nl[-1][1]
    for item in nl:
        if item[1] <= least:
           least = item[1]
        if item[1] > least and item[1] < second_least:
            second_least = item[1]
    for item in nl:
        if item[1] == second_least:
           print(item[0])


