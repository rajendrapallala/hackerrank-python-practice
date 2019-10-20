# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for at in attrs:
            print('->', at[0], '>', at[1])

    def handle_endtag(self, tag):
        print('End   :', tag)
    
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for at in attrs:
            print('->', at[0], '>', at[1])
'''
N = int(input())
t = []
for i in range(N):
    t.append(input().strip())
parser = MyHTMLParser()
parser.feed("t".join(t))
'''
parser = MyHTMLParser()
parser.feed(''.join([input().strip() for _ in range(int(input()))]))



