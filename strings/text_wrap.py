import textwrap

def wrap(string, max_width):
    #return_string=''
    #for i in range(0, len(string), max_width):
    #    return_string=return_string+string[i:i+max_width]+'\n'
    #return return_string
    return '\n'.join(textwrap.wrap(string,max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)