#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

pivot_matrix = []
for col in range(m):
    string = ''
    for row in range(n):
        string += matrix[row][col]
    pivot_matrix.append(string)

final_string = "".join(pivot_matrix)

print_string = re.sub('([a-zA-Z])([^a-zA-Z]+)([a-zA-Z])', '\g<1> \g<3>',final_string)

print(print_string)


