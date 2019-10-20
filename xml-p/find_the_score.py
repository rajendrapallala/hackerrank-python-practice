import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    return len(node.attrib) + sum(get_attr_number(e) for e in node.getchildren())


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))