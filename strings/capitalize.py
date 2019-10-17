#!/bin/python3

import math
import os
import random
import re
import sys

# '12abcd'.title() would be 12Abcd but we need 12abcd therefore we need below function
# Complete the solve function below.
def solve(s):
    #return s.title()
    for word in s.split():
        s = s.replace(word, word.capitalize())
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
