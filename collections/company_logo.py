#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict

class OrderedCounter(OrderedDict, Counter):
    pass

if __name__ == '__main__':
    s = input()
    #c = Counter(s)
    #print(c)
    #print(c.most_common())
    #for item in sorted(c.most_common(), key = lambda x: (-x[1],x[0]))[0:3] :
    #    print(*item)
    #for letter, counts in sorted(Counter(raw_input()).most_common(),key = lambda x:(-x[1],x[0]))[:3]:
    #print letter, counts
    [print(*c) for c in OrderedCounter(['a','b','a']).most_common(3)]
#from collections import Counter, OrderedDict

#class OrderedCounter(Counter, OrderedDict):
#    pass
