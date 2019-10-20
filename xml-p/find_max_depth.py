import xml.etree.ElementTree as etree
from collections import deque
maxdepth = 0
def depth(elem, level):
    maxdepth = -1
    # your code goes here
    q = deque()
    while True:
        if elem.getchildren():
            level += 1
            if maxdepth < level :
                maxdepth += 1
            for chd in elem.getiterator():
                q.appendleft((chd,level))
        if len(q) == 0:
            break
        elem, level = q.pop()
    return maxdepth  



if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)