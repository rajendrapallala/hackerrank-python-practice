# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for atr in attrs:
            name, value = atr
            string = "-> " + name + ' >' if value else ''
            print(string, value)


html = "".join([input().strip() for _ in range(int(input()))])
cl = MyHTMLParser()
cl.feed(html)


