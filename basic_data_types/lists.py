if __name__ == '__main__':
    N = int(input())
    output_list=[]
    input_list = [ input() for i in range(N) ]
    for line in input_list:
        cmd = line.split(" ")[0]
        operands = list(line.split(" ")[1:])
        if cmd.lower() == 'print':
            print(output_list)
        elif cmd.lower() == 'insert':
            output_list.insert(int(operands[0]), int(operands[1]))
        elif cmd.lower() == 'remove':
            output_list.remove(int(operands[0]))
        elif cmd.lower() == 'append':
            output_list.append(int(operands[0]))
        elif cmd.lower() == 'sort':
            output_list.sort()
        elif cmd.lower() == 'reverse':
            output_list.reverse()
        elif cmd.lower() == 'pop':
            output_list.pop()




